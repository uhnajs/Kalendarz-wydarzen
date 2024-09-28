import requests
from django.shortcuts import render
from django.http import JsonResponse

API_URL = "https://rekrutacja.teamwsuws.pl/events/"
API_KEY = "4ab29a5f350d7a68a8d7527c60d2f776"

def fetch_events_from_api():
    headers = {
        "api-key": API_KEY,
        "Content-Type": "application/json"
    }
    response = requests.get(API_URL, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Błąd {response.status_code}: {response.text}")
        return []

def event_list(request):
    events = fetch_events_from_api()
    return render(request, 'events/event_list.html', {'events': events})

def fetch_event_detail_from_api(event_id):
    url = f"{API_URL}{event_id}/"
    headers = {
        "api-key": API_KEY,
        "Content-Type": "application/json"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Błąd {response.status_code}: {response.text}")
        return None

def event_detail(request, event_id):
    event = fetch_event_detail_from_api(event_id)
    return render(request, 'events/event_detail.html', {'event': event})

def calendar_view(request):
    return render(request, 'events/calendar.html')

def events_api(request):
    events = fetch_events_from_api()
    formatted_events = [
        {
            'id': event['id'],
            'title': event['name'],
            'start': event['start_time'],
            'description': event['short_description']
        }
        for event in events
    ]
    return JsonResponse(formatted_events, safe=False)
