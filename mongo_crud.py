from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('localhost', 27017)

# Create or access a database
db = client['mydatabase']

# Create or access a collection
collection = db['mycollection']

# Insert document(s) into the collection
data = {"name": "John", "age": 30}
result = collection.insert_one(data)
print(f"Inserted document ID: {result.inserted_id}")

# Query document(s) from the collection
query = {"name": "John"}
result = collection.find(query)
for doc in result:
    print(doc)

# Update document(s) in the collection
update_query = {"name": "John"}
new_values = {"$set": {"age": 35}}
collection.update_one(update_query, new_values)
print("Document updated successfully")

query = {"name": "John"}
result = collection.find(query)
for doc in result:
    print(doc)

# Delete document(s) from the collection
delete_query = {"name": "John"}
collection.delete_one(delete_query)
print("Document deleted successfully")

query = {"name": "John"}
result = collection.find(query)
for doc in result:
    print(doc)
