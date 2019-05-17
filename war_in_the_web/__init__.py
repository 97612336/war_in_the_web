import json
import os

import pymysql

pymysql.install_as_MySQLdb()


def get_sql_conf():
    home_path = os.getenv("HOME")
    conf_file_path = home_path + "/conf/sqlconf"
    with open(conf_file_path, "r") as f:
        conf_str = f.read()
    conf_dict = json.loads(conf_str)
    return conf_dict
