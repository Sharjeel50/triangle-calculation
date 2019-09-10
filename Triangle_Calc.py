from Calculate import DataResult


def main():
    print("\n")
    print("Enter 'Exit' to close program")
    file = input("Enter file name: ") + ".csv".lower()
    print("\n")
    if file == "exit.csv" or file == "Exit.csv":
        exit()
    else:
        # DataResult(file)
        try:
            DataResult(file)
            main()
        except Exception as e:
            print(e, "\n")
            print(" - Try Again - ")
            main()



if __name__ == "__main__":
    main()
