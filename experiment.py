from worldbuilder.models import Character

def help(fileNumber): # Takes in a fileNumber and outputs it
    with open("help"+str(fileNumber), "r") as f:
        return read_file(f)

def read_file(f):
    #reply = ""
    #for line in f:
    #    reply += line
    return ''.join(f) 

#def listAllHelp():
#    reply = ""
#    for root,dirs,files in os.walk(os.getcwd()): 
#        for f in files:
#            if f.startswith("help"):
#                print "f: "+f
#                reply += (f+"\n")
#                helpfile=open(f, 'r')
#                if helpfile.readline() == tokens[1]:
#                    reply = readFileToReply(helpfile)
#                helpfile.close()   
#    return reply 

# Goes through every file in the current working directory looking to see if they start with "help". If it does, it prints it to the server console.
#def list_files():
#    for root,dirs,files in os.walk(os.getcwd()):
#        for f in files:
#            if f.startswith("help"):
#            	print "f: "+f

def prompt():
	return "{name} {characterClass} {level} hp: {currentHP}/{maxHP} ac: {ac} fort/ref/will: {fort}/{ref}/{will} status: {status}".format(name=name(), characterClass=character_class(), level=level(), currentHP=current_hp(), maxHP=max_hp(), ac=ac(), fort=fort(), ref=ref(), will=will(), status=status())

# Each of these functions returns an attribute of the character
def name():
	return "bob marley"
def character_class():
	return "fighter"
def level():
	return "2"
def current_hp():
	return "2"
def max_hp():
	return "12"
def ac():
	return "18"
def fort():
	return "4"
def ref():
	return "1"
def will():
	return "2"
# This function may end up bringing up a list of status effects, which is fine.
def status():
	return "BLEEDING"
print prompt()

def make_character_session():
    state = NEW_SESSION
    if newSession():      
        ask_for_character_name()
        state = NAMED
        if character_name in list_of_characters:
            ask_for_password()
            state = LOGGED_IN
        else:
            make_password()
            state = NEED_RACE
            state = NEED_CLASS
            state = NEED_HOMELAND
            state = LOGGED_IN



  # if new_session then ask for character name
  #     if old_character_name then ask for password
  #         if password_is_wrong then state incorrect password and close the session
  #     elif new_character_name then ask for password
  #         once password received, ask for race
  #         once race received, ask for class
  #         once class received, ask for hometown

# if the web browser's login matters, then:
# if new_session then ask for character name
#     if old_character_name then ask for password
#         if password_is_wrong then state incorrect password and close the session
#     elif new_character_name then ask for password
#         once password received, ask for race
#         once race received, ask for class
#         once class received, ask for hometown