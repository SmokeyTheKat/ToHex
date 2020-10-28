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
		try: print(hex(int(ags[1])))
		except: print("NOT A NUMBER")
		return
	else:
		while True:
			try: print(hex(int(input("# "))))
			except: continue




if "-help" in ags or "--help" in ags or agsc <= 1:
	chelp = True
	print("ToHex:")
	print("    EX:")
	print("        ToHex 4          - returns 0x4")
	print("        ToHex 3295       - returns 0xcdf")
	print("        ToHex -term      - continous entries")
	print("")
	print("")

if "-term" in ags:
	term = True

main()
