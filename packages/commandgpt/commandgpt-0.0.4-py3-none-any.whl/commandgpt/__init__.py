#!/usr/bin/env python3
import os
import openai
import argparse
import configparser
from pathlib import Path

__VERSION__ = "0.0.4"

# Constants
DEFAULT_MODEL = "gpt-3.5-turbo"
CONFIG_PATH = Path.home() / ".openai_config"


class OpenAIChat:
    """
    A class to interact with the OpenAI API for chat functionalities.

    Instance Attributes:
        api_key (str): The API key to access OpenAI services.
        model (str): The model to use for the chat.
    """

    def __init__(self):
        """
        Initializes the OpenAIChat instance with the OpenAI API key and the desired model.

        """
        self.__initialize_config()
        openai.api_key = self.api_key

    def chat(self, system_msg, user_prefix, query):
        """
        Sends a message to the OpenAI API and retrieves the response.

        Parameters:
            system_msg (str): System message to set the context for GPT.
            user_prefix (str): Prefix for the user message.
            query (str): The user's query.

        Returns:
            str: The response from the OpenAI API.
        """
        user_msg = f"{user_prefix} {query}"
        try:
            response = openai.ChatCompletion.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": system_msg},
                    {"role": "user", "content": user_msg},
                ],
            )
            return response["choices"][0]["message"]["content"]

        except openai.error.RateLimitError:
            return "You exceeded your current quota. Please check your plan and billing details."

        except openai.error.OpenAIError as e:
            return f"OpenAI API Error: {e}"

        except Exception as e:
            return f"An unexpected error occurred: {e}"

    def __initialize_config(self):
        """Method to initialize or read the API configuration."""
        if CONFIG_PATH.exists():
            config = configparser.ConfigParser()
            config.read(CONFIG_PATH)
            self.api_key = config["DEFAULT"].get("OPENAI_API_KEY", "").strip()
            if not self.api_key:
                raise ValueError("The API key in the config file is empty.")
            self.model = config["DEFAULT"].get("OPENAI_MODEL", DEFAULT_MODEL).strip()
        else:
            self.api_key = input("Enter your OpenAI API key: ").strip()
            while not self.api_key:
                print("Please provide a valid API key.")
                self.api_key = input("Enter your OpenAI API key: ").strip()

            print("Choose a model:")
            print("1: gpt-3.5-turbo (default)")
            print("2: gpt-4")
            choice = input("Choice: ").strip()

            if choice not in ["1", "2", ""]:
                print("Invalid choice. Using the default model.")
                choice = "1"

            self.model = DEFAULT_MODEL if choice == "1" or not choice else "gpt-4"

            # Save the choices to the config file
            config = configparser.ConfigParser()
            config["DEFAULT"] = {
                "OPENAI_API_KEY": self.api_key,
                "OPENAI_MODEL": self.model,
            }
            with CONFIG_PATH.open("w") as config_file:
                config.write(config_file)
            os.chmod(CONFIG_PATH, 0o600)


def main():
    """
    The main function to interact with OpenAI GPT from the command line.
    Parses command-line arguments, interacts with the OpenAI API, and prints the response.
    """
    parser = argparse.ArgumentParser(description="Interact with OpenAI GPT.")

    parser.add_argument("query", type=str, help="Your question or query.")

    parser.add_argument(
        "-s",
        "--system",
        type=str,
        default="You are a Linux based system administrator.",
        help="System message for GPT.",
    )

    parser.add_argument(
        "-u",
        "--user",
        type=str,
        default="Answer only with a command without any explanation and clarification. Provide the most comprehensive and accurate solution.",
        help="Prefix for user message.",
    )
    parser.add_argument(
        "-v",
        "--version",
        action="version",
        version=f"%(prog)s {__VERSION__}",
        help="Show the version number and exit.",
    )
    args = parser.parse_args()

    try:
        chatbot = OpenAIChat()
        response = chatbot.chat(args.system, args.user, args.query)
        print(response)
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
