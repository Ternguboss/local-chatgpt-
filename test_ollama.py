from ollama import chat
from ollama import ChatResponse

response: ChatResponse = chat(
  model='qwen2.5vl:latest',
  messages=[
    {
      'role': 'user',
      'content': 'hello',
    },
  ],
)
print(response.message.content)