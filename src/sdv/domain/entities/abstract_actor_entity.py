import abc
from abc import ABCMeta

from sdv.domain.documents.actor_document import ActorDocument
from sdv.domain.documents.actor_es_document import ActorEsDocument


class AbstractActorEntity(metaclass=ABCMeta):
    @abc.abstractmethod
    def to_document(self) -> ActorEsDocument:
        raise NotImplementedError
