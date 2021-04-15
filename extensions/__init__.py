from time import gmtime, strftime


class term:
	HEADER = '\033[95m'
	OKBLUE = '\033[94m'
	OKCYAN = '\033[96m'
	OK = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'
	NONE = ''


class output():
	def log(self, color, text):
		current = strftime("%H:%M:%S", gmtime())
		print(f"[{current}]: {color} {text} {term.ENDC}")
		
		