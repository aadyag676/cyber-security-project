# Home page for Cybersecurity Incidents and Data Breaches Project
import streamlit as st
from PIL import Image


# Apply dark theme styles
st.markdown(
	'''
	<style>
	body, .stApp {
		background: #101522 !important;
		color: #e0e6ed !important;
	}
	.big-font { font-size:28px !important; font-weight:600; color:#f3eb0a; }
	.subtitle { font-size:20px !important; color:#b3c6e0; }
	.stMarkdown, .stText, .stHeader, .stSubheader, .stInfo, .stAlert, .stDataFrame, .stTable {
		color: #e0e6ed !important;
	}
	.stAlert {
		background-color: #232946 !important;
		border-left: 6px solid #f3eb0a !important;
	}
	.st-bb, .st-cq, .st-cv, .st-cw, .st-cx, .st-cy, .st-cz {
		background: #232946 !important;
		color: #e0e6ed !important;
	}
	.stButton>button {
		background: #2e8bc0 !important;
		color: #fff !important;
	}
	</style>
	''',
	unsafe_allow_html=True
)

st.markdown(
	'''
	<div style="background: linear-gradient(90deg, #232946 60%, #2e8bc0 100%); padding: 18px 0; border-radius: 12px; margin-bottom: 18px; box-shadow: 0 2px 16px #0004;">
		<h1 style="color: #fff; text-align: center; font-family: 'Segoe UI', Arial, sans-serif; font-size: 2.7rem; letter-spacing: 1px; margin: 0;">
			<span style="color: #f3eb0a;">Cybersecurity</span> Incidents &amp; Data Breaches <span style="color: #f3eb0a;">2024</span>
		</h1>
	</div>
	''',
	unsafe_allow_html=True
)
st.image("assets/banner.gif")




st.markdown('<p class="big-font">Welcome to the Cybersecurity Incidents & Data Breaches Dashboard</p>', unsafe_allow_html=True)

st.markdown('<p class="subtitle">Explore real-world data on major cybersecurity incidents and breaches reported in 2024. Analyze attack types, vectors, industry impact, and more to gain actionable insights for risk mitigation and awareness.</p>', unsafe_allow_html=True)

st.markdown('<hr style="border:1px solid #2e8bc0;">', unsafe_allow_html=True)

st.header("Project Overview")
st.write(
	"""
	This interactive dashboard provides:
	- **Visual analytics** of attack types, vectors, and industry/country impact
	- **Key metrics**: records compromised, financial losses, recovery times, and more
	- **Insights** into security postures, regulatory fines, and reputational effects
	- **Data-driven guidance** for organizations and individuals to strengthen cyber defenses
	""",
)

st.header("Get Started")
st.write("Use the sidebar to navigate:")
st.markdown("- 📊 **Dashboard**: Explore interactive charts and trends\n- ℹ️ **About**: Learn more about the dataset")

st.markdown('<hr style="border:1px solid #2e8bc0;">', unsafe_allow_html=True)

st.info("""This project is for educational and analytical purposes, using a curated dataset of 2024's most significant cybersecurity incidents across industries and countries.""")
