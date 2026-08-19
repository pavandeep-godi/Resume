import streamlit as st

# Set page config (if this is part of your main app script)
st.set_page_config(
    page_title="Professional Summary", page_icon="💼", layout="wide"
)

# Heading
st.title("👨‍💻 Professional Summary")

# Professional Summary Content Block
summary_text = """
**Analytics & Insights Engineer (7+ years)** focused on turning messy data into reliable analytics. 

* **ETL & Data Pipelines:** Build and maintain SQL/Python + KNIME-based ETL pipelines, validate data quality, and engineer robust datasets.
* **Dashboards & Reporting:** Deliver Tableau dashboards + KPI datasets used directly by cross-functional business teams across Sales and Finance.
* **Process Automation:** Proven track record of migrating workflows from manual/Alteryx processes into automated pipelines, reducing report turnaround time and ad-hoc load by **double digits**.
"""

# Render in a clean card container
with st.container(border=True):
    st.markdown(summary_text)

# Quick Highlight Metrics
col1, col2, col3 = st.columns(3)
col1.metric(label="Experience", value="7+ Years")
col2.metric(label="Core Stack", value="SQL • Python • KNIME")
col3.metric(label="Impact", value="Double-Digit %", delta="Turnaround Speed")