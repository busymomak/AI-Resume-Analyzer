def generate_recommendations(matching_skills, missing_skills):
    print("\n==============================")
    print("      AI RECOMMENDATIONS")
    print("==============================")

    if missing_skills:
        print("\nSkills to consider developing:")
        for skill in missing_skills:
            print(f"  • {skill}")

    if matching_skills:
        print("\nYour resume already demonstrates:")
        for skill in matching_skills:
            print(f"  • {skill}")

    print("\nSuggested next steps:")

    if missing_skills:
        print(
            "  1. Consider adding relevant experience or projects "
            "that demonstrate your missing skills."
        )
        print(
            "  2. If you genuinely have experience with a missing "
            "skill, make sure it is clearly represented on your resume."
        )
    else:
        print(
            "  1. Your resume contains the skills identified "
            "in the job description."
        )

    print(
        "  3. Tailor your resume summary and project descriptions "
        "to the specific position."
    )