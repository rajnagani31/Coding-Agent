from google import genai 
from dotenv import load_dotenv
import os,json
import subprocess

load_dotenv()
client=genai.Client()
# api_key=os.getenv("GEMINI_API_KEY")

def run_command(cmd: str):
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    return result.stdout + ("\nError:\n" + result.stderr if result.stderr else "")

available_tools = {

    "run_command":run_command,
}
SYSTEM_PROMPT="""
        you are a helpfull AI coding Agent.

        Goal:user ask a any qestion about coding fiie creattion,creat a coding fille ,creat folder ,creat HTML,CSS,JS,Node.js,
        python,django,strimlight etc coding file you are capebul for creat ok.
         Output JSON Format:
                {{
                    "step": "string",
                    "content": "string",
                    "function": "The name of function if the step is action",
                    "input": "The input parameter for the function",
                }}
        
        available tools:
        -"run_command": Takes windows command as a string and executes the command and returns the output after executing it.

"""
query=input(">>")
prompt=f"""
{SYSTEM_PROMPT}
{query}
"""
while True:

    response=client.models.generate_content(
        model="gemini-2.5-flash-preview-05-20",
        contents=[
            prompt
        ]
    )


    

