# commands.py
from help import cmd_help
from cmds import *
#from create import create_character
# Reads the raw data, pattern matches against it to determine how to act, and then replies with the appropriate response. The first word is ALWAYS the command.
''' This command reads the data sent from the client to the server, parses it, and determines from that how to respond. Its response is a simple string return. So this function takes a string and returns a string '''
def parse(rawData):
	tokens = rawData.split(' ',1)
	command = tokens[0]
	args = tokens
	args.pop(0)
	response = "Command not found.\n"
	if command == "help": 
		response = cmd_help(tokens)
	elif command == "look":
		if len(tokens) >= 2:
			response = cmds.look.observe(tokens[1])
		else:
			response = cmds.look.look()
	elif command == "echo":
		if len(tokens >= 2):
			response = cmds.echo.echo(args)
		else:
			response = "No arguments found"
	#elif command == "name":
	#	return create_character(tokens)
	return response

def run(command):
	# Run the file based off the name of the command. Get the output.
	pass
