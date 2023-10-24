import os
import importlib
import pytest
from unittest.mock import patch

os.environ["PLUTARCH_API_KEY"] = "test_api_key"
import plutarch

def test_create_chat(mocker):
    mock_post = mocker.patch('requests.post')

    plutarch.create_chat()

    mock_post.assert_called_once_with(
        'https://api.plutarch.ai/chat',
        headers={"Authorization": 'test_api_key'},
    )

def test_add_message(mocker):
    mock_post = mocker.patch('requests.post')
    chat = plutarch.Chat("test_chat_id")

    message = {"role": "user", "content": "Hello, world!"}
    chat.add_message(message)

    mock_post.assert_called_once_with(
        'https://api.plutarch.ai/chat/test_chat_id/messages',
        headers={"Authorization": 'test_api_key'},
        json=message,
    )

def test_get_context(mocker):
    mock_post = mocker.patch('requests.post')
    chat = plutarch.Chat("test_chat_id")

    prompt = {"role": "user", "content": "What about next sunday?"}
    chat.get_context(prompt)

    mock_post.assert_called_once_with(
        'https://api.plutarch.ai/chat/test_chat_id/get_context',
        headers={"Authorization": 'test_api_key'},
        json=prompt,
    )

def test_delete_chat(mocker):
    mock_delete = mocker.patch('requests.delete')
    chat = plutarch.Chat("test_chat_id")

    chat.delete()

    mock_delete.assert_called_once_with(
        'https://api.plutarch.ai/chat/test_chat_id',
        headers={"Authorization": 'test_api_key'},
    )