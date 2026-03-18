student_scores = [180, 124, 165, 173, 189, 169, 146]

# With sum function
total_score = sum(student_scores)
print(f"total_score: {total_score}")


# With for loop
total_exam_score = 0
for score in student_scores:
    total_exam_score += score

print(f"total_exam_score: {total_exam_score}")


# Replicate the max function - This will pick out the largest number in the list
max_function = max(student_scores)
print(f"max_function: {max_function}")

highest_score = 0
for score in student_scores:
    if highest_score < score:
        highest_score = score

print(f"highest_score: {highest_score}")