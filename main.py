from pdf_reader import extract_text_from_pdf
from ai_analysis import generate_recommendations
from report_generator import create_report


def analyze_resume():
    print("\n========================================")
    print("          RESUME ANALYZER")
    print("========================================")

    resume_file = input("\nEnter your PDF resume filename: ")
    job_file = input("Enter the job description filename: ")

    try:
        resume = extract_text_from_pdf(resume_file)

        with open(job_file, "r", encoding="utf-8") as file:
            job_description = file.read()

    except FileNotFoundError:
        print("\nERROR: File not found.")
        print("Make sure the filename is correct.")
        return

    skills = [
        "python",
        "sql",
        "git",
        "machine learning",
        "apis",
        "docker",
        "aws",
        "data analysis",
        "pandas",
        "numpy",
        "rest apis",
    ]

    resume_lower = resume.lower()
    job_lower = job_description.lower()

    required_skills = [
        skill for skill in skills
        if skill in job_lower
    ]

    matching_skills = [
        skill for skill in required_skills
        if skill in resume_lower
    ]

    missing_skills = [
        skill for skill in required_skills
        if skill not in resume_lower
    ]

    if required_skills:
        match_percentage = (
            len(matching_skills) / len(required_skills)
        ) * 100
    else:
        match_percentage = 0

    print("\n========================================")
    print("              ANALYSIS")
    print("========================================")

    print(f"\nResume Match: {match_percentage:.1f}%")

    print("\nStrong Skill Matches:")
    for skill in matching_skills:
        print(f"  [MATCH] {skill}")

    print("\nSkill Gaps:")
    for skill in missing_skills:
        print(f"  [GAP] {skill}")

    print("\nJob Fit Summary:")

    if match_percentage >= 80:
        print("  Most of the identified job requirements")
        print("  appear in the resume.")

    elif match_percentage >= 60:
        print("  The resume matches many of the identified")
        print("  requirements, but some areas could be strengthened.")

    else:
        print("  Several identified requirements are not")
        print("  represented in the resume.")

    generate_recommendations(
        matching_skills,
        missing_skills
    )

    create_report(
        match_percentage,
        matching_skills,
        missing_skills
    )

    print("\nReport created successfully!")
    print("Saved as: resume_analysis_report.txt")


def view_report():
    try:
        with open(
            "resume_analysis_report.txt",
            "r",
            encoding="utf-8"
        ) as file:
            report = file.read()

        print("\n" + report)

    except FileNotFoundError:
        print("\nNo report exists yet.")
        print("Run an analysis first.")


def main():
    while True:
        print("\n========================================")
        print("          AI RESUME ANALYZER")
        print("========================================")
        print("1. Analyze Resume")
        print("2. View Previous Report")
        print("3. Exit")

        choice = input("\nChoose an option: ")

        if choice == "1":
            analyze_resume()

        elif choice == "2":
            view_report()

        elif choice == "3":
            print("\nGoodbye!")
            break

        else:
            print("\nInvalid choice. Please select 1, 2, or 3.")


if __name__ == "__main__":
    main()