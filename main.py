import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# 日本語フォントを設定
font_path = '/usr/share/fonts/truetype/fonts-japanese-gothic.ttf'  # IPAexGothicのパスを指定
font_prop = fm.FontProperties(fname=font_path)
plt.rcParams['font.family'] = font_prop.get_name()

# Streamlitアプリのタイトル
st.title('バクテリアデータ可視化アプリ')

# CSVファイルのURL
csv_url = "https://raw.githubusercontent.com/kento-koyama/food_micro_data_risk/main/%E9%A3%9F%E4%B8%AD%E6%AF%92%E7%B4%B0%E8%8F%8C%E6%B1%9A%E6%9F%93%E5%AE%9F%E6%85%8B_%E6%B1%9A%E6%9F%93%E7%8E%87.csv"

# データの読み込み (エンコーディングを指定)
df = pd.read_csv(csv_url, encoding='utf-8')

# 欠損値の削除
df = df.dropna(how='any', axis=0)

# バクテリア名のカウント
bacteria_counts = df['Bacteria'].value_counts().reset_index()
bacteria_counts.columns = ['バクテリア名', 'カウント数']

# テーブルの表示
st.write("バクテリア名とカウント数のテーブル")
st.write(bacteria_counts)

# バクテリアカウントをグラフで可視化
st.write("バクテリアのカウント数のグラフ")
fig, ax = plt.subplots(figsize=(10, 6))
ax.barh(bacteria_counts['バクテリア名'], bacteria_counts['カウント数'], color='skyblue')
ax.set_xlabel('カウント数', fontproperties=font_prop)
ax.set_ylabel('バクテリア名', fontproperties=font_prop)
ax.set_title('バクテリアのカウント数', fontproperties=font_prop)
ax.invert_yaxis()  # バーを上から降順に表示
st.pyplot(fig)
