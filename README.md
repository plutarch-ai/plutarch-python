# Plutarch

A client library for the Plutarch API.

## Installation
```
pip install plutarch
export PLUTARCH_API_KEY=your-api-key
```

## Usage
```
import plutarch


# Create a new chat
chat = plutarch.create_chat()

chat.id
> "5f6b3b6b-3b6b-4b6b-8b6b-6b3b6b3b6b3b"

# Add some messages
chat.add_message({"role": "user", "content": "What's the weather today?"})
chat.add_message({"role": "assistant", "content": "Where are you located?"})
chat.add_message({"role": "user", "content": "I'm in Paris"})
chat.add_message({"role": "assistant", "content": "Today we expect clear skyes with highs of 22c and lows of 15c"})

# Get context for next user prompt
context = chat.get_context({"role": "user", "prompt": "What about next sunday?"})
print(context)

# Delete chat with all its messages from Plutarch
chat.delete()

# Load chat
chat = plutarch.load_chat("5f6b3b6b-3b6b-4b6b-8b6b-6b3b6b3b6b3b")
```