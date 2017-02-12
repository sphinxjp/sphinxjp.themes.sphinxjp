History
=======

1.0.1 (unreleased)
------------------

1.0.0 (2017/02/12)
------------------
* theme parameter: repository_url
* doc: easy_install -> pip install
* doc: remove a note for sphinxjp.themecore
* doc: moved from pythonhosted.org to readthedocs
* repository: moved from bitbucket to github
* test: Drop py25,py26,py31, Add py35,py36

0.3.1 (2014/2/12)
------------------

* fix: now come back search feature

0.3.0 (2013/12/10)
------------------
* support Python-3.1, 3.2, 3.3.
* support Sphinx-1.2 theme plugin feature. sphinxjp.themecore is no longer
  needed (if you use Sphinx-1.1.3, you need sphinxjp.themecore).


0.2.0 (2013/10/5)
------------------
* fix: <ul><li> list item in the <ol><li> rendering as numbered list, thank you @usaturn!
* transplant many macro/header parts from sphinx basic theme.
* separate layout.html into some sub templates:

  * globalnavigation.html : top-right 3 icons
  * globaltoc.html : global toctree for sidebar
  * localtoc.html : local toctree for sidebar
  * relations.html : next/pref link for sidebar
  * searchbox.html : search box for sidebar
  * sourcelink.html : source link for sidebar

0.1.1 (2011/7/6)
------------------
* fix: namespace package declaration missing, thank you @togakushi!

0.1.0 (2011/2/19)
------------------
* first release

