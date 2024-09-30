from django.test import TestCase, Client
from django.urls import reverse
from unittest.mock import patch

class EventViewTests(TestCase):
    def setUp(self):
        self.client = Client()

    @patch('events.views.fetch_events_from_api')
    def test_event_list_view(self, mock_fetch_events):
        mock_fetch_events.return_value = [
            {
                'id': 1,
                'name': 'Test Event',
                'start_time': '2024-09-23T10:00:00',
                'short_description': 'This is a test event',
            }
        ]

        response = self.client.get(reverse('event_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'events/event_list.html')
        self.assertContains(response, 'Test Event')

    @patch('events.views.fetch_event_detail_from_api')
    def test_event_detail_view(self, mock_fetch_event_detail):
        mock_fetch_event_detail.return_value = {
            'id': 1,
            'name': 'Test Event Detail',
            'start_time': '2024-09-23T10:00:00',
            'short_description': 'Details of test event',
            'description': 'Full details of the test event',
        }

        response = self.client.get(reverse('event_detail', args=[1]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'events/event_detail.html')
        self.assertContains(response, 'Test Event Detail')

    def test_calendar_view(self):
        response = self.client.get(reverse('calendar_view'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'events/calendar.html')

    @patch('events.views.fetch_events_from_api')
    def test_events_api_view(self, mock_fetch_events):
        mock_fetch_events.return_value = [
            {
                'id': 1,
                'name': 'Test API Event',
                'start_time': '2024-09-23T10:00:00',
                'short_description': 'This is a test event for API',
            }
        ]

        response = self.client.get(reverse('events_api'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), [
            {
                'id': 1,
                'title': 'Test API Event',
                'start': '2024-09-23T10:00:00',
                'description': 'This is a test event for API'
            }
        ])

