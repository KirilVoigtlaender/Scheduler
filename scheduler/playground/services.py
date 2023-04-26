from .models import Event

def add_event(name, event_type, date, start_time, end_time, repetition):
    return Event.objects.create(name=name, event_type=event_type, date=date, start_time=start_time, end_time=end_time, repetition=repetition)

def delete_event(event_id):
    try:
        event = Event.objects.get(pk=event_id)
        event.delete()
        return True
    except Event.DoesNotExist:
        return False
    
def update_event(event_id, name, event_type, date, start_time, end_time, repetition):
    try:
        event = Event.objects.get(pk=event_id)
    except Event.DoesNotExist:
        return None
    if name:
        event.name=name
    if event_type:
        event.event_type=event_type
    if date:
        event.date=date
    if start_time:
        event.start_time=start_time
    if end_time: 
        event.end_time=end_time
    if repetition:
        event.repetition=repetition

    event.save()
    return event

def get_event(event_id, name, event_type, date, start_time, end_time, repetition):
    return event_id, name, event_type, date, start_time, end_time, repetition