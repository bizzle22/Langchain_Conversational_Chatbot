# 🤖 Conversational AI Chatbot with Google Gemini and LangChain

A powerful, conversational AI chatbot built with **Python**, leveraging **Google's Gemini** model via the **LangChain** framework.  
The user interface is created with **Streamlit** for a seamless and interactive chat experience.
Link to Chatbot - http://ec2-13-55-157-78.ap-southeast-2.compute.amazonaws.com:8501/

---

## ✨ Features

- **Conversational Memory** – Remembers the context of the conversation for coherent, follow-up answers.  
- **Powered by Google Gemini** – Uses the state-of-the-art `gemini-1.5-flash` model.  
- **Built with LangChain** – Provides robust and scalable LLM integration.  
- **Interactive UI** – A clean, user-friendly chat interface built with Streamlit.  
- **Secure & Deployable** – Manages API keys safely and supports one-click deployment.  

---

## 💡 Potential Applications

This chatbot can be extended into a variety of specialized AI assistants:

- **Customer Support Assistant** – Connect with product documentation to provide 24/7 automated support.  
- **Internal Knowledge Bot** – Access internal wikis or HR docs to help employees find information quickly.  
- **Personalized Learning Tutor** – Fine-tune with educational material to create an interactive learning companion.  
- **Lead Generation Tool** – Engage website visitors, answer product queries, and qualify leads automatically.  

---

## 🚀 Getting Started

### Prerequisites
- Python **3.8+**  
- A **Google AI API Key** from [Google AI Studio](https://aistudio.google.com/)

---

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/your-repository-name.git
cd your-repository-name
```

---

### 2. Create and Activate a Virtual Environment
**On macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**On Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

---

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

---

### 4. Set Up Environment Variables
Create a `.env` file in the project root and add your Google AI API key:
```bash
# .env
GOOGLE_API_KEY="Your-Google-AI-Studio-Key-Goes-Here"
```

---

### 5. Run the Streamlit App
```bash
streamlit run app.py
```

---

## 📌 Tech Stack
- **Python** – Core programming language  
- **LangChain** – LLM orchestration framework  
- **Google Gemini (gemini-1.5-flash)** – Large Language Model  
- **Streamlit** – Interactive UI  

---

## 📄 License
This project is licensed under the [MIT License](LICENSE).  

---
