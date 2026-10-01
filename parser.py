import re
from pathlib import Path

RESUME_PATH = Path("data/sample_resume.txt")

SKILLS = [
    "Python", "Pandas", "NumPy", "Scikit-learn", "SQL",
    "Machine Learning", "NLP", "Git", "GitHub", "Power BI",
    "TensorFlow", "PyTorch", "Excel"
]

text = RESUME_PATH.read_text(encoding="utf-8")

email_match = re.search(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", text)
phone_match = re.search(r"(?:\+91[-\s]?)?[6-9]\d{9}", text)

found_skills = [
    skill for skill in SKILLS
    if re.search(re.escape(skill), text, flags=re.IGNORECASE)
]

education_keywords = [
    "Bachelor", "B.E.", "B.Tech", "Master", "M.E.", "M.Tech",
    "BSc", "MSc", "Diploma"
]

experience_keywords = [
    "Intern", "Internship", "Engineer", "Developer",
    "Analyst", "Experience"
]

education = [
    keyword for keyword in education_keywords
    if re.search(re.escape(keyword), text, flags=re.IGNORECASE)
]

experience = [
    keyword for keyword in experience_keywords
    if re.search(re.escape(keyword), text, flags=re.IGNORECASE)
]

print("=== Resume Parser ===")
print("Email:", email_match.group(0) if email_match else "Not found")
print("Phone:", phone_match.group(0) if phone_match else "Not found")

print("\nSkills:")
for skill in found_skills:
    print("-", skill)

print("\nEducation keywords:")
for item in education:
    print("-", item)

print("\nExperience keywords:")
for item in experience:
    print("-", item)
