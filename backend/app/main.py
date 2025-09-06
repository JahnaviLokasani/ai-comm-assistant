import os
import pandas as pd
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Always use local CSV inside backend folder
BASE_DIR = os.path.dirname(__file__)
EMAIL_CSV_PATH = os.path.join(BASE_DIR, "..", "sample_emails.csv")

try:
    emails_df = pd.read_csv(EMAIL_CSV_PATH)
    print(f"✅ Loaded dataset from {EMAIL_CSV_PATH}, rows={len(emails_df)}")
    print("📌 Columns:", emails_df.columns.tolist())
except Exception as e:
    emails_df = pd.DataFrame()
    print(f"⚠️ Could not load dataset: {e}")

@app.get("/emails")
def get_emails():
    return emails_df.to_dict(orient="records")
