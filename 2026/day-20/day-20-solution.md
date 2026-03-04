Day 20 – Bash Scripting Challenge: Log Analyzer and Report Generator

LOG ANALYZER SCRIPT
====================================

#!/bin/bash

log_file=$1

if [ "$#" -eq 0 ]; then
    echo "Error: No arguments provided." >&2
    exit 1
fi

if [ ! -f "$log_file" ]; then
    echo "Error: File '$log_file' not found." >&2
    exit 1
fi

error_count=$(grep -iE "ERROR|Failed" "$log_file" | wc -l)

echo "Total error count is = $error_count"

echo "----------CRITICAL EVENT---------------"

critical_events=$(grep -n "CRITICAL" $log_file)
echo "$critical_events"

echo "--------TOP 5 ERROR MESSAGES----------"
top_error=$(grep "ERROR" "$log_file" | awk '{$1=$2=$3=""; print}' | sort | uniq -c | sort -nr | head -5)

echo "$top_error"

date=$(date '+%Y-%m-%d')
report="log_report_"$date".txt"
total_lines=$(wc -l < "$log_file")
{
echo "LOG ANALYSIS REPORT"
echo "Date: $date"
echo "log file: $log_file"
echo "Total error count: $log_file"
echo "Total error count: $error_count"
echo "Top error messages: $top_error"
echo "List of critical events"
echo "$critical_events"
} > "$report"

echo "***REPORT GENERATED = $report"

mkdir -p archive/
mv "$log_file" archive/

echo "Log file moved to archive..."
===================================================================

Tools Used
grep – search log patterns
awk – process text fields
sort – sort data
uniq – count repeated messages
wc – count lines

What I Learned
-analysing logs and soring important finding 
-using awk and sort and uniq tools makes output simpler and understandable 
-automating the task so we dont have to analyze the same task like log analyzer
