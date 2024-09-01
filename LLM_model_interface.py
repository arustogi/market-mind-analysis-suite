from abc import ABC, abstractmethod
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain import HuggingFaceHub



"""
This is the LLM Interface, set up the so each LLM can be accessed independently.

If you meet the need to extend this further by adding a new LLM_model subclass:
1) Create a new subclass of the LLM_Model_Interface
2) Implement the get_model method, each one has some default paramters defined by the abstract class
However, these can be changed/altered and more can be added depending on the LLM 

*Note: In order to get the model the create_model method needs to be called so that the model
can be stored as an attribute.
"""


class LLMModelInterface(ABC):
    """ Abstract class for a LLM Model"""
    model:str
    
    @abstractmethod
    def create_model(self, temperature, API_key, model_name):
        """
        Method to retrurn the LLM

        Parameters:
        temperature: (range 0-1)
        API_key: authentication API key
        model_name: name of the model

        returns: LLM
        """
        pass

    @abstractmethod
    def get_model(self):
        """
        Retrieves model saved in self.model
        Also checks to ensure that self.model is not None

        returns:
        model
        (or error if create_model is not called yet)
        """
        pass


class OpenAI_LLM_Model(LLMModelInterface):
    """ Class for a Open AI LLM Model"""
    def _init_(self):
        self.model = None

    def create_model(self, temperature, API_key, model_name, max_tokens=512):
        """
        Method to retrurn the LLM

        Parameters:
        temperature: (range 0-1)
        API_key: authentication API key
        model_name: name of the model
        max_tokens (optional): OPEN AI specific attribute default is 512

        returns: LLM
        """

        LLM = OpenAI(model_name = model_name, temperature = temperature, 
                    openai_api_key=API_key, max_tokens = max_tokens)
        
        self.model = LLM
        
        return LLM
    
    def get_model(self):
        """
        Retrieves model saved in self.model
        Also checks to ensure that self.model is not None

        returns:
        model
        (or error if create_model is not called yet)
        """

        if self.model == None:
            raise NotImplementedError ("self.model is NoneType, please call create_model first")
        
        return self.model


class ChatOpenAI_LLM_Model(LLMModelInterface):
    """ Class for a Chat Open AI Chat LLM Model"""
    def _init_(self):
        self.model = None

    def create_model(self, temperature, API_key, model_name, max_tokens=512):
        """
        Method to retrurn the LLM

        Parameters:
        temperature: (range 0-1)
        API_key: authentication API key
        model_name: name of the model
        max_tokens (optional): OPEN AI specific attribute default is 512

        returns: LLM
        """

        LLM = ChatOpenAI(model_name = model_name, temperature = temperature, 
                    openai_api_key=API_key, max_tokens = max_tokens)
        
        self.model = LLM

        return LLM
    
    def get_model(self):
        """
        Retrieves model saved in self.model
        Also checks to ensure that self.model is not None

        returns:
        model
        (or error if create_model is not called yet)
        """
        
        if self.model == None:
            raise NotImplementedError ("self.model is NoneType, please call create_model first")
        
        return self.model

class HuggingFaceHub_LLM_Model(LLMModelInterface):
    """ Class for a Chat Open AI Chat LLM Model"""
    def _init_(self):
        self.model = None

    def create_model(self, temperature, API_key, model_name, max_length=64):
        """
        Method to retrurn the LLM
        *get a token, set up API token 

        Parameters:
        temperature: (range 0-1)
        API_key: authentication API key
        model_name: name of the repo id
        max_length (optional): Hugging face specific attribute default is 64

        returns: LLM
        """

        LLM = HuggingFaceHub(repo_id=model_name, 
                             model_kwargs={"temperature": temperature, "max_length": max_length})
        
        self.model = LLM

        return LLM
    
    def get_model(self):
        """
        Retrieves model saved in self.model
        Also checks to ensure that self.model is not None

        returns:
        model
        (or error if create_model is not called yet)
        """
        
        if self.model == None:
            raise NotImplementedError ("self.model is NoneType, please call create_model first")
        
        return self.model