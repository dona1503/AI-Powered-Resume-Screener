import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load English NLP model
nlp = spacy.load("en_core_web_sm")

# Sample job description
job_description = "We are looking for a software engineer skilled in Python, machine learning, and NLP. Experience with FastAPI is a plus."

# Sample resumes
resumes = [
    "I have experience in Python, NLP, and deep learning. Worked on chatbot development.",
    "Expert in Java and web development. Built scalable applications with React and Node.js.",
    "Skilled in machine learning, Python, FastAPI, and data science. Developed AI models."
]

def extract_keywords(text):
    doc = nlp(text)
    return " ".join([token.lemma_ for token in doc if token.pos_ in ["NOUN", "PROPN", "VERB"]])

# Preprocess job description and resumes
job_keywords = extract_keywords(job_description)
resume_keywords = [extract_keywords(resume) for resume in resumes]

# Compute similarity scores
vectorizer = TfidfVectorizer()
resume_vectors = vectorizer.fit_transform([job_keywords] + resume_keywords)
similarity_scores = cosine_similarity(resume_vectors[0], resume_vectors[1:])

# Rank resumes based on similarity
ranked_resumes = sorted(zip(resumes, similarity_scores[0]), key=lambda x: x[1], reverse=True)

# Display ranked results
print("Ranking of Resumes:")
for i, (resume, score) in enumerate(ranked_resumes):
    print(f"{i+1}. Score: {score:.2f} - {resume}")
