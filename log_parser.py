import re

file = "./data/rsvp_agent_log.dat"

with open(file, "r") as data_file:
	for x in data_file:
		y = re.search("WARNING", x)
		if y == None:
			pass
		else:
			print(str(x[0:14])+" --"+str(re.split(":",x)[4]))
