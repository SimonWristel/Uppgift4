import csv
import os
import locale


products = []
def load_data(filename):


    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            id = int(row['id'])
            name = row['name']
            desc = row['desc']
            price = float(row['price'])
            quantity = int(row['quantity'])
            
            products.append(
                {
                    "id": id,
                    "name": name,
                    "desc": desc,
                    "price": price,
                    "quantity": quantity
                }
            )
    return products

def get_product(id, products):
    return f"{products[id] ["name"]} \t {products[id]["price"]}"

def get_products(products):
    product_list = []
    for product in products:
        product_info = f"{product["id"]} {product['name']} \t {product['desc']} \t {locale.currency(product['price'], grouping=True)}"
        product_list.append(product_info)
    
    return "\n".join(product_list)


#TODO: gör om så du slipper använda global-keyword
#TODO: write a function to return a specific product


locale.setlocale(locale.LC_ALL, 'sv_SE.UTF-8')  

os.system('cls')

load_data('db_products.csv')


print(get_products(products))

id= int(input("vilken produkt vill du visa?: "))


print(get_product(id, products))