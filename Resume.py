import pandas as pd
import plotly.express as px
import streamlit as st

# 1. Page Configuration
st.set_page_config(
    page_title="Analytics & Insights Engineer Portfolio",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Custom CSS for polished styling
st.markdown(
    """
    <style>
    .main-title {
        font-size: 2.4rem;
        font-weight: 700;
        color: #1E293B;
        margin-bottom: 0px;
    }
    .sub-title {
        font-size: 1.3rem;
        font-weight: 500;
        color: #0284C7;
        margin-bottom: 15px;
    }
    .contact-info {
        font-size: 0.95rem;
        color: #475569;
        margin-bottom: 25px;
    }
    .section-header {
        font-size: 1.4rem;
        font-weight: 600;
        color: #0F172A;
        border-bottom: 2px solid #E2E8F0;
        padding-bottom: 5px;
        margin-top: 15px;
        margin-bottom: 15px;
    }
    .company-header {
        font-size: 1.15rem;
        font-weight: 600;
        color: #1E293B;
    }
    .role-date {
        font-size: 0.95rem;
        font-weight: 500;
        color: #64748B;
        text-align: right;
    }
    .skill-badge {
        background-color: #F1F5F9;
        color: #334155;
        padding: 4px 10px;
        border-radius: 6px;
        font-size: 0.85rem;
        font-weight: 500;
        display: inline-block;
        margin: 2px;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# ---------------------------------------------------------
# 2. Sidebar Setup
# ---------------------------------------------------------
with st.sidebar:
    st.image(
        "https://api.dicebear.com/7.x/initials/svg?seed=AE&backgroundColor=0284c7",
        width=100,
    )
    st.markdown("### **Analytics & Insights Engineer**")
    st.caption("📍 Hyderabad, India | Open to Opportunities")

    st.markdown("---")
    st.markdown("### 📞 Contact Details")
    st.markdown("📧 **Email:** [your.email@example.com](mailto:your.email@example.com)")
    st.markdown("📱 **Phone:** +91 98765 43210")
    st.markdown("💼 **LinkedIn:** [linkedin.com/in/yourprofile](https://linkedin.com)")
    st.markdown("💻 **GitHub:** [github.com/yourprofile](https://github.com)")

    st.markdown("---")
    st.markdown("### 🧰 Core Stack Quick View")
    st.markdown(
        """
    - **Languages:** SQL, Python
    - **ETL/ELT:** KNIME, AWS Glue, Alteryx
    - **Visualization:** Tableau, Power BI
    - **Data Stores:** AWS Athena, SQL Server
    """
    )


# ---------------------------------------------------------
# 3. Header & Professional Summary
# ---------------------------------------------------------
col_header, col_contact = st.columns([3, 2])

with col_header:
    st.markdown('<p class="main-title">YOUR NAME</p>', unsafe_allow_html=True)
    st.markdown(
        '<p class="sub-title">Analytics & Insights Engineer (7+ Years)</p>',
        unsafe_allow_html=True,
    )

with col_contact:
    st.markdown(
        """
    <div style="text-align: right; padding-top: 10px;">
        📧 <b>your.email@example.com</b> | 📱 <b>+91 98765 43210</b><br>
        💼 <a href="https://linkedin.com" target="_blank">LinkedIn</a> | 💻 <a href="https://github.com" target="_blank">GitHub</a>
    </div>
    """,
        unsafe_allow_html=True,
    )

st.markdown("---")

# Key Impact Metric Cards
m1, m2, m3, m4 = st.columns(4)
m1.metric("Experience", "7+ Years", "Data & ETL Pipelines")
m2.metric("Workflow Migration", "15+ Workflows", "Alteryx ➔ KNIME")
m3.metric("Cost Savings Impact", "$450K+", "Solenis Spend Analytics")
m4.metric("Reporting Efficiency", "60% Reduction", "In Manual Requests")

st.markdown("<br>", unsafe_allow_html=True)

# Executive Summary Container
with st.container(border=True):
    st.markdown("#### **📌 Professional Profile**")
    st.write(
        """
        **Analytics & Insights Engineer** with over 7 years of experience focused on turning messy data into reliable, automated analytics. 
        Specialized in building and maintaining **SQL/Python + KNIME-based ETL pipelines**, validating data quality, and delivering **Tableau dashboards** 
        and KPI datasets used by cross-functional sales and finance teams. Proven track record of migrating workflows from manual/Alteryx processes into 
        automated pipelines, reducing report turnaround times and ad-hoc query loads by double digits.
        """
    )


# ---------------------------------------------------------
# 4. Main Tabs Layout
# ---------------------------------------------------------
tab_exp, tab_skills, tab_impact = st.tabs(
    ["💼 Professional Experience", "🛠️ Skills & Tools", "📈 Impact Breakdown"]
)

# ---------------------------------------------------------
# TAB 1: WORK EXPERIENCE
# ---------------------------------------------------------
with tab_exp:
    st.markdown('<p class="section-header">Career History</p>', unsafe_allow_html=True)

    # --- Role 1: Deloitte ---
    with st.container(border=True):
        c1, c2 = st.columns([3, 1])
        with c1:
            st.markdown(
                "### **Analytics & Insights Engineer** — *Deloitte*"
            )
        with c2:
            st.markdown(
                '<p class="role-date">June 2024 – Present</p>',
                unsafe_allow_html=True,
            )

        st.markdown(
            """
        * **ETL Migration & Optimization:** Converted **15+ Alteryx workflows into KNIME-based ETL**, consolidating repeated transformations into reusable nodes to support cost optimization and consistent dataset outputs.
        * **Pipeline Automation:** Built and automated **20+ ingestion pipelines** with standardized input formats and transformation steps, cutting pipeline runtime and enabling repeatable releases across parallel projects.
        * **Large-Scale Data Migrations:** Executed enterprise migrations across testing and production cycles using **IBM DataStage** and **SAP LSMW**, resolving quality anomalies across two distinct client projects.
        * **Self-Serve Dashboarding:** Delivered an interactive **Tableau self-serve dashboard for Cash Plus Pilot** (30+ client users), reducing manual reporting requests by **60%** within the pilot period.
        * **Executive KPI Redesign:** Rebuilt the Sales Executive KPI dashboard with clearer metric definitions and consistent filters, reducing ad-hoc query volume by **40%**.
        * **Process Automation:** Automated generation of Tableau-ready charts from recurring Excel templates, saving **~90 minutes/month** of manual rebuild work.
        * **End-to-End Delivery & Quality:** Owned complete lifecycles (Dataset Design ➔ Pipeline Automation ➔ Validation ➔ Dashboard Deployment). Triaged and fixed **12+ dashboard/data defects per release cycle**.
        """
        )

    # --- Role 2: Solenis ---
    with st.container(border=True):
        c1, c2 = st.columns([3, 1])
        with c1:
            st.markdown("### **Senior Data Analyst 2** — *Solenis*")
        with c2:
            st.markdown(
                '<p class="role-date">November 2021 – May 2024</p>',
                unsafe_allow_html=True,
            )

        st.markdown(
            """
        * **Working Capital Analytics:** Built a working capital cash-flow dashboard and refined KPI definitions based on stakeholder feedback, increasing adoption and usage by **30%**.
        * **Executive Reviews:** Developed an executive KPI dashboard for weekly performance reviews, improving visibility into core operational metrics and trends.
        * **Leadership Reporting:** Produced monthly executive performance decks using standardized SQL extracts, translating operational data trends into strategic actions for leadership.
        * **Cost Reduction Discovery:** Co-developed an interactive analytics view that surfaced **$450K+ in cost reduction opportunities** by segmenting spend and performance drivers.
        * **Stakeholder Enablement:** Converted ad-hoc business requests into reusable datasets/KPI logic to reduce repeat requests, and trained stakeholders on metric definitions (boosting post-session engagement by 5–10%).
        """
        )

    # --- Role 3: TCS ---
    with st.container(border=True):
        c1, c2 = st.columns([3, 1])
        with c1:
            st.markdown("### **Data Analyst** — *TCS*")
        with c2:
            st.markdown(
                '<p class="role-date">April 2019 – November 2021</p>',
                unsafe_allow_html=True,
            )

        st.markdown(
            """
        * **Cloud Data Processing:** Built a **PySpark ETL proof of concept on AWS** to separate and analyze historical vs. current datasets, enabling faster analysis-ready extracts.
        * **Operations Dashboards:** Developed Tableau KPI dashboards for operations leadership, surfacing key operational trends weekly.
        * **Python Automation:** Replaced repetitive Excel workflows with Python scripts, reducing manual effort and errors by **~60%** for recurring reporting tasks.
        """
        )

# ---------------------------------------------------------
# TAB 2: SKILLS & TOOLS
# ---------------------------------------------------------
with tab_skills:
    st.markdown(
        '<p class="section-header">Technical Skill Matrix</p>',
        unsafe_allow_html=True,
    )

    col_s1, col_s2 = st.columns(2)

    with col_s1:
        st.markdown("#### **Core Competency Categories**")

        skills_dict = {
            "BI & Visualization": ["Tableau", "Power BI"],
            "Analytics Engineering & Migration": [
                "KNIME",
                "AWS Glue",
                "IBM DataStage",
                "Alteryx",
                "SAP LSMW",
            ],
            "Programming & Querying": ["Python", "SQL", "PySpark (POC)"],
            "Data Prep & Analytics": ["Tableau Prep", "Advanced Excel"],
            "Data Platforms": ["AWS (Athena)", "SQL Server"],
            "Continuous Learning / Projects": ["dbt", "Snowflake"],
        }

        for category, items in skills_dict.items():
            st.markdown(f"**{category}**")
            badge_html = "".join(
                [
                    f'<span class="skill-badge">{item}</span>'
                    for item in items
                ]
            )
            st.markdown(badge_html, unsafe_allow_html=True)
            st.markdown("<div style='margin-bottom: 12px;'></div>", unsafe_allow_html=True)

    with col_s2:
        st.markdown("#### **Tool Mastery Distribution**")

        # Proficiency Visualization for interactive presentation
        skill_df = pd.DataFrame(
            {
                "Tool": [
                    "SQL",
                    "Tableau",
                    "Python",
                    "KNIME",
                    "AWS (Athena/Glue)",
                    "Alteryx",
                    "Power BI",
                ],
                "Experience Weight": [95, 90, 88, 85, 75, 80, 70],
                "Category": [
                    "Database",
                    "BI",
                    "Code",
                    "ETL",
                    "Cloud",
                    "ETL",
                    "BI",
                ],
            }
        )

        fig_skills = px.bar(
            skill_df,
            x="Experience Weight",
            y="Tool",
            color="Category",
            orientation="h",
            text="Tool",
            color_discrete_sequence=px.colors.qualitative.Blues_r,
        )
        fig_skills.update_layout(
            height=350,
            xaxis_title="Proficiency & Usage Focus (%)",
            yaxis_title="",
            showlegend=True,
            margin=dict(l=0, r=0, t=20, b=20),
        )
        st.plotly_chart(fig_skills, use_container_width=True)

# ---------------------------------------------------------
# TAB 3: IMPACT METRICS
# ---------------------------------------------------------
with tab_impact:
    st.markdown(
        '<p class="section-header">Quantifiable Engineering Outcomes</p>',
        unsafe_allow_html=True,
    )

    impact_data = pd.DataFrame(
        {
            "Initiative": [
                "Deloitte Cash Plus Pilot",
                "Deloitte Sales KPI Redesign",
                "TCS Reporting Automation",
                "Solenis Dashboard Adoption",
                "Deloitte Monthly Rebuilds",
            ],
            "Metric Improved": [
                "Manual Requests",
                "Ad-hoc Query Volume",
                "Manual Effort & Errors",
                "User Adoption",
                "Time Saved",
            ],
            "Percentage / Value": [60, 40, 60, 30, 90],
            "Unit": ["% Reduction", "% Reduction", "% Reduction", "% Increase", "Mins/Month Saved"],
        }
    )

    fig_impact = px.bar(
        impact_data,
        x="Initiative",
        y="Percentage / Value",
        color="Metric Improved",
        text="Percentage / Value",
        title="Key Quantifiable Achievements across Roles",
        color_discrete_sequence=px.colors.qualitative.Pastel,
    )
    fig_impact.update_traces(
        texttemplate="%{text}", textposition="outside"
    )
    fig_impact.update_layout(height=400, yaxis_title="Impact Score / Value")
    st.plotly_chart(fig_impact, use_container_width=True)

    st.markdown(
        """
    > **Summary of Key Achievements:**
    > * **$450K+** Cost reduction opportunities surfaced at Solenis via spend driver segmentation.
    > * **15+** Alteryx workflows migrated to KNIME at Deloitte to reduce license dependencies and standardize pipelines.
    > * **20+** Automated data ingestion pipelines built to achieve repeatable, low-latency releases.
    """
    )