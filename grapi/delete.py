import requests

from grapi import config
import grapi.utils.logger as logger


def get_url():
    """Return Destroy Bot URL."""
    base = config.config['DESTROY_BOT_URL'].get()
    token = '?token=' + config.config['GROUPME_TOKEN'].get()
    return base + token


def delete_bot(bot):
    """Delete specified bot."""

    body = {
        'bot_id': bot,
    }

    try:
        response = requests.post(get_url(), json=body)
        logger.log_delete(bot, str(response.status_code))
    except requests.exceptions.RequestException as e:
        logger.log_delete(bot, e)
