def main():
    while True:
        print("選択してください：")
        print("1: 赤")
        print("2: 青")
        print("3: 黄色")
        print("q: 終了")

        choice = input("> ")

        if choice == "1":
            print("赤が選ばれました。")
        elif choice == "2":
            print("青が選ばれました。")
        elif choice == "3":
            print("黄色が選ばれました。")
        elif choice == "q":
            print("プログラムを終了します。")
            break
        else:
            print("無効な入力です。もう一度選択してください。")

if __name__ == "__main__":
    main()
