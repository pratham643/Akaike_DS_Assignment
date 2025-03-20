import streamlit as st
from utils import generate_report

st.set_page_config(page_title="News Insight", page_icon="📢", layout="centered")


def main():
    st.markdown("<h1 style='text-align: center; color: #333;'>📢 News Insight</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #666;'>Get summarized news & sentiment analysis</p>", unsafe_allow_html=True)
    
    company_name = st.text_input("", placeholder="Enter company name (e.g., Tesla, Google)...", help="Enter a company's name to fetch recent news.")

    if st.button("Analyze", help="Click to generate report"):
        if company_name:
            generate_report(company_name)
        else:
            st.warning("Please enter a company name.")
    
    
    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #aaa;'>Built with ❤️ by Prathmesh</p>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
