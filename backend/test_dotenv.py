import os
from pathlib import Path
from dotenv import load_dotenv

# Print current working directory
print("Current working directory:", os.getcwd())

# Print env file path
env_path = Path(__file__).resolve().parent.parent / ".env"
print("Env file path:", env_path)
print("Env file exists:", env_path.exists())

# Load environment variables
load_dotenv(dotenv_path=env_path)

# Print environment variables
print("MONGODB_URI from os.environ:", os.environ.get("MONGODB_URI"))
print("MONGODB_DB from os.environ:", os.environ.get("MONGODB_DB"))