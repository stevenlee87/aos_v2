from optparse import make_option

from django.core.management.base import BaseCommand, CommandError
from polls.models import Poll, Choice

#class Command(BaseCommand):
#    args = '<poll_id poll_id ...>'
#    help = 'Closes the specified choice for voting'
#
#    def handle(self, *args, **options):
#        for choice_content in args:
#            try:
#                c = Choice.objects.filter(choice_text=choice_content)
#            except Choice.DoesNotExist:
#                raise CommandError('"%s" does not exist' % choice_content)
#
#            c.delete()
#
#            self.stdout.write('Successfully deleted  "%s"' % choice_content)

#class Command(BaseCommand):
#    option_list = BaseCommand.option_list + (
#        make_option('--delete',
#            action='store_true',
#            dest='delete',
#            default=False,
#            help='Delete poll instead of closing it'),
#        )
#
#    def handle(self, *args, **options):
#        # ...
#        if options['delete']:
#            poll.delete()
#            #print 'args is %s' % options['delete']
#            #print 'args is %s' % options
#            #print 'BaseCommand.option_list is "%s"' % BaseCommand.option_list

class Command(BaseCommand):
    option_list = BaseCommand.option_list + (
        make_option('--delete',
            action='store_true',
            dest='delete',
            default=False,
            help='Delete poll instead of closing it'),
        )

    def handle(self, *args, **options):
        # ...
        if options['delete']:

