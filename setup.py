#!/usr/bin/env python

from distutils.core import setup

setup(name='SSHClient',
      version='1.0.1',
      description='Manage SSH Connections via GUI',
      author='Vitor Villar',
      author_email='vitor.luis98@gmail.com',
      url='http://vitorluis.github.io/SSHClient/',
      packages=['collection', 'data', 'events', 'model', 'tools', 'windows', 'ui'],
      package_data={
          'data': ['data/sshclient.db'],
          'ui': ['ui/about_window.glade', 'ui/connection_window.glade', 'ui/delete_connection_window.glade',
                 'ui/file_export_dialog.glade', 'ui/main_window.glade', 'ui/message_box.glade',
                 'ui/new_tunnel_window.glade', 'ui/settings_window.glade']
      },
      data_files=[('bitmaps', ['ui/images/delete.png', 'ui/images/edit.png',
                               'ui/images/new.png', 'ui/images/ssh.png'])],
      requires=['Crypto', 'gi']
      )
