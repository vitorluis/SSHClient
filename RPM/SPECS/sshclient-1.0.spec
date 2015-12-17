# SPEC for SSHClient
Summary: SSHClient is a GUI to manage SSH Connections
Name: sshclient
Version: 1.0
Release: 1
License: GPL
Group: Applications/Internet
URL: http://vitorluis.github.io/SSHClient
Packager: Vitor Villar <vitor.luis98@gmail.com>
Requires: openssh-server, sshpass, vte, vte3, gcc, cpp, python3-pip, python-devel, python3-devel
BuildArch: noarch

%description
SSHClient is a GUI to manage SSH Connections

%prep
rm -rf $RPM_BUILD_ROOT
pip3 install pycrypto

%build
mkdir -p %{buildroot}
cd %{buildroot}
tar -xf %{_sourcedir}/sshclient-1.0.tar.gz

%install
mkdir -p /usr/local/sshclient
cp -arf %{buildroot}/* /usr/local/sshclient
ln -s /usr/local/sshclient/sshclient.py /usr/bin/sshclient


%clean
rm -rf %{buildroot}

%files
/usr/local/sshclient/LICENSE
/usr/local/sshclient/README.md
/usr/local/sshclient/collection/__init__.py
/usr/local/sshclient/collection/connections.py
/usr/local/sshclient/collection/tunnels.py
/usr/local/sshclient/data/__init__.py
/usr/local/sshclient/data/database.py
/usr/local/sshclient/data/sshclient.db
/usr/local/sshclient/events/__init__.py
/usr/local/sshclient/events/connection_window_events.py
/usr/local/sshclient/events/delete_connection_window_events.py
/usr/local/sshclient/events/file_export_dialog_events.py
/usr/local/sshclient/events/main_window_events.py
/usr/local/sshclient/events/new_tunnel_window_events.py
/usr/local/sshclient/events/settings_window_events.py
/usr/share/applications/sshclient.desktop
/usr/local/sshclient/model/__init__.py
/usr/local/sshclient/model/connection.py
/usr/local/sshclient/model/settings.py
/usr/local/sshclient/model/tunnel.py
/usr/local/sshclient/settings.py
/usr/local/sshclient/sshclient.py
/usr/local/sshclient/tools/__init__.py
/usr/local/sshclient/tools/password.py
/usr/local/sshclient/ui/__init__.py
/usr/local/sshclient/ui/about_window.glade
/usr/local/sshclient/ui/connection_window.glade
/usr/local/sshclient/ui/delete_connection_window.glade
/usr/local/sshclient/ui/file_export_dialog.glade
/usr/local/sshclient/ui/images/delete.png
/usr/local/sshclient/ui/images/edit.png
/usr/local/sshclient/ui/images/new.png
/usr/local/sshclient/ui/images/ssh.png
/usr/local/sshclient/ui/main_window.glade
/usr/local/sshclient/ui/message_box.glade
/usr/local/sshclient/ui/new_tunnel_window.glade
/usr/local/sshclient/ui/settings_window.glade
/usr/local/sshclient/windows/__init__.py
/usr/local/sshclient/windows/about_window.py
/usr/local/sshclient/windows/connection_window.py
/usr/local/sshclient/windows/delete_connection_window.py
/usr/local/sshclient/windows/file_export_dialog.py
/usr/local/sshclient/windows/main_window.py
/usr/local/sshclient/windows/message_box.py
/usr/local/sshclient/windows/new_tunnel_window.py
/usr/local/sshclient/windows/settings_window.py
/usr/local/sshclient/windows/shell.py
/usr/bin/sshclient
%defattr(-,root,root)
%doc /usr/local/sshclient/README.md

%changelog

