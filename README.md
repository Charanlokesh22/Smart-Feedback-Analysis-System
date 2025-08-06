# Smart Feedback Analysis System 🧠

An intelligent feedback collection and sentiment analysis platform using FastAPI and HuggingFace Transformers. Designed for organizations to gather user insights and visualize sentiment trends with secure API integration.

 Tech Stack
- FastAPI + Python
- MongoDB
- HuggingFace Transformers (BERT)
- JWT Auth + OAuth2
- Docker
- Angular (optional frontend)

 Features
- Submit user feedback via API
- NLP sentiment classification (positive, neutral, negative)
- JWT-secured admin login
- View dashboard with real-time sentiment stats
- Export feedback logs as CSV

 Installation
git clone https://github.com/Charanlokesh22/smart-feedback-analysis.git
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
