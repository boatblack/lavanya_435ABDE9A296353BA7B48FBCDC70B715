def linear_search_product(products, target_product):
    indices = []
    for index, product in enumerate(products):
        if product == target_product:
            indices.append(index)
    return indices

product_list = ["Apple", "Banana", "Orange", "Apple", "Grapes", "Apple"]
target = "Apple"
result = linear_search_product(product_list, target)
print(result) 
