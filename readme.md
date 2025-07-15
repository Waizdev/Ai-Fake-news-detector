# 🕵️ Truth Lens – AI-Powered Fake News Detection

**Truth Lens** is an AI-based web application that detects fake news using powerful NLP embeddings and an XGBoost classifier. It takes raw news content as input, transforms it into semantic vectors using a Sentence Transformer, and predicts whether the news is real or fake with high confidence.

---

## 🚀 Features

- ✅ Built with **FastAPI** for blazing-fast backend performance
- 🧠 Uses **Sentence-BERT** for semantic embedding of text
- 🌲 Powered by an optimized **XGBoost** model trained on labeled fake/real news data
- 💡 Provides clear predictions with confidence scores
- 🎨 Clean and responsive **web interface** (HTML/CSS/JS)
- 🖱️ Easy to deploy locally with `run_app.bat`

---

## 📁 Folder Structure

truth_lens/
├── embed_model/ # Pre-trained sentence transformer model
├── static/ # Frontend (index.html, styles, etc.)
├── templates/ # Optional (for Jinja2 templates)
├── pycache/ # Python cache
├── xgb_model.pkl # Trained XGBoost model
├── main.py # FastAPI backend code
├── run_app.bat # Windows batch file to launch server
├── requirements.txt # Python dependencies
├── readme.txt # Text version of the README
├── notes.txt # Development notes or logs
└── feedback_log.txt # Logs for user feedback (optional)


---

## ⚙️ How It Works

1. 📝 User enters a news headline or article snippet in the frontend.
2. 🧠 The backend loads the Sentence-BERT model and transforms the input into a dense vector.
3. 🌲 XGBoost uses this vector to classify the news as **real or fake**.
4. 📊 The prediction is sent back to the frontend along with a confidence score.

---

## 🛠️ Installation & Run (Local)

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/truth-lens.git
cd truth-lens
2. Create and Activate a Virtual Environment (Optional but Recommended)
python -m venv venv
venv\Scripts\activate  # Windows
3. Install Dependencies

pip install -r requirements.txt
4. Run the App 🚀

uvicorn main:app --reload
Or simply double-click run_app.bat

5. Open in Browser
Navigate to: http://127.0.0.1:8000

📊 Sample Output

📝 Input: "Government launches new scheme for rural development"
🟢 Prediction: Real News
📊 Confidence: 92.47%
🧠 Models Used
Embedder: sentence-transformers/all-MiniLM-L6-v2

Classifier: XGBoost trained on a labeled dataset of fake and real news

💡 Future Improvements
✅ Feedback-based retraining

🌐 Multilingual support

📱 Mobile responsive design

🔒 Improved model explainability (e.g., SHAP)

👨‍💻 Author
Waizdev – GitHub Profile
Bachelor’s Student in AI | Focused on NLP, ML, and System Design

📜 License
This project is open-source and available under the MIT License.


---








