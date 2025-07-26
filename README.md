# 🎮 Sarcasm Showdown: Fool the AI!

**Sarcasm Showdown** is an interactive sentiment analysis game built with Streamlit and HuggingFace Transformers. The goal? Trick the AI into misclassifying your sarcastic text as genuine — or vice versa. The better you fool the model, the higher you score!

![Screenshot](Screenshot%202025-07-26%20235200.png)

---

## 🚀 Features

- 🤖 Real-time sentiment classification using DistilBERT  
- 🧠 Scores based on whether the AI was fooled  
- 📈 Track your score, AI success rate, and sentiment predictions  
- 📊 Visualization of prediction history  
- 🔄 Reset and play as many rounds as you like  
- 💬 Simple, clean, and responsive Streamlit interface  

---

## 🧪 Tech Stack

- **Frontend**: Streamlit UI  
- **Backend/Model**: HuggingFace Transformers (`distilbert-base-uncased-finetuned-sst-2-english`)  
- **Visualization**: Matplotlib  
- **Programming Language**: Python

---

## 📁 Project Structure
- Sarcasm-Showdown/
- ├── app.py # Main Streamlit application
- ├── Screenshot 2025-07-26 235200.png # Screenshot of the running app
- ├── README.md # Project documentation
- └── requirements.txt # Python dependencies

---

## 🎮 How to Play

1. **Enter text** that might be sarcastic or genuine.
2. Click **"🔍 Analyze Sentiment"** to see what the AI predicts.
3. Choose whether your text was actually sarcastic.
4. Click **"✅ Submit Score"** to see if you fooled the AI:
   - Positive + Sarcasm → +10 points ✅  
   - Negative + Sarcasm → -5 points ❌  
   - No sarcasm → No penalty or reward 🎯

---

## 💻 How to Run Locally

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/Sarcasm-Showdown.git
   cd Sarcasm-Showdown

---

### 🔮 Future Enhancements
- 🎯 Add sarcasm-specific training for higher accuracy
- 🌐 Multi-language sarcasm detection
- 🎮 Leaderboard for multiplayer game
- 📊 Export gameplay analytics to CSV


### 🙌 Acknowledgements
- 🤗 Hugging Face for pretrained models
- 📊 Streamlit for the awesome UI framework
- 👨‍🏫 Mr. Lokesh Sir for mentorship and support

---
