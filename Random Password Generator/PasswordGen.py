import streamlit as st
import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    st.set_page_config(
        page_title="Password Generator",
        page_icon="🔐"
    )


    st.title("Random Password Generator")
    st.write("This app generates a strong random password based on your preferences.")

    st.markdown("### Hello there! 👋")
    name = st.text_input("Enter your name:", "John Doe")
    st.write(f"Welcome, {name}!")

    st.write("### Customize Your Password")
    st.write("Choose your desired password length:")
    password_length = st.slider("Password Length", min_value=12, max_value=20, value=16)

    generate_button = st.button("Generate Password")

    if generate_button:
        password = generate_password(password_length)

        st.write("#### Generated Password")
        st.success(password)
        
        st.write("#### Password Generated Description:")
        st.info("This password was generated using a combination of uppercase letters, lowercase letters, numbers, and special characters. It is designed to be difficult for others to guess or crack, enhancing the security of your accounts and personal information.")

if __name__ == "__main__":
    main()
