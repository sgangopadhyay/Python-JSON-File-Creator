# PROGRAM : Python Program to Create JSON File
# PROGRAMMER : Suman Gangopadhyay
# DATE : 8-Jan-2025
# CAVEATS : This will create a JSON file for Products

import json
import random

class SumanJSONFileCreator:

    def __init__(self, file_name, num_products):
        self.file = file_name
        self.num_products = num_products

    def generate_product_data(self):
        """
        Generates a list of dictionaries, each representing a product with
        name, manufacturer, price, and unit_sold.

        Returns:
            A list of dictionaries, where each dictionary represents a products in a JSON file.
        """

        product_names = ["Laptop", "Smartphone", "Tablet", "Headphones", "Watch",
                         "TV", "Refrigerator", "Washing Machine", "Air Conditioner",
                         "Microwave", "Blender", "Toaster", "Coffee Maker",
                         "Camera", "Drone", "Game Console", "Video Game",
                         "Speaker", "Router", "Smart Home Device"]

        manufacturers = ["Apple", "Samsung", "Google", "Microsoft", "Dell",
                         "HP", "Lenovo", "Asus", "Acer", "LG", "Sony",
                         "Panasonic", "Toshiba", "Philips", "Xiaomi", "OnePlus",
                         "Huawei", "Oppo", "Vivo", "Realme"]

        products = []
        for id in range(self.num_products):
            product = {
                "id": id + 1,
                "name": random.choice(product_names),
                "manufacturer": random.choice(manufacturers),
                "price": round(random.uniform(50, 1000), 2),
                "unit_sold": random.randint(10, 1000)
            }
            products.append(product)
        return products

    def json_file_creator(self):
    
        # Generate product data
        product_data = self.generate_product_data()
        
        # Write the data to a JSON file
        with open(self.file, "w") as file:
            json.dump(product_data, file, indent=2)
        print(f"Product data successfully saved to {self.file}")


# Main Executing Program

if __name__ == "__main__":
    number_of_data = 300
    file_name = "suman.json"
    suman = SumanJSONFileCreator(file_name, number_of_data)
    suman.json_file_creator()
