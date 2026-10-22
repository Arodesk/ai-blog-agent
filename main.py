import os
from groq import Groq

def run_research(topic: str):
    """রিসার্চ এজেন্ট: টপিক বিশ্লেষণ ও গ্যাপ খুঁজে বের করা"""
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
        model="llama3-70b-8192",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3,
    )
    return completion.choices[0].message.content

def generate_article(topic: str, research_brief: str):
    """রাইটার এজেন্ট: হিউম্যান-সেন্ট্রিক লং-ফর্ম আর্টিকেল লেখা"""
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
        model="llama3-70b-8192",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.5,
    )
    return completion.choices[0].message.content

if __name__ == "__main__":
    print("=== Master Orchestrator Started ===\n")
    
    # Step 1: Dynamic Topic
    selected_topic = "উইন্ডোজ ১১-এ র‍্যাম ক্যাশিং সমস্যা ও স্থায়ী সমাধান"
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
