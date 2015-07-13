sar =  """
   sar -w -d -u -n ETCP {sarinterval} {sarcount} -o {saroutfile} > /dev/null ;
   sadf -dht {saroutfile} -- -p -w -d -u -n ETCP {sarinterval} {sarcount} |
   tee --append {outfile}
   """

filesize = """
    for U in $(ls -d {targetdir}/*); do
      FCOUNT=0
      TOTALSIZE=0
      for FILE in $(find $U -type f 2>>{errfile}); do
        FCOUNT=$((FCOUNT + 1))
	FSIZE=$(du -b $FILE 2>>{errfile} |cut -f1)
	TOTALSIZE=$((TOTALSIZE + FSIZE))
      done
      echo $(basename $U),$FCOUNT,$TOTALSIZE \
      | tee --append {outfile}
    done;
    """

cpu = """
    ( ps -eo comm=,pid=,time=,rss= --sort=-time |head -n5;
    ps -eo comm=,pid=,time=,rss= --sort=-rss  |head -n5 ) \
    | tee --append {outfile}
    """

# siblingnodes all hosts not host; ' '.join(set(hosts) - set([host]))
ping = """
    for N in {siblingnodes}; do
      echo $(ping $N -q -c 1)
    done | tee --append {outfile}
    """

CMD_TEMPLATES = {
    'sar': sar,
    'filesize': filesize,
    'cpu': cpu,
    'ping': ping,
    }

