# import random
import unittest
import commands
from commands import parse

''' This section is illustrative of why test driven development works for this problem '''
class TestCommandsFunctions(unittest.TestCase):
    def setUP(self):
        pass

    ### AFFECT ###

    def test_affect(self):
        self.assertEqual(commands.parse("aff"), "Nothing")

    def test_affect_where_affected(self):
        pass

    ### AREAS ###

    def test_areas(self):
        self.assertEqual(commands.parse("areas"), "Example area listing needed")

    ### BALANCE ###

    def test_balance_where_bank_exists(self):
        self.assertEqual(commands.parse("balance"), "Example output needed")

    def test_balance_where_bank_does_not_exist(self):
        self.assertEqual(commands.parse("balance"), "There is no bank here")

    ### DEPOSIT ###

    def test_deposit_where_bank_exists(self):
        self.assertEqual(commands.parse("deposit 1000"), "Example output needed")

    def test_deposit_where_bank_does_not_exist(self):
        self.assertEqual(commands.parse("deposit 1000"), "There is no bank here")

    def test_deposit_no_arguments(self):
        self.assertEqual(commands.parse("deposit"), "No arguments found")

    def test_deposit_bad_arguments(self):
        self.assertEqual(commands.parse("deposit waaaghh"), "Problem with input")

    ### COMMANDS ###

    def test_commands(self):
        self.assertEqual(commands.parse("command"), "Example output needed")

    ### CONFIG ###

    def test_config(self):
        self.assertEqual(commands.parse("config"), "Example output needed")

    def test_consider(self):
        self.assertEqual(commands.parse("consider thargrugrog"), "Example output needed")

    ### DELETE ###

    def test_delete(self):
        self.assertEqual(commands.parse("delete"), "Delete successful!")
    
    ### DESC ###
    
    def test_desc(self):
        self.assertEqual(commands.parse("desc"), "Example description needed")

    def test_desc_with_argument(self):
        self.assertEqual(commands.parse("desc You look like a beautiful mermaid!"), "Example output needed")

    ### DICE ###

    def test_dice(self):
        self.assertEqual(commands.parse("dice 1d6"), range(6))

    def test_dice_without_argument(self):
        self.assertEqual(commands.parse("dice"), "No arguments provided")

    def test_dice_with_messy_argument(self):
        self.assertEqual(commands.parse("dice waaaghh"), "Problem with input")

    ### DROP ###

    def test_drop(self):
        self.assertEqual(commands.parse("drop longsword"), "You drop a longsword")

    def test_drop_without_argument(self):
        self.assertEqual(commands.parse("drop"), "Arguments needed")

    def test_drop_item_not_in_inventory(self):
        self.assertEqual(commands.parse("drop frogsword"), "You cannot find that item")

    ### EAST ###

    def test_east(self):
        self.assertEqual(commands.parse("east"), "You go east")

    def test_east_is_locked(self):
        self.assertEqual(commands.parse("east"), "East is locked.")

    def test_east_cannot_be_moved_to(self):
        self.assertEqual(commands.parse("east"), "Cannot go east.")

    ### ECHO ###

    def test_echo(self):
        self.assertEqual(commands.parse("echo blah blah blah"), "blah blah blah")

    def test_echo_without_argument(self):
        self.assertEqual(commands.parse("echo"), "Echo what?")

    ### EMOTE ###

    def test_emote(self):
        self.assertEqual(commands.parse("emote You grit your teeth"), "You grit your teeth")

    ### EXCLAMATION MARK ###

    def test_exclamation_mark(self):
        self.assertEqual(commands.parse("!"), "Example output needed")

    def test_exclamation_mark_should_fail(self):
        self.assertEqual(commands.parse("!"), "Wrong output needed")

    ### EXITS ####

    def test_exits(self):
        self.assertEqual(commands.parse("exits"), "Example output needed")
   
    def test_exits_with_argument(self):
        self.assertEqual(commands.parse("exits north"), "Example output needed")

    ### GET ###

    def test_get(self):
        self.assertEqual(commands.parse("get longsword"), "You get a longsword")

    def test_get_without_arguments(self):
        self.assertEqual(commands.parse("get"), "Get what?")

    ### HELP ###

    def test_help(self):
        self.assertEqual(commands.parse("help"), "Help takes 1 parameter. If the parameter is dir then the help directory is shown. If it is not dir, then it will search the help files for a match")

    def test_help_dir(self):
        self.assertEqual(commands.parse("help dir"), "Example output needed")

    def test_help_search(self):
        self.assertEqual(commands.parse("help test"))

    def test_help_parameter_is_a_number(self):
        self.assertEqual(commands.parse("help 000"), "Example output needed")

    ### INVENTORY ###

    def test_inventory(self):
        self.assertEqual(commands.parse("inventory"), "Example output needed")

    def test_inventory_get_by_type(self):
        self.assertEqual(commands.parse("inventory sword"), "Example output needed")

    ### LADDER ###

    def test_ladder(self):
        self.assertEqual(commands.parse("ladder"), "Example output needed")

    ### LAST SEEN ###

    def test_lastseen(self):
        self.assertEqual(commands.parse("lastseen thargrugrug"), "Example output needed")

    def test_lastseen(self):
        self.assertEqual(commands.parse("lastseen"), "Example output needed")

    ### LIMITED ###

    def test_limited(self):
        self.assertEqual(commands.parse("limited"), "Example output needed")

    def test_limited_show_by_type(self):
        self.assertEqual(commands.parse("limited sword"), "Example output needed")

    ### LOOK ###

    def test_look(self):
        self.assertEqual(commands.parse("look"), "Example output needed")

    def test_look_with_arguments(self):
        self.assertEqual(commands.parse("look sword"), "Example output needed")

    ### MARCHING ###
    def test_marching(self):
        self.assertEqual(commands.parse("marching front"))

if __name__ == '__main__':
    unittest.main()