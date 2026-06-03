import asyncio
from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.ui import Console
from autogen_ext.models.openai import OpenAIChatCompletionClient
from dotenv import load_dotenv

async def main():
    load_dotenv()
    openai_model_client=OpenAIChatCompletionClient(model="gpt-4o-mini")
    assistant=AssistantAgent(name="assistant", model_client= openai_model_client)
    await Console(assistant.run_stream(task="What is 25^3*5?"))
    await openai_model_client.close()


asyncio.run(main())