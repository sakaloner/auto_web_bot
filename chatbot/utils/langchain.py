#conversational-react-description agent type, which expects to be used with a memory component.

"""You must ask the following questions to the user and:
- What's the name of your company?
- Please enter your company logo
- What products/services do you offer?"""


import os
from langchain.agents import Tool, AgentType, initialize_agent 
from langchain.memory import ConversationBufferMemory
from langchain import OpenAI
from langchain.utilities import SerpAPIWrapper
from langchain.prompts import  (
    SystemMessagePromptTemplateChatPromptTemplate,
    PromptTemplate,
    SystemMessagePromptTemplate,
    AIMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)

os.environ["OPENAI_API_KEY"] = "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"
os.environ["SERPAPI_API_KEY"] = "218d14c3ee3ad7ab734199d125889b23a0acdf5144feaf540abdfa4a22ed3e65"


search = SerpAPIWrapper()
tools = [
    Tool(
        name = "Current Search",
        func=search.run,
        description="useful for when you need to answer questions about current events or the current state of the world"
    ),
]

template = """You are a requirements elicitation chatbot for a webpage maker. You have access to the following tools:
{tools}"""
system_message_prompt = SystemMessagePromptTemplate.from_template(template)



memory = ConversationBufferMemory(memory_key="chat_history")

llm=OpenAI(temperature=0)
agent_chain = initialize_agent(tools, llm, agent=AgentType.CONVERSATIONAL_REACT_DESCRIPTION, verbose=True, memory=memory, template=template)


#print(agent_chain.run(input="what's my name?"))
#print(agent_chain.run("what is the temperature in °C right now in Medellín, Colombia ?"))


count = 0
while True:
  if count == 0:
    print("Hello i am an AI assistant here to help you create a beutiful webpage. How can i start helping you today?")
  user_input = input()
  bot_res = print(agent_chain.run(input=user_input))
  print(bot_res)
  count += 1