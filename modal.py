import streamlit as st
from streamlit_modal import Modal
import streamlit.components.v1 as components

# Create a modal instance
modal = Modal(
    "User Input Modal", 
    key="user-input-modal",
    padding=20,    # Optional, default value is 20
    max_width=744  # Optional, default value is 744
)

# Button to open the modal
open_modal = st.button("Open User Input Modal")
if open_modal:
    modal.open()

# Content inside the modal
if modal.is_open():
    with modal.container():
        st.write("### Welcome to the User Input Modal")

        # HTML content with unique styling
        html_string = '''
        <h1 style="font-family: 'Courier New', Courier, monospace; color: #ff6347;">HTML string </h1>
        <p style="font-family: 'Arial', sans-serif; color: #4682b4;">This is a paragraph .</p>
        '''
        components.html(html_string)

        st.write("**Some fancy text:** Enjoy exploring the features of Streamlit modal with styled content!")

        # Interactive elements
        agree_to_terms = st.checkbox("Agree to terms and conditions")
        st.write(f"Checkbox checked: {agree_to_terms}")

        st.write("---")  # Separator line

        # Form example with additional inputs
        st.write("### Additional Information Form")
        with st.form(key='additional_info_form'):
            name = st.text_input("Name")  # Name input from user
            age = st.number_input("Age", min_value=0, max_value=120, step=1)  # Age input from user
            satisfaction = st.slider("Satisfaction Level", min_value=1, max_value=10, value=5)  # Satisfaction level
            feedback = st.selectbox("Feedback", ["Excellent", "Good", "Average", "Poor"])  # Feedback dropdown
            submit_button = st.form_submit_button(label='Submit')

        if submit_button:
            st.write(f"Hello, {name}! You are {age} years old.")
            st.write(f"Satisfaction Level: {satisfaction}")
            st.write(f"Feedback: {feedback}")

# Display the Streamlit app
st.write("This is the main app content.")
