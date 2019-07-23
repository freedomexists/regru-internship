import unittest
from unittest.mock import Mock
import task5 as t
import mysql.connector
from jinja2 import Template
import re
import datetime

select_all = [(22624301, 'srv_hosting_ispmgr', 'Host-Lite-0910', 46544, 26532, 'D', datetime.date(2016, 9, 23), datetime.timedelta(0, 82250), datetime.datetime(2010, 2, 27, 16, 52, 58), 5),
              (22712397, 'srv_vps', 'WIN-3', 345532, 26532, 'A', datetime.date(2016, 9, 29), datetime.timedelta(0, 35620), None, 0),
              (23200637, 'srv_parallels_wpb', 'WPB-Standart', 664082, 26532, 'A', datetime.date(2016, 10, 26), datetime.timedelta(0, 39800), None, 127),
              (27088203, 'srv_vps', 'SSD-VPS-1-0317', 26532, 26532, 'S', datetime.date(2017, 3, 6), datetime.timedelta(0, 47195), None, 3),
              (29414795, 'srv_vps', 'XEN-2-1216', 26112, 26532, 'D', datetime.date(2017, 6, 6), datetime.timedelta(0, 40834), datetime.datetime(2010, 3, 2, 16, 59, 55), 3),
              (30951405, 'srv_license_isp', 'lite5', 45532, 26532, 'O', datetime.date(2017, 8, 18), datetime.timedelta(0, 57881), None, 0),
              (32866369, 'srv_google_apps', 'trial', 382636, 393221, 'D', datetime.date(2017, 11, 3), datetime.timedelta(0, 32562), None, 1),
              (34490653, 'srv_websitebuilder', 'start', 208949, 26532, 'A', datetime.date(2018, 1, 11), datetime.timedelta(0, 78698), datetime.datetime(2010, 3, 12, 11, 25, 45), 0),
              (35109397, 'srv_vps', 'SSD-VPS-2-0317', 664082, 664082, 'D', datetime.date(2018, 2, 12), datetime.timedelta(0, 30684), None, -3),
              (35109399, 'srv_license_isp', 'lite5', 664082, 664082, 'S', datetime.date(2018, 2, 12), datetime.timedelta(0, 30562), datetime.datetime(2012, 7, 12, 12, 40, 15), 55)]


connect = mysql.connector.connect(user='blase', password='123',
                              host='test_db',
                              database='test_db')

sample_list = ['35109399;srv_license_isp;lite5;664082;664082;S;2018-02-12;08:29:22;2012-07-12 12:40:15;55',
               '35109397;srv_vps;SSD-VPS-2-0317;664082;664082;D;2018-02-12;08:31:24;NULL;-3',
               '34490653;srv_websitebuilder;start;208949;26532;A;2018-01-11;21:51:38;2010-03-12 11:25:45;0',
               '32866369;srv_google_apps;trial;382636;393221;D;2017-11-03;09:02:42;NULL;1',
               '30951405;srv_license_isp;lite5;45532;26532;O;2017-08-18;16:04:41;NULL;0',
               '29414795;srv_vps;XEN-2-1216;26112;26532;D;2017-06-06;11:20:34;2010-03-02 16:59:55;3',
               '27088203;srv_vps;SSD-VPS-1-0317;26532;26532;S;2017-03-06;13:06:35;NULL;3',
               '23200637;srv_parallels_wpb;WPB-Standart;664082;26532;A;2016-10-26;11:03:20;NULL;127',
               '22712397;srv_vps;WIN-3;345532;26532;A;2016-09-29;09:53:40;NULL;0',
               '22624301;srv_hosting_ispmgr;Host-Lite-0910;46544;26532;D;2016-09-23;22:50:50;2010-02-27 16:52:58;5']

sample_row_tuple = (None, 'srv_google_apps', 'start', '208949', '26532', 'A', '2018-01-11', '21:51:38', None, '66')


def clear_table(connect_db):
    cursor = connect_db.cursor()
    clear = ("TRUNCATE table_task1;")
    cursor.execute(clear)
    connect_db.commit()
    cursor.close()


def insert_data(connect_db, data):
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


def reinit_db(connect):
    data = sample_list
    for row in data:
        row = row.split(';')
        for i in range(len(row)):
            if row[i] == 'NULL':
                row[i] = None
        row = tuple(row)
        insert_data(connect, row)




class MyUnitTest(unittest.TestCase):
    clear_table(connect)
    def test_parse_csv(self):
        expected_data = sample_list
        with open('test_csv_data', 'rb') as f:
            test_data = f.read()
        data = t.parse_csv(test_data)
        self.assertEqual(data, expected_data)

    def test_parse_content(self):
        expected_data = sample_row_tuple
        with open('raw_data', 'rb') as f:
            test_data = f.read()
        data = t.parse_content(test_data)
        self.assertEqual(data, expected_data)

    def test_get_data(self):
        reinit_db(connect)
        expected_data = select_all
        try:
            data = t.get_data(connect)
        finally:
            clear_table(connect)
        self.assertEqual(data, expected_data)


    def test_del_row(self):
        reinit_db(connect)
        expected_data = select_all[1:]
        id = 22624301
        try:
            t.del_row(connect, id)
            data = t.get_data(connect)
        finally:
            clear_table(connect)

        self.assertEqual(data, expected_data)


    def test_insert_data(self):
        reinit_db(connect)
        expected_data = select_all + [(35109400, 'srv_google_apps', 'start', 208949, 26532, 'A', datetime.date(2018, 1, 11), datetime.timedelta(0, 78698), None, 66)]
        try:
            t.insert_data(connect, sample_row_tuple)
            data = t.get_data(connect)
        finally:
            clear_table(connect)

        self.assertEqual(data, expected_data)

    def test_update_row(self):
        reinit_db(connect)
        expected_data = select_all[:-1] + [(35109399, 'хопхей-лалалей', 'start', 208949, 26532, 'A', datetime.date(2018, 1, 11), datetime.timedelta(0, 78698), None, 66)]
        try:
            t.update_row(connect, (35109399, 'хопхей-лалалей', 'start', '208949', '26532', 'A', '2018-01-11', '21:51:38', None, '66'))
            data = t.get_data(connect)
        finally:
            clear_table(connect)

        self.assertEqual(data, expected_data)

    def test_clear_table(self):
        try:
            t.clear_table(connect)
            data = t.get_data(connect)
        finally:
            clear_table(connect)

        self.assertEqual(data, [])


