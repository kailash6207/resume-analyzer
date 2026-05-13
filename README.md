# AI-Powered ATS Resume Analyzer 🚀

A full-stack web application designed to help job seekers optimize their resumes using **Natural Language Processing (NLP)**. This tool semantically compares a resume against a job description to provide a matching score and identify missing skills.

## 🧠 Features
- **Semantic Skill Matching:** Uses the `all-MiniLM-L6-v2` transformer model to understand the context of skills (e.g., matching "VLSI" to "Hardware Architecture").
- **Multi-Format Support:** Extracts text from both **PDF** and **DOCX** files.
- **Real-Time Scoring:** Calculates an ATS score based on contact information and skill relevance.
- **Modern UI:** Built with Flask, HTML5, and CSS3 for a clean user experience.

## 🛠️ Tech Stack
- **Backend:** Python, Flask
- **AI/ML:** Sentence-Transformers (Hugging Face), Scikit-learn, NumPy
- **Parsing:** pdfplumber, python-docx
- **Frontend:** HTML, CSS, JavaScript

## 📂 Project Structure
- `app.py`: Main Flask server and routing logic.
- `utils/matcher.py`: Core AI logic for vector embeddings and cosine similarity.
- `utils/parser.py`: Text extraction and contact parsing.
- `static/`: Frontend assets (CSS/JS).
- `templates/`: HTML views.

## ⚖️ License
Copyright (c) 2026 Kailash N H. All Rights Reserved.  
*This repository is for portfolio showcasing purposes only. No license is granted to use, copy, or distribute this code.*