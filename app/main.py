from flask import Flask, render_template, request
import os

from app.resume_parser import extract_text
from app.preprocess import clean_text
from app.matcher import match_resume

app = Flask(
    __name__,
    template_folder="../templates",
    static_folder="../static"
)

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():
    file = request.files["resume"]
    job_desc = request.form["job_desc"]

    filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
    file.save(filepath)

    resume_text = extract_text(filepath)

    resume_text = clean_text(resume_text)
    job_desc = clean_text(job_desc)

    score = match_resume(resume_text, job_desc)

    return render_template("result.html", score=round(score, 2))


if __name__ == "__main__":
    app.run(debug=True)