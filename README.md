# CTMO Manager :telescope:

## Installation

To install, clone this repo and run the makefile.
Preferably use a virtual environment

    $ git clone https://github.com/CTMObservatory/CTMO_Manager.git
    $ cd CTMO_Manager
    $ mkvirtualenv -p python3 ctmo
    $ make
    $ sudo make install

Installation requires root privilege.

## Start any service with systemctl

Once the system is properly configured, you can start, stop or restart any of the services.

### In Linux OS:

    $ systemctl [action] [service]

Where `action` is one of: `start`, `stop` or `restart`
and service is any of `telescoped` or `schedulerd`.

### In MacOS:

    $ launchctl load /Library/LaunchAgents/org.ctmo.scheduler

To stop use `unload` instead.

## To clean and uninstall:

    $ make clean
    $ sudo -H make uninstall

## Test

You can test the availability of the service with `send_work_order.py` script:

    $ python3 send_work_order.py

You should see "Work order received." printed on the screen.
