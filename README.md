# Plutarch

A client library for the Plutarch API.

## Installation
pip install plutarch
export PLUTARCH_API_KEY=your-api-key

## Usage
import plutarch

chat = plutarch.create_chat()

chat.add_message({"role": "user", "content": "What's the weather today?"})
chat.add_message({"role": "assistant", "content": "Where are you located?"})
chat.add_message({"role": "user", "content": "I'm in Paris"})
chat.add_message({"role": "assistant", "content": "Today we expect clear skyes with highs of 22c and lows of 15c"})

context = chat.get_context({"role": "user", "content": "What about next sunday?"})
print(context)