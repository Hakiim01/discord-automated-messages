FROM python:3.14-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

RUN useradd --create-home --shell /usr/sbin/nologin appuser

COPY discord_auto_messaging/requirements.txt /tmp/requirements.txt

RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r /tmp/requirements.txt

COPY --chown=appuser:appuser discord_auto_messaging/ ./discord_auto_messaging/
COPY --chown=appuser:appuser data/ ./data/

USER appuser

CMD ["python", "-m", "discord_auto_messaging.cli"]