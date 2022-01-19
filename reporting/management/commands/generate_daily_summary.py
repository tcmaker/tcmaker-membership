from django.core.management.base import BaseCommand, CommandError

import reporting.util

class Command(BaseCommand):
    help = "Generates a daily summary record"

    def handle(self, *args, **options):
        reporting.util.create_todays_summary()
