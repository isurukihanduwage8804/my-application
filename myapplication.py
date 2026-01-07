import streamlit as st
import pandas as pd

# Page Configuration
st.set_page_config(
    page_title="Dinesh Isuru Sampath | Senior Developer Portfolio",
    page_icon="💻",
    layout="wide"
)

# Custom CSS
st.markdown("""
    <style>
    .main { background-color: #f4f7f6; }
    .job-card {
        background-color: white;
        padding: 25px;
        border-radius: 15px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        margin-bottom: 20px;
        border-left: 5px solid #007bff;
        color: #1f1f1f;
    }
    .skill-tag {
        background-color: #e1f5fe;
        color: #01579b;
        padding: 5px 12px;
        border-radius: 20px;
        font-size: 14px;
        font-weight: bold;
        display: inline-block;
        margin: 5px;
    }
    h1, h2, h3 { color: #0e1117; }
    </style>
    """, unsafe_allow_html=True)

# Sidebar Content
st.sidebar.markdown("# 👨‍💻 My Profile")
st.sidebar.info("Experience: **10+ Years**")
st.sidebar.markdown("---")
st.sidebar.markdown("### 📞 Contact Details")
st.sidebar.write("🏠 **Address:** 356/14, Naleen Jayasinghe Road, Pilagoda, Baddegama.")
st.sidebar.write("📅 **DOB:** 18th April 1988 (Age: 37)")
st.sidebar.write("📧 **Email:** dinesh.isuru@example.com")

# Main Header
col1, col2 = st.columns([1, 4])
with col1:
    st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=160)
with col2:
    st.title("Dinesh Isuru Sampath")
    st.subheader("Senior Software Developer & ML Specialist")
    st.write("A veteran developer with **10 years of professional experience** in Python, JavaScript, and HTML. Expert in building production-grade systems and scalable ML infrastructure.")

st.divider()

# Core Skills Section
st.header("🛠 Tech Stack & Expertise")
st.markdown("""
<div>
    <span class="skill-tag">Python (Expert)</span>
    <span class="skill-tag">JavaScript (Senior)</span>
    <span class="skill-tag">HTML5 / CSS3</span>
    <span class="skill-tag">Machine Learning Infrastructure</span>
    <span class="skill-tag">System Design & Architecture</span>
    <span class="skill-tag">Git / GitHub Automation</span>
</div>
""", unsafe_allow_html=True)

st.divider()

# Experience Section
st.header("💼 Professional Journey")

# HTML structure for experience card
experience_html = """
<div class="job-card">
    <h3>Senior Full-Stack Developer (2015 - Present)</h3>
    <p><b>10 Years of Industry Mastery:</b> Specialized in creating robust software solutions and shipping production-ready systems for a variety of use cases.</p>
    <ul>
        <li>Advanced backend development using <b>Python</b>.</li>
        <li>Dynamic and responsive web interfaces using <b>JavaScript</b> and <b>HTML</b>.</li>
        <li>Optimizing <b>ML pipelines</b>, including model evaluation, debugging, and fine-tuning.</li>
        <li>Direct experience in testing and launching scalable software products.</li>
    </ul>
</div>
"""
st.markdown(experience_html, unsafe_allow_html=True)

# Projects Section
st.header("🚀 Key Projects")
