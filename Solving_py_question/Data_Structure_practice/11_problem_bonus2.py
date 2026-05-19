#Given a dictionary of products and their prices, find the product with the highest price.

def most_expensiv_product(products):
    
    '''
    Find the product with the highest price.

    Parameters:
        products (dict): Dictionary of product: price pairs.

    Returns:
        tuple: (product_name, price) of the highest priced product.
    '''
    return max(products.items(), key=lambda x:x[1])


products ={
     "laptop" : 60000,
     "phone" : 20000,
    "watch" : 13000
}

product,  price = most_expensiv_product(products)
print(f"The most expensive product is '{product}' with price {price}")  



