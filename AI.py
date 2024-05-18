from langchain.prompts import ChatPromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.schema.output_parser import StrOutputParser
from langchain.agents import AgentType, initialize_agent, load_tools
from langchain.agents import load_tools
from langchain.utilities import OpenWeatherMapAPIWrapper
from decouple import config
import os 

os.environ["OPENAI_API_KEY"] = config("OPENAI_API_KEY")

os.environ["OPENWEATHERMAP_API_KEY"] = config("OPENWEATHERMAP_API_KEY")


model=ChatOpenAI()

weather = OpenWeatherMapAPIWrapper()
tools = load_tools(["openweathermap-api"], model)

prompt = ChatPromptTemplate.from_template(
    '''Your are a very friendly and charming AI assistant. Help ar the user questions in a friendly and funny tone. Use the your response should be in the language specified. Below a you 
    should demostrate in your response
    human:{question}
    context:{context}

''' )

chain=initialize_agent(
    tools=tools, llm=model, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True,handle_parsing_errors=True
)



def generate_response(prompt):

    try:
        return chain.run(input=prompt)


        
    except Exception as e:
        print("error:{e}")



