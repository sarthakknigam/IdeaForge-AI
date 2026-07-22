from io import BytesIO
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

def generate_roadmap_pdf(project):
    buffer = BytesIO()

    doc = SimpleDocTemplate(buffer)
    styles = getSampleStyleSheet()

    story = []

    story.append(Paragraph(f"<b>{project['title']}</b>", styles["Title"]))
    story.append(Paragraph(project["description"], styles["BodyText"]))

    roadmap = project["roadmap"]

    story.append(Paragraph("<br/><b>Duration</b>", styles["Heading2"]))
    story.append(Paragraph(roadmap["duration"], styles["BodyText"]))

    story.append(Paragraph("<br/><b>Skills Required</b>", styles["Heading2"]))

    for skill in roadmap["skills_required"]:
        story.append(Paragraph(f"• {skill}", styles["BodyText"]))

    story.append(Paragraph("<br/><b>Weekly Roadmap</b>", styles["Heading2"]))

    for week in roadmap["weeks"]:
        story.append(Paragraph(f"<b>{week['week']}</b>", styles["Heading3"]))
        story.append(Paragraph(f"Focus: {week['focus']}", styles["BodyText"]))

        for task in week["tasks"]:
            story.append(Paragraph(f"• {task}", styles["BodyText"]))

    doc.build(story)

    buffer.seek(0)

    return buffer