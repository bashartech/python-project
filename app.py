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
