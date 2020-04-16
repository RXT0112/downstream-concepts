#!/usr/bin/python3

###! Abstract: Provide a wrapper that terminates the shell and outputs a helpful message
###!
###! SYNOPSIS: die [arg] (message)
###!
###! Example:
###!
###!    user@example~$ die 1 "message" (FIXME: Proper command required)
###!    FATAL: message
###!
###! Additional info:
###! - End-users are expecte to have the ability to set format string using '$PALUDIS_DIE_FORMAT' in $paludisdir/(FIXME: where?)

# FIXME-QA: Stub implementation, QA required

import sys

def die(arg, message):
	def errorCode(arg):
		switcher = {
			1:print("FATAL: %s", message),
	}

	sys.exit(arg)