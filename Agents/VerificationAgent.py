from Agents.agent import AgentInterface

class VerificationAgent(AgentInterface):
    def _init__(self, name, description):
        self.name = name
        self.description = description
        self.agent = None
    
    def getAgent(self, llm, file_path):
        """
        Creates an Verification Agent

        Parameters:
        LLM: large language model to run agent (the actual model not the class)
        file_path: there is no database, but instead it is a prompt

        returns: the agent
        
        """
        return
    
    def runFunction(self, query: str, example_answer: str):
        """
        Creates the function to run the agent, therefore does not take in a query
        This is mainly for the tools
        Here self.agent cannot be NoneType otherwise method will raise error

        Parameters: 
        query: question to ask the 
        *To be implemented

        returns: running agent function
        """
        return 

