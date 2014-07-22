# commands.py
import cmds.aff
import cmds.areas
import cmds.bank_balance
import cmds.bank_deposit
import cmds.commands
import cmds.config
import cmds.consider
import cmds.delete
import cmds.desc
import cmds.dice
import cmds.drop
import cmds.east
import cmds.echo
import cmds.emote
import cmds.exclamation_mark
import cmds.exits
import cmds.help
import cmds.inventory
import cmds.ladder
import cmds.lastseen
import cmds.limited
import cmds.look
import cmds.marching_order
import cmds.mercantile_browse
import cmds.mercantile_buy
import cmds.mercantile_sell
import cmds.north
import cmds.password
import cmds.prompt
import cmds.quit

#from create import create_character
# Reads the raw data, pattern matches against it to determine how to act, and then replies with the appropriate response. The first word is ALWAYS the command.
''' This command reads the data sent from the client to the server, parses it, and determines from that how to respond. Its response is a simple string return. So this function takes a string and returns a string. I ordered the if/elif nest like this such that when I type ls in the command line,  I see an alphabetical ordering of commands, and likewise the if/elif nest is alphabetical. This makes it easy to see if functionality is missing and imposes an ordered structure on the program that is unbiasable. '''

cmd_history = {}

NO_ARGUMENTS_FOUND = "No arguments found"

def parse(rawData):
	tokens = rawData.split(' ',1)
	command = tokens[0]
	args = tokens
	args.pop(0)

	response = "Command not found."
	if command == "aff":
		response = cmds.aff.what_affects_me()
	elif command == "areas":
		response = cmds.areas.areas()
	elif command == "balance":
		response = cmds.bank_balance.balance()
	elif command == "deposit":
		if (len(tokens) >= 2):
			response = cmds.bank_deposit.deposit()
		else:
			response = NO_ARGUMENTS_FOUND
	elif command == "commands":
		if (len(tokens) >= 2):
			response = cmds.commands.output_syntax_of_command(token[1])
		else:
			response = cmds.commands.commands()
	elif command == "config":
		if (len(tokens) >= 2):
			response = cmds.config.set_config(args)
		else:
			response = cmds.config.config(args)
	elif command == "consider":
		if (len(tokens) >= 2):
			response = cmds.consider.consider(token[1])
		else:
			response = NO_ARGUMENTS_FOUND
	elif command == "delete":
		response = cmds.delete.delete()
	elif command == "desc":
		if (len(tokens) >= 2):
			response = cmds.desc.desc(args)
		else:
			response = cmds.desc.view()
	elif command == "dice":
		dice_string = args[0]
		args.pop(0)
		response = args+" "+cmds.dice.dice(dice_string)
	elif command == "drop":
		if (len(tokens) >= 2):
			response = cmds.drop.drop_item(token[1])
		else:
			response = NO_ARGUMENTS_FOUND
	elif command == "east":
		response = cmds.east.east()
	elif command == "echo":
		if (len(tokens) >= 2):
			response = cmds.echo.echo(args)
		else:
			response = NO_ARGUMENTS_FOUND
	elif command == "emote":
		if (len(tokens) >= 2):
			response = cmds.emote.emote(args)
		else:
			response = NO_ARGUMENTS_FOUND
	elif command == "!":
		response = cmds.exclamation_mark.reuse_last_command()
	elif command == "exits":
		response = cmds.exits.exits()
	elif command == "get":
		if (len(tokens) >= 2):
			response = cmds.get.get(token[1])
		else:
			response = NO_ARGUMENTS_FOUND
	elif command == "help":
		if (len(tokens) >= 2):
			response = cmds.help.help(tokens[1])
		else:
			response = cmds.help.index()
	elif command == "inventory":
		if (len(tokens) >= 2):
			response = cmds.inventory.get_by_type(token[1])
		else:
			response = cmds.inventory.get_all()
	elif command == "ladder":
		response = cmds.ladder.ladder()
	elif command == "lastseen":
		if len(tokens) >= 2:
			response = cmds.lastseen.lastseen(tokens[1])
		else:
			response = NO_ARGUMENTS_FOUND
	elif command == "limited":
		if len(tokens) >= 2:
			response = cmds.limited.limited_by_type(tokens[1])
		else:
			response = cmds.limited.limited()
	elif command == "look":
		if len(tokens) >= 2:
			response = cmds.look.observe(tokens[1])
		else:
			response = cmds.look.look()
	elif command == "marching":
		if (len(tokens) >= 2):
			response = cmds.marching_order.set(token[1])
		else:
			response = cmds.marching_order.get()
	elif command == "browse":
		response = cmds.mercantile_browse.browse()
	elif command == "buy":
		if (len(tokens) >= 2):
			response = cmds.mercantile_buy.mercantile_buy(token[1])
		else:
			response = NO_ARGUMENTS_FOUND
	elif command == "sell":
		if (len(tokens) >= 2):
			response = cmds.mercantile_sell.mercantile_sell(token[1])
		else:
			response = NO_ARGUMENTS_FOUND
	elif command == "north":
		response = cmds.north.north()
	elif command == "password":
		if (len(tokens) >= 2):
			response = cmds.password.set_password_with(token[1])
		else:
			response = cmds.password.set_password()
	elif command == "|":
		pass
	elif command == "prompt":
		response = cmds.prompt.get_prompt()
	elif command == "quit":
		response = cmds.quit.quit()
	elif command == "remove":
		if (len(tokens) >= 2):
			response = cmds.remove.remove(token[1])
		else:
			response = NO_ARGUMENTS_FOUND
	elif command == "role":
		if len(tokens) >= 2:
			response = cmds.role.role(args)
		else:
			response = cmds.role.display()
	elif command == "say":
		if (len(tokens) >= 2):
			response = cmds.say.say(args)
		else:
			response = "Say what?"
	elif command == "scan":
		if (len(tokens) >= 2):
			response = cmds.scan.scan_direction(token[1])
		else:
			response = cmds.scan.scan_all()
	elif command == "score":
		if (len(tokens) >= 2):
			response = cmds.score.show_score(tokens[1])
		else:
			response = cmds.score.all_my_scores()
	elif command == ";":
		pass
	elif command == "sleep":
		response = cmds.sleep.sleep()
	elif command == "social":
		if (len(tokens) >= 2):
			response = cmds.social.do_social(args)
		else:
			response = cmds.social.show_all_socials()
	elif command == "south":
		response = cmds.south.south()
	elif command == "tell":
		if (len(tokens) >= 2):
			response = cmds.tell.tell(args)
		else:
			response = "Tell who what?"
	elif command == "time":
		response = cmds.time.get_time()
	elif command == "title":
		response = cmds.title.get_my_title()
	elif command == "wake":
		if (len(tokens) >= 2):
			response = cmds.wake.wake_person(token[1])
		else:
			response = cmds.wake.wake_myself()
	elif command == "wear":
		if (len(tokens) >= 2):
			response = cmds.wear.wear_item(args)
		else:
			response = "Wear what?"
	elif command == "west":
		response = cmds.west.west()
	elif command == "who":
		response = cmds.who.who_is_online()
	elif command == "wield":
		if (len(tokens) >= 2):
			response = cmds.wield.wield_weapon(token[1])
		else:
			response = "Wield what?"
	elif command == "yell":
		if (len(tokens) >= 2):
			response = cmds.yell.yell(args)
		else:
			response = "Yell what?"
	#elif command == "name":
	#	return create_character(tokens)
	return response

def archive(rawData):
	print rawData
