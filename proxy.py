import os
import subprocess
from dotenv import load_dotenv

def main():
    # Load environment variables from .env file
    env_path = os.path.join(os.path.dirname(__file__), '.env')
    load_dotenv(env_path)

    # Ensure UTF-8 is preferred
    os.environ['PYTHONUTF8'] = '1'

    # Build the LiteLLM CLI command
    config_path = os.path.join(os.path.dirname(__file__), 'config.yaml')
    cmd = [
        'litellm',
        '--config', config_path,
        '--port', '4000',
        '--host', '0.0.0.0',
        '--debug'
    ]

    print(f"Starting LiteLLM proxy with config: {config_path}")
    print(f"Loaded .env from: {env_path}")

    # Run the command
    try:
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Proxy failed with error: {e}")
    except KeyboardInterrupt:
        print("\nProxy stopped by user")

if __name__ == "__main__":
    main()