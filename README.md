\# AI Resume Analyzer



A Python-based resume analysis tool that compares a PDF resume against a job description, identifies matching and missing skills, calculates a match percentage, generates recommendations, and creates a text analysis report.



\## Features



\- Extracts text from PDF resumes

\- Reads job descriptions from text files

\- Identifies required skills

\- Finds matching skills

\- Identifies skill gaps

\- Calculates an overall resume match percentage

\- Generates recommendations

\- Creates a reusable analysis report

\- Includes a simple command-line menu



\## Technologies Used



\- Python

\- pypdf

\- File processing

\- Text analysis

\- Rule-based skill matching



\## How It Works



1\. The user provides a PDF resume.

2\. The program extracts the resume text.

3\. The user provides a job description.

4\. The program identifies skills mentioned in the job description.

5\. The resume is compared against those skills.

6\. Matching and missing skills are displayed.

7\. A match percentage is calculated.

8\. Recommendations are generated.

9\. A report is saved as `resume\_analysis\_report.txt`.



\## Installation



Clone the repository and navigate into the project folder.



Create and activate a virtual environment:



```text

python -m venv venv

venv\\Scripts\\activate

