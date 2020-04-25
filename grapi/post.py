import requests

from grapi import config
import grapi.utils.logger as logger


def _get_url(req_type):
    """Return URL of specified type."""
    if req_type == 'message':
        return config.config['MESSAGE_URL'].get()
    elif req_type == 'bot':
        base = config.config['BASE_BOT_URL'].get()
        token = '?token=' + config.config['GROUPME_TOKEN'].get()
        return base + token


def post_message(message, bot):
    """Send message to group."""

    body = {
        'bot_id': bot,
        'text': message
    }

    try:
        response = requests.post(_get_url('message'), json=body)
        logger.log_message(message, bot, str(response.status_code))
    except requests.exceptions.RequestException as e:
        logger.log_message(message, bot, e)


def create_bot(group, name, avatar_url=None, callback_url=None):
    """Create bot in specified group."""
    body = {"bot":
                {
                    "name": name,
                    "group_id": group,
                    "callback_url": callback_url,
                    "avatar_url": avatar_url,
                }
    }
    try:
        response = requests.post(_get_url('bot'), json=body)
        logger.log_bot_create(name, group, str(response.text))
    except requests.exceptions.RequestException as e:
        logger.log_bot_create(name, group, e)
