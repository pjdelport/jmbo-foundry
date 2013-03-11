from django.contrib.sites.models import get_current_site
from django.conf import settings

from preferences import preferences

def foundry(request):
    return {
        'FOUNDRY': settings.FOUNDRY,
        'LAYER_PATH': settings.FOUNDRY['layers'][0] + '/',
        'CURRENT_SITE': get_current_site(request),
        'ANALYTICS_TAGS': preferences.GeneralPreferences.analytics_tags,
        'SITE_DESCRIPTION': preferences.GeneralPreferences.site_description,
        'FOUNDRY_HAS_FACEBOOK_CONNECT': getattr(settings, 'FACEBOOK_APP_ID', '') != '',
        'FOUNDRY_HAS_TWITTER_OAUTH': getattr(settings, 'TWITTER_CONSUMER_KEY', '') != '',
    }
