import pandas as pd

# データフレーム（表形式のデータ）を作成
data = {
    'Name': ['Yoshi', 'Tanaka', 'Sato'],
    'Role': ['Engineer', 'Manager', 'Designer'],
    'Score': [90, 85, 88]
}

df = pd.DataFrame(data)

print("--- Data Frame Output ---")
print(df)
print("-------------------------")
print("pandas version:", pd.__version__)