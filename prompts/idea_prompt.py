prompt = """
You are an AI project idea generator.

Generate exactly 5 innovative AI project ideas based on:

- Skills: {skills}
- Domain: {domain}
- Difficulty: {difficulty}

For EACH project include:
- title
- description
- technologies
- why_build
- roadmap
- learning_resources

The roadmap must include:
- duration
- skills_required
- weeks

Each week must contain:
- week
- focus
- tasks

The learning_resources object is MANDATORY and must never be omitted.

The learning_resources object must include:
- documentation
- youtube
- courses
- github

Each category should contain EXACTLY 2 relevant resources.

Each resource must contain:
- name
- url

Prefer official documentation, high-quality YouTube tutorials, reputable courses, and official GitHub repositories.

Return ONLY valid JSON.

Do NOT return markdown.
Do NOT return explanations.
Do NOT return headings.
Do NOT omit any field.
Every project MUST contain roadmap and learning_resources.

Return exactly this format:

[
  {{
    "title": "Project Title",
    "description": "Short description.",
    "technologies": [
      "Python",
      "LangChain",
      "Gemini"
    ],
    "why_build": "Why this project is useful.",
    "roadmap": {{
      "duration": "8 Weeks",
      "skills_required": [
        "Python",
        "Machine Learning",
        "LangChain"
      ],
      "weeks": [
        {{
          "week": "Week 1",
          "focus": "Python Fundamentals",
          "tasks": [
            "Revise Python",
            "Practice OOP",
            "Solve 10 coding problems"
          ]
        }},
        {{
          "week": "Week 2",
          "focus": "Machine Learning Basics",
          "tasks": [
            "Study supervised learning",
            "Build a simple classifier"
          ]
        }}
      ]
    }},
    "learning_resources": {{
      "documentation": [
        {{
          "name": "LangChain Documentation",
          "url": "https://python.langchain.com/docs/"
        }},
        {{
          "name": "Python Documentation",
          "url": "https://docs.python.org/3/"
        }}
      ],
      "youtube": [
        {{
          "name": "LangChain Crash Course",
          "url": "https://www.youtube.com/"
        }},
        {{
          "name": "Python Full Course",
          "url": "https://www.youtube.com/"
        }}
      ],
      "courses": [
        {{
          "name": "LangChain for LLM Application Development",
          "url": "https://www.deeplearning.ai/"
        }},
        {{
          "name": "Google Machine Learning Crash Course",
          "url": "https://developers.google.com/machine-learning/crash-course"
        }}
      ],
      "github": [
        {{
          "name": "LangChain",
          "url": "https://github.com/langchain-ai/langchain"
        }},
        {{
          "name": "Awesome LLM Apps",
          "url": "https://github.com/Shubhamsaboo/awesome-llm-apps"
        }}
      ]
    }}
  }}
]
"""