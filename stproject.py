import streamlit as st
import pandas as pd

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
    <style>
    .sidebar-header{
        text-align:center;
        margin-top:-40px;
    }

    .logo{
        font-size:48px;
        margin-bottom:-20px;
    }

    .edu{
        color:white;
        font-size:40px;
        font-weight:bold;
        margin-bottom:-15px;
    }

    .analytics{
        color:#9D7DFF;
        font-size:13px;
        letter-spacing:3px;
        margin-top:0px;
    }
    </style>

    <div class="sidebar-header">
        <div class="logo">🎓</div>
        <div class="edu">EDU AI</div>
        <div class="analytics">STUDENT ANALYTICS</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    st.markdown("## 📊 ANALYSIS HUB")

    page = st.radio(
        "",
        [
            "🏠 Overview",
            "📂 Upload & Preview",
            "🧹 Data Cleaning",
            "👨‍🎓 Student Demographics",
            "🤖 AI Usage Analytics",
            "📈 Academic Performance",
            "🧠 Learning Behavior",
            "😰 Student Well-being",
            "🔥 Correlation Analysis",
            "💡 Insights",
            "📥 Export Report"
        ]
    )

    st.markdown("---")

    st.markdown("## ⚙️ FILTERS")

    major_filter = st.multiselect(
        "🎓 Major Category",
        sorted(df["Major_Category"].unique())
    )

    year_filter = st.multiselect(
        "📚 Year of Study",
        sorted(df["Year_of_Study"].unique())
    )

    use_case_filter = st.multiselect(
        "🤖 Primary Use Case",
        sorted(df["Primary_Use_Case"].unique())
    )

    subscription_filter = st.multiselect(
        "💳 Paid Subscription",
        sorted(df["Paid_Subscription"].unique())
    )

    weekly_hours_filter = st.slider(
        "⏰ Weekly GenAI Hours",
        int(df["Weekly_GenAI_Hours"].min()),
        int(df["Weekly_GenAI_Hours"].max()),
        (
            int(df["Weekly_GenAI_Hours"].min()),
            int(df["Weekly_GenAI_Hours"].max())
        )
    )

    with st.expander("🔽 Advanced Filters"):

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


filtered_df = df.copy()

st.markdown(
    body="""
        <style>
            .block-container{
                    padding-top: 2px;
                }
        </style>
    """, 
    unsafe_allow_html=True
)
import streamlit as st

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
    font-size: 14px; 
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
.card{
    background-color:#111111;
    border:1px solid #3a1a2f;
    border-radius:8px;
    padding:8px;
    height:105px;
    margin-top:5px;
    text-align:center;
    box-shadow:0 0 10px rgba(255,75,75,0.12);
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
}
</style>
""", unsafe_allow_html=True)

col1,col2,col3,col4 = st.columns(4,gap="small")

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
.card{
    background-color:#111111;
    border:1px solid #3a1a2f;
    border-radius:8px;
    padding:8px;
    height:105px;
    text-align:center;
    box-shadow:0 0 10px rgba(255,75,75,0.12);
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

import plotly.express as px

st.subheader("🔥Top AI Use Cases")

use_counts = (
    filtered_df["Primary_Use_Case"]
    .value_counts()
    .head(5)
    .reset_index()
)
use_counts.columns = ["Use Case", "Count"]

fig = px.bar(
    use_counts,
    x="Use Case",
    y="Count",
    text="Count",
    color="Use Case",  
    color_discrete_sequence=["#c77e43", "#52d4a9", "#D34CBB", "#9357cc", "#d75151"] 
)

fig.update_traces(
    textposition="outside",
    marker=dict(line=dict(width=1, color="white"))  
)

fig.update_layout(
    plot_bgcolor="#111111",  
    paper_bgcolor="#111111",
    font=dict(color="white", size=14),
    xaxis=dict(title="", showgrid=False, tickangle=-50, tickfont=dict(size=16)),
    yaxis=dict(title="Count", showgrid=False, tickfont=dict(size=14)),
    margin=dict(l=40, r=40, t=40, b=40),
    height=600
)

st.plotly_chart(fig, use_container_width=True)

st.divider()
st.subheader("🌞 Student Distribution by Major and Year of Study")

major_year_counts = (
    df.groupby(["Major_Category", "Year_of_Study"])
    .size()
    .reset_index(name="Count")
)


fig = px.sunburst(
    major_year_counts,
    path=["Major_Category", "Year_of_Study"],  
    values="Count",
    color="Major_Category",
    color_discrete_sequence=px.colors.qualitative.Set2
)

fig.update_layout(
    title_text="Student Distribution by Major and Year of Study",
    font=dict(size=14, color="white"),
    plot_bgcolor="#111111",
    paper_bgcolor="#111111",
    margin=dict(l=40, r=40, t=40, b=40),
    height=500
)

st.plotly_chart(fig, use_container_width=True)
