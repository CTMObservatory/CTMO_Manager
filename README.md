# Scheduler

To install, download this repo and install the Python modules.
Preferably use a virtualenv

    $ mkvirtualenv -p python3 scheduler
    $ pip install .

The above command will install the `scheduler` module and the `epimetheus` executable.

To start the scheduler to run as a background process.

    $ epimetheus &

Notice that this will stop after the user logs out. To keep it running you can use nohup:

    $ nohup epimetheus &

To stop it, check the PID with ps and kill the process.

    $ ps -e | grep epimetheus
    $ kill [PID]

Or better yet, install it as a systemd service.

# Install scheduler as a systemd service

Python does not provide utilities to install systemd services,
but we facilitate a makefile to that end.
To install it:

    $ make
    $ sudo make install

To start, stop or restart the service, use

    $ systemctl [action] schedulerd

Where `action` is one of: `start`, `stop` or `restart`.

To uninstall:

    $ sudo make uninstall

### Test

You can test the availability of the service with `send_work_order.py` script:

    $ python3 send_work_order.py

You should see "Work order received." on the screen.
