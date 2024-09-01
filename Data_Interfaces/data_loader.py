from abc import ABC, abstractmethod
from langchain.document_loaders import TextLoader
from langchain.document_loaders.csv_loader import CSVLoader
from langchain.document_loaders import DataFrameLoader
import pandas as pd

"""
In this file Factory Design Pattern is used to make this functionalities more flexible & maintainable.
Currently there are four main file Loaders for PDF, DOCX, CSV, TXT. Each loader has an self.data attribute.
The attribute is none to begin with, when the load_file method is called, self.data is set to the loaded data.
Then the method get_loaded_data can be called to retrieve the loaded data.
If none is returned with get_loaded_data, this means that no data has been loaded - a check is neccessary when using this method

To extend these file types: 
1) Create a new subclass of FileLoader in this file.
2) Implement the load_file method: define the logic to process the file and return the extracted data. Ensure to set self.data to the return val
3) Implemente the get_loaded_data function - simply return self.data
4) Modify the FileLoaderFactory class to include your new subclass setting up the logic based on the input file's file type. 

"""

class FileLoader(ABC):
    """Abstract base class for file loaders."""

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def load_file(self, file_path):
        """Read the file_path and store it in a data loader.
           Store data in class attributte self.data

        Parameters:
        file_path (UploadedFile): path to file to read.

        Returns:
        loaded data

        """
        pass

    @abstractmethod
    def get_loaded_data(self):
        """Returns loaded data that is stores in self.data
        If none returned -> no data has been loaded 
        *check is neccessary when using this method


        Parameters:
        none

        Returns:
        loaded data

        """
        pass


                                ### SUBCLASS IMPLEMENTS ###
class TxtLoader(FileLoader):

    def __init__(self):
        self.data = None


    def load_file(self, file_path):
        """Read the file_path and store it in a data loader.

        Parameters:
        file_path (UploadedFile): path to file to read.

        Returns:
        loaded data

        """

        loader = TextLoader(file_path)
        data = loader.load()

        #remember to save loaded data in self.data
        self.data = data
        return data
    
    def get_loaded_data(self):
        """Returns loaded data that is stores in self.data

        Parameters:
        none

        Returns:
        loaded data

        """
        return self.data

class Python_FileLoader(FileLoader):

    def __init__(self):
        self.data = None

    def load_file(self, file_path):
        """Read the file_path and store it in a data loader.

        Parameters:
        file_path (UploadedFile): path to file to read.

        Returns:
        loaded data

        """

        loader = TextLoader(file_path)
        data = loader.load_and_split()

        #remember to save loaded data in self.data
        self.data = data
        return data
    
    def get_loaded_data(self):
        """Returns loaded data that is stores in self.data

        Parameters:
        none

        Returns:
        loaded data

        """
        return self.data


class CSVLoader(FileLoader):

    def __init__(self):
        self.data = None

    def load_file(self, file_path):
        """Read the file_path and store it in a data loader.

        Parameters:
        file_path (UploadedFile): path to file to read.

        Returns:
        loaded data

        """

        loader = CSVLoader(file_path = file_path)
        data = loader.load()

        #remember to save loaded data in self.data
        self.data = data
        return data
    
    def get_loaded_data(self):
        """Returns loaded data that is stores in self.data

        Parameters:
        none

        Returns:
        loaded data

        """
        return self.data


class PandasLoader(FileLoader):

    def __init__(self):
        self.data = None

    def load_file(self, file_path, page_content_column=None):
        """Read the file_path and store it in a data loader.

        Parameters:
        file_path (UploadedFile): path to file to read.
        page_content_column = optional parameter for how columns should be divided

        Returns:
        loaded data

        """

        df = pd.read_csv(file_path)
        if page_content_column != None:
            loader = DataFrameLoader(df, page_content_column = page_content_column)
        else:
            loader = DataFrameLoader(df)
        data = loader.load()
        
        #remember to save loaded data in self.data
        self.data = data
        return data
    
    def get_loaded_data(self):
        """Returns loaded data that is stores in self.data

        Parameters:
        none

        Returns:
        loaded data

        """
        return self.data

        