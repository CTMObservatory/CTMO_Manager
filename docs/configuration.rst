Configuring your system
=======================

Before you start the systemd services you may have to configure your manager
to work with your system.


Configuration file
------------------

Open the configuration file located in `/etc/ctmo/ctmo.conf.yaml`.
Inside you will find configuration for the services as well as logging.

The syntax for the configuration file is YAML.

Scheduler Address:
^^^^^^^^^^^^^^^^^^
**HTTP:** The full address and port to locate the `scheduler` service on the net.

**IP:** The IP address of the server running the `scheduler` service.

**Port:** The port for the address of the server running the `scheduler` service.

Telescope Address:
^^^^^^^^^^^^^^^^^^

See Scheduler Address.

Logging:
^^^^^^^^

**File:** File path to the log file that will be used to log.
Default is `/etc/ctmo/logs/ctmo.log`.

**Log Level:** One of DEBUG, INFO, WARNING, ERROR. Default: INFO.
