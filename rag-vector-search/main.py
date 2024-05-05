import os
from dotenv import load_dotenv
from pymongo import MongoClient
from pymongo.operations import SearchIndexModel
from langchain_openai import OpenAIEmbeddings
from langchain_mongodb import MongoDBAtlasVectorSearch
from langchain_community.document_loaders import DirectoryLoader
from langchain_openai import ChatOpenAI
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain
from langchain import hub

# Load environment variables
load_dotenv()

class RAGVectorSearch:
    def __init__(self, db_key, api_key, path):
        self.set_collection(db_key)
        self.embedding = OpenAIEmbeddings(api_key=api_key)
        self.llm = ChatOpenAI(api_key=api_key)
        self.path = path

    def set_collection(self, db_key: str):
        client = MongoClient(db_key)
        db_name = 'langchain_demo'
        collection_name = 'collection_of_text_blobs'
        self.collection = client[db_name][collection_name]

    def set_documents_data(self, path='./', glob='./*.txt', show_progress=True):
        loader = DirectoryLoader( path, glob=glob, show_progress=show_progress )
        self.data = loader.load()

    # Initialize the vector store
    # Vectorize the data and insert it in the collection
    def insert_embeddings(self):
        if not hasattr(self, 'data'):
            self.set_documents_data(self.path)

        MongoDBAtlasVectorSearch.from_documents(self.data, self.embedding, collection=self.collection)

    def set_vector_store(self):
        self.vector_store = MongoDBAtlasVectorSearch(self.collection, self.embedding, index_name='EmbeddingVectorSearchIndex')

    def set_retriever(self):
        if not hasattr(self, 'vector_store'):
            self.set_vector_store()
        self.retriever = self.vector_store.as_retriever()
        
    def set_retrieval_chain(self):
        retrieval_qa_chat_prompt = hub.pull('langchain-ai/retrieval-qa-chat')
        combine_docs_chain = create_stuff_documents_chain(
            self.llm, retrieval_qa_chat_prompt
        )
        self.retrieval_chain = create_retrieval_chain(self.retriever, combine_docs_chain)

    # Get the most similar document content
    def get_most_similar_doc(self, query: str):
        if not hasattr(self, 'vector_store'):
            self.set_vector_store()

        docs = self.vector_store.similarity_search(query, k=1)
        return docs[0].page_content

    def load_data(self, path=''):
        if path.strip() == '':
            path = self.path

        self.set_documents_data(path)
        self.insert_embeddings()

    # This will be available in a future version of MongoDB
    # Meanwhile, manual creation in the Atlas interface will be required
    def create_search_index(self):
        search_index_model = SearchIndexModel(
            definition={
                "mappings": {
                    "dynamic": True,
                        "fields": {
                            "embedding": {
                                "dimensions": 1536,
                                "similarity": "cosine",
                                "type": "knnVector"
                            }
                        }
                }
            },
            name="EmbeddingVectorSearchIndex",
            type="vectorSearch"
        )
        return self.collection.create_search_index(model=search_index_model)

    def update_vectors(self):
        self.set_vector_store()
        self.set_retriever()
        self.set_retrieval_chain()

    def query_data(self, query: str):
        atlas_answer = self.get_most_similar_doc(query)
        llm_answer = self.retrieval_chain.invoke({'input': query})
        return (atlas_answer, llm_answer['answer'])

    def handle_user_interaction(self):
        while True:
            try:
                query = input('Enter a question based on the documents or press "Ctrl + C" to exit\n')
                answers = self.query_data(query)
                print('\n\n-- Atlas Result:\n', answers[0])
                print('\n\n-- RAG Answer:\n', answers[1], '\n')
            except KeyboardInterrupt:
                print('\nExiting...')
                break

def main():
    db_key  = os.getenv('MONGO_CLIENT')
    api_key = os.getenv('OPENAI_TOKEN')
    path    = os.path.dirname(__file__) + '/sample-files'
    rag_v_search = RAGVectorSearch(db_key, api_key, path)

    while True:
        print('\nMain Menu:')
        print('1. Load Data')
        print('2. Create Search Index (might need manual creation due to MongoDB problems)')
        print('3. Update Vectors')
        print('4. Ask Questions') # Example: Did an error occur on August 16th?
        print('5. Exit')

        try:
            choice = input('\nEnter your choice: ')
        except KeyboardInterrupt:
            print('\nExiting...')
            break

        if choice == '1':
            rag_v_search.load_data()
        elif choice == '2':
            rag_v_search.create_search_index()
        elif choice == '3':
            rag_v_search.update_vectors()
        elif choice == '4':
            rag_v_search.update_vectors()
            rag_v_search.handle_user_interaction()
        elif choice == '5':
            print('Exiting...')
            break
        else:
            print('\nInvalid choice. Please enter a number between 1 and 5.')

if __name__ == '__main__':
    main()
