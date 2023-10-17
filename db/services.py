from db.connection import connection

def list_products():
    result = connection.execute("SELECT * FROM product;").fetchall()
    return result
