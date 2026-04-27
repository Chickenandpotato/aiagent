import argparse
import os


from dotenv import load_dotenv
from google import genai
from google.genai import types
from prompts import system_prompt
from functions.call_function import available_functions


def build_parser():
    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="Enter prompt here")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    return parser



def main():
    
    parser = build_parser()
    args = parser.parse_args()
    
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    if api_key == None:
        raise RuntimeError("Could not find API")
    
    client = genai.Client(api_key=api_key)
    messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]
    generate_content(client, messages, args.verbose)
    
    
    
    
def generate_content(client, messages, verbose):
    response = client.models.generate_content(
        model = "gemini-2.5-flash",
        contents = messages,
        config=types.GenerateContentConfig(
            tools=[available_functions],
            system_instruction=system_prompt,
            temperature=0)
    )
    if response.usage_metadata == None:
        raise RuntimeError("failed API request")
    
    if verbose:
        print(
            f"User prompt: {messages[0].parts[0].text}\nPrompt tokens: {response.usage_metadata.prompt_token_count}\nResponse tokens: {response.usage_metadata.candidates_token_count}"
    )
    function_calls = response.function_calls
    if function_calls:
        for function_call in function_calls:
            print(f"Calling function: {function_call.name}({function_call.args})")
    else:
        print(response.text)



if __name__ == "__main__":
    main()
