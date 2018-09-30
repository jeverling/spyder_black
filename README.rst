spyder-black
============


Description
-----------

A plugin to run the `black <https://github.com/ambv/black>`_ python autoformatter from within the python IDE `spyder <https://github.com/spyder-ide/spyder>`_.

It is a fork of the `spyder-autopep8 plugin <https://github.com/spyder-ide/spyder-autopep8>`_, that has been hastily adjusted to call `black <https://github.com/ambv/black>`_ instead of *autopep8*.


Install instructions
--------------------

Installation using pip/setuptools doesn't seem to work for this plugin. Just clone it into your user-plugin directory, e.g.
::

  cd ~/.config/spyder-py3/plugins
  git clone https://github.com/jeverling/spyder_black.git



Important Announcement: Spyder is unfunded!
-------------------------------------------

Since mid November/2017, `Anaconda, Inc`_ has
stopped funding Spyder development, after doing it for the past 18
months. Because of that, development will focus from now on maintaining
Spyder 3 at a much slower pace than before.

If you want to contribute to maintain Spyder, please consider donating at

https://opencollective.com/spyder

We appreciate all the help you can provide us and can't thank you enough for
supporting the work of Spyder devs and Spyder development.

If you want to know more about this, please read this
`page`_.


.. _Anaconda, Inc: https://www.anaconda.com/
.. _page: https://github.com/spyder-ide/spyder/wiki/Anaconda-stopped-funding-Spyder


Requirements
------------
::

  spyder
  black


Usage
-----

Press Shift+F8 (default) to run `black <https://github.com/ambv/black>`_ on the current file or go to ``Source > Run black code autoformatting``.

Information about the execution will be displayed in the statusbar.


Contributing
------------

Everyone is welcome to contribute!


Backers
~~~~~~~

Support sypder with a monthly donation and help them continue their activities.

.. image:: https://opencollective.com/spyder/backers.svg
   :target: https://opencollective.com/spyder#support
   :alt: Backers


Sponsors
~~~~~~~~

Become a sponsor to get your logo on the spyder README on Github.

.. image:: https://opencollective.com/spyder/sponsors.svg
   :target: https://opencollective.com/spyder#support
   :alt: Sponsors
