import streamlit as st

def main():
    st.title("Basic Streamlit Example")
    st.write("This is a basic Streamlit example.")

    # Add a text input widget
    user_input = st.text_input("Enter your name:", "")

    # Add a button widget
    button_clicked = st.button("Submit")

    # When the button is clicked, display a message
    if button_clicked:
        st.write(f"Hello, {user_input}!")

if __name__ == "__main__":
    main()
