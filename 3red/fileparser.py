import re

regex_security_id = re.compile(r'\x01{}=([^\x01]+)\x01'.format(48))
regex_symbol = re.compile(r'\x01{}=([^\x01]+)\x01'.format(55))
regex_security_type = re.compile(r'\x01{}=([^\x01]+)\x01'.format(167))
regex_product_complex = re.compile(r'\x01{}=([^\x01]+)\x01'.format(462))
regex_mleg_no = re.compile(r'\x01{}=([^\x01]+)\x01'.format(555))
regex_leg_security_id = re.compile(r'\x01{}=([^\x01]+)+\x01'.format(602))
regex_product_code = re.compile(r'\x01{}=([^\x01]+)\x01'.format(6937))


def lineparser(line):

    security_id = regex_security_id.findall(line)
    symbol = regex_symbol.search(line)
    security_type = regex_security_type.search(line)
    product_complex = regex_product_complex.search(line)
    mleg_no = regex_mleg_no.search(line)
    leg_security_id = regex_leg_security_id.findall(line)
    product_code = regex_product_code.search(line)

    return (security_id, symbol, security_type, product_complex,
            mleg_no, leg_security_id, product_code)


def lineparser2(line):

    return (regex_security_id.search(line),
            regex_symbol.search(line),
            regex_security_type.search(line),
            regex_product_complex.search(line),
            regex_mleg_no.search(line),
            regex_leg_security_id.search(line),
            regex_product_code.search(line)
            )
