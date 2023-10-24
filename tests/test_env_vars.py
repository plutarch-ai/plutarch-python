import pytest
import os
import importlib

def test_api_key_not_set():
    if "PLUTARCH_API_KEY" in os.environ:
        del os.environ["PLUTARCH_API_KEY"]
    with pytest.raises(ValueError):
        from plutarch import chat
        importlib.reload(chat)
