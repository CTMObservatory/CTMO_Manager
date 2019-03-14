# CTMO Manager :telescope:

## Installation

To install, clone this repo and run the makefile.
Preferably use a virtual environment

    $ git clone https://github.com/CTMObservatory/CTMO_Manager.git
    $ mkvirtualenv -p python3 ctmo
    $ make
    $ sudo make install

Installation requires root privilege.

## Start any service with systemctl

To start, stop or restart a service, use

    $ systemctl [action] [service]

Where `action` is one of: `start`, `stop` or `restart`
and service is any of `telescoped` or `schedulerd`.

## To clean and uninstall:

    $ make clean
    $ sudo -H make uninstall

## Test

You can test the availability of the service with `send_work_order.py` script:

    $ python3 send_work_order.py

You should see "Work order received." printed on the screen.
