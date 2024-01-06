import json
import os
from penelopa_dialog import PenelopaDialog
from gptintegration import GPTIntegration
from taskfeasibilityanalyzer import TaskFeasibilityAnalyzer

class ClarifyingQuestionsGenerator:
    def __init__(self, task, instruction, gpt_api_key, directory=os.getcwd(), max_iterations=5, model="gpt-3.5-turbo", temperature=0.7, max_tokens=1500, top_p=1.0, frequency_penalty=0.0, presence_penalty=0.0):
        self.task = task
        self.instruction = instruction
        self.directory = directory
        self.gpt_integration = GPTIntegration(gpt_api_key, model=model, temperature=temperature, max_tokens=max_tokens, top_p=top_p, frequency_penalty=frequency_penalty, presence_penalty=presence_penalty)
        self.max_iterations = max_iterations
        self.questions = []
        self.gpt_api_key = gpt_api_key

    def generate_questions(self):
        system_message = "Generate a set of clarifying questions along with multiple choice answers for each question. The questions should help clarify the details and requirements of a given task. Ensure the output is in the specified JSON format."

        user_message = f"""
        Given the task description: '{self.task}' and instructions: '{self.instruction}', generate a list of clarifying questions along with options for possible answers. The response should be in JSON format, where each question is an object with "question" and "answers" fields.
        Example format:
        [
          {{
            "question": "What is the primary goal of the task?",
            "answers": ["Optimizing performance", "Improving security", "Refactoring code"]
          }}
        ]
        """

        response = self.gpt_integration.query_gpt(system_message, user_message)
        questions_json = response.choices[0].message.content.strip()

        try:
            self.questions = json.loads(questions_json)
            return self.questions
        except json.JSONDecodeError:
            raise ValueError("Received invalid JSON response from GPT-3")

    def ask_questions(self, questions):
        dialog_responses = []
        for idx, question_data in enumerate(questions, 1):
            question_text = question_data['question']
            answers = question_data['answers']

            # Keep asking the current question until a valid response is received
            while True:
                print(f"\nQuestion {idx}: {question_text}")
                for ans_idx, answer in enumerate(answers, 1):
                    print(f" ({ans_idx}) {answer}")

                print("Please choose the number (1 to {}): ".format(len(answers)), end="")

                # Initialize PenelopaDialog to capture user input
                dialog = PenelopaDialog("")
                response = dialog.run()

                # Check if the response is a valid number within the range of answer options
                if response.isdigit() and 1 <= int(response) <= len(answers):
                    # If valid, append response and break the while loop
                    dialog_responses.append(int(response))  # Store as int for easier handling later
                    break
                else:
                    # If not valid, inform the user and repeat the question
                    print("Invalid input. Please enter a number corresponding to the answer options.")

        return dialog_responses

    def refine_task(self, answers):
        # System message instructing the model to create a concrete and detailed task description
        system_message = "Refine the task description based on the user's answers to the clarifying questions. Ensure the refined task is clear, detailed, and actionable, incorporating all specific details provided by the user."

        # Structuring the user message to include both the original task and the user's answers
        user_message = f"Original task: {self.task}\n\n"
        user_message += "Details provided by the user based on clarifying questions:\n"
        for q, a in zip(self.questions, answers):
            user_message += f" - For the question '{q['question']}', the user selected: '{q['answers'][int(a) - 1]}'\n"  # Adjusting for 0-based indexing

        # Query GPT-3 with both the system and user messages
        response = self.gpt_integration.query_gpt(system_message, user_message)
        refined_task = response.choices[0].message.content.strip()

        return refined_task

    def analyze_feasibility(self, refined_task):
        analyzer = TaskFeasibilityAnalyzer(self.directory, self.gpt_api_key)
        probability = analyzer.analyze_task(refined_task)
        print("The probability that the task can be completed successfully is", probability)
        return probability

    def run(self):
        for iteration in range(self.max_iterations):
            questions = self.generate_questions()
            answers = self.ask_questions(questions)
            refined_task = self.refine_task(answers)
            feasibility = self.analyze_feasibility(refined_task)

            if feasibility > 0.5:
                return refined_task

            self.task = refined_task

        return refined_task
