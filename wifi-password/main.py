import subprocess
import os

def read_file(filename):
	with open(filename, "r") as f:
		for line in f.readlines():
			if "name" in line:
				wifi_name = line.strip()[6:-7]
			if "keyMaterial" in line:
				wifi_pw = line.strip()[13:-14]
	return wifi_name , wifi_pw

def main():
	result = subprocess.run(["netsh", "wlan", "export", "profile", "key=clear"], 
                        capture_output= True, text=True)
	if result.returncode != 0:
		return
	path = os.getcwd()
	wifi_list = {}
	output_file = "wifi_passwords.txt"

	for filename in os.listdir(path):
		if filename.startswith("Wi-Fi") and filename.endswith(".xml"):
			wifi_name , wifi_pw = read_file(filename)
			wifi_list[wifi_name] = wifi_pw
			os.remove(filename)
	with open(output_file, "w") as f:
		for wifi_name, wifi_pw in wifi_list.items():
			f.write(wifi_name + " : " + wifi_pw + "\n")

if __name__ == "__main__":
	main()
