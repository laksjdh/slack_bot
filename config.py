# .envファイルをロードして環境変数へ反映
from dotenv import load_dotenv
load_dotenv()

# 環境変数を参照
import os

# SlackのAPIトークン
SLACK_BOT_TOKEN = os.getenv("SLACK_BOT_TOKEN")
SLACK_APP_TOKEN = os.getenv("SLACK_APP_TOKEN")

# ChatGPTのAPIトークン
CHATGPT_API_KEY = os.getenv("CHATGPT_API_KEY")