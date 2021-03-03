from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    help = 'This is a simple command to run the bot execution. Try type: manage.py bot run'

    def add_arguments(self, parser):
        parser.add_argument('run')

    def handle(self, *args, **options):
        try:
            self.stdout.write(self.style.SUCCESS('Bot starts execution . . .'))
            exec(open('socialnet/bot/http_bot.py').read())
            self.stdout.write(self.style.SUCCESS('Successfully Created users and posts'))
        except Exception as ex:
            raise CommandError('Something went wrong')
