def main():
    while True:
        print("選択してください：")
        print("1: おーちゃんがmain.pyを編集しました")
        print("2: はち子編集")
        print("3: ポテ吉が編集しました！")
        print("q: 終了")

        choice = input("> ")

        if choice == "1":
            print("おーちゃんがmain.pyを編集しました")
        elif choice == "2":
            print("はち子編集")
        elif choice == "3":
            print("ポテ吉が選ばれました！")
        elif choice == "q":
            print("プログラムを終了します。")
            break
        else:
            print("無効な入力です。もう一度選択してください。")

if __name__ == "__main__":
    main()
