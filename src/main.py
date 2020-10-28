import sys
import os
import time

ags = sys.argv
agsc = len(ags)

term = False
chelp = False


def main():
	if chelp: return
	if not term:
		try:
			v = ags[1]
			if v[0] == '0' and v[1] == 'x':
				print(str(int(int(v, 16))))
			else: print(str(hex(int(v))))
		except: print("NOT A NUMBER")
		return
	else:
		while True:
			try: 
				v = input("# ")
				if v == "exit": return
				if v[0] == '0' and v[1] == 'x':
					print(str(int(int(v, 16))))
				else: print(str(hex(int(v))))
			except: continue




if "-help" in ags or "--help" in ags or agsc <= 1:
	chelp = True
	print("ToHex:")
	print("    EX:")
	print("        ToHex 4          - returns 0x4")
	print("        ToHex 3295       - returns 0xcdf")
	print("        ToHex 0xc6a3      - returns 50851")
	print("        ToHex -term      - continous entries")
	print("    To exit \"-term\" mode, type exit anytime.")
	print("")
	print("")

if "-term" in ags:
	term = True

main()
