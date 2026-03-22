import subprocess
import os
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate

class CoderAgent:
    def __init__(self):
        self.llm = ChatOpenAI(model="gpt-4o", temperature=0)

    def run_command(self, command):
        try:
            result = subprocess.run(
                command, shell=True, capture_output=True, text=True, timeout=30
            )
            return result.stdout, result.stderr
        except Exception as e:
            return "", str(e)

    def iterative_fix(self, task_description, file_path):
        print(f"Task: {task_description}")
        for attempt in range(3):
            # 1. Ask LLM for code
            prompt = f"Write Python code to solve: {task_description}. Return ONLY the code."
            code = self.llm.invoke(prompt).content.replace("```python", "").replace("```", "").strip()
            
            # 2. Save Code
            with open(file_path, "w") as f:
                f.write(code)
            
            # 3. Run and Check
            stdout, stderr = self.run_command(f"python {file_path}")
            
            if not stderr:
                print(f"Success on attempt {attempt + 1}!")
                return stdout
            else:
                print(f"Attempt {attempt + 1} failed. Error: {stderr}")
                # Feed error back to LLM in next loop
                task_description = f"Fix this code: {code}\nError: {stderr}"
        
        return "Failed after 3 attempts."

if __name__ == "__main__":
    # agent = CoderAgent()
    # agent.iterative_fix("Write a function that calculates the 10th fibonacci number", "temp_code.py")
    print("Autonomous Coder Agent ready. Implements Write-Test-Fix loop logic.")
