import pandas as pd
import os

print("--- Python Script Start ---")

# データの作成
data = {
    'Tool': ['Docker', 'Python', 'Git'],
    'Level': ['Master', 'Intermediate', 'Start'],
    'Goal': ['Environment', 'Skill', 'Version Control']
}
df = pd.DataFrame(data)

# 画面に出力
print(df)

# CSVとして保存（コンテナ内で実行すると、ここにファイルができるはず）
output_file = 'skill_list.csv'
df.to_csv(output_file, index=False)
print(f"--- Saved to {output_file} ---")