import sys
#import importlib

sys.path.append("commands")

command_modules = [
#    "batima",
#    "bandeco",
#    "chuck",
    "fortune",
    "leave",
    "list",
    "welcome",
]

commands = []
for cmd in command_modules:
	mod = __import__(cmd)
	
	commands.extend(mod.command_description)
