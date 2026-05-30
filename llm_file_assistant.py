import os
from google import genai
from google.genai import types
import fs_tools

# 1. Initialize the Gemini client
client = genai.Client()

# 2. Provide the list of Python functions as tools
my_tools = [
    fs_tools.list_files,
    fs_tools.read_file,
    fs_tools.write_file,
    fs_tools.search_in_file
]

def run_assistant(user_prompt: str):
    # Define system instructions to guide the agent's behavior
    config = types.GenerateContentConfig(
        system_instruction=(
            "You are an advanced File System Assistant. Use the provided tools to "
            "interact with local files. Always rely on tool outputs rather than guessing. "
            "If a tool returns an error, communicate that to the user."
        ),
        tools=my_tools,
        temperature=0.2
    )
    
    try:
        # Create a multi-turn chat session so the loop handles tool calls automatically
        chat = client.chats.create(model="gemini-2.5-flash", config=config)
        response = chat.send_message(user_prompt)
        print(f"\n[Assistant]:\n{response.text}\n")
        
    except Exception as e:
        print(f"\n[Error]: An error occurred: {str(e)}\n")

if __name__ == "__main__":
    print("====================================================")
    print("🤖 Gemini File System Assistant Initialized!")
    print("Type your query below (or type 'exit' or 'quit' to stop).")
    print("====================================================\n")
    
    while True:
        # Prompt the user for input
        user_query = input("You: ").strip()
        
        # Check for break conditions
        if not user_query:
            continue
        if user_query.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break
            
        # Run the agent with the user's input
        run_assistant(user_query)