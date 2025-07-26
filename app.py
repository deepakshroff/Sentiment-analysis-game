# app.py - Sentiment Analysis Game with Streamlit

import os
import warnings
# Suppress all warnings
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 
warnings.filterwarnings('ignore')

import streamlit as st
import matplotlib.pyplot as plt
from transformers import pipeline
import time

# Set page config
st.set_page_config(
    page_title="Sentiment Analysis Game",
    page_icon="😊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize the model (with caching to load only once)
@st.cache_resource
def load_model():
    try:
        # Explicitly use CPU to avoid GPU-related warnings
        return pipeline("text-classification", 
                      model="distilbert-base-uncased-finetuned-sst-2-english",
                      device=-1)  # -1 means CPU
    except Exception as e:
        st.error(f"Failed to load model: {str(e)}")
        return None

classifier = load_model()

# Define functions
def analyze_sentiment(text):
    if not classifier:
        return "ERROR", 0.0
    try:
        result = classifier(text)
        return result[0]['label'], result[0]['score']
    except Exception as e:
        st.error(f"Analysis failed: {str(e)}")
        return "ERROR", 0.0

def plot_results(history):
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar([f"Round{i+1}" for i in range(len(history))], 
           [s[1] for s in history],
           color=['red' if s[0]=='POSITIVE' else 'blue' for s in history])
    ax.set_xlabel('Rounds')
    ax.set_ylabel('Confidence Score')
    ax.set_title('Sentiment Analysis Results')
    st.pyplot(fig)

# Main app function
def main():
    st.title("🎮 Sarcasm Showdown: Fool the AI! 🎮")
    st.markdown("""
    ### How to play:
    - Enter text that might be sarcastic
    - See if the AI detects the sarcasm
    - Score points when you fool the AI!
    - Positive sentiment + sarcasm = +10 points
    - Negative sentiment + sarcasm = -5 points
    """)
    
    # Initialize session state
    if 'score' not in st.session_state:
        st.session_state.score = 0
    if 'rounds' not in st.session_state:
        st.session_state.rounds = 0
    if 'history' not in st.session_state:
        st.session_state.history = []
    if 'last_input' not in st.session_state:
        st.session_state.last_input = ""
    
    # Sidebar for controls
    with st.sidebar:
        st.header("Game Controls")
        if st.button("🔄 Reset Game"):
            st.session_state.score = 0
            st.session_state.rounds = 0
            st.session_state.history = []
            st.session_state.last_input = ""
            st.rerun()
        
        st.markdown("---")
        st.subheader("📊 Current Stats")
        st.metric("🏆 Score", st.session_state.score)
        st.metric("🕹️ Rounds Played", st.session_state.rounds)
        
        if st.session_state.history:
            success_rate = len([h for h in st.session_state.history if h[0]=='NEGATIVE'])/len(st.session_state.history)
            st.metric("🤖 AI Success Rate", f"{success_rate:.1%}")
    
    # Main game area
    col1, col2 = st.columns([3, 1])
    
    with col1:
        user_input = st.text_area(
            "Enter your text (sarcastic or genuine):",
            value=st.session_state.last_input,
            height=150,
            key="input_area",
            placeholder="Type something like 'Oh great, another meeting...'"
        )
        
        analyze_col, score_col = st.columns(2)
        
        with analyze_col:
            if st.button("🔍 Analyze Sentiment"):
                if user_input.strip():
                    st.session_state.last_input = user_input
                    label, confidence = analyze_sentiment(user_input)
                    emoji = "😊" if label == "POSITIVE" else "😠" if label == "NEGATIVE" else "❌"
                    
                    st.session_state.history.append((label, confidence))
                    
                    st.subheader("Analysis Result")
                    st.markdown(f"### AI says: {emoji} {label} ({confidence:.2f} confidence)")
                    
                    # Scoring section
                    st.subheader("Scoring")
                    is_sarcasm = st.radio(
                        "Was this sarcasm?",
                        ("Yes", "No"),
                        index=1,
                        horizontal=True
                    )
        
        with score_col:
            if 'last_input' in st.session_state and st.session_state.last_input:
                if st.button("✅ Submit Score"):
                    if is_sarcasm == "Yes":
                        if label == "POSITIVE":
                            st.session_state.score += 10
                            st.success("✅ AI fooled! +10pts")
                        else:
                            st.session_state.score -= 5
                            st.error("❌ AI detected sarcasm! -5pts")
                    else:
                        st.info("➡ AI's judgment accepted")
                    
                    st.session_state.rounds += 1
                    st.rerun()
    
    with col2:
        st.subheader("📜 Game History")
        if st.session_state.history:
            for i, (label, conf) in enumerate(st.session_state.history, 1):
                st.metric(
                    f"Round {i}",
                    f"{label} ({conf:.2f})",
                    delta="+10" if (label == "POSITIVE" and i == len(st.session_state.history)) else 
                         "-5" if (label == "NEGATIVE" and i == len(st.session_state.history)) else None
                )
        
        if st.button("📈 Show Plot"):
            if st.session_state.history:
                plot_results(st.session_state.history)
            else:
                st.warning("No data to plot yet!")

if __name__ == "__main__":
    main()