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
