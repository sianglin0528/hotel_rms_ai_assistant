# 🏨 Hotel RMS AI Assistant

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-Framework-red?logo=streamlit)
![Prophet](https://img.shields.io/badge/Facebook-Prophet-green)
![SQLite](https://img.shields.io/badge/Database-SQLite-lightgrey?logo=sqlite)
![Status](https://img.shields.io/badge/Status-Prototype-yellow)

AI 驅動的飯店營運決策助理  
透過歷史數據預測入住率、分析價格策略，並提供自動化決策建議，協助飯店經理人做出更精準的營運決策。

---

## 🌟 專案特色
- **ETL 資料處理**：每日營運資料清洗 ➜ SQLite 儲存  
- **時間序列預測**：使用 Facebook Prophet 預測未來入住率  
- **動態策略建議**：根據入住率與價格生成營運建議  
- **可視化介面**：Streamlit 儀表板即時查看報表  
- **RAG 問答助理**：結合 ChatGPT API，即問即答  

---

## 📊 系統流程圖

```mermaid
flowchart LR
    A[每日營運資料] --> B[ETL_清理_存入_SQLite]
    B --> C[Prophet_預測入住率]
    C --> D[動態策略建議生成]
    D --> E[Streamlit_儀表板]
    E --> F[RAG_問答助理_ChatGPT_API]
    F --> G[飯店經理決策]


📂 專案結構

hotel_rms_ai_assistant/
├─ data/                # 資料夾 (SQLite DB & CSV)
│   ├─ hotel_data.db     # 資料庫
│   └─ sample_data.csv   # 範例資料
├─ utils/               # 資料前處理 & 建議產生函數
│   └─ preprocess.py
├─ app.py                # Streamlit 主程式
├─ etl_pipeline.py       # 每日資料 ETL 與更新 DB
├─ requirements.txt      # 依賴套件
└─ README.md


⚡ 安裝與執行
1️⃣ 下載專案
git clone https://github.com/sianglin0528/hotel_rms_ai_assistant.git
cd hotel_rms_ai_assistant
2️⃣ 安裝
pip install -r requirements.txt
3️⃣ 初始化資料
python etl_pipeline.py
4️⃣ 啟動前端
streamlit run app.py
