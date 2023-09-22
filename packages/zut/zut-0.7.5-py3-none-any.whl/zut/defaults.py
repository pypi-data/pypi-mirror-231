import locale

def enable_default_locale():
    return locale.setlocale(locale.LC_ALL, '')
