vininfo
=======
https://github.com/idlesign/vininfo

.. image:: https://idlesign.github.io/lbc/py2-lbc.svg
   :target: https://idlesign.github.io/lbc/
   :alt: LBC Python 2

----

|release| |lic| |ci| |coverage|

.. |release| image:: https://img.shields.io/pypi/v/vininfo.svg
    :target: https://pypi.python.org/pypi/vininfo

.. |lic| image:: https://img.shields.io/pypi/l/vininfo.svg
    :target: https://pypi.python.org/pypi/vininfo

.. |ci| image:: https://img.shields.io/travis/idlesign/vininfo/master.svg
    :target: https://travis-ci.org/idlesign/vininfo

.. |coverage| image:: https://img.shields.io/coveralls/idlesign/vininfo/master.svg
    :target: https://coveralls.io/r/idlesign/vininfo


Description
-----------

*Extracts useful information from Vehicle Identification Number (VIN)*

* Can be used as a standalone console application (CLI).
* One can also use import it as any other package in your Python code.
* Gives basic and detailed info (is available) about VIN.
* Allows VIN checksum verification.

Additional info available for many vehicles from:

* AvtoVAZ
* Nissan
* Opel
* Renault


Requirements
------------

* Python 2.7, 3.6+
* `click` package for CLI


Usage
-----

CLI
~~~

`click` package is required for CLI. You can install `vininfo` with `click` using::

    $ pip install vininfo[cli]


.. code-block:: bash

    $ vininfo --help

    ; Print out VIN info:
    $ vininfo show XTAGFK330JY144213

    ; Basic:
    ; Country: USSR/CIS
    ; Manufacturer: AvtoVAZ
    ; Region: Europe
    ; Years: 2018, 1988
    ;
    ; Details:
    ; Body: Station Wagon, 5-Door
    ; Engine: 21179
    ; Model: Vesta
    ; Plant: Izhevsk
    ; Serial: 144213
    ; Transmission: Manual Renault

    ; Verify checksum
    $ vininfo check 1M8GDM9AXKP042788
    ; Checksum is valid


Python
~~~~~~

.. code-block:: python

    from vininfo import Vin

    vin = Vin('VF1LM1B0H36666155')

    vin.country  # France
    vin.manufacturer  # Renault
    vin.region  # Europe
    vin.wmi  # VF1
    vin.vds  # LM1B0H
    vin.vis  # 36666155

    annotated = vin.annotate()
    details = vin.details

    vin.verify_checksum()  # False
    Vin('1M8GDM9AXKP042788').verify_checksum()  # True
