# Resume Parser

A lightweight resume parsing project that extracts basic contact information, skills, education keywords, and experience keywords from plain-text resumes.

This portfolio version intentionally uses a `.txt` input so it runs without external OCR or PDF parsing dependencies.

## Technologies
Python, Regular Expressions, Text Processing

## Structure
```text
15_Resume-Parser/
├── data/
│   └── sample_resume.txt
├── parser.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Run
```bash
pip install -r requirements.txt
python parser.py
```

You can replace `data/sample_resume.txt` with another plain-text resume.
