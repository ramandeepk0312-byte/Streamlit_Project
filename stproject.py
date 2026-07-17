import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu
import plotly.express as px
import plotly.graph_objects as go
import numpy as np

st.set_page_config(
    page_title="AI IMPACT ANALYTICS",
    layout="wide"
)
st.markdown("""
<style>
[data-testid="stSidebar"] > div:first-child{
    padding-top: 0rem;
}
.block-container{
    padding-top: 0.5rem;
}
</style>
""", unsafe_allow_html=True)
df = pd.read_csv("ai_student_impact_dataset (1).csv")
with st.sidebar:

    st.markdown("""
            <div style='text-align:center;'>
                <div style='
                    font-size:50px;
                    margin-bottom:-23px;
                    margin-top:-20px;
                '>
                    🎓
                </div>
                <h2 style='
                    color:white;
                    font-size:38px;
                    margin-top:0px;
                    margin-bottom:-13px;
                '>
                    EDU AI
                </h2>
                <h4 style='
                    color:white;
                    font-size:16px;
                    letter-spacing:3px;
                    margin-top:0px;
                    margin-bottom:-23px;
                '>
                    STUDENT ANALYTICS
                </h4>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("""
<h2 style='text-align:center; color:white; margin-bottom:5px;'>
📊 ANALYSIS HUB
</h2>
""", unsafe_allow_html=True)
    page = option_menu(
                    menu_title=None,
                    options=[
                        "Overview",
                        "Upload & Preview",
                        "Data Cleaning",
                        "Student Demographics",
                        "AI Usage Analytics",
                        "Academic Performance",
                        "Learning Behavior",
                        "Student Well-Being",
                        "Correlation Analysis",
                        "Insights",
                        "Export Report"
                    ],
                    icons=[
                        "house",
                        "folder",
                        "brush",
                        "people",
                        "robot",
                        "graph-up",
                        "book",
                        "emoji-frown",
                        "fire",
                        "lightbulb",
                        "download"
                    ],
                    default_index=0,
                    styles={
                        "container": {
                            "padding": "0!important",
                            "background-color": "#262730"
                        },
                        "icon": {
                            "color": "#FF4B4B",
                            "font-size": "18px"
                        },
                        "nav-link": {
                            "font-size": "15px",
                            "text-align": "left",
                            "margin": "4px",
                            "--hover-color": "#3a1a2f"
                        },
                        "nav-link-selected": {
                            "background-color": "#FF4B4B",
                            "color": "white"
                        }
                    }
                )
    filtered_df = df.copy()
filter_pages = [
    "Overview",
    "Student Demographics",
    "AI Usage Analytics",
    "Academic Performance",
    "Learning Behavior",
    "Student Well-Being",
    "Correlation Analysis",
    "Insights"
]

if page in filter_pages:
            st.sidebar.markdown("## ⚙️ Filters")
            major_filter = st.sidebar.multiselect(
                "🎓 Major Category",
                sorted(df["Major_Category"].unique())
            )

            year_filter = st.sidebar.multiselect(
                "📚 Year of Study",
                sorted(df["Year_of_Study"].unique())
            )

            use_case_filter = st.sidebar.multiselect(
                "🤖 Primary Use Case",
                sorted(df["Primary_Use_Case"].unique())
            )

            subscription_filter = st.sidebar.multiselect(
                "💳 Paid Subscription",
                sorted(df["Paid_Subscription"].unique())
            )

            weekly_hours_filter = st.sidebar.slider(
                "⏰ Weekly GenAI Hours",
                int(df["Weekly_GenAI_Hours"].min()),
                int(df["Weekly_GenAI_Hours"].max()),
                (
                    int(df["Weekly_GenAI_Hours"].min()),
                    int(df["Weekly_GenAI_Hours"].max())
                )
            )

            with st.sidebar.expander("🔽 Advanced Filters", expanded=False):

                prompt_filter = st.multiselect(
                    "🛠 Prompt Engineering Skill",
                    sorted(df["Prompt_Engineering_Skill"].unique())
                )

                tool_filter = st.multiselect(
                    "🔧 Tool Diversity",
                    sorted(df["Tool_Diversity"].unique())
                )

                dependency_filter = st.multiselect(
                    "🤝 AI Dependency",
                    sorted(df["Perceived_AI_Dependency"].unique())
                )

                policy_filter = st.multiselect(
                    "🏫 Institutional Policy",
                    sorted(df["Institutional_Policy"].unique())
                )

                anxiety_filter = st.multiselect(
                    "😟 Anxiety During Exams",
                    sorted(df["Anxiety_Level_During_Exams"].unique())
                )

                burnout_filter = st.multiselect(
                    "🔥 Burnout Risk Level",
                    sorted(df["Burnout_Risk_Level"].unique())
                )

            if major_filter:
                filtered_df = filtered_df[
                    filtered_df["Major_Category"].isin(major_filter)
                ]

            if year_filter:
                filtered_df = filtered_df[
                    filtered_df["Year_of_Study"].isin(year_filter)
                ]

            if use_case_filter:
                filtered_df = filtered_df[
                    filtered_df["Primary_Use_Case"].isin(use_case_filter)
                ]

            if subscription_filter:
                filtered_df = filtered_df[
                    filtered_df["Paid_Subscription"].isin(subscription_filter)
                ]

            if prompt_filter:
                filtered_df = filtered_df[
                    filtered_df["Prompt_Engineering_Skill"].isin(prompt_filter)
                ]

            if tool_filter:
                filtered_df = filtered_df[
                    filtered_df["Tool_Diversity"].isin(tool_filter)
                ]

            if dependency_filter:
                filtered_df = filtered_df[
                    filtered_df["Perceived_AI_Dependency"].isin(dependency_filter)
                ]

            if policy_filter:
                filtered_df = filtered_df[
                    filtered_df["Institutional_Policy"].isin(policy_filter)
                ]

            if anxiety_filter:
                filtered_df = filtered_df[
                    filtered_df["Anxiety_Level_During_Exams"].isin(anxiety_filter)
                ]

            if burnout_filter:
                filtered_df = filtered_df[
                    filtered_df["Burnout_Risk_Level"].isin(burnout_filter)
                ]

            filtered_df = filtered_df[
                (filtered_df["Weekly_GenAI_Hours"] >= weekly_hours_filter[0]) &
                (filtered_df["Weekly_GenAI_Hours"] <= weekly_hours_filter[1])
            ]

            st.markdown("""
            <style>
            .block-container{
                padding-top:2px;
            }
            </style>
            """, unsafe_allow_html=True)
if page=="Overview":
            st.markdown("""
                    <div style="display: flex; 
                        flex-direction: column; 
                        justify-content: flex-start;
                        line-height: 1.1; 
                        margin-top: 40px;">
                        <span style="color: #FF4B4B; 
                        font-size: 55px; 
                        font-weight: 800; 
                        letter-spacing: 4px; 
                        margin: 0; 
                        padding: 0;">
                            AI IMPACT ANALYTICS
                        </span>
                        <span style="color: gray; 
                        font-size: 15px; 
                        letter-spacing: 3px; 
                        margin-top: 5px; 
                        margin-bottom:5px;
                        padding: 0;">
                            Advanced Student Learning & Performance Insights System
                        </span>
                    </div>
                    </style>
                    """, unsafe_allow_html=True)

            st.markdown("""
                    <style>
                    .card {
                        background-color:#111111;
                        border:1px solid #3a1a2f;
                        border-radius:8px;
                        padding:8px;
                        height:105px;
                        margin-top:5px;
                        text-align:center;
                        box-shadow:0 0 10px rgba(255,75,75,0.12);
                        transition: all 0.3s ease-in-out; 
                    }

                    .card:hover {
                        transform: translateY(-5px); 
                        box-shadow: 0 8px 20px rgba(255, 75, 75, 0.4); 
                    }

                    .card-value {
                        color:#FF4B4B;
                        font-size:24px;
                        font-weight:bold;
                        margin-top:5px;
                        margin-bottom:8px;
                    }
                    .card-info {
                        color: #aaa;
                        font-size: 12px;
                        margin-top: 4px;
                    }
                            
                    .card-label {
                        color:white;
                        font-size:14px;
                        font-weight:600;
                        letter-spacing: 1px; 
                    }
                    </style>
                    """, unsafe_allow_html=True)

            col1, col2, col3, col4 = st.columns(4, gap="small")
            with col1:
                        st.markdown(f"""
                        <div class="card" title="Total number of students available in the dataset">
                            <div class="card-value">{len(filtered_df):,}</div>
                            <div class="card-label">TOTAL STUDENTS</div>
                        </div>
                        """,unsafe_allow_html=True)

            with col2:
                            majors = ", ".join(sorted(filtered_df["Major_Category"].unique()))

                            st.markdown(f"""
                            <div class="card"
                                title="Major Categories: {majors}">
                                <div class="card-value">
                                    {filtered_df["Major_Category"].nunique()}
                                </div>
                                <div class="card-label">
                                    MAJOR CATEGORIES
                                </div>
                            </div>
                            """,unsafe_allow_html=True)


            with col3:
                            use_cases = ", ".join(
                                filtered_df["Primary_Use_Case"].unique()[:5]
                            )

                            st.markdown(f"""
                            <div class="card"
                                title="Top Use Cases: {use_cases}">
                                <div class="card-value">
                                    {filtered_df["Primary_Use_Case"].nunique()}
                                </div>
                                <div class="card-label">
                                    AI USE CASES
                                </div>
                            </div>
                            """,unsafe_allow_html=True)

            with col4:
                            st.markdown(f"""
                            <div class="card"
                                title="Average post-semester GPA of students">
                                <div class="card-value">
                                    {round(filtered_df["Post_Semester_GPA"].mean(),2)}
                                </div>
                                <div class="card-label">
                                    AVERAGE GPA
                                </div>
                            </div>
                            """,unsafe_allow_html=True)

            st.markdown("""
                        <style>
                        .card {
                            background-color:#111111;
                            border:1px solid #3a1a2f;
                            border-radius:8px;
                            padding:8px;
                            height:105px;
                            margin-top:5px;
                            text-align:center;
                            box-shadow:0 0 10px rgba(255,75,75,0.12);
                            transition: all 0.3s ease-in-out; 
                        }

                        .card:hover {
                            transform: translateY(-5px); 
                            box-shadow: 0 8px 20px rgba(255, 75, 75, 0.4); 
                        }

                        .card-value {
                            color:#FF4B4B;
                            font-size:24px;
                            font-weight:bold;
                            margin-top:5px;
                            margin-bottom:8px;
                        }

                        .card-info {
                            color: #aaa;
                            font-size: 12px;
                            margin-top: 4px;
                        }
                            
                        .card-label {
                            color:white;
                            font-size:14px;
                            font-weight:600;
                            letter-spacing: 1px; 
                        }
                        </style>
                        """, unsafe_allow_html=True)
            col5,col6,col7,col8 = st.columns(4,gap="small")

            with col5:
                            st.markdown(f"""
                            <div class="card"
                                title="Average weekly hours spent using GenAI tools">
                                <div class="card-value">
                                    {round(filtered_df["Weekly_GenAI_Hours"].mean(),1)}
                                </div>
                                <div class="card-label">
                                    AVERAGE AI HOURS
                                </div>
                            </div>
                            """,unsafe_allow_html=True)

            with col6:
                            paid_percentage = round(
                                filtered_df["Paid_Subscription"].mean()*100,1
                            )

                            st.markdown(f"""
                            <div class="card"
                                title="Percentage of students using paid AI subscriptions">
                                <div class="card-value">
                                    {paid_percentage}%
                                </div>
                                <div class="card-label">
                                    PAID SUBSCRIPTION
                                </div>
                            </div>
                            """,unsafe_allow_html=True)
                            
            with col7:
                            st.markdown(f"""
                            <div class="card"
                                title="Average student skill retention score">
                                <div class="card-value">
                                    {round(filtered_df["Skill_Retention_Score"].mean(),1)}
                                </div>
                                <div class="card-label">
                                    SKILL RETENTION
                                </div>
                            </div>
                            """,unsafe_allow_html=True)

            with col8:
                            st.markdown(f"""
                            <div class="card"
                                title="Total number of columns in the dataset">
                                <div class="card-value">
                                    {filtered_df.shape[1]}
                                </div>
                                <div class="card-label">
                                    DATASET COLUMNS
                                </div>
                            </div>
                            """,unsafe_allow_html=True)
            st.divider()

            st.markdown("""
                    <style>
                    .insight-card {
                        background-color:#111111;
                        border:1px solid #3a1a2f;       
                        border-radius: 8px;
                        padding: 8px;
                        height:105px;
                        margin-top:5px;
                        text-align:center;
                        box-shadow:0 0 10px rgba(255,75,75,0.12);
                        transition: all 0.3s ease-in-out;
                        position: relative;
                    }
                    .insight-card:hover {
                        transform: translateY(-5px);
                        box-shadow: 0 4px 12px rgba(37, 99, 235, 0.6);
                    }

                    .insight-card[data-tooltip] {
                        position: relative;
                        cursor: pointer;
                    }

                    .insight-card[data-tooltip]:hover::after {
                        content: attr(data-tooltip);
                        white-space: pre-line; 
                        position: absolute;
                        left: 50%;
                        top: -100%;
                        transform: translateX(-50%);
                        background: #333;
                        color: #fff;
                        padding: 8px 12px;
                        border-radius: 6px;
                        font-size: 13px;
                        box-shadow: 0 2px 6px rgba(0,0,0,0.3);
                        z-index: 999;
                        width: max-content;
                        max-width: 240px;
                        opacity: 0;
                        transition: opacity 0.3s ease-in-out;
                    }
                    
                    .insight-card[data-tooltip]:hover::after {
                        opacity: 1;
                    }
                    </style>
                    """, unsafe_allow_html=True)

            st.markdown("### 💡 QUICK INSIGHTS")

            col1, col2, col3 = st.columns(3, gap="small")

            if not filtered_df.empty:

                            with col1:
                                top_major = filtered_df["Major_Category"].mode()[0]
                                st.markdown(f"""
                                <div class="insight-card"
                                data-tooltip="Major Categories in Dataset:\n• STEM\n• Business\n• Arts\n• Humanities\n• Medical">
                                    <div class="insight-icon">🎓</div>
                                    <div class="insight-title">Most Common Major</div>
                                    <div class="insight-value">{top_major}</div>
                                </div>
                                """, unsafe_allow_html=True)

                            
                            with col2:
                                top_use = filtered_df["Primary_Use_Case"].mode()[0]
                                st.markdown(f"""
                                <div class="insight-card"
                                data-tooltip="Popular AI Activities:\n• Debugging/Troubleshooting\n• Copywriting/Drafting\n• Direct Answer Generation\n• Summarizing Reading\n• Ideation">
                                    <div class="insight-icon">🤖</div>
                                    <div class="insight-title">Most Popular AI Use Case</div>
                                    <div class="insight-value">{top_use}</div>
                                </div>
                                """, unsafe_allow_html=True)


                            
                            with col3:
                                improvement = round(
                                    filtered_df["Post_Semester_GPA"].mean()
                                    - filtered_df["Pre_Semester_GPA"].mean(),
                                    2
                                )
                                st.markdown(f"""
                                <div class="insight-card"
                                data-tooltip="A positive value indicates an improvement in GPA after AI usage during the semester.">
                                    <div class="insight-icon">📈</div>
                                    <div class="insight-title">Average GPA Improvement</div>
                                    <div class="insight-value">+{improvement}</div>
                                </div>
                                """, unsafe_allow_html=True)
            else:
                        st.warning("No data available after filtering.")

            st.divider()
            st.markdown("<br>", unsafe_allow_html=True)

            st.markdown("""
            <div style="
                background-color:#111111;
                border:1px solid #3a1a2f;
                border-radius:12px;
                padding:25px;
                margin-top:20px;
                box-shadow:0 0 12px rgba(255,75,75,0.15);
            ">

            <h2 style="
                color:#FF4B4B;
                margin-top:0;
                margin-bottom:20px;
                text-align:center;
            ">
            🎯 Project Objectives
            </h2>

            <p style="color:white; font-size:18px; line-height:1.8;">

            ✅ Analyze AI adoption patterns among students.<br>

            ✅ Study the impact of AI on academic performance.<br>

            ✅ Understand learning behavior and study habits.<br>

            ✅ Examine anxiety, burnout, and student well-being.<br>

            ✅ Explore relationships between AI usage and academic outcomes.<br>

            ✅ Generate insights for responsible and effective AI usage.

            </p>

            </div>
            """, unsafe_allow_html=True)
            st.divider()
            st.markdown("""
            <div style="
                background-color:#111111;
                border:1px solid #3a1a2f;
                border-radius:12px;
                padding:20px;
                margin-top:20px;
                box-shadow:0 0 12px rgba(255,75,75,0.15);
            ">

            <h2 style="
                color:#FF4B4B;
                text-align:center;
                margin-bottom:15px;
            ">
            ⚙️ Project Workflow
            </h2>

            <p style="
                color:white;
                font-size:18px;
                text-align:center;
                line-height:1.8;
            ">
            📥 Data Collection &nbsp; | &nbsp;
            🧹 Data Cleaning &nbsp; | &nbsp;
            📊 Analysis &nbsp; | &nbsp;
            📈 Visualization &nbsp; | &nbsp;
            🔗 Correlation &nbsp; | &nbsp;
            💡 Insights
            </p>

            </div>
            """, unsafe_allow_html=True)
            st.divider()
            st.markdown("""
        <div style="
            text-align:center;
            padding:20px;
            margin-top:25px;
            color:#b0b0b0;
            font-size:17px;
            line-height:1.8;
        ">

        🚀 Explore how Generative AI is reshaping student learning,
        academic performance, and well-being through interactive analytics.

        <br><br>

        <span style="color:#FF6B6B; font-size:20px; font-weight:600;">
        Scroll through the dashboard to uncover insights and trends.
        </span>

        </div>
        """, unsafe_allow_html=True)
elif page == "Upload & Preview":
    st.markdown("""
                                <div style="display: flex; 
                                    flex-direction: column; 
                                    justify-content: flex-start;
                                    line-height: 1.1; 
                                    margin-top: 40px;">
                                    <span style="color: #FF4B4B; 
                                    font-size: 55px; 
                                    font-weight: 800; 
                                    letter-spacing: 4px; 
                                    margin: 0; 
                                    padding: 0;">
                                    <span style="font-size:50px;">📁</span>
                                         Upload & Preview
                                    </span>
                                    <span style="color: gray; 
                        font-size: 15px; 
                        letter-spacing: 3px; 
                        margin-top: 5px; 
                        margin-bottom:5px;
                        padding: 0;">
                            Explore dataset structure, preview records, and review key information.
                        </span>
                                </div>
                                </style>
                                """, unsafe_allow_html=True)

    st.markdown("""
            <style>
            .card {
                background-color:#111111;
                border:1px solid #3a1a2f;
                border-radius:8px;
                padding:8px;
                height:110px;
                margin-top:5px;
                text-align:center;
                box-shadow:0 0 10px rgba(255,75,75,0.12);
                transition: all 0.3s ease-in-out;
            }

            .card:hover {
                transform: translateY(-5px);
                box-shadow: 0 8px 20px rgba(255,75,75,0.4);
            }

            .card-value {
                color:#FF4B4B;
                font-size:24px;
                font-weight:bold;
                margin-top:5px;
                margin-bottom:8px;
            }

            .card-label {
                color:white;
                font-size:14px;
                font-weight:600;
                letter-spacing:1px;
            }
            </style>
            """, unsafe_allow_html=True)

    col1, col2, col3, col4, col5= st.columns(5, gap="small")
                
    with col1:
                                                st.markdown(f"""
                                                <div class="card">
                                                    <div class="card-value">{df.shape[0]:,}</div>
                                                    <div class="card-label"> 👥 TOTAL ROWS</div>
                                                </div>
                                                """, unsafe_allow_html=True)

    with col2:
                                                st.markdown(f"""
                                                <div class="card">
                                                    <div class="card-value">{df.shape[1]}</div>
                                                    <div class="card-label">📋 TOTAL COLUMNS</div>
                                                </div>
                                                """, unsafe_allow_html=True)

    with col3:
                                                st.markdown(f"""
                                                <div class="card">
                                                    <div class="card-value">{df.isnull().sum().sum()}</div>
                                                    <div class="card-label">⚠️ MISSING VALUES</div>
                                                </div>
                                                """, unsafe_allow_html=True)

    with col4:
                                                st.markdown(f"""
                                                <div class="card">
                                                    <div class="card-value">{df.duplicated().sum()}</div>
                                                    <div class="card-label">🔄 DUPLICATE RECORDS</div>
                                                </div>
                                                """, unsafe_allow_html=True)
    memory_usage = df.memory_usage(deep=True).sum() / (1024 * 1024)

    with col5:
                                                st.markdown(f"""
                                            <div class="card">
                                                <div class="card-value">{memory_usage:.2f} MB</div>
                                                <div class="card-label">💾 MEMORY USAGE</div>
                                            </div>
                                            """, unsafe_allow_html=True)
    st.divider()
    st.markdown("""
        <div style="
        text-align:center;
        margin:30px 0px 20px 0px;
">
    <h2 style="
        color:#ff4d4d;
        font-size:32px;
        font-weight:700;
        margin:0;
        margin-top:-30px;
        margin-bottom:-10px;
    ">
        📊 Analytics Modules
    </h2>
    <p style="
        color:#888;
        font-size:15px;
        margin-top:0px;
    ">
        Explore the key analytical areas of the dashboard
    </p>
</div>
""", unsafe_allow_html=True)
    st.markdown("""
    <style>
    .coverage-card{
    background:#0d0d0d;
    border:1px solid rgba(255,0,90,0.35);
    border-radius:18px;
    padding:15px;
    text-align:center;
    transition:0.3s ease;
    margin-bottom:15px;
}
    .coverage-card:hover{
    transform:translateY(-8px) scale(1.02);
    box-shadow:0px 0px 30px rgba(255,77,77,0.55);
}

    .coverage-icon{
    font-size:35px;
    margin-bottom:10px;
}

    .coverage-title{
    color:white;
    font-size:17px;
    font-weight:600;
}

    .coverage-subtitle{
    color:#ff4d6d;
    font-size:13px;
    margin-top:8px;
}
</style>
""", unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
    <div class="coverage-card">
        <div class="coverage-icon">👨‍🎓</div>
        <div class="coverage-title">Student Demographics</div>
        <div class="coverage-subtitle">Student profile analysis</div>
    </div>
    """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
    <div class="coverage-card">
        <div class="coverage-icon">⚡</div>
        <div class="coverage-title">AI Usage Analytics</div>
        <div class="coverage-subtitle">AI usage patterns</div>
    </div>
    """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
    <div class="coverage-card">
        <div class="coverage-icon">📈</div>
        <div class="coverage-title">Academic Performance</div>
        <div class="coverage-subtitle">GPA insights</div>
    </div>
    """, unsafe_allow_html=True)

    col4, col5, col6 = st.columns(3)

    with col4:
        st.markdown("""
    <div class="coverage-card">
        <div class="coverage-icon">🧠</div>
        <div class="coverage-title">Learning Behavior</div>
        <div class="coverage-subtitle">Study habits analysis</div>
    </div>
    """, unsafe_allow_html=True)

    with col5:
        st.markdown("""
    <div class="coverage-card">
        <div class="coverage-icon">😊</div>
        <div class="coverage-title">Student Well-being</div>
        <div class="coverage-subtitle">Stress & burnout trends</div>
    </div>
    """, unsafe_allow_html=True)

    with col6:
        st.markdown("""
    <div class="coverage-card">
        <div class="coverage-icon">🔗</div>
        <div class="coverage-title">Correlation Analysis</div>
        <div class="coverage-subtitle">Feature relationships</div>
    </div>
    """, unsafe_allow_html=True)
    st.divider()
    tab1, tab2, tab3 = st.tabs([
    "📄 Dataset Preview",
    "ℹ️ Dataset Information",
    "📊 Category Distribution"
])
    with tab1:
        st.subheader("📄 Dataset Preview")

        st.dataframe(
            df.head(10),
            use_container_width=True,
            hide_index=True
        )

        st.caption(f"Showing first 10 rows out of {len(df):,} records.")
        show_full = st.checkbox("Show complete dataset")

        if show_full:
            st.dataframe(df, use_container_width=True)
    with tab2:
        st.subheader("ℹ️ Dataset Information")

        info_df = pd.DataFrame({
            "Column Name": df.columns,
            "Data Type": df.dtypes.astype(str),
            "Missing Values": df.isnull().sum().values,
            "Unique Values": df.nunique().values
        })

        st.dataframe(
            info_df,
            use_container_width=True,
            hide_index=True
        )
    with tab3:
        st.subheader("📊 Category Distribution")

        selected_col = st.selectbox(
            "Select Category",
            [
                "Major_Category",
                "Year_of_Study",
                "Primary_Use_Case",
                "Paid_Subscription",
                "Burnout_Risk_Level"
            ]
        )

        counts = df[selected_col].value_counts()

        st.bar_chart(counts)
    st.markdown("""
    <div style="margin-top:20px;">
        <h1 style="
            color:#ff4d4d;
            margin-bottom:0px;
            font-size:32px;
        ">
            📊 Dataset Composition
        </h1>
        <p style="
            color:#9ca3af;
            font-size:15px;
            margin-top:0px;
        ">
            Dataset structure and feature distribution
        </p>
    </div>
    """, unsafe_allow_html=True)
    num_cols = len(df.select_dtypes(include=['int64', 'float64']).columns)
    cat_cols = len(df.select_dtypes(include=['object']).columns)
    composition_df = pd.DataFrame({
        "Feature Type": [
            "Numerical Features",
            "Categorical Features"
        ],
        "Count": [
            num_cols,
            cat_cols
        ]
    })
    fig = px.pie(
        composition_df,
        names="Feature Type",
        values="Count",
        hole=0.72,
        color="Feature Type",
        color_discrete_map={
            "Numerical Features": "#6366F1",
            "Categorical Features": "#FF4D4D"
        }
    )
    fig.update_traces(
        textinfo='percent',
        textfont_size=18,
        hovertemplate=
        "<b>%{label}</b><br>" +
        "Columns: %{value}<br>" +
        "Percentage: %{percent}<extra></extra>"
    )
    fig.add_annotation(
        text=f"""
        <span style='font-size:34px'><b>{len(df.columns)}</b></span>
        <br>
        <span style='font-size:16px;color:gray'>Total Columns</span>
        """,
        x=0.5,
        y=0.5,
        showarrow=False,
        font=dict(color="white")
    )
    fig.update_layout(
        template="plotly_dark",
        height=550,
        showlegend=True,
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        title={
            "text": "<b>Dataset Structure</b>",
            "x": 0.5,
            "font": {
                "size": 28
            }
        },
        legend=dict(
            orientation="h",
            y=-0.12,
            x=0.25,
            font=dict(
                size=15
            )
        ),
        margin=dict(
            t=80,
            b=80,
            l=20,
            r=20
        )
    )
    st.plotly_chart(
        fig,
        use_container_width=True
    )
    st.markdown("""
    <style>
    .summary-box{
        background: linear-gradient(135deg,#111111,#1a1a1a);
        border:1px solid rgba(255,77,77,0.4);
        border-left:6px solid #ff4d4d;
        border-radius:15px;
        padding:20px;
        margin-top:20px;
        box-shadow:0px 0px 20px rgba(255,77,77,0.15);
    }
    .summary-title{
        color:#ff4d4d;
        font-size:24px;
        font-weight:700;
        margin-bottom:15px;
    }
    .summary-text{
        color:white;
        font-size:16px;
        line-height:2;
    }
    </style>
    <div class="summary-box">
        <div class="summary-title">
            📌 Key Dataset Insights
        </div>
        <div class="summary-text">
            • Dataset contains <b>50,000 student records</b> and <b>16 features</b>.<br>
            • Students belong to <b>5 major categories</b> across multiple years of study.<br>
            • Dataset quality is excellent with <b>0 missing values</b> and <b>0 duplicate records</b>.<br>
            • The dataset contains both <b>numerical</b> and <b>categorical</b> variables.<br>
            • The data is ready for advanced analytics and visualization tasks.
        </div>
    </div>
    """, unsafe_allow_html=True)

elif page == "Data Cleaning":
        st.markdown("""
    <div style="display:flex;
                flex-direction:column;
                justify-content:flex-start;
                line-height:1.1;
                margin-top:40px;">
        <span style="color:#ff4d4d;
                    font-size:55px;
                    font-weight:800;
                    letter-spacing:4px;">
            🧹 Data Cleaning
        </span>
        <span style="color:gray;
                    font-size:15px;
                    letter-spacing:3px;
                    margin-top:5px;
                    margin-bottom:5px;">
            Detect missing values, remove duplicates,
            validate data quality, and prepare the
            dataset for analysis.
        </span>
    </div>
    """, unsafe_allow_html=True)
        total_records = len(df)
        total_features = len(df.columns)

        numeric_columns = df.select_dtypes(
            include=['int64', 'float64']
        ).shape[1]

        categorical_columns = df.select_dtypes(
            include=['object']
        ).shape[1]

        missing_values = df.isnull().sum().sum()

        duplicate_records = df.duplicated().sum()

        memory_usage = (
            df.memory_usage(deep=True).sum()
            / (1024 * 1024)
        )
        st.markdown("""
        <style>
        .card{
            background-color:#111111;
            border:1px solid #3a1a2f;
            border-radius:8px;
            padding:8px;
            height:112px;
            margin-top:5px;
            text-align:center;
            box-shadow:0 0 10px rgba(255,75,75,0.12);
            transition:all 0.3s ease-in-out;
        }
        .card:hover{
            transform:translateY(-5px);
            box-shadow:0 8px 20px rgba(255,75,75,0.4);
        }
        .card-value{
            color:#FF4B4B;
            font-size:24px;
            font-weight:bold;
            margin-top:5px;
            margin-bottom:8px;
        }
        .card-label{
            color:white;
            font-size:14px;
            font-weight:600;
            letter-spacing:1px;
        }
        </style>
        """, unsafe_allow_html=True)
        col1, col2, col3, col4, col5, col6 = st.columns(
            6,
            gap="small"
        )
        with col1:
            st.markdown(f"""
            <div class="card">
                <div class="card-value">{total_records:,}</div>
                <div class="card-label">📄 TOTAL RECORDS</div>
            </div>
            """, unsafe_allow_html=True)
        with col2:
            st.markdown(f"""
            <div class="card">
                <div class="card-value">{total_features}</div>
                <div class="card-label">📊 TOTAL FEATURES</div>
            </div>
            """, unsafe_allow_html=True)
        with col3:
            st.markdown(f"""
            <div class="card">
                <div class="card-value">{numeric_columns}</div>
                <div class="card-label">🔢 NUMERIC COLUMNS</div>
            </div>
            """, unsafe_allow_html=True)
        with col4:
            st.markdown(f"""
            <div class="card">
                <div class="card-value">{categorical_columns}</div>
                <div class="card-label">🔤 CATEGORICAL COLUMNS</div>
            </div>
            """, unsafe_allow_html=True)
        with col5:
            st.markdown(f"""
            <div class="card">
                <div class="card-value">{missing_values:,}</div>
                <div class="card-label">⚠️ MISSING VALUES</div>
            </div>
            """, unsafe_allow_html=True)
        with col6:
            st.markdown(f"""
            <div class="card">
                <div class="card-value">{duplicate_records:,}</div>
                <div class="card-label">🔄 DUPLICATES</div>
            </div>
            """, unsafe_allow_html=True)
        st.divider()
        st.subheader("🛠 Cleaning Steps Performed")

        st.markdown("""
        ✔ Checked for missing values in all columns.

        ✔ Verified duplicate records in the dataset.

        ✔ Validated data types of all features.

        ✔ Separated numerical and categorical columns.

        ✔ Prepared the dataset for analysis and visualization.
        """)
        st.divider()
        st.subheader("🗂 Dataset Structure")

        col_info = pd.DataFrame({
            "Column Name": df.columns,
            "Data Type": df.dtypes.astype(str),
            "Missing Values": df.isnull().sum().values
        })

        st.dataframe(
            col_info,
            use_container_width=True,
            hide_index=True
        )
        st.divider()
        st.subheader("📌 Data Cleaning Outcome")

        st.success("Dataset quality validation completed successfully.")

        st.write("• No missing values were detected in the dataset.")
        st.write("• No duplicate records were found.")
        st.write("• All columns contained valid data types.")
        st.write("• The dataset was ready for analysis without additional preprocessing.")

elif page=="Student Demographics":
    st.markdown("""
    <div style="display: flex;
                flex-direction: column;
                justify-content: flex-start;
                line-height: 1.1;
                margin-top: 40px;">
        <span style="color: #FF4B4B;
                    font-size: 55px;
                    font-weight: 800;
                    letter-spacing: 4px;
                    margin: 0;
                    padding: 0;">
                <span style="font-size:50px;">👥</span>
             Student Demographics
        </span>
        <span style="color: gray;
                    font-size: 15px;
                    letter-spacing: 3px;
                    margin-top: 5px;
                    margin-bottom: 5px;
                    padding: 0;">
            Explore student distribution across majors, years of study, subscription preferences, and AI usage patterns.
        </span>
    </div>
    """, unsafe_allow_html=True)
    total_students = len(df)

    major_categories = df["Major_Category"].nunique()

    years_of_study = df["Year_of_Study"].nunique()
    paid_percentage = round(df["Paid_Subscription"].mean() * 100, 1
)
    avg_ai_hours = round(
            df["Weekly_GenAI_Hours"].mean(),
            1
        )

    st.markdown("""
    <style>
    .card {
        background-color:#111111;
        border:1px solid #3a1a2f;
        border-radius:8px;
        padding:8px;
        height:110px;
        margin-top:10px;
        text-align:center;
        box-shadow:0 0 10px rgba(255,75,75,0.12);
        transition: all 0.3s ease-in-out;
    }

    .card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 20px rgba(255,75,75,0.4);
    }

    .card-value {
        color:#FF4B4B;
        font-size:24px;
        font-weight:bold;
        margin-top:5px;
        margin-bottom:8px;
    }

    .card-label {
        color:white;
        font-size:14px;
        font-weight:600;
        letter-spacing:1px;
    }
    </style>
    """, unsafe_allow_html=True)

    col1, col2, col3, col4, col5 = st.columns(5, gap="small")

    with col1:
            st.markdown(f"""
            <div class="card">
                <div class="card-value">{total_students:,}</div>
                <div class="card-label">👥 TOTAL STUDENTS</div>
            </div>
            """, unsafe_allow_html=True)

    with col2:
            st.markdown(f"""
            <div class="card">
                <div class="card-value">{major_categories}</div>
                <div class="card-label">🎓 MAJOR CATEGORIES</div>
            </div>
            """, unsafe_allow_html=True)

    with col3:
            st.markdown(f"""
            <div class="card">
                <div class="card-value">{years_of_study}</div>
                <div class="card-label">📚 YEARS OF STUDY</div>
            </div>
            """, unsafe_allow_html=True)

    with col4:
            st.markdown(f"""
            <div class="card">
                <div class="card-value">{paid_percentage}%</div>
                <div class="card-label">💳 PAID SUBSCRIPTIONS</div>
            </div>
            """, unsafe_allow_html=True)

    with col5:
            st.markdown(f"""
            <div class="card">
                <div class="card-value">{avg_ai_hours}</div>
                <div class="card-label">🤖 AVG AI HOURS</div>
            </div>
            """, unsafe_allow_html=True)

    st.divider()
    st.subheader("🎓 Major Category Distribution")

    major_counts = (
        df["Major_Category"]
        .value_counts()
        .reset_index()
    )

    major_counts.columns = [
        "Major_Category",
        "Students"
    ]

    major_counts["Percentage"] = round(
        major_counts["Students"] /
        major_counts["Students"].sum() * 100,
        1
    )


    chart_type = st.radio(
        "Select Visualization Type",
        [
            "📊 Horizontal Bar Chart",
            "🌹 Nightingale Rose Diagram"
        ],
        horizontal=True,
        key="major_chart_radio"
    )


    fig = None  
    if chart_type == "📊 Horizontal Bar Chart":

            title_col, slider_col = st.columns([5, 2])

            with title_col:
                st.markdown(
                    "<h4 style='margin-bottom:0;'>Students by Major Category</h4>",
                    unsafe_allow_html=True
                )

            with slider_col:
                sort_order = st.select_slider(
                    " ",
                    options=[
                        "Lowest → Highest",
                        "Highest → Lowest"
                    ],
                    value="Highest → Lowest"
                )

            if sort_order == "Highest → Lowest":
                major_counts = major_counts.sort_values(
                        "Students",
                        ascending=False
                    )
            else:
                major_counts = major_counts.sort_values(
                        "Students",
                        ascending=True
                    )
            
            fig = px.bar(
                major_counts,
                x="Students",
                y="Major_Category",
                orientation="h",
                text="Students"
            )

            fig.update_traces(
                textposition="outside",
                hovertemplate=
                "<b>%{y}</b><br>" +
                "Students: %{x}<extra></extra>"
            )

            fig.update_layout(
                hoverlabel=dict(
                    bgcolor="black",
                    font_color="white",
                    font_size=13
                )
            )
    else:
        fig = px.bar_polar(
            major_counts,
            r="Percentage",
            theta="Major_Category",
            color="Major_Category",
            template="plotly_dark"
        )

        fig.update_traces(
            hovertemplate=
            "<b>%{theta}</b><br>" +
            "Percentage: %{r}%<extra></extra>"
        )

        fig.update_layout(
            height=500,
            margin=dict(
                t=60,
                b=40,
                l=40,
                r=40
            ),
            hoverlabel=dict(
                bgcolor="black",
                font_color="white",
                font_size=13
            )
        )

    st.plotly_chart(
        fig,
        use_container_width=True,
        key="major_distribution_chart"
    )
    st.divider()
    st.subheader("🎓 Student Distribution by Year of Study")

    year_counts = (
                    df["Year_of_Study"]
                    .value_counts()
                    .reset_index()
                )

    year_counts.columns = [
                    "Year_of_Study",
                    "Students"
                ]

    chart_type = st.radio(
            "Select Visualization Type",
            [
                "🍩 Donut Chart",
                "📍 Lollipop Chart"
            ],
            horizontal=True,
            key="year_chart_radio"
        )
    if chart_type == "🍩 Donut Chart":

                    fig = px.pie(
                    year_counts,
                    names="Year_of_Study",
                    values="Students",
                    hole=0.55
                )

                    fig.update_traces(
                        textinfo="label+percent",
                        pull=[0.04] * len(year_counts),
                        hovertemplate=
                        "<b>%{label}</b><br>" +
                        "Students: %{value}<br>" +
                        "Percentage: %{percent}<extra></extra>"
                )

                    fig.update_layout(
                        height=500,
                        uniformtext_minsize=12,
                        uniformtext_mode="hide"
                )

    else:
                    fig = px.scatter(
                        year_counts,
                        x="Students",
                        y="Year_of_Study",
                        size="Students",
                        text="Students",
                        title=""
                    )

                    for _, row in year_counts.iterrows():

                        fig.add_shape(
                            type="line",
                            x0=0,
                            y0=row["Year_of_Study"],
                            x1=row["Students"],
                            y1=row["Year_of_Study"],
                            line=dict(
                                width=3
                            )
                        )


                    fig.update_traces(
                    textposition="middle right",
                    marker=dict(
                        size=18,
                        line=dict(
                            width=2
                        )
                    ),
                    hovertemplate=
                    "<b>%{y}</b><br>" +
                    "Students: %{x}<extra></extra>"
                )
                    
                    fig.update_layout(
                        height=500,
                        xaxis_title="Number of Students",
                        yaxis_title="Year of Study",
                        showlegend=False,
                        hoverlabel=dict(
                            bgcolor="black",
                            font_color="white",
                            font_size=13
                        )
                    )

    st.plotly_chart(
        fig,
        use_container_width=True,
        key="year_distribution_chart"
    )
    st.divider()
    st.subheader("📌 Demographic Insights")


    most_common_major = df["Major_Category"].mode()[0]

    largest_year = (
                df["Year_of_Study"]
                .value_counts()
                .idxmax()
            )

    total_years = df["Year_of_Study"].nunique()
    largest_major_share = round(
                (df["Major_Category"].value_counts().max() / len(df)) * 100,
                1
            )
    st.markdown(
                """
                <style>
                .insight-card {
                background: linear-gradient(
                    135deg,
                    rgba(255,255,255,0.08),
                    rgba(255,255,255,0.03)
                );
                padding: 20px;
                border-radius: 18px;
                border: 1px solid rgba(255,0,0,0.3);
                box-shadow:
                    0 0 10px rgba(255,0,0,0.25);
                transition: 0.3s;
                height: 150px;
            }
                .insight-card:hover {
                transform: translateY(-6px);
                box-shadow:
                    0 0 18px rgba(255,0,0,0.45);
                border: 1px solid rgba(255,0,0,0.7);
            }
                .insight-title {
                    font-size: 15px;
                    color: #ff6b6b;
                    font-weight: 600;
                }
                .insight-value {
                    font-size: 24px;
                    font-weight: bold;
                    color: white;
                    margin-top: 12px;
                }
                .insight-icon {
                    font-size: 30px;
                }
                </style>
                """,
                unsafe_allow_html=True
            )

    col1, col2, col3, col4 = st.columns(4)


    with col1:
                    st.markdown(
                    f"""
                    <div class="insight-card">
                        <div class="insight-icon">🎓</div>
                        <div class="insight-title">
                            Most Common Major
                        </div>
                        <div class="insight-value">
                            {most_common_major}
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )


    with col2:
                st.markdown(
                    f"""
                    <div class="insight-card">
                        <div class="insight-icon">👥</div>
                        <div class="insight-title">
                            Largest Student Group
                        </div>
                        <div class="insight-value">
                            {largest_year}
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )


    with col3:
                st.markdown(
                    f"""
                    <div class="insight-card">
                        <div class="insight-icon">📊</div>
                        <div class="insight-title">
                            Academic Years Covered
                        </div>
                        <div class="insight-value">
                            {total_years} Years
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

    with col4:
                st.markdown(
                    f"""
                    <div class="insight-card">
                        <div class="insight-icon">📈</div>
                        <div class="insight-title">
                            Largest Major Share
                        </div>
                        <div class="insight-value">
                            {largest_major_share}%
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )


elif page=="AI Usage Analytics":
        st.markdown("""
    <div style="display: flex;
                flex-direction: column;
                justify-content: flex-start;
                line-height: 1.1;
                margin-top: 40px;">
        <span style="color: #FF4B4B;
                    font-size: 55px;
                    font-weight: 800;
                    letter-spacing: 4px;
                    margin: 0;
                    padding: 0;">
            <span style="font-size:50px;">📊</span>
            AI Usage Analytics
        </span>
        <span style="color: gray;
                    font-size: 15px;
                    letter-spacing: 3px;
                    margin-top: 5px;
                    margin-bottom: 5px;
                    padding: 0;">
            Analyze how students use Generative AI tools, explore usage patterns, subscription trends, prompt skills, and tool diversity insights.
        </span>
    </div>
    """, unsafe_allow_html=True)
        st.markdown("""
        <style>
        .card {
            background-color:#111111;
            border:1px solid #3a1a2f;
            border-radius:8px;
            padding:8px;
            height:110px;
            margin-top:10px;
            text-align:center;
            box-shadow:0 0 10px rgba(255,75,75,0.12);
            transition: all 0.3s ease-in-out;
        }

        .card:hover {
            transform: translateY(-5px);
            box-shadow: 0 8px 20px rgba(255,75,75,0.4);
        }

        .card-value {
            color:#FF4B4B;
            font-size:24px;
            font-weight:bold;
            margin-top:5px;
            margin-bottom:8px;
        }

        .card-label {
            color:white;
            font-size:14px;
            font-weight:600;
            letter-spacing:1px;
        }
        </style>
        """, unsafe_allow_html=True)
        avg_ai_hours = round(
            filtered_df["Weekly_GenAI_Hours"].mean(),
            1
        )

        ai_use_cases = round(
            (filtered_df["Primary_Use_Case"].nunique() / len(filtered_df["Primary_Use_Case"].unique())) * 100,
            1
        )

        paid_users = round(
            filtered_df["Paid_Subscription"].mean() * 100,
            1
        )

        skill_map = {
            "Beginner": 1,
            "Intermediate": 2,
            "Advanced": 3
        }

        skilled_users = round(
            filtered_df["Prompt_Engineering_Skill"]
            .map(skill_map)
            .mean(),
            1
        )

        tool_diversity = round(
            filtered_df["Tool_Diversity"].mean(),
            1
        )

        col1, col2, col3, col4, col5 = st.columns(5, gap="small")

        with col1:
            st.markdown(f"""
            <div class="card">
                <div class="card-value">{avg_ai_hours}</div>
                <div class="card-label">🤖 AVG AI HOURS</div>
            </div>
            """, unsafe_allow_html=True)

        with col2:
            st.markdown(f"""
            <div class="card">
                <div class="card-value">{ai_use_cases}%</div>
                <div class="card-label">🎯 AI USE CASES</div>
            </div>
            """, unsafe_allow_html=True)

        with col3:
            st.markdown(f"""
            <div class="card">
                <div class="card-value">{paid_users}%</div>
                <div class="card-label">💳 PAID USERS</div>
            </div>
            """, unsafe_allow_html=True)

        with col4:
            st.markdown(f"""
            <div class="card">
                <div class="card-value">{skilled_users}</div>
                <div class="card-label">🧠 SKILLED USERS</div>
            </div>
            """, unsafe_allow_html=True)

        with col5:
            st.markdown(f"""
            <div class="card">
                <div class="card-value">{tool_diversity}</div>
                <div class="card-label">🛠 TOOL DIVERSITY</div>
            </div>
            """, unsafe_allow_html=True)

        st.divider()

        title_col, radio_col = st.columns([4, 3])

        with title_col:
            st.subheader("🎯 Primary Use Case Distribution")

        with radio_col:
            chart_type = st.radio(
                "",
                [
                    "📊 Horizontal Bar Chart",
                    "🟩 Treemap",
                    "🌹 Nightingale Chart"
                ],
                horizontal=True,
                key="use_case_chart",
                label_visibility="collapsed"
            )

        use_case_counts = (
            df["Primary_Use_Case"]
            .value_counts()
            .reset_index()
        )

        use_case_counts.columns = [
            "Primary_Use_Case",
            "Students"
        ]
        use_case_counts["Primary_Use_Case"] = (
        use_case_counts["Primary_Use_Case"]
        .str.replace("_", " ")
    )

        use_case_counts["Percentage"] = round(
            use_case_counts["Students"] /
            use_case_counts["Students"].sum() * 100,
            1
        )

        if chart_type == "📊 Horizontal Bar Chart":

            fig = px.bar(
                use_case_counts.sort_values(
                    "Students",
                    ascending=False
                ),
                x="Students",
                y="Primary_Use_Case",
                orientation="h",
                text="Students",
                color="Students"
            )

            fig.update_traces(
                textposition="outside",
                hovertemplate=
                "<b>%{y}</b><br>" +
                "Students: %{x}<extra></extra>"
            )

            fig.update_layout(
                height=550,
                yaxis_title="",
                xaxis_title="Number of Students",
                hoverlabel=dict(
                    bgcolor="black",
                    font_color="white",
                    font_size=13
                )
            )

        elif chart_type == "🟩 Treemap":

            fig = px.treemap(
                use_case_counts,
                path=["Primary_Use_Case"],
                values="Students",
                color="Students"
            )

            fig.update_traces(
                textinfo="label+value+percent root",
                hovertemplate=
                "<b>%{label}</b><br>" +
                "Students: %{value}<br>" +
                "Percentage: %{percentRoot}<extra></extra>"
            )

            fig.update_layout(
                height=550,
                margin=dict(
                    t=30,
                    b=20,
                    l=20,
                    r=20
                )
            )

        else:

            fig = px.bar_polar(
                use_case_counts,
                r="Percentage",
                theta="Primary_Use_Case",
                color="Primary_Use_Case",
                template="plotly_dark"
            )

            fig.update_traces(
                hovertemplate=
                "<b>%{theta}</b><br>" +
                "Percentage: %{r}%<extra></extra>"
            )

            fig.update_layout(
                height=550,
                margin=dict(
                    t=50,
                    b=20,
                    l=20,
                    r=20
                ),
                hoverlabel=dict(
                    bgcolor="black",
                    font_color="white",
                    font_size=13
                )
            )

        st.plotly_chart(
            fig,
            use_container_width=True,
            key="primary_use_case_chart"
        )


        st.divider()

        st.subheader("⏰ Weekly GenAI Hours Distribution")

        chart_type = st.radio(
        "Select Visualization Type",
        [
            "📊 Histogram",
            "📦 Box Plot",
            "🎻 Violin Plot"
        ],
        horizontal=True,
        key="weekly_hours_chart_radio"
    )


        if chart_type == "📊 Histogram":

            fig = px.histogram(
                df,
                x="Weekly_GenAI_Hours",
                nbins=15,
                text_auto=True,
                template="plotly_dark"
            )

            fig.update_traces(
                hovertemplate=
                "<b>Hours Range:</b> %{x}<br>" +
                "Students: %{y}<extra></extra>"
            )

            fig.update_layout(
                title="Distribution of Weekly AI Usage Hours",
                xaxis_title="Weekly GenAI Hours",
                yaxis_title="Number of Students",
                height=500,
                hoverlabel=dict(
                    bgcolor="black",
                    font_color="white",
                    font_size=13
                )
            )


        elif chart_type == "📦 Box Plot":

            fig = px.box(
            df,
            y="Weekly_GenAI_Hours",
            points="all",
            template="plotly_dark"
        )

            fig.update_traces(
            hovertemplate=
            "Weekly AI Hours: %{y}<extra></extra>"
        )

            fig.update_layout(
            title="Weekly AI Hours Spread and Outliers",
            yaxis_title="Weekly GenAI Hours",
            height=500,
            hoverlabel=dict(
                bgcolor="black",
                font_color="white",
                font_size=13
            )
        )


        else:

            fig = px.violin(
            df,
            y="Weekly_GenAI_Hours",
            box=True,
            points="all",
            template="plotly_dark"
        )

            fig.update_traces(
            hovertemplate=
            "Weekly AI Hours: %{y}<extra></extra>"
        )

            fig.update_layout(
            title="Density Distribution of Weekly AI Usage",
            yaxis_title="Weekly GenAI Hours",
            height=500,
            hoverlabel=dict(
                bgcolor="black",
                font_color="white",
                font_size=13
            )
        )


        st.plotly_chart(
            fig,
            use_container_width=True,
            key="weekly_hours_distribution_chart"
)

        st.divider()
        st.subheader("📈 Average GenAI Usage Hours Across Academic Years")
        year_usage = (
                    filtered_df.groupby(["Year_of_Study", "Primary_Use_Case"])
                    .agg(
                        Average_GenAI_Hours=("Weekly_GenAI_Hours", "mean"),
                        Number_of_Students=("Year_of_Study", "count")
                    )
                    .reset_index()
                )

        fig = px.bar(
                    year_usage,
                    x="Year_of_Study",
                    y="Average_GenAI_Hours",
                    color="Primary_Use_Case",
                    barmode="group",
                    title="Weekly GenAI Usage Comparison by Academic Year",
                    labels={
                        "Year_of_Study": "Year of Study",
                        "Average_GenAI_Hours": "Average Weekly GenAI Hours",
                        "Primary_Use_Case": "AI Use Case"
                    },
                    text_auto=".1f"
                )

        fig.update_traces(
                    hovertemplate=
                    "<b>Year of Study:</b> %{x}<br>" +
                    "<b>Primary Use Case:</b> %{fullData.name}<br>" +
                    "<b>Average Weekly GenAI Hours:</b> %{y:.2f}<br>" +
                    "<b>Number of Students:</b> %{customdata}<br>" +
                    "<extra></extra>",
                    customdata=year_usage["Number_of_Students"]
                )

        fig.update_layout(
                    hoverlabel=dict(
                        bgcolor="#1e1e1e",
                        font_size=13,
                        font_color="white"
                    ),
                    height=450,
                    xaxis_title="Year of Study",
                    yaxis_title="Average Weekly GenAI Hours",
                    legend_title="Primary Use Case"
                )

        fig.update_traces(
                    textposition="outside"
                )

        st.plotly_chart(fig, use_container_width=True)
 

        st.divider()
        st.subheader("🧩 AI Tool Diversity Levels Among Students")
        tool_diversity = (
            filtered_df["Tool_Diversity"]
            .value_counts()
            .reset_index()
        )

        tool_diversity.columns = [
            "Tool_Diversity",
            "Number_of_Students"
        ]

        tool_diversity = tool_diversity.sort_values(
            "Tool_Diversity"
        )

        fig = px.scatter(
            tool_diversity,
            x="Tool_Diversity",
            y="Number_of_Students",
            size="Number_of_Students",
            color="Tool_Diversity",
            title="Student Adoption of Multiple AI Tools",
            labels={
                "Tool_Diversity": "Number of AI Tools Used",
                "Number_of_Students": "Number of Students"
            },
            size_max=70
        )

        fig.update_traces(
            hovertemplate=
            "<b>AI Tools Used:</b> %{x}<br>" +
            "<b>Number of Students:</b> %{y}<br>" +
            "<extra></extra>"
        )

        fig.update_layout(
            height=450,
            xaxis=dict(
                dtick=1
            ),
            hoverlabel=dict(
                bgcolor="#1e1e1e",
                font_size=13,
                font_color="white"
            )
        )

        st.plotly_chart(
            fig,
            use_container_width=True
)

        st.divider()

        st.markdown("""
        <style>

        .insight-box {
            background-color:#111111;
            padding:15px;
            border-radius:10px;
            border:1px solid #3a1a2f;
            box-shadow:0 0 10px rgba(255,75,75,0.15);
            position:relative;
            transition:0.3s ease-in-out;
        }

        .insight-box:hover {
            transform:translateY(-3px);
            border:1px solid #FF4B4B;
            box-shadow:
            0 0 15px rgba(255,75,75,0.8),
            0 0 30px rgba(255,75,75,0.4);
        }

        .insight-title {
            color:white;
            font-size:18px;
            font-weight:bold;
            margin-bottom:10px;
        }

        .insight-item {
            color:#dddddd;
            font-size:13px;
            line-height:1.8;
            margin:2px 0;
        }


        .tooltip-text {
            visibility:hidden;
            width:300px;
            background-color:#222222;
            color:white;
            padding:10px;
            border-radius:8px;
            position:absolute;
            z-index:10;
            top:105%;
            left:50%;
            transform:translateX(-50%);
            font-size:12px;
            text-align:left;
            box-shadow:0 0 15px rgba(255,75,75,0.5);
        }

        .insight-box:hover .tooltip-text {
            visibility:visible;
        }

    </style>
    """, unsafe_allow_html=True)

        st.markdown("""
        <div class="insight-box">

        <div class="insight-title">
        💡 Key Insights
        </div>
        <div class="insight-item">
        🔹 <b>Popular AI Purpose:</b> Identifies the most common reason students use GenAI tools.
        </div>

        <div class="insight-item">
        🔹 <b>Usage Intensity:</b> Shows the weekly time students spend using GenAI tools.
        </div>

        <div class="insight-item">
        🔹 <b>Academic Usage Trend:</b> Compares GenAI usage patterns across different years of study.
        </div>

        <div class="insight-item">
        🔹 <b>AI Tool Adoption:</b> Represents the diversity of AI tools explored by students.
        </div>

        <div class="tooltip-text">
        • Summary of student GenAI usage behavior based on purpose, frequency, academic year, and tool diversity.
        </div>

        </div>
        """, unsafe_allow_html=True)

elif page=="Academic Performance":
        st.markdown("""
                <div style="display: flex; 
                    flex-direction: column; 
                    justify-content: flex-start;
                    line-height: 1.1; 
                    margin-top: 40px;">
                    <span style="color: #FF4B4B; 
                    font-size: 55px; 
                    font-weight: 800; 
                    letter-spacing: 4px; 
                    margin: 0; 
                    padding: 0;">
                    <span style="font-size:50px;">📚</span>
                        Academic Performance
                    </span>
                    <span style="color: gray; 
                    font-size: 15px; 
                    letter-spacing: 3px; 
                    margin-top: 5px; 
                    margin-bottom:5px;
                    padding: 0;">
                        Analyze GPA trends, academic improvements, and the impact of GenAI usage on student performance.
                </div>
                """, unsafe_allow_html=True)
     
        st.markdown("""
        <style>

        .card {
            background-color:#111111;
            border:1px solid #3a1a2f;
            border-radius:8px;
            padding:8px;
            height:110px;
            margin-top:10px;
            text-align:center;
            box-shadow:0 0 10px rgba(255,75,75,0.12);
            transition: all 0.3s ease-in-out;
        }

        .card:hover {
                        transform: translateY(-5px); 
                        box-shadow: 0 8px 20px rgba(255, 75, 75, 0.4); 
                    }

        .card-value {
            color:#FF4B4B;
            font-size:24px;
            font-weight:bold;
            margin-top:5px;
            margin-bottom:8px;
        }

        .card-label {
            color:white;
            font-size:14px;
            font-weight:600;
            letter-spacing:1px;
        }

        </style>
        """, unsafe_allow_html=True)

        avg_pre_gpa = round(
            filtered_df["Pre_Semester_GPA"].mean(),
            2
        )

        avg_post_gpa = round(
            filtered_df["Post_Semester_GPA"].mean(),
            2
        )

        gpa_improvement = round(
            avg_post_gpa - avg_pre_gpa,
            2
        )

        highest_gpa = round(
            filtered_df["Post_Semester_GPA"].max(),
            2
        )

        improved_students = round(
            (
                (filtered_df["Post_Semester_GPA"] > filtered_df["Pre_Semester_GPA"])
                .sum()
                /
                len(filtered_df)
            ) * 100,
            1
        )

        col1, col2, col3, col4, col5 = st.columns(5, gap="small")


        with col1:
            st.markdown(f"""
            <div class="card">
                <div class="card-value">{avg_pre_gpa}</div>
                <div class="card-label">📚 AVG PRE GPA</div>
            </div>
            """, unsafe_allow_html=True)


        with col2:
            st.markdown(f"""
            <div class="card">
                <div class="card-value">{avg_post_gpa}</div>
                <div class="card-label">🚀 AVG POST GPA</div>
            </div>
            """, unsafe_allow_html=True)


        with col3:
            st.markdown(f"""
            <div class="card">
                <div class="card-value">{gpa_improvement}</div>
                <div class="card-label">📈 GPA CHANGE</div>
            </div>
            """, unsafe_allow_html=True)


        with col4:
            st.markdown(f"""
            <div class="card">
                <div class="card-value">{highest_gpa}</div>
                <div class="card-label">⭐ HIGHEST GPA</div>
            </div>
            """, unsafe_allow_html=True)


        with col5:
            st.markdown(f"""
            <div class="card">
                <div class="card-value">{improved_students}%</div>
                <div class="card-label">📈 GPA IMPROVEMENT RATE</div>
            </div>
            """, unsafe_allow_html=True)

        st.divider()
        st.subheader("📈 Pre vs Post Semester GPA Comparison")

        avg_pre_gpa = round(
            filtered_df["Pre_Semester_GPA"].mean(),
            2
        )

        avg_post_gpa = round(
            filtered_df["Post_Semester_GPA"].mean(),
            2
        )

        fig = go.Figure()

        fig.add_trace(
            go.Scatter(
                x=[avg_pre_gpa, avg_post_gpa],
                y=["Average GPA", "Average GPA"],
                mode="lines",
                line=dict(width=5),
                showlegend=False,
                hoverinfo="skip"
            )
        )

        fig.add_trace(
            go.Scatter(
                x=[avg_pre_gpa],
                y=["Average GPA"],
                mode="markers+text",
                marker=dict(size=18),
                text=[f"Pre GPA: {avg_pre_gpa}"],
                textposition="top left",
                name="Pre-Semester GPA",
                hovertemplate=
                "<b>Pre-Semester GPA</b><br>" +
                f"Average GPA: {avg_pre_gpa}<extra></extra>"
            )
        )

        fig.add_trace(
            go.Scatter(
                x=[avg_post_gpa],
                y=["Average GPA"],
                mode="markers+text",
                marker=dict(size=18),
                text=[f"Post GPA: {avg_post_gpa}"],
                textposition="top right",
                name="Post-Semester GPA",
                hovertemplate=
                "<b>Post-Semester GPA</b><br>" +
                f"Average GPA: {avg_post_gpa}<extra></extra>"
            )
        )

        fig.update_layout(
            title="Average GPA Improvement Before and After GenAI Usage",
            height=400,

            xaxis=dict(
                title="Average GPA",
                range=[
                    min(avg_pre_gpa, avg_post_gpa)-1,
                    max(avg_pre_gpa, avg_post_gpa)+1
                ]
            ),

            yaxis=dict(
                title=""
            ),

            template="plotly_dark",

            hoverlabel=dict(
                bgcolor="#1e1e1e",
                font_color="white",
                font_size=13
            ),

            showlegend=True
        )


        st.plotly_chart(
            fig,
            use_container_width=True,
            key="gpa_dumbbell_chart"
        )

        st.divider()
        import plotly.graph_objects as go
        st.subheader("📊 GPA Improvement Distribution")

        gpa_improvement = (
            filtered_df["Post_Semester_GPA"] -
            filtered_df["Pre_Semester_GPA"]
        )


        counts, bins = np.histogram(
            gpa_improvement,
            bins=30
        )

        bin_centers = (
            bins[:-1] + bins[1:]
        ) / 2


        fig = go.Figure()

        fig.add_trace(
            go.Bar(
                x=bin_centers,
                y=counts,
                name="Students",
                opacity=0.7,
                hovertemplate=
                "<b>GPA Improvement:</b> %{x:.2f}<br>" +
                "<b>Students:</b> %{y}<extra></extra>"
            )
        )

        fig.add_trace(
            go.Scatter(
                x=bin_centers,
                y=counts,
                mode="lines+markers",
                name="Trend",
                line=dict(width=3),
                marker=dict(size=6),
                hovertemplate=
                "<b>GPA Improvement:</b> %{x:.2f}<br>" +
                "<b>Students:</b> %{y}<extra></extra>"
            )
        )

        fig.add_vline(
            x=0,
            line_width=3,
            line_dash="dash",
            annotation_text="No Change",
            annotation_position="top"
        )


        fig.update_layout(
            title="Distribution of GPA Improvement After GenAI Usage",

            height=500,

            xaxis_title="GPA Improvement (Post GPA - Pre GPA)",
            yaxis_title="Number of Students",

            hoverlabel=dict(
                bgcolor="#1e1e1e",
                font_color="white",
                font_size=13
            ),

            legend_title="Analysis"
        )


        st.plotly_chart(
            fig,
            use_container_width=True,
            key="gpa_improvement_hist_line"
        )

        st.divider()

        st.subheader("🔥 Average GPA by Academic Year & AI Usage Level")

        filtered_df["AI_Usage_Level"] = pd.cut(
            filtered_df["Weekly_GenAI_Hours"],
            bins=[-1, 5, 15, float("inf")],
            labels=[
                "Low Usage",
                "Medium Usage",
                "High Usage"
            ]
        )

        gpa_year_usage = (
            filtered_df.groupby(
                ["Year_of_Study", "AI_Usage_Level"],
                observed=True
            )
            .agg(
                Average_Post_GPA=(
                    "Post_Semester_GPA",
                    "mean"
                )
            )
            .reset_index()
        )


        gpa_year_usage["Average_Post_GPA"] = round(
            gpa_year_usage["Average_Post_GPA"],
            2
        )

        fig = px.density_heatmap(
            gpa_year_usage,
            x="AI_Usage_Level",
            y="Year_of_Study",
            z="Average_Post_GPA",
            text_auto=".2f",
            title="Average Post-Semester GPA Across Academic Years and AI Usage Levels",
            labels={
                "AI_Usage_Level": "GenAI Usage Level",
                "Year_of_Study": "Academic Year",
                "Average_Post_GPA": "Average Post GPA"
            }
        )


        fig.update_traces(
            hovertemplate=
            "<b>Year:</b> %{y}<br>" +
            "<b>AI Usage:</b> %{x}<br>" +
            "<b>Average GPA:</b> %{z:.2f}<extra></extra>"
        )


        fig.update_layout(
            height=450,
            xaxis_title="GenAI Usage Level",
            yaxis_title="Year of Study",
            hoverlabel=dict(
                bgcolor="#1e1e1e",
                font_color="white",
                font_size=13
            )
        )


        st.plotly_chart(
            fig,
            use_container_width=True,
            key="gpa_year_usage_heatmap"
        )

        st.divider()

        st.markdown("""
        <style>

        .summary-box {
            background-color:#111111;
            padding:18px;
            border-radius:12px;
            border:1px solid #3a1a2f;
            box-shadow:0 0 10px rgba(255,75,75,0.15);
            transition:0.3s ease-in-out;
            position:relative;
        }

        .summary-box:hover {
            transform:translateY(-4px);
            border:1px solid #FF4B4B;
            box-shadow:
            0 0 15px rgba(255,75,75,0.8),
            0 0 30px rgba(255,75,75,0.4);
        }


        .summary-title {
            color:#FF4B4B;
            font-size:20px;
            font-weight:700;
            margin-bottom:12px;
        }


        .summary-item {
            color:#dddddd;
            font-size:14px;
            line-height:1.8;
        }


        .tooltip-box {
            visibility:hidden;
            width:320px;
            background:#222222;
            color:white;
            padding:12px;
            border-radius:8px;
            position:absolute;
            top:100%;
            left:50%;
            transform:translateX(-50%);
            z-index:10;
            font-size:12px;
            box-shadow:0 0 15px rgba(255,75,75,0.5);
        }


        .summary-box:hover .tooltip-box {
            visibility:visible;
        }

        </style>
        """, unsafe_allow_html=True)


        st.markdown("""
        <div class="summary-box">

        <div class="summary-title">
        💡 Academic Performance Insights
        </div>


        <div class="summary-item">
        🔹 Pre and Post GPA comparison highlights the overall academic change after GenAI adoption.
        </div>


        <div class="summary-item">
        🔹 GPA distribution analysis shows how performance varies among different AI usage levels.
        </div>


        <div class="summary-item">
        🔹 Improvement distribution identifies students who improved, maintained, or decreased their GPA.
        </div>


        <div class="summary-item">
        🔹 Year-wise analysis reveals performance patterns across different academic groups.
        </div>


        <div class="tooltip-box">
        • Summary of academic impact based on GPA comparison, AI usage intensity, improvement trends, and year-wise performance analysis.
        </div>


        </div>
        """, unsafe_allow_html=True)



elif page=="Learning Behavior":
        st.markdown("""
                <div style="display: flex; 
                    flex-direction: column; 
                    justify-content: flex-start;
                    line-height: 1.1; 
                    margin-top: 40px;">
                    <span style="color: #FF4B4B; 
                    font-size: 55px; 
                    font-weight: 800; 
                    letter-spacing: 4px; 
                    margin: 0; 
                    padding: 0;">
                    <span style="font-size:50px;"> 📖 </span>
                         Learning Behavior
                    </span>
                    <span style="color: gray; 
                    font-size: 15px; 
                    letter-spacing: 3px; 
                    margin-top: 5px; 
                    margin-bottom:5px;
                    padding: 0;">
                    Explore how students interact with GenAI tools, learning patterns,study habits, prompt skills, and AI-assisted learning approaches.
                """, unsafe_allow_html=True)
        st.markdown("""
            <style>

            .card {
                background-color:#111111;
                border:1px solid #3a1a2f;
                border-radius:8px;
                padding:8px;
                height:110px;
                margin-top:10px;
                text-align:center;
                box-shadow:0 0 10px rgba(255,75,75,0.12);
                transition: all 0.3s ease-in-out;
            }

            .card:hover {
                            transform: translateY(-5px); 
                            box-shadow: 0 8px 20px rgba(255, 75, 75, 0.4); 
                        }

            .card-value {
                color:#FF4B4B;
                font-size:24px;
                font-weight:bold;
                margin-top:5px;
                margin-bottom:8px;
            }

            .card-label {
                color:white;
                font-size:14px;
                font-weight:600;
                letter-spacing:1px;
            }

            </style>
            """, unsafe_allow_html=True)
        top_prompt_skill = (
            filtered_df["Prompt_Engineering_Skill"]
            .value_counts()
            .idxmax()
)


        avg_tool_diversity = round(
            filtered_df["Tool_Diversity"].mean(),
            1
        )

        top_learning_activity = (
            filtered_df["Primary_Use_Case"]
            .value_counts()
            .idxmax()
        )
        activity_map = {
    "Debugging & Troubleshooting": "Debugging",
    "Research & Information Gathering": "Research",
    "Content Creation": "Writing",
    "Coding Assistance": "Coding",
    "Learning & Study": "Learning",
    "Problem Solving": "Problem Solving"
}


        activity_lower = top_learning_activity.lower()

        if "debug" in activity_lower:
            top_learning_activity = "Debugging"

        elif "research" in activity_lower:
            top_learning_activity = "Research"

        elif "coding" in activity_lower:
            top_learning_activity = "Coding"

        elif "content" in activity_lower:
            top_learning_activity = "Writing"

        elif "learn" in activity_lower:
            top_learning_activity = "Learning"

        elif "problem" in activity_lower:
            top_learning_activity = "Problem Solving"

        else:
            top_learning_activity = top_learning_activity[:12]
            top_learning_activity = activity_map.get(
                    top_learning_activity,
                    top_learning_activity.replace("_"," ")
                )


        if len(top_learning_activity) > 12:
            top_learning_activity = (
                top_learning_activity[:12] + "..."
            )


        avg_ai_hours = round(
            filtered_df["Weekly_GenAI_Hours"].mean(),
            1
        )

        active_ai_learners = round(
            (
                filtered_df["Weekly_GenAI_Hours"] > 0
            ).mean() * 100,
            1
        )

        col1, col2, col3, col4, col5 = st.columns(
            5,
            gap="small"
        )


        with col1:
            st.markdown(f"""
            <div class="card">
                <div class="card-value">
                    {top_prompt_skill}
                </div>
                <div class="card-label">
                    🧠 PROMPT SKILL LEVEL
                </div>
            </div>
            """,
            unsafe_allow_html=True)


        with col2:
            st.markdown(f"""
            <div class="card">
                <div class="card-value">
                    {avg_tool_diversity}
                </div>
                <div class="card-label">
                    🔄 AI TOOLS USED
                </div>
            </div>
            """,
            unsafe_allow_html=True)


        with col3:
            st.markdown(f"""
            <div class="card">
                <div class="card-value">
                    {top_learning_activity}
                </div>
                <div class="card-label">
                    📚 TOP ACTIVITY
                </div>
            </div>
            """, unsafe_allow_html=True)


        with col4:
            st.markdown(f"""
            <div class="card">
                <div class="card-value">
                    {avg_ai_hours}
                </div>
                <div class="card-label">
                    ⏱️ AVG AI HOURS
                </div>
            </div>
            """,
            unsafe_allow_html=True)


        with col5:
            st.markdown(f"""
            <div class="card">
                <div class="card-value">
                    {active_ai_learners}%
                </div>
                <div class="card-label">
                    🎯 ACTIVE AI LEARNERS
                </div>
            </div>
            """,
            unsafe_allow_html=True)

        st.divider()

        st.subheader("🕸️ Learning Purpose Distribution")


        purpose_counts = (
                filtered_df["Primary_Use_Case"]
                .value_counts()
                .reset_index()
            )

        purpose_counts.columns = [
                "Learning_Purpose",
                "Students"
            ]

        purpose_counts["Learning_Purpose"] = (
                purpose_counts["Learning_Purpose"]
                .str.replace("_", " ")
            )
        purpose_counts["Learning_Purpose"] = (
        purpose_counts["Learning_Purpose"]
        .replace({
            "Debugging/Troubleshooting": "Debugging",
            "Copywriting/Drafting": "Writing",
            "Direct Answer Generation": "Answer Generation",
            "Summarizing Reading": "Summarizing"
        })
)

        fig = px.line_polar(
                purpose_counts,
                r="Students",
                theta="Learning_Purpose",
                line_close=True,
                template="plotly_dark"
            )

        fig.update_traces(
                fill="toself",
                hovertemplate=
                "<b>%{theta}</b><br>" +
                "Students: %{r}<extra></extra>"
            )

        fig.update_layout(
                height=550,
                hoverlabel=dict(
                    bgcolor="#1e1e1e",
                    font_color="white",
                    font_size=13
                ),
                polar=dict(
                    radialaxis=dict(
                        visible=True
                    )
                )
            )

        st.plotly_chart(
                fig,
                use_container_width=True,
                key="learning_purpose_radar"
            )
        
        st.divider()

        st.subheader("🧠 Prompt Engineering Skill Distribution")

        skill_counts = (
            df["Prompt_Engineering_Skill"]
            .value_counts()
            .reset_index()
        )

        skill_counts.columns = [
            "Skill_Level",
            "Students"
        ]

        skill_order = [
            "Beginner",
            "Intermediate",
            "Advanced"
        ]

        skill_counts["Skill_Level"] = pd.Categorical(
            skill_counts["Skill_Level"],
            categories=skill_order,
            ordered=True
        )

        skill_counts = skill_counts.sort_values("Skill_Level")

        fig = px.pie(
            skill_counts,
            names="Skill_Level",
            values="Students",
            hole=0.55,
            template="plotly_dark"
        )

        fig.update_traces(
            textposition="inside",
            textinfo="percent+label",
            hovertemplate=
            "<b>%{label}</b><br>" +
            "Students: %{value}<br>" +
            "Percentage: %{percent}<extra></extra>"
        )

        fig.update_layout(
            height=550,
            showlegend=True,
            legend_title="Skill Level",
            hoverlabel=dict(
                bgcolor="#1e1e1e",
                font_color="white",
                font_size=13
            ),
            annotations=[
                dict(
                    text="Prompt<br>Skills",
                    x=0.5,
                    y=0.5,
                    showarrow=False,
                    font_size=18
                )
            ]
        )

        st.plotly_chart(
            fig,
            use_container_width=True,
            key="prompt_skill_distribution"
        )

        st.divider()

        st.subheader("📦 Skill Retention Score Distribution")

        fig = px.box(
            df,
            y="Skill_Retention_Score",
            template="plotly_dark",
            points=False
        )

        fig.update_traces(
            hovertemplate=
            "Skill Retention Score: %{y}<extra></extra>"
        )

        fig.update_layout(
            height=500,
            yaxis_title="Skill Retention Score",
            hoverlabel=dict(
                bgcolor="#1e1e1e",
                font_color="white",
                font_size=13
            )
        )

        st.plotly_chart(
            fig,
            use_container_width=True,
            key="skill_retention_distribution"
        )

        st.divider()
        st.subheader("📈 AI Usage Hours by Prompt Skill Level")

        skill_hours = (
            df.groupby("Prompt_Engineering_Skill")["Weekly_GenAI_Hours"]
            .mean()
            .reset_index()
        )

        skill_order = [
            "Beginner",
            "Intermediate",
            "Advanced"
        ]

        skill_hours["Prompt_Engineering_Skill"] = pd.Categorical(
            skill_hours["Prompt_Engineering_Skill"],
            categories=skill_order,
            ordered=True
        )

        skill_hours = skill_hours.sort_values(
            "Prompt_Engineering_Skill"
        )

        fig = px.line(
            skill_hours,
            x="Prompt_Engineering_Skill",
            y="Weekly_GenAI_Hours",
            markers=True,
            template="plotly_dark"
        )

        fig.update_traces(
            mode="lines+markers+text",
            text=round(skill_hours["Weekly_GenAI_Hours"], 1),
            textposition="top center",
            marker=dict(size=14),
            line=dict(width=4),
            hovertemplate=
            "<b>%{x}</b><br>" +
            "Average AI Hours: %{y:.1f}<extra></extra>"
        )

        fig.update_layout(
            height=500,
            xaxis_title="Prompt Engineering Skill Level",
            yaxis_title="Average Weekly GenAI Hours",
            hoverlabel=dict(
                bgcolor="#1e1e1e",
                font_color="white",
                font_size=13
            )
        )
        fig.update_yaxes(range=[0, 10])

        st.plotly_chart(
            fig,
            use_container_width=True,
            key="prompt_skill_ai_hours_line"
        )

        st.divider()

        st.markdown("""
        <div style="
            background-color:#111111;
            border:1px solid #3a1a2f;
            border-left:5px solid #FF4B4B;
            border-radius:10px;
            padding:20px;
            margin-top:10px;
            box-shadow:0 0 10px rgba(255,75,75,0.12);
        ">

        <h4 style="margin-top:0; margin-bottom:12px; color:white;">
        💡 Learning Behavior Insights
        </h4>

        • Students primarily use GenAI for <b>Debugging</b> and <b>Writing</b> tasks.<br>

        • Most students belong to the <b>Intermediate Prompt Engineering Skill</b> category.<br>

        • Skill retention remains relatively strong despite regular AI usage.<br>

        • Advanced users spend slightly more time using AI tools than beginners.<br>

        • Prompt skill level shows a positive relationship with AI usage hours.

        </div>
        """, unsafe_allow_html=True)

elif page=="Student Well-Being":
        st.markdown("""
        <div style="display: flex; 
            flex-direction: column; 
            justify-content: flex-start;
            line-height: 1.1; 
            margin-top: 40px;">
            <span style="
                color: #FF6B6B; 
                font-size: 55px; 
                font-weight: 800; 
                letter-spacing: 4px; 
                margin: 0; 
                padding: 0;">
                <span style="font-size:50px;"> 🙁 </span>
                Student Well-Being
            </span>
           <span style="
            color: gray; 
            font-size: 15px; 
            letter-spacing: 3px; 
            margin-top: 5px; 
            margin-bottom:5px;
            padding: 0;">
            Anxiety, Burnout & AI Dependency Analysis
        </span>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("""
        <style>

        .card {
            background-color:#111111;
            border:1px solid #3a1a2f;
            border-radius:8px;
            padding:8px;
            height:110px;
            margin-top:10px;
            text-align:center;
            box-shadow:0 0 10px rgba(255,75,75,0.12);
            transition: all 0.3s ease-in-out;
        }

        .card:hover {
            transform: translateY(-5px);
            box-shadow:0 8px 20px rgba(255,75,75,0.4);
        }

        .card-value {
            color:#FF4B4B;
            font-size:24px;
            font-weight:bold;
            margin-top:5px;
            margin-bottom:8px;
        }

        .card-label {
            color:white;
            font-size:14px;
            font-weight:600;
            letter-spacing:1px;
        }

        </style>
        """, unsafe_allow_html=True)
        high_anxiety = round(
            (
                filtered_df["Anxiety_Level_During_Exams"]
                .astype(str)
                .str.contains("High", case=False, na=False)
                .mean()
            ) * 100,
            1
        )
        high_burnout = round(
            (filtered_df["Burnout_Risk_Level"]=="High").mean()*100,
            1
        )

        avg_dependency = round(
            filtered_df["Perceived_AI_Dependency"].mean(),
            2
        )

        avg_skill = round(
            filtered_df["Skill_Retention_Score"].mean(),
            2
        )


        col1, col2, col3, col4 = st.columns(4)


        with col1:
            st.markdown(f"""
            <div class="card">
                <div class="card-value">😰 {high_anxiety}%</div>
                <div class="card-label">HIGH ANXIETY STUDENTS</div>
            </div>
            """, unsafe_allow_html=True)


        with col2:
            st.markdown(f"""
            <div class="card">
                <div class="card-value">🔥 {high_burnout}%</div>
                <div class="card-label">HIGH BURNOUT RISK</div>
            </div>
            """, unsafe_allow_html=True)


        with col3:
            st.markdown(f"""
            <div class="card">
                <div class="card-value">🤖 {avg_dependency}</div>
                <div class="card-label">AI DEPENDENCY SCORE</div>
            </div>
            """, unsafe_allow_html=True)


        with col4:
            st.markdown(f"""
            <div class="card">
                <div class="card-value">🧠 {avg_skill}</div>
                <div class="card-label">SKILL RETENTION SCORE</div>
            </div>
            """, unsafe_allow_html=True)

        st.divider()
        col1, col2 = st.columns(2)


        with col1:

            st.subheader("😰 Anxiety Level Distribution")

            anxiety_count = (
                filtered_df["Anxiety_Level_During_Exams"]
                .value_counts()
                .reset_index()
            )

            anxiety_count.columns = ["Anxiety Level", "Students"]


            fig1 = px.pie(
                anxiety_count,
                names="Anxiety Level",
                values="Students",
                hole=0.55,
                color="Anxiety Level",
                color_discrete_map={
                    "Low Anxiety": "#21BA61",
                    "Medium Anxiety": "#C3882A",
                    "High Anxiety": "#D53030"
                }
            )


            fig1.update_traces(
                textinfo="percent+label",
                textfont_size=13,
                hovertemplate=
                "<b>%{label}</b><br>" +
                "Students: %{value}<br>" +
                "Percentage: %{percent}<extra></extra>"
            )


            fig1.update_layout(
                template="plotly_dark",
                height=400,
                showlegend=False
            )


            st.plotly_chart(
                fig1,
                use_container_width=True
            )


        with col2:

            st.subheader("🔥 Burnout Risk Distribution")


            burnout_count = (
                filtered_df["Burnout_Risk_Level"]
                .value_counts()
                .reset_index()
            )

            burnout_count.columns = ["Burnout Risk", "Students"]


            fig2 = px.bar(
                burnout_count,
                x="Burnout Risk",
                y="Students",
                text="Students",
                color="Burnout Risk",
                color_discrete_map={
                    "Low": "#21BA61",
                    "Medium": "#C3882A",
                    "High": "#D53030"
                }
            )


            fig2.update_traces(
                textposition="outside",
                hovertemplate=
                "<b>%{x}</b><br>" +
                "Students: %{y}<extra></extra>"
            )


            fig2.update_layout(
                template="plotly_dark",
                height=400,
                showlegend=False,
                xaxis_title="Burnout Risk Level",
                yaxis_title="Number of Students"
            )


            st.plotly_chart(
                fig2,
                use_container_width=True
            )

        st.divider()
        st.subheader("📊 Average AI Usage Hours by Anxiety Level")


        ai_anxiety = (
            filtered_df
            .groupby("Anxiety_Level_During_Exams")["Weekly_GenAI_Hours"]
            .mean()
            .reset_index()
        )

        ai_anxiety.columns = ["Anxiety Level", "Average AI Hours"]


        fig = px.bar(
            ai_anxiety,
            x="Anxiety Level",
            y="Average AI Hours",
            text="Average AI Hours",
            color="Anxiety Level",
            color_discrete_map={
                "Low Anxiety": "#2ECC71",
                "Medium Anxiety": "#F39C12",
                "High Anxiety": "#FF4B4B"
            }
        )


        fig.update_traces(
            texttemplate="%{text:.1f}",
            textposition="outside",
            hovertemplate=
            "<b>%{x}</b><br>" +
            "Average AI Hours: %{y:.2f}<extra></extra>"
        )


        fig.update_layout(
            template="plotly_dark",
            height=420,
            showlegend=False,
            xaxis_title="Anxiety Level",
            yaxis_title="Average Weekly GenAI Hours"
        )


        st.plotly_chart(fig, use_container_width=True)
        st.divider()
        st.subheader("🧠 Skill Retention Score Distribution")


        fig = px.histogram(
            filtered_df,
            x="Skill_Retention_Score",
            nbins=15,
            text_auto=True,
            color_discrete_sequence=["#9B59B6"] 
        )


        fig.update_traces(
            marker_line_color="#FFFFFF",
            marker_line_width=1,
            hovertemplate=
            "<b>Skill Retention Score:</b> %{x}<br>" +
            "<b>Students:</b> %{y}<extra></extra>"
        )


        fig.update_layout(
            template="plotly_dark",
            height=420,
            xaxis_title="Skill Retention Score",
            yaxis_title="Number of Students",
            bargap=0.15
        )


        st.plotly_chart(
            fig,
            use_container_width=True
        )


        st.divider()
        st.subheader("📈 Anxiety Level Across Year of Study")


        anxiety_year = (
            filtered_df
            .groupby(
                ["Year_of_Study", "Anxiety_Level_During_Exams"]
            )
            .size()
            .reset_index(name="Students")
        )


        fig = px.bar(
            anxiety_year,
            x="Year_of_Study",
            y="Students",
            color="Anxiety_Level_During_Exams",
            barmode="stack",
            color_discrete_map={
                "Low Anxiety": "#2ECC71",
                "Medium Anxiety": "#F39C12",
                "High Anxiety": "#FF4B4B"
            }
        )


        fig.update_layout(
            template="plotly_dark",
            height=450,
            xaxis_title="Year of Study",
            yaxis_title="Number of Students"
        )


        st.plotly_chart(
            fig,
            use_container_width=True
        )

        st.divider()
       
        st.subheader("📌 Key Findings")

        st.markdown("""
        <div style="
            background-color:#111111;
            border:1px solid #3a1a2f;
            border-left:5px solid #FF4B4B;
            border-radius:10px;
            padding:20px;
            margin-top:10px;
            box-shadow:0 0 10px rgba(255,75,75,0.12);
        ">

        <p style="font-size:16px; margin-bottom:12px;">
        🔹 Most students experience <b>moderate anxiety</b> during exams.
        </p>

        <p style="font-size:16px; margin-bottom:12px;">
        🔹 Burnout risk varies among students, showing different stress patterns.
        </p>

        <p style="font-size:16px; margin-bottom:12px;">
        🔹 Higher AI usage can influence students' learning behaviour and dependency.
        </p>

        <p style="font-size:16px; margin-bottom:12px;">
        🔹 Skill retention score helps evaluate the impact of AI on student learning.
        </p>

        <p style="font-size:16px; margin-bottom:0;">
        🔹 Student well-being is affected by AI usage patterns and academic workload.
        </p>

        </div>
        """, unsafe_allow_html=True)


elif page=="Correlation Analysis":
        st.markdown("""
        <div style="display: flex; 
            flex-direction: column; 
            justify-content: flex-start;
            line-height: 1.1; 
            margin-top: 40px;">
            <span style="
                color: #FF6B6B; 
                font-size: 55px; 
                font-weight: 800; 
                letter-spacing: 4px; 
                margin: 0; 
                padding: 0;">
                <span style="font-size:50px;"> 🧩  </span>
                Correlation Analysis
            </span>
           <span style="
            color: gray; 
            font-size: 15px; 
            letter-spacing: 3px; 
            margin-top: 5px; 
            margin-bottom:5px;
            padding: 0;">
             Exploring Relationships Between Student Metrics
        </span>
        </div>
        """, unsafe_allow_html=True)


        st.markdown("""
        <div style="
            background: linear-gradient(90deg,#111111,#1a1a1a);
            border:1px solid #3a1a2f;
            border-radius:10px;
            padding:18px;
            text-align:center;
            margin-bottom:20px;
            margin-top:35px;
        ">

        <h3 style="color:#FF6B6B;">
        🔍 Discovering hidden relationships in student data
        </h3>

        <p style="color:gray;">
        Understanding how AI usage influences academic performance,
        learning behaviour, anxiety, and overall well-being.
        </p>

        </div>
        """, unsafe_allow_html=True)

        st.divider()
        st.subheader("🔥 Correlation Heatmap")

        corr_df = filtered_df.copy()

        if "Prompt_Engineering_Skill" in corr_df.columns:
            corr_df["Prompt_Engineering_Skill_Num"] = corr_df[
                "Prompt_Engineering_Skill"
            ].map({
                "Beginner": 1,
                "Intermediate": 2,
                "Advanced": 3
            })

        if "Burnout_Risk_Level" in corr_df.columns:
            corr_df["Burnout_Risk_Num"] = corr_df[
                "Burnout_Risk_Level"
            ].map({
                "Low": 1,
                "Moderate": 2,
                "High": 3
            })

        corr_columns = [
            "Weekly_GenAI_Hours",
            "Pre_Semester_GPA",
            "Post_Semester_GPA",
            "Skill_Retention_Score",
            "Tool_Diversity",
            "Perceived_AI_Dependency",
            "Prompt_Engineering_Skill_Num",
            "Anxiety_Level_During_Exams",
            "Burnout_Risk_Num"
        ]

        corr_columns = [col for col in corr_columns if col in corr_df.columns]

        corr_matrix = corr_df[corr_columns].corr(numeric_only=True)

        fig = px.imshow(
            corr_matrix,
            text_auto=".2f",
            color_continuous_scale="RdBu_r",
            aspect="auto",
            title="Correlation Matrix"
        )

        fig.update_layout(
            height=650,
            title_x=0.5,
            paper_bgcolor="#0E1117",
            plot_bgcolor="#0E1117",
            font=dict(color="white"),
            coloraxis_colorbar=dict(title="Correlation")
        )

        fig.update_xaxes(tickangle=45)
        fig.update_layout(
        font=dict(
            color="white",
            size=14
    )
)

        fig.update_xaxes(
                tickfont=dict(size=12),
                tickangle=45
            )

        fig.update_yaxes(
                tickfont=dict(size=12)
)

        st.plotly_chart(fig, use_container_width=True)

        st.divider()
        col1, col2 = st.columns(2)
        col1, spacer, col2 = st.columns([1, 0.12, 1])
        with col1:
            st.subheader("📈 AI Usage vs GPA")

            filtered_df["AI_Usage_Group"] = pd.cut(
                filtered_df["Weekly_GenAI_Hours"],
                bins=[0, 5, 10, 15, 20, filtered_df["Weekly_GenAI_Hours"].max()],
                labels=["0-5 hrs", "6-10 hrs", "11-15 hrs", "16-20 hrs", "20+ hrs"],
                include_lowest=True
            )

            ai_gpa = (
                filtered_df.groupby("AI_Usage_Group")["Post_Semester_GPA"]
                .mean()
                .reset_index()
            )

            fig = px.line(
                ai_gpa,
                x="AI_Usage_Group",
                y="Post_Semester_GPA",
                markers=True
            )

            fig.update_layout(
                paper_bgcolor="#0E1117",
                plot_bgcolor="#0E1117",
                font=dict(color="white"),
                height=400
            )

            st.plotly_chart(fig, use_container_width=True)


        with col2:
            st.subheader("🛠 Prompt Skill vs GPA")

            prompt_gpa = (
                filtered_df.groupby("Prompt_Engineering_Skill")["Post_Semester_GPA"]
                .mean()
                .reset_index()
            )

            fig = px.bar(
                prompt_gpa,
                x="Prompt_Engineering_Skill",
                y="Post_Semester_GPA",
                color="Prompt_Engineering_Skill"
            )

            fig.update_layout(
                paper_bgcolor="#0E1117",
                plot_bgcolor="#0E1117",
                font=dict(color="white"),
                height=400,
                showlegend=False
            )

            st.plotly_chart(fig, use_container_width=True)


        st.divider()

        col3, col4 = st.columns(2)
        col3, spacer, col4 = st.columns([1, 0.12, 1])
        with col3:
            st.subheader("😰 Anxiety vs Burnout")

            anxiety_burnout = (
                    filtered_df.groupby("Burnout_Risk_Level")[
                        "Anxiety_Level_During_Exams"
                    ]
                    .mean()
                    .reset_index()
                )

            fig = px.bar(
                    anxiety_burnout,
                    x="Burnout_Risk_Level",
                    y="Anxiety_Level_During_Exams",
                    color="Burnout_Risk_Level",
                    labels={
                        "Anxiety_Level_During_Exams": "Average Anxiety Score"
                    }
                )

            fig.update_layout(
                    paper_bgcolor="#0E1117",
                    plot_bgcolor="#0E1117",
                    font=dict(color="white"),
                    height=400,
                    showlegend=False,
                    xaxis_title="Burnout Risk Level",
                    yaxis_title="Average Anxiety Score"
                )

            st.plotly_chart(
                    fig,
                    use_container_width=True,
                    key="anxiety_burnout"
                )

        with col4:
            st.subheader("🤖 AI Dependency vs Skill Retention")

            dependency_data = (
                    filtered_df.groupby("Perceived_AI_Dependency")["Skill_Retention_Score"]
                    .mean()
                    .reset_index()
                )

            fig = px.bar(
                    dependency_data,
                    x="Perceived_AI_Dependency",
                    y="Skill_Retention_Score",
                    color="Perceived_AI_Dependency",
                    color_continuous_scale="Blues"
                )

            fig.update_layout(
                    paper_bgcolor="#0E1117",
                    plot_bgcolor="#0E1117",
                    font=dict(color="white"),
                    height=400,
                    showlegend=False
                )

            st.plotly_chart(fig, use_container_width=True)
            

        st.divider()

        corr_matrix = filtered_df.select_dtypes(include="number").corr()


        corr_pairs = corr_matrix.unstack().reset_index()
        corr_pairs.columns = ["Feature 1", "Feature 2", "Correlation"]


        corr_pairs = corr_pairs[
            corr_pairs["Feature 1"] != corr_pairs["Feature 2"]
        ]

        corr_pairs["Pair"] = corr_pairs.apply(
            lambda x: tuple(sorted([x["Feature 1"], x["Feature 2"]])),
            axis=1
        )

        corr_pairs = corr_pairs.drop_duplicates(subset="Pair")

        positive_corr = corr_pairs.sort_values(
            by="Correlation",
            ascending=False
        ).head(5)

        negative_corr = corr_pairs.sort_values(
            by="Correlation",
            ascending=True
        ).head(5)

        def format_name(col):
            return col.replace("_", " ")

        st.subheader("🧠 Strongest Positive Relationships")

        for _, row in positive_corr.iterrows():
            st.markdown(
                f"""
                • **{format_name(row['Feature 1'])}**
                ↔
                **{format_name(row['Feature 2'])}**
                <span style='color:#FF6B6B; font-weight:bold;'>
                ({row['Correlation']:.2f})
                </span>
                """,
                unsafe_allow_html=True
            )

        st.markdown("<br>", unsafe_allow_html=True)

        st.subheader("📉 Strongest Negative Relationships")

        for _, row in negative_corr.iterrows():
            st.markdown(
                f"""
                • **{format_name(row['Feature 1'])}**
                ↔
                **{format_name(row['Feature 2'])}**
                <span style='color:#FF6B6B; font-weight:bold;'>
                ({row['Correlation']:.2f})
                </span>
                """,
                unsafe_allow_html=True
            )

        st.divider()

        st.caption(
            "Correlation indicates association between variables and does not establish causation."
        )
elif page=="Insights":

        st.markdown("""
            <div style="display: flex; 
                flex-direction: column; 
                justify-content: flex-start;
                line-height: 1.1; 
                margin-top: 40px;">
                <span style="
                    color: #FF6B6B; 
                    font-size: 55px; 
                    font-weight: 800; 
                    letter-spacing: 4px; 
                    margin: 0; 
                    padding: 0;">
                    <span style="font-size:50px;">💡</span>
                    Insights
                </span>
                <span style="
                    color: gray; 
                    font-size: 15px; 
                    letter-spacing: 3px; 
                    margin-top: 5px; 
                    margin-bottom:5px;
                    padding: 0;">
                    Key Findings and Conclusions from the Analysis
                </span>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

        st.subheader("🔍 Major Findings")

        st.markdown("""
            <div style='font-size:18px; font-weight:600; line-height:1.0'>

            🔹 AI usage has become a regular part of student learning.<br><br>

            🔹 Moderate AI usage is associated with improved academic performance.<br><br>

            🔹 Students using AI for learning support achieved better outcomes.<br><br>

            🔹 Higher AI usage is linked with greater AI dependency.<br><br>

            🔹 Excessive AI dependency may reduce skill retention.<br><br>

            🔹 Strong prompt engineering skills improve AI effectiveness.<br><br>

            🔹 Burnout risk and exam anxiety influence student well-being.<br><br>

            🔹 Using multiple AI tools enhances learning experiences.

            </div>
            """, unsafe_allow_html=True)

        st.divider()

        st.subheader("🎯 Recommendations")

        st.markdown("""
            - Encourage responsible and balanced AI usage.
            - Use AI as a learning assistant rather than a replacement for independent thinking.
            - Improve awareness of prompt engineering techniques.
            - Monitor excessive dependency on AI tools.
            - Combine AI-assisted learning with traditional study methods.
            """)

        st.divider()

        st.subheader("🏁 Final Conclusion")

        st.markdown("""
            The analysis demonstrates that Generative AI can positively influence
            learning outcomes and academic performance when used appropriately.

            However, excessive dependence on AI tools may affect skill retention,
            increase dependency, and influence student well-being.

            Therefore, a balanced and responsible approach to AI adoption is essential
            for maximizing benefits while minimizing potential risks.
            """)



elif page=="Export Report":

        st.markdown("""
        <div style="display: flex; 
            flex-direction: column; 
            justify-content: flex-start;
            line-height: 1.1; 
            margin-top: 40px;">
            <span style="
                color: #FF6B6B; 
                font-size: 55px; 
                font-weight: 800; 
                letter-spacing: 4px; 
                margin: 0; 
                padding: 0;">
                <span style="font-size:50px;">📤</span>
                Export Report
            </span>
            <span style="
                color: gray; 
                font-size: 15px; 
                letter-spacing: 3px; 
                margin-top: 5px; 
                margin-bottom:5px;
                padding: 0;">
                Download Analysis Results and Dashboard Summary
            </span>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

        st.subheader("📋 Project Summary")

        st.write("• Dataset analyzed successfully.")
        st.write("• Missing values and duplicates were handled.")
        st.write("• Student demographics and AI usage patterns were explored.")
        st.write("• Academic performance and learning behavior were analyzed.")
        st.write("• Well-being indicators such as anxiety and burnout were studied.")
        st.write("• Correlation analysis identified important relationships.")
        st.write("• Key findings and recommendations were generated.")

        st.divider()

        st.subheader("📥 Download Dataset")

        csv = filtered_df.to_csv(index=False).encode("utf-8")

        st.download_button(
            label="⬇️ Download Filtered Dataset",
            data=csv,
            file_name="AI_Student_Analysis_Report.csv",
            mime="text/csv"
        )

        st.divider()

        st.success(
            "Dashboard analysis completed successfully. Thank you for exploring the AI Impact on Students project."
        )