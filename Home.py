import openai
import streamlit as st

def main():
    """A simple Streamlit app"""
    st.title("Simpson’s Paradox: A Counter-Intuitive Statistical Phenomenon")

    st.write("""
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
             
    ## How to use this Experience
             
    ### Tools
             
    This experience included one interactive data tool and two distinct LLM chatbot pages. The "Iris Flower Experience" and "Talk with Judea" are introduced in the relevant chapters.
             
    You can always access our ChatGPT implementation to deepen your learning or when you feel stuck. Just keep in mind that for ChatGPT, we only allow preset prompts to avoid cheating. Also, LLMs make mistakes, watch out!
             
    ### Pages & Chapters
             
    Each Chapter links to a Notion page with the chapter content and links to any further material. You can always go back to this page and use the tools provided here. We recommend opening the Notion pages in seperate tabs.
             
    ### Concept & Review Blocks
             
    Most chapters include Concepts Blocks, wich briefly summarize key concepts that have been introduced in the material. Use them to refresh your memory or make sure you understood the concept. Also, at the end of most pages you find a Review Block. Make sure you understood the concepts listed there before moving on.
             
    ### Tasks & Assessments
             
    Tasks are indicated in the Chapter pages. Please follow along carefully and stick to the instructions. The Springfield Assignment and the Final Quiz are used to measure your learning progress at the end of this experience.
    
    ### Start with Chapter 1. Have fun! 🥳
             
    """)

if __name__ == "__main__":
    main()
