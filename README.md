# AI-Powered Resume Screener

## Overview
This is a simple AI-powered resume screener that uses NLP to extract key skills from resumes and compare them against a job description using TF-IDF and cosine similarity. The resumes are ranked based on relevance to the job description.

## Features
- Extracts keywords from job descriptions and resumes using **spaCy**.
- Computes **TF-IDF vectors** for text comparison.
- Uses **cosine similarity** to rank resumes based on relevance.
- Simple and efficient implementation for resume screening.

## Installation
### Prerequisites
- Python 3.8+
- Virtual environment (optional but recommended)

### Install Dependencies
```bash
pip install spacy scikit-learn
python -m spacy download en_core_web_sm
```

## Usage
Run the script using:
```bash
python resume_screener.py
```

## How It Works
1. **Extracts Keywords**: The script processes the job description and resumes using spaCy to extract relevant keywords.
2. **TF-IDF Vectorization**: Converts the extracted keywords into numerical vectors.
3. **Similarity Matching**: Uses cosine similarity to rank resumes based on how well they match the job description.

## Example Output
```
Ranking of Resumes:
1. Score: 0.75 - Skilled in machine learning, Python, FastAPI, and data science. Developed AI models.
2. Score: 0.65 - I have experience in Python, NLP, and deep learning. Worked on chatbot development.
3. Score: 0.20 - Expert in Java and web development. Built scalable applications with React and Node.js.
```

## Future Enhancements
- Support for **PDF and DOCX** resume parsing.
- Improved **NER-based skill extraction**.
- Integration with **Flask or FastAPI** for a web-based API.

## License
This project is open-source and available under the **MIT License**.

