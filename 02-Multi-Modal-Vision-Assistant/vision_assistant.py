import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage
import base64

load_dotenv()

def analyze_image(image_path, prompt):
    # 1. Initialize Vision Model
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash")

    # 2. Encode Image
    with open(image_path, "rb") as image_file:
        image_data = base64.b64encode(image_file.read()).decode("utf-8")

    # 3. Create Message
    message = HumanMessage(
        content=[
            {"type": "text", "text": prompt},
            {
                "type": "image_url",
                "image_url": {"url": f"data:image/jpeg;base64,{image_data}"},
            },
        ]
    )

    # 4. Invoke LLM
    response = llm.invoke([message])
    return response.content

if __name__ == "__main__":
    # Example usage:
    # result = analyze_image("machine_part.jpg", "What is wrong with this component?")
    # print(result)
    print("Multi-Modal Vision Assistant ready. Provide image path and prompt to use.")
