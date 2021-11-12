# ficture for all tests
import pytest
from dotenv import load_dotenv

# load environment variables
@pytest.fixture(scope='module', autouse=True)
def load_env():
    load_dotenv()
