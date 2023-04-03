# ChatGPT for SlackBot

## 使い方
1. リポジトリをクローンする。
    ```shell
    $ git clone https://github.com/laksjdh/slack_bot.git
    ```
2. ディレクトリを移動する。
    ```shell
    $ cd slack_bot
    ```
1. 必要なライブラリをインストールする。
    ```shell
    $ pip install openai slack-bolt python-dotenv
    ```
1. 資産直下に`.env`ファイルを作成する。
    ```
    SLACK_BOT_TOKEN=${YOUR_SLACK_BOT_TOKEN}
    SLACK_APP_TOKEN=${YOUR_SLACK_APP_TOKEN}

    CHATGPT_API_KEY=${YOUR_CHATGPT_API_KEY}
    ```
    例
    ```
    SLACK_BOT_TOKEN=abcabcabcabc
    SLACK_APP_TOKEN=lmnlmnlmnlmn

    CHATGPT_API_KEY=xyzxyzxyzxyz
    ```
1. 資産直下に`init_messages.json`ファイルを作成する。ファイルの内容は以下のような形式に沿う必要がある。
    ```
    {
        "---任意の名前---": {
            "role": "system",
            "content": "---任意に設定---"
        },
        "example01": {
            "role": "system",
            "content": "あなたはこれからロールプレイを行います。あなたが演じる役の名前は「hawawa」です。あなたはuserの友人です。あなたはuserをおちょくったり揶揄ったりすることが大好きです。そのような性格の人物であると想定してuserの問いかけに対し答えてください。"
        },
        "example02": {
            "role": "system",
            "content": "あなたは英語教師です。あなたの名前は「hoee」です。userの発言に文法上の誤りが見られる場合は適宜訂正してください。"
        },
        ---以下同じように好きなだけ追加する---
    }
    ```
1. `main.py`を実行する。
    ```shell
    $ python3 main.py
    ```
1. （初回のみ）以下の通り回答する。2回目以降は任意の回答をする。
    ```
    デフォルト設定で会話を始めますか？（y/n）
    >>> n

    新しい会話を始めますか？（y/n）
    >>> y

    init messageを選んでください。
    >>> （任意のmessageを選択）

    log fileの名前を決めてください。拡張子「.json」を必ず含めてください。
    >>> log.json
    ```
    - デフォルト設定で会話を始めますか？
        - y: log.jsonの内容を読み込み前回の会話の続きから会話を開始する。詳細設定が面倒な場合に選択。
        - n: その他の方法で会話を開始する。詳細に設定したい場合に選択。
    - 新しい会話を開始しますか？
        - y: 新しい会話を開始する。
        - n: すでに存在するlog fileの内容を読み込み前回の会話の続きから会話を開始する。
    - init messageを選んでください。
        - init_messages.jsonからChatGPTへのプロンプトとなるメッセージを選択する。
    - log fileの名前を決めてください。
        - 任意のファイル名を設定する。ファイル名の拡張子は必ず.jsonとする。指定した名称のファイルがlog_filesフォルダ内に作成される。すでに存在するファイル名であった場合、log fileが上書きされるので要注意。
    - log fileを選んでください。
        - どのlog fileを読み込むかを選択する。
1. 以下の表示が出たらOK。
    ```
    ⚡️ Bolt app is running!
    ```
1. Slackでslack botにメンションをつけて会話する。

## How to Use
1. Clone this repository.
    ```shell
    $ git clone https://github.com/laksjdh/slack_bot.git
    ```
1. Change directory to the cloned repository.
    ```shell
    $ cd slack_bot
    ```
1. Install required libraries.
    ```shell
    $ pip install openai slack-bolt python-dotenv
    ```
1. Create `.env` file in the root directory. Below is the content of the file. Please write your own token that you obtained in ${YOUR_XXX}.
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
1. Run `main.py`.
    ```shell
    $ python3 main.py
    ```