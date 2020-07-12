# Banter-Bot: A GroupMe bot

## Description
Using the GroupMe API and your personal developer's token (which you can get here: https://dev.groupme.com/), Banter-Bot posts a select birthday wish for each member
of your desired group, on his/her respective birthdays.

## Getting Started
Insert your token in `configs.yaml`, create a bot using GroupMe's POST endpoint and then add the BOT name and BOT ID to `configs.yaml`. Next, add entries to `birthdays.csv` for
your group members. Finally, using a system scheduler such as `cron`, you can schedule your bot to run daily at a specified time. If a birthday from `birthdays.csv` matches the
current date, Banter-Bot will wish the lucky individual a happy birthday!
