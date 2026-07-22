# 🔥 IdeaForge AI

Empowering developers to build innovative AI solutions. Generate tailored project ideas, explore emerging technologies, and transform your skills into structured, actionable learning roadmaps.

---

##  Overview

**IdeaForge AI** is an AI-powered project brainstorming and roadmap generation tool. It enables developers to input their current tech stack, choose a domain of interest, and select a difficulty level to generate 5 personalized project ideas. 

Each project comes with a tailored, step-by-step weekly roadmap, direct learning resources, and options to export the roadmap as a clean PDF document or a JSON data file.

---

##  Features:

- **Personalized AI Recommendations**: Projects generated are customized dynamically based on your current skillset (e.g., Python, React, Machine Learning).
- **Domain & Difficulty Filters**: Refine search criteria using 10 domains (Healthcare, Finance, Education, Cybersecurity, Smart Cities, etc.) and 3 difficulty levels (Beginner, Intermediate, Advanced).
- **Comprehensive Roadmaps**: Every project includes a weekly timeline with actionable tasks, target durations, and required competencies.
- **Curated Learning Resources**: Aggregates direct references to official documentation, YouTube tutorials, online courses, and relevant GitHub repositories.
- **Export Capabilities**:
  - **PDF Export**: Generate and download a formatted PDF roadmap containing the project outline and weekly breakdown.
  - **JSON Export**: Save the entire generated dataset in a structured JSON file for future reference.
- **Premium User Interface**: Implements a customized dark-themed layout in Streamlit using CSS-in-JS injection, featuring responsive timelines, custom metric displays, and elegant typography.

---

##  Tech Stack

- **Frontend / Presentation**: [Streamlit](https://streamlit.io/)
- **Orchestration**: [LangChain](https://www.langchain.com/)
- **LLM Provider**: [Google Gemini API (ChatGoogleGenerativeAI)](https://ai.google.dev/) (via model: `gemini-flash-latest`)
- **PDF Generation**: [ReportLab](https://www.reportlab.com/)
- **Environment Management**: `python-dotenv`

---

## 📂 Project Structure

```text
AI Innovation Lab/
├── agents/
│   ├── __init__.py
│   ├── idea_generator.py      # Core agent handling prompt execution & response parsing
├── prompts/
│   └── idea_prompt.py         # System & structural prompt definitions for Gemini
├── utils/
│   ├── __init__.py
│   ├── llm.py                 # Google Gemini client initialization
│   └── pdf_generator.py       # PDF document builder using ReportLab
├── app.py                     # Main Streamlit web application & styling
├── list_models.py             # Script to verify model capabilities & list Google models
├── requirements.txt           # Python package dependencies
├── .env                       # Environment variables (API Key)
└── Readme.md                  # Project documentation (this file)
```

---

##  Setup & Installation

### Prerequisites

- Python 3.9 or higher
- A Google Gemini API Key. You can get one from the [Google AI Studio](https://aistudio.google.com/).

### Installation Steps

1. **Clone the Repository** (or navigate to the project directory):
   ```bash
   cd "AI Innovation Lab"
   ```

2. **Create and Activate a Virtual Environment**:
   * **On Windows (PowerShell/CMD)**:
     ```powershell
     python -m venv .venv
     .venv\Scripts\activate
     ```
   * **On macOS/Linux**:
     ```bash
     python3 -m venv .venv
     source .venv/bin/activate
     ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables**:
   Create a `.env` file in the root directory and add your Google Gemini API Key:
   ```env
   GOOGLE_API_KEY=your_gemini_api_key_here
   ```

---
##  Running the Application

To launch the Streamlit server locally, execute:

```bash
streamlit run app.py
```

Once running, the application will automatically open in your default browser at `http://localhost:8501`.


## 💡 How it Works

1. **Input Parameters**: Enter your programming skills/tools in the input field, separated by commas (e.g., `Python, HTML, SQLite`), select a target domain, and pick a difficulty level.
2. **AI Generation**: Click **Generate Project Ideas** to start the LLM execution pipeline. The agents format and query the Gemini API.
3. **Explore Results**: Explore the 5 interactive project expanders:
   - Read the project outline and the value proposition (**Why Build It?**).
   - Review the detailed weekly breakdown.
   - Access direct links to documentation, guides, and source code.
4. **Export Options**: Export individual roadmaps as a formatted PDF or download the full set of generated ideas in a structured JSON file.

