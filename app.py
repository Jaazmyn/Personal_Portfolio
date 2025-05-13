import streamlit as st

# 项目列表
projects = [
    {
        "image": "conch.png",
        "title": "Conch AI",
        "description": "Customizable AI avatars help bridge the emotional gap."
    },
    {
        "image": "figma.png",
        "title": "Figma Redesign",
        "description": "Enhance the overall search experience for design teams."
    },
    {
        "image": "maris.png",
        "title": "Maris VR",
        "description": "A unique ocean rescue strategy VR game with a giant's perspective."
    }
]

if "page" not in st.session_state:
    st.session_state["page"] = "About"

st.set_page_config(page_title="Jazmyn UX Portfolio", layout="centered")

# 设置header和title字体为Helvetica
st.markdown('''
    <style>
    h1, h2, .st-emotion-cache-10trblm, .st-emotion-cache-1v0mbdj {
        font-family: Helvetica, Arial, sans-serif !important;
        letter-spacing: 0.01em;
    }
    </style>
''', unsafe_allow_html=True)

st.title("Jazmyn Zhang")

tab1, tab2 = st.tabs(["About", "Projects"])

with tab1:
    st.image("images/about.jpeg", caption=None, use_container_width=False)
    st.header("About")
    st.write("I'm a detail-oriented UX designer passionate about XR and AI, currently pursuing a Master's in Technology Innovation at the University of Washington. I design immersive experiences that seamlessly blend the digital and physical worlds.")
    st.markdown("### Experience")
    st.markdown("""
**Ionic Tech | Product Designer**  
*Sept. 2023 – May 2024, Shanghai*  
- Improved the emotional support capabilities of an AI chatbot app, leading to 34,000 initial users and securing $5 million in funding.
- Enhanced the AI chatting experience with milestone popups and integrated 10 emotional responses for video chatting, increasing user chat duration by 24%.
- Streamlined the character creation process using MBTI tags, reducing bounce rate by 28%.
- Revamped the design system to ensure accessibility and documented 4 design iterations for consistency and continuous improvement.

**VeeR VR | Interaction Design Co-op Intern**  
*Mar. 2023 – Jun. 2023, Beijing*  
- Contributed to the design and development of an ocean conservation VR game, incorporating a giant's perspective to enhance player engagement within short gameplay sessions.
- Conducted 3 rounds of physical prototyping and game balancing, refining mechanics to improve engagement and educational value.
- Designed and prototyped a raise-to-wake quick access panel in Unity, streamlining gameplay interactions as a primary control mechanism.
- Developed a cohesive retro design system, aligning with the game's narrative, and created architectural elements from sketches to 3D models to enhance the game environment.
""")
    st.markdown("### Skills")
    # (paste the Skills block here)
    st.markdown("""
**Design:**  
UX Research, UI/Interaction Design, User Journey Mapping, Usability Testing, Storyboarding, Wireframing, Prototyping, 3D Modeling, Iconography, Information Architecture, Fabrication, 3D Printing

**Software:**  
Figma, Miro, Zeplin, Basic Unity, Rhino, Grasshopper, SketchUp, V-ray, Fusion, Python, VS Code, GitHub, Adobe Creative Suite
""")
with tab2:
    st.header("Projects")
    for project in projects:
        st.image("images/" + project['image'])
        st.subheader(project['title'])
        st.write(project['description'])
        # 可加：st.markdown("**Role:** UX Designer  |  **Tools:** Figma, Sketch")
        # 可加：st.expander("See more...") 展开详细过程 