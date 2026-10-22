import os
from groq import Groq

def generate_article(topic: str, research_brief: str):
    client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
    
    prompt = f"""
    You are an expert Human-Centered Content Writer. 
    Write a detailed, engaging, and natural long-form blog post in Bengali based on the following topic and research brief.
    
    Topic: {topic}
    Research Brief: {research_brief}
    
    Follow these strict rules:
    1. Start directly with the core answer/solution (No fluff/long intro).
    2. Use a natural tone with active voice, avoiding cliché robotic words.
    3. Include practical steps, sub-headings (H2, H3), and clear formatting.
    4. Mention honest limitations or restrictions where applicable.
    5. Conclude with actionable next steps for the reader.
    """
    
    completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.5,
    )
    
    return completion.choices[0].message.content

if __name__ == "__main__":
    sample_topic = "স্মার্টফোনের ব্যাটারি লাইফ বাড়ানোর ৫টি কার্যকর উপায়"
    print(f"Writing article for dynamic topic: {sample_topic}\n")
    print("Writer agent ready.")
