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

## RAG LLM Example Results
### Question related to the content
![CleanShot 2024-05-04 at 19 31 19@2x](https://github.com/LeonSilva15/atlas-vector-search/assets/36859776/86fa7b7b-8d75-4c23-8e4f-b24cedc3ebd7)

### Question NOT related to the content
![CleanShot 2024-05-04 at 19 33 01@2x](https://github.com/LeonSilva15/atlas-vector-search/assets/36859776/ccb27564-f91c-46ba-9659-16a1b27727a7)


### References
| Reference | Official Website |
|------------|------------------|
| Beau's Video | https://youtu.be/JEBDfGqrAUA |
| MongoDB Atlas | https://www.mongodb.com/atlas/database |
| Hugging Face Model | https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2 |
| Langchain API | https://api.python.langchain.com/en/latest/langchain_api_reference.html |
| Langchain Docs | https://python.langchain.com/docs/get_started/introduction |
| Atlas Index Creation | https://www.mongodb.com/docs/atlas/atlas-search/create-index/ |
| PyMongo Docs | https://pymongo.readthedocs.io/en/stable/index.html |
| OpenAI Docs | https://platform.openai.com/docs/introduction |

> My Python version 3.10.13

Python environment commands:
```bash
python -m venv .venv
source .venv/bin/activate
deactivate || source deactivate
```
