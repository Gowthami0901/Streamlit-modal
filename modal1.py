import streamlit as st
from streamlit_modal import Modal
import streamlit.components.v1 as components


st.write("### Welcome to Our Course Platform")
st.write("Click the below button to provide your feedback.")

# Create a modal 
modal = Modal(
    "Student Feedback Form", 
    key="student-feedback-modal",
    padding=20,    
    max_width=744  
)

# Button 
open_modal = st.button("Provide Feedback")
if open_modal:
    modal.open()

# Content inside the modal
if modal.is_open():
    with modal.container():
        st.write("### We Value Your Feedback")

        html_string = '''
        <h1 style="font-family: 'Courier New', Courier, monospace; color: #ff6347;">Student Feedback Form</h1>
        <p style="font-family: 'Arial', sans-serif; color: #4682b4;">Please provide your feedback below:</p>
        '''
        components.html(html_string)

        st.write("**Your feedback helps us improve our courses and services.**")

        # Feedback form
        with st.form(key='feedback_form'):
            name = st.text_input("Name")  
            age = st.number_input("Age", min_value=10, max_value=100, step=1)  
            course = st.text_input("Course")  
            rating = st.slider("Course Rating", min_value=1, max_value=5, value=3)  
            comments = st.text_area("Comments")  
            submit_button = st.form_submit_button(label='Submit Feedback')

        if submit_button:
            st.write("### Thank you for your feedback!")
            st.write(f"**Name:** {name}")
            st.write(f"**Age:** {age}")
            st.write(f"**Course:** {course}")
            st.write(f"**Rating:** {rating}")
            st.write(f"**Comments:** {comments}")

