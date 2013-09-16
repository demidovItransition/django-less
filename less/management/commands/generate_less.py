import os, fnmatch

from django.core.management.base import NoArgsCommand
from django.conf import settings

from less.templatetags.less import less


class Command(NoArgsCommand):
    def handle_noargs(self, **options):
        for root, dirnames, filenames in os.walk(settings.STATIC_ROOT, followlinks=True):
            for filename in fnmatch.filter(filenames, '*.less'):
                less(os.path.join(root, filename)[len(settings.STATIC_ROOT) + 1:])
