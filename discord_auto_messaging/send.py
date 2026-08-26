import requests
import json

webhook_url = "https://discord.com/api/webhooks/1542280440361123850/Bxawt8hy7eyLePNpWLnUeNZKBv1gHTnCrswDAL9YjNXEeiJZWgj-6ofx93zJHB53bB7N"

def send_discord_message(webhook_url, message_content):
    """
    Sends a message to a Discord channel using a webhook URL.

    Parameters:
    - webhook_url (str): The Discord webhook URL.
    - message_content (str): The content of the message to send.

    Returns:
    - bool: True if the message was sent successfully, False otherwise.
    """
    data = {
        "content": message_content
    }

    headers = {
        "Content-Type": "application/json"
    }

    response = requests.post(webhook_url, data=json.dumps(data), headers=headers)

    if response.status_code == 204:
        print("Message sent successfully!")
        return True
    else:
        print(f"Failed to send message. Status code: {response.status_code}")
        print(response.text)
        return False
