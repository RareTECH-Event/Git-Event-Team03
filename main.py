def main():
    while True:
        print("選択してください：")
        print("1: ベホマズン")
        print("2: カガケン")
        print("3: わっさん")
        print("q: ぽんた")

        choice = input("> ")

        if choice == "1":
            print("ベホマズンが選ばれました。")
        elif choice == "2":
            print("カガケンが選ばれました。")
        elif choice == "3":
            print("わっさんが選ばれました。")
        elif choice == "q":
            print("ぽんた。が選ばれました！ ")
            break
        else:
            print("無効な入力です。もう一度選択してください。")

if __name__ == "__main__":
    main()
