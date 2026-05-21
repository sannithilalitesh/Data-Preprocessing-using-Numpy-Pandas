import numpy as np
import pandas as pd

df = pd.read_csv("student_dataset.csv")

math_scores = np.array(df["math_score"])

print("Mean:", np.mean(math_scores))
print("Median:", np.median(math_scores))
print("Maximum:", np.max(math_scores))
print("Minimum:", np.min(math_scores))

normalized_scores = (
    (math_scores - np.min(math_scores)) /
    (np.max(math_scores) - np.min(math_scores))
)

print("\nNormalized Scores:")
print(normalized_scores)s