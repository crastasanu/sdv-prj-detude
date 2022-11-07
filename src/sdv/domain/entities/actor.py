from abc import ABCMeta
from dataclasses import dataclass
from datetime import datetime

from sdv.domain.documents.actor_document import ActorDocument
from sdv.domain.documents.actor_es_document import ActorEsDocument
from sdv.domain.entities.abstract_actor_entity import AbstractActorEntity


@dataclass
class Actor(AbstractActorEntity):
    """Class for defining an actor."""
    id: int
    first_name: str
    last_name: str
    last_update: datetime

    def to_document(self) -> ActorEsDocument:

        """ we can do the processing here before creating the document that will be indexed later on elasticsearch"""

        self.first_name = f"{self.first_name} PSG {self.last_name}"

        return ActorEsDocument(
            id=self.id,
            first_name=self.first_name,
            last_name=self.last_name,
            last_update=self.last_update
        )
