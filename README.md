# Automated Threat Intelligence & Forensics Agent (ATIF)

An automated forensic analysis and threat intelligence platform powered by LangGraph, FastAPI, and specialized forensic tools. This agent-based system automates the process of artifact collection, malware scanning, and forensic synthesis.

## 🚀 Features

- **Automated Workflow**: Uses LangGraph to orchestrate a multi-step forensic analysis process.
- **YARA Scanning**: Integrated malware detection using custom YARA rules.
- **Registry Parsing**: Automated Windows Registry analysis using `regipy`.
- **Intelligent Synthesis**: AI-driven analysis of raw artifacts to generate human-readable forensic reports.
- **Caching & Persistence**: MongoDB integration for caching analysis results and maintaining an audit trail.
- **RESTful API**: FastAPI-based endpoints for file submission and report retrieval.

## 🏗️ Architecture

The system operates as a stateful graph:
1.  **Entry**: File is uploaded and hashed.
2.  **Tool Selection**: The Router node determines which forensic tools to run.
3.  **Execution**: YARA scanner and Registry parser extract artifacts.
4.  **Synthesis**: An LLM agent summarizes the findings into a forensic report.
5.  **Persistence**: Results are stored in MongoDB.

## 🛠️ Setup

### Prerequisites
- Python 3.9+
- MongoDB
- Google Gemini API Key (for LangChain integration)

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/JVAISAG/Automated-Threat-Intelligence-Forensics-Agent-.git
   cd Automated-Threat-Intelligence-Forensics-Agent-
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables:**
   Create a `.env` file in the root directory:
   ```env
   PROJECT_NAME="ATIF Agent"
   MONGODB_URL="mongodb://localhost:27017"
   DATABASE_NAME="atif_db"
   GOOGLE_API_KEY="your_gemini_api_key_here"
   ```

## 🖥️ Usage

### Start the Application
```bash
python -m app.main
```
The API will be available at `http://localhost:8000`.

### Analyze a File
```bash
curl -X POST "http://localhost:8000/api/v1/forensics/analyze" \
     -H "accept: application/json" \
     -H "Content-Type: multipart/form-data" \
     -F "file=@path/to/your/file"
```

## 📂 Project Structure

- `app/`
  - `agents/`: LangGraph workflow and node definitions.
  - `api/`: FastAPI routes and endpoints.
  - `core/`: Configuration and database connection logic.
  - `models/`: Pydantic models for data validation.
  - `services/`: Core business logic (file handling).
  - `tools/`: Forensic scanning tools (YARA, Registry).
- `rules/`: Storage for `.yar` malware detection rules.

## 🛡️ License
Distributed under the MIT License.
