# Grade Evaluator

## Description
A Python program that reads student grades from a CSV file, calculates GPA, determines Pass/Fail status per category and identifies assignments for resubmission.

## Files
- `grade-evaluator.py` - Main Python script
- `grades.csv` - Sample student grades data
- `organizer.sh` - Shell script to archive old grades

## How to Run

### Python Script
```bash
python3 grade-evaluator.py
```
When prompted, enter: `grades.csv`

### Shell Script
```bash
chmod +x organizer.sh
./organizer.sh
```

## GPA Scale
- GPA = (Final Grade / 100) × 5.0

## Pass/Fail Criteria
- Formative category must score >= 50%
- Summative category must score >= 50%
- Student must pass BOTH categories to pass overall

## Author
Elham Abdul Rahman
