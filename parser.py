from collections import Counter

# Step 1: Read the log file
with open("sample_auth.log", "r") as file:
    lines = file.readlines()

# Step 2: Extract failed login IPs
failed_ips = []

for line in lines:
    if "Failed password" in line:
        parts = line.split("from ")
        if len(parts) > 1:
            ip = parts[1].split()[0]
            failed_ips.append(ip)

# Step 3: Count attempts per IP
ip_counter = Counter(failed_ips)

# Step 4: Write the output to a report file
with open("failed_ips.txt", "w") as out:
    out.write("Failed login attempts by IP:\n\n")
    for ip, count in ip_counter.most_common():
        out.write(f"{ip}: {count} attempts\n")

print("Report written to failed_ips.txt")
