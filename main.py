#!/usr/bin/env python3
"""
main.py

CrewAI-based multi-agent social media bot.

Usage:
    python main.py --topic "Your topic here" [--num_posts 7]
"""

import argparse
from crewai import Crew


def parse_args():
    parser = argparse.ArgumentParser(
        description="Multi-agent social media bot using CrewAI"
    )
    parser.add_argument(
        "--topic",
        required=True,
        help="Topic for social media posts",
    )
    parser.add_argument(
        "--num_posts",
        type=int,
        default=7,
        help="Number of posts to generate",
    )
    return parser.parse_args()


def main():
    args = parse_args()
    topic = args.topic
    num_posts = args.num_posts

    crew = Crew()

    content_creator = crew.create_agent(
        name="ContentCreator",
        role="Generate engaging social media posts",
    )
    scheduler = crew.create_agent(
        name="Scheduler",
        role="Schedule posts for optimal reach",
    )
    analyzer = crew.create_agent(
        name="Analyzer",
        role="Analyze engagement and suggest improvements",
    )

    crew.add_task(
        agent=content_creator,
        objective=f"Create {num_posts} social media posts about '{topic}'",
    )
    crew.add_task(
        agent=scheduler,
        objective=f"Schedule the {num_posts} posts for maximum engagement",
    )
    crew.add_task(
        agent=analyzer,
        objective="Analyze post content and provide suggested hashtags and improvements",
    )

    results = crew.run()

    print("\n=== Multi-Agent Social Media Bot Results ===")
    for agent_name, output in results.items():
        print(f"\n-- {agent_name} Output --\n{output}")


if __name__ == "__main__":
    main()