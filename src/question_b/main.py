from question_b import create_stock_file, get_stock_list, display_stock_list

def main():
    create_stock_file()
    stocks = get_stock_list()

    while True:
        print("\nMenu:")
        print("1. Display Stock Report")
        print("2. Exit")

        choice = input("Enter choice 1 or 2: ")

        if choice == "1":
            display_stock_list(stocks)
        elif choice == "2":
            print("Exiting Program")
            break
        else:
            print("Invalid input. Enter 1 or 2.")

if __name__ == "__main__":
    main() 