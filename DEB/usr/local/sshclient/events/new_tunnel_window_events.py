# -*- coding: utf-8 -*-
from model.tunnel import Tunnel
from windows.message_box import MessageBox


class NewTunnelWindowEvents:

    window = None
    builder = None
    add_tunnel_callback = None

    def __init__(self, window, builder, add_tunnel_callback):
        # Copy the parameters
        self.window = window
        self.builder = builder
        self.add_tunnel_callback = add_tunnel_callback

    def on_btn_add_clicked(self, btn):
        # Get the entries
        txt_local_port = self.builder.get_object("txt_local_port")
        txt_address = self.builder.get_object("txt_host")
        txt_remote_port = self.builder.get_object("txt_remote_port")

        # Validate the form
        if self.validate_form(txt_local_port, txt_address, txt_remote_port):
            # Create a new Tunnel
            tunnel = Tunnel()
            tunnel.local_port = txt_local_port.get_text()
            tunnel.address = txt_address.get_text()
            tunnel.remote_port = txt_remote_port.get_text()

            # Call the callback
            self.add_tunnel_callback(tunnel)

            # Destroy the Window
            self.window.destroy()

    def on_btn_cancel_clicked(self, btn):
        self.window.destroy()

    def validate_form(self, local_port, address, remote_port):
        # Start the validation
        if (len(local_port.get_text()) == 0 or len(address.get_text()) == 0 or
                len(remote_port.get_text()) == 0):

            # Show the message
            MessageBox("All fields are mandatory")

            # Return False to not call the callback
            return False

        elif local_port.get_text().isdigit() is False:
            # Show the message
            MessageBox("Local port must be a number")

            # Return False to not call the callback
            return False

        elif remote_port.get_text().isdigit() is False:
            # Show the message
            MessageBox("Remote port must be a number")

            # Return False to not call the callback
            return False

        elif int(local_port.get_text()) <= 0 or int(local_port.get_text()) > 65565:
            # Show the message
            MessageBox("Local port must be greater than 0 and less than 65565")

            # Return False to not call the callback
            return False

        elif int(remote_port.get_text()) <= 0 or int(remote_port.get_text()) > 65565:
            # Show the message
            MessageBox("Remote port must be greater than 0 and less than 65565")

            # Return False to not call the callback
            return False

        # If everything is OK, return True
        return True


