# ChatGPT for SlackBot

## How to Use
1. Clone this repository.
    ```shell
    $ git clone
    ```
1. Create a `.env` file in the root directory. 
1. Install required libraries.
    ```shell
    $ pip install 
    ```
1. Run `main.py`.
    ```shell
    $ python3 main.py
    ```

## Specification
- Respond to mentions.


## SlackBotを作る手順

- slackのAPI トークンを取得
    - 参考
        - [URL](https://miyabikno-jobs.com/entrance-labotlatori/)
        - [URL](https://miyabikno-jobs.com/slackbot-api-token/)
    - 

- APIトークンを環境変数として反映
    - 参考
        - [URL](https://maku77.github.io/python/env/dotenv.html)
    - .env
        - トークンを記述
        - gitで追跡をしないよう注意（セキュリティのため）
            - つまり `.gitignore` に `.env` を追加する
    - config.py
        - .envで記述したトークンを環境変数として反映し参照
    - slackbot_setting.py
        - トークンを呼び出す

- ログをjsonファイルとして保存したい