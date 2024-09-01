from Agents.AnalysisAgent import *
from Agents.DataAgent import *
from Agents.InsightAgent import *
from Agents.IntentAgent import *
from Agents.VerificationAgent import *
from Data_Interfaces.data_loader import *
from Data_Interfaces.database import *
from Data_Interfaces.text_splitter import *

from Tools.AnalysisTool import *
from Tools.DataTool import *
from Tools.VerificationTool import *
from Tools.InsightTool import *
from Tools.InsightTool import *

from Memory.chat_history_list import *
from LLM_model_interface import *

import os

from langchain.memory import ConversationBufferMemory
from langchain.agents import initialize_agent

# This is the main python script
API_key = os.environ["OPENAI_API_KEY"] = " REPLACE"

#1. Create the LLM

ChatOpenAI_LLM = ChatOpenAI_LLM_Model().create_model(0, API_key, "REPLACE")
OpenAI_LLM = OpenAI_LLM_Model().create_model(0, API_key, "REPLACE")

#3. Create the memory objects
chat_history = chat_history_list.create_memory()
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)


#2. Create the Tools
#create Data tool
file_path_to_deeplake_db = ""
file_path_to_csv = ""
code_reading_agent = AnalysisTool().createTool(ChatOpenAI_LLM, file_path_to_deeplake_db)
csv_agent = DataTool().createTool(ChatOpenAI_LLM, file_path_to_csv)
#create Insight Tool
file_path_to_insightdocs =""
insight_loader = TxtLoader()
vectordb = insight_loader.load_file(file_path_to_insightdocs)


Main_Agent_prompt_template = """You are a financial expert specializing in risk management for investment portfolios.

The main objective of the user is to (Replace).
if you don't know the answer, tell the user you don't know the answer. Do not make stuff up!

Your goal is to answer the question the user asks in detail.

Question: {query}

You have a set of tools at your disposal and must choose the relevant tools for each question. You cannot make any assumptions and must use the tools and assocaited files for any information.
{tools}

Follow these steps exactly for your answer:
(REPLACE)

Thought:{agent_scratchpad}

"""

prompt_template = PromptTemplate(
    input_variables=["query", "tools", "agent_scratchpad"],
    template=Main_Agent_prompt_template
)