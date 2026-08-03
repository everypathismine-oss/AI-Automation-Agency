import streamlit as st

# Configure the page layout and dark mode styling
st.set_page_config(
    page_title="AI Automation Agency",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Sidebar Navigation Panel
st.sidebar.title("🤖 AI_AGENCY")
st.sidebar.markdown("---")
menu = st.sidebar.radio("Navigate Site", ["Marketing Homepage", "Client Portal Dashboard"])

# ----------------- HOMEPAGE VIEW -----------------
if menu == "Marketing Homepage":
    st.title("We Build Smart AI Automations For Your Business")
    st.subheader("Stop wasting hours on manual tasks. We integrate intelligent AI workflows into your daily systems.")
    
    st.markdown("---")
    
    # Services Columns
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("### 01 / AI Lead Gen")
        st.write("Automated bots scrape targets, compose hyper-personalized emails, and book qualified prospects.")
    with col2:
        st.markdown("### 02 / Custom CRM")
        st.write("We connect OpenAI and Claude directly to your customer workflows to automatically summarize client needs.")
    with col3:
        st.markdown("### 03 / Workflows")
        st.write("Connect Make.com, Zapier, and Airtable with smart AI logic to instantly handle file processing.")

    st.markdown("---")
    
    # Interactive Pricing Tool
    st.markdown("## Interactive Systems Pricing")
    st.write("Adjust the slider to see estimates based on your automation complexity:")
    
    complexity = st.slider("Select Number of Core Integrations Needed", 1, 10, 3)
    estimated_cost = complexity * 850
    st.metric(label="Estimated Project Build Cost", value=f"${estimated_cost:,} USD", delta="One-time payment")
    
    st.markdown("---")
    st.markdown("### Ready to get started?")
    st.link_button("Book Free Strategy Call", "https://cal.com")

# ----------------- CLIENT DASHBOARD VIEW -----------------
elif menu == "Client Portal Dashboard":
    st.title("🔐 Secure Client Operations Dashboard")
    st.write("Welcome to your automated systems terminal.")
    
    # Mock Secure Login Environment
    username = st.text_input("Agency Username")
    password = st.text_input("Security Access Token", type="password")
    
    if username == "admin" and password == "agency2026":
        st.success("Access Granted! Loading your real-time automation streams...")
        
        # User Specific Metrics
        db_col1, db_col2, db_col3 = st.columns(3)
        db_col1.metric("API Requests Handled", "45,201", "+12% this week")
        db_col2.metric("Total Execution Hours Saved", "184 hrs", "+22 hrs")
        db_col3.metric("System Operational Health", "99.98%")
        
        st.markdown("### Active Automation Pipelines")
        st.info("🔄 Pipeline 1: Email Scraper ➡️ Claude Filter ➡️ Slack Alert [RUNNING]")
        st.info("🔄 Pipeline 2: Shopify Webhook ➡️ OpenAI Auto-Refund ➡️ Customer Email [RUNNING]")
    else:
        st.warning("Please enter your client access credentials above to view operational data pipelines.")
