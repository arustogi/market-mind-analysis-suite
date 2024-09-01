from Agents.agent import AgentInterface

from langchain import LLMMathChain



"""
This is the Math Agent

"""

class MathAgent(AgentInterface):

    def __init__(self, name:str, description:str):
        self.name = name
        self.description = description
        self.agent = None

    def getAgent(self, llm):

        """
        Creates a math chain based agent

        Parameters:
        LLM: large language model to run agent

        returns: the math agent
        
        """
        
        math_chain = LLMMathChain.from_llm(llm, verbose=True)
        
        
        self.agent = math_chain

        return math_chain
    
    def runFunction(self, query):
        """
        Creates the function to run the agent, therefore does not take in a query
        This is mainly for the tools
        Here self.agent cannot be NoneType otherwise method will raise error

        Parameters: 
        query: asked by the user

        returns: running agent function (not with query, but for tool/another agent to use)
        """
        answer = self.agent.run(query)
        return answer