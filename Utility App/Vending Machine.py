



## Code for the Welcome Menu of the Vending Machine ###############################################################


width = 100  
blue = '\033[94m'
reset = '\033[0m'
    
print("=" * width)
print(f"""
{blue}██╗░░░██╗███████╗███╗░░██╗██████╗░██╗███╗░░██╗░██████╗░  ███╗░░░███╗░█████╗░░█████╗░██╗░░██╗██╗███╗░░██╗███████╗            
██║░░░██║██╔════╝████╗░██║██╔══██╗██║████╗░██║██╔════╝░  ████╗░████║██╔══██╗██╔══██╗██║░░██║██║████╗░██║██╔════╝
╚██╗░██╔╝█████╗░░██╔██╗██║██║░░██║██║██╔██╗██║██║░░██╗░  ██╔████╔██║███████║██║░░╚═╝███████║██║██╔██╗██║█████╗░░
░╚████╔╝░██╔══╝░░██║╚████║██║░░██║██║██║╚████║██║░░╚██╗  ██║╚██╔╝██║██╔══██║██║░░██╗██╔══██║██║██║╚████║██╔══╝░░
░░╚██╔╝░░███████╗██║░╚███║██████╔╝██║██║░╚███║╚██████╔╝  ██║░╚═╝░██║██║░░██║╚█████╔╝██║░░██║██║██║░╚███║███████╗
░░░╚═╝░░░╚══════╝╚═╝░░╚══╝╚═════╝░╚═╝╚═╝░░╚══╝░╚═════╝░  ╚═╝░░░░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚═╝╚═╝░░╚══╝╚══════╝{reset}""".center(width))
print("=" * width)
print("Here you can find a variety of snacks, drinks, and treats".center(width))                         ## Welcome Message with ASCII art
print("Use the item code to select your products".center(width))
print("=" * width)




## Code for the Item Menu of the Vending Machine ###############################################################


from tabulate import tabulate                         ## Importing tabulate for tabular menu in vending machine

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
        "008": ("7-Up", 2.00, 5)                                    ## Nested Dictionary containing the Items in the Vending Machine
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


def print_items(items):
    width = 100 
    orange = '\033[38;5;214m'                                       ## Defining the Print Items function and Initializing the colors
    green = '\033[92m'
    yellow = '\033[93m'
    reset = '\033[0m'
    
    for category, products in items.items():
        print(f"\n{category.title()}:".center(width))                                             
        
        table_data = []
        for code, (item, price, stock) in products.items():
            table_data.append([code, f"{orange}{item}{reset}", f"{green}${price:.2f}{reset}", f"{yellow}{stock}{reset}"])                 ##  Resetting colors after each word because if I dont the Tables get colored halfway

        print(tabulate(table_data, headers=["Code", "Item", "Price", "Stock"], tablefmt="fancy_grid", numalign="center").center(width))

        
print_items(items)


## Code for the working of the Vending Machine ###############################################################


def purchase_items(items):
    width = 100

    red = "\033[31m"
    orange = "\033[38;5;214m"                                          ## Initializing colors for the Working function
    green = "\033[92m"                                  
    reset = "\033[0m"

    total_cost = 0

    while True:
        print("\n" + "=" * width)
        print(f"{red}Enter the item code to purchase or type 'exit' to quit.{reset}".center(width))                ## Asking user to enter code for an item
        print("=" * width)
        user_input = input("Item Code: ").strip()                 

        if user_input.lower() == "exit":
            if total_cost > 0:
                print("\n" + "=" * width)
                print(f"{green}Your total is: ${total_cost:.2f}{reset}".center(width))
                
                while True:
                    try:
                        payment = float(input(f"\n{green}Please enter payment amount: ${reset}"))                   ## Asking user for payment 
                        if payment < total_cost:                                                                      
                            print(f"{red}Insufficient payment. Please enter at least ${total_cost:.2f}.{reset}")    ## If payment is less than total cost than inform the user
                        else:
                            change = payment - total_cost                                                                          ## Calculating the change 
                            print(f"{green}Your change is: {change:.2f}{reset}$".center(width))                                   
                            print(f"{green}Thanks for using the vending machine! Have a great day!{reset}".center(width))             ## Thanks you message for using the Vending Machine
                            print("=" * width)
                            break
                    except ValueError:
                        print(f"{red}Invalid input. Please enter a valid number.{reset}")                                            ## If payment is not a numerical value than issues an error
                break
            else:
                print("\n" + "=" * width)
                print(f"{green}Thank you for using the vending machine! Have a great day!{reset}".center(width))
                print("=" * width)
                break

        found = False
        for category, products in items.items():
            if user_input in products:
                found = True
                item, price, stock = products[user_input]

                print("\n" + "-" * width)
                print(f"{red}Category: {category}{reset}".center(width))
                print("-" * width)

                if stock > 0:
                    print(f"{red}You selected: {orange}{item}{red} - ${price:.2f}{reset}".center(width))
                    products[user_input] = (item, price, stock - 1)
                    total_cost += price
                    print(f"{red}Purchase successful! Remaining stock for {orange}{item}{red}: {products[user_input][2]}{reset}".center(width))
                    print(f"{green}Total cost so far: ${total_cost:.2f}{reset}".center(width))
                else:
                    print(f"{red}Sorry, {orange}{item}{red} is out of stock.{reset}".center(width))
                break

        if not found:
            print("\n" + "-" * width)
            print(f"{red}Invalid item code. Please try again.{reset}".center(width))
            print("-" * width)

purchase_items(items)
