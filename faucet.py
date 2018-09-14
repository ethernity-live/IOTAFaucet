import MySQLdb
import configparser
from iotacontroller import IOTAController
from mysqlcontroller import MySQLController

config = configparser.ConfigParser()
config.read('config.ini')

seed_conf       = config['IOTA']['seed']
percentage_conf = int(config['DEFAULT']['percentage'])

class IOTAFaucet:
    def __init__(self):
        self.MySQLController = MySQLController()
        self.IOTAController = IOTAController(seed_conf)

    def WeeklyPay(self):
        tranCount = self.MySQLController.getTranCount()
        if (tranCount == 0):
            tranCount = 1
        addresses = self.IOTAController.getAddresses(addressCount = tranCount)
        balance = self.IOTAController.getBalance(addresses)
        if balance > 0:
            #print balance, percentage_conf
            amountToBePaid = int(balance / 100 * percentage_conf)
            #print amountToBePaid
            members = self.MySQLController.getMembersWithRep()
            #Make Payment
            self.IOTAController.MakePayment(members, amountToBePaid)
            print 'Payment OK'
        else:
            print 'Balance is 0'

IOTAFaucet().WeeklyPay()
