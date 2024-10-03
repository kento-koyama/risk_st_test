import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# CSVファイルのURL
csv_url = "https://raw.githubusercontent.com/kento-koyama/food_micro_data_risk/main/%E9%A3%9F%E4%B8%AD%E6%AF%92%E7%B4%B0%E8%8F%8C%E6%B1%9A%E6%9F%93%E5%AE%9F%E6%85%8B_%E6%B1%9A%E6%9F%93%E7%8E%87.csv"

# フォントファイルのパスを設定
font_path = 'NotoSansCJKjp-Regular.otf'  # プロジェクトディレクトリ内のフォントファイルを指定

# Streamlit のアプリケーション
st.title('食中毒細菌の検体数の統計まとめ')
st.write('食中毒細菌汚染実態_汚染率.csvの可視化です。')
st.write('表の右上に表示されるボタンから、表をcsvファイルとしてダウンロードできます。')
st.write('-----------')

# フォントの設定
fm.fontManager.addfont(font_path)
font_prop = fm.FontProperties(fname=font_path)
plt.rcParams['font.family'] = font_prop.get_name()

# データの読み込み
df = pd.read_csv(csv_url, encoding='utf-8-sig')

# 必要なカラムの欠損値を削除（仮に '検体数' というカラムが存在すると仮定）
df = df[df['検体数'].notna()]

# サイドバーで食品群を選択
food_groups = df['食品カテゴリ'].unique()  # ユニークな食品群を取得
selected_group = st.sidebar.selectbox('食品群を選択してください:', ['すべて'] + list(food_groups))

# 選択された食品群に基づいてデータをフィルタリング
if selected_group != 'すべて':
    df = df[df['食品カテゴリ'] == selected_group]

# 細菌ごとの検体数の合計を計算
bacteria_counts = df.groupby('細菌名')['検体数'].sum().reset_index()

# カラム名の変更
bacteria_counts.columns = ['バクテリア名', '検体数の合計']

# サイドバイサイドのレイアウト
col1, col2 = st.columns(2)

with col1:
    # テーブルの表示
    st.write('細菌毎の検体数の合計:')
    st.dataframe(bacteria_counts)

with col2:
    # 検体数の合計をグラフで可視化
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.barh(bacteria_counts['バクテリア名'], bacteria_counts['検体数の合計'], color='skyblue')
    
    # フォントサイズの調整
    ax.set_xlabel('検体数の合計', fontsize=18)
    ax.set_ylabel('細菌名', fontsize=18)
    ax.set_title('細菌毎の検体数の合計', fontsize=20)
    ax.tick_params(axis='both', which='major', labelsize=18)
    
    ax.invert_yaxis()  # バーを上から降順に表示
    
    # グラフを表示
    st.pyplot(fig)

st.write('-----------')
