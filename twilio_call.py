#! /usr/bin/env python3.3
import sched, time
from datetime import datetime
from twilio.rest import TwilioRestClient


def send_message():
	account_sid = "AC3e245acb15c1325f3760b6ec00788037"
	auth_token  = "xxxxxx" # need private password to work

	number_to_call = "+15554195448"
	number_to_call_from = "+14253364642"

	# make call
	client = TwilioRestClient(account_sid, auth_token)
	call = client.calls.create(
			url="http://www.kwirky.ca/cgi-bin/jana.py",
	    to=number_to_call,
	    from_=number_to_call_from,
	    method="GET"
	)

	print "calling " + number_to_call + " from " + number_to_call_from

def make_call():
	# get the seconds from now until the call time
	call_time = datetime(2013, 11, 21, 21, 34)
	current_time = datetime.now()
	seconds_until_call = 1     #int((call_time - current_time).total_seconds())

	# schedule the call
	s = sched.scheduler(time.time, time.sleep)
	s.enter(seconds_until_call, 1, send_message, ())
	s.run()


make_call()
