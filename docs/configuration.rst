.. _conf:

Configuring your system
=======================

Before you start the services you may have to configure your manager
to work with your system.


Configuration file
------------------

Open the configuration file located in ``/etc/ctmo/ctmo.conf.yaml``.
Inside you will find a `YAML`_ configuration file for the services.

.. _sch:

Scheduler Address
^^^^^^^^^^^^^^^^^
**HTTP:** The full address and port to locate the ``scheduler`` service on the net.

**IP:** The IP address of the server running the ``scheduler`` service.

**Port:** The port for the address of the server running the ``scheduler`` service.

Telescope Address
^^^^^^^^^^^^^^^^^

See :ref:`sch`.

Logging
^^^^^^^

**File:** File path to the log file that will be used to log.
Default is ``/etc/ctmo/logs/ctmo.log``.

**Log Level:** One of ``DEBUG``, ``INFO``, ``WARNING``, ``ERROR``. Default: ``INFO``.

.. _YAML: https://yaml.org
