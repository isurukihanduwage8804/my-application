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
        background-color: white; padding: 25px; border-radius: 15px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1); margin-bottom: 20px;
        border-left: 5px solid #007bff; color: #1f1f1f;
    }
    .skill-tag {
        background-color: #e1f5fe; color: #01579b; padding: 5px 12px;
        border-radius: 20px; font-size: 14px; font-weight: bold;
        display: inline-block; margin: 5px;
    }
    .project-box {
        background-color: #e3f2fd; padding: 20px; border-radius: 10px;
        border: 1px dashed #007bff; text-align: center;
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
st.sidebar.write("📧 **Email:** isurukihanduwage8804@gmail.com")

# Main Header
col1, col2 = st.columns([1, 4])
with col1:
    try:
        st.image("poto1.jpg", width=200, caption="Dinesh Isuru Sampath")
    except:
        st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=200)

with col2:
    st.title("Dinesh Isuru Sampath")
    st.subheader("Senior Software Developer & ML Specialist")
    st.write("A veteran developer with **10 years of professional experience** in Python, JavaScript, and HTML.")

st.divider()

# Core Skills Section
st.header("🛠 Tech Stack")
st.markdown("""
<div>
    <span class="skill-tag">Python (Expert)</span>
    <span class="skill-tag">JavaScript (Senior)</span>
    <span class="skill-tag">HTML5 / CSS3</span>
    <span class="skill-tag">Machine Learning</span>
    <span class="skill-tag">System Architecture</span>
</div>
""", unsafe_allow_html=True)

st.divider()

# --- අලුතින් ඇතුළත් කළ මගේ ව්‍යාපෘති කොටස ---
st.header("🚀 Featured Live Project")
st.markdown("""
<div class="project-box">
    <h3>🌐 Live Application: SVP Web System</h3>
    <p>This is a production-ready application hosted on Streamlit Cloud.</p>
    <a href="https://svpweb.streamlit.app/" target="_blank" style="text-decoration: none;">
        <button style="background-color: #007bff; color: white; padding: 10px 20px; border: none; border-radius: 5px; cursor: pointer; font-size: 16px;">
            Open Project Link
        </button>
    </a>
    <div style="margin-top: 15px; font-size: 14px; color: #555;">
        <b>Login Credentials:</b><br>
        Username: <code style="background: #fff; padding: 2px 5px;">isurusoft</code> | 
        Password: <code style="background: #fff; padding: 2px 5px;">123456</code>
    </div>
</div>
""", unsafe_allow_html=True)

st.divider()

# Experience Section
st.header("💼 Professional Journey")
experience_html = """
<div class="job-card">
    <h3>Senior Full-Stack Developer (2015 - Present)</h3>
    <p><b>10 Years of Industry Mastery:</b> Expert in backend (Python) and frontend (JS/HTML) development.</p>
    <ul>
        <li>Optimizing ML pipelines and production workflows.</li>
        <li>Direct experience in launching scalable software products.</li>
    </ul>
</div>
"""
st.markdown(experience_html, unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("<p style='text-align: center; color: grey;'>Built with Streamlit & Python | 2026 Dinesh Isuru Sampath</p>", unsafe_allow_html=True)
