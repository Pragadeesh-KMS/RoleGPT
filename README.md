# Advanced Chatbot

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
  - [Configuration](#configuration)
  - [Starting a Conversation](#starting-a-conversation)
- [Demo](#demo)
- [Dependencies](#dependencies)
- [Error Handling](#error-handling)
- [Contributing](#contributing)
- [Testing](#testing)
- [Contact Information](#contact-information)

## Overview

The **Advanced Chatbot** is a Python-based conversational AI tool that allows users to engage in dynamic conversations with fictional characters. It utilizes the OpenAI GPT-3.5 model to provide realistic responses in the persona of a chosen fictional character. Users can specify the character they want to interact with, and the chatbot will adopt that character's identity and respond accordingly.

## Features

- Seamless integration with the OpenAI GPT-3.5 model for natural language processing.
- User-friendly interface for initiating conversations with fictional characters.
- Dynamic persona shifting to match the chosen character's identity.
- The chatbot maintains a sequence-based memory for context-aware responses.
- Professional and concise responses, staying in character without providing information about other fictional characters.

## Getting Started

### Prerequisites

Before using the **Advanced Chatbot**, ensure you have the following prerequisites installed:

- Python 3.6 or higher
- OpenAI Python library (install using `pip install openai`)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Pragadeesh-KMS/advanced-chatbot.git
   ```

2. Navigate to the project directory:

   ```bash
   cd advanced-chatbot
   ```

### Configuration

3. Open the `config.py` file and replace `"YOUR_API_KEY_HERE"` with your OpenAI GPT-3.5 API key.

4. Save the changes to the `config.py` file.

## Usage

### Starting a Conversation

1. Create an instance of the `AdvancedChatbot` class with your desired prompt and API key:

   ```python
   prompt = """PROMPT SPECIFIED IN THE MAIN PYTHON FILE"""
   api_key = "your-api-key-here"
   
   chatbot = AdvancedChatbot(prompt, api_key)
   ```

2. Start a conversation with the chatbot by entering user input. The chatbot will respond in character:

   ```python
   while True:
       user_input = input("user : ")
       if user_input.lower() == "exit":
           break
       response = chatbot.generate_response(user_input)
       print("bot:", response)
   ```

3. To exit the conversation, simply type "exit."

## Demo

For a visual demonstration of how to use the Advanced Chatbot, watch our [demo video](link-to-demo-video).

## Dependencies

To set up the required dependencies, run the following command:

```bash
pip install -r requirements.txt
```

## Error Handling

If you encounter any issues, please ensure your API key in `config.py` is correct. For further assistance, refer to our [troubleshooting guide](link-to-troubleshooting).

## Contributing

We welcome contributions! To contribute to the project, please follow our [contribution guidelines](link-to-contribution-guidelines).

## Testing

To run tests for the project, execute the following command:

```bash
python tests.py
```


## Contact Information

For inquiries or support, contact us at kmspragadeesh6000@gmail.com.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- The **Advanced Chatbot** utilizes the OpenAI GPT-3.5 model for its natural language processing capabilities.
