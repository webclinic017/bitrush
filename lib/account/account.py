from abc import ABCMeta, abstractmethod


class Account(metaclass=ABCMeta):

    @abstractmethod
    def get_id(self) -> int:
        pass

    @abstractmethod
    def get_access_key(self) -> str:
        pass

    @abstractmethod
    def get_secret_key(self) -> str:
        pass

    @abstractmethod
    def get_alias(self) -> str:
        pass

    def __repr__(self):
        return f"""Account(id={self.get_id()}, alias={self.get_alias()})"""
