# python main dependency on the project
FROM python:3.11-slim

# use uv for the venv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# copy my code
WORKDIR /app

# pull the requirement
COPY requirement.txt .

# run the requirement file
RUN uv pip install --system --no-cache -r requirement.txt

# copy my code
COPY . .

# expose the port forthe final runnign file 
EXPOSE 8501

# how to run app.py
CMD ["streamlit", "run", "app.py", "--server.address=0.0.0.0", "--server.port=8501"]





