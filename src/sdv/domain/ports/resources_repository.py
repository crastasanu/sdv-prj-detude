import abc
from abc import ABCMeta
from typing import List

from sdv.domain.entities.abstract_actor_entity import AbstractActorEntity


class ResourceRepository(metaclass=ABCMeta):
    @abc.abstractmethod
    def find_all(self) -> List[AbstractActorEntity]:
        raise NotImplementedError

    @abc.abstractmethod
    def find_by_ids(self, ids: List[int]) -> List[AbstractActorEntity]:
        raise NotImplementedError



