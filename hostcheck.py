# hostcheck.py
"""Run commands on remote hosts using Popen, parse and report results"""

import sys
import subprocess
from datetime import datetime, timedelta
from collections import defaultdict
from hostcheck_cfg import CMD_TEMPLATES

#### Configs ####
#
# output results from commands to local machine
out_file = '/tmp/hostcheck.tmp'
err_file = '/tmp/hostcheck.err'
#
# outfile used by sadf; sar interval, count
sar_outfile = '/tmp/sar.tmp'
sar_interval = 1
sar_count = 30
#
# set directory to be searched
# e.g. /home/
target_dir = '/home'
#
# globals
errors = defaultdict(list)
reports = defaultdict(lambda: defaultdict(list))

host_file = 'hostfile'
hosts = []
with open(host_file) as fh:
    for h in fh:
        hosts.append(h.strip('\n '))


def print_report(reports):

    print '\n*** Remote commands completed.  Generating reports ***\n'
    for h in reports:
        print 'Host', h, 'summary:\n'
        for cmd in reports[h]:
            for report in reports[h][cmd]:
    	        if 'sar' in cmd:
    	            print '  Retransmits {retrans:.2f}'.format(**report)
    	            print '  CPU Load {current_cpuload:.2f}'.format(**report)
    	            print '  CPU Load Avg {cpuload:.2f}'.format(**report)
    	            print '  Context Switches {cswch}'.format(**report)
    		    print '\n  Device Avg Service Times'
    		    for d in report['devices']:
    		        print '{:>8}: {:.2f}'.format(d, report['devices'][d])
    	        if 'filesize' in cmd:
    	            print '  Directory Size'
    	            print '{:>15} {:>7} {:>12}'.format(
		          'Name','Count','AvgSize')
    		    for d in report:
    	                print '{:>15} {:>7} {:>12}'.format(d, report[d][0], 
			                         report[d][1]/report[d][0])
    	        if 'cpu' in cmd:
    	            print '\n  Top Five High Memory Procs'
    		    print '{:>16} {:>8} {:>10}'.format('NAME','PID','USAGE')
    		    for i in report['memsort']:
    		        print '{:>16} {:>8} {:>10}'.format(i[0],i[1],i[3])
    	            print '\n  Top Five Longest Running Processes'
    		    print '{:>16} {:>8} {:>12}'.format('NAME','PID','TIME')
    		    for i in report['timesort']:
    		        print '{:>16} {:>8} {:>12}'.format(i[0],i[1],i[2])
    	        if 'ping' in cmd:
    		    print '\n  Ping'
    		    for i in errors[h]:
    		        if 'ping' in i:
    		            print '    Problem reaching node: {}'.format(i[2])
        print '\n\n'

	        
def make_sadf_record(sadf, delimiter=','):
    """Parse sadf results"""

    record = []
    devices = {}

    # clean up results, remove header
    sadf = sadf.strip().split('\n')
    sadf = sadf[1:]

    for ret in sadf:

	# cpu
        ret = ret.split(delimiter)
	(hostname, i, ts, cpu, user, nice, system, iowait, 
	 steal, idle, procs, cswch) = ret[:12]

	# interface
	atmptf, estres, retrans, isegerr, orsts = ret[-5:]

	cpuload = float(user) + float(nice) + float(system)
        cswch = float(cswch)
	retrans = float(retrans)

	# for each dev
	ret = ret[12:]
	ret = ret[:-5]
	while ret:
	    dev, await = ret[0], ret[6]
	    devices[dev] = float(await)
            ret = ret[9:] 
	    
	record.append((ts, hostname, cpuload, cswch, retrans, devices))

    return record

def process_results(cmd, cmd_results):
    """Apply required logic for each command result.
       Command results for sar are pre-parsed with make_sadf_record.
    """

    tmp = {}

    if 'sar' in cmd:
        records = make_sadf_record(cmd_results, delimiter=';')
	for i, rec in enumerate(records):
	    ts, hostname, cpuload, cswch, retrans, devices = rec
	    if i == 0:
	        tmp['cswch'] = cswch

		# "current_cpuload" is the first count taken by sar
		# "cpuload" is cumulative
	        tmp['current_cpuload'] = tmp['cpuload'] = cpuload
	        tmp['retrans'] = retrans
		tmp['devices'] = defaultdict(float)
		for k,v in devices.iteritems():
		    tmp['devices'][k] = v
	    else:
	        tmp['cswch'] += cswch
	        tmp['retrans'] += retrans
	        tmp['cpuload'] += cpuload
		for k,v in devices.iteritems():
		    tmp['devices'][k] += v

	# averages: cpuload, device
	tmp['cpuload'] /= len(records)
        for k,v in devices.iteritems():
	    tmp['devices'][k] /= len(records)

    elif 'filesize' in cmd:
        cmd_results = cmd_results.strip()
	for i in cmd_results.split('\n'):
	    user, count, filesize = i.split(',')
	    tmp[user] = int(count), int(filesize)
        
    elif 'cpu' in cmd:
	tmp['timesort'] = []
	tmp['memsort'] = []
        ret = cmd_results.split()
	timesort = ret[:20]
	memsort = ret[20:]
	while timesort:
	    name, pid, cputime, mem = timesort[:4]
	    tmp['timesort'].append((name, pid, cputime, mem))
	    timesort = timesort[4:]
	while memsort:
	    name, pid, cputime, mem = memsort[:4]
	    tmp['memsort'].append((name, pid, cputime, mem))
	    memsort = memsort[4:]
        
    elif 'ping' in cmd:
	# pings will only be displayed where errors occured.
	tmp['ping'] = 'ping'
        pass
    else:
        print 'Unknown command', cmd
    
    return tmp


def format_cmd(host, cmd, template):
    """Commands run on remote host are configured in the
       hostcheck_cfg.py file"""

    if 'sar' in cmd:
        ret = template.format(outfile=out_file, saroutfile=sar_outfile, 
	                      sarinterval=sar_interval, sarcount=sar_count, 
			      errfile=err_file)
    elif 'filesize' in cmd:
        ret = template.format(outfile=out_file, targetdir=target_dir, 
	                      errfile=err_file)
    elif 'cpu' in cmd:
        ret = template.format(outfile=out_file)
    elif 'ping' in cmd:
        sibling_nodes = ' '.join(set(hosts) - set([host]))
	ret = template.format(siblingnodes=sibling_nodes, outfile=out_file)
    else:
	errors[host].append('Cannot format {}: {}'.format(cmd, template))
	ret = None

    return ret


for host in hosts:

    # reset reportfile on each host
    ret = subprocess.call(['ssh', host, 
                           'cat /dev/null >{outfile} >{saroutfile}'.format(
			   outfile=out_file, saroutfile=sar_outfile)])
    if ret == 0:
        print 'Running commands on remote host', host
    else:
	errors[host].append(['Cannot reset outfile on', host])
	print 'Failed to initiate on {}, skipping '.format(host)
	continue

    # run each command on host
    for cmd in CMD_TEMPLATES:
	fcmd = format_cmd(host, cmd, CMD_TEMPLATES[cmd])
        ret = subprocess.Popen(['ssh', host, fcmd], stdout=subprocess.PIPE, 
	                       stderr=subprocess.PIPE, close_fds=True)
        stdout, stderr = ret.communicate()
	if stderr:
	    errors[host].append(['Failed on command', cmd, stderr])
        ret = process_results(cmd, stdout)
	reports[host][cmd].append(ret)

print_report(reports)

