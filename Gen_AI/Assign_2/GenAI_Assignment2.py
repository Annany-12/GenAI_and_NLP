from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

while True:
    prompt = str(input("User > "))
    if prompt == 'exit':
        break
    result = model.invoke(prompt)
    print(f"AI > {result.content}")
