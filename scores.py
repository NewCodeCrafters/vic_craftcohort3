# create a list of scores
scores = [56,89,19,20,67,56,87,98,39,76,98,76,98]
# Get highest and lowest scores
# Set a variable to get them
highest = 0
lowest = scores[0]

# List students and their scores
for i in range(len(scores)):
    print(f"student {i}: {scores[i]}")
    if highest > scores[i]:
        highest = scores[i]
    if scores[i] < lowest:
        lowest = scores[i]
print()
print(f"== Attendance ==")        
print(f"{len(scores)} student took the test")
print()
print(f"== Highest ===")
print()