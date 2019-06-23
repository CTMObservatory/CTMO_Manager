.. CTMO Manager documentation master file, created by
   sphinx-quickstart on Thu Mar 14 13:04:41 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

CTMO Manager's Documentation
============================

The CTMO Manager is a collection of installable daemons (services) to automize telescope 
operations.

The communication between modules is done using the `XML-RPC`_ protocol over sockets.
This allows the modules to be distributed on different machines, as well as a single computer.

Contents:
^^^^^^^^^
.. toctree::
   :maxdepth: 2

   installation
   configuration
   services
   workorders

.. _XML-RPC: http://xmlrpc.scripting.com
