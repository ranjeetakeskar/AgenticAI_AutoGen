
import asyncio
from autogen_agentchat.messages import MultiModalMessage
from autogen_agentchat.ui import Console
from autogen_core import Image
from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_agentchat.agents import AssistantAgent
from dotenv import load_dotenv
import os


async def main():
    load_dotenv()
    openai_model_client=OpenAIChatCompletionClient(model="gpt-4o-mini")
    assistant=AssistantAgent(name="MultiModalAssistant", model_client= openai_model_client)
    image=Image.from_file(os.path.join(os.getcwd(),"Image.png"))
    multimodal_message= MultiModalMessage(
        content=["What do you see in image?", image], source="user"
    )
    await Console (assistant.run_stream(task=multimodal_message))

asyncio.run(main())