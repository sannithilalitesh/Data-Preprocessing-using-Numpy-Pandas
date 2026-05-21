import pandas as pd

df = pd.read_csv("processed_student_dataset.csv")

df["average_score"] = (
    df["math_score"] +
    df["science_score"]
) / 2

top_students = df.sort_values(
    by="average_score",
    ascending=False
).head(5)

print("Top 5 Students:")
print(top_students)

correlation = df["attendance"].corr(
    df["average_score"]
)

print("\nCorrelation between Attendance and Average Score:")
print(correlation)

grouped = df.groupby("gender")[[
    "math_score",
    "science_score",
    "average_score"
]].mean()

print("\nAverage Marks Grouped by Gender:")
print(grouped)