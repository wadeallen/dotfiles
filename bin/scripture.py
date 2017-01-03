#!/usr/bin/env python3

import gi
gi.require_version('WebKit', '3.0')

from gi.repository import Gtk,WebKit

view = WebKit.WebView() 

sw = Gtk.ScrolledWindow() 
sw.add(view) 

win = Gtk.Window() 
win.add(sw) 
win.show_all() 

view.open("index.html") 
Gtk.main()
