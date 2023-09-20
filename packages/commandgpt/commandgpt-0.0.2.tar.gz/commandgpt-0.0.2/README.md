# Command GPT

A simple command-line utility to interact with OpenAI's API and retrieve shell suggestions. By default, predefined system and user messages are used to facilitate the interaction. However, flags are available to allow customization of these messages per request.

## Prerequisites

1. **Python 3**
2. **An OpenAI API Key**

## Install

```bash
pip install commandgpt
```

## Usage

By default, the system and user messages are set as:
- System: "You are a Linux based OS system administrator. Answer as briefly as possible."
- User: "Answer only with command without any background explanation and clarification. Provide the most comprehensive and accurate solution."

You can use the utility without specifying these defaults:

```bash
$ gpt "Your query here"
```

However, if you wish to customize the system or user messages:

```bash
$ gpt "Your query here" --system "Your custom system message" --user "Your custom user prefix"
```

**Example**:

```bash
$ gpt "How do I check disk space?"
'df -h'

```

```bash
$ gpt "How can I see all running processes?"
'ps aux'
```
```bash
$ gpt "How do I find my machine's IP address?"
'ip addr show'
```

## Configuration

On the first run, Command GPT will create a configuration file named `.openai_config` in your home directory. This file will store the OpenAI API key and model to facilitate future interactions without the need to repeatedly input those details.

It's recommended to check the file's permissions and ensure it's protected, as it contains sensitive information. Always be careful about where and how you store your API keys.

## Output Safety Warning

The output from Command GPT is not escaped or quoted by default. This means that special characters or command structures in the output can have direct consequences if executed in a shell or scripting environment.

Using the raw output in scripts or as part of piped commands can be hazardous. I strongly advise against directly integrating the output of Command GPT into another command, script, or pipeline without meticulously reviewing and understanding its implications.

Before utilizing any output, please ensure you're fully aware of its content and potential side effects. 

## License

[MIT](https://choosealicense.com/licenses/mit/)