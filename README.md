# IntelliDoc

An AI-powered document processing platform built for extraction of content and generating well-curated reports from them

## Phase 1: Backend Setup
- Flask app with file upload endpoint (`/upload`).
- Stores PDFs/images in `uploads/` folder.
- Saves metadata in SQLite database (`documents.db`).

## Setup
1. Clone the repo: `git clone https://github.com/Savant261/Intellidoc.git`
2. Install Python 3.9+ and create a virtual environment: `python -m venv venv`
3. Activate: `venv\Scripts\activate` (Windows) or `source venv/bin/activate` (Linux/macOS)
4. Install dependencies: `pip install -r requirements.txt`
5. Run: `python app.py`
6. Test upload: `curl -X POST -F "file=@/path/to/sample.pdf" http://localhost:5000/upload`
