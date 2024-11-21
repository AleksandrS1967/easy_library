import pathlib
from start_pack.functions.create_book_input import create_book
from start_pack.functions.get_start_input_message import get_start_input_message
from start_pack.classes.DataJson import DataJson
work_with_json = DataJson()

project_path = pathlib.Path(__file__).parent.parent
data_book_path = pathlib.Path(project_path, 'books.json')