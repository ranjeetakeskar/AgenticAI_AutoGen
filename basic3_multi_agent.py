import asyncio

from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.conditions import MaxMessageTermination
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.ui import Console
from dotenv import load_dotenv
from autogen_ext.models.openai import OpenAIChatCompletionClient


async def main():
    load_dotenv()
    openai_model_client=OpenAIChatCompletionClient(model="gpt-4o-mini")
    agent_1 = AssistantAgent(name="MathTeacher",model_client=openai_model_client, 
                        system_message="YOu are math teacher. Explain concepts clearly and ask  follow up questions")

    agent_2 = AssistantAgent(name="Student",model_client=openai_model_client,
                            system_message="You are a curious student. Ask questions and show your thinking process.")

    ## Termination based on max message  ie, after 4
    team = RoundRobinGroupChat(participants=[agent_1, agent_2],
                               termination_condition= MaxMessageTermination(max_messages=4))

    await Console(team.run_stream(task="Lets discuss what is multiplication and how it works"))

    await openai_model_client.close()

asyncio.run(main())