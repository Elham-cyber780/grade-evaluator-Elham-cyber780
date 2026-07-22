#!/usr/bin/python3
import csv
import sys
import os

def load_csv_data():
    """
    Prompts the user for a filename, checks if it exists,
    and extracts all fields into a list of dictionaries.
    """
    filename = input("Enter the name of the CSV file to process (e.g., grades.csv): ")
    if not os.path.exists(filename):
        print(f"Error: The file '{filename}' was not found.")
        sys.exit(1)
    assignments = []
    try:
        with open(filename, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                assignments.append({
                    'assignment': row['assignment'],
                    'group': row['group'],
                    'score': float(row['score']),
                    'weight': float(row['weight'])
                })
        return assignments
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        sys.exit(1)

def evaluate_grades(data):
    """
    Evaluates student grades from CSV data.
    """
    print("\n--- Processing Grades ---")

    # a) Check if all scores are between 0-100
    for item in data:
        if item['score'] < 0 or item['score'] > 100:
            print(f"Error: Invalid score {item['score']} for '{item['assignment']}'. Must be 0-100.")
            sys.exit(1)

    # b) Validate total weights
    total_weight = sum(item['weight'] for item in data)
    formative_weight = sum(item['weight'] for item in data if item['group'] == 'Formative')
    summative_weight = sum(item['weight'] for item in data if item['group'] == 'Summative')

    if total_weight != 100:
        print(f"Error: Total weights must equal 100. Got {total_weight}.")
        sys.exit(1)
    if formative_weight != 60:
        print(f"Error: Formative weights must equal 60. Got {formative_weight}.")
        sys.exit(1)
    if summative_weight != 40:
        print(f"Error: Summative weights must equal 40. Got {summative_weight}.")
        sys.exit(1)

    # c) Calculate Final Grade and GPA
    formative_items = [item for item in data if item['group'] == 'Formative']
    summative_items = [item for item in data if item['group'] == 'Summative']

    formative_score = sum(item['score'] * (item['weight'] / 100) for item in formative_items)
    summative_score = sum(item['score'] * (item['weight'] / 100) for item in summative_items)

    final_grade = formative_score + summative_score
    gpa = (final_grade / 100) * 5.0

    formative_percentage = (formative_score / formative_weight) * 100
    summative_percentage = (summative_score / summative_weight) * 100

    # d) Determine Pass/Fail
    formative_pass = formative_percentage >= 50
    summative_pass = summative_percentage >= 50
    overall_pass = formative_pass and summative_pass

    # e) Check for failed formative assignments for resubmission
    resubmit = None
    if not formative_pass:
        failed_formative = [item for item in formative_items if item['score'] < 50]
        if failed_formative:
            resubmit = max(failed_formative, key=lambda x: x['weight'])

    # f) Print final decision
    print(f"\n--- Grade Report ---")
    print(f"Formative Score: {formative_score:.2f}/{formative_weight} ({formative_percentage:.2f}%) -> {'PASS' if formative_pass else 'FAIL'}")
    print(f"Summative Score: {summative_score:.2f}/{summative_weight} ({summative_percentage:.2f}%) -> {'PASS' if summative_pass else 'FAIL'}")
    print(f"Final Grade: {final_grade:.2f}/100")
    print(f"GPA: {gpa:.2f}/5.0")

    if overall_pass:
        print("\nFinal Decision: PASSED! 🎉")
    else:
        print("\nFinal Decision: FAILED!")
        if resubmit:
            print(f"Recommended Resubmission: '{resubmit['assignment']}' (Weight: {resubmit['weight']}%)")

if __name__ == "__main__":
    course_data = load_csv_data()
    evaluate_grades(course_data)
