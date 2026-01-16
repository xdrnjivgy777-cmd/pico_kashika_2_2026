import streamlit as st
import matplotlib.pyplot as plt

# 确保字体设置
plt.rcParams['font.family'] = 'Meiryo'

st.subheader('確率分布の実験')

# 方式 1：使用 st.markdown
st.markdown("### 正規分布")
st.markdown("母数（パラメータ）を変化させたときのグラフの変化の確認")

# 方式 2：使用 st.write
st.write("确认显示：グラフ")

# 方式 3：Matplotlib 内部显示
fig, ax = plt.subplots()
ax.set_title("グラフのタイトル (Graph Title)")
st.pyplot(fig)