students=[]
for i in range(2):
    name=input("enter name:")
    role=str(input("enter role:"))
    students.append((name, role))
    print("\n students")
    for student in students:
        print(student)
        
student_skills = set(input("Enter your skills: ").split())
job_skills = {"Python", "SQL", "Git"}

matched = student_skills & job_skills
missing = job_skills - student_skills

print("\nMatched Skills:", matched)
print("Missing Skills:", missing)