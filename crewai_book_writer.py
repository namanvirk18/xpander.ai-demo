#!/usr/bin/env python3
"""
crewai_book_writer.py

Usage:
    python crewai_book_writer.py

This script prompts the user for a book topic, creates a Researcher agent to gather information
and a Writer agent to write chapters based on the research. It then runs the crew and prints the output.

Dependencies:
    pip install crewai
"""

from crewai import Crew

def main():
    topic = input("Enter the book topic: ")

    crew = Crew()
    researcher = crew.create_agent(name="Researcher", role="Gather information on the topic")
    writer = crew.create_agent(name="Writer", role="Write book chapters based on research")

    crew.add_task(agent=researcher, objective=f"Gather detailed research material on '{topic}'")
    crew.add_task(agent=writer, objective="Write the first draft of book chapters using the research")

    results = crew.run()

    print("\n=== Book Writing Crew Results ===")
    for agent_name, output in results.items():
        print(f"\n-- {agent_name} Output --\n{output}")

if __name__ == "__main__":
    main()