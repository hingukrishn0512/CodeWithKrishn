menu = {"panner": 250, "kajur": 300, "chai": 50}

def greet():
    print("Hello, sir! What would you like to have?")

def bill():
    order1 = input("Enter your first dish (paneer/kajur/chai): ").lower().strip()
    order2 = input("Enter your second dish (paneer/kajur/chai): ").lower().strip()
    order3 = input("Enter your third dish (paneer/kajur/chai): ").lower().strip()

    total = 0
    gst_rate = 0.05

    for order in [order1, order2, order3]:
        if order in menu:
            price = menu[order]
            gst_price = price + price * gst_rate
            print(f"Price of {order} with GST: ₹{gst_price:.2f}")
            total += gst_price
        else:
            print(f"Sorry, {order} is not available.")

    print(f"\n Total Bill (including GST): ₹{total:.2f}")

# Run the program
greet()
bill()
