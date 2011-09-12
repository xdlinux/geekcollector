import os
import sys

sys.path.append('/srv/')
sys.path.append('/srv/xdlinux/')

os.environ['DJANGO_SETTINGS_MODULE'] = 'xdlinux.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

