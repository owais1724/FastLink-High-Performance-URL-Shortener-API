# FastLink-High-Performance-URL-Shortener-API

FastLink is a lightweight, high-performance URL Shortener API built using FastAPI.
It allows users to convert long URLs into short links and seamlessly redirect back to the original URL.

✨ Features

⚡ Fast and lightweight (FastAPI powered)

🔗 Shortens long URLs into compact links

🚀 Automatic redirection using short codes

📘 Interactive Swagger API documentation

🧠 In-memory storage (easy to extend to DB)

🛠 Simple and clean project structure

🏗️ Tech Stack

Backend: FastAPI

Language: Python 3.9+

Server: Uvicorn

Validation: Pydantic

📂 Project Structure
url-shortner/
│
├── main.py          # Main FastAPI application
├── README.md        # Project documentation
└── requirements.txt

▶️ How to Run the Project

1️⃣ Clone the repository

git clone <your-repo-url>
cd url-shortner

2️⃣ Install dependencies

pip install fastapi uvicorn

3️⃣ Run the server

uvicorn main:app --reload

🌐 API Documentation

Once the server is running, open:

http://127.0.0.1:8000/docs


You’ll get an interactive Swagger UI to test the API.

🔧 API Endpoints
🔹 Shorten a URL

POST /shorten

Request Body

{
  "long_url": "https://www.google.com"
}


Response

{
  "short_url": "http://127.0.0.1:8000/aB3xZ9",
  "original_url": "https://www.google.com"
}

🔹 Redirect to Original URL

GET /{short_code}

Example:

http://127.0.0.1:8000/aB3xZ9


➡️ Redirects to the original long URL.

🧪 Example Workflow

Go to /docs

Use POST /shorten to generate a short URL

Copy the short URL

Paste it in the browser

Get redirected 🎉

🚧 Future Enhancements

🗄️ Database support (SQLite / MongoDB)

⏳ URL expiry feature

🔐 Authentication & rate limiting

🎨 Frontend UI

☁️ Cloud deployment (AWS / Render / Railway)

👨‍💻 Author

Syed Owais Mohiuddin

AI & ML | Backend | FastAPI | Python

📜 License

This project is open-source and free to use for learning and development.
