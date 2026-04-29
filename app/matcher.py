from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def match_resume(resume, job_desc):
    docs = [resume, job_desc]

    tfidf = TfidfVectorizer()
    matrix = tfidf.fit_transform(docs)

    score = cosine_similarity(matrix[0:1], matrix[1:2])

    return score[0][0] * 100