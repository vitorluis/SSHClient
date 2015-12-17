#!/usr/bin/env python

from distutils.core import setup

setup(name='SSHClient',
      version='1.0',
      description='Manage SSH Connections via GUI',
      author='Vitor Villar',
      author_email='vitor.luis98@gmail.com',
      url='http://vitorluis.github.io/SSHClient/',
      packages=['distutils', 'distutils.command'],
      requires=['Crypto', 'gi']
      )
