import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# CSVファイルのURL
csv_url = "https://raw.githubusercontent.com/kento-koyama/food_micro_data_risk/main/%E9%A3%9F%E4%B8%AD%E6%AF%92%E7%B4%B0%E8%8F%8C%E6%B1%9A%E6%9F%93%E5%AE%9F%E6%85%8B_%E6%B1%9A%E6%9F%93%E7%8E%87.csv"

# フォントファイルのパスを設定
font_path = 'NotoSansCJKjp-Regular.otf'  # プロジェクトディレクトリ内のフォントファイルを指定

# Streamlit のアプリケーション
st.title('バクテリアカウント可視化')

# フォントの設定
fm.fontManager.addfont(font_path)
font_prop = fm.FontProperties(fname=font_path)
plt.rcParams['font.family'] = font_prop.get_name()

# データの読み込み
df = pd.read_csv(csv_url)

# 欠損値の削除
df = df.dropna(how='any', axis=0)

# バクテリア名のカウント
bacteria_counts = df['Bacteria'].value_counts().reset_index()

# カラム名の変更
bacteria_counts.columns = ['バクテリア名', 'カウント数']

# テーブルの表示
st.write('バクテリアのカウント数:')
st.dataframe(bacteria_counts)

# バクテリアカウントをグラフで可視化
fig, ax = plt.subplots(figsize=(10, 6))
ax.barh(bacteria_counts['バクテリア名'], bacteria_counts['カウント数'], color='skyblue')
ax.set_xlabel('カウント数')
ax.set_ylabel('バクテリア名')
ax.set_title('バクテリアのカウント数')
ax.invert_yaxis()  # バーを上から降順に表示

# グラフを表示
st.pyplot(fig)
