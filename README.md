# ChatGPT for SlackBot

## How to Use
1. Clone this repository.
    ```shell
    $ git clone 
    ```
1. Change directory to the cloned repository.
    ```shell
    $ cd slack_bot
    ```
1. Create a `.env` file in the root directory. Below is the content of the file. Please write your own token that you obtained in ${YOUR_XXX}.
    ```
    SLACK_BOT_TOKEN=${YOUR_SLACK_BOT_TOKEN}
    SLACK_APP_TOKEN=${YOUR_SLACK_APP_TOKEN}

    CHATGPT_API_KEY=${YOUR_CHATGPT_API_KEY}
    ```
    Example
    ```
    SLACK_BOT_TOKEN=abcabcabcabc
    SLACK_APP_TOKEN=lmnlmnlmnlmn

    CHATGPT_API_KEY=xyzxyzxyzxyz
    ```
1. Install required libraries.
    ```shell
    $ pip install openai slack-bolt python-dotenv
    ```
1. Run `main.py`.
    ```shell
    $ python3 main.py
    ```