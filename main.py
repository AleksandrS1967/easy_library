import start_pack


def start_app():
    '''
    Функция выполняющая основной цикл приложения - использует init данные пакета start_pack
    :return:
    '''
    while True:
        # Выводим стартовое сообщение и получаем стартовый ввод от пользователя
        start_result = start_pack.get_start_input_message()
        if start_result == '1':
            # Добавляем книгу в файл
            start_pack.work_with_json.add_data(start_pack.create_book(), start_pack.data_book_path)
        if start_result == '2':
            # Удаляем книгу по ее book_id
            id_book = 0
            start_pack.work_with_json.delete_data(start_pack.data_book_path, id_book)
        if start_result == '3':
            # Ищем книгу по ключевым словам
            start_pack.work_with_json.get_filter_books(start_pack.work_with_json.get_data(start_pack.data_book_path))
        if start_result == '4':
            # Получаем список всех книг
            start_pack.work_with_json.get_list_books(start_pack.work_with_json.get_data(start_pack.data_book_path))
        if start_result == '5':
            # Меняем статус книги по ее book_id
            start_pack.work_with_json.rename_status_book(start_pack.data_book_path)
        if start_result == '6':
            # Выход из цикла
            break
        if start_result not in ['1', '2', '3', '4', '5', '6']:
            print('команда не распознана - попробуйте еще раз\n')


if __name__ == '__main__':
    start_app()
