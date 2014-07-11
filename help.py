# help.py

# Takes in a fileNumber and outputs it. The input must be clean.
# It is good practice to use the with keyword when dealing with file objects.
# This has the advantage that the file is properly closed after its suite finishes, even if an exception is raised on the way.
# It is also much shorter than writing equivalent try-finally blocks.
def help(fileNumber): 
    with open("help"+str(fileNumber), "r") as f:  
        return read_file(f)

def read_file(f):
    return ''.join(f) 

# Strips the space and newline from a token.
def clean(token):
	return token.strip(' \n')

# This function is called by the commands.py file, which in turn is called by the server.py file.
# It calls the other functions in this file.
def cmd_help(tokenised):
	print tokenised
	# ['help', '\n']
	if tokenised[1] == '\n': 						
		return "Help requires arguments. For more information, type: help help\n"
	elif tokenised[1] == 'help \n': 													# This is required since the data format from the client is like this: ['help', 'help \n']
		return "You successfully typed help help. Despite this, its not very useful\n"
	else: 
		return help(clean(tokenised[1]))
