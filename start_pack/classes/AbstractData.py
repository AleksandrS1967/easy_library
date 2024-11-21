from abc import ABC, abstractmethod

class AbstractData(ABC):
    @abstractmethod
    def get_data(self, books_data_path):
        pass

    @abstractmethod
    def add_data(self, book, books_data_path):
        pass

    @abstractmethod
    def delete_data(self, books_data_path, id_book):
        pass

    @abstractmethod
    def get_filter_books(self, list_books):
        pass

    @abstractmethod
    def get_list_books(self, list_books):
        pass

    @abstractmethod
    def rename_status_book(self, books_data_path):
        pass