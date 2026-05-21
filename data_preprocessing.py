import pandas as pd

df = pd.read_csv("student_dataset.csv")

df["math_score"] = pd.to_numeric(
    df["math_score"],
    errors="coerce"
)

df["science_score"] = pd.to_numeric(
    df["science_score"],
    errors="coerce"
)

df["attendance"] = pd.to_numeric(
    df["attendance"],
    errors="coerce"
)

df["math_score"].fillna(
    df["math_score"].mean(),
    inplace=True
)

df["science_score"].fillna(
    df["science_score"].mean(),
    inplace=True
)

df["attendance"].fillna(
    df["attendance"].mean(),
    inplace=True
)

df["exam_date"] = pd.to_datetime(
    df["exam_date"],
    errors="coerce"
)


def remove_outliers(column):
    q1 = column.quantile(0.25)
    q3 = column.quantile(0.75)

    iqr = q3 - q1

    lower = q1 - 1.5 * iqr
    upper = q3 + 1.5 * iqr

    return column.where(
        (column >= lower) & (column <= upper),
        column.median()
    )


df["math_score"] = remove_outliers(
    df["math_score"]
)

df["science_score"] = remove_outliers(
    df["science_score"]
)

df.drop_duplicates(inplace=True)

print(df)

df.to_csv(
    "processed_student_dataset.csv",
    index=False
)

print("\nPreprocessing completed.")