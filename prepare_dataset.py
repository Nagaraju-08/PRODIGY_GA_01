# prepare_dataset.py

input_file = "dataset/movie_lines.txt"
output_file = "dataset/train.txt"

with open(input_file, "r", encoding="utf-8", errors="ignore") as infile:
    lines = infile.readlines()

with open(output_file, "w", encoding="utf-8") as outfile:
    for line in lines:
        parts = line.strip().split(" +++$+++ ")

        if len(parts) == 5:
            dialogue = parts[4].strip()

            if dialogue:
                outfile.write(dialogue + "\n")

print("Dataset prepared successfully!")