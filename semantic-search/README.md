# Semantic Search
Semantic search is an advanced method of searching that goes beyond simple keyword matching to understand the intent and contextual meaning of the search query. It aims to improve search accuracy by understanding the searcher’s intent and the contextual meaning of terms as they appear in the searchable dataspace, whether on the web or within a specific database or document collection. 

## Setup
1. Go to [MongoDB Atlas](https://www.mongodb.com/atlas/database)
2. Create a new project deploying a free (optional) cloud environment
3. Once the cluster is created add the `movies sample data`
4. Go to the `connect` button and get the `MongoDB connection driver string`
5. Create a password for the cluster
6. Go to the Cluster's `Search` tab
7. Create a `Search Index` using the `JSON Editor`

### Using HuggingFace
> movie_recs_hf.py
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

### Using OpenAI
> movie_recs_oai.py
8. Select `sample_mflix - embedded_movies`
9. Name the Index as **PlotSemanticSearchOpenAI**
10. Use the following Index
```json
{
  "mappings": {
    "dynamic": true,
    "fields": {
      "plot_embedding": [
        {
          "dimensions": 1536,
          "similarity": "euclidean",
          "type": "knnVector"
        }
      ]
    }
  }
}
```
11. Go to [OpenAI](https://platform.openai.com/settings/profile?tab=api-keys)
12. Create an access token
