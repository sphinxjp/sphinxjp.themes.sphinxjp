A sphinx theme for sphinx-users.jp site.

Features
========
* provide ``sphinxjp`` theme used on the sphinx-users.jp site
  ( http://sphinx-users.jp/ ).

Setup
=====
Make environment with easy_install::

    $ easy_install sphinxjp.themes.sphinxjp


Convert Usage
==============
setup conf.py with::

    extensions = ['sphinxjp.themecore']
    html_theme = 'sphinxjp'

and run::

    $ make html


Requirements
============
* sphinx 1.0.x or later.
* sphinxjp.themecore


License
=======
Licensed under the `MIT license <http://www.opensource.org/licenses/mit-license.php>`_ .
See the LICENSE file for specific terms.

