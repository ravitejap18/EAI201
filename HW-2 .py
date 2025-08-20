def grade_student():
    print("AI Grading Assistant")
    subs = ["Intro to aiMl", "DSA", "Discrete_maths", "Engineering Maths III", "German "]
    marks = []
    t = []
    op = "pass"  

    for i in range(5):
        x = float(input(f"marks of {subs[i]} out of(100:) "))
        if x > 100 or x < 0:
            print("sorry something is wrong with the entry !!!")
            return  # stop program for invalid input
        else:
            marks.append(x)
            if x < 35:
                op = "fail"
                t.append(i)

    if 0 in marks:
        print("Result is invalid student got zero in some subject")
        return
    else:
        s = sum(marks)
        print("Total marks : ", s)
        result = s / 5
        print("The final result : ", result, "%")

    # Check pass/fail outside
    if op == "fail":
        for idx in t:
            print(f"Student Failed in {subs[idx]}!!!! ")
    else:
        print("Student pass!!!!!!!!!!!!")


# Main loop to run again
while True:
    grade_student()
    again = input("\nDo you want to run again ? (y/n): ").lower()
    if again != "y":
        print("Exiting program.!!!!!!!!!!!!")
        break
