# AI-Powered Communication Assistant — Starter (Full-stack)

This is a hackathon-ready starter project: a minimal **FastAPI** backend and a simple **React** frontend.
It implements:
- CSV email loader and filter (support-related subjects)
- Simple extraction (phones, emails), sentiment heuristic, priority detection
- Priority ordered API endpoint
- Mock LLM reply generation endpoint
- Minimal React dashboard to view prioritized emails, generate & edit replies, and mark as resolved

## How to use
1. Backend
   ```
   cd backend
   python -m venv venv
   source venv/bin/activate     # Windows: venv\Scripts\activate
   pip install -r requirements.txt
   uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
   ```
2. Frontend (requires Node.js & npm/yarn)
   ```
   cd frontend
   npm install
   npm start
   ```
3. Open frontend: http://localhost:3000

## Notes
- The backend reads the provided sample CSV by default from `/mnt/data/68b1acd44f393_Sample_Support_Emails_Dataset.csv`.
- Replace mock reply generator with OpenAI/HuggingFace calls in `backend/app/main.py` when you're ready.

## Repo structure
See `backend/` and `frontend/` directories.
