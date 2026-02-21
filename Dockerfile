FROM python:3.10-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    libgl1 \
    libglib2.0-0 \
    curl \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Install uv
RUN pip install uv

# Copy requirements
COPY requirements.txt .

# --- NETWORK SETTINGS ---
ENV UV_HTTP_TIMEOUT=3600
ENV UV_CONCURRENT_DOWNLOADS=1

# --- CPU-ONLY PYTORCH ---
RUN uv pip install --system --no-cache \
    "torch>=2.0.0" \
    "torchvision>=0.15.0" \
    --index-url https://download.pytorch.org/whl/cpu

# --- INSTALL REMAINING REQUIREMENTS ---
RUN uv pip install --system --no-cache -r requirements.txt

# Copy application
COPY . .

EXPOSE 8501

# --- FIX: USE PYTHON -M STREAMLIT ---
# This avoids the "executable file not found" error by asking Python to run the module directly
HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

ENTRYPOINT ["python", "-m", "streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]