# ssh-log-parser
Python script that parses SSH logs to detect and summarize failed login attempts by IP for early brute-force activity analysis

This Python code identifies and summarizes unsuccessful login attempts by IP by processing SSH authentication logs (`auth.log`) to mimic a rudimentary SOC detection workflow. It illustrates how basic log analysis methods can be used to identify early brute-force activity.

## Overview

- Input: Sample `auth.log` file (simulated)
- Output: `failed_ips.txt` containing IPs with corresponding failed login counts

## Methodology

1. Created a sample authentication log with timestamps and failed login attempts
2. Wrote a Python script to:
   - Open and read the file line-by-line
   - Search for `"Failed password"` entries
   - Extract and count occurrences by IP address
3. Exported the results to a report (`failed_ips.txt`) showing suspicious IPs and attempt counts

## Example Output

192.168.1.10: 5 failed attempts
203.0.113.25: 3 failed attempts
