from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="commandgpt",
    version="0.0.2",
    packages=find_packages(),
    install_requires=[
        "openai",
    ],
    entry_points={
        "console_scripts": [
            "gpt=commandgpt:main",
        ],
    },
    author="Michael Knap",
    description="A CLI utility for interacting with OpenAI GPT.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/michaelknap/commandgpt",
    python_requires=">=3.6",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
    ],
)
