
# Simple Reflex agent
# Perceives: User input through the console

# Processes: Uses the Groq language model

# Acts: Generates and streams responses back to the user

from agno.agent import Agent # agent 
from agno.models.groq import Groq # LLm
from dotenv import load_dotenv
load_dotenv()
# Create your Agent
agent = Agent(
    model=Groq(id="llama-3.3-70b-versatile"),
    instructions="You are a helpful AI assistant.", # system prompt
    markdown=True, # beautiful markdown style chat interface
    debug_mode=True, # it will give us all the details of what agent has done while processing oour query 
    
)

# Run
while True:
    user_input=input("Ask from AI :")
    if user_input.lower()=='exit':
        break
    agent.print_response(user_input, stream=True)