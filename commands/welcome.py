welcome_msg = """Welcome to the irc channel of JIIT-OSDC. See http://opensource.jiitu.org/wiki/ and  http://groups.google.com/group/jiitlug. Chat away freely in the spirit of foss."""

def welcome(bot):
	bot.connection.privmsg(bot.CHANNEL, welcome_msg.lstrip())

command_description = [("welcome", welcome, tuple())]

