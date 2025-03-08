import streamlit as st
import random
import string
import pandas as pd

# Function to generate password
def generate_password(length, use_numbers, use_special_chars, use_ascii_letters, exclude_similar):
    characters = ""
    if use_numbers:
        characters += string.digits
    if use_special_chars:
        characters += string.punctuation
    if use_ascii_letters:
        characters += string.ascii_letters
    if not characters:
        return "Please select at least one character type."
    if exclude_similar:
        similar_chars = "1lI0O"
        characters = ''.join([char for char in characters if char not in similar_chars])
    return ''.join(random.choice(characters) for _ in range(length))

# Password strength checker
def password_strength(password):
    strength = sum([
        len(password) >= 12,
        any(char in string.digits for char in password),
        any(char in string.punctuation for char in password),
        any(char in string.ascii_letters for char in password)
    ])
    return strength

# Initialize session state
if 'password_history' not in st.session_state:
    st.session_state.password_history = []
if 'dark_mode' not in st.session_state:
    st.session_state.dark_mode = False

# Page Config
st.set_page_config(page_title="Password Strength Meter", layout="wide")

# Custom CSS for modern UI
st.markdown(
    """
    <style>
        .stApp {background: linear-gradient(to right, #6a11cb, #2575fc); color: white;}
        .main-title {text-align: center; font-size: 36px; font-weight: bold;}
        .stButton>button {background-color: #ff5733; color: white; border-radius: 10px; padding: 10px 20px;}
        .stButton>button:hover {background-color: #c70039;}
        .password-box {font-size: 24px; font-weight: bold; background: white; color: black; padding: 10px; border-radius: 5px; text-align: center;}
    </style>
    """,
    unsafe_allow_html=True
)

# Dark Mode Toggle
if st.sidebar.button("🌙 Toggle Dark Mode"):
    st.session_state.dark_mode = not st.session_state.dark_mode
    st.rerun()

# UI Title
st.markdown("<div class='main-title'>🔐 Secure Password Generator</div>", unsafe_allow_html=True)

# Sidebar Options
st.sidebar.header("⚙️ Customize Your Password")
password_length = st.sidebar.slider("Password Length", 6, 32, 12)
use_numbers = st.sidebar.checkbox("Include Numbers")
use_special_chars = st.sidebar.checkbox("Include Special Characters")
use_ascii_letters = st.sidebar.checkbox("Include Letters", value=True)
exclude_similar = st.sidebar.checkbox("Exclude Similar Characters")

# Generate Password Button
if st.sidebar.button("Generate Password 🎲"):
    password = generate_password(password_length, use_numbers, use_special_chars, use_ascii_letters, exclude_similar)
    st.session_state.password_history.append(password)
    
    st.markdown(f"<div class='password-box'>{password}</div>", unsafe_allow_html=True)
    
    strength = password_strength(password)
    if strength == 4:
        st.success("🔒 Strong Password")
    elif strength == 3:
        st.warning("🔑 Moderate Password")
    else:
        st.error("🔓 Weak Password")

# Password History
st.sidebar.header("📜 Password History")
if st.session_state.password_history:
    for idx, pwd in enumerate(st.session_state.password_history, 1):
        st.sidebar.write(f"{idx}. `{pwd}`")
    if st.sidebar.button("Export CSV 📂"):
        df = pd.DataFrame(st.session_state.password_history, columns=["Password"])
        df.to_csv("password_history.csv", index=False)
        st.sidebar.success("Exported Successfully!")
    if st.sidebar.button("🗑 Clear History"):
        st.session_state.password_history = []
        st.sidebar.success("History Cleared!")

# Footer
st.markdown("""---
**🚀 Developed by Mahar Ahmad Sarfraz**""")
