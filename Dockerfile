# Temel Python imajını kullanıyoruz
FROM python:3.10-slim
# Uv ve uvx'i resmi imajdan kopyalıyoruz
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/
# Çalışma dizinini oluşturuyoruz ve konteynerın içine geçiyoruz
WORKDIR /app
# Uygulamanın çalışması için gerekli olan sistem kütüphanelerini yüklüyoruz
RUN apt-get update && apt-get install -y --no-install-recommends \
    libgomp1 \
    && rm -rf /var/lib/apt/lists/*
# Uygulama için gerekli dosyaları konteynera kopyalıyoruz
COPY pyproject.toml uv.lock ./
# Bağımlılıkları yüklemek için uv kullanıyoruz
RUN uv sync --frozen --no-dev
# Model dosyasını ve uygulama kodunu konteynera kopyalıyoruz
COPY lightgbm_model.pkl main.py ./
# Uygulamanın çalışacağı portu açıyoruz
EXPOSE 8000
# Uvicorn'u kullanarak FastAPI uygulamasını başlatıyoruz
CMD ["uv", "run", "--no-dev", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]