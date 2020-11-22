ltt = {
" ": "=" ,
"a": "zy",
"b": "yx",
"c": "xv",
"d": "vu",
"e": "ut",
"f": "ts",
"g": "sr",
"h": "rq",
"i": "qp",
"j": "po",
"k": "on",
"l": "nm",
"m": "ml",
"n": "lk",
"o": "jk",
"p": "kj",
"q": "ji",
"r": "ih",
"s": "hg",
"t": "gf",
"u": "fe",
"v": "ed",
"w": "xd",
"x": "dc",
"y": "cb",
"z": "ba",
"!": "~"
}


ltt2 = {
 "=":" ",
"zy":"a", 
"yx":"b",
"xv":"c",
"vu":"d",
"ut":"e",
"ts":"f",
"sr":"g",
"rq":"h",
"qp":"i",
"po":"j",
"on":"k",
"nm":"l",
"ml":"m",
"lk":"n",
"jk":"o",
"kj":"p",
"ji":"q",
"ih":"r",
"hg":"s",
"gf":"t",
"fe":"u",
"ed":"v",
"xd":"w",
"dc":"x",
"cb":"y",
"ba":"z",
"~" :"!",
"1" :""
}

def enc():
	ui = input("Enter a msg encrypt: ")
	ot = ""

	for x in ui:
		ot += ltt.get(x)+"1"
	print("\n"+">>>  "+ot+"  <<<")
	print("Message encrypted successfully!")

def dec():
	ui = input("Enter a msg decrypt: ")
	ot = ""

	for x in ui:
		ot += ltt2.get(x)+"1"
	print("\n"+">>>  "+ot+"  <<<")
	print("Message decrypted successfully!")


#while True:

print("""
SPY MESSAGE's hider
by: Anikin Luke

Hide a message   == [1]
Unhide a message == [2]


""")
#Exit ----------  == [3]

useri = str(input("Select a number 1/2: "))

if(useri == "1"):
	enc()

elif(useri == "2"):
	dec()

#elif(useri == "3"):
#	print("exiting..")
		
else:
	print("Error! wrong input!!\n")