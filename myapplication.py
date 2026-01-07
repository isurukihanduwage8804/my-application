import streamlit as st
import pandas as pd

# Page Configuration
st.set_page_config(page_title="Dinesh Isuru | Senior Developer Portfolio", page_icon="💻", layout="wide")

# Custom CSS for a professional look
st.markdown("""
    <style>
    .main { background-color: #f4f7f6; }
    .stHeader { color: #0e1117; }
    .job-card {
        background-color: white;
        padding: 25px;
        border-radius: 15px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        margin-bottom: 20px;
        border-left: 5px solid #007bff;
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
    </style>
    """, unsafe_content_allowed=True)

# Sidebar Content
st.sidebar.markdown("# 👨‍💻 My Profile")
st.sidebar.info("Experience: **10+ Years**")
st.sidebar.markdown("---")
st.sidebar.markdown("### 📞 Contact Details")
st.sidebar.write("📧 Email: your-email@example.com")
st.sidebar.write("🏠 Address: 356/14, Naleen Jayasinghe Road, Pilagoda, Baddegama.")
st.sidebar.write("📅 DOB: 18th April 1988")

# Main Header
col1, col2 = st.columns([1, 4])
with col1:
    st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=160)
with col2:
    st.title("Dinesh Isuru Sampath")
    st.subheader("Senior Software Developer & ML Systems Specialist")
    st.write("A results-driven engineer with a decade of experience in crafting scalable web applications and high-performance machine learning infrastructures.")

st.divider()

# Core Skills Section
st.header("🛠 Tech Stack & Expertise")
st.markdown("""
<div style='line-height: 2;'>
    <span class="skill-tag">Python (Expert)</span>
    <span class="skill-tag">JavaScript</span>
    <span class="skill-tag">HTML5 / CSS3</span>
    <span class="skill-tag">Machine Learning</span>
    <span class="skill-tag">System Architecture</span>
    <span class="skill-tag">Git / GitHub</span>
    <span class="skill-tag">Production-Grade Deployment</span>
</div>
""", unsafe_content_allowed=True)

st.divider()

# Experience Section
st.header("💼 Professional Journey")

st.markdown(f"""
<div class="job-card">
    <h3>Senior Full-Stack Developer (10 Years Experience)</h3>
    <p><strong>Professional Mastery:</strong> Over 10 years of hands-on experience in the software industry. 
    Proven track record of designing, building, and maintaining production-ready systems.</p>
    <ul>
        <li>Expert in <b>Python</b> for backend logic and automation.</li>
        <li>Specialized in building interactive web frontends using <b>JavaScript</b> and <b>HTML</b>.</li>
        <li>Deep understanding of <b>Scalable Architecture</b> and shipping production-grade systems.</li>
    </ul>
</div>
""", unsafe_content_allowed=True)

# Projects Section (Connecting your app.py)
st.header("🚀 Key Projects")
col_p1, col_p2 = st.columns(2)

with col_p1:
    with st.expander("Production-Grade ML Script (app.py)", expanded=True):
        st.write("A core implementation of machine learning workflows, focusing on data processing and high-efficiency model deployment.")
        st.markdown("[🔗 View on GitHub](https://github.com/your-username-here)") # මෙතනට ඔබේ GitHub ලින්ක් එක දාන්න

with col_p2:
    with st.expander("Cricket Performance Analytics"):
        st.write("An analytical tool designed to process sports data, providing insights into team performances and match statistics.")
        # Simple Chart Placeholder
        chart_data = pd.DataFrame({'Stat': ['Win Rate', 'Efficiency', 'Accuracy'], 'Value': [85, 92, 88]})
        st.bar_chart(chart_data, x='Stat', y='Value')

st.divider()

# Practical Experience Note
st.header("🎓 Academic & Practical Foundation")
st.success("**Equivalent Practical Experience (EPE):** Recognized as a Senior Engineer based on 10 years of verified industry experience in Python and Web Technologies.")
st.write("Education: G.C.E. Advanced Level (A/L) and Ordinary Level (O/L).")

# Footer
st.markdown("---")
st.center_text = st.markdown("<p style='text-align: center;'>Built with ❤️ by Dinesh Isuru | 2026</p>", unsafe_content_allowed=True)
