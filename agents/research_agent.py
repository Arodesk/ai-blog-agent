import os
from groq import Groq

def run_research(topic: str):
    client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
    
    prompt = f"""
    You are an expert Research Agent for a professional blog. 
    Analyze the following topic: '{topic}'
    Provide a structured research brief in Bengali containing:
    1. Primary Search Intent & Audience Pain Points
    2. Content Gaps (what competitors miss)
    3. Essential Evidence & Fact-checking needs
    4. Suggested Outline & Key Takeaways
    """
    
    completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3,
    )
    
    return completion.choices[0].message.content

if __name__ == "__main__":
    topic_name = "উইন্ডোজ ১১-এ র‍্যাম ক্যাশিং সমস্যা ও স্থায়ী সমাধান"
    print(f"Researching topic: {topic_name}\n")
    result = run_research(topic_name)
    print(result)
