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

# Function to compile item information from orders
def get_items(orders):
    items = {}
    for order in orders:
        for item in order['items']:
            if item['name'] not in items:
                items[item['name']] = {'price': item['price'], 'orders': 1}
            else:
                items[item['name']]['orders'] += 1
    return items

# Update main function to include item compilation
def main():
    # Existing setup, order loading, and customer extraction...

    items = get_items(orders)
    print(items)  # Temporary print to verify compilation

# Existing if __name__ == "__main__" block...