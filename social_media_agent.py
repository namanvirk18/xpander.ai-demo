#!/usr/bin/env python3
"""
Multi-Agent Social Media Content Generator

This script uses the latest CrewAI syntax to create a multi-agent system that:
 1) Researcher agent gathers information on a user-specified topic.
 2) Writer agent drafts social media content.
 3) Publisher agent simulates posting the content.

Usage:
    pip install -r requirements.txt
    python social_media_agent.py "Your Topic Here"

For more details, see: https://docs.crewai.com/introduction
"""

import sys
from crewai import Crew

# Initialize the Crew
crew = Crew()


@crew.agent
async def researcher(topic: str) -> str:
    """
    Researcher agent gathers information on the topic.
    (Simulated logic; replace with real research/API calls as needed.)
    """
    # Simulate research results
    return f"Research results on '{topic}': Simulated information."


@crew.agent
async def writer(research_results: str) -> str:
    """
    Writer agent drafts social media content based on research results.
    """
    # Simulate drafting process
    return f"Draft social media post based on research:\n{research_results}\n## End of draft ##"


@crew.agent
async def publisher(draft: str) -> None:
    """
    Publisher agent simulates posting the content by printing and writing to a file.
    """
    print("\n--- Publishing Content ---\n")
    print(draft)
    with open("published_post.txt", "w", encoding="utf-8") as f:
        f.write(draft)
    print("\nContent written to 'published_post.txt'.")


@crew.flow
async def social_media_flow(topic: str):
    """
    Defines a flow that connects the Researcher, Writer, and Publisher agents.
    """
    research = await researcher(topic)
    draft = await writer(research)
    await publisher(draft)


def main():
    # Determine topic from command-line argument or prompt user
    if len(sys.argv) > 1:
        topic = sys.argv[1]
    else:
        topic = input("Enter the topic for social media content: ").strip()

    # Run the flow
    crew.run(flow=social_media_flow, inputs={"topic": topic})


if __name__ == "__main__":
    main()