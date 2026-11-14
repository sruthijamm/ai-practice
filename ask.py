from dotenv import load_dotenv
from anthropic import Anthropic
from tools import tools, get_package_price

load_dotenv()
client = Anthropic()

messages = [{"role": "user", "content": "How much is the mini package?"}]

response = client.messages.create(
    model="claude-haiku-5-5",
    max_tokens=500,
    tools=tools,
    messages=messages,
)

results = []
for block in response.content:
    if block.type == "tool_use":
        answer = get_package_price(block.input["package_name"])
        results.append(
            {"type": "tool_result", "tool_use_id": block.id, "content": answer}
        )

messages.append({"role": "assistant", "content": response.content})
messages.append({"role": "user", "content": results})

final = client.messages.create(
    model="claude-haiku-5-5",
    max_tokens=500,
    tools=tools,
    messages=messages,
)
print(final.content[0].text)