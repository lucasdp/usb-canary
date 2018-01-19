import sys
import canary.settings
import telepot

def load_telegram_settings():

    telegram_settings = canary.settings.open_settings()

    telegram = telegram_settings['settings']['telegram']

    try:
        # sanity check that the user has actually supplied data
        if not telegram['token']:
            print('Error 80: Telegram token has been left blank')
            sys.exit(80)
        elif not telegram['chat_id']:
            print('Error 81: Telegram chat_id has been left blank')
            sys.exit(81)
        else:
            return telegram
    except KeyError:
        print('Error 90: Telegram config missing in the settings file')
        sys.exit(90)