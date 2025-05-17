class Stock:
    def __init__(self, symbol, company_name):
        self.__symbol = symbol
        self.__company_name = company_name

    def get_symbol(self):
        return self.__symbol
    
    def get_company_name(self):
        return self.__company_name
    
def create_stock_file():
    with open('stock_file.dat', 'w') as f:
        f.write("AAPL Apple Inc\n")
        f.write("CAT Caterpillar\n")
        f.write("EK Eastman Kodak\n")
        f.write("MSFT Microsoft\n")

def get_stock_list():
    return [
        Stock("AAPL", "Apple Inc"),
        Stock("CAT", "Caterpillar"),
        Stock("EK", "Eastman Kodak"),
        Stock("GOOG", "Google"),
        Stock("MSFT", "Microsoft")
    ]
def display_stock_list(stock_list):
    print("\nStock Report")
    print("Company\t\tSymbol")
    print("-" * 30)
    for stock in stock_list:
        print(f"{stock.get_company_name()}\t{stock.get_symbol()}")

def test_config():
    return True