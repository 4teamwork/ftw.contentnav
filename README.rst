

.. contents:: Table of Contents




Introduction
============


Provides a content navigation behavior, which allows you to show sub content by category.


Compatibility
-------------

Plone 4.3.x

.. image:: https://jenkins.4teamwork.ch/job/ftw.contentnav-master-test-plone-4.3.x.cfg/badge/icon
   :target: https://jenkins.4teamwork.ch/job/ftw.contentnav-master-test-plone-4.3.x.cfg


Installation
============

- Add the package to your buildout configuration:

::

    [instance]
    eggs +=
        ...
        ftw.contentnav


- Install the generic import profile.


Usage
=====

First steps
-----------

If you assign one or more categories to a contenttype, it will be listet on its parent.


Development
===========

**Python:**

1. Fork this repo
2. Clone your fork
3. Shell: ``ln -s development.cfg buidlout.cfg``
4. Shell: ``python boostrap.py``
5. Shell: ``bin/buildout``

Run ``bin/test`` to test your changes.

Or start an instance by running ``bin/instance fg``.


Links
=====

- Github: https://github.com/4teamwork/ftw.contentnav
- Issues: https://github.com/4teamwork/ftw.contentnav/issues
- Pypi: http://pypi.python.org/pypi/ftw.contentnav
- Continuous integration: https://jenkins.4teamwork.ch/search?q=ftw.contentnav


Copyright
=========

This package is copyright by `4teamwork <http://www.4teamwork.ch/>`_.

``ftw.contentnav`` is licensed under GNU General Public License, version 2.
