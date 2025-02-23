# # Import

# import streamlit as st
# import pandas as pd 
# import os 
# from io import BytesIO

# #Set up our App
# st.set_page_config(page_title="Data sweeper", layout = "wide")
# st.title(" Data Sweeper ")
# st.write("Transform your files between CSV and Excel formats with built-in data cleaning and visualization")

# uploaded_files = st.file_uploader("Upload you files (CSV or Excel):", type = ["csv", "xlsx"],
#         accept_multiple_files=True)

# if uploaded_files:
#     for file in uploaded_files:
#         file_ext = os.path.splitext(file.name)[-1].lower()

#         if file_ext == ".csv":
#             df = pd.read_csv(file)
#         elif file_ext == ".xlsx":
#             df = pd.read_excel(file)
#         else:st.error("unsupported file type: {file_ext}")
#         continue

#     # Display info about the file 
#     st.write(f"**File Name:** {file.name}")
#     st.write(f"**File Size:** {file.size/1024}")

#     # Show 5 rows of our df
#     st.write("Preview the Head of the DataFrame")
#     st.dataframe(df.head())

#     # Option for data cleaning 
#     st.subheader("Data Cleanig Options")
#     if st.checkbox(f"Clean Data for {file.name}"): 
#         col1, col2 = st.columns(2)

#         with col1:
#             if st.button(f"Remove Duplicates from {file.name}"):
#                 df.drop_duplicates(inplace=True)
#                 st.write("Duplicates Removed")

#                 with col2:
#                     if st.button(f"Fill Missing Values for {file.name}"):
#                         numeric_cols = df.select_dtypes(include=["number"]).columns 
#                         df[numeric_cols]  = df[numeric_cols].fillna(df[numeric_cols].mean())
#                         st.write("Missing Values have been Filled!")

#                         # Choose Specific Coloumns to keep or Convert
#                         st.subheader("Select Coloumns to Convert")
#                         columns = st.multiselect(f"Choode Columns for {file.name}", df.columns, df.columns)
#                         df = df[columns]

#                         # Create Some Visualizations
#                         st.subheader(" Data Visualization")
#                         if st.checkbox(f"Show Visualization for {file.name}"): 
#                             st.bar_chart(df.select_dtypes(include="number").iloc[:,:2])

#                         # Convert the file From CSV to Excel 
#                         st.subheader("Conversion Option")
#                         conversion_type = st.radio(f"Convert {file.name} to: ", ["CSV","Excel"], key= file.name)  
#                         if st.button(f"Convert {file.name}"):
#                             buffer = BytesIO()
#                             if conversion_type == "CSV":
#                                 df.to_csv (buffer, index=False)
#                                 file_name = file.name.replace(file_ext, ".csv")
#                                 mime_type = "text/csv"

#                             elif conversion_type == "Excel":
#                                 df.to_excel(buffer, index=False)
#                                 file_name = file.name.replace(file_ext,".xlsx")
#                                 mime_type = "application/vnd.openxmlformats-officedpcument.spreadsheetml.sheet"
#                                 buffer.seek(0)

#                                 # Download Button

#                                 st.download_button(
#                                     label=f" Download {file.name} as {conversion_type}",
#                                     data=buffer,
#                                     file_name=file_name,
#                                     mime=mime_type
#                                 )

#                                 st.success("All files processed !")

import streamlit as st

st.set_page_config(page_title="Growth Mindset Project", page_icon="★")

st.title("Growth Mindset Challenge: Web Application with Streamlit")
st.header("Welcome to Your Growth Journey!")
st.write("Embrace challenges, learn from mistakes, and unlock your full potential.")

# Quote section
st.header("Today's Growth Mindset Quote")
st.write("Success is not final, failure is not fatal: it is the courage to continue that counts.")

st.header("What's Your Challenge Today?")
user_input = st.text_input("Describe a challenge you are facing:")

# Condition
if user_input:
    st.success(f"You are facing: {user_input}. Keep pushing towards your goal.")
else:
    st.warning("Tell us about your challenge to get started!")

# Reflecting
st.header("Reflect on Your Learning")
reflection = st.text_area("Write your reflections here:")

if reflection:
    st.success(f"Great insight! Your reflection: {reflection}")
else:  
    st.info("Reflecting on past experiences helps you grow through difficulties.")

# Achievements
st.header("Celebrate Your Wins!")
achievement = st.text_input("Share something you have recently accomplished:")

if achievement:
    st.success(f"Amazing! You achieved: {achievement}")
else:  
    st.info("Big or small, every achievement matters!")

# Footer
st.write("---")
st.write("Keep believing in yourself!")
st.write("Created by Bashar Sheikh")
