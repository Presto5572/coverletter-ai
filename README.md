# CoverLetter-AI Agent

An intelligent, full-stack application designed to generate highly tailored cover letters for Data Analyst roles. By utilizing Large Language Models (LLMs), this agent creates two distinct personas—**Corporate** and **Technical**—to help job seekers align their applications with specific company cultures.

## Features

- **Dual-Tone Generation:** Switch between a 'Corporate' (culture/values focused) and 'Technical' (methodology/stack focused) tone.
- **Data-Driven Insights:** Specifically optimized for Data Analyst roles, emphasizing SQL, Python, and visualization expertise.
- **Full-Stack Architecture:** Powered by a Python/Flask backend and a modern React frontend.
- **Secure Environment:** Integrated with `.env` protection to keep API keys safe.

## Tech Stack

- **Backend:** Python 3.x, Flask
- **Frontend:** React.js, Tailwind CSS
- **AI Integration:** [e.g., OpenAI GPT-4 / LangChain]
- **Source Control:** Git & GitHub

## Installation & Setup

### Prerequisites
- Python 3.8+
- Node.js & npm

### Backend Setup
1. Navigate to the backend folder:
   ```bash
   cd backend

#### Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate

#### Install dependencies:
   ```bash
   pip install -r requirements.txt

#### Create a .env file and add your API keys:
   ```bash
   touch .env
   OPENAI_API_KEY="your_openai_api_key"

### Frontend Setup
cd frontend

#### Install dependencies
npm install

#### Start the development server
npm start

## Project Structure
coverletter-ai/
├── backend/            # Python/Flask API
│   ├── .env           # (Hidden) API Keys
│   └── main.py        # Logic for AI generation
├── frontend/           # React Application
│   └── src/           # UI Components
├── .gitignore          # Rules for excluded files
└── requirements.txt    # Python dependencies

## Contributing
Developed by Colson Keim
AI assistance via OpenAI ChatGPT, Google Gemini, & Microsoft Copilot Chat via VSSCode Extension