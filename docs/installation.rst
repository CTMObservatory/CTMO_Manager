Installing CTMO Manager
=======================

Requirements
------------

To install this software you need 

* Python 3.6 installed, preferably in a virtual environment or a local installation.
* Linux distro with systemd (most modern OS have it).
* Root or sudo access.


Installation
------------

To install, clone the CTMO Manager repo and run the makefile.
Preferably use a virtual environment::

    $ git clone https://github.com/CTMObservatory/CTMO_Manager.git
    $ cd CTMO_Manager
    $ mkvirtualenv -p python3 ctmo
    $ make
    $ sudo make install

Installation requires root privilege.

Root will only be used to install the systemd services.

This will install two systemd services named `telescope` and `scheduler` under 
`/etc/systemd/system` (the default path to install services) 
and a configuration file under `/etc/ctmo`

Uninstall
---------

To clean (delete intermediate files) and uninstall::

    $ make clean
    $ sudo -H make uninstall
