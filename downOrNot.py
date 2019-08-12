"""
Simple Python Script to check if website is UP or DOWN
 >> Made by Anna Kushina , just for fun :)

 Version: v0.1
 Open Source
"""

#import system modules for system commands
import platform
import os
import sys

#main checkers
import validators #for checking url
import requests #for getting url response
import socket #checking internet connecttion

#import colorama, for better ui and script look
from colorama import init 
from colorama import Fore, Style

#initialize colorama
init()

class DownOrNot():
	def __init__(self, webUrl, rawUrl):
		super(DownOrNot, self).__init__()
		self.__web = rawUrl
		self.__reqUrl = webUrl
		self.__reqHeaders = {
			"User-Agent": "downOrNot (Website UP or DOWN Checker)"
		}
		self.__tryCheck = 2

	def run(self):
		print(Fore.YELLOW + "\n\t\t  [i] Checking " + Fore.CYAN + self.__reqUrl + Fore.YELLOW + " validity...")
		try:
			print(Fore.YELLOW + "\t\t  [i] Getting response...")
			__response = requests.head(self.__reqUrl, timeout=5, stream=True, allow_redirects=True, headers=self.__reqHeaders)
			__webStatusCode = __response.status_code

			#print output in the screen
			print(Fore.CYAN + "\n\n\t\t    ---> Result: ")
			print(Fore.CYAN + "\t\t\t  [i] Host: " + Fore.GREEN + self.__web)
			print(Fore.GREEN + "\n\t\t\t  [ok] Website is UP!")
			print(Fore.GREEN + "\t\t\t  [ok] Response: " + str(__webStatusCode))
			print(Style.RESET_ALL + "\t\t  ----------------------------------")
		except Exception:
			print(Fore.LIGHTRED_EX + "\n\n\t\t  [!] Connection REFUSED! Website may be DOWN...")
			try:
				print(Fore.YELLOW + "\t\t    [i] Retrying...")
				if checkNet() == False:
					print(Fore.RED + "\n\t\t  [!] INTERNET Connection was reset!")
				else:
					self.__tryCheck -= 1
					if self.__tryCheck == 0:
						#print output in the screen
						print(Fore.CYAN + "\n\n\t\t    ---> Result: ")
						print(Fore.CYAN + "\t\t\t  [i] Host: " + Fore.GREEN + self.__web)
						print(Fore.LIGHTRED_EX + "\n\t\t\t  [ok] Website is DOWN!")
						print(Fore.LIGHTRED_EX + "\t\t\t  [ok] Response: NO RESPONSE")
						print(Style.RESET_ALL + "\t\t  ---------------------------------------")
					else:
						self.run() #rerun script
			except Exception as netErr:
				print(Fore.RED + "\n\t\t  [!]Error!", netErr)
			print(Style.RESET_ALL)

#check for internet connection
def checkNet():
	try:
        # connect to the host -- tells us if the host is actually reachable
		socket.create_connection(("www.google.com", 80))
		socket.create_connection(("www.google.com", 443))
		return True
	except OSError:
		pass
	return False

def checkOs():
	try:
		osName = platform.system()
		if osName == 'Windows':
			return os.system("cls")
		else:
			return os.system("clear")
	except Exception as e:
		print(Fore.RED + "\n\t\t  [!] An Error has occurred!", e)

def __startChecker(url, inUrl):
	if not validators.url(url):
		print(Fore.RED + "\n\t\t  [!] Url is not valid! Try again...")
	else:
		__d0wnCheck3r = DownOrNot(url, inUrl)
		__d0wnCheck3r.run()
def __getUrl(initUrl):
	if initUrl.startswith("http://") or initUrl.startswith("https://"):
		__rUrl = initUrl.replace("http://", "").replace("https://", "")
		__startChecker(initUrl, __rUrl)
	else:
		__startChecker("http://" + initUrl, initUrl)

def __interHandler():
	try:
		print(Fore.YELLOW)
		__exit = "no"
		while __exit != "n" or __exit != "no":
			__exit = input("\n\t\t  [i] Do you want to exit? (Y/n) ~#: ")
			if __exit == "y" or __exit == "yes":
				checkOs()
				print(Fore.YELLOW + "\n\t  [i] Exiting... Goodbye! :)")
				sys.exit(0)
			elif __exit == "n" or __exit == "no":
				main()
			elif __exit == "" or __exit == None:
				pass
			else:
				pass
	#catch all tracebacks
	except Exception:
		pass #do nothing

def banner():
	__mainBanner = """

	      d8b                                                                            
	      88P                                                                       d8P  
	     d88                                                                     d888888P
	 d888888   d8888b  ?88   d8P  d8P  88bd88b      d8888b       88bd88b  d8888b   ?88'  
	d8P' ?88  d8P' ?88 d88  d8P' d8P'  88P' ?8b    d8P' ?88      88P' ?8bd8P' ?88  88P   
	88b  ,88b 88b  d88 ?8b ,88b ,88'  d88   88P    88b  d88     d88   88P88b  d88  88b   
	`?88P'`88b`?8888P' `?888P'888P'  d88'   88b    `?8888P'    d88'   88b`?8888P'  `?8b  
	                      
	                 Down or Not [Website Response CHecker] v0.1                                                 
		                                                                                     
	"""
	return __mainBanner
def main():
	try:
		checkOs() #clear the screen
		print(Fore.CYAN + banner() + Style.RESET_ALL)
		print(Fore.GREEN + "\t\t  Enter the url to be checked, for example: 'www.google.com'. \n\t\t\t Type '00' or 'exit' to exit the script...")
		__url = "www.google.com"
		while __url != "00":
			print(Fore.BLUE)
			__url = input("\n\t\t\t  [downOrNot] url ~#: ")
			if __url == '' or __url == None:
				pass
			elif __url == '00' or __url == 'exit':
				checkOs()
				print(Fore.YELLOW + "\n\t  [i] Exiting... Goodbye! :)")
				sys.exit(0)
			else:
				__getUrl(__url)
	except KeyboardInterrupt:
		__interHandler()
	except EOFError:
		__interHandler()
	except Exception:
		pass #do nothing with other errors

if __name__ == '__main__':
	#check internet connection
	print(Fore.YELLOW + "\n\t  [i] Checking presequites...")
	if checkNet() == False:
		print(Fore.RED + "\t  [!] An Internet Connection is required for this script to run!")
	else:
		#if internet is present, run main script
		main()