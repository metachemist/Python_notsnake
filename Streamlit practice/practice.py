import pandas as pd
import streamlit as st
import os
from io import BytesIO

# Set up our App
st.set_page_config(page_title="Data Sweeper", page_icon="📀", layout="wide")
st.title("Data Sweeper")
st.write("Transform your files between CSV and Excel formats.")

uploaded_files = st.file_uploader("Upload a file (CSV or Excel):", type=["csv", "xlsx"], accept_multiple_files = True)

if uploaded_files:
    for file in uploaded_files:
        file_ext = os.path.splitext(file.name)[-1].lower()

        if file_ext == ".csv":
            df = pd.read_csv(file)
        elif file_ext in [".xls", ".xlsx"]:   
            df = pd.read_excel(file)
        else:
            st.error(f"Unsupported file format: {file_ext}")
            continue
         
         # Display info about the file
        st.write(f"**File Name:** {file.name}")
        st.write(f"**File Size:** {file.size/1024}")

        # Show five rows of our data frame
        st.write("Preview the head of the dataframe:")
        st.dataframe(df.head())

        # Options for data cleaning
        st.subheader("Data Cleaning Options")
        if st.checkbox(f"Clean Data for {file.name}"):
           col1, col2 = st.columns(2)

           with col1:
               if st.button("Remove Duplicates from filename"):
                   df.drop_duplicates(inplace=True)
                   st.write("Duplicates removed!.")
           with col2:
               if st.button(f"Fill Missing Values for {file.name}"):
                   numeric_cols = df.select_dtypes(include=["number"]).columns
                   df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
                   st.write("Missing values ave been filled!")
                                