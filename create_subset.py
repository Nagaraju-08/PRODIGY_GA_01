input_file = "dataset/train.txt"
output_file = "dataset/train_subset.txt"

limit = 10000

with open(input_file, "r", encoding="utf-8") as infile:
    lines = infile.readlines()

with open(output_file, "w", encoding="utf-8") as outfile:
    outfile.writelines(lines[:limit])

print(f"Created dataset with {limit} dialogues.")