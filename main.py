# @hdawgofficial on X

import config

# Added default OpenAI testing prompts
from openai import OpenAI

client = OpenAI(
    api_key= config.openAPI
)

completion = client.chat.completions.create(
  model="gpt-4o-mini",
  store=True,
  messages=[
    {"role": "user", "content": "write a haiku about ai"}
  ]
)

print(completion.choices[0].message)


# Adding API Key and environment configuration to LangSmith
LANGSMITH_TRACING= True
LANGSMITH_ENDPOINT="https://api.smith.langchain.com"
LANGSMITH_API_KEY= config.langAPI
LANGSMITH_PROJECT="first_chatbot"
OPENAI_API_KEY= config.openAPI

from langchain_openai import ChatOpenAI

llm = ChatOpenAI()
llm.invoke("Hello, world!")