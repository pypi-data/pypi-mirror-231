deprecation
===========

[![Documentation
Status](https://readthedocs.org/projects/deprecation/badge/?version=latest)](http://deprecation.readthedocs.io/en/latest/)

Fork of Brian Curtin's [deprecation](https://github.com/briancurtin/deprecation)
library, updated primarily for use in the
[`snakebids`](https://github.com/akhanf/snakebids) library.


The following README is copied from the original library, with relevant
modifications. The linked documentation is generally applicable, although
installation instructions will refer back to the original library.


# README

The `deprecated` library provides a `deprecated` decorator and a
`fail_if_not_removed` decorator for your tests. Together, the two enable the
automation of several things:

1. The docstring of a deprecated method gets the deprecation details appended to
   the end of it. If you generate your API docs direct from your source, you
   don't need to worry about writing your own notification. You also don't need
   to worry about forgetting to write it. It's done for you.
2. Rather than having code live on forever because you only deprecated it but
   never actually moved on from it, you can have your tests tell you when it's
   time to remove the code. The `@deprecated` decorator can be told when it's
   time to entirely remove the code, which causes `@fail_if_not_removed` to
   raise an `AssertionError`, causing either your unittest or py.test tests to
   fail.

See http://deprecation.readthedocs.io/ for the full documentation.

## Installation

```bash
pip install pvandyken.deprecated
```

## Usage

```py

from pvandyken import deprecated

@deprecated.deprecated(deprecated_in="1.0", removed_in="2.0",
                        current_version=__version__,
                        details="Use the bar function instead")
def foo():
   """Do some stuff"""
   return 1
```

## ...but doesn't Python ignore `DeprecationWarning`?

Yes, by default since 2.7—and for good reason [^1] —and this works fine with
that.

1. It often makes sense for you to run your tests with a `-W` flag or the
   `PYTHONWARNINGS` environment variable so you catch warnings in development
   and handle them appropriately. The warnings raised by this library show up
   there, as they're subclasses of the built-in `DeprecationWarning`. See the
   [Command Line](https://docs.python.org/2/using/cmdline.html#cmdoption-W) and
   [Environment
   Variable](https://docs.python.org/2/using/cmdline.html#envvar-PYTHONWARNINGS)
   documentation for more details.
2. Even if you don't enable those things, the behavior of this library remains
   the same. The docstrings will still be updated and the tests will still fail
   when they need to. You'll get the benefits regardless of what Python cares
   about `DeprecationWarning`.

----

[^1]: Exposing application users to `DeprecationWarning`s that are emitted by
      lower-level code needlessly involves end-users in "how things are done."
      It often leads to users raising issues about warnings they're presented,
      which on one hand is done rightfully so, as it's been presented to them as
      some sort of issue to resolve. However, at the same time, the warning
      could be well known and planned for. From either side, loud
      `DeprecationWarning`s can be seen as noise that isn't necessary outside of
      development.
