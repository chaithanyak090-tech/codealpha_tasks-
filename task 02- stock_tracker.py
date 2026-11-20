# Stock Portfolio Tracker

# Dictionary containing stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "MSFT": 400,
    "GOOGL": 150,
    "AMZN": 190
}

# Store user's investments
portfolio = {}

total_investment = 0


print("   STOCK PORTFOLIO TRACKER        ")


print("\nAvailable Stocks:")

for stock, price in stock_prices.items():
    print(stock, ":", price)

# Ask how many stocks the user wants to enter
while True:
    try:
        number = int(input("\nHow many stocks do you want to buy? "))

        if number <= 0:
            print("Please enter a positive number.")
            continue

        break

    except ValueError:
        print("Please enter a valid whole number.")

# Get stock details
for i in range(number):

    stock_name = input("\nEnter stock name: ").upper()

    if stock_name not in stock_prices:
        print("Stock not available!")
        continue

    try:
        quantity = int(input("Enter quantity: "))

        if quantity <= 0:
            print("Quantity must be positive.")
            continue

    except ValueError:
        print("Invalid quantity!")
        continue

    # Calculate investment
    price = stock_prices[stock_name]
    investment = price * quantity

    # Save investment
    portfolio[stock_name] = portfolio.get(stock_name, 0) + quantity

    total_investment += investment

    print("Investment value:", investment)

# Display final portfolio
print("\n        PORTFOLIO SUMMARY         ")

for stock, quantity in portfolio.items():
    value = stock_prices[stock] * quantity

    print(stock, "| Quantity:", quantity,
          "| Total Value:", value)


print("Total Investment:", total_investment)

# Save result in a text file
with open("portfolio.txt", "w") as file:

    file.write("STOCK PORTFOLIO SUMMARY\n")

    for stock, quantity in portfolio.items():
        value = stock_prices[stock] * quantity

        file.write(
            f"{stock} - Quantity: {quantity}, Value: {value}\n"
        )

    file.write(f"\nTotal Investment: {total_investment}")

print("\nPortfolio saved successfully in portfolio.txt")
