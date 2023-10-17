from db.services import list_products

def get_root():
    return {"Hello": "World"}

def get_products_list():
    products = list_products()
    return [
        {"id": p[0], "product_name": p[1], "category": p[2]}
        for p in products
    ]
