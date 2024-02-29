import json
import sys

# Function to load orders from a given JSON file
def load_orders(filepath):
    with open(filepath) as f:
        return json.load(f)

# Main function setup
def main():
    if len(sys.argv) < 2:
        print("Usage: python script.py <orders_file>")
        sys.exit(1)
        
    orders_file = sys.argv[1]
    orders = load_orders(orders_file)
    print(orders)  # Temporary print to verify loading

if __name__ == "__main__":
    main()
    
# Function to extract customers' information from orders
def get_customers(orders):
    return {order['phone']: order['name'] for order in orders}

# Update main function to include customer extraction
def main():
    # Existing setup and order loading...

    customers = get_customers(orders)
    print(customers)  # Temporary print to verify extraction

# Existing if __name__ == "__main__" block...