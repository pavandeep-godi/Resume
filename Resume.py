import pandas as pd
import streamlit as st

# 1. Page Configuration
st.set_page_config(
    page_title="Godi Pavan Deep | Analytics & Insights Engineer",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

# 2. Modern Clean & Professional CSS
st.markdown(
    """
    <style>
    /* Force Light Color Scheme for Consistent Contrast */
    :root {
        color-scheme: light !important;
    }

    /* Main App Canvas */
    .stApp {
        background-color: #F8FAFC !important;
        color: #0F172A !important;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    }

    /* Left Sidebar Redesign */
    [data-testid="stSidebar"] {
        background-color: #FFFFFF !important;
        border-right: 1px solid #E2E8F0 !important;
        box-shadow: 2px 0 8px rgba(0, 0, 0, 0.02);
    }
    [data-testid="stSidebar"] * {
        color: #0F172A !important;
    }

    .sidebar-profile {
        text-align: center;
        padding: 20px 10px 10px 10px;
    }
    .sidebar-avatar {
        border-radius: 50%;
        border: 3px solid #0284C7;
        padding: 3px;
        background-color: #FFFFFF;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
    }
    .sidebar-name {
        font-size: 1.25rem;
        font-weight: 700;
        color: #0F172A !important;
        margin-top: 12px;
        margin-bottom: 2px;
        letter-spacing: -0.3px;
    }
    .sidebar-role {
        font-size: 0.85rem;
        font-weight: 600;
        color: #0284C7 !important;
        margin-bottom: 6px;
    }
    .sidebar-location {
        font-size: 0.8rem;
        color: #64748B !important;
        font-weight: 500;
    }

    /* Core Focus Card in Sidebar */
    .sidebar-focus-box {
        background-color: #F1F5F9;
        border-radius: 8px;
        padding: 14px;
        margin-top: 12px;
        border-left: 3px solid #0284C7;
    }
    .sidebar-focus-title {
        font-size: 0.8rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        color: #475569 !important;
        margin-bottom: 8px;
    }

    /* Main Header Typography */
    .candidate-name {
        font-size: 2.6rem;
        font-weight: 800;
        color: #0F172A !important;
        letter-spacing: -0.8px;
        line-height: 1.1;
    }
    .candidate-title {
        font-size: 1.25rem;
        font-weight: 600;
        color: #0284C7 !important;
        margin-top: 4px;
        margin-bottom: 8px;
    }

    /* Single-Line Contact Details Bar */
    .contact-bar {
        display: flex;
        justify-content: flex-end;
        align-items: center;
        gap: 12px;
        font-size: 0.9rem;
        color: #334155 !important;
        padding-top: 10px;
        white-space: nowrap;
    }
    .contact-bar a {
        color: #0284C7 !important;
        text-decoration: none;
        font-weight: 600;
    }
    .contact-bar a:hover {
        text-decoration: underline;
    }

    /* Recruiter Quick-Snapshot Cards */
    .snapshot-card {
        background-color: #FFFFFF !important;
        border: 1px solid #E2E8F0 !important;
        border-radius: 10px;
        padding: 16px;
        box-shadow: 0 1px 3px rgba(15, 23, 42, 0.04);
        height: 100%;
        transition: transform 0.15s ease-in-out;
    }
    .snapshot-label {
        font-size: 0.72rem;
        font-weight: 700;
        text-transform: uppercase;
        color: #64748B !important;
        letter-spacing: 0.6px;
        margin-bottom: 6px;
    }
    .snapshot-value {
        font-size: 1.0rem;
        font-weight: 700;
        color: #0F172A !important;
        line-height: 1.3;
    }
    .snapshot-sub {
        font-size: 0.8rem;
        color: #475569 !important;
        margin-top: 4px;
    }

    /* Custom Streamlit Container Elevation */
    div[data-testid="stVerticalBlockBorderWrapper"] {
        background-color: #FFFFFF !important;
        border: 1px solid #E2E8F0 !important;
        border-radius: 10px !important;
        box-shadow: 0 1px 3px rgba(15, 23, 42, 0.03) !important;
    }
    div[data-testid="stVerticalBlockBorderWrapper"] * {
        color: #0F172A !important;
    }

    /* Custom Skill Badges */
    .skill-badge {
        background-color: #F1F5F9 !important;
        color: #0F172A !important;
        border: 1px solid #CBD5E1 !important;
        padding: 6px 14px;
        border-radius: 6px;
        font-size: 0.88rem;
        font-weight: 600;
        display: inline-block;
        margin: 4px 3px;
    }

    /* Tab Styling */
    button[data-baseweb="tab"] {
        background-color: transparent !important;
        color: #64748B !important;
        font-weight: 600 !important;
        font-size: 0.95rem !important;
        padding: 10px 16px !important;
    }
    button[data-baseweb="tab"][aria-selected="true"] {
        color: #0284C7 !important;
        border-bottom-color: #0284C7 !important;
        border-bottom-width: 2px !important;
    }

    /* Table Styling Override */
    div[data-testid="stDataFrame"] {
        background-color: #FFFFFF !important;
        border-radius: 8px !important;
        border: 1px solid #E2E8F0 !important;
    }

    /* Experience Headers */
    .company-title {
        font-size: 1.15rem;
        font-weight: 700;
        color: #0F172A !important;
    }
    .role-dates {
        font-size: 0.9rem;
        font-weight: 600;
        color: #0284C7 !important;
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
    st.markdown(
        """
        <div class="sidebar-profile">
            <img class="sidebar-avatar" src="https://api.dicebear.com/7.x/initials/svg?seed=GD&backgroundColor=0284c7" width="90">
            <div class="sidebar-name">Godi Pavan Deep</div>
            <div class="sidebar-role">Analytics & Insights Engineer</div>
            <div class="sidebar-location">📍 Hyderabad, India</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="sidebar-focus-box">
            <div class="sidebar-focus-title">⚡ Core Technical Expertise</div>
            <div style="font-size: 0.85rem; color: #334155; line-height: 1.6;">
                • <b>Pipelines:</b> SQL, Python, KNIME<br>
                • <b>Data Platforms:</b> AWS, DataStage, SAP<br>
                • <b>BI & Visuals:</b> Tableau, Power BI<br>
                • <b>Domains:</b> Sales, Finance & Ops
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("<br>", unsafe_allow_html=True)
    st.caption("✨ Built with Streamlit")


# ---------------------------------------------------------
# 4. Main Header
# ---------------------------------------------------------
col_header, col_contact = st.columns([6, 4])

with col_header:
    st.markdown('<div class="candidate-name">GODI PAVAN DEEP</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="candidate-title">Analytics & Insights Engineer (7+ Years Experience)</div>',
        unsafe_allow_html=True,
    )

with col_contact:
    st.markdown(
        """
    <div class="contact-bar">
        <span>📧 <b>pavandeep459@gmail.com</b></span>
        <span>|</span>
        <span>📱 <b>+91 8099490199</b></span>
        <span>|</span>
        <a href="https://www.linkedin.com/in/pavan-deep-godi-3aa8ba16a/" target="_blank">LinkedIn</a>
        <span>|</span>
        <a href="https://github.com/pavandeep-godi" target="_blank">GitHub</a>
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
    st.markdown("#### **📌 Executive Summary**")
    st.write(
        """
        **Analytics & Insights Engineer (7+ years)** focused on turning complex raw data into reliable business intelligence. 
        Specialized in building and scaling **SQL/Python + KNIME-based ETL pipelines**, enforcing rigorous data quality standards, 
        and deploying **Tableau dashboards & KPI models** for executive leadership across sales and finance operations. 
        Proven track record of migrating legacy/manual reporting into fully automated cloud-supported workflows.
        """
    )

st.markdown("<br>", unsafe_allow_html=True)

# ---------------------------------------------------------
# 6. Structured Tabs Layout
# ---------------------------------------------------------
tab_exp, tab_skills, tab_impact = st.tabs(
    ["💼 Professional Experience", "🛠️ Technical Skills & Tools", "📊 Impact Highlights"]
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
                '<div class="company-title">Analytics & Insights Engineer &nbsp;|&nbsp; Deloitte</div>',
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
                '<div class="company-title">Senior Data Analyst 2 &nbsp;|&nbsp; Solenis</div>',
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
                '<div class="company-title">Data Analyst &nbsp;|&nbsp; TCS</div>',
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
    with st.container(border=True):
        st.markdown("#### **Technical Skill Matrix & Toolset**")
        st.markdown("<br>", unsafe_allow_html=True)

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

        col1, col2 = st.columns(2)
        items_list = list(skills_dict.items())

        with col1:
            for category, items in items_list[:3]:
                st.markdown(f"**{category}**")
                badge_html = "".join(
                    [f'<span class="skill-badge">{item}</span>' for item in items]
                )
                st.markdown(badge_html, unsafe_allow_html=True)
                st.markdown("<div style='margin-bottom: 16px;'></div>", unsafe_allow_html=True)

        with col2:
            for category, items in items_list[3:]:
                st.markdown(f"**{category}**")
                badge_html = "".join(
                    [f'<span class="skill-badge">{item}</span>' for item in items]
                )
                st.markdown(badge_html, unsafe_allow_html=True)
                st.markdown("<div style='margin-bottom: 16px;'></div>", unsafe_allow_html=True)

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