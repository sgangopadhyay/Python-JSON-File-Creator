# JSON File Creator

This Python program generates a JSON file containing product data. Each product entry includes fields such as `id`, `name`, `manufacturer`, `price`, and `unit_sold`. The program can create a specified number of product entries with randomized values.

## Features

## Program Description

* **Functionality:** Performs monkey testing on a website.
* **Programmer:** Suman Gangopadhyay
* **Email ID:** linuxgurusuman@gmail.com
* **Date:** 1-Jan-2025
* **Version:** 1.0
* **Code Library:** Selenium
* **Prerequisites:** Python, Selenium, ChromeDriver
* **Caveats:** None

## Features

- **Randomized Product Data:** Generates random product names, manufacturers, prices, and units sold.
- **JSON File Output:** Saves the generated data into a specified JSON file.
- **Configurable Number of Products:** Allows the user to specify how many products to generate.

## Usage

### Prerequisites
- Python 3.x

### Installation
1. Clone the repository or copy the script file.
2. Ensure Python 3.x is installed on your system.

### Running the Program

1. Save the script in a file, e.g., `json_file_creator.py`.
2. Open a terminal and navigate to the directory containing the script.
3. Run the script:

   ```bash
   python json_file_creator.py
   ```
4. The script will generate a JSON file (default: `suman.json`) containing the product data.

### Customizing the Output

- To change the number of products:
  - Modify the `number_of_data` variable in the `__main__` section.

  ```python
  number_of_data = 300  # Set the desired number of products
  ```

- To change the output file name:
  - Modify the `file_name` variable in the `__main__` section.

  ```python
  file_name = "custom_file.json"  # Set the desired file name
  ```

## Example Output

Here is an example of the JSON output:

```json
[
  {
    "id": 1,
    "name": "Laptop",
    "manufacturer": "Apple",
    "price": 899.99,
    "unit_sold": 450
  },
  {
    "id": 2,
    "name": "Smartphone",
    "manufacturer": "Samsung",
    "price": 499.49,
    "unit_sold": 300
  }
  // ...more entries
]
```

## Code Overview

### Classes and Methods

- **`JSONFileCreator`**:
  - **`__init__(file_name, num_products)`**: Initializes the class with the file name and number of products.
  - **`generate_product_data()`**: Generates a list of product dictionaries with randomized data.
  - **`json_file_creator()`**: Writes the generated data to the specified JSON file.

### Key Variables

- `product_names`: List of possible product names.
- `manufacturers`: List of possible manufacturers.
- `price`: Randomly generated price between 50 and 1000 (rounded to 2 decimal places).
- `unit_sold`: Randomly generated integer representing units sold (between 10 and 1000).

## License
This project is open source and available under the [MIT License](LICENSE).

## Author
**Suman Gangopadhyay**  
Date: 8-Jan-2025
