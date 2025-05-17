class Stock:
    def __init__(self, symbol, company_name):
        self.__symbol = symbol
        self.__company_name = company_name

    @property
    def symbol(self):
        return self.__symbol
    
    @property
    def company_name(self):
        return self.__company_name
    
def get_stock_data():
    return [
        Stock("AAPL", "Apple Inc"),
        Stock("Cat", "Caterpillar"),
        Stock("EK", "Eastman Kodak"),
        Stock("GOOG", "Google"),
        Stock("MSFT", "Microsoft")
    ]
    
def display_stock_history(stocks):
    print("\nStock Purchase History")
    print(f"{'Symbol':<8}{'Company Name':<20}")
    print ("-" * 28)
    for stock in stocks:
        print(f"{stock.symbol:<8}{stock.company_name:<20}")

def show_menu():
    while True:
        print("\n Main Menu:")
        print("1. Display stock purchase history")
        print("2. Exit")

        choice = input("Please enter your choice 1 or 2: ").strip()

        if choice == "1":
            return "display"
        elif choice == "2":
            return "exit"
        else:
            print("Invalid selection. Please enter 1 or 2.")
        
def test_config():
    return True