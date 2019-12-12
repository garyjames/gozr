import re

regex_security_id = re.compile(r'\x01{}=([^\x01]+)\x01'.format(48))
regex_symbol = re.compile(r'\x01{}=([^\x01]+)\x01'.format(55))
regex_security_type = re.compile(r'\x01{}=([^\x01]+)\x01'.format(167))
regex_maturity = re.compile(r'\x01{}=([^\x01]+)\x01'.format(200))
regex_product_complex = re.compile(r'\x01{}=([^\x01]+)\x01'.format(462))
regex_mleg_no = re.compile(r'\x01{}=([^\x01]+)\x01'.format(555))
regex_leg_security_id = re.compile(r'\x01{}=([^\x01]+)+\x01'.format(602))
regex_product_code = re.compile(r'\x01{}=([^\x01]+)\x01'.format(6937))

def regex(line):

    security_id = regex_security_id.search(line).group(1)
    symbol = regex_symbol.search(line).group(1)
    security_type = regex_security_type.search(line).group(1)
    maturity = regex_maturity.search(line).group(1)
    product_complex = regex_product_complex.search(line)
    mleg_no = regex_mleg_no.search(line)
    leg_security_id = regex_leg_security_id.findall(line)
    product_code = regex_product_code.search(line).group(1)

    if product_complex:
        product_complex = product_complex.group(1)
    else:
        product_complex = ''

    if mleg_no:
        mleg_no = mleg_no.group(1)
    else:
        mleg_no = ''

    return (security_id,
            symbol,
            security_type,
            maturity,
            product_complex,
            mleg_no,
            leg_security_id,
            product_code)


def foobar(line):

    retr = []

    for tag in ['48', '55']:
        idx1 = line.find('\x01{}='.format(tag))
        idx2 = line[idx1+4:].find('\x01')
        val = line[idx1+4:idx1+4+idx2]
        retr.append(val)
    for tag in ['167', '462']:
        idx1 = line.find('\x01{}='.format(tag))
        idx2 = line[idx1+5:].find('\x01')
        val = line[idx1+5:idx1+5+idx2]
        retr.append(val)

    return retr
