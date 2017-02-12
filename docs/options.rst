===============
conf.py sample
===============

Sample
=======

.. code-block:: python

    # -*- coding: utf-8 -*-
    source_suffix = '.rst'
    master_doc = 'index'

    project = u'sphinx-users.jp theme sample'
    version = release = '1.0.0'
    copyright = u'2011-2017, Sphinx-users.jp'

    ################################################################
    # HTML theme setting
    # You need to install `pip install sphinxjp.themes.sphinxjp`

    html_theme = 'sphinxjp'

    ################################################################
    # HTML theme options for `sphinxjp` theme

    html_theme_options = {
        'hatena_bookmark': False,
        'hatena_star': False,
        'hatena_star_token': '<GET YOUR HATENA STAR TOKEN AND SET HERE>',
    }


HTML theme options
===================

:hatena_bookmark:
    Show hatena-bookmark bookmarked count and link.
    default is False.
    See also: http://b.hatena.ne.jp/help

:hatena_star:
    Show hatena-star stars.
    default is False.
    See also: http://s.hatena.ne.jp/

:hatena_star_token:
    If you set `hatena_star = True`, you need set this token.
    See also: http://s.hatena.ne.jp/

