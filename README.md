# FastAPI Server Setup

This guide will help you set up and run a FastAPI server.

## Prerequisites

- Python 3.7 or higher
- `pip` (Python package installer)

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/danieltonad/niyo-grp-backend-assesment
cd niyo-grp-backend-assesment
```

### 2. Create a Virtual Environment

Create a virtual environment to manage dependencies.

```bash
python -m venv env
```

### 3. Activate the Virtual Environment

- On **Windows**:

  ```bash
  .\env\Scripts\activate
  ```

- On **macOS** and **Linux**:

  ```bash
  source env/bin/activate
  ```

### 4. Install Dependencies

Install the required dependencies from `requirements.txt`.

```bash
pip install -r requirements.txt
```

### 5. Start the Uvicorn Server

Run the FastAPI application using Uvicorn.

```bash
uvicorn main:app --reload
```

- `main` is the Python file that contains your FastAPI app.
- `app` is the FastAPI instance inside the `main.py` file.
- The `--reload` flag will auto-reload the server when you make changes to the code.

### 6. Access the API

Open your web browser and go to `http://127.0.0.1:8000` to see your FastAPI application in action.

### 7. API Documentation

FastAPI automatically generates interactive API documentation:

- **Swagger UI**: `http://127.0.0.1:8000/docs`
- **ReDoc**: `http://127.0.0.1:8000/redoc`

## Additional Commands

### Deactivate the Virtual Environment

When you're done, deactivate the virtual environment.

```bash
deactivate
```

## Troubleshooting

If you encounter any issues, here are a few common solutions:

- Ensure you have the correct version of Python installed.
- Verify that all required dependencies are installed.
- Check for typos in file names and paths.

For more information, refer to the [FastAPI documentation](https://fastapi.tiangolo.com/).

## License

This project is licensed under the MIT License.
```