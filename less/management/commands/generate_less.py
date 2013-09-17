import os
import fnmatch

from django.core.management.base import NoArgsCommand
from django.conf import settings

from less.templatetags.less import less


class Command(NoArgsCommand):

    help = "Generates css files for all *.less fles in the STATIC_ROOT and files listed in GENERATE_LESS."
    usage_str = "Usage: ./manage.py generate_less"

    def handle_noargs(self, **options):
        for root, dirnames, filenames in os.walk(settings.STATIC_ROOT):
            for filename in fnmatch.filter(filenames, '*.less'):
                found = os.path.join(root, filename)[len(settings.STATIC_ROOT) + 1:]
                self.stdout.write("Processing '{0}'".format(found))
                less(found)
        for media_url in settings.LESS_GENERATE:
            self.stdout.write("Processing '{0}'".format(media_url))
            less(media_url)
