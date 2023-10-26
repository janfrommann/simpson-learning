import openai
import streamlit as st

def main():
    """A simple Streamlit app"""
    st.title("Welcome to Your Interactive Learning Experience")

    st.write("""
    ## Simpson’s Paradox: A Counter-Intuitive Statistical Phenomenon
    Welcome to this interactive learning experience about Simpson’s Paradox - one of the most counter-intuitive phenomena in statistics!

    Unfortunately, this paradox is not related to the “The Simpsons”, however, we will visit Springfield for a decision-making case at the end of this course.
    """)

    # Assuming you have an image file in the same directory as your script, 
    # or provide the correct path to your image file.
    # If your image is hosted online, you can use the URL directly.
    image_file = 'homer.png'  # replace with your own image

    # Display the image. If it's on the web, you can use st.image with a URL directly.
    st.image(image_file, use_column_width=True)

    st.write("""
    ## Let's Get Started!
    Now that you're here, we'll explore the intriguing world of Simpson's Paradox. Prepare to challenge your understanding of statistics and data interpretation!
    """)

if __name__ == "__main__":
    main()
