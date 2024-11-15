#[Assume all arrays and data has already been set up and stored as per mentioned in the question]

#class combines total mark for studentNo entered and returns it
def combinedTotalMark(studentNo):
    score = 0
    for i in range(SubjectNo):
        score += StudentMark[studentNo][i]
    #adds value at index i of array StudentMark[StudentNo] for SubjectNo times
    return score

#class calculates average, rounds it to closest int, and returns it
def calculateAverage(studentNo):
    score = combinedTotalMark(studentNo)/SubjectNo
    return round(score)
    #rounds the thing

#class determines grade awarded
def GradeAwarded(StudentNo):
    if calculateAverage(StudentNo) < 40:
        return "Failed"
    elif 40 <= calculateAverage(StudentNo) < 55:
        return "Pass"
    elif 55 <= calculateAverage(StudentNo) < 70:
        return "Merit"
    elif 70 <= calculateAverage(StudentNo):
        return "Distinction"
    else:
        return "Invalid"

#class prints the thing when called
def gradeInfo(studentNo):
    print(f"Name: {StudentName[StudentNo]}")
    print(f"Combined Total Mark: {combinedTotalMark(StudentNo)}")
    print(f"Average Mark: {calculateAverage(StudentNo)}")
    print(f"Grade Awarded: {GradeAwarded(StudentNo)}")

#calls gradeInfo for student i ClassSize times
for i in range(ClassSize):
    gradeInfo(i)

