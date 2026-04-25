import argparse
parser = argparse.ArgumentParser(description="Chatbot")
parser.add_argument("user_prompt", type=str, help="Enter prompt here")
args = parser.parse_args()

import os
from dotenv import load_dotenv
load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
if api_key == None:
    raise RuntimeError("Could not find API")


from google import genai

client = genai.Client(api_key=api_key)

def main():
    print("Hello from aiagent!")
    response = client.models.generate_content(
        model = "gemini-2.5-flash", contents = args.user_prompt
    )
    if response.usage_metadata == None:
        raise RuntimeError("failed API request")
    print(
        f"Prompt tokens: {response.usage_metadata.prompt_token_count}\nResponse tokens: {response.usage_metadata.candidates_token_count}"
    )
    
    print(response.text)


if __name__ == "__main__":
    main()
