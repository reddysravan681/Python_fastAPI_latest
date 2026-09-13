# Python API - FastAPI & MySQL

A RESTful API built with **FastAPI** and **PyMySQL**, using raw SQL queries (no SQLAlchemy — yet).

## Branches

| Branch                | Description                                                        |
| --------------------- | ------------------------------------------------------------------ |
| `main`                | Current working version using raw PyMySQL queries (no ORM).        |
| `sqlalchemy-integration` | In-progress: integrating SQLAlchemy models and database session. |

## Tech Stack

- **Python 3** + [FastAPI](https://fastapi.tiangolo.com/)
- **PyMySQL** for direct MySQL access
- **Pydantic** for request validation and schemas
- **Uvicorn** as the ASGI server

## Project Structure

```
Python_API_FCC/
├── app/
│   ├── main.py        # FastAPI app + all endpoints
│   ├── schemas.py     # Pydantic models (Post)
│   └── sql_conn.py    # MySQL connection + cursor (raw PyMySQL)
├── requirements.txt
├── .env               # Database credentials (NOT committed)
└── .gitignore
```

## Getting Started

### 1. Prerequisites

- Python 3.8+
- MySQL running locally with a `fastapi` database

### 2. Clone & setup

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO.git
cd Python_API_FCC
python -m venv .venv
.\.venv\Scripts\pip install -r requirements.txt
```

### 3. Configure environment variables

Create a `.env` file in the project root:

```
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=your_password
DB_DATABASE=fastapi
```

### 4. Create the table

The API expects a `posts` table in the `fastapi` database:

```sql
CREATE TABLE posts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    content TEXT,
    published BOOLEAN DEFAULT TRUE
);
```

### 5. Run the server

```bash
.\.venv\Scripts\uvicorn app.main:app --reload
```

Server starts at `http://127.0.0.1:8000`. Interactive docs at `http://127.0.0.1:8000/docs`.

## API Endpoints

| Method | Path            | Description                          |
| ------ | --------------- | ------------------------------------ |
| GET    | `/`             | Welcome message                      |
| GET    | `/posts`        | Get all posts                        |
| GET    | `/posts/{id}`   | Get a single post by ID              |
| POST   | `/create_posts` | Create a new post (201 on success)   |
| PUT    | `/posts/{id}`   | Update a post's title and content    |
| DELETE | `/posts/{id}`   | Delete a post by ID (204 on success) |

### Sample POST body (`/create_posts`)

```json
{
  "title": "Hello world",
  "content": "My first post",
  "published": true
}
```

`title` is required; `content` defaults to `"content"` and `published` defaults to `true`.

## Roadmap

- [ ] Integrate SQLAlchemy (models + session) on the `sqlalchemy-integration` branch
- [ ] Replace raw SQL queries with ORM operations
- [ ] Add automated tests

## License

MIT