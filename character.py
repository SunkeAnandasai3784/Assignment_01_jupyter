print("Enter a Character: ", end="")
Character = input()

word = len(Character)
if word==1:
    asc = ord(Character)
    print("\nASCII Value of \"" +(Character)+ "\" = " +str(asc))
else:
    print("\nnot yet correct check out once!")
