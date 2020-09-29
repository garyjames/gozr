# foobar.py

"""foobar ver 0.1"""

import csv

class Stock(object): 
    def __init__(self, symbol, description, country, shares, 
                 price, currency, total_value):
        self.symbol = symbol
        self.description = description 
        self.country = country 
        self.shares = float(shares)
        self.price = float(price) 
        self.currency = currency
        self.total_value = total_value

    def __str__(self):
        return "{} {} {} {} {}".format(self.symbol, self.description, 
                                    self.shares, self.price, 
                                    self.total_value,)

    def cashDividend(self, cash=0):
        self.price = self.price - cash
        self.total_value = self.price * self.shares

    def stockDividend(self, ratio=1):
        self.shares = self.shares * ratio
        self.price = self.price / ratio
        self.total_value = self.price * self.shares

    def stockSplit(self, post_split=1, pre_split=1):
        ratio = pre_split/float(post_split)
        self.shares = self.shares / ratio 
        self.price = self.price * ratio
        self.total_value = self.price * self.shares

    def symbolChange(self, newsymbol=''):
        self.symbol = newsymbol

    def descriptionChange(self, newdescription=''):
        self.description = newdescription


def print_portfolio(portfolio):
    for i in portfolio:
        print i
    print

def parser(fh):
    ret = []
    for line in fh:
        line = line.strip('\n')
        if len(line) < 1:
            continue
        # config file
        if '=' in line:
            exchange_configs, symbol_configs = line.split('=')
            line = ','.join([exchange_configs, symbol_configs])
        # symbol file
        else:
	    pass

        ret.append(line)

    return ret

def findMissingSymbols(symbols, configs, searchKey=''):
    missing = []
    symbols = set(symbols)
    for config in configs:
        config_name, config_str = config.split(',')
        if searchKey in config_name:
            config_items = config_str.split()
            config_symbols = [ s for s in config_items[0::3] ]
            config_symbols = set(config_symbols)
            missing.append([config_name, symbols - config_symbols])

    return missing


# problem 1
with open('fileA') as sFile, open('fileB') as cFile:
    symbols = parser(sFile)
    configs = parser(cFile)

print "Missing from GroupA"
for i in findMissingSymbols(symbols, configs, 'groupA'):
    print i

print "Missing from ExchangeB"
for i in findMissingSymbols(symbols, configs, 'exchangeB'):
    print i

print "Missing from ExchangeC"
for i in findMissingSymbols(symbols, configs, 'exchangeC'):
    print i


# problem 2
print
# This here is me making some typing noises to make sure the distraction is real

with open('fileC') as fh:
    configs = parser(fh)

check_failed = []
for config in configs:
    config_name, config_str = config.split(',')
    port1, ip, port2 = config_str.split()
    ip = ip.strip(';').split('.')
    port_check = 50000 + int(ip[2]) * 200 + int(ip[3])
    if port_check != int(port1):
        print "Check Failed:\nsubstitute [{}] for line {}".format(port_check, config)
        

# problem 3
# initialize portfolio using csv file 'portfolio.txt'
print
portfolio = []
with open('portfolio.txt') as fh:
    csv_reader = csv.reader(fh)
    csv_header = csv_reader.next()
    for row in csv_reader:
        #print "{}".format(row)
        stock = Stock(*row)
        portfolio.append(stock)

print_portfolio(portfolio)

# corp action 1
for i in portfolio:
    if i.symbol == 'BAC':
        i.cashDividend(cash=.02)

# corp action 2
for i in portfolio:
    if i.symbol == 'REX':
        i.stockSplit(post_split=9, pre_split=10)

# corp action 3,4
for i in portfolio:
    if i.symbol == 'RIM':
        i.symbolChange(newsymbol='BB')
        i.descriptionChange(newdescription='Blackberry')

print "MONDAY"
print_portfolio(portfolio)

# corp action 5
for i in portfolio:
    if i.symbol == 'INTC':
        i.cashDividend(cash=.21)

# corp action 6
for i in portfolio:
    if i.symbol == 'POT':
        i.cashDividend(cash=.07)

# corp action 7
for i in portfolio:
    if i.symbol == 'BARC':
        i.cashDividend(cash=3)

print "TUESDAY"
print_portfolio(portfolio)

# corp action 8
for i in portfolio:
    if i.symbol == 'GOOG':
        i.stockSplit(post_split=3, pre_split=1)

# corp action 9
for i in portfolio:
    if i.symbol == 'SIRI':
        i.stockSplit(post_split=1, pre_split=3)

print "WEDNESDAY"
print_portfolio(portfolio)

# corp action 10
for i in portfolio:
    if i.symbol == 'T':
        i.stockDividend(ratio=1.075)

print "THURSDAY"
print_portfolio(portfolio)

# corp action 11
for i in portfolio:
    if i.symbol == 'QQQ':
        i.cashDividend(cash=.4125)

print "FRIDAY"
print_portfolio(portfolio)

