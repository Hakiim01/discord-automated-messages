import os
from discord_auto_messaging.service import DiscordMessageService


def main():
    webhook_url = os.environ["DISCORD_WEBHOOK_URL"]

    service = DiscordMessageService(
        webhook_url=webhook_url,
        file_path=os.environ["FILE_PATH"],
        interval_seconds=3600*int(os.environ["INTERVAL_HOURS"]),
    )
    service.start_sending()


if __name__ == "__main__":
    main()