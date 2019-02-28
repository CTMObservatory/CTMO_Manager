# Scheduler

To install, download this repo and install:

    $ pip install .

Then summon Epimetheus

    $ epimetheus &

### Test

You can test the availability of the service with `send_work_order.py` script:

    $ python3 send_work_order.py

You should see "Work order received." on the screen.

### To kill Epimetheus

Check the PID with ps

    $ ps -e | grep epimetheus
    $ kill [PID]

# Install scheduler as a systemd service

Python does not provide utilities to install systemd daemons,
but you can create one easily copying the `scheduler.service` file to the `systemd` directory:

    $ sudo cp scheduler.service /etc/systemd/system

To start, stop or restart the service, use

    $ systemctl epimetheus [action]

Where `action` is one of `start`, `stop` or `restart`
