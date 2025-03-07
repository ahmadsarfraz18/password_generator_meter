# Import necessary libraries

import streamlit as st  # For creating the web app
import random  # For generating random passwords
import string  # For handling string operations

# Function to generate a password based on user preferences
def generate_password(length, use_numbers, use_special_chars, use_ascii_letters):
    characters = ""  # Initialize an empty string for characters
    
    # Add ASCII letters (uppercase and lowercase) if checkbox is checked
    if use_ascii_letters:
        characters += string.ascii_letters
    
    # Add numbers if checkbox is checked
    if use_numbers:
        characters += string.digits
    
    # Add special characters if checkbox is checked
    if use_special_chars:
        characters += string.punctuation
    
    # If no character type is selected, default to ASCII letters
    if not characters:
        characters = string.ascii_letters
    
    # Generate the password using random choices
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Function to simulate a chatbot response
def chatbot_response(user_input):
    # Simple chatbot logic
    if "hello" in user_input.lower():
        return "Hi there! How can I help you?"
    elif "password" in user_input.lower():
        return "Sure! Generate a password using the options on the left."
    else:
        return "I'm sorry, I didn't understand that. Can you rephrase?"

# Streamlit app layout
def main():
    # Set the title of the app
    st.title("Password Generator Meter with Chatbot")
    
    # Sidebar for password options
    st.sidebar.header("Password Settings")
    
    # Slider for password length
    length = st.sidebar.slider("Password Length", 8, 32, 12)
    
    # Checkboxes for password options
    use_numbers = st.sidebar.checkbox("Include Numbers", value=True)
    use_special_chars = st.sidebar.checkbox("Include Special Characters", value=True)
    use_ascii_letters = st.sidebar.checkbox("Include ASCII Letters", value=True)
    
    # Generate password button
    if st.sidebar.button("Generate Password"):
        password = generate_password(length, use_numbers, use_special_chars, use_ascii_letters)
        st.success(f"Generated Password: {password}")
    
    # Chatbot section
    st.header("Chatbot")
    user_input = st.text_input("Ask me anything about passwords:")
    if user_input:
        response = chatbot_response(user_input)
        st.text_area("Chatbot:", value=response, height=100)

# Run the app
if __name__ == "__main__":
    main()