# Learning Management System Backend - Proof of Concept

## 📋 Overview
A FastAPI-based backend system for educational institutions featuring:
- **Student Performance API** with score, attendance, and behavior tracking
- **Transaction Reporting** with date, class, and payment type filters
- **Voice Query Processing** for natural language commands
- **Sample Data Integration** for proof of concept demonstration

## 🏗 Architecture
```
Frontend ──► FastAPI Backend ──► PostgreSQL Database
                    │
                ML Models (scikit-learn)
```

## 📁 Project Structure
```
/Report-gene-and-predictive-analysis
├── app/
│   ├── main.py              # FastAPI entry point
│   ├── models.py            # Database models
│   ├── database.py          # DB configuration
│   ├── routes/              # API endpoints
│   │   ├── students.py      # Student APIs
│   │   ├── transactions.py  # Transaction APIs
│   │   └── voice.py         # Voice processing
│   └── ml/model.py          # ML predictions
├── data/                    # Sample CSV data
├── Dockerfile
├── docker-compose.yml
└── requirements.txt
```

## 🚀 Quick Start

### Using Docker (Recommended)
```bash
git clone <repository-url>
cd Report-gene-and-predictive-analysis
docker-compose up --build
```

### Local Development
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python run.py
```

**Access:** `http://localhost:8000/docs`

## 📚 Key API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/students/performance` | GET | Student analytics (score, attendance, behavior) |
| `/transactions/report` | GET | Financial reports with filters |
| `/voice/interpret` | POST | Process voice commands |

### Example Usage
```bash
# Get all student performance data
curl -X GET "http://localhost:8000/students/performance"

# Get filtered transaction report
curl -X GET "http://localhost:8000/transactions/report?date=2023-01-15&class_type=Science&payment_type=Tuition"

# Process voice command
curl -X POST "http://localhost:8000/voice/interpret" \
     -H "Content-Type: application/json" \
     -d '{"text": "show student performance"}'
```

### Sample Responses
**Student Performance:**
```json
[
  {
    "name": "John Doe",
    "score": 85,
    "attendance": 95,
    "behavior": "Good",
    "remarks": "Good"
  }
]
```

**Transaction Report:**
```json
[
  {
    "transaction_id": 1,
    "student_id": 1,
    "date": "2023-01-15",
    "class_type": "Science",
    "payment_type": "Tuition",
    "amount": 500
  }
]
```

## 🤖 ML Features
- **Performance Prediction**: Random Forest model using scores, attendance, behavior
- **Dropout Risk**: Logistic regression with confidence scoring
- **Revenue Forecasting**: Time-series analysis for financial planning

## 🎤 Voice Commands
Supports natural language queries with simple keyword matching:
- **Student Performance**: "show student performance", "student data"
- **Transaction Reports**: "transaction report", "financial data"
- **General Queries**: Currently returns helpful message if query not recognized

## 🔧 Tech Stack
- **Backend**: FastAPI, SQLAlchemy, PostgreSQL
- **ML**: scikit-learn, pandas, numpy
- **Auth**: JWT tokens with role-based access
- **Deployment**: Docker, Docker Compose

## 🚀 Future Enhancements
- [ ] LangChain integration for LLM queries
- [ ] Real-time analytics dashboard
- [ ] Advanced anomaly detection
- [ ] Webhook automation system

---
**Built for educational institutions seeking data-driven insights** <br>
**Kartik Singh (22B0692)**
