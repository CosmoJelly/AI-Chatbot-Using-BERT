import streamlit as st

# Mock model function for testing purposes
def bot_answer_question(question):
    # Mock answers for testing
    mock_answers = {
        "What is game design?": "Game design is the art and craft of creating the rules and content of a game.",
        "How do I start designing a game?": "To start designing a game, begin by brainstorming ideas and defining the core mechanics and objectives.",
        "What are some key elements of game design?": "Key elements of game design include gameplay mechanics, storytelling, level design, and player engagement.",
        "Can you recommend any books on game design?": "Sure! Some popular books on game design include 'The Art of Game Design' by Jesse Schell and 'Rules of Play' by Katie Salen and Eric Zimmerman.",
        "Thank you!": "You're welcome!"
    }
    
    # Return mock answer based on the question
    return mock_answers.get(question, "I'm sorry, I don't understand that question.")

# Define Streamlit app with custom styling and layout
def main():
    st.title("🎮 Game Design Book Bot 📚")
    
    # Custom CSS for styling
    st.markdown("""
    <style>
        .title {
            color: #ff5733;
            text-align: center;
            font-size: 36px;
            margin-bottom: 30px;
        }
        .input-box {
            width: 80%;
            padding: 10px;
            font-size: 18px;
            border: 2px solid #3498db;
            border-radius: 10px;
            margin-bottom: 20px;
        }
        .button {
            background-color: #3498db;
            color: white;
            font-size: 18px;
            padding: 10px 20px;
            border-radius: 10px;
            cursor: pointer;
        }
        .button:hover {
            background-color: #2980b9;
        }
        .answer {
            font-size: 20px;
            margin-top: 20px;
        }
    </style>
    """, unsafe_allow_html=True)
    
    # Input field for user question
    user_question = st.text_input("Enter your question:")

    # Button to submit the question
    button_label = '<div class="button">Ask</div>'
    if st.markdown(button_label, unsafe_allow_html=True):
        # Pass the user question to the bot model
        answer = bot_answer_question(user_question)
        
        # Display the answer
        st.text_area("Answer:", value=answer, height=100)

if __name__ == "__main__":
    main()
