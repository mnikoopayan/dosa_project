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
