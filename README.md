# Plutarch

A client library for the Plutarch API.

Sign up for an API key and 1M free tokens per month at https://www.plutarch.api

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
> '30d201cb-9e49-49ab-abfc-f8c66a118b42'

# Add some messages
chat.add_message({"role": "user", "content": "What's the weather today?"})
chat.add_message({"role": "assistant", "content": "Where are you located?"})
chat.add_message({"role": "user", "content": "I'm in Paris"})
chat.add_message({"role": "assistant", "content": "Today we expect clear skies with highs of 22c and lows of 15c"})

# Get context for next user prompt
chat.get_context({"role": "user", "prompt": "What about next Sunday?"})
> {'chat_id': '30d201cb-9e49-49ab-abfc-f8c66a118b42', 'prompt': 'What about next Sunday?', 'context': 'The user is asking about the weather for next Sunday.'}

# Delete chat with all its messages from Plutarch
chat.delete()

# Load chat
chat = plutarch.load_chat("5f6b3b6b-3b6b-4b6b-8b6b-6b3b6b3b6b3b")
```