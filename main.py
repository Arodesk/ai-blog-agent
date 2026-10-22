import os
import sys

# Add the current directory to python path so it can find 'agents' folder
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from agents.research_agent import run_research
from agents.writer_agent import generate_article
from groq import Groq

def discover_dynamic_topic():
    """স্বয়ংক্রয়ভাবে একটি নতুন ও দরকারী টেক টপিক আবিষ্কার করবে"""
    client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
    prompt = "Suggest one trending, highly useful tech troubleshooting or PC optimization topic for a tech blog in Bengali. Provide only the topic title clearly, nothing else."
    
    completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
    )
    return completion.choices[0].message.content.strip()

if __name__ == "__main__":
    print("=== Master Orchestrator Started ===\n")
    
    # Step 1: Discover a dynamic topic automatically
    print("1. Discovering a new topic...")
    selected_topic = discover_dynamic_topic()
    print(f"-> Selected Topic: {selected_topic}\n")
    
    # Step 2: Run Research Agent
    print("2. Running Research Agent for Information Gain & Gaps...")
    research_brief = run_research(selected_topic)
    print("-> Research Brief Generated Successfully!\n")
    
    # Step 3: Run Writer Agent
    print("3. Running Human-Centered Writer Agent...")
    final_article = generate_article(selected_topic, research_brief)
    
    print("\n=== Final Generated Article ===\n")
    print(final_article)
