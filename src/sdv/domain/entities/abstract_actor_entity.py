import abc
from abc import ABCMeta

from sdv.domain.documents.actor_document import ActorDocument


class AbstractActorEntity(metaclass=ABCMeta):
    @abc.abstractmethod
    def to_document(self) -> ActorDocument:
        raise NotImplementedError
