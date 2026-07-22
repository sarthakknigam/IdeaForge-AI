prompt = """
You are an AI learning roadmap generator.

Create a detailed learning and development roadmap for the following AI project.

Project Name:
{project_name}

Project Description:
{description}

Difficulty Level:
{difficulty}

Return ONLY valid JSON.

Format:

{{
  "roadmap_title": "Learning Roadmap for Project",
  "duration": "8 weeks",
  "weeks": [
    {{
      "week": "Week 1",
      "focus": "Topic to learn",
      "tasks": [
        "Task 1",
        "Task 2"
      ]
    }}
  ],
  "skills_required": [
    "Python",
    "Machine Learning"
  ]
}}
"""