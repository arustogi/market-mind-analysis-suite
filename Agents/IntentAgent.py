from Agents.agent import AgentInterface
from langchain import LLMChain
from pydantic import BaseModel
from langchain.prompts import PromptTemplate

"""
This is the Intent Agent

SHould just be the human validation tool that cna be addded into any agent
"""

class IntentAgent(AgentInterface):

    def _init__(self, name, description):
        self.name = name
        self.description = description
        self.agent = None

    def getAgent(self, llm, file_path):

        """
        Creates an agent based

        Parameters:
        LLM: large language model to run agent
        file_path: give access to data required by the agent 
        *this varies agent to agent

        returns: the agent
        
        """
        intent_chain = LLMChain(llm=llm, prompt=check_information_prompt)

        pass
    
    def runFunction(self):
        """
        Creates the function to run the agent, therefore does not take in a query
        This is mainly for the tools
        Here self.agent cannot be NoneType otherwise method will raise error

        Parameters: 
        none

        returns: running agent function (not with query, but for tool/another agent to use)
        """
        pass