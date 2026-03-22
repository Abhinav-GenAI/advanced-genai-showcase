from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate

class LLMJudge:
    def __init__(self):
        self.llm = ChatOpenAI(model="gpt-4o", temperature=0)

    def evaluate_response(self, question, context, response):
        prompt = PromptTemplate(
            template="""You are a neutral judge. Evaluate the quality of the 'Response' based on the 'Question' and 'Context' provided.
            
            Metrics:
            1. Faithfulness: Is the answer derived solely from the context? (Score 1-5)
            2. Relevance: Does the answer address the question? (Score 1-5)
            
            Question: {question}
            Context: {context}
            Response: {response}
            
            Return the scores and a brief justification in JSON format.""",
            input_variables=["question", "context", "response"]
        )
        
        chain = prompt | self.llm
        return chain.invoke({
            "question": question,
            "context": context,
            "response": response
        }).content

if __name__ == "__main__":
    judge = LLMJudge()
    q = "What is the capital of France?"
    ctx = "Paris is the capital of France and its largest city."
    ans = "The capital of France is Paris."
    # print(judge.evaluate_response(q, ctx, ans))
    print("LLM-as-Judge Framework ready. Use it to grade RAG or Agent outputs.")
