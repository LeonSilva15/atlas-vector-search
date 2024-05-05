# Atlas Vector Search
Extending and updating the work of Beau Carnes from freeCodeCamp, this work implements Vector Search using Atlas MongoDB.

## Vector Embeddings
Vector embeddings are a type of data representation where items, such as words, phrases, or entire documents, are mapped to vectors of real numbers. These embeddings capture the essence of the items in a way that positions similar items closer together in the vector space, which makes them particularly useful for natural language processing (NLP) and machine learning tasks.

## Vector Search
Vector search, also known as similarity search or approximate nearest neighbor (ANN) search, is a method used to quickly retrieve the most similar items from a large set of data points in a vector space. This technique is particularly important in systems that use vector embeddings, where data points (such as text, images, or other types of information) are represented as vectors in a high-dimensional space.

## MongoDB Atlas Vector Search
MongoDB Atlas Vector Search is a feature integrated into MongoDB's cloud database service, Atlas, that enables users to perform efficient and scalable searches for similar documents based on vector embeddings. This feature allows for embedding-based searches directly within a MongoDB database, supporting applications such as recommendation systems, image retrieval, and natural language processing tasks directly within the database environment.

## Semantic Search Example Results
### With Hugging Face (Limited)
![hf results](https://github.com/LeonSilva15/atlas-vector-search/assets/36859776/626554fb-af5e-4d88-bab9-818ae8eb894e)
### With OpenAI
![openai results](https://github.com/LeonSilva15/atlas-vector-search/assets/36859776/f3b4ae0d-7874-49e1-a23d-db943ec8abf0)

### References
| Reference | Official Website |
|------------|------------------|
| Beau's Video | https://youtu.be/JEBDfGqrAUA |
| MongoDB Atlas | https://www.mongodb.com/atlas/database |
| Hugging Face Model | https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2 |

> My Python version 3.10.13

Python environment commands:
```bash
python -m venv .venv
source .venv/bin/activate
deactivate || source deactivate
```
