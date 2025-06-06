# Multi-Agent Social Media Bot

This repository contains a CrewAI-based multi-agent social media bot implementation.

## Architecture

The bot uses the [CrewAI](https://pypi.org/project/crewai/) framework to coordinate multiple specialized agents:

- **ContentCreator**: Generates engaging social media posts for a given topic.
- **Scheduler**: Plans optimal posting schedule for maximum reach.
- **Analyzer**: Analyzes posts and suggests hashtags and improvements.

## Setup

Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the bot to generate social media posts:
```bash
python main.py --topic "Your topic here" --num_posts 7
```

| Option       | Description                                    |
| ------------ | ---------------------------------------------- |
| `--topic`    | Subject for the social media campaign (required) |
| `--num_posts`| Number of posts to generate (default: 7)       |

The bot will output the generated posts, schedule, and suggested improvements.