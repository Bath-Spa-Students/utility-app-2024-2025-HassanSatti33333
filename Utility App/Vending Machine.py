# Code for the Welcome Menu of the Vending Machine ###############################################################

width = 100  ##Set the width of the display
blue = '\033[94m'  ##Color code for blue text
white = '\033[97m'  ##Color code for white text

##Print the welcome banner with the machine's name
print("=" * width)
print(f"""
{blue}██╗░░░██╗███████╗███╗░░██╗██████╗░██╗███╗░░██╗░██████╗░  ███╗░░░███╗░█████╗░░█████╗░██╗░░██╗██╗███╗░░██╗███████╗            
██║░░░██║██╔════╝████╗░██║██╔══██╗██║████╗░██║██╔════╝░  ████╗░████║██╔══██╗██╔══██╗██║░░██║██║████╗░██║██╔════╝
╚██╗░██╔╝█████╗░░██╔██╗██║██║░░██║██║██╔██╗██║██║░░██╗░  ██╔████╔██║███████║██║░░╚═╝███████║██║██╔██╗██║█████╗░░
░╚████╔╝░██╔══╝░░██║╚████║██║░░██║██║██║╚████║██║░░╚██╗  ██║╚██╔╝██║██╔══██║██║░░██╗██╔══██║██║██║╚████║██╔══╝░░
░░╚██╔╝░░███████╗██║░╚███║██████╔╝██║██║░╚███║╚██████╔╝  ██║░╚═╝░██║██║░░██║╚█████╔╝██║░░██║██║██║░╚███║███████╗                                                          
░░░╚═╝░░░╚══════╝╚═╝░░╚══╝╚═════╝░╚═╝╚═╝░░╚══╝░╚═════╝░  ╚═╝░░░░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚═╝╚═╝░░╚══╝╚══════╝{white}""".center(width))  
print("=" * width)
print("Here you can find a variety of snacks, drinks, and treats".center(width))  ##Info about available products
print("Use the item code to select your products".center(width))  ##Instruction for selecting items
print("=" * width)

# Code for the Item Menu of the Vending Machine ###############################################################

from tabulate import tabulate  ##Importing the tabulate module to format product list into a table

##Defining items and their details 
items = {
    "Chips": {
        "001": ("Doritos", 3.00, 5),
        "002": ("Lay's", 2.00, 5),
        "003": ("Cheetos", 3.50, 5),
        "004": ("Kurkure", 2.50, 5)
    },
    "Soda": {
        "005": ("Coca-Cola", 2.00, 5),
        "006": ("Pepsi", 2.00, 5),
        "007": ("Sprite", 2.00, 5),
        "008": ("7-Up", 2.00, 5)
    },
    "Candy": {
        "009": ("Snickers", 3.00, 5),
        "010": ("M&Ms", 2.50, 5),
        "011": ("Galaxy", 3.00, 5)
    },
    "Water": {
        "012": ("Aquafina", 1.00, 8),
        "013": ("Dasani", 1.00, 8),
        "014": ("Mai", 1.00, 8),
        "015": ("Falcon", 1.00, 8)
    }
}

##Function to print items in a table
def print_items(items):
    width = 100  ##Set the width of the table
    orange = '\033[38;5;214m'  ##Color code for orange text                         
    green = '\033[92m'  ##Color code for green text
    yellow = '\033[93m'  ##Color code for yellow text
    white = '\033[97m'  ##Color code for white text

    ##Loop through the categories and print each product's details in a table
    for category, products in items.items():
        print(f"\n{category.title()}:".center(width))  ##Print category name

        table_data = []  ##Initialize a list for the product details
        for code, (item, price, stock) in products.items():
            table_data.append([code, f"{orange}{item}{white}", f"{green}${price:.2f}{white}", f"{yellow}{stock}{white}"])
        
        ##Print the table using the tabulate function
        print(tabulate(table_data, headers=["Code", "Item", "Price", "Stock"], tablefmt="fancy_grid", numalign="center").center(width))

print_items(items)  ##Call the function to display the item list

# Code for the working of the Vending Machine ###############################################################

def purchase_items(items):
    width = 100  ##Set the width of the display

    red = "\033[31m"  ##Red color for error messages
    orange = "\033[38;5;214m"  ##Orange color for item names
    green = "\033[92m"  ##Green color for success messages
    white = "\033[97m"  ##White color for regular text

    total_cost = 0  ##Variable to calculate the total cost of the items

    while True:  ##Infinite loop to keep asking for items until user exits
        print("\n" + "=" * width)
        print(f"{red}Enter the item code to purchase or type 'exit' to quit.{white}".center(width))
        print("=" * width)
        user_input = input("Item Code: ").strip()  ##Take the user input

        if user_input.lower() == "exit":  ##Exit condition
            if total_cost > 0:
                print("\n" + "=" * width)
                print(f"{green}Your total is: ${total_cost:.2f}{white}".center(width))

                while True:  ##Loop to handle payment
                    try:
                        payment = float(input(f"\n{green}Please enter payment amount: ${white}"))
                        if payment < total_cost:
                            print(f"{red}Insufficient payment. Please enter at least ${total_cost:.2f}.{white}")
                        else:
                            change = payment - total_cost
                            print(f"{green}Your change is: {change:.2f}{white}$".center(width))
                            print(f"{green}Thanks for using the vending machine! Have a great day!{white}".center(width))
                            print("=" * width)
                            break
                    except ValueError:  ##Handle invalid input for payment
                        print(f"{red}Invalid input. Please enter a valid number.{white}")
                break
            else:
                print("\n" + "=" * width)
                print(f"{green}Thank you for using the vending machine! Have a great day!{white}".center(width))
                print("=" * width)
                break

        found = False  ##Checking if the item code is valid
        for category, products in items.items():  ##Loop through each category to find the product
            if user_input in products:  ##Check if the user input matches a product code
                found = True
                item, price, stock = products[user_input]  ##Get product details

                print("\n" + "-" * width)
                print(f"{red}Category: {category}{white}".center(width))
                print("-" * width)

                if stock > 0:  ##Check if the product is in stock
                    print(f"{red}You selected: {orange}{item}{red} - ${price:.2f}{white}".center(width))
                    products[user_input] = (item, price, stock - 1)  ##Update stock
                    total_cost += price  ##Add price to total cost
                    print(f"{red}Purchase successful! Remaining stock for {orange}{item}{red}: {products[user_input][2]}{white}".center(width))
                    print(f"{green}Total cost so far: ${total_cost:.2f}{white}".center(width))
                else:  ##If out of stock it notify the user
                    print(f"{red}Sorry, {orange}{item}{red} is out of stock.{white}".center(width))
                break

        if not found:  ##If the user input does not match any valid product code
            print(f"{red}Invalid product code. Please try again.{white}".center(width))

##Start the purchase process when the user types Start
while True:
    user_input = input("\nType 'Start' to purchase Items or 'Exit' to quit: ").strip().lower()  ##Convert to lowercase so it isnt case sensitive

    if user_input == "start":  ##If user types 'Start', starts the program
        purchase_items(items)
    elif user_input == "exit":  ##If user types 'exit', exit the program
        print("\nThank you for using the vending machine! Have a great day!")
        break
    else:
        print("Invalid input. Please type 'Start' to begin or 'Exit' to quit.")
