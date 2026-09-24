import base64
import os
import pandas as pd
import streamlit as st

# ---------------------------------------------------------
# 1. Page Configuration
# ---------------------------------------------------------
st.set_page_config(
    page_title="Pavan Deep Godi | Analytics & Insights Engineer",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ---------------------------------------------------------
# Profile Image Loader
# ---------------------------------------------------------
IMAGE_FILENAME = "professional_photo.JPG"


def get_base64_image(image_path):
    if not os.path.exists(image_path):
        return None

    ext = os.path.splitext(image_path)[1].lower()
    mime_type = "image/png" if ext == ".png" else "image/jpeg"

    with open(image_path, "rb") as file:
        encoded = base64.b64encode(file.read()).decode("utf-8")
        return f"data:{mime_type};base64,{encoded}"


img_src = get_base64_image(IMAGE_FILENAME)

if not img_src:
    img_src = "https://api.dicebear.com/7.x/initials/svg?seed=PDG&backgroundColor=0284c7"

# ---------------------------------------------------------
# 2. Fully Responsive CSS Theme
# ---------------------------------------------------------
st.markdown(
    """
    <style>
    :root {
        color-scheme: light !important;
    }

    .stApp {
        background-color: #F8FAFC !important;
        color: #0F172A !important;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    }

    [data-testid="stSidebar"], [data-testid="collapsedControl"] {
        display: none !important;
    }

    .hero-card {
        background: linear-gradient(135deg, #FFFFFF 0%, #F1F5F9 100%);
        border: 1px solid #E2E8F0;
        border-radius: 16px;
        padding: clamp(16px, 3vw, 24px);
        box-shadow: 0 4px 12px rgba(15, 23, 42, 0.03);
        margin-bottom: 16px;
    }

    .hero-wrapper {
        display: flex;
        flex-wrap: wrap;
        align-items: center;
        justify-content: space-between;
        gap: 16px;
    }

    .profile-group {
        display: flex;
        align-items: center;
        gap: 16px;
        flex-wrap: wrap;
    }

    .header-avatar {
        border-radius: 12px !important;
        border: 2px solid #0284C7 !important;
        padding: 0px !important;
        background-color: #FFFFFF;
        box-shadow: 0 4px 8px rgba(2, 132, 199, 0.15);
        width: 90px !important;
        height: 90px !important;
        object-fit: cover !important;
        display: block;
    }

    .candidate-name {
        font-size: clamp(1.6rem, 5vw, 2.4rem);
        font-weight: 800;
        color: #0F172A !important;
        letter-spacing: -0.8px;
        line-height: 1.15;
    }

    .candidate-title {
        font-size: clamp(1.0rem, 3vw, 1.2rem);
        font-weight: 700;
        color: #0284C7 !important;
        margin-top: 4px;
    }

    .status-badge {
        display: inline-block;
        background-color: #F0FDF4;
        color: #166534;
        border: 1px solid #BBF7D0;
        font-size: 0.78rem;
        font-weight: 700;
        padding: 3px 10px;
        border-radius: 20px;
        margin-top: 6px;
    }

    .contact-bar {
        display: flex;
        flex-wrap: wrap;
        align-items: center;
        gap: 8px 12px;
        font-size: 0.85rem;
        color: #475569 !important;
    }
    .contact-item {
        display: inline-flex;
        align-items: center;
        gap: 4px;
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

    .val-card {
        background: #FFFFFF;
        border: 1px solid #E2E8F0;
        border-radius: 12px;
        padding: clamp(14px, 3vw, 20px);
        box-shadow: 0 2px 4px rgba(15, 23, 42, 0.02);
        margin-bottom: 20px;
    }

    .pillar-wrapper {
        display: flex;
        flex-wrap: wrap;
        gap: 6px;
        margin-top: 10px;
    }

    .pillar-pill {
        background-color: #EFF6FF;
        color: #1E40AF;
        border: 1px solid #BFDBFE;
        font-size: 0.8rem;
        font-weight: 700;
        padding: 4px 10px;
        border-radius: 6px;
        display: inline-block;
    }

    .metrics-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
        gap: 12px;
        margin-bottom: 20px;
    }

    .metric-card {
        background: #FFFFFF;
        border: 1px solid #E2E8F0;
        border-left: 4px solid #0284C7;
        border-radius: 12px;
        padding: 16px;
        box-shadow: 0 2px 4px rgba(15, 23, 42, 0.04);
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }
    .metric-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 12px rgba(15, 23, 42, 0.08);
    }
    .metric-card.accent-emerald { border-left-color: #10B981; }
    .metric-card.accent-indigo { border-left-color: #6366F1; }
    .metric-card.accent-amber { border-left-color: #F59E0B; }

    .metric-val {
        font-size: clamp(1.75rem, 4vw, 2rem);
        font-weight: 800;
        line-height: 1;
    }
    .metric-lbl {
        font-size: 0.8rem;
        font-weight: 700;
        color: #64748B;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        margin-top: 6px;
    }
    .metric-sub {
        font-size: 0.78rem;
        color: #475569;
        margin-top: 4px;
        line-height: 1.3;
    }

    .skills-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
        gap: 12px;
    }

    .skill-card {
        background: #FFFFFF;
        border: 1px solid #E2E8F0;
        border-radius: 12px;
        padding: 16px;
        height: 100%;
        box-shadow: 0 1px 3px rgba(15, 23, 42, 0.02);
    }
    .skill-title {
        font-size: 0.95rem;
        font-weight: 700;
        color: #0F172A;
        margin-bottom: 10px;
        display: flex;
        align-items: center;
        gap: 8px;
    }

    .chips-wrapper {
        display: flex;
        flex-wrap: wrap;
        gap: 6px;
    }

    .chip {
        display: inline-block;
        background-color: #F1F5F9;
        color: #334155;
        border: 1px solid #CBD5E1;
        padding: 4px 10px;
        border-radius: 20px;
        font-size: 0.8rem;
        font-weight: 600;
    }
    .chip-primary {
        background-color: #E0F2FE;
        color: #0369A1;
        border-color: #BAE6FD;
    }

    .exp-header {
        display: flex;
        flex-wrap: wrap;
        justify-content: space-between;
        align-items: baseline;
        gap: 4px 12px;
        margin-bottom: 8px;
    }
    .exp-company {
        font-size: clamp(1.05rem, 3vw, 1.2rem);
        font-weight: 800;
        color: #0F172A;
    }
    .exp-date {
        font-size: 0.85rem;
        font-weight: 700;
        color: #0284C7;
    }

    button[data-baseweb="tab"] {
        background-color: transparent !important;
        color: #64748B !important;
        font-weight: 700 !important;
        font-size: clamp(0.88rem, 2.5vw, 1rem) !important;
        padding: 10px 12px !important;
    }
    button[data-baseweb="tab"][aria-selected="true"] {
        color: #0284C7 !important;
        border-bottom-color: #0284C7 !important;
        border-bottom-width: 3px !important;
    }

    .table-container {
        width: 100%;
        overflow-x: auto;
        -webkit-overflow-scrolling: touch;
    }

    @media (max-width: 640px) {
        .hero-wrapper {
            flex-direction: column;
            align-items: flex-start;
        }
        .contact-bar {
            justify-content: flex-start;
            font-size: 0.8rem;
        }
    }
    </style>
""",
    unsafe_allow_html=True,
)

# ---------------------------------------------------------
# 3. Header Hero Section
# ---------------------------------------------------------
st.markdown(
    f"""
    <div class="hero-card">
        <div class="hero-wrapper">
            <div class="profile-group">
                <img class="header-avatar" src="{img_src}">
                <div>
                    <div class="candidate-name">PAVAN DEEP GODI</div>
                    <div class="candidate-title">Analytics & Insights Engineer</div>
                    <div class="status-badge">🟢 7+ Years Experience &nbsp;•&nbsp; Converting Complex Data into Actionable Insights</div>
                </div>
            </div>
            <div class="contact-bar">
                <span class="contact-item">📱 8099490199</span>
                <span class="contact-item">📧 <a href="mailto:pavandeep459@gmail.com">pavandeep459@gmail.com</a></span>
                <span class="contact-item">🔗 <a href="https://www.linkedin.com/in/pavan-deep-godi-3aa8ba16a/" target="_blank">LinkedIn Profile</a></span>
                <span class="contact-item">💻 <a href="https://github.com/pavandeep-godi" target="_blank">GitHub Profile</a></span>
            </div>
        </div>
    </div>
""",
    unsafe_allow_html=True,
)

# ---------------------------------------------------------
# 4. Executive Summary Section
# ---------------------------------------------------------
st.markdown(
    """
    <div class="val-card">
        <div style="font-size: 1.05rem; font-weight: 800; color: #0F172A; margin-bottom: 6px;">
            📝 Summary
        </div>
        <div style="font-size: 0.92rem; color: #334155; line-height: 1.6;">
            <b>Analytics & Insights Engineer</b> with 7+ years of experience converting complex data into actionable insights for sales and finance leaders. Enhances SQL, Python, and KNIME data pipelines, Tableau dashboards, and KPI frameworks to improve data quality, accelerate reporting, and reduce ad-hoc requests. Delivers measurable, double-digit efficiency gains by transforming manual and Alteryx-based processes into scalable, automated analytics solutions.
        </div>
        <div class="pillar-wrapper">
            <span class="pillar-pill">⚡ SQL, Python & KNIME Pipelines</span>
            <span class="pillar-pill">📊 Tableau & Power BI</span>
            <span class="pillar-pill">🎯 Scalable ETL & Automation</span>
            <span class="pillar-pill">📈 KPI Frameworks</span>
            <span class="pillar-pill">💼 Sales & Finance Analytics</span>
        </div>
    </div>
""",
    unsafe_allow_html=True,
)

# ---------------------------------------------------------
# 5. High-Impact Highlights
# ---------------------------------------------------------
st.markdown(
    "<div style='font-size: 1.05rem; font-weight: 800; color: #0F172A; margin-bottom: 10px;'>📈 Key Accomplishments & Metrics</div>",
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="metrics-grid">
        <div class="metric-card">
            <div class="metric-val" style="color: #0284C7;">60%</div>
            <div class="metric-lbl">Manual Requests Reduced</div>
            <div class="metric-sub">Delivered Cash Plus Pilot self-serve dashboard at Deloitte</div>
        </div>
        <div class="metric-card accent-emerald">
            <div class="metric-val" style="color: #10B981;">$450K+</div>
            <div class="metric-lbl">Cost Opportunities Surfaced</div>
            <div class="metric-sub">Segmented spend/performance drivers at Solenis</div>
        </div>
        <div class="metric-card accent-indigo">
            <div class="metric-val" style="color: #6366F1;">15+</div>
            <div class="metric-lbl">Alteryx Workflows Converted</div>
            <div class="metric-sub">Transformed into reusable KNIME ETL nodes at Deloitte</div>
        </div>
        <div class="metric-card accent-amber">
            <div class="metric-val" style="color: #D97706;">90 Min</div>
            <div class="metric-lbl">Saved Per Month</div>
            <div class="metric-sub">Automated recurring Excel to Tableau chart workflows</div>
        </div>
    </div>
""",
    unsafe_allow_html=True,
)

# ---------------------------------------------------------
# 6. Main Content Tabs
# ---------------------------------------------------------
tab_exp, tab_skills, tab_matrix, tab_projects_edu = st.tabs(
    [
        "💼 Professional Experience",
        "🛠️ Technical Skills",
        "📊 Impact Matrix",
        "🏆 Achievements, Projects & Education",
    ]
)

# TAB 1: PROFESSIONAL EXPERIENCE
with tab_exp:
    with st.container(border=True):
        st.markdown(
            """
            <div class="exp-header">
                <div class="exp-company">Analytics & Engineer 2 &nbsp;|&nbsp; DELOITTE</div>
                <div class="exp-date">Jun 2024 – Present</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.markdown(
            """
        * Converted **15+ Alteryx workflows into KNIME-based ETL**, consolidating repeated transformations into reusable nodes to support cost optimization and consistent dataset outputs.
        * Built/automated **20+ ingestion pipelines** with standardized input formats and transformation steps, cutting pipeline runtime and making releases repeatable across parallel projects.
        * Executed large-scale data migrations across all testing and production cycles using **IBM DataStage** and **SAP LSMW**, resolving quality anomalies for two distinct projects.
        * Delivered an interactive **Tableau self-serve dashboard for Cash Plus Pilot** (30+ client users), backed by automated datasets; reduced manual reporting requests by **60%** within the pilot period.
        * Rebuilt the Sales Executive KPI dashboard with clearer metric definitions and consistent filters, reducing ad-hoc query volume by **40%**.
        * Automated the generation of Tableau-ready charts from recurring Excel templates, saving **~90 minutes/month** of manual rebuild work.
        * Owned end-to-end delivery from dataset design → pipeline automation → validation → dashboard deployment.
        * Triaged and fixed **12+ dashboard/data defects** per release cycle, ensuring post-migration data accuracy and preventing stale metric outputs.
        """
        )

    with st.container(border=True):
        st.markdown(
            """
            <div class="exp-header">
                <div class="exp-company">Senior Data Analyst – 2 &nbsp;|&nbsp; SOLENIS</div>
                <div class="exp-date">Nov 2021 – May 2024</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.markdown(
            """
        * Designed and streamlined a working capital dashboard to monitor cash flow, providing enhanced visibility into financial metrics for finance leadership, increasing usage by **30%**.
        * Built a working capital cash-flow dashboard and refined KPI definitions based on stakeholder feedback, increasing adoption/usage by **30%**.
        * Developed an executive KPI dashboard for weekly performance reviews, improving visibility into core operational metrics and trends.
        * Produced monthly executive performance decks using standardized SQL extracts, translating operational data trends into actions and targets for leadership.
        * Managed the company’s most widely used Purchase Price Variance dashboard, processing millions of records to deliver actionable BU-level, category-level and financial insights to business leaders; maintained weekly and monthly reporting while implementing new metrics, visualizations, and business logic enhancements.
        * Co-developed an interactive analytics view that surfaced **$450K+ cost reduction opportunities** by segmenting spend/performance drivers and enabling targeted operational actions.
        * Partnered with business owners for ad-hoc analytics requests, converting one-off questions into reusable datasets/KPI logic to reduce repeat work.
        * Trained stakeholders on dashboard usage and metric definitions, improving engagement by **5–10%** post-session.
        """
        )

    with st.container(border=True):
        st.markdown(
            """
            <div class="exp-header">
                <div class="exp-company">Data Analyst &nbsp;|&nbsp; TCS</div>
                <div class="exp-date">Apr 2019 – Nov 2021</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.markdown(
            """
        * Built a **PySpark ETL proof of concept on AWS** to separate and analyze historical vs current datasets, enabling faster analysis-ready extracts for the team.
        * Developed Tableau-KPI dashboards for operations leadership, surfacing key trends weekly.
        * Replaced repetitive Excel workflows with Python automation, reducing manual effort and errors by **~60%** for recurring reporting tasks.
        """
        )

# TAB 2: TECHNICAL SKILLS
with tab_skills:
    st.markdown(
        """
        <div class="skills-grid">
            <div class="skill-card">
                <div class="skill-title">📊 BI & Visualization</div>
                <div class="chips-wrapper">
                    <span class="chip chip-primary">Tableau</span>
                    <span class="chip chip-primary">Power BI</span>
                </div>
            </div>
            <div class="skill-card">
                <div class="skill-title">⚙️ Analytics Engineering & ETL</div>
                <div class="chips-wrapper">
                    <span class="chip chip-primary">KNIME</span>
                    <span class="chip chip-primary">AWS Glue</span>
                    <span class="chip">IBM DataStage</span>
                    <span class="chip">SAP LSMW</span>
                </div>
            </div>
            <div class="skill-card">
                <div class="skill-title">💻 Programming & Querying</div>
                <div class="chips-wrapper">
                    <span class="chip chip-primary">Python</span>
                    <span class="chip chip-primary">SQL</span>
                </div>
            </div>
            <div class="skill-card">
                <div class="skill-title">🧹 Data Preparation & Analysis</div>
                <div class="chips-wrapper">
                    <span class="chip chip-primary">Tableau Prep</span>
                    <span class="chip chip-primary">Excel</span>
                </div>
            </div>
            <div class="skill-card">
                <div class="skill-title">🗄️ Data Platforms</div>
                <div class="chips-wrapper">
                    <span class="chip chip-primary">Amazon Athena</span>
                    <span class="chip chip-primary">SQL Server</span>
                </div>
            </div>
            <div class="skill-card">
                <div class="skill-title">🔹 Additional Exposure</div>
                <div class="chips-wrapper">
                    <span class="chip">dbt</span>
                    <span class="chip">Snowflake</span>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

# TAB 3: IMPACT MATRIX
with tab_matrix:
    st.markdown(
        "<div style='font-size: 1rem; font-weight: 700; color: #0F172A; margin-bottom: 12px;'>📋 Deliverables & Business Impact Breakdown</div>",
        unsafe_allow_html=True,
    )

    impact_df = pd.DataFrame(
        {
            "Company": [
                "Deloitte",
                "Deloitte",
                "Deloitte",
                "Solenis",
                "Solenis",
                "TCS",
            ],
            "Key Initiative": [
                "Cash Plus Self-Serve BI Pilot",
                "Sales Executive KPI Dashboard",
                "Alteryx to KNIME Conversion & Excel Automation",
                "Spend Driver Analytics View",
                "Working Capital Dashboard",
                "Python Reporting Automation",
            ],
            "Quantifiable Business Impact": [
                "⚡ 60% Reduction in manual reporting requests",
                "📉 40% Reduction in ad-hoc query volume",
                "⏱️ ~90 Minutes saved/month & consolidated reusable nodes",
                "💰 $450K+ Cost reduction opportunities surfaced",
                "📈 30% Increase in executive dashboard usage/adoption",
                "🤖 ~60% Reduction in manual effort and errors",
            ],
            "Domain / Focus": [
                "Finance Analytics",
                "Sales Operations",
                "ETL Optimization & Automation",
                "Procurement / Spend",
                "Finance / Cash Flow",
                "Operations",
            ],
        }
    )

    st.markdown('<div class="table-container">', unsafe_allow_html=True)
    st.dataframe(
        impact_df,
        use_container_width=True,
        hide_index=True,
    )
    st.markdown("</div>", unsafe_allow_html=True)

# TAB 4: ACHIEVEMENTS, PROJECTS & EDUCATION
with tab_projects_edu:
    st.markdown("#### 🏆 Professional Achievements")
    st.markdown(
        """
    * **Applause Award — Deloitte:** Recognized for contributions to the Cash Plus Pilot and Sales Executive Insights Dashboard.
    * **Employee Award — Solenis:** Honored for co-developing a raw-material procurement dashboard that identified savings opportunities and contributed to more than $500,000 in cost savings.
    * **Client Recognition — Solenis:** Received multiple commendations for delivering timely reports, actionable KPIs, and data-driven solutions that supported leadership discussions and decision-making.
    """
    )

    st.markdown("---")
    st.markdown("#### 🚀 Personal Projects")
    with st.container(border=True):
        st.markdown(
            """
        **IPL Auction Analytics – IPL**
        * **App Link:** [IPL_Analytics_App](#)
        * **GitHub Link:** [Github_IPL_Analytics](https://github.com/pavandeep-godi)
        * **Description:** This tool aids decision-making by analyzing various unique parameters that teams consider when building their squads during auctions.
        * **Tools used:** Python (Streamlit)
        """
        )

    st.markdown("---")
    st.markdown("#### 🎓 Education")
    with st.container(border=True):
        st.markdown(
            """
        **Bachelor of Technology in Engineering** | Gitam University (2015 – 2019)
        * **Course:** Electronics and Communication Engineering
        """
        )