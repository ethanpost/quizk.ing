#!/usr/bin/env python3


"""
Example:

```
python together_ai_call.py --api-key "xxxxxxxxxxxxxxxxx" --model "mistralai/Mixtral-8x7B-Instruct-v0.1" --temperature 0.7 --system "You are a helpful assistant." 
"What is the capital of France?" 
```

You can also load a system prompt from a file:
```
python together_ai_call.py --system-file path/to/system_prompt.txt "What is the capital of France?"
```

API key can be provided:
1. Via --api-key command line argument
2. Via TOGETHER_API_KEY environment variable
3. In a file named together_api.secret in the current directory

"""

import requests
import json
import os
import argparse
import sys
from typing import List, Dict, Any, Optional

class TogetherAI:
    """
    Client for interacting with Together.ai's API to generate chat completions.
    """
    
    def __init__(self, api_key: Optional[str] = None):
        """
        Initialize the Together.ai client.
        
        Args:
            api_key: The API key for Together.ai. If not provided, will look for 
                     TOGETHER_API_KEY environment variable or together_api.secret file.
        """
        # Try to get API key from command line argument
        self.api_key = api_key
        
        # If not provided, try environment variable
        if not self.api_key:
            self.api_key = os.environ.get("TOGETHER_API_KEY")
            
        # If still not found, try to read from secret file
        if not self.api_key and os.path.exists("together_api.secret"):
            try:
                with open("together_api.secret", 'r') as f:
                    self.api_key = f.read().strip()
            except Exception as e:
                print(f"Error reading API key from together_api.secret: {e}", file=sys.stderr)
        
        # If we still don't have the API key, raise an error
        if not self.api_key:
            raise ValueError(
                "API key must be provided via --api-key argument, TOGETHER_API_KEY environment variable, "
                "or together_api.secret file in the current directory"
            )
        
        self.base_url = "https://api.together.xyz/v1/chat/completions"
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
    
    def generate_chat_completion(
        self,
        messages: List[Dict[str, str]],
        model: str = "mistralai/Mixtral-8x7B-Instruct-v0.1",
        temperature: float = 0.7,
        max_tokens: int = 1024,
        stream: bool = False
    ) -> Dict[str, Any]:
        """
        Generate a chat completion using the Together.ai API.
        
        Args:
            messages: List of message dictionaries with 'role' and 'content' keys
            model: The model to use for generation
            temperature: Controls randomness, higher is more random (0-2)
            max_tokens: Maximum number of tokens to generate
            stream: Whether to stream the response
            
        Returns:
            The API response as a dictionary
        """
        payload = {
            "model": model,
            "messages": messages,
            "temperature": temperature,
            "max_tokens": max_tokens,
            "stream": stream
        }
        
        try:
            response = requests.post(
                self.base_url,
                headers=self.headers,
                json=payload
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error making request to Together.ai API: {e}", file=sys.stderr)
            if hasattr(e, 'response') and e.response:
                print(f"Response content: {e.response.text}", file=sys.stderr)
            sys.exit(1)

def parse_arguments():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description="Call Together.ai API for chat completions")
    
    parser.add_argument("--api-key", help="Together.ai API key (or set TOGETHER_API_KEY env var)")
    parser.add_argument("--model", default="mistralai/Mixtral-8x7B-Instruct-v0.1", 
                        help="Model to use for generation")
    parser.add_argument("--temperature", type=float, default=0.7, 
                        help="Temperature for generation (0-2)")
    parser.add_argument("--max-tokens", type=int, default=1024, 
                        help="Maximum tokens to generate")
    parser.add_argument("--system", 
                        help="System message for the chat")
    parser.add_argument("--system-file",
                        help="File containing the system message")
    parser.add_argument("--prompt-file",
                        help="File containing the user prompt")
    parser.add_argument("--output-file",
                        help="File to write the response to (fails if file exists)")
    parser.add_argument("prompt", nargs="?", 
                        help="User prompt (if not provided, will read from stdin or --prompt-file)")
    
    return parser.parse_args()

def main():
    args = parse_arguments()
    
    # Check if output file exists
    if args.output_file and os.path.exists(args.output_file):
        print(f"Error: Output file '{args.output_file}' already exists. Will not overwrite.", file=sys.stderr)
        sys.exit(1)
    
    # Get prompt from argument, file, or stdin
    if args.prompt:
        prompt_text = args.prompt
    elif args.prompt_file:
        try:
            with open(args.prompt_file, 'r', encoding='utf-8') as f:
                prompt_text = f.read().strip()
            if not prompt_text:
                print("Error: Prompt file is empty", file=sys.stderr)
                sys.exit(1)
        except Exception as e:
            print(f"Error reading prompt file: {e}", file=sys.stderr)
            sys.exit(1)
    else:
        # Read from stdin if no prompt or prompt file provided
        prompt_text = sys.stdin.read().strip()
        if not prompt_text:
            print("Error: No prompt provided either as argument, file, or via stdin", file=sys.stderr)
            sys.exit(1)
    
    # Initialize messages
    messages = []
    
    # Handle system message (prioritize direct system message over file)
    if args.system:
        system_content = args.system
    elif args.system_file:
        try:
            with open(args.system_file, 'r', encoding='utf-8') as f:
                system_content = f.read().strip()
        except Exception as e:
            print(f"Error reading system prompt file: {e}", file=sys.stderr)
            sys.exit(1)
    else:
        system_content = None
    
    # Add system message if available
    if system_content:
        messages.append({"role": "system", "content": system_content})
    
    # Add user message
    messages.append({"role": "user", "content": prompt_text})
    
    # Initialize client and call API
    client = TogetherAI(api_key=args.api_key)
    response = client.generate_chat_completion(
        messages=messages,
        model=args.model,
        temperature=args.temperature,
        max_tokens=args.max_tokens
    )
    
    # Extract the assistant's response
    try:
        assistant_message = response["choices"][0]["message"]["content"]
        
        # Write to output file if specified
        if args.output_file:
            try:
                with open(args.output_file, 'w', encoding='utf-8') as f:
                    f.write(assistant_message)
                print(f"Response written to '{args.output_file}'")
            except Exception as e:
                print(f"Error writing to output file: {e}", file=sys.stderr)
                # Still print the response to stdout if file write fails
                print(assistant_message)
                sys.exit(1)
        else:
            # Print to stdout if no output file
            print(assistant_message)
            
    except (KeyError, IndexError) as e:
        print(f"Error parsing API response: {e}", file=sys.stderr)
        print(f"Full response: {json.dumps(response, indent=2)}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()



