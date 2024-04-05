# OpenAI_Chatbot_Integration_With_Slack
This project is a Slack bot designed to generate answer based on user input. It utilizes the OpenAI API for natural language processing and conversation generation.

## Features

- Generates job proposals based on provided job descriptions.
- Handles irrelevant messages by prompting users to provide proper information.
- Ensures that the generated proposals contain only relevant project details.
- Outputs information in a simple and easy-to-understand format.
- Utilizes natural language processing to generate human-like responses.

## Dependencies

- Python 3.7+
- Slack Bolt
- Slack Bolt Socket Mode Adapter
- Langchain
- Langchain OpenAI
- dotenv

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your_username/your_repo.git   ```

## Install dependencies:

   ```bash
pip install -r requirements.txt
 ```

Create a .env file in the root directory and add your Slack bot token:
- env
- Copy code
- SLACK_BOT_TOKEN=your_slack_bot_token
- 
## Usage
- Run the Slack bot application:

```bash
python app.py
```
Interact with the bot in your Slack workspace by mentioning its name and providing job descriptions.

## Configuration

Modify the prompt_template1 variable in app.py to customize the job proposal template according to your requirements.
Adjust the temperature and model_name parameters in the ChatOpenAI initialization to fine-tune the natural language processing model.
Contributing
Contributions are welcome! Please feel free to submit issues or pull requests.

## License
This project is licensed under the MIT License - see the LICENSE file for details.







