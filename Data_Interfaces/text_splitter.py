from abc import ABC, abstractmethod
from langchain.text_splitter import CharacterTextSplitter
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.text_splitter import (
    RecursiveCharacterTextSplitter,
    Language,
)

"""
In this file _______________ is used to make this functionalities more flexible & maintainable.
Currently there are two ways to split the documents, character and text.

If you met the need to extend this further by adding a new splitter subclass:
1) Create a new subclass of Splitter in this file.
2) Implement the split_text method: Define the logic to split the text into chunks according to the desired strategy.
4) Optionally, implement any additional methods specific to your text processing strategy. 

"""

class Splitter(ABC):
    """ Abstract class for splitting data """

    @abstractmethod
    def split_text(self, data, chunk_size, chunk_overalap):
        """Splits the loaded data so that it can be embedded.

        Parameters:
        chunk_size: size of each chunk (i.e. 1000)
        chunk_overlap: how much overlap chunks should have (0)
        data: this is the data you want to split

        Returns:
        splitted texts/documents

        """
        pass

class Split_Character_Data(Splitter):

    def split_text(self, data, chunk_size=1000, chunk_overlap=0):
        """Splits the loaded data by characters to be embedded.

        Parameters:
        data: this is the data you want to split
        chunk_size (optional): size of each chunk (i.e. 1000)
        chunk_overlap(optional): how much overlap chunks should have (0)

        Returns:
        splitted texts/documents
        """

        text_splitter = CharacterTextSplitter(chunk_size, chunk_overlap)

        #This method is split_documents but it can also be split_text
        docs = text_splitter.split_documents(data)
        return docs


class Split_Python_Code(Splitter):


    def split_text(self, data, chunk_size=50, chunk_overlap=0):

        """Splits the loaded code by characters to be embedded.

        Parameters:
        data: this is the python code that needs to be split
        chunk_size (optional): size of each chunk (default = 50)
        chunk_overlap(optional): how much overlap chunks should have (default = 0)

        Returns:
        splitted python code documents 
        """
        
        
        python_splitter = RecursiveCharacterTextSplitter.from_language(
        language=Language.PYTHON, chunk_size=chunk_size,
        chunk_overlap=chunk_overlap)

        python_docs = python_splitter.create_documents(data)
        return python_docs


class Split_Recursive_Character_Data(Splitter):

    def split_text(self, data, chunk_size=1000, chunk_overlap=0):

        """Splits the loaded data by characters to be embedded.

        Parameters:
        data: this is the data you want to split
        chunk_size (optional): size of each chunk (i.e. 1000)
        chunk_overlap(optional): how much overlap chunks should have (0)

        Returns:
        splitted texts/documents
        """

        text_splitter = RecursiveCharacterTextSplitter(chunk_size, chunk_overlap)

        #This method is split_documents but it can also be split_text
        docs = text_splitter.split_documents(data)
        return docs



