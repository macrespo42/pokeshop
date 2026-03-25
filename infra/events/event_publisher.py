from typing import Callable

from domain.event.event_publisher import Event, IEventPublisher


class InMemoryEventPublisher(IEventPublisher):
    def __init__(self):
        self._handlers = {}

    def subscribe(self, event_type: type, handler: Callable):
        if not self._handlers.get(event_type):
            self._handlers[event_type] = []
        self._handlers[event_type].append(handler)

    def publish_event(self, event: Event):
        for handler in self._handlers.get(type(event), []):
            handler(event)
