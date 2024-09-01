
"""
This implementation is a 'hard-coded' version of a sequential chain, where each function will control each one of the three chains


"""
import time
from langchain.vectorstores import Chroma
import os
from langchain.document_loaders import TextLoader
from langchain.document_loaders import DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.document_loaders import TextLoader
from langchain.chains import RetrievalQA
from langchain.document_loaders import TextLoader
from langchain import OpenAI, PromptTemplate

from langchain.embeddings import OpenAIEmbeddings


from Agents.DataAgent import *
from Agents.AnalysisAgent import *
from Agents.IntentAgent import *
from Agents.InsightAgent import *
from Data_Interfaces.database import *
from Agents.SimpleAgent import *
from Memory.chat_history_list import *
from LLM_model_interface import OpenAI_LLM_Model
from langchain.chat_models import ChatOpenAI

API_key = os.environ["OPENAI_API_KEY"] = "Replace with your API key"

state = False
def Intent_Chain(query: str):
    """
    This is the intent agent, it takes query and the LLM through a conversation chain
    gets feedback from the user and verifies the intent of their question

    Parameters:
    query: the question asked by the user

    return:
    (total_context, Memory): tuple
    total_context: str, the clarification context given by the intent agent
    Memory: created by the intent chain and stored as a attribute of the intent chain

    """

    llm = OpenAI(model_name="Replace with your model",
    temperature=0,
    openai_api_key=API_key)

    IntentChain = IntentAgent("Intent agent", "confirms the intent of the user, and gets extra details from them")

    IntentChain.getAgent(llm)

    result = " "

    #The query to be passed onto the other agent with the full context of the conversation
    
    total_context = query
    #'give me a moment' is a phrase that will indicate the agent is done collecting all information
   
    result = IntentChain.runFunction(query)
    st.info(result)
    if "give me a moment" in result.lower():
        print("ENTER")
        


    newquery = st.text_area('Ask Refined Query', key = "newquery")

    if st.button("Submit Query"):
        
        answer = newquery
        st.write(answer.__str__())
    total_context += newquery
    
    #return (total_context, IntentChain.memory)

        #total_context += newquery
        
    print("\n\n got query:" )
    return (total_context, IntentChain.memory)
    
    
    
            

def check_intent_agent(query: str):
    
    """
    This function tries to differentiate whether the query requires the data chain or not.

    It will reply with either "Data Agent required" or "Insight Agent required"
    
    
    
    """

    llm = OpenAI(model_name="Replace with your Model",
    temperature=0,
    openai_api_key=API_key)

    check_intent_chain = ChainVerifierAgent("check_intent agent", "checks whether specific data needs to be extracted, or if just the insight agent is needed")

    check_intent_chain.getAgent(llm)

    result = check_intent_chain.runFunction(query)
    if "data" in result.lower():
        return 'data agent'
    else:
        return 'insight agent'
        

def data_chain(query: str):
    """
    This is the data chain, it takes in a csv file and the user's query, and returns prism scores

    Parameters:
    query: the question asked by the user

    return:
    response (str)
    
    """
    file_path_to_csv = "Replace with your Data CSV File"
    Dataagent = CSVAgent()
    Dataagent._init__("DATA Agent", "This agent has access to csv files with information about securities and their prism scores")
    Dataagent.getAgent(OpenAI(), file_path_to_csv, verbose = True)
    response = Dataagent.agent.run("Here is the security: " + query + " find the (REPLACE WITH DESIRED INFORMATION).")

    return response

def verify_data_chain(information: str):
    """
    This is the verification data chain, verifies whether the information given by the data chain is correct and explains why

    Parameters:
    information: the information given by the data chain

    return:
    Answer (str)
    
    """

    file_path_to_csv = "REPLACE with your csv data"
    agent = CSVAgent()
    agent._init__("DATA Agent", "This agent has access to csv files with information about (Replace with desired information)")
    agent.getAgent(OpenAI(), file_path_to_csv, verbose = True)
    verification_check = agent.agent.run("Here is the information: " + information + " verifiy all the information is correct and matches each other and answer TRUE or FALSE and expalin why")

    return verification_check


def code_agent(response: str, chat_history_obj: chat_history_list):
    """
    This is the code agent chain, for analysing the prism scores based on the code

    Parameters:
    response: returned by the data chain
    chat_history: global memory object created in main function

    return:
    explanation given by the code agent
    
    """

    #Initialize embedings
    embedding = OpenAIEmbeddings()

    #Load the dataset and model
    db_obj = DeepLakeDatabase().__init__()
    db = db_obj.get_database(embedding, "Replace with path to db")
    
    #Get the model
    model = OpenAI(model_name='Replace with model')

    #Create the query and the agent
    analysis_chain = AnalysisAgent()
    analysis_chain.getAgent(model, db, verbose = True)
    query = """Here are the (Replace with Desired Information): """ + response + """
    Explain how to find the relative contribution (%) of each factor using the (Replace with function) to the overall score. Do not calculate"""

    #Run the chain
    result = analysis_chain.runFunction(query, chat_history_obj.memory)

    #Append to chat_history
    chat_history_obj.add_to_memory((query, result["answer"]))


    #print(result['answer'])

    return result['answer']


def insight_chain(query):
   
    insight_chain = InsightAgent("Insight_agent", "Explains different (Desired Information) in an easy to understand format")
    llm = OpenAI(model_name="Replace with model",
            temperature=0,
            openai_api_key=API_key)
    file_path =  'REplace with data path'
    agent = insight_chain.getAgent(llm, file_path)
    return insight_chain.runFunction(query)



def main_run(query):
    return
    

import streamlit as st
from langchain.llms import OpenAI

st.title(" AI FinancialAdvisor")

openai_api_key = "REPLACE with api key"

def generate_response(input_text):
  llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)
  st.info(llm(input_text))


text = st.text_area('Enter text:', 'What can we help you with?')
submitted = st.button('Submit')
if submitted and openai_api_key.startswith('sk-'):
    main_run(text)