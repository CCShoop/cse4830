import os

for vuln in os.listdir("vulns/"):
	if(vuln != "flag.txt" and vuln[:2] != "._"):
		#print(vuln)
		os.system("python3 aeg.py BIN=vulns/"+str(vuln))