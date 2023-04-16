# slackとの連携に必要なライブラリ
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

# 別ファイルの呼び出し
import config
import reply_by_chatgpt
import setting

import re

# 各トークンを格納
SLACK_BOT_TOKEN = config.SLACK_BOT_TOKEN
SLACK_APP_TOKEN = config.SLACK_APP_TOKEN

# 応答生成器を指定
reply_generator = reply_by_chatgpt.GPT3_5(setting.log, setting.log_file)

# slackbotとの連携
app = App(token=SLACK_BOT_TOKEN)

# 特定のメッセージに反応
# @app.message("hawawa")
# def ask_who(say):
#     say("hoee")

# メンションに反応
@app.event("app_mention")
def respond_to_mention(event, say):
    raw_text = event["text"]
    user = event["user"]

    text = re.sub("<@.*> ", "", raw_text) # メンションの文字列を除去

    reply_generator.input_message(text)
    reply = reply_generator.get_response()["content"]
    reply_generator.write_json()

    say(thread_ts=event["event_ts"], text=f"<@{user}> {reply}")

SocketModeHandler(app, SLACK_APP_TOKEN).start()