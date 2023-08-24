def main():
    results = []

    while True:
        input_line = input("Exam points and exercises completed: ")

        if input_line == "":
            break

        exam_points, exercises_completed = map(int, input_line.split())
        results.append((exam_points, exercises_completed))


    print_statistics(results)

def calculate_exercise_points(exercises_completed):
    exercise_points = min(exercises_completed // 10, 10)
    return exercise_points

def calculate_grade(exam_points, exercise_points):
    total_points = exam_points + (exercise_points)
    
    if exam_points < 10:
        return 0
    
    if total_points < 15:
        return 0
    elif total_points < 18:
        return 1
    elif total_points < 21:
        return 2
    elif total_points < 24:
        return 3
    elif total_points < 28:
        return 4
    else: 
        return 5
 


def print_statistics(results):
    total_students = len(results)
    total_exam_points = 0
    total_exercise_points = 0
    pass_count = 0
    grade_distribution = [0, 0, 0, 0, 0, 0]  # To store the count of each grade

    for exam_points, exercises_completed in results:
        exercise_points = calculate_exercise_points(exercises_completed)
        total_exam_points += exam_points
        total_exercise_points += exercise_points

        grade = calculate_grade(exam_points, exercise_points)

        if grade > 0:
            pass_count += 1
        grade_distribution[grade] += 1

    points_average = (total_exam_points + total_exercise_points) / total_students
    pass_percentage = (pass_count / total_students) * 100

    print("Statistics:")
    print(f"Points average: {points_average:.1f}")
    print(f"Pass percentage: {pass_percentage:.1f}")
    print("Grade distribution:")

    for i in range(5, 0, -1):
        stars = "*" * grade_distribution[i]
        print(f"  {i}: {stars}")

    print(f"  0: {'*' * grade_distribution[0]}")

main()

