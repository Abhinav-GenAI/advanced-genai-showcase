# Project 05: Automated "News Insights" Dashboard

## Overview
A sophisticated automation system that monitors news feeds, cleans data using LLMs, and presents visualized insights or audio briefings.

## Key Features
- **Targeted Scraping**: Monitors RSS feeds or specific news domains.
- **Sentiment Analysis**: Tracks market or public sentiment over time.
- **Auto-Briefing**: Generates a 2-minute daily audio briefing using TTS.

## Tech Stack
- **Scraper**: BeautifulSoup / Playwright
- **Reasoning**: DeepSeek-R1 / Gemini 1.5 Flash
- **Database**: PostgreSQL / Supabase
- **Frontend**: Streamlit / Next.js
- **Audio**: ElevenLabs API

## Workflow
1. **Collect**: Daily scrape of top 50 headlines.
2. **Analyze**: Cluster related stories; remove duplicate/noisy data.
3. **Generate**: Summarize the "Bottom Line" for the user.
4. **Publish**: Update dashboard and generate audio.
