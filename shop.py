####################### DO NOT MODIFY THIS CODE ########################
menu = {
    "original cupcake": 2,
    "signature cupcake": 2.750,
    "coffee": 1,
    "tea": 0.900,
    "bottled water": 0.750
}
original_flavors = ["vanilla", "chocolate", "strawberry", "caramel", "raspberry"]
original_price = 2
signature_price = 2.750

############################# Start Here! ##############################
cupcake_shop_name = "Aljumiah's Shop"
signature_flavors = ["tuna","salmon","red herring"]
order_list = []


def print_menu():
    """
    Print the items in the menu dictionary.
    """
    # your code goes here!
    for item in menu:
        print ("- \"%s\" (KD %s)" %(item,menu[item]))


def print_originals():
    """
    Print the original flavor cupcakes.
    """
    print("Our original flavor cupcakes (KD %s each):" % original_price)
    # your code goes here!
    for flavor in original_flavors:
        print ("- \"%s\"" %(flavor))

def print_signatures():
    """
    Print the signature flavor cupcakes.
    """
    print("Our signature flavor cupcake (KD %s each):" % signature_price)
    # your code goes here!
    for Sflavor in signature_flavors:
        print("- \"%s\"" %(Sflavor)) 
    

def is_valid_order(order):
    """
    Check if an order exists in the shop.
    """
    # your code goes here!
    if order in menu or order in signature_flavors or order in original_flavors:
        return True
    else:
        return False



def get_order():
    """
    Repeatedly ask customer for order until they end their order by typing "Exit".
    """
    order_list = []
    # your code goes here!\
    while True:
        order = input("Please type your order or exit to end: ")
        if order == "exit":
            break
        elif is_valid_order(order) == False: 
            print("Sorry, your order does not Exist.")
            
        elif is_valid_order(order) == True:
            order_list.append(order)
        else:
            print("error")
    return order_list
    get_total_price(order_list)

def accept_credit_card(total):
    """
    Return whether an order is eligible for credit card payment.
    """
    # your code goes here!
    if total > 5:
        print("Eligible for credit card payment")
    else: 
        print("Price is not Eligible for credit card payment")


def get_total_price(order_list):
    """
    Calculate and return total price of the order.
    """
    total = 0
    # your code goes here!
    for order in order_list:
        if order in menu:
            total += menu[order]
        elif order in signature_flavors:
            total += signature_price             
        elif order in original_flavors:
            total += original_price
    return total


def print_order(order_list):
    """
    Print the order of the customer.
    """
    print()
    print("That's all, Your order is: ")
    # your code goes here!
    for order in order_list:
        print ("- %s" %(order))
    #print(order_list)
    print("Your total is: %s" %(get_total_price(order_list)))
    print(accept_credit_card(get_total_price(order_list)))
    print ("Thank you for shopping at %s " %(cupcake_shop_name))