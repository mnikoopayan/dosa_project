import json
import os
import sys

# Function to load orders from a given JSON file
def load_orders(filepath):
    with open(filepath) as f:
        return json.load(f)

# Function to extract customers' information from orders
def get_customers(orders):
    # Creates a dictionary with phone numbers as keys and customer names as values
    return {order['phone']: order['name'] for order in orders}

# Function to compile item information from orders
def get_items(orders):
    items = {}
    for order in orders:
        for item in order['items']:
            name = item['name']
            if name not in items:
                # Initializes the item with price and order count if not already in dictionary
                items[name] = {'price': item['price'], 'orders': 0}
            # Increments the order count for each item
            items[name]['orders'] += 1
    return items

# Function to save a dictionary to a JSON file in a specified directory
def save_json(data, filename, directory):
    path = os.path.join(directory, filename)
    with open(path, 'w') as f:
        # Dumps the data into the file with indentation for readability
        json.dump(data, f, indent=4)
        
# Main function that coordinates the script's workflow and manages its execution
def main():
    # Checks if the correct number of command line arguments are provided
    if len(sys.argv) < 3:
        print("Usage: python script.py <orders_file> <output_dir>")
        sys.exit(1)
        
    orders_file = sys.argv[1]
    output_dir = sys.argv[2]
    
    # Loads orders from the specified file
    orders = load_orders(orders_file)
    # Extracts customers information
    customers = get_customers(orders)
    # Compiles items information
    items = get_items(orders)
    
    # Saves the extracted information to JSON files
    save_json(customers, 'customers.json', output_dir)
    save_json(items, 'items.json', output_dir)

# Ensures that the script can be run directly
if __name__ == "__main__":
    main()
