from Agents.agent import AgentInterface
from langchain.chains import ConversationalRetrievalChain
from Data_Interfaces.database import DeepLakeDatabase
"""
This is the Analysis Agent that analyses PYTHON CODE specifically. It is subclass implement of AgentInterface.
but there are some implementation differences with how this agent works listed below:

1. The Deeplake_db is passed into the agent instead of file_path, this assumes you have successfull created a database,
then only can you call the agent. 
2. The runFunction requires chathistory (subclass of Memory Interface) that must be a global object that keep track of the chathistory for this agent specifically
**So the chatHistory class must have an attribute that allows to add the result to it (this will be called in the tool class for the analysis Agent)
3. Query is passed into the run function (this to support the structured tool implementation we are following)

"""

class AnalysisAgent(AgentInterface):

    def _init__(self, name, description):
        self.name = name
        self.description = description
        self.agent = None

    def getAgent(self, llm, DeepLake_db, verbose=False):

        """
        Creates an Analysis Agent

        Parameters:
        LLM: large language model to run agent
        DeepLake_db: give access to database required by the agent 
        verbose = default is False

        returns: the agent
        
        """
        #First get the database
        agent_database = DeepLake_db.get_database()

        #Then get access to the retriever
        retriever = agent_database.as_retreiver()

        #Create and return the agent
        qa = ConversationalRetrievalChain.from_llm(llm,retriever=retriever, verbose = verbose)

        #Set agent attribute
        self.agent = qa
        return qa


    def runFunction(self, query: str, chat_history: list):
        """
        Creates the function to run the agent, therefore does not take in a query
        This is mainly for the tools
        Here self.agent cannot be NoneType otherwise method will raise error

        Parameters: 
        query: question to ask the 
        chat_history: list that has the chat history (this will be accessed by a method of memory object)
        *To be implemented

        returns: running agent function
        """

        #Check that self.agent is not NoneType otherwise raise Error
        if self.agent == None:
            raise NotImplementedError ("Self.agent is NoneType, please call getAgent first")
        
        qa = self.agent
        result = qa({"question": query, "chat_history": chat_history})
        return result
