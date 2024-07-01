import streamlit as st
import pandas as pd

# CSVファイルのパス
csv_file_path = 'FEH_00351000_240628103233.csv'

# CSVファイルを読み込む
df = pd.read_csv(csv_file_path,encoding='latin1',engine='python',skiprows=6)

df_cleaned = df.dropna()
# アプリのタイトル
st.title('CSVデータ表示アプリ')

# データフレームを表示
st.write('以下はアップロードされたCSVファイルの内容です。')
st.dataframe(df_cleaned)