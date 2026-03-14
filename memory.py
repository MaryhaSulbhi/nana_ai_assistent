import chromadb

client = chromadb.Client()
collection = client.create_collection("memories")

def save_memory(text):
    collection.add(
        documents=[text],
        ids=[str(hash(text))]
    )

def get_memory():
    results = collection.get()
    return results["documents"]