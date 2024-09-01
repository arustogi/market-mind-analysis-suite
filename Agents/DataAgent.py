from Agents.agent import AgentInterface
from langchain.agents import create_csv_agent
from langchain.agents.agent_types import AgentType

class CSVAgent(AgentInterface):
    """SubClass of AgentInterface, implementation of csv agent."""

    def _init__(self, name, description):
        self.name = name
        self.description = description
        self.agent = None

    
    def getAgent(self, llm, file_path: str, verbose = False):

        """
        Creates a csv agent

        Parameters:
        LLM: large language model to run agent (not the class but the actual model)
        file_path: access to data required by the agent - this must be a csv file
        verbose (optional): default is set to False

        returns: csv agent
        
        """

        #Specify agent_type as ZERO_SHOT_REACT_DESCRIPTION, and this parameter is curently not changeable (for consistency reasons)
        csv_agent = create_csv_agent(llm, file_path, verbose=verbose, agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION)

        #Set agent attribute
        self.agent = csv_agent
        return csv_agent


    def runFunction(self):
        """
        Creates the function to run the agent, therefore does not take in a query
        This is mainly for the tools
        Here self.agent cannot be none otherwise method will raise error

        Parameters: 
        none

        returns: running agent function (not with query, but for tool/another agent to use)
        """

        #Check that self.agent is not NoneType otherwise raise Error
        if self.agent == None:
            raise NotImplementedError ("Self.agent is NoneType, please call getAgent first")
        
        return self.agent.run


