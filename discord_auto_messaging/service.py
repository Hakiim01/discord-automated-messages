import random
import time

from discord_auto_messaging.utils import get_logger
from discord_auto_messaging.send import send_discord_message


def random_line(path: str) -> str:
    with open(path, encoding="utf-8") as messages_file:
        lines = [line.strip() for line in messages_file if line.strip()]

    if not lines:
        raise ValueError(f"No non-empty messages in {path}")

    return random.choice(lines)


class DiscordMessageService:
    def __init__(self, webhook_url: str, file_path: str, interval_seconds: int = 3600):
        self.webhook_url = webhook_url
        self.file_path = file_path
        self.interval_seconds = interval_seconds
        self.logger = get_logger(__name__)

    def start_sending(self):
        self.logger.info(
            "Starting Discord message service; interval=%s seconds",
            self.interval_seconds,
        )

        while True:
            try:
                message = random_line(self.file_path)
                success = send_discord_message(self.webhook_url, message)

                if success:
                    self.logger.info("Sent one Discord message.")
                else:
                    self.logger.error("Discord rejected or failed to accept the message.")

            except Exception:
                self.logger.exception("Message cycle failed.")

            time.sleep(self.interval_seconds)