import json
from langchain_core.prompts import PromptTemplate
from prompts.idea_prompt import prompt
from utils.llm import llm

template = PromptTemplate.from_template(prompt)


def generate_ideas(skills, domain, difficulty):

    chain = template | llm

    response = chain.invoke({
        "skills": skills,
        "domain": domain,
        "difficulty": difficulty
    })

    content = response.content

    
    if isinstance(content, list):
        text = ""

        for item in content:
            if isinstance(item, dict):
                if item.get("type") == "text":
                    text += item.get("text", "")
            else:
                text += str(item)

    else:
        text = str(content)

    
    text = text.strip()

    if text.startswith("```json"):
        text = text.replace("```json", "", 1)

    if text.startswith("```"):
        text = text.replace("```", "", 1)

    if text.endswith("```"):
        text = text[:-3]

    text = text.strip()

    # Print raw Gemini response
    print("\n" + "=" * 80)
    print("RAW GEMINI RESPONSE")
    print("=" * 80)
    print(text)
    print("=" * 80 + "\n")

    try:
        ideas = json.loads(text)

        
        for project in ideas:

            if "roadmap" not in project:
                project["roadmap"] = {
                    "duration": "Not Generated",
                    "skills_required": [],
                    "weeks": []
                }

            # Ensure every project has learning resources
            if "learning_resources" not in project:
                project["learning_resources"] = {
                    "documentation": [],
                    "youtube": [],
                    "courses": [],
                    "github": []
                }

        return ideas

    except json.JSONDecodeError as e:
        print("JSON Parsing Error:")
        print(text)
        raise Exception(f"Invalid JSON returned by Gemini: {e}")