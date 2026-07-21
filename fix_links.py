import os
import glob

# Rename freelancer.php to freelancer.html
old_path = os.path.join("workshop", "freelancer.php")
new_path = os.path.join("workshop", "freelancer.html")

if os.path.exists(old_path):
    os.rename(old_path, new_path)
    print(f"Renamed {old_path} to {new_path}")
else:
    print(f"{old_path} does not exist.")

# Find all html files and update links
files = glob.glob("**/*.html", recursive=True)
for filepath in files:
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if "freelancer.php" in content:
            content = content.replace("freelancer.php", "freelancer.html")
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Updated links in {filepath}")
    except Exception as e:
        print(f"Failed to process {filepath}: {e}")

print("Done fixing links.")
