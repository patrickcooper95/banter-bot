import csv
import datetime

import birthday_wishes as bw
import grapi.post as post

birthdays = dict()
birthday_is_today = list()
YEAR = datetime.date.today().year

# Test
BOT_ID = ""

num_birthdays = 0


# Read csv file of birthdays into DictReader object
with open('birthdays.csv') as csvfile:
    bdays = csv.DictReader(csvfile)
    for row in bdays:
        # Move K/V pairs from DictReader to Python dict
        birthdays.update({row['Name']: row['Birthday']})


# Test if birthday was today
# birthdays['Name'] = "xx/xx/xx"

# TODO: Update this to use Python logger.
def log_run(msg, inc_date=False):
    """Add message post to log file."""
    with open('bot-log.txt', 'a') as file:
        if inc_date:
            file.write("\n" + msg + " - " + str(datetime.datetime.utcnow()))
        else:
            file.write("\n" + msg)


def check_date(birthday):
    """Compare birthday in list of birthdays to today's date.
        :return True, if today is a birthday."""
    bday_list = birthday.split('/')
    bday_result = datetime.date.today() - datetime.date(YEAR, int(bday_list[0]), int(bday_list[1]))
    if bday_result.days == 0:
        return True
    else:
        return False


log_run("\nRUNNING BIRTHDAY-BOT", inc_date=True)

for key, value in birthdays.items():
    today_is_a_birthday = check_date(value)
    if today_is_a_birthday:
        birthday_is_today.append(key)
        num_birthdays += 1


def birthday_fmt_string():
    """Creates a dynamic string, adjusted to the number of birthdays for the day."""
    if num_birthdays == 1:
        return birthday_is_today[0]

    elif num_birthdays == 2:
        bday_string = ""
        for b in birthday_is_today:
            if len(bday_string) == 0:
                bday_string = b
            else:
                bday_string = bday_string + " and " + b

        return bday_string

    elif num_birthdays > 2:
        bday_string = ""
        for b in birthday_is_today:
            if b == birthday_is_today[-1]:
                bday_string = bday_string + ", and " + b
            elif b == birthday_is_today[0]:
                bday_string = b
            else:
                bday_string = bday_string + ", " + b

        return bday_string


if len(birthday_is_today) > 0:
    log_run("### Birthday(s) noted today")
    bday_names = birthday_fmt_string()
    message = "Happy Birthday {name}! {birthday_wish}".format(name=bday_names,
                                                                 birthday_wish=bw.select_birthday_wish())
    post.post_message(message, BOT_ID)
    log_run("### Birthday message passed to GRAPI")
    log_run("### Run complete", inc_date=True)

else:
    log_run("### No birthdays today. Birthday-bot, signing off. ###")
    log_run("### Run complete", inc_date=True)
