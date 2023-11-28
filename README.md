# Battery percent

Checks current battery percentage, sends telegram message if percent is lower than 20\
You need to have telegram ```bot_key``` and ```chat_id``` in .env file. See .env.example\
This script is useful if added to cron. For example: ```* * * * * python '<path>/main.py'```