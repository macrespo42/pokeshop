from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass(frozen=True)
class Event:
    pass


class IEventPublisher(ABC):
    @abstractmethod
    def publish_event(self, event: Event):
        pass
