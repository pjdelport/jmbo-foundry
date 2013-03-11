from urllib import urlretrieve
import dateutil.parser

from django.core.files import File

from social_auth.signals import pre_update
from social_auth.backends.facebook import FacebookBackend


def facebook_extra_values(sender, user, response, details, **kwargs):
    mapping = {
        'email': 'email',
        'first_name': 'first_name',
        'last_name': 'last_name', 
        'bio': 'about_me',
        'gender': 'gender',
        'birthday': 'dob'

    for key, fieldname in mapping.items():
        value = details.get(key, '')

        # Sanitize some fields
        if key == 'gender':
            if value:
                value = value[0]
        elif key == 'birthday':
            try:
                value = dateutil.parser.parse(value)
            except ValueError:
                value = None

        if value:
            setattr(user, fieldname, value)

    # Image
    username = details['username']
    url = 'http://graph.facebook.com/%s/picture' % username
    tempfile = urlretrieve(url)
    user.image.save('%s.jpg' % username, File(open(tempfile[0])))

    return True

pre_update.connect(facebook_extra_values, sender=FacebookBackend)
