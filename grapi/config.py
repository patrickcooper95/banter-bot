import os

import confuse

# Set ENV variable for config search
os.environ['BANTER_BOTDIR'] = '/Path/to/banter-bot/grapi/'

# Load in config object
config = confuse.Configuration('banter_bot')
