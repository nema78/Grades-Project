
import pandas as pd

# 1. Read the CSV file
df = pd.read_csv("Grades_Short.csv")

# 2. Columns to calculate the average from
grade_columns = ["Assignment_1", "Assignment_2", "Quiz_1", "Quiz_2", "Mid_Term_Exam", "Final_Exam"]

# 3. Calculate the final grade (average)
df["FinalGrade"] = df[grade_columns].mean(axis=1)

# 4. Function to determine letter grade
def get_letter_grade(final_grade):
    if final_grade >= 90:
        return "A+"
    elif final_grade >= 80:
        return "A"
    elif final_grade >= 70:
        return "B"
    elif final_grade >= 60:
        return "C"
    elif final_grade > 55:
        return "D"
    else:
        return "F"

# 5. Apply the function to create a new column
df["LetterGrade"] = df["FinalGrade"].apply(get_letter_grade)

# 6. Save the modified data to a new CSV file
df.to_csv("Grades_Final.csv", index=False)

print("Grades_Final.csv has been created successfully.")




