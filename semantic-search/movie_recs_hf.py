import os
import pymongo
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Hugging Face Model URL
embedding_url = 'https://api-inference.huggingface.co/pipeline/feature-extraction/sentence-transformers/all-MiniLM-L6-v2'

# DB client and collection
client = None
collection = None

# Connect to the MongoDB client
def connectToDB():
    global db, client, collection
    
    # Set MongoDB client
    try:
        client = pymongo.MongoClient(os.getenv('MONGO_CLIENT'))
    except:
        raise ConnectionError('Unable to connect to database')
    
    # Identify the database and collection
    db = client.sample_mflix
    collection = db.movies

# Get first items in the collection
def firstItems(num = 5):
    items = collection.find().limit( num )
    for item in items:
        print( item )

# Generate plot vector embeddings
def generate_embedding(text: str) -> list[float]:
    response = requests.post(
        embedding_url,
        headers={'Authorization': f"Bearer {os.getenv('HF_TOKEN')}"},
        json={'inputs': text}
    )

    if response.status_code != 200:
        raise ValueError(f'Request failed with status code {response.status_code}: {response.text}')

    return response.json()

# Embed the database collections plots
def embedDataBaseRecords(maxRecords = None):
    connectToDB()
    records = collection.find({
        'plot':{'$exists': True},
        'plot_embedding_hf':{'$exists': False}
    })
    
    if maxRecords:
        records = records.limit(maxRecords)
    for doc in records:
        doc['plot_embedding_hf'] = generate_embedding(doc['plot'])
        collection.replace_one({'_id': doc['_id']}, doc)

# Get the best results on the vector search
def getSearchResults(query):
    results = collection.aggregate([
        { '$vectorSearch': {
            'queryVector': generate_embedding(query),
            'path': 'plot_embedding_hf',
            'numCandidates': 100,
            'limit': 4,
            'index': 'PlotSemanticSearch',
            }
        }
    ])
    return results

# Print the vector search results
def printResults(results):
    for document in results:
        print(f"Movie Name: {document['title']},\nMovie Plot: {document['plot']}\n")

# Get and print the vector search results
def getVectorSearch(query):
    results = getSearchResults(query)
    printResults(results)

# Connect to the Data base
# Prompt for a plot to look for
def main():
    connectToDB()

    while(True):
        try:
            query = input('Enter a plot to look for or press "Ctrl + C" to exit\n')
            getVectorSearch(query)

        except KeyboardInterrupt:
            break

if __name__ == '__main__':
    # embedDataBaseRecords()
    main()
