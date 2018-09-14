#import generateNewAddress
import MySQLdb
import configparser
from iota import Iota, ProposedTransaction, Address, Tag, TryteString, Address

config = configparser.ConfigParser()
config.read('config.ini')

IOTA_node_URI_conf  = config['IOTA']['node']
seed = config['IOTA']['seed']
percentage_conf     = config['DEFAULT']['percentage']
mysql_conf_hostname = config['mysql']['host']
mysql_conf_user     = config['mysql']['user']
mysql_conf_passwd   = config['mysql']['passwd']
mysql_conf_db       = config['mysql']['db']

class balance():
    def __init__(self):
        self.seed = seed
        self.IOTA_connection = Iota(IOTA_node_URI_conf, seed = seed)
        self.mysql_connection = MySQLdb.Connection(host = mysql_conf_hostname, user = mysql_conf_user, passwd = mysql_conf_passwd, db = mysql_conf_db)
        self.cursor = self.mysql_connection.cursor()
        self.cursor.execute('select trancount from tranCount')
        self.trancount =  int(self.cursor.fetchone()[0])
        addresses = self.getAddresses(addressCount = self.trancount)
        balance = self.getBalance(addresses)
        iota_to_be_delivered = balance * int(percentage_conf) / 100
        print 'balance is: ', balance
        print 'percentage for Faucet: ', percentage_conf
        print 'iota to be delivered: ', iota_to_be_delivered

    #Get balances for a list of addresses
    def getBalance(self, addresses):
        balances = self.IOTA_connection.get_balances(addresses)
        balance = sum(balances['balances'])
        return balance

    def getAddresses(self, addressCount):
        addresses = self.IOTA_connection.get_new_addresses(count = self.trancount)
        addresses_aux = [str(address) for address in addresses['addresses']]
        #print len(addresses_aux)
        return addresses_aux


balance()
