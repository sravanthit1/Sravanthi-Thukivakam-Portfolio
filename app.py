from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profilepic.jpg"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Portfolio | Sravanthi Thukivakam"
PAGE_ICON = ":wave:"
NAME = "Sravanthi Thukivakam"
DESCRIPTION = """
Data Engineer & Graduate Student
"""
EMAIL = "thusra05@gmail.com"
CONTACT = "+1 816-205-5362"
SOCIAL_MEDIA = {
    "LeetCode": "https://leetcode.com/u/tsravanthireddy/",
    "LinkedIn": "https://www.linkedin.com/in/sravanthi-thukivakam-1b36041b2/",
    "GitHub": "https://github.com/sravanthit1",
}
PROJECTS = {
    "🏆 AWS DataEngineering Pipeline - Building a data pipeline using S3, Glue, Lambda": "https://github.com/sravanthit1/AWS-DataEngineering-Pipeline",
    "🏆 AWS IoT Greengrass for MySQL - Data from MySQL pushed to S3 using greengrass": "https://github.com/sravanthit1/AWS-IoT-Greengrass-Custom-Component-for-MySQL",
    "🏆 Food Ordering App - Food ordering and delivery application": "https://github.com/Jitender-Singh-NWM/FoodDeliveryApp-Web",
}
CERTIFICATIONS = {
    "🏆 AWS Certified Cloud Practitioner": "https://www.credly.com/badges/4a25deea-c25b-46c7-b700-0f05eb386e5f/linked_in_profile",
    "🏆 AWS Certified Solutions Architect – Associate": "https://www.credly.com/badges/53bdbe10-c1e4-4ca2-a03f-c781594d5292/public_url",
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("Email: ", EMAIL)
    st.write("Phone: ", CONTACT)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qulifications")
st.write(
    """
- ✔️ 2 Years expereince extracting actionable insights from data
- ✔️ Strong hands on experience and knowledge in AWS, SQL, Python and ETL
- ✔️ Good understanding of data pipelines and their respective applications
- ✔️ Excellent team-player and displaying strong sense of initiative on tasks
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programming: Python, SQL, VBA, Java, C++
- 📊 Data Visulization: Tableau, PowerBi, MS Excel, QuickSight
- 📚 ETL: SSIS, SSMS, SAS
- 🗄️ Databases: Postgres, MongoDB, MySQL
- 🔧 DevOps Tools: Docker, Kubernetes, Git, EKS
- ☁️ Cloud: AWS
"""
)


# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "**Associate Cloud Engineer | Data Destination Inc.**")
st.write("07/2024 - Present")
st.write(
    """
- ► Developed and deployed a Python AWS Greengrass component for automated MySQL-to-S3 data extraction, optimizing pipeline efficiency with secure connectivity and monitoring.
- ► Architected and deployed AWS CDK infrastructure with EC2, S3, RDS, Lambda, API Gateway, and DynamoDB, integrating with CloudFormation, VPC, and IAM for optimized automation.
- ► Implemented an ETL pipeline with AWS Glue to convert CSV to Parquet in S3, using Athena for optimized querying and analytics.
"""
)

# --- JOB 2
st.write('\n')
st.write("🚧", "**Data Analyst | Deloitte**")
st.write("06/2022 - 01/2023")
st.write(
    """
- ► Orchestrated end-to-end ETL processes using SQL Server, SSIS, Excel VBA, and UI Path to streamline reporting and enhance efficiency.
- ► Developed interactive data visualizations and a financial dashboard using SQL Server, Tableau, Python, and Microsoft SQL Server to enhance report generation and support informed decision-making.
- ► Executed data cleaning, transformation, and validation, automated reporting and performance testing (UAT), and facilitated smooth production deployment.
"""
)

# --- JOB 3
st.write('\n')
st.write("🚧", "**Intern Data Analyst | Deloitte**")
st.write("02/2022 - 06/2022")
st.write(
    """
- ► Automated Tableau dashboards and ETL processes with SSIS and executed seamless data migration to SQL Server with SQL and SSIS, enhancing visualization, reporting, and integration.
- ► Developed automated Python and SQL scripts for efficient data extraction, processing, and reporting, including data cleaning, transformation, and validation.
- ► Collaborated with analyst team to oversee end-to-end process surrounding customers' return data
"""
)


# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")


# --- CERTIFICATIONS ---
st.write('\n')
st.subheader("Certifications")
st.write("---")
for cert, linkk in CERTIFICATIONS.items():
    st.write(f"[{cert}]({linkk})")