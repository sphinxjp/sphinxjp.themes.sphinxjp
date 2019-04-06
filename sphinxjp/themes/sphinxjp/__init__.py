# -*- coding: utf-8 -*-

from os import path

package_dir = path.abspath(path.dirname(__file__))
template_path = path.join(package_dir, 'templates', 'sphinxjp')


def setup(app):
    app.add_html_theme('sphinxjp', template_path)

    return {
        'version': '1.0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
