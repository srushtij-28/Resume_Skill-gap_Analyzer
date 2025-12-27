def get_skills(input_text):
    skills = input_text.lower().split(",")
    return set(skill.strip() for skill in skills)


print("====== RESUME SKILL GAP ANALYZER ======\n")

resume_input = input("Enter your resume skills (comma separated): ")
job_input = input("Enter job required skills (comma separated): ")

resume_skills = get_skills(resume_input)
job_skills = get_skills(job_input)

matched_skills = resume_skills & job_skills
missing_skills = job_skills - resume_skills

print("\n✅ Matching Skills:")
if matched_skills:
    for skill in matched_skills:
        print("-", skill)
else:
    print("None")

print("\n❌ Missing Skills (Skill Gap):")
if missing_skills:
    for skill in missing_skills:
        print("-", skill)
else:
    print("No skill gap! You match the job requirements.")
