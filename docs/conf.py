# -*- coding: utf-8 -*-
source_suffix = '.rst'
master_doc = 'index'

project = u'sphinx-users.jp theme sample'
version = release = '1.0.0'
copyright = u'2011-2017, Sphinx-users.jp'

################################################################
# Extension and Theme setting
# You need to install `pip install sphinxjp.themes.sphinxjp`

html_theme = 'sphinxjp'

################################################################
# HTML theme options for `sphinxjp` theme

html_theme_options = {
    'hatena_bookmark': False,
    'hatena_star': False,
    'hatena_star_token': '<GET YOUR HATENA STAR TOKEN AND SET HERE>',
    'repository_url': 'https://github.com/sphinxjp/sphinxjp.themes.sphinxjp/',
}

