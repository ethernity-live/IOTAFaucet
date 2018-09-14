#import generateNewAddress
import MySQLdb
import configparser
from iota import Iota, ProposedTransaction, Address, Tag, TryteString, Address
from mysqlcontroller import MySQLController

config = configparser.ConfigParser()
config.read('config.ini')

IOTA_node_URI_conf  = config['IOTA']['node']

class IOTAController():
    def __init__(self, seed):
        self.seed = seed
        self.IOTA_connection = Iota(IOTA_node_URI_conf, seed = seed)

    def MakePayment(self, members, amountToBePaid):
        total_reputation = int(sum(int(member[1]) for member in members))
        #print total_reputation, ', total_reputation'
        IOTA_per_rep_score = amountToBePaid / (total_reputation * 1.00)
        #print amountToBePaid
        for member in members:
            #print member, ', member'
            try:
                if self.isValid(member[0]):
                    #print IOTA_per_rep_score
                    IOTA_to_be_paid = int(IOTA_per_rep_score * int(member[1]))
                    print 'IOTA to be paid: ', IOTA_to_be_paid
                    #print IOTA_to_be_paid
                    #print member[0], IOTA_to_be_paid
                    self.sendTransfer(address = str(member[0]), value = IOTA_to_be_paid, depth = 100)
            except TypeError:
                continue

    def sendTransfer(self, address, value, depth = 100):
        address = str(address)
        value = int(value)
        self.IOTA_connection.send_transfer(
            depth = depth,
            transfers = [
                ProposedTransaction(
                    address = Address(address),
                    value = value,
                ),
            ],
        )

    #Get balances for a list of addresses
    def getBalance(self, addresses):
        balances = self.IOTA_connection.get_balances(addresses)
        balance = sum(balances['balances'])
        return balance

    #Check whether an address is valid
    def isValid(self, address):
        #check whether an IOTA address is valid
        try:
            Address(address)
            return True
        except ValueError, TypeError:
            return False

    def getAddresses(self, addressCount):
        if addressCount <= 5:
            addressCount = 5
        addresses = self.IOTA_connection.get_new_addresses(count = addressCount)
        addresses_aux = [str(address) for address in addresses['addresses']]
        #print len(addresses_aux)
        return addresses_aux
