# openaiのAPI連携
import openai

# 別ファイルの呼び出し
import config

# その他必要なライブラリ
# import os
import json

# openaiのAPI KEY
openai.api_key = config.CHATGPT_API_KEY

class GPT3_5:
    def __init__(self, log, log_file):
        self.messages = log
        self.path = f"./log_files/{log_file}"

    def call_methods(self, input):
        self.input_message(input)
        reply = self.get_response()["content"]
        self.write_json()
        return reply

    def input_message(self, input):
        user_message = {
            'role': 'user',
            'content': input
        }
        self.messages.append(user_message)

    def get_response(self):
        response = openai.ChatCompletion.create(
            model='gpt-3.5-turbo',
            messages=self.messages,
            temperature=0.0,
        )
        bot_message = {
            'role': 'assistant',
            'content': response["choices"][0]["message"]["content"]
        }
        self.messages.append(bot_message)
        return bot_message

    def write_json(self):
        with open(self.path, mode="w", encoding="utf-8") as outfile:
            json.dump(self.messages, outfile, ensure_ascii=False, indent=2)
