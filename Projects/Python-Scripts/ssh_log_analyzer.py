# SSH Log Analyzer
# A simple tool to scan SSH log files for security events

print("[+] Starting SSH Log Analysis")
print("=" * 50)

# Name of the log file to analyze
log_filename = 'auth.log'

try:
    # Open the log file for reading
    with open(log_filename, 'r') as log_file:
        # Read through each line in the file
        for line in log_file:
            # Check for failed password attempts (brute force attacks)
            if "Failed password" in line:
                print(f"[!] FAILED LOGIN: {line.strip()}")
            
            # Check for invalid usernames (reconnaissance attempts)
            elif "Invalid user" in line:
                print(f"[!] INVALID USER: {line.strip()}")
            
            # Check for successful logins (for monitoring)
            elif "Accepted password" in line:
                # Clean any special characters that might appear
                clean_line = line.replace('ï»¿', '')
                print(f"[+] SUCCESSFUL LOGIN: {clean_line.strip()}")
            
            # Check for connection closures (normal activity)
            elif "Connection closed" in line:
                print(f"[ ] CONNECTION CLOSED: {line.strip()}")

except FileNotFoundError:
    # This runs if the log file doesn't exist
    print(f"[ERROR] File '{log_filename}' not found.")
    print("Please make sure:")
    print("1. The log file exists in the same folder as this script")
    print("2. The filename is spelled correctly")
    print("3. Or update the 'log_filename' variable in the script")

except Exception as e:
    # This catches any other unexpected errors
    print(f"[ERROR] Something went wrong: {e}")

print("[+] Analysis complete.")