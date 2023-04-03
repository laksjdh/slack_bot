import json
import os

is_default = ""
is_new = ""

while is_default != "y" and is_default != "n":
    is_default = input("デフォルト設定で会話を始めますか？（y/n）")

    if is_default == "y":
        with open("./log_files/log.json", mode="r", encoding="utf-8") as infile:
            log = json.load(infile)
            log_file = "log.json"

    elif is_default == "n":
        while is_new != "y" and is_new != "n":
            is_new = input("新しい会話を始めますか？（y/n）")

            if is_new == "y":
                with open('init_messages.json') as infile:
                    init_messages = json.load(infile)
                init_message_options = init_messages.keys()
                print("init messageを選んでください。")
                for init_message_option in init_message_options:
                    print(">", init_message_option)
                init_message = input("init message: ")
                log = []
                log.append(init_messages[init_message])

                print("log fileの名前を決めてください。拡張子「.json」を必ず含めてください。")
                log_file = input("log file: ")
                while not log_file.endswith(".json"):
                    print("拡張子「.json」を含めて入力してください。")
                    log_file = input("log file: ")

            elif is_new == "n":
                path = "./log_files"
                log_files = os.listdir(path)
                print("log fileを選んでください。")
                for log_file_option in log_files:
                    if log_file_option.endswith(".json"):
                        print(">", log_file_option)
                log_file = input("log file: ")
                while log_file not in log_files:
                    print(f"{log_file} というlog fileは存在しません。再度入力してください。")
                    log_file = input("log file: ")

                with open(f"./log_files/{log_file}", mode="r", encoding="utf-8") as infile:
                    log = json.load(infile)

            else:
                print("yまたはnで答えてください。")
                continue

    else:
        print("yまたはnで答えてください。")
        continue