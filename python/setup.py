#!/usr/bin/env python

from distutils.core import setup, Extension

pysequoia_sources = ['sequoiamodule.c', 'py-session.c', 'py-sequence.c', 'py-trigger.c', 'py-port.c']

sequoia_extension = Extension("sequoia",
                                sources=pysequoia_sources,
                                libraries=['sequoia', 'jack'])

setup(name="sequoia", ext_modules=[sequoia_extension])
