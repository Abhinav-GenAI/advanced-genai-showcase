# Project 03: Voice-Native Real-Time Agent

## Overview
A low-latency, voice-first AI agent designed for natural, human-like conversations. It handles interruptions, emotional tone, and real-time streaming audio.

## Key Features
- **Full Duplex Chat**: Natural turn-taking and interruption handling.
- **Sub-1s Latency**: Optimized STT -> LLM -> TTS pipeline.
- **Emotional Intelligence**: Tone detection and expressive speech synthesis.

## Tech Stack
- **Real-time Engine**: OpenAI Realtime API / LiveKit
- **STT**: Whisper (Streaming)
- **TTS**: ElevenLabs / Deepgram Aura
- **Orchestration**: WebSockets / FastAPI

## Architecture
- **Input**: Microphone streaming -> WebSocket.
- **Process**: Real-time token generation with function calling support.
- **Output**: Latency-optimized audio playback.
