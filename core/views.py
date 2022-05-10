from abc import ABC, abstractmethod


class AbsView(ABC):
    @abstractmethod
    def get_details(self):
        pass

    @abstractmethod
    def add(self):
        pass


class Book(AbsView):
    def get_details(self):
        pass

    def add(self):
        pass


class Author(AbsView):
    def get_details(self):
        pass

    def add(self):
        pass


class Status(AbsView):
    def get_details(self):
        pass

    def add(self):
        pass
