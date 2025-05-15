from setuptools import setup, find_packages

setup(
    name='clarifyquestgen',
    version='2025.5.151003',
    author='Eugene Evstafev',
    author_email='chigwel@gmail.com',
    description='Clarifying Questions Generator for task refinement',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/chigwell/ClarifyingQuestionsGenerator',
    packages=find_packages(),
    install_requires=[
        'penelopa-dialog',
        'gptintegration',
        'TaskFeasibilityAnalyzer'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
    python_requires='>=3.6',
)
