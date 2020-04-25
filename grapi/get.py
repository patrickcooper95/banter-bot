import requests

from grapi import config
import grapi.utils.logger as logger


def _get_url():
    """Return URL of specified type."""
    base = config.config['BASE_BOT_URL'].get()
    token = '?token=' + config.config['GROUPME_TOKEN'].get()
    return base + token


def get_all():
    """Send message to group."""

    try:
        response = requests.get(_get_url())
        logger.log_get(response.text)
    except requests.exceptions.RequestException as e:
        logger.log_get(e)

    return response
