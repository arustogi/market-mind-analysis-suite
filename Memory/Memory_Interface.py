from abc import ABC, abstractmethod

"""
In this file is the Memory Interface.

If you met the need to extend this further by adding a new Memory_Interface subclass:
1) Create a new file and a new subclass of Memory_Interface
2) Implement the create_memory, get_memory method and add_to_memory method adding any extra paramters needed
3) Optionally, implement any additional methods specific to your ensure your memory functions properly

Note: To create a new instance of any subclass you must supply name and type for the memory.
Type refers to which agen the memory is for, whether it is a global agent or not

"""

class Memory_Interface(ABC):
    """ Abstract Class for the Memory Interface """
    name: str
    #Type refers to which agent this memory is for
    type: str 

    def create_memory(self):
        """
        Method to create the memory and store it in self.memory
        
        """
        pass
    def get_memory(self):
        """
        Method to retrieve memory from memory object
        
        """
        pass

    def add_to_memory(self):

        """
        Method to add to memory 

        """
        pass
