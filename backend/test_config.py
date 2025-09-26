import os
import sys
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from .env file
env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(dotenv_path=env_path)

print("MONGODB_URI in os.environ:", "MONGODB_URI" in os.environ)
if "MONGODB_URI" in os.environ:
    print("MONGODB_URI value:", os.environ["MONGODB_URI"])

# Add the parent directory to the path
sys.path.append(str(Path(__file__).parent))

from app.core.config import settings

print("MONGODB_URI from settings:", settings.MONGODB_URI)
print("MONGODB_DB from settings:", settings.MONGODB_DB)
print("Current working directory:", os.getcwd())
print("Env file path:", Path(__file__).resolve().parent.parent / ".env")