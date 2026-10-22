import os
from groq import Groq

def run_research(topic: str):
    """রিসર્ચ এজেন্ট: টপিক বিশ্লেষণ ও গ্যাপ খুঁজে বের করা"""
    client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
    
    prompt = f"""
    You are an expert Research Agent for a professional blog. 
    Analyze the following topic: '{topic}'
    Provide a structured research brief in English containing:
    1. Primary Search Intent & Audience Pain Points
    2. Content Gaps (what competitors miss)
    3. Essential Evidence & Fact-checking needs
    4. Suggested Outline & Key Takeaways
    """
    
    completion = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3,
    )
    return completion.choices[0].message.content

def generate_article(topic: str, research_brief: str):
    """রাইটার এজেন্ট: হিউম্যান-সেন্ট্রিক ও এআই ডিটেক্টর বাইপাস করার উপযোগী ইংলিশ আর্টিকেল লেখা"""
    client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
    
    prompt = f"""
    You are an expert Human-Centered Content Writer and SEO Specialist. 
    Write a detailed, highly engaging, and completely natural long-form blog post in English based on the following topic and research brief.
    
    Topic: {topic}
    Research Brief: {research_brief}
    
    CRITICAL INSTRUCTIONS TO BYPASS AI DETECTORS & SOUND 100% HUMAN:
    1. Write in a natural, conversational, yet authoritative tone using active voice. Avoid robotic clichés, fluff, and overly formal transitions.
    2. Vary sentence length significantly—mix short, punchy sentences with longer, detailed explanations.
    3. Start directly with the core solution or answer without a generic introductory paragraph.
    4. Include practical steps, real-world context, clear markdown formatting (H2, H3), bullet points, and code snippets or tables where helpful.
    5. Maintain high "Information Gain" by sharing unique insights and clear actionable takeaways.
    """
    
    completion = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
    )
    return completion.choices[0].message.content

if __name__ == "__main__":
    print("=== Master Orchestrator Started ===\n")
    
    # Step 1: Dynamic Topic (in English for global/English blog)
    selected_topic = "Windows 11 RAM Caching High Memory Usage: Root Causes and Permanent Fixes"
    print(f"-> Selected Topic: {selected_topic}\n")
    
    # Step 2: Research Agent
    print("2. Running Research Agent...")
    research_brief = run_research(selected_topic)
    print("-> Research Brief Generated Successfully!\n")
    
    # Step 3: Writer Agent
    print("3. Running Human-Centered Writer Agent...")
    final_article = generate_article(selected_topic, research_brief)
    
    print("\n=== Final Generated Article ===\n")
    print(final_article)
