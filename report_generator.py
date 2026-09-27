def create_report(match_percentage, matching_skills, missing_skills):
    report = []

    report.append("================================")
    report.append("       RESUME ANALYSIS REPORT")
    report.append("================================")

    report.append("")
    report.append(f"Overall Match: {match_percentage:.1f}%")

    report.append("")
    report.append("MATCHING SKILLS")
    report.append("--------------------------------")

    if matching_skills:
        for skill in matching_skills:
            report.append(f"[MATCH] {skill}")
    else:
        report.append("No matching skills found.")

    report.append("")
    report.append("MISSING SKILLS")
    report.append("--------------------------------")

    if missing_skills:
        for skill in missing_skills:
            report.append(f"[MISSING] {skill}")
    else:
        report.append("No missing skills identified.")

    report.append("")
    report.append("RECOMMENDATIONS")
    report.append("--------------------------------")

    if missing_skills:
        report.append(
            "Consider adding projects, coursework, or experience "
            "that demonstrates your missing skills."
        )

        for skill in missing_skills:
            report.append(
                f"Consider developing or demonstrating experience "
                f"with {skill}."
            )
    else:
        report.append(
            "Your resume contains all of the skills identified "
            "in the job description."
        )

    report.append("")
    report.append("================================")

    report_text = "\n".join(report)

    with open(
        "resume_analysis_report.txt",
        "w",
        encoding="utf-8"
    ) as file:
        file.write(report_text)

    return report_text