from Agents.agent import AgentInterface
from langchain.chains import RetrievalQA
from langchain.memory import ConversationBufferMemory
from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI

class InsightAgent(AgentInterface):
    #after merging, add database, text, and retriever code
    template = """
                Use the following context (delimited by <ctx></ctx>) and the chat history (delimited by <hs></hs>) to answer the question (If you don't know the answer, just say that you don't know, don't try to make up an answer.):
                ------
                <ctx>
                {context}
                </ctx>
                ------
                <hs>
                {history}
                </hs>
                ------
                {question}
                Answer:
                """
    def get_prompt(self):
        prompt = PromptTemplate(
            input_variables=["history", "context", "question"],
            template= self.template,
        )
        return prompt
    
    
    def get_agent(self):
        qa_chain = RetrievalQA.from_chain_type(llm=OpenAI(), 
                                        chain_type="stuff", 
                                        retriever=retriever, 
                                        return_source_documents=True,
                                        chain_type_kwargs={
                                            "verbose": True,
                                            "prompt" : self.get_prompt(),
                                            "memory": ConversationBufferMemory(
                                                memory_key="history",
                                                input_key="question"),
                                                            }
            )
        return qa_chain
    
    def process_llm_response(llm_response):
        print(llm_response['result'])
        print('\n\nSources:')
        for source in llm_response["source_documents"]:
            print(source.metadata['source'])
    
    
    
    def run(self,query:str):
        agent =  self.get_agent()
        response = agent(query)
        return response['result']