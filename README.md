# Voting System

A simple **voting application** built with **FastAPI (backend), MongoDB (database), and Streamlit (frontend)**. Users can vote for candidates and view real-time results.

## Project Structure

```
voting_app/
│── backend/
│   │── main.py            # FastAPI backend
│   │── database.py        # MongoDB connection
│   │── models.py          # Pydantic models
│   │── crud.py            # CRUD operations
│
│── frontend/
│   │── app.py             # Streamlit UI
│
│── requirements.txt       # Required dependencies
│── README.md              # Project documentation
```

---

## Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/voting-app.git
cd voting-app
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Start MongoDB

Ensure that MongoDB is running locally or update the connection string in `database.py`.

### 4. Start the Backend (FastAPI)

```bash
uvicorn backend.main:app --reload
```

The FastAPI backend will be available at: **`http://127.0.0.1:8000`**

### 5. Start the Frontend (Streamlit)

```bash
streamlit run frontend/app.py
```

The Streamlit UI will be available at: **`http://localhost:8501`**

---

## API Endpoints

### Submit a Vote

**Endpoint:** `POST /vote/`
**Payload:**

```json
{
  "candidate": "Alice"
}
```

**Response:**

```json
{
  "message": "Vote submitted!"
}
```

### Get Voting Results

**Endpoint:** `GET /results/`
**Response Example:**

```json
{
  "Alice": 5,
  "Bob": 3,
  "Charlie": 7
}
```

---

## Features

✅ Vote for a candidate\
✅ View real-time voting results\
✅ Simple UI with Streamlit\
✅ FastAPI for backend\
✅ MongoDB for database storage

---

## Future Improvements

- ✅ User authentication for secure voting
- ✅ IP tracking to prevent multiple votes
- ✅ Deploy on cloud (e.g., AWS, Heroku)

---

## License

This project is licensed under the MIT License.

---

### ✨ Happy Voting! 🚀

