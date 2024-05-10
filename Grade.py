def calculate_average(grades):
  """Calculates the average grade in a list of grades.

  Args:
    grades: A list of numerical grades.

  Returns:
    The average grade as a float.
  """
  return sum(grades) / len(grades)

def find_highest_lowest(grades):
  """Finds the highest and lowest grades in a list of grades.

  Args:
    grades: A list of numerical grades.

  Returns:
    A tuple containing the highest and lowest grades.
  """
  return max(grades), min(grades)

def count_above_threshold(grades, threshold):
  """Counts the number of students with grades above a certain threshold.

  Args:
    grades: A list of numerical grades.
    threshold: The minimum grade to be counted.

  Returns:
    The number of students with grades above the threshold as an integer.
  """
  return sum(grade > threshold for grade in grades)

# Sample list of student grades
grades = [85, 72, 91, 68, 98]

# Calculate average grade
average_grade = calculate_average(grades.copy())  # Use a copy to avoid modifying the original list
print(f"Average grade: {average_grade:.2f}")

# Find highest and lowest grades
highest, lowest = find_highest_lowest(grades.copy())
print(f"Highest grade: {highest}")
print(f"Lowest grade: {lowest}")

# Count students above 80
num_above_80 = count_above_threshold(grades.copy(), 80)
print(f"Number of students with grades above 80: {num_above_80}")
