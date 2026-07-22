import json
import streamlit as st
from agents.idea_generator import generate_ideas
from utils.pdf_generator import generate_roadmap_pdf
st.set_page_config(
    page_title="IdeaForge AI",
    page_icon="🔥",
    layout="wide"
)
DOMAINS = [
    "Healthcare",
    "Finance",
    "Education",
    "Agriculture",
    "Cybersecurity",
    "E-commerce",
    "Environment",
    "Sports",
    "Smart Cities",
    "General AI"
]
DIFFICULTIES = ["Beginner", "Intermediate", "Advanced"]
# Theme
def inject_custom_css():
    st.markdown("""
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;600;700&family=IBM+Plex+Sans:wght@400;500;600&family=IBM+Plex+Mono:wght@400;500;600&display=swap" rel="stylesheet">

    <style>
    :root{
        --bg:#0d141d;
        --panel:#141d29;
        --panel-2:#1a2431;
        --line:#26333f;
        --text:#e7edf3;
        --text-dim:#8fa0b3;
        --text-faint:#546575;
        --ember:#ff8c42;
        --ember-2:#ffd166;
        --teal:#5fd3a3;
    }

    .stApp{
        background:
          linear-gradient(#101a25 1px, transparent 1px) 0 0/100% 42px,
          linear-gradient(90deg, #101a25 1px, transparent 1px) 0 0/42px 100%,
          var(--bg);
        color: var(--text);
        font-family: 'IBM Plex Sans', sans-serif;
    }

    section[data-testid="stSidebar"]{
        background: var(--panel);
        border-right: 1px solid var(--line);
    }
    section[data-testid="stSidebar"] h1,
    section[data-testid="stSidebar"] h2,
    section[data-testid="stSidebar"] h3{
        font-family:'Space Grotesk', sans-serif;
        color: var(--text);
    }

    h1, h2, h3{
        font-family:'Space Grotesk', sans-serif !important;
        letter-spacing:-0.01em;
        color: var(--text) !important;
    }
    h1 { font-weight:700 !important; }
    p, li, span, label, .stMarkdown{ color: var(--text-dim); }

    .forge-eyebrow{
        font-family:'IBM Plex Mono', monospace;
        font-size: 11px;
        letter-spacing: .16em;
        text-transform: uppercase;
        color: var(--text-faint);
        margin-bottom: 10px;
    }
    .forge-hero-title{
        font-family:'Space Grotesk', sans-serif;
        font-weight:700;
        font-size: 42px;
        color: var(--text);
        margin: 6px 0 12px 0;
    }
    .forge-hero-sub{
        color: var(--text-dim);
        font-size: 15.5px;
        max-width: 640px;
        margin-bottom: 12px;
        line-height: 1.7;
    }

    hr{ border-color: var(--line) !important; margin: 28px 0 !important; }

    /* Inputs */
    .stTextInput input, .stSelectbox div[data-baseweb="select"] > div{
        background: var(--panel-2) !important;
        border: 1px solid var(--line) !important;
        color: var(--text) !important;
        border-radius: 8px !important;
    }
    .stTextInput input::placeholder{ color: var(--text-faint) !important; }
    .stTextInput label, .stSelectbox label{
        font-family:'IBM Plex Mono', monospace !important;
        font-size: 11.5px !important;
        letter-spacing: .08em;
        text-transform: uppercase;
        color: var(--text-faint) !important;
        margin-bottom: 8px !important;
    }

    /* Buttons */
    .stButton > button{
        background: linear-gradient(180deg, var(--ember) 0%, #e6702a 100%) !important;
        color: #1a0f06 !important;
        font-family:'Space Grotesk', sans-serif !important;
        font-weight: 600 !important;
        border: none !important;
        border-radius: 8px !important;
        box-shadow: 0 6px 18px -6px rgba(255,140,66,.55);
        transition: filter .12s ease, transform .12s ease;
        margin-top: 10px;
    }
    .stButton > button:hover{ filter: brightness(1.06); transform: translateY(-1px); }

    .stDownloadButton > button{
        background: transparent !important;
        color: var(--text) !important;
        border: 1px dashed var(--line) !important;
        border-radius: 8px !important;
        font-family:'IBM Plex Mono', monospace !important;
        font-size: 12.5px !important;
        width: 100%;
    }
    .stDownloadButton > button:hover{
        border-color: var(--ember) !important;
        color: var(--ember-2) !important;
    }

    /* Card container (project) */
    div[data-testid="stExpander"]{
        background: var(--panel);
        border: 1px solid var(--line) !important;
        border-radius: 12px !important;
        margin-bottom: 24px;
        overflow: hidden;
    }
    div[data-testid="stExpander"] summary{
        font-family:'Space Grotesk', sans-serif !important;
        font-size: 17px !important;
        font-weight: 600 !important;
        color: var(--text) !important;
        padding: 14px 16px !important;
    }
    div[data-testid="stExpander"] summary:hover{ background: var(--panel-2); }
    div[data-testid="stExpander"] .stMarkdown{ margin-bottom: 6px; }

    /* Tabs (resources) */
    .stTabs [data-baseweb="tab-list"]{
        gap: 4px;
        border-bottom: 1px solid var(--line);
        margin-bottom: 12px;
    }
    .stTabs [data-baseweb="tab"]{
        font-family:'IBM Plex Mono', monospace;
        font-size: 12.5px;
        color: var(--text-faint);
        background: transparent;
        padding: 10px 14px;
    }
    .stTabs [aria-selected="true"]{
        color: var(--ember-2) !important;
        border-bottom: 2px solid var(--ember) !important;
    }

    /* Metrics (duration / skill count) — plain, no box */
    div[data-testid="stMetric"]{
        background: transparent;
        border: none;
        padding: 4px 0 12px 0;
    }
    div[data-testid="stMetricLabel"]{
        font-family:'IBM Plex Mono', monospace !important;
        text-transform: uppercase;
        letter-spacing: .08em;
        font-size: 10.5px !important;
        color: var(--text-faint) !important;
        margin-bottom: 4px !important;
    }
    div[data-testid="stMetricValue"]{
        font-family:'Space Grotesk', sans-serif !important;
        color: var(--ember-2) !important;
        font-size: 26px !important;
    }

    /* Custom chips / badges */
    .forge-pill-row{ display:flex; flex-wrap:wrap; gap:10px; margin: 10px 0 18px; }
    .forge-pill{
        font-family:'IBM Plex Mono', monospace;
        font-size: 12px;
        padding: 5px 12px;
        border-radius: 20px;
        border: 1px solid rgba(95,211,163,.4);
        color: var(--teal);
        background: rgba(95,211,163,.07);
        display:inline-block;
    }

    /* Why Build It — plain highlighted text, no box */
    .forge-why-box{
        border-left: none;
        background: transparent;
        padding: 0;
        color: var(--ember-2);
        font-size: 14.5px;
        font-weight: 500;
        line-height: 1.7;
        margin: 8px 0 18px;
    }

    .forge-subhead{
        font-family:'IBM Plex Mono', monospace;
        font-size: 11.5px;
        letter-spacing: .1em;
        text-transform: uppercase;
        color: var(--text-faint);
        margin: 30px 0 12px;
    }

    /* Weekly timeline (replaces nested expanders) */
    .forge-timeline{ position:relative; margin: 10px 0 8px 6px; padding-left: 24px; }
    .forge-timeline::before{
        content:""; position:absolute; left:5px; top:6px; bottom:6px; width:1px;
        background: repeating-linear-gradient(var(--line) 0 4px, transparent 4px 8px);
    }
    .forge-week{ position:relative; margin-bottom: 24px; }
    .forge-week::before{
        content:""; position:absolute; left:-24px; top:4px; width:9px; height:9px;
        border-radius:50%; background: var(--panel); border:2px solid var(--ember);
    }
    .forge-week-head{ display:flex; align-items:baseline; gap:12px; margin-bottom: 6px; }
    .forge-week-name{ font-family:'IBM Plex Mono', monospace; font-size:12.5px; color: var(--ember-2); }
    .forge-week-focus{ font-size:14px; color: var(--text); font-weight:500; }
    .forge-week-tasks{ margin: 8px 0 0 0; padding: 0; list-style:none; }
    .forge-week-tasks li{
        font-size:13.5px; color: var(--text-dim); padding: 5px 0 5px 20px; position:relative;
    }
    .forge-week-tasks li::before{ content:"✓"; position:absolute; left:0; top:5px; color: var(--teal); font-size:12px; }

    a{ color: var(--ember-2) !important; }
    </style>
    """, unsafe_allow_html=True)

# Section renderers

def render_hero():
    st.markdown('<div class="forge-eyebrow">🚀Dream It. Forge It. Launch It.</div>', unsafe_allow_html=True)
    st.markdown('<div class="forge-hero-title">🔥 IdeaForge AI</div>', unsafe_allow_html=True)
    st.markdown(
        '''
        <div class="forge-hero-sub">
        Empowering developers to build innovative AI solutions.
        Generate project ideas, explore emerging technologies, and transform
        your skills into impactful real-world projects.
        </div>
        ''',
        unsafe_allow_html=True
    )
    st.write("")


def render_sidebar():
    with st.sidebar:
        st.header("⚙️ Settings")
        st.write("Customize your AI project generation.")


def render_input_panel():
    col1, col2, col3 = st.columns([1.4, 1, 1])

    with col1:
        skills = st.text_input(
            "🛠️ Enter your skills",
            placeholder="Python, Machine Learning, React"
        )
    with col2:
        domain = st.selectbox("🌍 Select Domain", DOMAINS)
    with col3:
        difficulty = st.selectbox("📈 Difficulty Level", DIFFICULTIES)

    return skills, domain, difficulty


def render_pills(items):
    pills_html = "".join(f'<span class="forge-pill">{item}</span>' for item in items)
    st.markdown(f'<div class="forge-pill-row">{pills_html}</div>', unsafe_allow_html=True)


def render_weekly_timeline(weeks):
    # NOTE: built as flat, unindented strings on purpose — Markdown treats
    # 4+ leading spaces as a code block, which breaks HTML rendering for
    
    parts = ['<div class="forge-timeline">']
    for week in weeks:
        tasks_html = "".join(f"<li>{task}</li>" for task in week["tasks"])
        parts.append(
            '<div class="forge-week">'
            '<div class="forge-week-head">'
            f'<span class="forge-week-name">{week["week"]}</span>'
            f'<span class="forge-week-focus">{week["focus"]}</span>'
            '</div>'
            f'<ul class="forge-week-tasks">{tasks_html}</ul>'
            '</div>'
        )
    parts.append('</div>')
    st.markdown("".join(parts), unsafe_allow_html=True)


def render_resources(resources):
    resources = resources or {"documentation": [], "youtube": [], "courses": [], "github": []}

    tab_docs, tab_yt, tab_courses, tab_github = st.tabs(
        ["📖 Documentation", "🎥 YouTube", "🎓 Courses", "💻 GitHub"]
    )

    with tab_docs:
        for item in resources["documentation"]:
            st.markdown(f"- [{item['name']}]({item['url']})")

    with tab_yt:
        for item in resources["youtube"]:
            st.markdown(f"- [{item['name']}]({item['url']})")

    with tab_courses:
        for item in resources["courses"]:
            st.markdown(f"- [{item['name']}]({item['url']})")

    with tab_github:
        for item in resources["github"]:
            st.markdown(f"- [{item['name']}]({item['url']})")


def render_project_card(project, index):
    with st.expander(f"🚀 {index}. {project['title']}", expanded=(index == 1)):

        st.markdown('<div class="forge-subhead">📝 Description</div>', unsafe_allow_html=True)
        st.write(project["description"])

        st.markdown('<div class="forge-subhead">🛠 AI Technologies</div>', unsafe_allow_html=True)
        render_pills(project["technologies"])

        st.markdown('<div class="forge-subhead">⭐ Why Build It?</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="forge-why-box">{project["why_build"]}</div>', unsafe_allow_html=True)

        st.divider()
        st.markdown('<div class="forge-subhead">📚 Learning Roadmap</div>', unsafe_allow_html=True)

        roadmap = project["roadmap"]

        m1, m2 = st.columns(2)
        m1.metric("Duration", roadmap["duration"])
        m2.metric("Skills Required", len(roadmap["skills_required"]))

        render_pills(roadmap["skills_required"])

        st.markdown('<div class="forge-subhead">🗓 Weekly Roadmap</div>', unsafe_allow_html=True)
        render_weekly_timeline(roadmap["weeks"])

        pdf = generate_roadmap_pdf(project)
        st.download_button(
            "📄 Export Roadmap as PDF",
            data=pdf,
            file_name=f"{project['title'].replace(' ', '_')}_roadmap.pdf",
            mime="application/pdf",
            key=f"pdf_{index}"
        )

        st.divider()
        st.markdown('<div class="forge-subhead">📚 Learning Resources</div>', unsafe_allow_html=True)
        render_resources(project.get("learning_resources"))


def render_results(ideas):
    st.divider()
    st.markdown("## 💡 Personalized Project Ideas")

    for i, project in enumerate(ideas, start=1):
        render_project_card(project, i)

    st.divider()
    st.download_button(
        "📥 Download JSON",
        data=json.dumps(ideas, indent=4),
        file_name="ai_project_ideas.json",
        mime="application/json",
        use_container_width=True
    )

# App entry point


def main():
    inject_custom_css()
    render_hero()
    render_sidebar()

    skills, domain, difficulty = render_input_panel()

    if "ideas" not in st.session_state:
        st.session_state.ideas = None

    if st.button("🚀 Generate Project Ideas", use_container_width=True):
        if not skills.strip():
            st.warning("⚠️ Please enter your skills.")
        else:
            with st.spinner("🤖 AI is generating innovative project ideas..."):
                st.session_state.ideas = generate_ideas(skills, domain, difficulty)
            st.success("✅ Ideas Generated Successfully!")

    if st.session_state.ideas:
        render_results(st.session_state.ideas)


if __name__ == "__main__":
    main()