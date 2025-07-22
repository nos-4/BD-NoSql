from pymongo import MongoClient

def get_database():
    client = MongoClient("mongodb://localhost:27017/") #Conecta ao servidor MongoDB
    db = client["pedido_db"]
    return db 
