from Memory.Memory_Interface import *
from langchain.prompts import MessagesPlaceholder
class chat_history_list(Memory_Interface):
    """ Instance Class of the Memory Interface, this one is chat_history as a list
         Intended use for Analysis Agent """
    
    def _init_(self, name, type):
        self.name = name
        self.type = type
        self.memory = None

    def create_memory(self):
        """
        Method to create the memory and store it in self.memory

        parameters:
        None

        returns: memory
        
        """
        memory = MessagesPlaceholder(variable_name="chat_history")
        self.memory = memory
        return memory
    
    def get_memory(self):
        """
        Method to retrieve memory from memory object
        Also checks to ensure memory is not None

        paramters:
        None

        returns: memory
        
        """
        if self.memory == None:
            raise NotImplementedError ("Memory is NoneType, please call create_memory first")
        return self.memory

    def add_to_memory(self, chat):

        """
        Method to add to memory
        Also checks to ensure memory is not None
        
        paramters:
        chat: Tuple in the following form -> (query, result['answer']

        returns: None

        """
        if self.memory == None:
            raise NotImplementedError ("Memory is NoneType, please call create_memory first")
        
        self.memory.append(chat)
        return
