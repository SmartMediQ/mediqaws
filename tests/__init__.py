import os, sys
from dotenv import load_dotenv

# Add the parent directory to the sys.path
sys.path.append(os.path.join(
  os.path.dirname(__file__), os.pardir, "src",
))

# Don't write .pyc files
sys.dont_write_bytecode = True

# Define the data directory
data_dir = os.path.join(os.path.dirname(__file__), 'data')
output_dir = os.path.join(os.path.dirname(__file__), 'output')

# Load the .env file
load_dotenv()