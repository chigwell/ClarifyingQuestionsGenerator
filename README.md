[![PyPI version](https://badge.fury.io/py/clarifyquestgen.svg)](https://badge.fury.io/py/clarifyquestgen)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Downloads](https://static.pepy.tech/badge/clarifyquestgen)](https://pepy.tech/project/clarifyquestgen)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-blue)](https://www.linkedin.com/in/eugene-evstafev-716669181/)

# ClarifyingQuestionsGenerator

`ClarifyingQuestionsGenerator` is a Python package designed to refine task descriptions through an iterative process of asking clarifying questions. It uses GPT models from OpenAI to generate questions and refine tasks, streamlining the process of task clarification and ensuring tasks are well-understood and actionable.

## Installation

To install `ClarifyingQuestionsGenerator`, you can use pip:

```bash
pip install clarifyquestgen
```

## Usage

### As a Python Module

You can use `ClarifyingQuestionsGenerator` as a module in your Python scripts.

Example:

```python
from clarifyquestgen import ClarifyingQuestionsGenerator

# Initialize the generator with a task, instruction, and your OpenAI API key
clarifier = ClarifyingQuestionsGenerator(
    task="Describe the task here",
    instruction="Additional instructions here",
    gpt_api_key='your-openai-api-key'
)

# Run the generator to refine your task
refined_task = clarifier.run()
print("Refined Task Description:")
print(refined_task)
```

### Customizing Your Generator

You can customize the behavior of `ClarifyingQuestionsGenerator` by adjusting the initialization parameters, such as the model, temperature, max tokens, etc., to fit the specific needs of your application or to tweak the behavior of the GPT model.

## Output Example

When you run `ClarifyingQuestionsGenerator`, it iteratively asks questions, refines the task, and analyzes its feasibility until a satisfactory level of clarity and feasibility is reached. Here is an example interaction:

```
Question 1: What specific parts of the database schema need to be refactored?
...user chooses an answer...
Question 2: What is the expected format or style of the comments?
...user chooses an answer...
...
Refined Task Description:
Refined task: Add comments to specific sections or functions within two code files. Follow the expected format for comments and adhere to specific guidelines or conventions provided.
```

## Contributing

Contributions, issues, and feature requests are welcome! Feel free to check [issues page](https://github.com/yourusername/ClarifyingQuestionsGenerator/issues).

## License

[MIT](https://choosealicense.com/licenses/mit/)
