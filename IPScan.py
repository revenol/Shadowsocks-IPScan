# find the best server ip form 'gui-config.json'
# thanks to 'http://ghoulmind.com/2011/02/python-threading-ping/'

import os, re
import json
import subprocess
from threading import Thread 
from Queue import Queue

LOST_PATTERN = re.compile(r'Lost\s=\s(\d)', re.M)
DELAY_PATTERN = re.compile(r'Average\s=\s(\d*)', re.M)

# read in all server ip address from "gui-config.json", and save them in ip_list
ip_list = []
# store every available ip along with the corresponding delay
available_list = []


with open(os.path.join( os.path.dirname(os.path.realpath(__file__)), "gui-config.json")) as jsonfile:
	json_data = json.load(jsonfile)
	# print json_data['configs']
	for key in json_data['configs']:
		# print key['server']
		ip_list.append(key['server'])

# print ip_list

# find the best ip server
num_ping_threads = 5
queue = Queue()


def pingSingleIP(i, iq):
	while True:
		ip = iq.get()
		# print "[*]Thread %s: Pinging %s" % (i,ip) 
		# we change the default timeout value from 4000 to 500
		ret = subprocess.Popen("ping -n 5 -w 500 %s" % ip, shell = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
		
		stdout,stderr = ret.communicate()
		print 'stdout : ',stdout
		# print 'stderr : ',stderr
		
		lost_match = LOST_PATTERN.search(stdout)
		lost_count = lost_match and int(lost_match.group(1)) or 0
		# print lost_count
		if lost_count == 0:
			print "[*]%s: is alive." % ip
			delay_match = DELAY_PATTERN.search(stdout)
			delay_time = delay_match and int(delay_match.group(1))
			available_list.append((ip, delay_time))
			# print "Average delay is : ", delay_time, " ms"
		# else:
		# 	print "[*]%s: did not respond" % ip


		
		iq.task_done()

if __name__ == '__main__':
	for ip in ip_list:
		print ip
		queue.put(ip)

	for i in range(num_ping_threads):
		worker = Thread(target = pingSingleIP, args = (i, queue))
		worker.setDaemon(True)
		worker.start()

	print "[*]Main Thred Waiting"
	queue.join()

	print "[*]Done!"

	print available_list

	min_delay = 1000
	best_item = []

	for item in available_list:
		if item[1] < min_delay:
			min_delay = item[1]
			best_item = item

	print "The best server (ip, delay in ms) : ", best_item

	os.system("pause")


