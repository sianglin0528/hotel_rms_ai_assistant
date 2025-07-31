import streamlit as st
import pandas as pd
from prophet import Prophet
from utils.preprocess import load_and_process_data
from utils.generate_suggestion import generate_suggestion

st.set_page_config(page_title="🏨 飯店營運決策AI助理", layout="wide")
st.title("🏨 飯店營運決策 AI 助理")
st.markdown("預測入住率 ➜ 自動策略建議 ➜ 助你快速決策")

# 1️⃣ 載入資料
df, prophet_df = load_and_process_data()

with st.expander("📄 查看最新原始資料"):
    st.dataframe(df.tail(10))

# 2️⃣ Prophet 建模與預測
model = Prophet()
model.fit(prophet_df)
future = model.make_future_dataframe(periods=7)
forecast = model.predict(future)

# 取出最後 7 天預測，並格式化日期
forecast_week = forecast[["ds", "yhat"]].tail(7)
forecast_week.columns = ["日期", "預測入住率"]
forecast_week["日期"] = pd.to_datetime(forecast_week["日期"]).dt.strftime("%Y-%m-%d")

st.subheader("📈 未來 7 天入住率預測")
st.line_chart(forecast_week.set_index("日期")["預測入住率"])
st.dataframe(forecast_week)

# 3️⃣ AI 決策建議
st.subheader("💡 AI 決策建議")
user_question = st.text_input("請輸入問題（例如：今天入住率很低怎麼辦？）")
if user_question:
    suggestion = generate_suggestion(user_question)
    st.success(suggestion)
