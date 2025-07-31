import streamlit as st
import pandas as pd
from prophet import Prophet
from utils.preprocess import load_and_process_data
from utils.generate_suggestion import generate_suggestion
import altair as alt

st.set_page_config(page_title="🏨 飯店營運決策AI助理", layout="wide")

st.title("🏨 飯店營運決策 AI 助理")
st.markdown("預測入住率 ➜ 自動策略建議 ➜ 助你快速決策")

# 1️⃣ 讀取資料
df, prophet_df = load_and_process_data()

with st.expander("📄 查看最新原始資料"):
    st.dataframe(df.tail(10))

# 2️⃣ Prophet 預測
model = Prophet()
model.fit(prophet_df)
future = model.make_future_dataframe(periods=7)
forecast = model.predict(future)

# 取最後 7 天
forecast_7days = forecast.tail(7).copy()
forecast_7days["入住率(%)"] = (forecast_7days["yhat"] * 100).round(2)
forecast_7days["日期"] = pd.to_datetime(forecast_7days["ds"]).dt.strftime("%Y-%m-%d")
forecast_7days = forecast_7days[["日期", "入住率(%)"]]

# 3️⃣ 折線圖
st.subheader("📉 未來 7 天入住率預測")

# 設定要標示的日期
highlight_date = "2024-12-22"

# 折線圖
line_chart = alt.Chart(forecast_7days).mark_line(point=True).encode(
    x=alt.X('日期:T', title='日期'),
    y=alt.Y('入住率(%)', title='入住率 (%)'),
    tooltip=['日期', '入住率(%)']
).properties(width=700, height=300)

# 只在指定日期標註文字
highlight_text = alt.Chart(forecast_7days[forecast_7days["日期"] == highlight_date]).mark_text(
    align='left', dx=5, dy=-10
).encode(
    x='日期:T',
    y='入住率(%)',
    text='入住率(%)'
)

# 疊加圖表
st.altair_chart(line_chart + highlight_text, use_container_width=True)

# 4️⃣ 表格顯示
st.dataframe(forecast_7days, hide_index=True)

# 5️⃣ AI 決策建議
st.subheader("🤖 AI 決策建議")
user_question = st.text_input("請輸入問題（例如：今天入住率很低怎麼辦？）")
if user_question:
    suggestion = generate_suggestion(user_question)
    st.success(suggestion)
