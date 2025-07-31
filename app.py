# app.py
import streamlit as st
from prophet import Prophet
from utils.preprocess import load_and_process_data
from utils.generate_suggestion import generate_suggestion

st.set_page_config(page_title="🏨 飯店營運決策AI助理", layout="wide")

st.title("🏨 飯店營運決策 AI 助理")
st.markdown("預測入住率 ➜ 自動策略建議 ➜ 助你快速決策")

# 1️⃣ 讀取資料 + 快取
@st.cache_data
def get_data():
    return load_and_process_data()

df, prophet_df = get_data()

with st.expander("📄 查看最新原始資料"):
    st.dataframe(df.tail(10))

# 2️⃣ Prophet 預測
model = Prophet()
model.fit(prophet_df)
future = model.make_future_dataframe(periods=7)
forecast = model.predict(future)

st.subheader("📈 未來 7 天入住率預測")
st.line_chart(forecast[["ds", "yhat"]].set_index("ds"))

# 下載預測結果 CSV
forecast_7days = forecast[["ds", "yhat"]].tail(7)  # 只取未來 7 天
csv = forecast_7days.to_csv(index=False).encode('utf-8')
st.download_button(
    label="📥 下載未來 7 天預測結果 CSV",
    data=csv,
    file_name="hotel_forecast_7days.csv",
    mime="text/csv",
)

# 3️⃣ AI 決策建議
st.subheader("🤖 AI 決策建議")
user_question = st.text_input("請輸入問題（例如：今天入住率很低怎麼辦？）")
if user_question:
    suggestion = generate_suggestion(user_question)
    st.success(suggestion)
