import os
import pymongo
import openai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# OpenAI API Token
openai.api_key = os.getenv('OPENAI_TOKEN')
# DB client and collection
client = pymongo.MongoClient(os.getenv('MONGO_CLIENT'))
# Select the sample movies database
db = client.sample_mflix
# The sample collection has an embedded property using OpenAI
collection = db.embedded_movies

# Get first items in the collection
def get_first_items(num = 5):
    return collection.find().limit( num )

# Generate plot vector embeddings
def generate_embedding(text: str) -> list[float]:
    response = openai.embeddings.create(
        model='text-embedding-ada-002',
        input=[text]
    )
    return response.data[0].embedding

# Get the best results on the vector search
def get_search_results(query):
    results = collection.aggregate([
        { '$vectorSearch': {
            'queryVector': generate_embedding(query),
            'path': 'plot_embedding',
            'numCandidates': 100,
            'limit': 4,
            'index': 'PlotSemanticSearchOpenAI',
            }
        }
    ])
    return results

# Print the vector search results
def print_results(results):
    for document in results:
        print(f"Movie Name: {document['title']},\nMovie Plot: {document['plot']}\n")

# Get and print the vector search results
def get_vector_search(query):
    results = get_search_results(query)
    print_results(results)

# Prompt for a plot to look for
def main():
    while(True):
        try:
            query = input('Enter a plot to look for or press "Ctrl + C" to exit\n')
            get_vector_search(query)

        except KeyboardInterrupt:
            break

if __name__ == '__main__':
    main()
    
