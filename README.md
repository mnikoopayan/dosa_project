# dosa_project
## Dosa Orders Analysis System
## Overview
This project is designed to assist the owner of a new Dosa restaurant in analyzing orders received over the past year. By processing these orders, the system aims to improve the restaurant's operational efficiency and customer service. The system reads orders from a JSON file and generates two new JSON files: one mapping customers' phone numbers to their names and another detailing menu items, their prices, and the number of times each has been ordered.

## Design
The system is implemented in Python and follows idiomatic Python conventions for clarity and maintainability. It consists of several key functions:

- `load_orders`: Reads orders from a JSON file.
- `get_customers`: Extracts customer information from orders.
- `get_items`: Compiles information about ordered items.
- `save_json`: Saves data to a JSON file in the specified directory.

The project structure is straightforward, emphasizing readability and ease of use. It has been formatted with Black for consistent styling and has undergone linting with pylint to ensure adherence to best practices and to address potential issues.

## Usage
To use this system, ensure that Python is installed on your machine. The script requires two command line arguments: the path to the orders JSON file and the output directory for the generated JSON files.

php
python script.py <path_to_orders_json> <output_directory>
Example:

bash
python script.py example_orders.json ./output
This command reads the orders from example_orders.json and generates customers.json and items.json in the specified ./output directory.

## Dependencies
- Python 3.x
No external libraries are required for the core functionality of this system.

## Enhancements
- **Code Formatting**: The code has been formatted using Black, ensuring a consistent and readable style throughout the project.
- **Linting**: The project has been linted with pylint, addressing all raised issues to ensure the code meets high-quality standards.

## Contributing
We welcome contributions and suggestions! Please fork the repository and submit a pull request with your proposed changes.

For any questions or issues, please open an issue in the GitHub repository.
