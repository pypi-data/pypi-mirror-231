Development
===========

The extension is developed in a git repository that can be cloned by running::

    git clone https://git.dittberner.info/jan/sphinxext-ip.git

Running test
------------

To install all dependencies and run the tests use::

    pipenv install --dev
    pipenv run tox

Release a new version
---------------------

Start by deciding the new release number and perform the following steps:

* update CHANGES.rst
* change ``version`` in setup.cfg
* change ``__version__`` in jandd/sphinxext/ip/__init__.rst
* change ``version`` in tests/root/conf.py
* commit and push your changes ::

     git commit -m "Release <version>"
     git push

* create an annotated and signed tag with the new version number (``git
  shortlog <previous_tag>..HEAD`` could help to create a good release tag
  message) ::

     git tag -s -a <version>

* build the release artifacts ::

     rm -rf dist jandd.sphinxext.ip.egg-info
     pipenv run python3 setup.py egg_info -b <version< bdist_wheel sdist

* upload to PyPI using twine ::

     pipenv run twine upload -s dist/*

* push the tag to git ::

     git push --tags
