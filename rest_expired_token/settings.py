from django.conf import settings


SETTINGS_KEY = 'TOKEN_AUTHENTICATION'
DEFAULTS = {
    'is_expired': False,
    'expiration_time': 30
}


class APISettings(object):

    def __init__(self, user_settings=None, defaults=None):
        self.user_settings = user_settings or {}
        self.defaults = defaults or {}

    def __getattr__(self, attr):
        if attr not in self.defaults.keys():
            raise AttributeError("Invalid API setting: '%s'" % attr)

        val = self.defaults[attr]
        if attr in self.user_settings.keys():
            val = self.user_settings[attr]

        # Cache the result
        setattr(self, attr, val)
        return val


USER_SETTINGS = getattr(settings, SETTINGS_KEY, None)
api_settings = APISettings(USER_SETTINGS, DEFAULTS)
