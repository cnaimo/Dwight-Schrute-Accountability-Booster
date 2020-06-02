[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

[![HitCount](http://hits.dwyl.io/cnaimo/Dwight-Schrute-Accountability-Booster.svg)](http://hits.dwyl.io/cnaimo/Dwight-Schrute-Accountability-Booster) [![PyPI license](https://img.shields.io/pypi/l/ansicolortags.svg)](https://pypi.python.org/pypi/ansicolortags/) [![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com) [![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/dwyl/esta/issues)  


# Dwight-Schrute-Accountability-Booster
This project was created to simulate the Dunder Mifflin Scranton accountability booster using Python. All credit for creative inspiration
goes to NBC and the cast and crew of The Office.

# Usage
Clone this repository and edit config.py to include a valid gmail and password, a recipient email address for the doomsday email, and
your preferred host IP and port number for Flask. Run accountability_booster.py. HTTP requests can be sent to two endpoints to add strikes and retrieve office stats.
Each mistake made in the office is one strike, five strikes in one day is a home run, one home run and you're out! When one home run
is reached, an email will automatically be sent at 5PM containing the contents of the email_attachment_docs folder which should contain
a negative consultant report and a series of sensitive emails from the office staff.

# TODO
* add option to block minesweeper





