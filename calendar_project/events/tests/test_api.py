from django.test import TestCase
from unittest.mock import patch
from events.views import fetch_events_from_api

class EventApiConnectionTest(TestCase):

    @patch('events.views.requests.get')
    def test_fetch_events_from_api(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = [
            {
                'id': 1,
                'name': 'Test Event',
                'start_time': '2024-09-23T10:00:00',
                'short_description': 'This is a test event'
            }
        ]

        events = fetch_events_from_api()
        self.assertEqual(len(events), 1)
        self.assertEqual(events[0]['name'], 'Test Event')
