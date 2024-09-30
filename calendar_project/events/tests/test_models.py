from django.test import TestCase
from events.models import Event
from datetime import datetime
from django.utils.timezone import make_aware

class EventModelTest(TestCase):
    def setUp(self):
        self.event = Event.objects.create(
            title='Test Event',
            description='This is a test event',
            start_time=make_aware(datetime(2024, 9, 23, 10, 0)),
            end_time=make_aware(datetime(2024, 9, 23, 12, 0))
        )

    def test_event_creation(self):
        self.assertEqual(self.event.title, 'Test Event')
        self.assertEqual(self.event.description, 'This is a test event')

    def test_event_str(self):
        self.assertEqual(str(self.event), 'Test Event')
