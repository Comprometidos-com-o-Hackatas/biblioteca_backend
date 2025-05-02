FROM python:3.12

WORKDIR /app

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1


RUN apt-get update && \
    apt-get install -y build-essential curl && \
    rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip && pip install pdm

COPY pyproject.toml pdm.lock* /app/
COPY README.md /app/README.md

RUN pdm install

COPY . /app

EXPOSE 8001

COPY start.sh /app/start.sh
RUN chmod +x /app/start.sh
CMD ["/app/start.sh"]