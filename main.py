import os
from groq import Groq

def run_research(topic: str):
    client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
    
    prompt = f"""
    Analyze the technical topic: '{topic}'
    Provide a clear, structured research summary in English including:
    1. Main user pain points and search intent.
    2. Missing angles or content gaps in existing guides.
    3. Technical facts or troubleshooting needs.
    4. Key sections for an expert blog post.
    """
    
    completion = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.4,
    )
    return completion.choices[0].message.content

def generate_article(topic: str, research_brief: str):
    client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
    
    prompt = f"""
    Write a comprehensive, professional English blog post based on the topic and research brief below.
    
    Topic: {topic}
    Research Brief: {research_brief}
    
    Guidelines:
    - Use natural, engaging language with active voice.
    - Start directly with practical solutions or core insights.
    - Format cleanly with Markdown headings (H2, H3), bullet points, and code examples where necessary.
    - Avoid generic introductions or repetitive corporate jargon.
    """
    
    completion = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.6,
    )
    return completion.choices[0].message.content

if __name__ == "__main__":
    print("=== Master Orchestrator Started ===\n")
    
    selected_topic = "Windows 11 RAM Caching High Memory Usage: Root Causes and Permanent Fixes"
    print(f"-> Selected Topic: {selected_topic}\n")
    
    print("2. Running Research Agent...")
    research_brief = run_research(selected_topic)
    print("-> Research Brief Generated Successfully!\n")
    
    print("3. Running Human-Centered Writer Agent...")
    final_article = generate_article(selected_topic, research_brief)
    
    print("\n=== Final Generated Article ===\n")
    print(final_article)
