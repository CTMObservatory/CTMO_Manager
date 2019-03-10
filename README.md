# Scheduler

To install, clone this repo and run the makefile.
Preferably use a virtual environment

    $ git clone https://github.com/CTMObservatory/Scheduler.git
    $ mkvirtualenv -p python3 scheduler
    $ make
    $ sudo make install

Installation requires root privilege.

# Start the schedulerd service with systemctl

To start, stop or restart the service, use

    $ systemctl [action] schedulerd

Where `action` is one of: `start`, `stop` or `restart`.

# To clean and uninstall:

    $ make clean
    $ sudo make uninstall

# Test

You can test the availability of the service with `send_work_order.py` script:

    $ python3 send_work_order.py

You should see "Work order received." printed on the screen.
