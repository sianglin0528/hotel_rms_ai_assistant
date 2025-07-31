def generate_suggestion(question):
    # 簡單模擬AI回覆，可之後接OpenAI API或RAG
    if "低" in question:
        return "建議推出促銷方案或增加OTA廣告投放"
    elif "高" in question:
        return "建議調整價格提高收益，同時保持客戶體驗"
    else:
        return "根據當前數據，建議保持現有策略並持續觀察"
