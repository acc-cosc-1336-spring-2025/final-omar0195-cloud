from question_c import get_stock_data, display_stock_history, show_menu

def main():
    stocks = get_stock_data()

    while True:
        user_choice = show_menu()

        if user_choice == "display":
            display_stock_history(stocks)
        elif user_choice == "exit":
            print("Exiting Program")
            break

if __name__ == "__main__":
    main()