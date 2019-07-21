from http.server import HTTPServer, BaseHTTPRequestHandler
import mysql.connector
from jinja2 import Template
import re


class Router:
    def __init__(self):
        self.paths = []

    def register(self, path, view=None):
        if view is None:

            def decorator(fn):
                self.paths.append((path, fn))
                return fn

            return decorator
        else:
            self.paths.append((path, view))

    def resolve(self, request_path, body=None):
        for path, view in self.paths:
            match = re.match(path, request_path)
            if match:
                view(body, *match.groups())
                return True


class MyRequestHandler(BaseHTTPRequestHandler):

    router = Router()

    def do_GET(self):
        if self.router.resolve(self.path, ):
            self.do_response()
        else:
            self.send_error(404, 'Not found')

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)

        if self.router.resolve(self.path, body):
            self.do_response()
        else:
            self.send_error(404, 'Not found')

    def do_response(self):
        self.send_response(200)
        self.end_headers()
        html = open('index.html').read()
        template = Template(html)
        table = get_data()
        self.wfile.write(template.render(table=table).encode())


connect_db = mysql.connector.connect(user='blase', password='123',
                              host='127.0.0.1',
                              database='day9')
handler = MyRequestHandler


@handler.router.register('/opencsv/')
def insert_data_from_csv_to_table(body):
    data = read_csv(body)
    if data:
        clear_table()
        for row in data:
            row = row.split(';')
            for i in range(len(row)):
                if row[i] == 'NULL':
                    row[i] = None
            row = tuple(row)
            insert_data(row)


@handler.router.register('/create/')
def insert_new_row_in_table(body):
    data = parse_content(body)
    insert_data(data)


@handler.router.register('/update/')
def update_row_in_table(body):
    data = parse_content(body)
    try:
        update_row(data)
    except mysql.connector.errors.DataError:
        pass


@handler.router.register('(/delete/)(\d+)')
def delete_row_in_table(*kwargs):
    del_row(kwargs[2])


@handler.router.register('/')
def send_index(body):
    pass


def parse_content(content):

    content = content.decode('utf-8').replace('%3A', ':').replace('T', ' ')
    content = content.split('&')

    if len(content) == 10:
        parsed_content_list = []
    else:
        parsed_content_list = [None]

    for kv in content:
        value = kv.split('=')[1]
        if value == 'None' or value == '':
            value = None
        parsed_content_list.append(value)

    return tuple(parsed_content_list)


def read_csv(csv_data):
    data = csv_data.decode('utf-8').split('\n')[5:-3]
    return data


def insert_data(data):
    cursor = connect_db.cursor()
    add_data = ("INSERT INTO table_task1 "
                "(service_id, servtype, subtype, user_id, referrer_user_id, "
                "state, creation_date, creation_time, creation_request_sent_date,"
                "notified_about_expiration)"
                "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                ";")

    cursor.execute(add_data, data)
    connect_db.commit()
    cursor.close()


def update_row(data):
    cursor = connect_db.cursor()
    update = ("UPDATE table_task1 SET servtype = %s, subtype = %s, user_id = %s, referrer_user_id = %s, "
              "state = %s, creation_date = %s, creation_time = %s, creation_request_sent_date = %s, "
              "notified_about_expiration = %s "
              "WHERE service_id = {};".format(data[0]))
    cursor.execute(update, data[1:])
    connect_db.commit()
    cursor.close()


def clear_table():
    cursor = connect_db.cursor()
    clear = ("TRUNCATE table_task1;")
    cursor.execute(clear)
    connect_db.commit()
    cursor.close()


def del_row(id):
    cursor = connect_db.cursor()
    delete = ("DELETE FROM table_task1 WHERE service_id = {};".format(id))
    cursor.execute(delete)
    connect_db.commit()
    cursor.close()


def get_data():
    cursor = connect_db.cursor()
    query = ("SELECT * FROM table_task1;")
    cursor.execute(query)
    data = cursor.fetchall()
    cursor.close()
    return data


httpd = HTTPServer(('10.0.2.15', 8000), MyRequestHandler)
httpd.serve_forever()
