import re

def classify_with_regex(log_message): 
    patterns = {
        r'(\sUser|User) User\d+ logged (out|in).': 'User Action',
        r'(\s*Backup|Backup) (started|ended) at \d{4}-\d{2}-\d{2} \d+:\d+:\d+.': 'System Notification',
        r'Backup completed successfully.': 'System Notification',
        r'System updated to version \d+.\d+.\d+.': 'System Notification',
        r'Disk cleanup completed successfully.': 'System Notification',
        r'System reboot initiated by user User\d+.': 'System Notification',
        r'Account with ID \d+ created by User\d+.': 'User Action', 
        r'(\s*User|User) \d+ (has escalated|escalated) (privileges to|to) admin level': 'Security Alert',
        r'(\s*Admin|Admin) privilege escalation alert for user \d+': 'Security Alert',
        r'Elevation of admin privileges detected for user \d+': 'Security Alert'
    }
    
    for pattern, label in patterns.items(): 
        if re.search(pattern, log_message, re.IGNORECASE):
            return label
    return 'Unclassified'

if __name__ == '__main__': 
    log_messages = [
        "User User123 logged in.",
        "Backup started at 2025-07-19 12:30:45.",
        "System reboot initiated by user User5678.",
        "User 4321 made multiple incorrect login attempts.",
        "Disk cleanup completed successfully.",
        "Module X reported an unexpected shutdown.",
        "User User987 logged out.",
        "System updated to version 2.5.3.",
        "Account with ID 7890 created by User567.",
        "Unexpected message not matching any pattern."
    ]
    
    for msg in log_messages: 
        print(classify_with_regex(msg)) 