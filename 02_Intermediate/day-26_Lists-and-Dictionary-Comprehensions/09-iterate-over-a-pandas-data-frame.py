import pandas

student_dict = {
    "student": ["Angela", "James", "Lilly"],
    "score": [56, 76, 98]
}

student_data_frame = pandas.DataFrame(student_dict)
print(f"student_data_frame: {student_data_frame}\n")

# Loop through rows of data frame
for (index, row) in student_data_frame.iterrows():
    if row.student == "Angela":
        print(f"row.student == \"Angela\" (print score): {row.score}\n")