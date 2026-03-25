from domain.event.event_publisher import Event, IEventPublisher


class InMemoryEventPublisher(IEventPublisher):
    def __init__(self):
        self.events = []

    def publish_event(self, event: Event):
        self.events.append(event)
