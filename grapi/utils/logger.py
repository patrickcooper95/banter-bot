import datetime


def log_message(msg, bot, resp):
    """Add message post to log file."""
    with open('/Path/to/logs', 'a') as file:
        file.write('\nPOST: message: ' + msg + ', bot: ' + bot + ', result: ' + resp + ', ' +
                   str(datetime.datetime.utcnow()))


def log_bot_create(name, grp, resp):
    """Add bot create post to log file."""
    with open('/Path/to/logs', 'a') as file:
        file.write('\nPOST: bot_name: ' + name + ', group: ' + grp +
                   ', response: ' + resp + ', ' + str(datetime.datetime.utcnow()))


def log_delete(bot, resp):
    """Add bot delete to log file."""
    with open('/Path/to/logs', 'a') as file:
        file.write('\nDELETE: bot_name: ' + bot + ', response: ' + resp + ', ' + str(datetime.datetime.utcnow()))


def log_get(resp):
    """Add bot get to log file."""
    with open('/Path/to/logs', 'a') as file:
        file.write('\nGET: response: ' + resp + ', ' + str(datetime.datetime.utcnow()))
