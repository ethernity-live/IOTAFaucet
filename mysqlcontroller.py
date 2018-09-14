import MySQLdb
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

percentage_conf     = config['DEFAULT']['percentage']
mysql_conf_hostname = config['mysql']['host']
mysql_conf_user     = config['mysql']['user']
mysql_conf_passwd   = config['mysql']['passwd']
mysql_conf_db       = config['mysql']['db']

class MySQLController():
    def __init__(self):
        self.mysql_connection = MySQLdb.Connection(host = mysql_conf_hostname, user = mysql_conf_user, passwd = mysql_conf_passwd, db = mysql_conf_db)
        self.cursor = self.mysql_connection.cursor()

    def getTranCount(self):
        self.cursor.execute('select trancount from tranCount')
        trancount = int(self.cursor.fetchall()[0][0])
        return trancount

    def updateTranCount(self):
        self.cursor.execute('update tranCount set trancount = trancount + 1')
        self.mysql_connection.commit()
        return True

    def getMembersWithRep(self):
        self.cursor.execute('select IOTA_adress, reputation from wp_users where reputation > 0')
        members = self.cursor.fetchall()
        return members
