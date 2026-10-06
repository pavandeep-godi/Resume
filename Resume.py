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


IMAGE_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), IMAGE_FILENAME)
img_src = get_base64_image(IMAGE_PATH)

if not img_src:
    img_src = "https://api.dicebear.com/7.x/initials/svg?seed=PDG&backgroundColor=0284c7"

# ---------------------------------------------------------
# 2. Fully Responsive CSS Theme
# ---------------------------------------------------------
st.markdown(
    """
    <style>
    .stApp {
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

    /* Use Streamlit's active foreground/background so light and dark themes both work. */
    .hero-card,
    .val-card,
    .metric-card,
    .skill-card {
        background: rgba(127, 127, 127, 0.07) !important;
        color: inherit !important;
        border: 1.5px solid rgba(127, 127, 127, 0.48) !important;
        border-radius: 1rem !important;
        box-shadow: 0 5px 18px rgba(0, 0, 0, 0.09) !important;
    }

    .hero-card {
        background-image: none !important;
        border-left: 4px solid currentColor !important;
    }

    .candidate-name,
    .candidate-title,
    .skill-title,
    .exp-company,
    .exp-date,
    .contact-bar,
    .metric-sub,
    .metric-lbl,
    .contact-bar a,
    .val-card,
    .skill-card {
        color: inherit !important;
    }

    .status-badge,
    .pillar-pill,
    .chip,
    .chip-primary {
        color: inherit !important;
        background: rgba(127, 127, 127, 0.08) !important;
        border-color: rgba(127, 127, 127, 0.4) !important;
    }

    .stMarkdown div[style*="color: #0F172A"],
    .stMarkdown div[style*="color: #334155"] {
        color: inherit !important;
    }

    .metric-val[style] {
        color: inherit !important;
    }

    [class*="st-key-card-"] {
        box-sizing: border-box !important;
        margin: 0.55rem 0 1rem !important;
        padding: clamp(1rem, 2.5vw, 1.4rem) !important;
        border: 2px solid currentColor !important;
        border-radius: 1rem !important;
        background: rgba(127, 127, 127, 0.12) !important;
        box-shadow: 0 6px 20px rgba(0, 0, 0, 0.12) !important;
        color: inherit !important;
        transition: transform 0.18s ease, box-shadow 0.18s ease;
    }

    [class*="st-key-card-"]:hover {
        transform: translateY(-2px);
        box-shadow: 0 9px 24px rgba(0, 0, 0, 0.15) !important;
    }

    [class*="st-key-card-"] [data-testid="stMarkdownContainer"] {
        color: inherit !important;
    }

    [class*="st-key-card-"] p:last-child,
    [class*="st-key-card-"] ul:last-child {
        margin-bottom: 0;
    }

    [data-testid="stTabs"] [role="tablist"] {
        display: flex !important;
        flex-wrap: wrap !important;
        gap: 0.4rem !important;
        border-bottom: 1px solid rgba(127, 127, 127, 0.35) !important;
    }

    [data-testid="stTab"],
    button[data-baseweb="tab"] {
        flex: 1 1 10rem !important;
        min-width: min(10rem, 100%) !important;
        min-height: 2.8rem !important;
        padding: 0.65rem 0.8rem !important;
        border: 1px solid rgba(127, 127, 127, 0.35) !important;
        border-bottom: 3px solid transparent !important;
        border-radius: 0.65rem 0.65rem 0 0 !important;
        background: rgba(127, 127, 127, 0.04) !important;
        color: inherit !important;
        white-space: normal !important;
    }

    [data-testid="stTab"] p,
    button[data-baseweb="tab"] p {
        color: inherit !important;
        white-space: normal !important;
        line-height: 1.25 !important;
    }

    [data-testid="stTab"][aria-selected="true"],
    button[data-baseweb="tab"][aria-selected="true"] {
        color: inherit !important;
        border-bottom-color: currentColor !important;
    }

    [data-testid="stTab"]:focus-visible,
    button[data-baseweb="tab"]:focus-visible,
    .agentic-cta:focus-visible {
        outline: 3px solid currentColor !important;
        outline-offset: 2px !important;
    }

    .agentic-cta {
        display: flex;
        align-items: center;
        justify-content: space-between;
        gap: 0.75rem;
        width: fit-content;
        max-width: 100%;
        padding: 0.85rem 1.1rem;
        border: 2px solid currentColor;
        border-radius: 0.75rem;
        background: rgba(127, 127, 127, 0.08);
        color: inherit !important;
        font-weight: 750;
        line-height: 1.3;
        text-decoration: none !important;
        box-shadow: 0 5px 14px rgba(0, 0, 0, 0.16);
        transition: transform 0.15s ease, box-shadow 0.15s ease;
    }

    .agentic-cta:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 18px rgba(0, 0, 0, 0.2);
        filter: brightness(1.08);
    }

    .agentic-cta-arrow {
        font-size: 1.15rem;
        flex: 0 0 auto;
    }

    .table-container {
        max-width: 100%;
    }

    @media (max-width: 640px) {
        .hero-card,
        .val-card,
        .metric-card,
        .skill-card {
            padding: 1rem !important;
        }

        [class*="st-key-card-"] {
            padding: 0.9rem !important;
            margin: 0.45rem 0 0.85rem !important;
        }

        .profile-group {
            align-items: flex-start;
        }

        .header-avatar {
            width: 68px !important;
            height: 68px !important;
        }

        .contact-item {
            white-space: normal;
            overflow-wrap: anywhere;
        }

        .metrics-grid,
        .skills-grid {
            grid-template-columns: minmax(0, 1fr) !important;
        }

        [data-testid="stTab"],
        button[data-baseweb="tab"] {
            flex-basis: calc(50% - 0.4rem) !important;
            min-width: 0 !important;
            font-size: 0.82rem !important;
        }

        .agentic-cta {
            width: 100%;
            box-sizing: border-box;
        }
    }

    @media (prefers-reduced-motion: reduce) {
        *, *::before, *::after {
            scroll-behavior: auto !important;
            transition-duration: 0.01ms !important;
            animation-duration: 0.01ms !important;
        }
    }

    /* Recruiter portfolio refresh */
    [data-testid="stMainBlockContainer"] {
        width: 100% !important;
        max-width: 1600px !important;
        padding-top: clamp(1.2rem, 4vw, 3rem) !important;
        padding-right: clamp(1rem, 3vw, 3.5rem) !important;
        padding-bottom: 3rem !important;
        padding-left: clamp(1rem, 3vw, 3.5rem) !important;
        box-sizing: border-box !important;
    }

    .hero-card {
        position: relative;
        overflow: hidden;
        container-type: inline-size;
        padding: clamp(1.35rem, 4vw, 2.6rem) !important;
        border: 1px solid rgba(148, 197, 255, 0.34) !important;
        border-left: 1px solid rgba(148, 197, 255, 0.34) !important;
        border-radius: 1.5rem !important;
        background: radial-gradient(ellipse at 90% 0%, rgba(56, 189, 248, 0.2), transparent 38%), linear-gradient(130deg, #0B1730 0%, #123454 58%, #14506B 100%) !important;
        color: #F8FAFC !important;
        box-shadow: 0 18px 44px rgba(2, 12, 27, 0.24) !important;
    }

    .hero-card::after {
        content: "DATA  /  INSIGHT  /  IMPACT";
        position: absolute;
        right: clamp(1rem, 3vw, 2rem);
        bottom: 0.8rem;
        color: rgba(226, 242, 255, 0.48);
        font-size: 0.65rem;
        font-weight: 800;
        letter-spacing: 0.18em;
        pointer-events: none;
    }

    .hero-wrapper {
        position: relative;
        z-index: 1;
        align-items: center;
        gap: 1.5rem;
    }

    .profile-group {
        flex-wrap: nowrap;
        gap: clamp(1rem, 2vw, 1.4rem);
    }

    .hero-eyebrow {
        margin-bottom: 0.6rem;
        color: #BAE6FD;
        font-size: 0.7rem;
        font-weight: 800;
        letter-spacing: 0.17em;
        text-transform: uppercase;
    }

    .header-avatar {
        width: clamp(116px, 10vw, 140px) !important;
        height: clamp(116px, 10vw, 140px) !important;
        border: 3px solid rgba(186, 230, 253, 0.85) !important;
        border-radius: 1.4rem !important;
        box-shadow: 0 8px 24px rgba(0, 0, 0, 0.26) !important;
    }

    .candidate-name {
        color: #FFFFFF !important;
        font-size: clamp(2rem, 5vw, 3.25rem) !important;
        line-height: 1.02 !important;
        letter-spacing: -0.055em !important;
    }

    .candidate-title {
        margin-top: 0.55rem !important;
        color: #9BE3FF !important;
        font-size: clamp(1rem, 2.5vw, 1.25rem) !important;
        font-weight: 700 !important;
        letter-spacing: 0.015em;
    }

    .status-badge {
        margin-top: 0.8rem !important;
        padding: 0.42rem 0.75rem !important;
        border: 1px solid rgba(191, 219, 254, 0.3) !important;
        border-radius: 99px !important;
        background: rgba(255, 255, 255, 0.1) !important;
        color: #E0F2FE !important;
        font-size: 0.78rem !important;
        line-height: 1.4;
    }

    .contact-bar {
        max-width: 27rem;
        justify-content: flex-end;
        gap: 0.55rem !important;
        color: #E2E8F0 !important;
        font-size: 0.82rem !important;
    }

    .contact-item {
        padding: 0.52rem 0.7rem;
        border: 1px solid rgba(226, 242, 255, 0.23);
        border-radius: 0.7rem;
        background: rgba(255, 255, 255, 0.075);
        backdrop-filter: blur(8px);
    }

    .contact-bar a {
        color: #FFFFFF !important;
    }

    .contact-item:hover {
        background: rgba(255, 255, 255, 0.15);
    }

    .val-card {
        display: grid;
        grid-template-columns: minmax(0, 1.7fr) minmax(13rem, 0.8fr);
        align-items: center;
        gap: 1rem 1.6rem;
        margin-top: 1.25rem;
        padding: clamp(1.2rem, 3vw, 1.8rem) !important;
        border-radius: 1.15rem !important;
    }

    .val-card > div:first-child {
        grid-column: 1 / -1;
        margin: 0 !important;
        font-size: 0.78rem !important;
        letter-spacing: 0.13em;
        text-transform: uppercase;
        opacity: 0.75;
    }

    .val-card > div:nth-child(2) {
        font-size: clamp(1rem, 1.5vw, 1.12rem) !important;
        line-height: 1.75 !important;
    }

    .summary-kicker {
        color: inherit;
    }

    .pillar-wrapper {
        gap: 0.45rem !important;
        margin-top: 0 !important;
    }

    .pillar-pill {
        padding: 0.38rem 0.62rem !important;
        border: 1px solid rgba(127, 127, 127, 0.35) !important;
        border-radius: 99px !important;
        background: rgba(127, 127, 127, 0.1) !important;
        font-size: 0.75rem !important;
    }

    .metrics-grid {
        grid-template-columns: repeat(4, minmax(0, 1fr)) !important;
        gap: 0.85rem !important;
        margin: 0 0 1.5rem !important;
    }

    .metric-card {
        min-height: 9.3rem;
        padding: 1.15rem !important;
        border: 1px solid rgba(127, 127, 127, 0.34) !important;
        border-top: 3px solid currentColor !important;
        border-radius: 1rem !important;
        background: rgba(127, 127, 127, 0.055) !important;
        box-shadow: 0 6px 18px rgba(0, 0, 0, 0.07) !important;
    }

    .metric-card:hover {
        transform: translateY(-3px);
        box-shadow: 0 12px 24px rgba(0, 0, 0, 0.13) !important;
    }

    .metric-val {
        font-size: clamp(1.8rem, 3vw, 2.35rem) !important;
        letter-spacing: -0.045em;
    }

    .metric-lbl {
        margin-top: 0.55rem !important;
        font-size: 0.71rem !important;
        letter-spacing: 0.08em !important;
    }

    .metric-sub {
        margin-top: 0.4rem !important;
        line-height: 1.45 !important;
    }

    [data-testid="stTabs"] [role="tablist"] {
        gap: 0.55rem !important;
        margin: 0.5rem 0 0.2rem;
        padding: 0.35rem !important;
        border: 1px solid rgba(127, 127, 127, 0.24) !important;
        border-radius: 1rem !important;
        background: rgba(127, 127, 127, 0.055);
    }

    [data-testid="stTab"],
    button[data-baseweb="tab"] {
        flex: 1 1 11rem !important;
        min-height: 3rem !important;
        padding: 0.7rem 1rem !important;
        border: 1px solid transparent !important;
        border-radius: 0.75rem !important;
        background: transparent !important;
        font-size: 0.9rem !important;
        font-weight: 700 !important;
        text-align: center;
    }

    [data-testid="stTab"][aria-selected="true"],
    button[data-baseweb="tab"][aria-selected="true"] {
        border-color: rgba(127, 127, 127, 0.3) !important;
        background: rgba(127, 127, 127, 0.14) !important;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
    }

    [data-testid="stTab"] p,
    button[data-baseweb="tab"] p {
        margin: 0 !important;
        font-weight: 700 !important;
    }

    [data-testid="stTabPanel"] {
        padding-top: 1.3rem !important;
    }

    [class*="st-key-card-"] {
        margin: 0.65rem 0 1.05rem !important;
        padding: clamp(1.1rem, 2.6vw, 1.65rem) !important;
        border: 2px solid currentColor !important;
        border-left: 4px solid currentColor !important;
        border-radius: 1.15rem !important;
        background: rgba(127, 127, 127, 0.1) !important;
        box-shadow: 0 7px 22px rgba(0, 0, 0, 0.075) !important;
    }

    .exp-header {
        align-items: center;
        padding-bottom: 0.9rem;
        margin-bottom: 0.8rem !important;
        border-bottom: 1px solid rgba(127, 127, 127, 0.28);
    }

    .exp-company {
        font-size: clamp(1.12rem, 2.5vw, 1.35rem) !important;
        letter-spacing: -0.02em;
    }

    .exp-date {
        padding: 0.34rem 0.65rem;
        border: 1px solid rgba(127, 127, 127, 0.35);
        border-radius: 99px;
        background: rgba(127, 127, 127, 0.09);
        font-size: 0.78rem !important;
    }

    [data-testid="stMarkdownContainer"] ul {
        padding-left: 1.2rem;
    }

    [data-testid="stMarkdownContainer"] li {
        padding-left: 0.15rem;
        margin: 0.35rem 0;
        line-height: 1.6;
    }

    .skills-grid {
        grid-template-columns: repeat(3, minmax(0, 1fr)) !important;
        gap: 0.9rem !important;
    }

    .skill-card {
        min-height: 8rem;
        padding: 1.2rem !important;
        border-radius: 1rem !important;
        background: rgba(127, 127, 127, 0.055) !important;
    }

    .skill-title {
        margin-bottom: 0.85rem !important;
        font-size: 0.95rem !important;
    }

    .chip {
        padding: 0.35rem 0.6rem !important;
        border-radius: 99px !important;
        font-size: 0.76rem !important;
    }

    .agentic-cta {
        justify-content: center;
        width: fit-content;
        max-width: 100%;
        border: 1px solid #0EA5E9 !important;
        border-radius: 0.8rem !important;
        background: linear-gradient(110deg, #0369A1, #0284C7) !important;
        color: #FFFFFF !important;
        box-shadow: 0 8px 18px rgba(2, 132, 199, 0.25) !important;
        text-align: center;
    }

    .project-kicker {
        color: #0284C7;
        font-size: 0.7rem;
        font-weight: 800;
        letter-spacing: 0.14em;
    }

    .project-title {
        margin: 0.35rem 0 0.45rem !important;
        font-size: clamp(1.35rem, 3vw, 1.8rem) !important;
        letter-spacing: -0.04em;
    }

    .project-summary {
        max-width: 70ch;
        margin: 0 0 1rem !important;
        line-height: 1.65;
    }

    .project-actions {
        display: flex;
        flex-wrap: wrap;
        align-items: center;
        gap: 0.75rem 1rem;
        margin: 0.8rem 0 1.1rem;
    }

    .project-secondary-link {
        padding: 0.75rem 0.2rem;
        color: inherit !important;
        font-weight: 700;
        text-decoration-thickness: 1px !important;
        text-underline-offset: 0.2em;
    }

    .project-highlights {
        margin-top: 0.8rem !important;
    }

    .project-tech {
        display: inline-block;
        margin-top: 0.45rem;
        padding: 0.5rem 0.75rem;
        border: 1px solid rgba(127, 127, 127, 0.3);
        border-radius: 0.7rem;
        background: rgba(127, 127, 127, 0.07);
        font-size: 0.84rem;
    }

    .table-container [data-testid="stDataFrame"] {
        overflow: hidden;
        border: 1px solid rgba(127, 127, 127, 0.35);
        border-radius: 1rem;
        box-shadow: 0 6px 18px rgba(0, 0, 0, 0.07);
    }

    @media (max-width: 900px) {
        .hero-wrapper {
            flex-direction: column;
            align-items: center;
            text-align: center;
        }

        .profile-group {
            justify-content: center;
        }

        .hero-copy {
            text-align: center;
        }

        .contact-bar {
            max-width: none;
            width: 100%;
            justify-content: center;
        }

        .metrics-grid {
            grid-template-columns: repeat(2, minmax(0, 1fr)) !important;
        }

        .skills-grid {
            grid-template-columns: repeat(2, minmax(0, 1fr)) !important;
        }
    }

    @container (max-width: 950px) {
        .hero-wrapper {
            display: grid;
            grid-template-columns: minmax(0, 1fr) minmax(15rem, 17rem);
            align-items: center;
            gap: 1rem;
        }

        .profile-group {
            min-width: 0;
            justify-content: flex-start;
        }

        .hero-copy {
            min-width: 0;
            text-align: left;
        }

        .contact-bar {
            max-width: none;
            width: 100%;
            justify-content: flex-end;
        }
    }

    @container (max-width: 700px) {
        .hero-wrapper {
            display: flex;
            flex-direction: column;
            align-items: stretch;
        }

        .contact-bar {
            justify-content: flex-start;
        }
    }

    @media (max-width: 640px) {
        [data-testid="stMainBlockContainer"] {
            padding: 0.8rem 0.75rem 2rem !important;
        }

        .hero-card {
            border-radius: 1.15rem !important;
            padding: 1.1rem !important;
        }

        .hero-card::after {
            display: none;
        }

        .profile-group {
            gap: 0.9rem;
            flex-wrap: wrap;
        }

        .header-avatar {
            width: 80px !important;
            height: 80px !important;
        }

        .hero-eyebrow {
            font-size: 0.6rem;
        }

        .candidate-name {
            font-size: clamp(1.7rem, 8vw, 2.2rem) !important;
        }

        .status-badge {
            font-size: 0.7rem !important;
        }

        .contact-bar {
            gap: 0.45rem !important;
            font-size: 0.75rem !important;
        }

        .contact-item {
            white-space: normal;
            overflow-wrap: anywhere;
        }

        .val-card {
            grid-template-columns: 1fr;
            gap: 0.8rem;
            padding: 1.1rem !important;
        }

        .val-card > div:first-child {
            grid-column: auto;
        }

        .metrics-grid,
        .skills-grid {
            grid-template-columns: repeat(2, minmax(0, 1fr)) !important;
            gap: 0.6rem !important;
        }

        .metric-card {
            min-height: 8.7rem;
            padding: 0.9rem !important;
        }

        .metric-val {
            font-size: 1.75rem !important;
        }

        .metric-lbl {
            font-size: 0.64rem !important;
        }

        [data-testid="stTab"] {
            flex-basis: calc(50% - 0.4rem) !important;
            min-width: 0 !important;
            padding: 0.6rem 0.35rem !important;
            font-size: 0.76rem !important;
        }

        [class*="st-key-card-"] {
            padding: 0.95rem !important;
        }

        .agentic-cta {
            width: 100%;
            box-sizing: border-box;
            font-size: 0.9rem;
        }

        .project-secondary-link {
            width: 100%;
            text-align: center;
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
                <img class="header-avatar" src="{img_src}" alt="Pavan Deep Godi">
                <div class="hero-copy">
                    <div class="hero-eyebrow">Analytics Engineering &nbsp;·&nbsp; BI &nbsp;·&nbsp; Automation</div>
                    <div class="candidate-name">PAVAN DEEP GODI</div>
                    <div class="candidate-title">Analytics & Insights Engineer</div>
                    <div class="status-badge">7+ years turning complex data into business decisions</div>
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
        <div class="summary-kicker">Profile</div>
        <div class="summary-copy"><strong>Analytics & Insights Engineer</strong> with 7+ years of experience turning complex data into reliable analytics for sales and finance teams. Builds SQL, Python, and KNIME pipelines, validates data quality, and delivers Tableau dashboards and KPI datasets. Automates manual and Alteryx-based processes to reduce reporting turnaround and ad-hoc workload. Independently exploring agentic AI through a procurement analytics learning project.</div>
        <div class="pillar-wrapper">
            <span class="pillar-pill">SQL · Python · KNIME</span>
            <span class="pillar-pill">Tableau · Power BI</span>
            <span class="pillar-pill">ETL & Automation</span>
            <span class="pillar-pill">KPI Frameworks</span>
            <span class="pillar-pill">Sales & Finance Analytics</span>
            <span class="pillar-pill">Agentic AI · Learning Project</span>
        </div>
    </div>
""",
    unsafe_allow_html=True,
)

# ---------------------------------------------------------
# 5. High-Impact Highlights
# ---------------------------------------------------------
st.markdown("#### 📈 Selected impact", unsafe_allow_html=True)

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
    with st.container(border=True, key="card-experience-deloitte"):
        st.markdown(
            """
            <div class="exp-header">
                <div class="exp-company">Analytics & Insights Engineer &nbsp;|&nbsp; DELOITTE</div>
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

    with st.container(border=True, key="card-experience-solenis"):
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
        * Built a working capital cash-flow dashboard and refined KPI definitions based on stakeholder feedback, increasing adoption/usage by **30%**.
        * Developed an executive KPI dashboard for weekly performance reviews, improving visibility into core operational metrics and trends.
        * Produced monthly executive performance decks using standardized SQL extracts, translating operational data trends into actions and targets for leadership.
        * Managed the company’s most widely used Purchase Price Variance dashboard, processing millions of records to deliver actionable BU-level, category-level and financial insights to business leaders; maintained weekly and monthly reporting while implementing new metrics, visualizations, and business logic enhancements.
        * Co-developed an interactive analytics view that surfaced **$450K+ cost reduction opportunities** by segmenting spend/performance drivers and enabling targeted operational actions.
        * Partnered with business owners for ad-hoc analytics requests, converting one-off questions into reusable datasets/KPI logic to reduce repeat work.
        * Trained stakeholders on dashboard usage and metric definitions, improving engagement by **5–10%** post-session.
        """
        )

    with st.container(border=True, key="card-experience-tcs"):
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
                    <span class="chip">Agentic AI</span>
                    <span class="chip">Claude</span>
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
        width="stretch",
        hide_index=True,
    )
    st.markdown("</div>", unsafe_allow_html=True)

# TAB 4: ACHIEVEMENTS, PROJECTS & EDUCATION
with tab_projects_edu:
    st.markdown("#### 🏆 Professional Achievements")
    with st.container(border=True, key="card-achievements"):
        st.markdown(
            """
    * **Applause Award — Deloitte:** Recognized for contributions to the Cash Plus Pilot and Sales Executive Insights Dashboard.
    * **Employee Award — Solenis:** Honored for co-developing a raw-material procurement dashboard that identified savings opportunities and contributed to more than $500,000 in cost savings.
    * **Client Recognition — Solenis:** Received multiple commendations for delivering timely reports, actionable KPIs, and data-driven solutions that supported leadership discussions and decision-making.
            """
        )

    st.markdown("---")
    st.markdown("#### 🚀 Personal Projects")
    with st.container(border=True, key="card-project-purchase-intelligence"):
        st.markdown(
            """
        <div class="project-kicker">PERSONAL LEARNING PROJECT &nbsp;·&nbsp; MOCK DATA</div>
        <h3 class="project-title">Purchase Intelligence</h3>
        <p class="project-summary"><strong>Project:</strong> An independent learning project exploring how AI can safely assist procurement analytics, using mock purchase data. It is not real company data and not a purchasing system.</p>
        <p class="project-summary"><strong>What it does:</strong> It validates purchase and supplier-quote records, calculates quarterly spend and indicative savings, and explains what moved spend. An “Ask the analyst” tab answers plain-English questions by running a fixed set of approved analyses. Groq AI can choose which analysis to run and write a short summary; it never calculates, changes data, or places orders. Every number comes from Python, AI-produced figures are cross-checked against it, and the app falls back to plain answers if AI is unavailable.</p>
        <p class="project-summary"><strong>Tech used:</strong> Python, Streamlit, pandas, Plotly, CSV data, Groq AI (free tier, with a token-budget guard), and automated tests with an 18-question evaluation set.</p>
        <div class="project-actions">
            <a class="agentic-cta" href="https://purchaseintelligence.streamlit.app/" target="_blank" rel="noopener noreferrer">🚀 Explore the live demo <span aria-hidden="true">↗</span></a>
            <a class="project-secondary-link" href="https://github.com/pavandeep-godi/Purchase-Intelligence" target="_blank" rel="noopener noreferrer">View source on GitHub ↗</a>
        </div>
        """,
            unsafe_allow_html=True,
        )

    with st.container(border=True, key="card-project-ipl-analytics"):
        st.markdown(
            """
        <div class="project-kicker">PERSONAL PROJECT &nbsp;·&nbsp; SPORTS ANALYTICS</div>
        <h3 class="project-title">IPL Auction Analytics</h3>
        <p class="project-summary"><strong>Project:</strong> An interactive decision-support tool for IPL auction analysis.</p>
        <p class="project-summary"><strong>What it does:</strong> It analyzes player and squad-building parameters to help compare potential auction choices.</p>
        <p class="project-summary"><strong>Tech used:</strong> Python and Streamlit.</p>
        <div class="project-actions">
            <a class="agentic-cta" href="https://iplanalytics-gpd718.streamlit.app/" target="_blank" rel="noopener noreferrer">🏏 Explore the dashboard <span aria-hidden="true">↗</span></a>
            <a class="project-secondary-link" href="https://github.com/pavandeep-godi/IPL_Analytics" target="_blank" rel="noopener noreferrer">View source on GitHub ↗</a>
        </div>
        """,
            unsafe_allow_html=True,
        )

    with st.container(border=True, key="card-project-data-analyst-ai-agent"):
        st.markdown(
            """
        <div class="project-kicker">FREE-TIER BUILD &nbsp;·&nbsp; NATURAL-LANGUAGE ANALYTICS</div>
        <h3 class="project-title">Text to SQL Analytics AI Agent</h3>
        <p class="project-summary"><strong>Project:</strong> A cost-conscious Text-to-SQL analytics proof of concept built with free-tier resources.</p>
        <p class="project-summary"><strong>What it does:</strong> It turns plain-English questions about synthetic sales and procurement data into SQL-backed results with a chart, concise summary, and results table.</p>
        <p class="project-summary"><strong>Tech used:</strong> Python, Streamlit, DuckDB, SQL, and the Groq AI API with free-tier access.</p>
        <div class="project-actions">
            <a class="agentic-cta" href="https://text-to-sql-analyst.streamlit.app/" target="_blank" rel="noopener noreferrer">🤖 Try the live AI agent <span aria-hidden="true">↗</span></a>
            <a class="project-secondary-link" href="https://github.com/pavandeep-godi/Text_To_SQL_Analyst" target="_blank" rel="noopener noreferrer">View source on GitHub ↗</a>
        </div>
        """,
            unsafe_allow_html=True,
        )

    st.markdown("---")
    st.markdown("#### 🎓 Education")
    with st.container(border=True, key="card-education"):
        st.markdown(
            """
        **Bachelor of Technology in Engineering** | Gitam University (2015 – 2019)
        * **Course:** Electronics and Communication Engineering
        """
        )