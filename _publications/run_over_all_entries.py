import os
import re

INPUT_FILE = "allpub_entries.md"
OUTPUT_DIR = "publications"

os.makedirs(OUTPUT_DIR, exist_ok=True)

with open(INPUT_FILE, "r", encoding="utf-8") as f:
    content = f.read()

# Split entries when a new title starts
entries = re.split(r"\n(?=\s*title:)", content)

def clean_title_fragment(title, length=15):
    title = title.lower()
    title = re.sub(r"[^a-z0-9]", "", title)
    return title[:length]

for entry in entries:
    entry = entry.strip()
    if not entry:
        continue

    # Replace your name
    entry = entry.replace("C. B. Saner", "Can Berk Saner")

    # Enforce exactly two spaces before title:
    entry = re.sub(r"^\s*title:", "  title:", entry)

    # Extract title and date
    title_match = re.search(r'title:\s*"(.+?)"', entry)
    date_match = re.search(r'date:\s*([0-9\-]+)', entry)

    if not title_match or not date_match:
        continue

    title = title_match.group(1)
    date = date_match.group(1)

    title_part = clean_title_fragment(title)
    filename = f"{date}_{title_part}.md"
    filepath = os.path.join(OUTPUT_DIR, filename)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write("---\n")
        f.write(entry + "\n")
        f.write("---\n")

    print(f"Written: {filepath}")
