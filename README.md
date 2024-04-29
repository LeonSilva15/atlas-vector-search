# Atlas Vector Search
Extending the work of @BeauCarnes from freeCodeCamp, this work implements Vector Search using Atlas MongoDB.

## Vector Embeddings
Vector embeddings are a type of data representation where items, such as words, phrases, or entire documents, are mapped to vectors of real numbers. These embeddings capture the essence of the items in a way that positions similar items closer together in the vector space, which makes them particularly useful for natural language processing (NLP) and machine learning tasks.

## Vector Search
Vector search, also known as similarity search or approximate nearest neighbor (ANN) search, is a method used to quickly retrieve the most similar items from a large set of data points in a vector space. This technique is particularly important in systems that use vector embeddings, where data points (such as text, images, or other types of information) are represented as vectors in a high-dimensional space.

## MongoDB Atlas Vector Search
MongoDB Atlas Vector Search is a feature integrated into MongoDB's cloud database service, Atlas, that enables users to perform efficient and scalable searches for similar documents based on vector embeddings. This feature allows for embedding-based searches directly within a MongoDB database, supporting applications such as recommendation systems, image retrieval, and natural language processing tasks directly within the database environment.

## Setup
1. Go to [MongoDB Atlas](https://www.mongodb.com/atlas/database)
2. Create a new project deploying a free (optional) cloud environment
3. Once the cluster is created add the `movies sample data`
4. Go to the `connect` button and get the `MongoDB connection driver string`
5. Create a password for the cluster
6. Go to the Cluster's `Search` tab
7. Create a `Search Index` using the `JSON Editor`
8. Select `sample_mflix - movies`
9. Name the Index as **PlotSemanticSearch**
10. Use the following Index
```json
{
  "mappings": {
    "dynamic": true,
    "fields": {
      "plot_embedding_hf": [
        {
          "dimensions": 384,
          "similarity": "dotProduct",
          "type": "knnVector"
        }
      ]
    }
  }
}
```
11. Go to [Hugging Face Tokens](https://huggingface.co/settings/tokens)
12. Create an access token

### References
| Dependency | Official Website |
|------------|------------------|
| Beau's Video | https://youtu.be/JEBDfGqrAUA |
| MongoDB Atlas | https://www.mongodb.com/atlas/database |
| Hugging Face Model | https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2 |

> My Python version 3.10.13

Python environment command:
```bash
python -m venv .venv
```
