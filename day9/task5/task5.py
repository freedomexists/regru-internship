from http.server import HTTPServer, BaseHTTPRequestHandler
import mysql.connector
from jinja2 import Template


def parse_content(content):
    content = content.decode('utf-8').replace('%3A', ':').replace('T', ' ')
    parsed_content_list = []
    content = content.split('&')
    for kv in content:
        parsed_content_list.append(kv.split('=')[1])
    print(parsed_content_list)
    return tuple(parsed_content_list)


def read_csv(csv_data):
    data = csv_data.decode('utf-8').split('\n')[5:-3]

    return data


def insert_data(data):
    cursor = connect_db.cursor()
    add_data = ("INSERT INTO table_task1 "
                "(servtype, subtype, user_id, referrer_user_id, "
                "state, creation_date, creation_time, creation_request_sent_date,"
                "notified_about_expiration)"
                "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
                ";")

    cursor.execute(add_data, data)
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


class MyRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        pth = self.path.split('/')
        if pth[1] == 'delete':
            del_row(pth[2])
        self.gen_page()


    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)

        if self.path == '/create/':
            data = parse_content(body)
            insert_data(data)

        if self.path == '/opencsv/':
            data = read_csv(body)
            if data:
                clear_table()
                for row in data:
                    row = row.split(';')[1:]
                    for i in range(len(row)):
                        if row[i] == 'NULL':
                            row[i] = None
                    row = tuple(row)
                    insert_data(row)

        self.gen_page()


    def gen_page(self):
        self.send_response(200)
        self.end_headers()
        html = open('index.html').read()
        template = Template(html)
        table = get_data()
        self.wfile.write(template.render(table=table).encode())

connect_db = mysql.connector.connect(user='blase', password='123',
                              host='127.0.0.1',
                              database='day9')

httpd = HTTPServer(('10.0.2.15', 8000), MyRequestHandler)
httpd.serve_forever()
