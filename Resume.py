import pandas as pd
import plotly.express as px
import streamlit as st

# 1. Page Configuration
st.set_page_config(
    page_title="Godi Pavan Deep | Analytics & Insights Engineer",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

# 2. Modern Clean CSS
st.markdown(
    """
    <style>
    /* Main Canvas */
    .stApp {
        background-color: #F8FAFC;
    }
    
    /* Header Typography (Enlarged Name & Title) */
    .candidate-name {
        font-size: 3.0rem;
        font-weight: 800;
        color: #0F172A;
        letter-spacing: -0.8px;
        margin-bottom: 2px;
        line-height: 1.1;
    }
    .candidate-title {
        font-size: 1.4rem;
        font-weight: 600;
        color: #0284C7;
        margin-top: 4px;
        margin-bottom: 12px;
    }
    
    /* Recruiter Snapshot Cards */
    .snapshot-card {
        background-color: #FFFFFF;
        border: 1px solid #E2E8F0;
        border-radius: 10px;
        padding: 14px 16px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.03);
        height: 100%;
    }
    .snapshot-label {
        font-size: 0.72rem;
        font-weight: 700;
        text-transform: uppercase;
        color: #64748B;
        letter-spacing: 0.6px;
        margin-bottom: 4px;
    }
    .snapshot-value {
        font-size: 0.95rem;
        font-weight: 700;
        color: #0F172A;
        line-height: 1.3;
    }
    .snapshot-sub {
        font-size: 0.8rem;
        color: #64748B;
        margin-top: 3px;
    }

    /* Custom Skill Badges */
    .skill-badge {
        background-color: #F0F9FF;
        color: #0369A1;
        border: 1px solid #BAE6FD;
        padding: 5px 12px;
        border-radius: 6px;
        font-size: 0.85rem;
        font-weight: 600;
        display: inline-block;
        margin: 3px 2px;
    }
    
    /* Experience Headers */
    .company-title {
        font-size: 1.15rem;
        font-weight: 700;
        color: #0F172A;
    }
    .role-dates {
        font-size: 0.9rem;
        font-weight: 600;
        color: #0284C7;
        text-align: right;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# ---------------------------------------------------------
# 3. Sidebar Configuration
# ---------------------------------------------------------
with st.sidebar:
    st.image(
        "https://api.dicebear.com/7.x/initials/svg?seed=GD&backgroundColor=0284c7",
        width=90,
    )
    st.markdown("### **Godi Pavan Deep**")
    st.caption("📍 Hyderabad, India | Open to Opportunities")

    st.markdown("---")
    st.markdown("#### 📞 Contact Information")
    st.markdown("📧 **Email:** [pavandeep459@gmail.com](mailto:pavandeep459@gmail.com)")
    st.markdown("📱 **Phone:** +91 8099490199")
    st.markdown("💼 **LinkedIn:** [linkedin.com/in/pavan-deep-godi](https://www.linkedin.com/in/pavan-deep-godi-3aa8ba16a/)")
    st.markdown("💻 **GitHub:** [github.com/pavandeep-godi](https://github.com/pavandeep-godi)")

    st.markdown("---")
    st.markdown("#### ⚡ Core Stack Summary")
    st.markdown(
        """
    - **Languages:** SQL, Python
    - **ETL/ELT:** KNIME, AWS Glue, Alteryx, IBM DataStage
    - **Visualization:** Tableau, Power BI
    - **Data Stores:** AWS (Athena), SQL Server
    """
    )


# ---------------------------------------------------------
# 4. Main Header
# ---------------------------------------------------------
col_header, col_contact = st.columns([7, 3])

with col_header:
    st.markdown('<div class="candidate-name">GODI PAVAN DEEP</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="candidate-title">Analytics & Insights Engineer (7+ Years Experience)</div>',
        unsafe_allow_html=True,
    )

with col_contact:
    st.markdown(
        """
    <div style="text-align: right; font-size: 0.95rem; color: #334155; padding-top: 8px;">
        📧 <b>pavandeep459@gmail.com</b> &nbsp;|&nbsp; 📱 <b>+91 8099490199</b><br>
        💼 <a href="https://www.linkedin.com/in/pavan-deep-godi-3aa8ba16a/" target="_blank" style="color:#0284C7; text-decoration:none;">LinkedIn Profile</a> &nbsp;|&nbsp; 
        💻 <a href="https://github.com/pavandeep-godi" target="_blank" style="color:#0284C7; text-decoration:none;">GitHub Profile</a>
    </div>
    """,
        unsafe_allow_html=True,
    )

st.markdown("<br>", unsafe_allow_html=True)

# ---------------------------------------------------------
# 5. Recruiter Quick-Snapshot Cards
# ---------------------------------------------------------
c1, c2, c3, c4 = st.columns(4)

with c1:
    st.markdown(
        """
        <div class="snapshot-card">
            <div class="snapshot-label">Primary Specialization</div>
            <div class="snapshot-value">Analytics Engineering</div>
            <div class="snapshot-sub">ETL Pipelines & BI Data Modeling</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with c2:
    st.markdown(
        """
        <div class="snapshot-card">
            <div class="snapshot-label">Career Progression</div>
            <div class="snapshot-value">7+ Years Track Record</div>
            <div class="snapshot-sub">Deloitte • Solenis • TCS</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with c3:
    st.markdown(
        """
        <div class="snapshot-card">
            <div class="snapshot-label">Core Tech Stack</div>
            <div class="snapshot-value">SQL • Python • KNIME</div>
            <div class="snapshot-sub">Tableau • AWS (Athena/Glue)</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with c4:
    st.markdown(
        """
        <div class="snapshot-card">
            <div class="snapshot-label">Domain Focus</div>
            <div class="snapshot-value">Sales & Finance Analytics</div>
            <div class="snapshot-sub">Workflow Migration & Automation</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown("<br>", unsafe_allow_html=True)

# Executive Summary Container
with st.container(border=True):
    st.markdown("#### **📌 Professional Profile**")
    st.write(
        """
        **Analytics & Insights Engineer (7+ years)** focused on turning messy data into reliable analytics. Build and maintain 
        **SQL/Python + KNIME-based ETL pipelines**, validate data quality, and deliver **Tableau dashboards + KPI datasets** used by 
        business teams across sales and finance. Experience migrating workflows from manual/Alteryx processes into automated 
        pipelines, reducing report turnaround time and ad-hoc load by double digits.
        """
    )

st.markdown("<br>", unsafe_allow_html=True)

# ---------------------------------------------------------
# 6. Structured Tabs Layout
# ---------------------------------------------------------
tab_exp, tab_skills, tab_impact = st.tabs(
    ["💼 Professional Experience", "🛠️ Technical Skills & Tools", "📊 Migration & Impact Highlights"]
)

# ---------------------------------------------------------
# TAB 1: WORK EXPERIENCE
# ---------------------------------------------------------
with tab_exp:
    # Role 1: Deloitte
    with st.container(border=True):
        c1, c2 = st.columns([3, 1])
        with c1:
            st.markdown(
                '<div class="company-title">Analytics & Insights Engineer &nbsp;|&nbsp; <span style="color:#475569; font-weight:500;">Deloitte</span></div>',
                unsafe_allow_html=True,
            )
        with c2:
            st.markdown(
                '<div class="role-dates">June 2024 – Present</div>',
                unsafe_allow_html=True,
            )

        st.markdown(
            """
        * **ETL Migration & Optimization:** Converted **15+ Alteryx workflows into KNIME-based ETL**, consolidating repeated transformations into reusable nodes to support cost optimization and consistent dataset outputs.
        * **Pipeline Automation:** Built and automated **20+ ingestion pipelines** with standardized input formats and transformation steps, cutting pipeline runtime and making releases repeatable across parallel projects.
        * **Large-Scale Data Migrations:** Executed enterprise migrations across testing and production cycles using **IBM DataStage** and **SAP LSMW**, resolving quality anomalies for two distinct projects.
        * **Self-Serve Dashboarding:** Delivered an interactive **Tableau self-serve dashboard for Cash Plus Pilot** (30+ client users), backed by automated datasets; reduced manual reporting requests by **60%** within the pilot period.
        * **Executive KPI Redesign:** Rebuilt the Sales Executive KPI dashboard with clearer metric definitions and consistent filters, reducing ad-hoc query volume by **40%**.
        * **Process Automation:** Automated the generation of Tableau-ready charts from recurring Excel templates, saving **~90 minutes/month** of manual rebuild work.
        * **End-to-End Quality Ownership:** Owned end-to-end delivery from dataset design → pipeline automation → validation → dashboard deployment. Triaged and fixed **12+ dashboard/data defects per release cycle**, ensuring post-migration data accuracy.
        """
        )

    # Role 2: Solenis
    with st.container(border=True):
        c1, c2 = st.columns([3, 1])
        with c1:
            st.markdown(
                '<div class="company-title">Senior Data Analyst 2 &nbsp;|&nbsp; <span style="color:#475569; font-weight:500;">Solenis</span></div>',
                unsafe_allow_html=True,
            )
        with c2:
            st.markdown(
                '<div class="role-dates">November 2021 – May 2024</div>',
                unsafe_allow_html=True,
            )

        st.markdown(
            """
        * **Working Capital Analytics:** Built a working capital cash-flow dashboard and refined KPI definitions based on stakeholder feedback, increasing adoption/usage by **30%**.
        * **Executive Reviews:** Developed an executive KPI dashboard for weekly performance reviews, improving visibility into core operational metrics and trends.
        * **Leadership Reporting:** Produced monthly executive performance decks using standardized SQL extracts, translating operational data trends into actions and targets for leadership.
        * **Cost Reduction Discovery:** Co-developed an interactive analytics view that surfaced **$450K+ cost reduction opportunities** by segmenting spend/performance drivers and enabling targeted operational actions.
        * **Ad-Hoc Logic Reusability:** Partnered with business owners for ad-hoc analytics requests, converting one-off questions into reusable datasets/KPI logic to reduce repeat work.
        * **Stakeholder Training:** Trained stakeholders on dashboard usage and metric definitions, improving engagement by **5–10%** post-session.
        """
        )

    # Role 3: TCS
    with st.container(border=True):
        c1, c2 = st.columns([3, 1])
        with c1:
            st.markdown(
                '<div class="company-title">Data Analyst &nbsp;|&nbsp; <span style="color:#475569; font-weight:500;">TCS</span></div>',
                unsafe_allow_html=True,
            )
        with c2:
            st.markdown(
                '<div class="role-dates">April 2019 – November 2021</div>',
                unsafe_allow_html=True,
            )

        st.markdown(
            """
        * **Cloud Data Processing:** Built a **PySpark ETL proof of concept on AWS** to separate and analyze historical vs current datasets, enabling faster analysis-ready extracts for the team.
        * **Operations Dashboards:** Developed Tableau-KPI dashboards for operations leadership, surfacing key trends weekly.
        * **Python Automation:** Replaced repetitive Excel workflows with Python automation, reducing manual effort and errors by **~60%** for recurring reporting tasks.
        """
        )

# ---------------------------------------------------------
# TAB 2: SKILLS & TOOLS
# ---------------------------------------------------------
with tab_skills:
    col_s1, col_s2 = st.columns(2)

    with col_s1:
        st.markdown("#### **Skill Categories & Toolset**")

        skills_dict = {
            "BI & Visualization": ["Tableau", "Power BI", "Tableau Prep"],
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
                [f'<span class="skill-badge">{item}</span>' for item in items]
            )
            st.markdown(badge_html, unsafe_allow_html=True)
            st.markdown("<div style='margin-bottom: 10px;'></div>", unsafe_allow_html=True)

    with col_s2:
        st.markdown("#### **Technical Mastery Breakdown**")

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
                "Relative Depth (%)": [95, 90, 88, 85, 75, 80, 70],
                "Domain": [
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

        slate_palette = ["#334155", "#0284C7", "#475569", "#0EA5E9", "#64748B"]

        fig_skills = px.bar(
            skill_df,
            x="Relative Depth (%)",
            y="Tool",
            color="Domain",
            orientation="h",
            color_discrete_sequence=slate_palette,
        )
        fig_skills.update_layout(
            height=340,
            xaxis_title="Proficiency & Project Exposure (%)",
            yaxis_title="",
            margin=dict(l=0, r=0, t=10, b=10),
        )
        st.plotly_chart(fig_skills, use_container_width=True)

# ---------------------------------------------------------
# TAB 3: IMPACT & MIGRATION HIGHLIGHTS
# ---------------------------------------------------------
with tab_impact:
    st.markdown("#### **Quantifiable Engineering Achievements**")

    impact_table = pd.DataFrame(
        {
            "Project Initiative": [
                "Deloitte Cash Plus Pilot",
                "Deloitte Sales KPI Redesign",
                "TCS Reporting Automation",
                "Solenis Dashboard Adoption",
                "Deloitte Chart Generation",
                "Solenis Spend Analytics",
            ],
            "Quantifiable Outcome": [
                "60% Reduction in Manual Requests",
                "40% Reduction in Ad-Hoc Query Volume",
                "60% Reduction in Manual Effort & Errors",
                "30% Increase in User Adoption",
                "90 Minutes/Month Saved",
                "$450K+ Cost Reduction Opportunities Surfaced",
            ],
            "Primary Domain": [
                "Finance / Cash Flow",
                "Sales Analytics",
                "Operations",
                "Finance / Working Capital",
                "Reporting Automation",
                "Procurement / Spend",
            ],
        }
    )

    st.dataframe(
        impact_table,
        use_container_width=True,
        hide_index=True,
    )

    st.markdown("<br>", unsafe_allow_html=True)
    with st.container(border=True):
        st.markdown("#### **Key Migration & Automation Highlights**")
        st.markdown(
            """
        * **15+ Alteryx Workflows Migrated:** Converted complex Alteryx ETL into reusable KNIME nodes to support cost optimization and standardized outputs.
        * **20+ Automated Ingestion Pipelines:** Built with standardized input formats and transformation steps to enable repeatable releases across parallel projects.
        * **12+ Defects Triaged per Release:** Ensured post-migration accuracy and prevented stale metric outputs across enterprise testing and production cycles.
        """
        )