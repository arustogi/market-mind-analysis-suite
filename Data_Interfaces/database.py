from abc import ABC, abstractmethod
from langchain.vectorstores import DeepLake
from langchain.vectorstores import FAISS
from langchain.vectorstores import Chroma
from langchain.embeddings.openai import OpenAIEmbeddings

"""
In this file ____ is used to make this functionalities more flexible & maintainable.
Databases or vectorstores are ways to embed the data, both will need retriever methods that can be used in the agents.
Databases may require additional authentication. Class has a self.database attribute that will store the database for access.

If you meet the need to extend this further by adding a new Database subclass:
1) Create a new subclass of Database or Vectorstore in this file.
2) Implement the create_database method: Define how you want to create the database, using preferred library from the docs and embeddings
3) Alternatively, implement the create_vectorstore method: Define how to create vectorstores or other representations from the text chunks.
4) return self.database in the get_database method (or optionally your own implementation of how to get database without loading data everytime)
5) Optionally, implement any additional methods specific to database/vectorstore creating strategy. 

"""


class Database(ABC):
    """ Abstract class for creating a database """

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def create_database(self, docs, embeddings, dataset_path):
        """"
        Creates a databse using the docs and embeddings, and add documents to the database.
        Optionally may need to add in username or some authentication in the environment file.
        
        Parameters:
        docs: documents that need to be embedded
        embeddings (depending on model): embeddings to be used to create the vectorstore
        dataset_path: Path to the database (online/local) where data will be stored

        Returns:
        loaded database
        """
        pass

    @abstractmethod
    def get_database(self):
        """"
        Returns database that is stores in self.database.
        Implemented to data does not need to be loaded everytime it needs to be accessed

        Parameters:
        none

        Returns:
        loaded database

        """
        pass


class DeepLakeDatabase(Database):

    def __init__(self, database):
        self.database = None

    def create_database(self, docs, embeddings, dataset_path):
        """"
        Creates a database using the docs and embeddings, and add documents to the database.
        Optionally may need to add in username or some authentication in the environment file.
        
        Parameters:
        docs: documents that need to be embedded
        embeddings (depending on model): embeddings to be used to create the vectorstore
        dataset_path: Path to the database (online/local) where data will be stored
            **Here dataset_path must include username and must be a f'string

        Returns:
        loaded database
        """
        
        db = DeepLake(dataset_path=dataset_path, embedding_function=embeddings)
        db.add_documents(docs)

        #Store database in class attribute
        self.database = db
        return db
    
    def get_database(self):
        """"
        Returns database that is stores in self.database

        Parameters:
        none

        Returns:
        loaded database
        """
        return self.database
    


class Vectorstore(ABC):

    """ Abstract class for creating a vectorstore """

    def __init__(self):
        self.database = None

    @abstractmethod
    def create_vectorstore(self, docs, embeddings):
        """Uses embeddings and docs to create a vectorstore.

        Parameters:
        docs: documents that need to be embedded
        embeddings (depending on ): embeddings to be used to create the vectorstore

        Returns:
        vectorstore

        """
        pass

    @abstractmethod
    def get_vectorstore(self):
        """"
        Returns vectorstore that is stores in self.vectorstore

        Parameters:
        none

        Returns:
        loaded database

        """
        pass