import json
import os
from start_pack.classes.AbstractData import AbstractData


class DataJson(AbstractData):
    def get_data(self, books_data_path):
        '''
        Получает данные из json файла - в случае его отсутствия создает новый
        :param books_data_path:
        :return:
        '''
        if not os.path.exists(books_data_path):
            with open(books_data_path, 'a') as f:
                pass
        with open(books_data_path, encoding='utf-8') as f:
            if os.stat(books_data_path).st_size != 0:
                return json.load(f)
        return None

    def add_data(self, book, books_data_path):
        '''
        Записываем данные книги в json в виде списка словарей
        :param book:
        :param books_data_path:
        :return:
        '''
        with open(books_data_path, 'a+', encoding='utf-8') as f:
            list_ = list()
            data = self.get_data(books_data_path)
            f.truncate(0)
            if data:
                [list_.append(i) for i in data]
            list_.append(book)
            json.dump(list_, f, ensure_ascii=False)

    def delete_data(self, books_data_path, id_):
        '''
        Удаляем книгу используя переданный book_id при изменении статуса
        книги методом данного класса rename_status_book или ели он не был передан
        запрашиваем его у пользователя.
        Проверяет валидность book_id.
        :param books_data_path:
        :param id_:
        :return:
        '''
        save_id = int()
        if id_ == 0:
            save_id = id_
            print('Укажите book_id для удаления книги')
            id_ = input()
        with open(books_data_path, 'a+', encoding='utf-8') as f:
            list_ = list()
            check_list = list()
            data = self.get_data(books_data_path)
            if data:
                [list_.append(i) for i in data if i['book_id'] != id_]
                [check_list.append(i_['book_id']) for i_ in data]
            if id_ not in check_list:
                print(f'Данный book_id({id_}) не найден\n')
            else:
                if save_id == 0:
                    print(f'Удаление книги с id {id_} прошло успешно\n')
            f.truncate(0)
            json.dump(list_, f, ensure_ascii=False)

    def get_filter_books(self, list_books):
        '''
        Запрашивает слова для фильтрации у пользователя.
        Выводит в консоль результат запроса
        :param list_books:
        :return:
        '''
        print(f'Введите ключевые слова для фильтрации книг через пробел: ')
        filter_words = input().split(' ')
        finish_list = list()
        for i in list_books:
            for i_ in i.values():
                if i_ in filter_words:
                    if i not in finish_list:
                        finish_list.append(i)
        if finish_list:
            print(f'\nНайденные книги по запросу {filter_words}:')
            for i in finish_list:
                print(i)
        else:
            print(f'По запросу {filter_words} не чего не найдено(...')
        print('\n')

    def get_list_books(self, list_books):
        '''
        Принимает список всех книг.
        Проверяет наличие элементов в списке.
        Выводит книги в консоль поочередно в виде словарей
        :param list_books:
        :return:
        '''
        if list_books:
            print(f'Список всех книг:')
            for i in list_books:
                print(i)
        else:
            print('Пока список книг пуст(...')
        print('\n')

    def rename_status_book(self, books_data_path):
        '''
        Спрашивает у пользователя book_id.
        Спрашивает новый статус.
        Проверяет book_id и статус на валидность.
        Изменяет статус найденной по book_id книги.
        :param books_data_path:
        :return:
        '''
        print('Укажите id книги для изменения ее статуса:\n')
        book_id = input()
        check_id_list = list()
        list_books = self.get_data(books_data_path)
        if list_books:
            [check_id_list.append(i['book_id']) for i in list_books]
        if book_id not in check_id_list:
            print(f'Книги с id-{book_id} не найдено\n')
        else:
            print('Укажите новый статус:\n'
                  'в наличии - введите 1\n'
                  'выдана - введите 2')
            new_status = input()
            if new_status not in ['1', '2']:
                print(f'Статус {new_status} не распознан\n')
            else:
                book_list = list()
                [book_list.append(i) for i in list_books if i['book_id'] in check_id_list]
                if new_status == '1':
                    book_list[0]['book_status'] = 'в наличии'
                if new_status == '2':
                    book_list[0]['book_status'] = 'выдана'
                new_book = book_list[0]
                self.delete_data(books_data_path, book_id)
                self.add_data(new_book, books_data_path)
                print('Статус успешно изменен')
                print('\n')
