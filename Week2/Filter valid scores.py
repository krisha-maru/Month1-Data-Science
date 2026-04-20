scores = [45, 67, -5, 89, 120, 34, 76]
valid_scores = [score for score in scores if 0 <= score <= 100]
print("Original scores:", scores)
print("Valid scores:", valid_scores)