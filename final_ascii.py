def ascii_art(artify):
	k=50
	run = []
	runer=""
	import os
	artify = str(artify).lower()
	out1=[]
	out2=[]
	out3=[]
	out4=[]
	varsis = 1
	out5=[]
	for i in run:
		for x in i:
			if k >= varsis-10:
				for x in out1:
					print(x,end="",flush=True)
				print()
				for x in out2:
					print(x,end="",flush=True)
				print()
				for x in out3:
					print(x,end="",flush=True)
				print()
				for x in out4:
					print(x,end="",flush=True)
				print()
				for x in out5:
					print(x,end="",flush=True)
				print()
				print("\n\n")
				out1=[]
				out2=[]
				out3=[]
				out4=[]
				out5=[]
				k=0
			if x == "a":
				out1.append(" █████ ")
				out2.append("██   ██")
				out3.append("███████")
				out4.append("██   ██")
				out5.append("██   ██")
				k+=7
			elif x == "b":
				out1.append("██████ ")
				out2.append("██   ██")
				out3.append("██████ ")
				out4.append("██   ██")
				out5.append("██████ ")
				k+=7
			elif x == "c":
				out1.append(" ██████")
				out2.append("██     ")
				out3.append("██     ")
				out4.append("██     ")
				out5.append(" ██████")
				k+=7
			elif x == "d":
				out1.append("██████ ")
				out2.append("██   ██")
				out3.append("██   ██")
				out4.append("██   ██")
				out5.append("██████ ")
				k+=7
			elif x == "e":
				out1.append("███████")
				out2.append("██     ")
				out3.append("█████  ")
				out4.append("██     ")
				out5.append("███████")
				k+=7
			elif x == "f":
				out1.append("███████")
				out2.append("██     ")
				out3.append("█████  ")
				out4.append("██     ")
				out5.append("██     ")
				k+=7
			elif x == "g":
				out1.append(" ██████ ")
				out2.append("██      ")
				out3.append("██   ███")
				out4.append("██    ██")
				out5.append(" ██████ ")
				k+=7
			elif x == "h":
				out1.append("██   ██")
				out2.append("██   ██")
				out3.append("███████")
				out4.append("██   ██")
				out5.append("██   ██")
				k+=7
			elif x == "i":
				out1.append("██")
				out2.append("██")
				out3.append("██")
				out4.append("██")
				out5.append("██")
				k+=2
			elif x == "j":
				out1.append("     ██")
				out2.append("     ██")
				out3.append("     ██")
				out4.append("██   ██")
				out5.append(" █████ ")
				k+=7
			elif x == "k":
				out1.append("██   ██")
				out2.append("██  ██ ")
				out3.append("█████  ")
				out4.append("██  ██ ")
				out5.append("██   ██")
				k+=7
			elif x == "l":
				out1.append("██     ")
				out2.append("██     ")
				out3.append("██     ")
				out4.append("██     ")
				out5.append("███████")
				k+=7
			elif x == "m":
				out1.append("███    ███")
				out2.append("████  ████")
				out3.append("██ ████ ██")
				out4.append("██  ██  ██")
				out5.append("██      ██")
				k+=10
			elif x == "n":
				out1.append("███    ██")
				out2.append("████   ██")
				out3.append("██ ██  ██")
				out4.append("██  ██ ██")
				out5.append("██   ████")
				k+=9
			elif x == "o":
				out1.append(" ██████ ")
				out2.append("██    ██")
				out3.append("██    ██")
				out4.append("██    ██")
				out5.append(" ██████ ")
				k+=8
			elif x == "p":
				out1.append("██████ ")
				out2.append("██   ██")
				out3.append("██████ ")
				out4.append("██     ")
				out5.append("██     ")
				k+=7
			elif x == "q":
				out1.append(" ██████ ")
				out2.append("██    ██")
				out3.append("██ ▄▄ ██")
				out4.append(" ██████ ")
				out5.append("    ▀▀  ")
				k+=8
			elif x == "r":
				out1.append("██████ ")
				out2.append("██   ██")
				out3.append("██████ ")
				out4.append("██   ██")
				out5.append("██   ██")
				k+=7
			elif x == "s":
				out1.append("███████")
				out2.append("██     ")
				out3.append("███████")
				out4.append("     ██")
				out5.append("███████")
				k+=7
			elif x == "t":
				out1.append("████████")
				out2.append("   ██   ")
				out3.append("   ██   ")
				out4.append("   ██   ")
				out5.append("   ██   ")
				k+=7
			elif x == "u":
				out1.append("██    ██")
				out2.append("██    ██")
				out3.append("██    ██")
				out4.append("██    ██")
				out5.append(" ██████ ")
				k+=7
			elif x == "v":
				out1.append("██    ██")
				out2.append("██    ██")
				out3.append("██    ██")
				out4.append(" ██  ██ ")
				out5.append("  ████  ")
				k+=7
			elif x == "w":
				out1.append("██     ██")
				out2.append("██     ██")
				out3.append("██  █  ██")
				out4.append("██ ███ ██")
				out5.append(" ███ ███ ")
				k+=9
			elif x == "x":
				out1.append("██   ██")
				out2.append(" ██ ██ ")
				out3.append("  ███  ")
				out4.append(" ██ ██ ")
				out5.append("██   ██")
				k+=7
			elif x == "y":
				out1.append("██    ██")
				out2.append(" ██  ██ ")
				out3.append("  ████  ")
				out4.append("   ██   ")
				out5.append("   ██   ")
				k+=7
			elif x == "z":
				out1.append("███████")
				out2.append("   ███ ")
				out3.append("  ███  ")
				out4.append(" ███   ")
				out5.append("███████")
				k+=7
			elif x == "1":
				out1.append(" ██")
				out2.append("███")
				out3.append(" ██")
				out4.append(" ██")
				out5.append(" ██")
				k+=3
			elif x == "2":
				out1.append("██████ ")
				out2.append("     ██")
				out3.append(" █████ ")
				out4.append("██     ")
				out5.append("███████")
				k+=7
			elif x == "3":
				out1.append("██████ ")
				out2.append("     ██")
				out3.append(" █████ ")
				out4.append("     ██")
				out5.append("██████ ")
				k+=7
			elif x == "4":
				out1.append("██   ██")
				out2.append("██   ██")
				out3.append("███████")
				out4.append("     ██")
				out5.append("     ██")
				k+=7
			elif x == "5":
				out1.append("███████")
				out2.append("██     ")
				out3.append("███████")
				out4.append("     ██")
				out5.append("███████")
				k+=7
			elif x == "6":
				out1.append(" ██████ ")
				out2.append("██      ")
				out3.append("███████ ")
				out4.append("██    ██")
				out5.append(" ██████ ")
				k+=7
			elif x == "7":
				out1.append("███████")
				out2.append("     ██")
				out3.append("    ██ ")
				out4.append("   ██  ")
				out5.append("   ██  ")
				k+=7
			elif x == "8":
				out1.append(" █████ ")
				out2.append("██   ██")
				out3.append(" █████ ")
				out4.append("██   ██")
				out5.append(" █████ ")
				k+=7
			elif x == "9":
				out1.append(" █████ ")
				out2.append("██   ██")
				out3.append(" ██████")
				out4.append("     ██")
				out5.append(" █████ ")
				k+=7
			elif x == "0":
				out1.append(" ██████ ")
				out2.append("██  ████")
				out3.append("██ ██ ██")
				out4.append("████  ██")
				out5.append(" ██████ ")
				k+=7
			elif x == ".":
				out1.append("  ")
				out2.append("  ")
				out3.append("  ")
				out4.append("  ")
				out5.append("██")
				k+=2
			elif x == "!":
				out1.append("██")
				out2.append("██")
				out3.append("██")
				out4.append("  ")
				out5.append("██")
				k+=2
			elif x == "?":
				out1.append("██████ ")
				out2.append("     ██")
				out3.append("  ▄███ ")
				out4.append("  ▀▀   ")
				out5.append("  ██   ")
				k+=7
			elif x == ":":
				out1.append("  ")
				out2.append("██")
				out3.append("  ")
				out4.append("██")
				out5.append("  ")
				k+=2
			elif x == " ":
				out1.append("     ")
				out2.append("     ")
				out3.append("     ")
				out4.append("     ")
				out5.append("     ")
				k+=5
			out1.append("  ")
			out2.append("  ")
			out3.append("  ")
			out4.append("  ")
			out5.append("  ")
			k+=2
		print(k)
		out1=[]
		out2=[]
		out3=[]
		out4=[]
		out5=[]
ascii_art("programer")