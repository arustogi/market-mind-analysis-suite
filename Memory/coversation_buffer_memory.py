from Memory.Memory_Interface import *
from langchain.memory import ConversationBufferMemory
class chat_history_list(Memory_Interface):
    """ Instance Class of the Memory Interface, this one is conversation memory buffer
         Intended use for Main Agent """
    
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
        memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
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
        raise NotImplementedError ("Memory does not have add feature")
        
        return
