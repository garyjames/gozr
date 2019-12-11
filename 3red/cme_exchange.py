from ftplib import FTP

cmehost = 'ftp.cmegroup.com'
sfname = 'SBEFix/Production/secdef.dat.gz'
tfname = 'secdef.dat.gz'


def get_file(server=cmehost, source=sfname, target=tfname):
    with open(target, 'wb') as FH:
        ftp = FTP()
        ftp.connect(server)
        ftp.login()
        ftp.retrbinary('RETR {}'.format(source), FH.write)
