#!/bin/bash

# Get today's date
DATE=$(date +%Y-%m-%d)

# Define file names
GRADES_FILE="grades.csv"
ARCHIVE_FILE="grades_${DATE}.csv"
LOG_FILE="organizer.log"

# Check if grades.csv exists
if [ ! -f "$GRADES_FILE" ]; then
    echo "Error: $GRADES_FILE not found!"
    exit 1
fi

# Archive the old grades.csv
cp "$GRADES_FILE" "$ARCHIVE_FILE"
echo "Archived $GRADES_FILE to $ARCHIVE_FILE"

# Create fresh empty grades.csv
echo "assignment,group,score,weight" > "$GRADES_FILE"
echo "Created fresh $GRADES_FILE"

# Log what happened
echo "[$DATE] Archived $GRADES_FILE to $ARCHIVE_FILE" >> "$LOG_FILE"
echo "[$DATE] Created fresh $GRADES_FILE" >> "$LOG_FILE"

echo "Done! Check $LOG_FILE for details."
