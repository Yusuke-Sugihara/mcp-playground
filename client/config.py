import os
import json
from dotenv import load_dotenv

load_dotenv()
env = os.getenv

# Model mapping
MODEL_OPTIONS = {
    'OpenAI': 'gpt-4o',
    'Antropic': 'claude-3-5-sonnet-20240620',
    'Google': 'gemini-2.5-flash',
    'Bedrock': 'us.anthropic.claude-3-7-sonnet-20250219-v1:0'
    }

# Streamlit defaults
DEFAULT_MAX_TOKENS = 4096
DEFAULT_TEMPERATURE = 1.0

# API Keys from environment variables
API_KEYS = {
    'OpenAI': env('OPENAI_API_KEY'),
    'Antropic': env('ANTHROPIC_API_KEY') or env('CLAUDE_API_KEY'),
    'Google': env('GOOGLE_API_KEY') or env('GEMINI_API_KEY'),
}

# AWS Credentials for Bedrock
AWS_CREDENTIALS = {
    'region_name': env('AWS_REGION') or env('AWS_DEFAULT_REGION'),
    'aws_access_key': env('AWS_ACCESS_KEY_ID'),
    'aws_secret_key': env('AWS_SECRET_ACCESS_KEY'),
}

# Load server configuration
config_path = os.path.join('.', 'servers_config.json')
if os.path.exists(config_path):
    with open(config_path, 'r') as f:
        SERVER_CONFIG = json.load(f)