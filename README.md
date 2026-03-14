# 👴 Nana Ji AI Assistant

An AI-powered conversational assistant that responds like a wise Indian grandfather (Nana Ji).
The assistant gives life advice, motivation, and emotional support in a warm and friendly tone.

This project uses **AI + voice interaction** to simulate conversations with a virtual elder who guides users with wisdom and positivity.

---

## 🚀 Features

* 👴 Nana Ji personality-based responses
* 💬 Conversational AI chat
* 🎤 Voice input (speech-to-text)
* 🔊 Voice output (text-to-speech)
* 🧠 Conversation memory
* 🌐 Streamlit web interface

---

## 🛠 Tech Stack

* Python
* Streamlit
* Groq API (LLM inference)
* SpeechRecognition
* pyttsx3

---

## 📂 Project Structure

```
nana_ai_assistent
│
├── app.py                # Main Streamlit application
├── voice.py              # Voice input/output functions
├── memory.py             # Conversation memory system
├── dataset.json          # Training conversation examples
├── nana_personality.txt  # Nana Ji personality dataset
├── requirements.txt      # Project dependencies
└── README.md             # Project documentation
```

---

## ⚙️ Installation

### 1️⃣ Clone the repository

```
git clone https://github.com/MaryhaSulbhi/nana_ai_assistent.git
cd nana_ai_assistent
```

---

### 2️⃣ Install dependencies

```
pip install -r requirements.txt
```

---

### 3️⃣ Add your Groq API key

Create a `.env` file:

```
GROQ_API_KEY=your_api_key_here
```

---

### 4️⃣ Run the application

```
streamlit run app.py
```

The app will start at:

```
http://localhost:8501
```

---

## 🌐 Deployment

This project can be deployed using:

* Streamlit Community Cloud
* Render
* Hugging Face Spaces

For Streamlit deployment:

1. Push the project to GitHub
2. Connect the repository to Streamlit Cloud
3. Add your API key in **Secrets**

---

## 💡 Future Improvements

* ChatGPT-style chat interface
* Nana Ji avatar or animated character
* Emotion detection from user input
* Multi-language support (Hindi + English)
* Mobile-friendly UI

---

🚀 Live Demo

👉 Try the App:
(https://nanaaiassistent-l6qbahgs2kncgv7kquusov.streamlit.app/)
---

## 👩‍💻 Author

**Maryha Sulbhi**

---

## ⭐ Support

If you like this project, please consider giving it a **star ⭐ on GitHub**.
