import os
from app.main import app
def test_debig_is_false():
    debug_mode = os.environ.get("DEBUG", "false").lower() in ["true","1","t"]
    assert debug_mode is False