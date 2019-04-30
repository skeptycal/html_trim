#  version

---

```bash

.
├── Pipfile
├── Pipfile.lock
├── README.md
├── bin
│   ├── activate
│   ├── activate.csh
│   ├── activate.fish
│   ├── easy_install
│   ├── easy_install-3.7
│   ├── pip
│   ├── pip3
│   ├── pip3.7
│   ├── python -> python3
│   └── python3 -> /usr/local/bin/python3
├── codecov.yml
├── html_trim.py
├── include
└── lib
    └── python3.7
        └── site-packages
            ├── __pycache__
            │   └── easy_install.cpython-37.pyc
            ├── easy_install.py
            ├── pip
            │   ├── __init__.py
            │   ├── __main__.py
            │   ├── __pycache__
            │   │   ├── __init__.cpython-37.pyc
            │   │   └── __main__.cpython-37.pyc
            │   ├── _internal
            │   │   ├── __init__.py
            │   │   ├── __pycache__
            │   │   │   ├── __init__.cpython-37.pyc
            │   │   │   ├── build_env.cpython-37.pyc
            │   │   │   ├── cache.cpython-37.pyc
            │   │   │   ├── configuration.cpython-37.pyc
            │   │   │   ├── download.cpython-37.pyc
            │   │   │   ├── exceptions.cpython-37.pyc
            │   │   │   ├── index.cpython-37.pyc
            │   │   │   ├── locations.cpython-37.pyc
            │   │   │   ├── pep425tags.cpython-37.pyc
            │   │   │   ├── pyproject.cpython-37.pyc
            │   │   │   ├── resolve.cpython-37.pyc
            │   │   │   └── wheel.cpython-37.pyc
            │   │   ├── build_env.py
            │   │   ├── cache.py
            │   │   ├── cli
            │   │   │   ├── __init__.py
            │   │   │   ├── __pycache__
            │   │   │   │   ├── __init__.cpython-37.pyc
            │   │   │   │   ├── autocompletion.cpython-37.pyc
            │   │   │   │   ├── base_command.cpython-37.pyc
            │   │   │   │   ├── cmdoptions.cpython-37.pyc
            │   │   │   │   ├── main_parser.cpython-37.pyc
            │   │   │   │   ├── parser.cpython-37.pyc
            │   │   │   │   └── status_codes.cpython-37.pyc
            │   │   │   ├── autocompletion.py
            │   │   │   ├── base_command.py
            │   │   │   ├── cmdoptions.py
            │   │   │   ├── main_parser.py
            │   │   │   ├── parser.py
            │   │   │   └── status_codes.py
            │   │   ├── commands
            │   │   │   ├── __init__.py
            │   │   │   ├── __pycache__
            │   │   │   │   ├── __init__.cpython-37.pyc
            │   │   │   │   ├── check.cpython-37.pyc
            │   │   │   │   ├── completion.cpython-37.pyc
            │   │   │   │   ├── configuration.cpython-37.pyc
            │   │   │   │   ├── download.cpython-37.pyc
            │   │   │   │   ├── freeze.cpython-37.pyc
            │   │   │   │   ├── hash.cpython-37.pyc
            │   │   │   │   ├── help.cpython-37.pyc
            │   │   │   │   ├── install.cpython-37.pyc
            │   │   │   │   ├── list.cpython-37.pyc
            │   │   │   │   ├── search.cpython-37.pyc
            │   │   │   │   ├── show.cpython-37.pyc
            │   │   │   │   ├── uninstall.cpython-37.pyc
            │   │   │   │   └── wheel.cpython-37.pyc
            │   │   │   ├── check.py
            │   │   │   ├── completion.py
            │   │   │   ├── configuration.py
            │   │   │   ├── download.py
            │   │   │   ├── freeze.py
            │   │   │   ├── hash.py
            │   │   │   ├── help.py
            │   │   │   ├── install.py
            │   │   │   ├── list.py
            │   │   │   ├── search.py
            │   │   │   ├── show.py
            │   │   │   ├── uninstall.py
            │   │   │   └── wheel.py
            │   │   ├── configuration.py
            │   │   ├── download.py
            │   │   ├── exceptions.py
            │   │   ├── index.py
            │   │   ├── locations.py
            │   │   ├── models
            │   │   │   ├── __init__.py
            │   │   │   ├── __pycache__
            │   │   │   │   ├── __init__.cpython-37.pyc
            │   │   │   │   ├── candidate.cpython-37.pyc
            │   │   │   │   ├── format_control.cpython-37.pyc
            │   │   │   │   ├── index.cpython-37.pyc
            │   │   │   │   └── link.cpython-37.pyc
            │   │   │   ├── candidate.py
            │   │   │   ├── format_control.py
            │   │   │   ├── index.py
            │   │   │   └── link.py
            │   │   ├── operations
            │   │   │   ├── __init__.py
            │   │   │   ├── __pycache__
            │   │   │   │   ├── __init__.cpython-37.pyc
            │   │   │   │   ├── check.cpython-37.pyc
            │   │   │   │   ├── freeze.cpython-37.pyc
            │   │   │   │   └── prepare.cpython-37.pyc
            │   │   │   ├── check.py
            │   │   │   ├── freeze.py
            │   │   │   └── prepare.py
            │   │   ├── pep425tags.py
            │   │   ├── pyproject.py
            │   │   ├── req
            │   │   │   ├── __init__.py
            │   │   │   ├── __pycache__
            │   │   │   │   ├── __init__.cpython-37.pyc
            │   │   │   │   ├── constructors.cpython-37.pyc
            │   │   │   │   ├── req_file.cpython-37.pyc
            │   │   │   │   ├── req_install.cpython-37.pyc
            │   │   │   │   ├── req_set.cpython-37.pyc
            │   │   │   │   ├── req_tracker.cpython-37.pyc
            │   │   │   │   └── req_uninstall.cpython-37.pyc
            │   │   │   ├── constructors.py
            │   │   │   ├── req_file.py
            │   │   │   ├── req_install.py
            │   │   │   ├── req_set.py
            │   │   │   ├── req_tracker.py
            │   │   │   └── req_uninstall.py
            │   │   ├── resolve.py
            │   │   ├── utils
            │   │   │   ├── __init__.py
            │   │   │   ├── __pycache__
            │   │   │   │   ├── __init__.cpython-37.pyc
            │   │   │   │   ├── appdirs.cpython-37.pyc
            │   │   │   │   ├── compat.cpython-37.pyc
            │   │   │   │   ├── deprecation.cpython-37.pyc
            │   │   │   │   ├── encoding.cpython-37.pyc
            │   │   │   │   ├── filesystem.cpython-37.pyc
            │   │   │   │   ├── glibc.cpython-37.pyc
            │   │   │   │   ├── hashes.cpython-37.pyc
            │   │   │   │   ├── logging.cpython-37.pyc
            │   │   │   │   ├── misc.cpython-37.pyc
            │   │   │   │   ├── models.cpython-37.pyc
            │   │   │   │   ├── outdated.cpython-37.pyc
            │   │   │   │   ├── packaging.cpython-37.pyc
            │   │   │   │   ├── setuptools_build.cpython-37.pyc
            │   │   │   │   ├── temp_dir.cpython-37.pyc
            │   │   │   │   ├── typing.cpython-37.pyc
            │   │   │   │   └── ui.cpython-37.pyc
            │   │   │   ├── appdirs.py
            │   │   │   ├── compat.py
            │   │   │   ├── deprecation.py
            │   │   │   ├── encoding.py
            │   │   │   ├── filesystem.py
            │   │   │   ├── glibc.py
            │   │   │   ├── hashes.py
            │   │   │   ├── logging.py
            │   │   │   ├── misc.py
            │   │   │   ├── models.py
            │   │   │   ├── outdated.py
            │   │   │   ├── packaging.py
            │   │   │   ├── setuptools_build.py
            │   │   │   ├── temp_dir.py
            │   │   │   ├── typing.py
            │   │   │   └── ui.py
            │   │   ├── vcs
            │   │   │   ├── __init__.py
            │   │   │   ├── __pycache__
            │   │   │   │   ├── __init__.cpython-37.pyc
            │   │   │   │   ├── bazaar.cpython-37.pyc
            │   │   │   │   ├── git.cpython-37.pyc
            │   │   │   │   ├── mercurial.cpython-37.pyc
            │   │   │   │   └── subversion.cpython-37.pyc
            │   │   │   ├── bazaar.py
            │   │   │   ├── git.py
            │   │   │   ├── mercurial.py
            │   │   │   └── subversion.py
            │   │   └── wheel.py
            │   └── _vendor
            │       ├── __init__.py
            │       ├── __pycache__
            │       │   ├── __init__.cpython-37.pyc
            │       │   ├── appdirs.cpython-37.pyc
            │       │   ├── distro.cpython-37.pyc
            │       │   ├── ipaddress.cpython-37.pyc
            │       │   ├── pyparsing.cpython-37.pyc
            │       │   ├── retrying.cpython-37.pyc
            │       │   └── six.cpython-37.pyc
            │       ├── appdirs.py
            │       ├── cachecontrol
            │       │   ├── __init__.py
            │       │   ├── __pycache__
            │       │   │   ├── __init__.cpython-37.pyc
            │       │   │   ├── _cmd.cpython-37.pyc
            │       │   │   ├── adapter.cpython-37.pyc
            │       │   │   ├── cache.cpython-37.pyc
            │       │   │   ├── compat.cpython-37.pyc
            │       │   │   ├── controller.cpython-37.pyc
            │       │   │   ├── filewrapper.cpython-37.pyc
            │       │   │   ├── heuristics.cpython-37.pyc
            │       │   │   ├── serialize.cpython-37.pyc
            │       │   │   └── wrapper.cpython-37.pyc
            │       │   ├── _cmd.py
            │       │   ├── adapter.py
            │       │   ├── cache.py
            │       │   ├── caches
            │       │   │   ├── __init__.py
            │       │   │   ├── __pycache__
            │       │   │   │   ├── __init__.cpython-37.pyc
            │       │   │   │   ├── file_cache.cpython-37.pyc
            │       │   │   │   └── redis_cache.cpython-37.pyc
            │       │   │   ├── file_cache.py
            │       │   │   └── redis_cache.py
            │       │   ├── compat.py
            │       │   ├── controller.py
            │       │   ├── filewrapper.py
            │       │   ├── heuristics.py
            │       │   ├── serialize.py
            │       │   └── wrapper.py
            │       ├── certifi
            │       │   ├── __init__.py
            │       │   ├── __main__.py
            │       │   ├── __pycache__
            │       │   │   ├── __init__.cpython-37.pyc
            │       │   │   ├── __main__.cpython-37.pyc
            │       │   │   └── core.cpython-37.pyc
            │       │   ├── cacert.pem
            │       │   └── core.py
            │       ├── chardet
            │       │   ├── __init__.py
            │       │   ├── __pycache__
            │       │   │   ├── __init__.cpython-37.pyc
            │       │   │   ├── big5freq.cpython-37.pyc
            │       │   │   ├── big5prober.cpython-37.pyc
            │       │   │   ├── chardistribution.cpython-37.pyc
            │       │   │   ├── charsetgroupprober.cpython-37.pyc
            │       │   │   ├── charsetprober.cpython-37.pyc
            │       │   │   ├── codingstatemachine.cpython-37.pyc
            │       │   │   ├── compat.cpython-37.pyc
            │       │   │   ├── cp949prober.cpython-37.pyc
            │       │   │   ├── enums.cpython-37.pyc
            │       │   │   ├── escprober.cpython-37.pyc
            │       │   │   ├── escsm.cpython-37.pyc
            │       │   │   ├── eucjpprober.cpython-37.pyc
            │       │   │   ├── euckrfreq.cpython-37.pyc
            │       │   │   ├── euckrprober.cpython-37.pyc
            │       │   │   ├── euctwfreq.cpython-37.pyc
            │       │   │   ├── euctwprober.cpython-37.pyc
            │       │   │   ├── gb2312freq.cpython-37.pyc
            │       │   │   ├── gb2312prober.cpython-37.pyc
            │       │   │   ├── hebrewprober.cpython-37.pyc
            │       │   │   ├── jisfreq.cpython-37.pyc
            │       │   │   ├── jpcntx.cpython-37.pyc
            │       │   │   ├── langbulgarianmodel.cpython-37.pyc
            │       │   │   ├── langcyrillicmodel.cpython-37.pyc
            │       │   │   ├── langgreekmodel.cpython-37.pyc
            │       │   │   ├── langhebrewmodel.cpython-37.pyc
            │       │   │   ├── langhungarianmodel.cpython-37.pyc
            │       │   │   ├── langthaimodel.cpython-37.pyc
            │       │   │   ├── langturkishmodel.cpython-37.pyc
            │       │   │   ├── latin1prober.cpython-37.pyc
            │       │   │   ├── mbcharsetprober.cpython-37.pyc
            │       │   │   ├── mbcsgroupprober.cpython-37.pyc
            │       │   │   ├── mbcssm.cpython-37.pyc
            │       │   │   ├── sbcharsetprober.cpython-37.pyc
            │       │   │   ├── sbcsgroupprober.cpython-37.pyc
            │       │   │   ├── sjisprober.cpython-37.pyc
            │       │   │   ├── universaldetector.cpython-37.pyc
            │       │   │   ├── utf8prober.cpython-37.pyc
            │       │   │   └── version.cpython-37.pyc
            │       │   ├── big5freq.py
            │       │   ├── big5prober.py
            │       │   ├── chardistribution.py
            │       │   ├── charsetgroupprober.py
            │       │   ├── charsetprober.py
            │       │   ├── cli
            │       │   │   ├── __init__.py
            │       │   │   ├── __pycache__
            │       │   │   │   ├── __init__.cpython-37.pyc
            │       │   │   │   └── chardetect.cpython-37.pyc
            │       │   │   └── chardetect.py
            │       │   ├── codingstatemachine.py
            │       │   ├── compat.py
            │       │   ├── cp949prober.py
            │       │   ├── enums.py
            │       │   ├── escprober.py
            │       │   ├── escsm.py
            │       │   ├── eucjpprober.py
            │       │   ├── euckrfreq.py
            │       │   ├── euckrprober.py
            │       │   ├── euctwfreq.py
            │       │   ├── euctwprober.py
            │       │   ├── gb2312freq.py
            │       │   ├── gb2312prober.py
            │       │   ├── hebrewprober.py
            │       │   ├── jisfreq.py
            │       │   ├── jpcntx.py
            │       │   ├── langbulgarianmodel.py
            │       │   ├── langcyrillicmodel.py
            │       │   ├── langgreekmodel.py
            │       │   ├── langhebrewmodel.py
            │       │   ├── langhungarianmodel.py
            │       │   ├── langthaimodel.py
            │       │   ├── langturkishmodel.py
            │       │   ├── latin1prober.py
            │       │   ├── mbcharsetprober.py
            │       │   ├── mbcsgroupprober.py
            │       │   ├── mbcssm.py
            │       │   ├── sbcharsetprober.py
            │       │   ├── sbcsgroupprober.py
            │       │   ├── sjisprober.py
            │       │   ├── universaldetector.py
            │       │   ├── utf8prober.py
            │       │   └── version.py
            │       ├── colorama
            │       │   ├── __init__.py
            │       │   ├── __pycache__
            │       │   │   ├── __init__.cpython-37.pyc
            │       │   │   ├── ansi.cpython-37.pyc
            │       │   │   ├── ansitowin32.cpython-37.pyc
            │       │   │   ├── initialise.cpython-37.pyc
            │       │   │   ├── win32.cpython-37.pyc
            │       │   │   └── winterm.cpython-37.pyc
            │       │   ├── ansi.py
            │       │   ├── ansitowin32.py
            │       │   ├── initialise.py
            │       │   ├── win32.py
            │       │   └── winterm.py
            │       ├── distlib
            │       │   ├── __init__.py
            │       │   ├── __pycache__
            │       │   │   ├── __init__.cpython-37.pyc
            │       │   │   ├── compat.cpython-37.pyc
            │       │   │   ├── database.cpython-37.pyc
            │       │   │   ├── index.cpython-37.pyc
            │       │   │   ├── locators.cpython-37.pyc
            │       │   │   ├── manifest.cpython-37.pyc
            │       │   │   ├── markers.cpython-37.pyc
            │       │   │   ├── metadata.cpython-37.pyc
            │       │   │   ├── resources.cpython-37.pyc
            │       │   │   ├── scripts.cpython-37.pyc
            │       │   │   ├── util.cpython-37.pyc
            │       │   │   ├── version.cpython-37.pyc
            │       │   │   └── wheel.cpython-37.pyc
            │       │   ├── _backport
            │       │   │   ├── __init__.py
            │       │   │   ├── __pycache__
            │       │   │   │   ├── __init__.cpython-37.pyc
            │       │   │   │   ├── misc.cpython-37.pyc
            │       │   │   │   ├── shutil.cpython-37.pyc
            │       │   │   │   ├── sysconfig.cpython-37.pyc
            │       │   │   │   └── tarfile.cpython-37.pyc
            │       │   │   ├── misc.py
            │       │   │   ├── shutil.py
            │       │   │   ├── sysconfig.cfg
            │       │   │   ├── sysconfig.py
            │       │   │   └── tarfile.py
            │       │   ├── compat.py
            │       │   ├── database.py
            │       │   ├── index.py
            │       │   ├── locators.py
            │       │   ├── manifest.py
            │       │   ├── markers.py
            │       │   ├── metadata.py
            │       │   ├── resources.py
            │       │   ├── scripts.py
            │       │   ├── t32.exe
            │       │   ├── t64.exe
            │       │   ├── util.py
            │       │   ├── version.py
            │       │   ├── w32.exe
            │       │   ├── w64.exe
            │       │   └── wheel.py
            │       ├── distro.py
            │       ├── html5lib
            │       │   ├── __init__.py
            │       │   ├── __pycache__
            │       │   │   ├── __init__.cpython-37.pyc
            │       │   │   ├── _ihatexml.cpython-37.pyc
            │       │   │   ├── _inputstream.cpython-37.pyc
            │       │   │   ├── _tokenizer.cpython-37.pyc
            │       │   │   ├── _utils.cpython-37.pyc
            │       │   │   ├── constants.cpython-37.pyc
            │       │   │   ├── html5parser.cpython-37.pyc
            │       │   │   └── serializer.cpython-37.pyc
            │       │   ├── _ihatexml.py
            │       │   ├── _inputstream.py
            │       │   ├── _tokenizer.py
            │       │   ├── _trie
            │       │   │   ├── __init__.py
            │       │   │   ├── __pycache__
            │       │   │   │   ├── __init__.cpython-37.pyc
            │       │   │   │   ├── _base.cpython-37.pyc
            │       │   │   │   ├── datrie.cpython-37.pyc
            │       │   │   │   └── py.cpython-37.pyc
            │       │   │   ├── _base.py
            │       │   │   ├── datrie.py
            │       │   │   └── py.py
            │       │   ├── _utils.py
            │       │   ├── constants.py
            │       │   ├── filters
            │       │   │   ├── __init__.py
            │       │   │   ├── __pycache__
            │       │   │   │   ├── __init__.cpython-37.pyc
            │       │   │   │   ├── alphabeticalattributes.cpython-37.pyc
            │       │   │   │   ├── base.cpython-37.pyc
            │       │   │   │   ├── inject_meta_charset.cpython-37.pyc
            │       │   │   │   ├── lint.cpython-37.pyc
            │       │   │   │   ├── optionaltags.cpython-37.pyc
            │       │   │   │   ├── sanitizer.cpython-37.pyc
            │       │   │   │   └── whitespace.cpython-37.pyc
            │       │   │   ├── alphabeticalattributes.py
            │       │   │   ├── base.py
            │       │   │   ├── inject_meta_charset.py
            │       │   │   ├── lint.py
            │       │   │   ├── optionaltags.py
            │       │   │   ├── sanitizer.py
            │       │   │   └── whitespace.py
            │       │   ├── html5parser.py
            │       │   ├── serializer.py
            │       │   ├── treeadapters
            │       │   │   ├── __init__.py
            │       │   │   ├── __pycache__
            │       │   │   │   ├── __init__.cpython-37.pyc
            │       │   │   │   ├── genshi.cpython-37.pyc
            │       │   │   │   └── sax.cpython-37.pyc
            │       │   │   ├── genshi.py
            │       │   │   └── sax.py
            │       │   ├── treebuilders
            │       │   │   ├── __init__.py
            │       │   │   ├── __pycache__
            │       │   │   │   ├── __init__.cpython-37.pyc
            │       │   │   │   ├── base.cpython-37.pyc
            │       │   │   │   ├── dom.cpython-37.pyc
            │       │   │   │   ├── etree.cpython-37.pyc
            │       │   │   │   └── etree_lxml.cpython-37.pyc
            │       │   │   ├── base.py
            │       │   │   ├── dom.py
            │       │   │   ├── etree.py
            │       │   │   └── etree_lxml.py
            │       │   └── treewalkers
            │       │       ├── __init__.py
            │       │       ├── __pycache__
            │       │       │   ├── __init__.cpython-37.pyc
            │       │       │   ├── base.cpython-37.pyc
            │       │       │   ├── dom.cpython-37.pyc
            │       │       │   ├── etree.cpython-37.pyc
            │       │       │   ├── etree_lxml.cpython-37.pyc
            │       │       │   └── genshi.cpython-37.pyc
            │       │       ├── base.py
            │       │       ├── dom.py
            │       │       ├── etree.py
            │       │       ├── etree_lxml.py
            │       │       └── genshi.py
            │       ├── idna
            │       │   ├── __init__.py
            │       │   ├── __pycache__
            │       │   │   ├── __init__.cpython-37.pyc
            │       │   │   ├── codec.cpython-37.pyc
            │       │   │   ├── compat.cpython-37.pyc
            │       │   │   ├── core.cpython-37.pyc
            │       │   │   ├── idnadata.cpython-37.pyc
            │       │   │   ├── intranges.cpython-37.pyc
            │       │   │   ├── package_data.cpython-37.pyc
            │       │   │   └── uts46data.cpython-37.pyc
            │       │   ├── codec.py
            │       │   ├── compat.py
            │       │   ├── core.py
            │       │   ├── idnadata.py
            │       │   ├── intranges.py
            │       │   ├── package_data.py
            │       │   └── uts46data.py
            │       ├── ipaddress.py
            │       ├── lockfile
            │       │   ├── __init__.py
            │       │   ├── __pycache__
            │       │   │   ├── __init__.cpython-37.pyc
            │       │   │   ├── linklockfile.cpython-37.pyc
            │       │   │   ├── mkdirlockfile.cpython-37.pyc
            │       │   │   ├── pidlockfile.cpython-37.pyc
            │       │   │   ├── sqlitelockfile.cpython-37.pyc
            │       │   │   └── symlinklockfile.cpython-37.pyc
            │       │   ├── linklockfile.py
            │       │   ├── mkdirlockfile.py
            │       │   ├── pidlockfile.py
            │       │   ├── sqlitelockfile.py
            │       │   └── symlinklockfile.py
            │       ├── msgpack
            │       │   ├── __init__.py
            │       │   ├── __pycache__
            │       │   │   ├── __init__.cpython-37.pyc
            │       │   │   ├── _version.cpython-37.pyc
            │       │   │   ├── exceptions.cpython-37.pyc
            │       │   │   └── fallback.cpython-37.pyc
            │       │   ├── _version.py
            │       │   ├── exceptions.py
            │       │   └── fallback.py
            │       ├── packaging
            │       │   ├── __about__.py
            │       │   ├── __init__.py
            │       │   ├── __pycache__
            │       │   │   ├── __about__.cpython-37.pyc
            │       │   │   ├── __init__.cpython-37.pyc
            │       │   │   ├── _compat.cpython-37.pyc
            │       │   │   ├── _structures.cpython-37.pyc
            │       │   │   ├── markers.cpython-37.pyc
            │       │   │   ├── requirements.cpython-37.pyc
            │       │   │   ├── specifiers.cpython-37.pyc
            │       │   │   ├── utils.cpython-37.pyc
            │       │   │   └── version.cpython-37.pyc
            │       │   ├── _compat.py
            │       │   ├── _structures.py
            │       │   ├── markers.py
            │       │   ├── requirements.py
            │       │   ├── specifiers.py
            │       │   ├── utils.py
            │       │   └── version.py
            │       ├── pep517
            │       │   ├── __init__.py
            │       │   ├── __pycache__
            │       │   │   ├── __init__.cpython-37.pyc
            │       │   │   ├── _in_process.cpython-37.pyc
            │       │   │   ├── build.cpython-37.pyc
            │       │   │   ├── check.cpython-37.pyc
            │       │   │   ├── colorlog.cpython-37.pyc
            │       │   │   ├── compat.cpython-37.pyc
            │       │   │   ├── envbuild.cpython-37.pyc
            │       │   │   └── wrappers.cpython-37.pyc
            │       │   ├── _in_process.py
            │       │   ├── build.py
            │       │   ├── check.py
            │       │   ├── colorlog.py
            │       │   ├── compat.py
            │       │   ├── envbuild.py
            │       │   └── wrappers.py
            │       ├── pkg_resources
            │       │   ├── __init__.py
            │       │   ├── __pycache__
            │       │   │   ├── __init__.cpython-37.pyc
            │       │   │   └── py31compat.cpython-37.pyc
            │       │   └── py31compat.py
            │       ├── progress
            │       │   ├── __init__.py
            │       │   ├── __pycache__
            │       │   │   ├── __init__.cpython-37.pyc
            │       │   │   ├── bar.cpython-37.pyc
            │       │   │   ├── counter.cpython-37.pyc
            │       │   │   ├── helpers.cpython-37.pyc
            │       │   │   └── spinner.cpython-37.pyc
            │       │   ├── bar.py
            │       │   ├── counter.py
            │       │   ├── helpers.py
            │       │   └── spinner.py
            │       ├── pyparsing.py
            │       ├── pytoml
            │       │   ├── __init__.py
            │       │   ├── __pycache__
            │       │   │   ├── __init__.cpython-37.pyc
            │       │   │   ├── core.cpython-37.pyc
            │       │   │   ├── parser.cpython-37.pyc
            │       │   │   ├── test.cpython-37.pyc
            │       │   │   ├── utils.cpython-37.pyc
            │       │   │   └── writer.cpython-37.pyc
            │       │   ├── core.py
            │       │   ├── parser.py
            │       │   ├── test.py
            │       │   ├── utils.py
            │       │   └── writer.py
            │       ├── requests
            │       │   ├── __init__.py
            │       │   ├── __pycache__
            │       │   │   ├── __init__.cpython-37.pyc
            │       │   │   ├── __version__.cpython-37.pyc
            │       │   │   ├── _internal_utils.cpython-37.pyc
            │       │   │   ├── adapters.cpython-37.pyc
            │       │   │   ├── api.cpython-37.pyc
            │       │   │   ├── auth.cpython-37.pyc
            │       │   │   ├── certs.cpython-37.pyc
            │       │   │   ├── compat.cpython-37.pyc
            │       │   │   ├── cookies.cpython-37.pyc
            │       │   │   ├── exceptions.cpython-37.pyc
            │       │   │   ├── help.cpython-37.pyc
            │       │   │   ├── hooks.cpython-37.pyc
            │       │   │   ├── models.cpython-37.pyc
            │       │   │   ├── packages.cpython-37.pyc
            │       │   │   ├── sessions.cpython-37.pyc
            │       │   │   ├── status_codes.cpython-37.pyc
            │       │   │   ├── structures.cpython-37.pyc
            │       │   │   └── utils.cpython-37.pyc
            │       │   ├── __version__.py
            │       │   ├── _internal_utils.py
            │       │   ├── adapters.py
            │       │   ├── api.py
            │       │   ├── auth.py
            │       │   ├── certs.py
            │       │   ├── compat.py
            │       │   ├── cookies.py
            │       │   ├── exceptions.py
            │       │   ├── help.py
            │       │   ├── hooks.py
            │       │   ├── models.py
            │       │   ├── packages.py
            │       │   ├── sessions.py
            │       │   ├── status_codes.py
            │       │   ├── structures.py
            │       │   └── utils.py
            │       ├── retrying.py
            │       ├── six.py
            │       ├── urllib3
            │       │   ├── __init__.py
            │       │   ├── __pycache__
            │       │   │   ├── __init__.cpython-37.pyc
            │       │   │   ├── _collections.cpython-37.pyc
            │       │   │   ├── connection.cpython-37.pyc
            │       │   │   ├── connectionpool.cpython-37.pyc
            │       │   │   ├── exceptions.cpython-37.pyc
            │       │   │   ├── fields.cpython-37.pyc
            │       │   │   ├── filepost.cpython-37.pyc
            │       │   │   ├── poolmanager.cpython-37.pyc
            │       │   │   ├── request.cpython-37.pyc
            │       │   │   └── response.cpython-37.pyc
            │       │   ├── _collections.py
            │       │   ├── connection.py
            │       │   ├── connectionpool.py
            │       │   ├── contrib
            │       │   │   ├── __init__.py
            │       │   │   ├── __pycache__
            │       │   │   │   ├── __init__.cpython-37.pyc
            │       │   │   │   ├── _appengine_environ.cpython-37.pyc
            │       │   │   │   ├── appengine.cpython-37.pyc
            │       │   │   │   ├── ntlmpool.cpython-37.pyc
            │       │   │   │   ├── pyopenssl.cpython-37.pyc
            │       │   │   │   ├── securetransport.cpython-37.pyc
            │       │   │   │   └── socks.cpython-37.pyc
            │       │   │   ├── _appengine_environ.py
            │       │   │   ├── _securetransport
            │       │   │   │   ├── __init__.py
            │       │   │   │   ├── __pycache__
            │       │   │   │   │   ├── __init__.cpython-37.pyc
            │       │   │   │   │   ├── bindings.cpython-37.pyc
            │       │   │   │   │   └── low_level.cpython-37.pyc
            │       │   │   │   ├── bindings.py
            │       │   │   │   └── low_level.py
            │       │   │   ├── appengine.py
            │       │   │   ├── ntlmpool.py
            │       │   │   ├── pyopenssl.py
            │       │   │   ├── securetransport.py
            │       │   │   └── socks.py
            │       │   ├── exceptions.py
            │       │   ├── fields.py
            │       │   ├── filepost.py
            │       │   ├── packages
            │       │   │   ├── __init__.py
            │       │   │   ├── __pycache__
            │       │   │   │   ├── __init__.cpython-37.pyc
            │       │   │   │   └── six.cpython-37.pyc
            │       │   │   ├── backports
            │       │   │   │   ├── __init__.py
            │       │   │   │   ├── __pycache__
            │       │   │   │   │   ├── __init__.cpython-37.pyc
            │       │   │   │   │   └── makefile.cpython-37.pyc
            │       │   │   │   └── makefile.py
            │       │   │   ├── six.py
            │       │   │   └── ssl_match_hostname
            │       │   │       ├── __init__.py
            │       │   │       ├── __pycache__
            │       │   │       │   ├── __init__.cpython-37.pyc
            │       │   │       │   └── _implementation.cpython-37.pyc
            │       │   │       └── _implementation.py
            │       │   ├── poolmanager.py
            │       │   ├── request.py
            │       │   ├── response.py
            │       │   └── util
            │       │       ├── __init__.py
            │       │       ├── __pycache__
            │       │       │   ├── __init__.cpython-37.pyc
            │       │       │   ├── connection.cpython-37.pyc
            │       │       │   ├── queue.cpython-37.pyc
            │       │       │   ├── request.cpython-37.pyc
            │       │       │   ├── response.cpython-37.pyc
            │       │       │   ├── retry.cpython-37.pyc
            │       │       │   ├── ssl_.cpython-37.pyc
            │       │       │   ├── timeout.cpython-37.pyc
            │       │       │   ├── url.cpython-37.pyc
            │       │       │   └── wait.cpython-37.pyc
            │       │       ├── connection.py
            │       │       ├── queue.py
            │       │       ├── request.py
            │       │       ├── response.py
            │       │       ├── retry.py
            │       │       ├── ssl_.py
            │       │       ├── timeout.py
            │       │       ├── url.py
            │       │       └── wait.py
            │       └── webencodings
            │           ├── __init__.py
            │           ├── __pycache__
            │           │   ├── __init__.cpython-37.pyc
            │           │   ├── labels.cpython-37.pyc
            │           │   ├── mklabels.cpython-37.pyc
            │           │   ├── tests.cpython-37.pyc
            │           │   └── x_user_defined.cpython-37.pyc
            │           ├── labels.py
            │           ├── mklabels.py
            │           ├── tests.py
            │           └── x_user_defined.py
            ├── pip-19.0.3.dist-info
            │   ├── INSTALLER
            │   ├── LICENSE.txt
            │   ├── METADATA
            │   ├── RECORD
            │   ├── WHEEL
            │   ├── entry_points.txt
            │   └── top_level.txt
            ├── pkg_resources
            │   ├── __init__.py
            │   ├── __pycache__
            │   │   ├── __init__.cpython-37.pyc
            │   │   └── py31compat.cpython-37.pyc
            │   ├── _vendor
            │   │   ├── __init__.py
            │   │   ├── __pycache__
            │   │   │   ├── __init__.cpython-37.pyc
            │   │   │   ├── appdirs.cpython-37.pyc
            │   │   │   ├── pyparsing.cpython-37.pyc
            │   │   │   └── six.cpython-37.pyc
            │   │   ├── appdirs.py
            │   │   ├── packaging
            │   │   │   ├── __about__.py
            │   │   │   ├── __init__.py
            │   │   │   ├── __pycache__
            │   │   │   │   ├── __about__.cpython-37.pyc
            │   │   │   │   ├── __init__.cpython-37.pyc
            │   │   │   │   ├── _compat.cpython-37.pyc
            │   │   │   │   ├── _structures.cpython-37.pyc
            │   │   │   │   ├── markers.cpython-37.pyc
            │   │   │   │   ├── requirements.cpython-37.pyc
            │   │   │   │   ├── specifiers.cpython-37.pyc
            │   │   │   │   ├── utils.cpython-37.pyc
            │   │   │   │   └── version.cpython-37.pyc
            │   │   │   ├── _compat.py
            │   │   │   ├── _structures.py
            │   │   │   ├── markers.py
            │   │   │   ├── requirements.py
            │   │   │   ├── specifiers.py
            │   │   │   ├── utils.py
            │   │   │   └── version.py
            │   │   ├── pyparsing.py
            │   │   └── six.py
            │   ├── extern
            │   │   ├── __init__.py
            │   │   └── __pycache__
            │   │       └── __init__.cpython-37.pyc
            │   └── py31compat.py
            ├── setuptools
            │   ├── __init__.py
            │   ├── __pycache__
            │   │   ├── __init__.cpython-37.pyc
            │   │   ├── _deprecation_warning.cpython-37.pyc
            │   │   ├── archive_util.cpython-37.pyc
            │   │   ├── build_meta.cpython-37.pyc
            │   │   ├── config.cpython-37.pyc
            │   │   ├── dep_util.cpython-37.pyc
            │   │   ├── depends.cpython-37.pyc
            │   │   ├── dist.cpython-37.pyc
            │   │   ├── extension.cpython-37.pyc
            │   │   ├── glibc.cpython-37.pyc
            │   │   ├── glob.cpython-37.pyc
            │   │   ├── launch.cpython-37.pyc
            │   │   ├── lib2to3_ex.cpython-37.pyc
            │   │   ├── monkey.cpython-37.pyc
            │   │   ├── msvc.cpython-37.pyc
            │   │   ├── namespaces.cpython-37.pyc
            │   │   ├── package_index.cpython-37.pyc
            │   │   ├── pep425tags.cpython-37.pyc
            │   │   ├── py27compat.cpython-37.pyc
            │   │   ├── py31compat.cpython-37.pyc
            │   │   ├── py33compat.cpython-37.pyc
            │   │   ├── sandbox.cpython-37.pyc
            │   │   ├── site-patch.cpython-37.pyc
            │   │   ├── ssl_support.cpython-37.pyc
            │   │   ├── unicode_utils.cpython-37.pyc
            │   │   ├── version.cpython-37.pyc
            │   │   ├── wheel.cpython-37.pyc
            │   │   └── windows_support.cpython-37.pyc
            │   ├── _deprecation_warning.py
            │   ├── _vendor
            │   │   ├── __init__.py
            │   │   ├── __pycache__
            │   │   │   ├── __init__.cpython-37.pyc
            │   │   │   ├── pyparsing.cpython-37.pyc
            │   │   │   └── six.cpython-37.pyc
            │   │   ├── packaging
            │   │   │   ├── __about__.py
            │   │   │   ├── __init__.py
            │   │   │   ├── __pycache__
            │   │   │   │   ├── __about__.cpython-37.pyc
            │   │   │   │   ├── __init__.cpython-37.pyc
            │   │   │   │   ├── _compat.cpython-37.pyc
            │   │   │   │   ├── _structures.cpython-37.pyc
            │   │   │   │   ├── markers.cpython-37.pyc
            │   │   │   │   ├── requirements.cpython-37.pyc
            │   │   │   │   ├── specifiers.cpython-37.pyc
            │   │   │   │   ├── utils.cpython-37.pyc
            │   │   │   │   └── version.cpython-37.pyc
            │   │   │   ├── _compat.py
            │   │   │   ├── _structures.py
            │   │   │   ├── markers.py
            │   │   │   ├── requirements.py
            │   │   │   ├── specifiers.py
            │   │   │   ├── utils.py
            │   │   │   └── version.py
            │   │   ├── pyparsing.py
            │   │   └── six.py
            │   ├── archive_util.py
            │   ├── build_meta.py
            │   ├── cli-32.exe
            │   ├── cli-64.exe
            │   ├── cli.exe
            │   ├── command
            │   │   ├── __init__.py
            │   │   ├── __pycache__
            │   │   │   ├── __init__.cpython-37.pyc
            │   │   │   ├── alias.cpython-37.pyc
            │   │   │   ├── bdist_egg.cpython-37.pyc
            │   │   │   ├── bdist_rpm.cpython-37.pyc
            │   │   │   ├── bdist_wininst.cpython-37.pyc
            │   │   │   ├── build_clib.cpython-37.pyc
            │   │   │   ├── build_ext.cpython-37.pyc
            │   │   │   ├── build_py.cpython-37.pyc
            │   │   │   ├── develop.cpython-37.pyc
            │   │   │   ├── dist_info.cpython-37.pyc
            │   │   │   ├── easy_install.cpython-37.pyc
            │   │   │   ├── egg_info.cpython-37.pyc
            │   │   │   ├── install.cpython-37.pyc
            │   │   │   ├── install_egg_info.cpython-37.pyc
            │   │   │   ├── install_lib.cpython-37.pyc
            │   │   │   ├── install_scripts.cpython-37.pyc
            │   │   │   ├── py36compat.cpython-37.pyc
            │   │   │   ├── register.cpython-37.pyc
            │   │   │   ├── rotate.cpython-37.pyc
            │   │   │   ├── saveopts.cpython-37.pyc
            │   │   │   ├── sdist.cpython-37.pyc
            │   │   │   ├── setopt.cpython-37.pyc
            │   │   │   ├── test.cpython-37.pyc
            │   │   │   ├── upload.cpython-37.pyc
            │   │   │   └── upload_docs.cpython-37.pyc
            │   │   ├── alias.py
            │   │   ├── bdist_egg.py
            │   │   ├── bdist_rpm.py
            │   │   ├── bdist_wininst.py
            │   │   ├── build_clib.py
            │   │   ├── build_ext.py
            │   │   ├── build_py.py
            │   │   ├── develop.py
            │   │   ├── dist_info.py
            │   │   ├── easy_install.py
            │   │   ├── egg_info.py
            │   │   ├── install.py
            │   │   ├── install_egg_info.py
            │   │   ├── install_lib.py
            │   │   ├── install_scripts.py
            │   │   ├── launcher\ manifest.xml
            │   │   ├── py36compat.py
            │   │   ├── register.py
            │   │   ├── rotate.py
            │   │   ├── saveopts.py
            │   │   ├── sdist.py
            │   │   ├── setopt.py
            │   │   ├── test.py
            │   │   ├── upload.py
            │   │   └── upload_docs.py
            │   ├── config.py
            │   ├── dep_util.py
            │   ├── depends.py
            │   ├── dist.py
            │   ├── extension.py
            │   ├── extern
            │   │   ├── __init__.py
            │   │   └── __pycache__
            │   │       └── __init__.cpython-37.pyc
            │   ├── glibc.py
            │   ├── glob.py
            │   ├── gui-32.exe
            │   ├── gui-64.exe
            │   ├── gui.exe
            │   ├── launch.py
            │   ├── lib2to3_ex.py
            │   ├── monkey.py
            │   ├── msvc.py
            │   ├── namespaces.py
            │   ├── package_index.py
            │   ├── pep425tags.py
            │   ├── py27compat.py
            │   ├── py31compat.py
            │   ├── py33compat.py
            │   ├── sandbox.py
            │   ├── script\ (dev).tmpl
            │   ├── script.tmpl
            │   ├── site-patch.py
            │   ├── ssl_support.py
            │   ├── unicode_utils.py
            │   ├── version.py
            │   ├── wheel.py
            │   └── windows_support.py
            └── setuptools-40.8.0.dist-info
                ├── INSTALLER
                ├── LICENSE
                ├── METADATA
                ├── RECORD
                ├── WHEEL
                ├── dependency_links.txt
                ├── entry_points.txt
                ├── top_level.txt
                └── zip-safe

108 directories, 816 files

```

---

##

```bash


```
