import subprocess
import sys
import os
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GLib, Gdk
from threading import Thread
from time import sleep

# VERSION = 1.1.7
ver = "1.1.7"


# TODO


# CHECK IF THE NORDVPN COMMANDLINE TOOL IS INSTALLED
file = "/usr/bin/nordvpn"
if os.path.exists(file):
	print("Found the nordvpn binary. (CONTINUE)")
else:
	print("Can't find the nordvpn binary. It should be in /usr/bin/ (EXIT)")
	sys.exit(0)


# CHECK IF YOU'RE LOGGED INTO NORDVPN
print("Checking if you are logged in to nordvpn. Please wait.")
status = subprocess.Popen("/usr/bin/nordvpn login", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
							universal_newlines=True)
rcstat = status.wait()
statout, staterr = status.communicate()
statout = statout.strip('\n')

if "already" in statout:
	print("You are logged in to nordvpn. (CONTINUE)")
else:
	print(statout)
	print("You are not logged in to nordvpn. Please log in to nordvpn first.(EXIT)")
	sys.exit(0)


# GUI SIGNAL HANDLER FUNCTIONS

def Stop_Application(obj):
	Gtk.main_quit()
	sys.exit(0)


def Key_Event(obj, event):
	if event.keyval == Gdk.KEY_q and event.state & Gdk.ModifierType.CONTROL_MASK:
		Gtk.main_quit()
		sys.exit(0)

	if event.keyval == Gdk.KEY_m and event.state & Gdk.ModifierType.CONTROL_MASK:
		win.iconify()


def Button_Connect_Clicked(obj):
	item = combobox1.get_model()[combobox1.get_active()]
	if item[0] != "Select Country  ":
		status = subprocess.Popen("/usr/bin/nordvpn c " + item[0], shell=True,
								stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
		rcstat = status.wait()
	else:
		status = subprocess.Popen("/usr/bin/nordvpn c", shell=True,
								stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
		rcstat = status.wait()


def Button_Disconnect_Clicked(obj):
	status = subprocess.Popen("/usr/bin/nordvpn d", shell=True,
								stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
	rcstat = status.wait()


def Technology_Changed(obj):
	item = combobox2.get_model()[combobox2.get_active()]
	#print("technology changed" + " to " + item[0])
	if item[0] != "Technology    ":
		status = subprocess.Popen("/usr/bin/nordvpn set technology " + item[0], shell=True,
			stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
		rcstat = status.wait()
	combobox2.set_active(0)


def Protocol_Changed(obj):
	item = combobox3.get_model()[combobox3.get_active()]
	#print("protocol changed" + " to " + item[0])
	if item[0] != "Protocol      ":
		status = subprocess.Popen("/usr/bin/nordvpn set protocol " + item[0], shell=True,
								stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
		rcstat = status.wait()
	combobox3.set_active(0)


def Routing_Changed(obj):
	item = combobox51.get_model()[combobox51.get_active()]
	if item[0] != "Routing       ":
		routing = subprocess.Popen("/usr/bin/nordvpn set routing " + item[0], shell=True,
								   stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
		rcstat = routing.wait()
	combobox51.set_active(0)


def Killswitch_Changed(obj):
	item = combobox4.get_model()[combobox4.get_active()]
	#print("killswitch changed" + " to " + item[0])
	if item[0] != "Kill Switch   ":
		status = subprocess.Popen("/usr/bin/nordvpn set killswitch " + item[0], shell=True,
								stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
		rcstat = status.wait()
	combobox4.set_active(0)


def Connect_Changed(obj):
	item = combobox3a.get_model()[combobox3a.get_active()]
	if item[0] != "Auto-Connect  ":
		status = subprocess.Popen("/usr/bin/nordvpn set autoconnect " + item[0], shell=True,
								stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
		rcstat = status.wait()
	combobox3a.set_active(0)


def Notify_Changed(obj):
	item = combobox4a.get_model()[combobox4a.get_active()]
	if item[0] != "Notification  ":
		status = subprocess.Popen("/usr/bin/nordvpn set notify " + item[0], shell=True,
								stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
		rcstat = status.wait()
	combobox4a.set_active(0)



def Analytics_Changed(obj):
	item = combobox6a.get_model()[combobox6a.get_active()]
	if item[0] != "Analytics      ":
		status = subprocess.Popen("/usr/bin/nordvpn set analytics " + item[0], shell=True,
								stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
		rcstat = status.wait()
	combobox6a.set_active(0)


def IPV6_Changed(obj):
	item = combobox6b.get_model()[combobox6b.get_active()]
	if item[0] != "IPV6           ":
		status = subprocess.Popen("/usr/bin/nordvpn set ipv6 " + item[0], shell=True,
								stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
		rcstat = status.wait()
	combobox6b.set_active(0)


def Lan_Discovery_Changed(obj):
	item = combobox6c.get_model()[combobox6c.get_active()]
	if item[0] != "Lan Discovery  ":
		status = subprocess.Popen("/usr/bin/nordvpn set lan-discovery " + item[0], shell=True,
								stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
		rcstat = status.wait()
	combobox6c.set_active(0)


def Update_TextView(st):
	tbuffer.set_text("\n  " + st)


def Get_Nordvpn_Status():
	i = 1
	while i != 0:
		txt = ""
		y = 0
		status = subprocess.Popen("/usr/bin/nordvpn status", shell=True, stdout=subprocess.PIPE,
								stderr=subprocess.PIPE, universal_newlines=True)
		rcstat = status.wait()
		statout, staterr = status.communicate()
		statout = statout.strip('\n')
		lstatus = statout.split('\n')
		for st in lstatus:
			if st != "\r" and st != "-" and st != "/" and st != "\\" and st != "|" and st != "\n":
				if st != "":
					txt = txt + "\n  " + st

		status = subprocess.Popen("/usr/bin/nordvpn settings", shell=True, stdout=subprocess.PIPE,
								stderr=subprocess.PIPE, universal_newlines=True)
		rcstat = status.wait()
		statout, staterr = status.communicate()
		statout = statout.strip('\n')
		lsettings = statout.split('\n')

		while y < len(lsettings):
			if "Routing" in lsettings[y]:
				txt = txt + "\n  ------\n  " + lsettings[y] + "\n"
			y = y + 1
		y = 0

		while y < len(lsettings):
			if "Kill" in lsettings[y]:
				txt = txt + "  " + lsettings[y] + "\n"
			y = y + 1
		y = 0

		while y < len(lsettings):
			if "Auto" in lsettings[y]:
				txt = txt + "  " + lsettings[y] + "\n"
			y = y + 1
		y = 0

		while y < len(lsettings):
			if "Notify" in lsettings[y]:
				txt = txt + "  " + lsettings[y] + "\n"
			y = y + 1
		y = 0

		while y < len(lsettings):
			if "Analytics" in lsettings[y]:
				txt = txt + "  " + lsettings[y] + "\n"
			y = y + 1
		y = 0

		while y < len(lsettings):
			if "IPv6" in lsettings[y]:
				txt = txt + "  " + lsettings[y] + "\n"
			y = y + 1
		y = 0

		while y < len(lsettings):
			if "LAN" in lsettings[y]:
				txt = txt + "  " + lsettings[y] + "\n"
			y = y + 1
		y = 0

		txt = txt.strip()
		GLib.idle_add(Update_TextView, txt)
		sleep(4)


# MAIN CODE

# CREATE THE MAIN WINDOW
win = Gtk.Window()
win.set_title("gNordVPN " + ver)
win.set_default_size(350, 530)
file = "./gnordvpn.svg"
if os.path.exists(file):
	win.set_default_icon_from_file("./gnordvpn.svg")
win.set_resizable(False)
win.connect("destroy", Stop_Application)
win.connect("key-press-event", Key_Event)

css_provider = Gtk.CssProvider()
css_provider.load_from_path('./gnordvpn.css')

screen = win.get_screen()
context = win.get_style_context()
context.add_provider_for_screen(screen, css_provider, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)

# CREATE SOME SEPARATORS
sep1 = Gtk.Separator()
sep2 = Gtk.Separator()
sep3 = Gtk.Separator()
sep4 = Gtk.Separator()

# CREATE THE GUI CONTAINER
box1 = Gtk.VBox(spacing=6)
win.add(box1)
boxs = Gtk.Box(spacing=6)
boxs.pack_start(sep1, True, True, 0)
box1.pack_start(boxs, False, False, 0)
box2 = Gtk.Box(spacing=6)
box1.pack_start(box2, False, False, 0)
boxss = Gtk.Box(spacing=6)
boxss.pack_start(sep2, True, True, 0)
box1.pack_start(boxss, False, False, 0)
box3 = Gtk.Box(spacing=6)
box1.pack_start(box3, True, True, 0)
boxsss = Gtk.Box(spacing=6)
boxsss.pack_start(sep3, True, True, 0)
box1.pack_start(boxsss, False, False, 0)
box4 = Gtk.Box(spacing=6)
box1.pack_start(box4, False, False, 0)
box51 = Gtk.Box(spacing=6)
box1.pack_start(box51, False, False, 0)
box6a = Gtk.Box(spacing=6)
box1.pack_start(box6a, False, False, 0)
box7 = Gtk.Box(spacing=6)
box7.pack_start(sep4, True, True, 0)
box1.pack_start(box7, False, False, 0)
box8 = Gtk.Box(spacing=6)
box1.pack_start(box8, False, False, 0)

# BUILT USER INTERFACE
label0 = Gtk.Label()
label0.set_width_chars(1)
box2.pack_start(label0, False, False, 0)
label1 = Gtk.Label()
label1.set_text("VPN Connection")
label1.set_width_chars(13)
box2.pack_start(label1, False, False, 0)
label1a = Gtk.Label()
label1a.set_width_chars(1)
box2.pack_start(label1a, False, False, 0)

liststore1 = Gtk.ListStore(str)
liststore1.append(['Select Country  '])
liststore1.append(['au'])
liststore1.append(['be'])
liststore1.append(['br'])
liststore1.append(['ca'])
liststore1.append(['co'])
liststore1.append(['de'])
liststore1.append(['fi'])
liststore1.append(['fr'])
liststore1.append(['it'])
liststore1.append(['jp'])
liststore1.append(['nl'])
liststore1.append(['no'])
liststore1.append(['nz'])
liststore1.append(['uk'])
liststore1.append(['us'])
liststore1.append(['p2p'])
liststore1.append(['double_vpn'])
liststore1.append(['onion_over_vpn'])

cell = Gtk.CellRendererText()
combobox1 = Gtk.ComboBox()
combobox1.pack_start(cell, True)
combobox1.add_attribute(cell, 'text', 0)
combobox1.set_model(liststore1)
combobox1.set_active(0)
box2.pack_start(combobox1, False, False, 0)

button1 = Gtk.Button.new_with_label("  Connect  ")
button1.connect("clicked", Button_Connect_Clicked)
box2.pack_start(button1, False, False, 0)

button2 = Gtk.Button.new_with_label("Disconnect")
button2.connect("clicked", Button_Disconnect_Clicked)
box2.pack_start(button2, False, False, 0)

label2 = Gtk.Label()
box2.pack_start(label2, True, True, 0)

# CREATE THE TEXTVIEW
tbuffer = Gtk.TextBuffer()
textview = Gtk.TextView.new_with_buffer(tbuffer)
textview.set_name("textview")
textview.set_buffer(tbuffer)
textview.set_editable(False)
textview.set_wrap_mode(Gtk.WrapMode.WORD)
box3.pack_start(textview, True, True, 0)

label3 = Gtk.Label()
label3.set_width_chars(1)
box4.pack_start(label3, False, False, 0)
liststore2 = Gtk.ListStore(str)
liststore2.append(['Technology    '])
liststore2.append(['nordlynx'])
liststore2.append(['openvpn'])
cell2 = Gtk.CellRendererText()
combobox2 = Gtk.ComboBox()
combobox2.set_name("cbbox")
combobox2.pack_start(cell2, True)
combobox2.add_attribute(cell2, 'text', 0)
combobox2.set_model(liststore2)
combobox2.set_active(0)
combobox2.connect("changed", Technology_Changed)
box4.pack_start(combobox2, False, False, 0)

label51 = Gtk.Label()
label51.set_width_chars(1)
box51.pack_start(label51, False, False, 0)
liststore3 = Gtk.ListStore(str)
liststore3.append(['Protocol      '])
liststore3.append(['tcp'])
liststore3.append(['udp'])
cell3 = Gtk.CellRendererText()
combobox3 = Gtk.ComboBox()
combobox3.set_name("cbbox")
combobox3.pack_start(cell3, True)
combobox3.add_attribute(cell3, 'text', 0)
combobox3.set_model(liststore3)
combobox3.set_active(0)
combobox3.connect("changed", Protocol_Changed)
box51.pack_start(combobox3, False, False, 0)

label6a = Gtk.Label()
label6a.set_width_chars(1)
box6a.pack_start(label6a, False, False, 0)
liststore51 = Gtk.ListStore(str)
liststore51.append(['Routing       '])
liststore51.append(['enable'])
liststore51.append(['disable'])
cell51 = Gtk.CellRendererText()
combobox51 = Gtk.ComboBox()
combobox51.set_name("cbbox")
combobox51.pack_start(cell51, True)
combobox51.add_attribute(cell51, 'text', 0)
combobox51.set_model(liststore51)
combobox51.set_active(0)
combobox51.connect("changed", Routing_Changed)
box6a.pack_start(combobox51, False, False, 0)

liststore4 = Gtk.ListStore(str)
liststore4.append(['Kill Switch   '])
liststore4.append(['enable'])
liststore4.append(['disable'])
cell4 = Gtk.CellRendererText()
combobox4 = Gtk.ComboBox()
combobox4.set_name("cbbox")
combobox4.pack_start(cell4, True)
combobox4.add_attribute(cell4, 'text', 0)
combobox4.set_model(liststore4)
combobox4.set_active(0)
combobox4.connect("changed", Killswitch_Changed)
box4.pack_start(combobox4, False, False, 0)

liststore3a = Gtk.ListStore(str)
liststore3a.append(['Auto-Connect  '])
liststore3a.append(['enable'])
liststore3a.append(['disable'])
cell3a = Gtk.CellRendererText()
combobox3a = Gtk.ComboBox()
combobox3a.set_name("cbbox")
combobox3a.pack_start(cell3a, True)
combobox3a.add_attribute(cell3a, 'text', 0)
combobox3a.set_model(liststore3a)
combobox3a.set_active(0)
combobox3a.connect("changed", Connect_Changed)
box51.pack_start(combobox3a, False, False, 0)

liststore4a = Gtk.ListStore(str)
liststore4a.append(['Notification  '])
liststore4a.append(['enable'])
liststore4a.append(['disable'])
cell4a = Gtk.CellRendererText()
combobox4a = Gtk.ComboBox()
combobox4a.set_name("cbbox")
combobox4a.pack_start(cell4a, True)
combobox4a.add_attribute(cell4a, 'text', 0)
combobox4a.set_model(liststore4a)
combobox4a.set_active(0)
combobox4a.connect("changed", Notify_Changed)
box6a.pack_start(combobox4a, False, False, 0)

liststore6a = Gtk.ListStore(str)
liststore6a.append(['Analytics      '])
liststore6a.append(['enable'])
liststore6a.append(['disable'])
cell6a = Gtk.CellRendererText()
combobox6a = Gtk.ComboBox()
combobox6a.set_name("cbbox")
combobox6a.pack_start(cell6a, True)
combobox6a.add_attribute(cell6a, 'text', 0)
combobox6a.set_model(liststore6a)
combobox6a.set_active(0)
combobox6a.connect("changed", Analytics_Changed)
box4.pack_start(combobox6a, False, False, 0)

liststore6b = Gtk.ListStore(str)
liststore6b.append(['IPV6           '])
liststore6b.append(['enable'])
liststore6b.append(['disable'])
cell6b = Gtk.CellRendererText()
combobox6b = Gtk.ComboBox()
combobox6b.set_name("cbbox")
combobox6b.pack_start(cell6b, True)
combobox6b.add_attribute(cell6b, 'text', 0)
combobox6b.set_model(liststore6b)
combobox6b.set_active(0)
combobox6b.connect("changed", IPV6_Changed)
box51.pack_start(combobox6b, False, False, 0)
label6c = Gtk.Label()
box51.pack_start(label6c, True, True, 0)

liststore6c = Gtk.ListStore(str)
liststore6c.append(['Lan Discovery  '])
liststore6c.append(['enable'])
liststore6c.append(['disable'])
cell6c = Gtk.CellRendererText()
combobox6c = Gtk.ComboBox()
combobox6c.set_name("cbbox")
combobox6c.pack_start(cell6c, True)
combobox6c.add_attribute(cell6c, 'text', 0)
combobox6c.set_model(liststore6c)
combobox6c.set_active(0)
combobox6c.connect("changed", Lan_Discovery_Changed)
box6a.pack_start(combobox6c, False, False, 0)

# ADD A STATUSBAR WITH NORDVPN VERSION
sb = Gtk.Statusbar()
box8.pack_start(sb, True, True, 0)
result = subprocess.Popen("/usr/bin/nordvpn version", shell=True,
						stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
rc = result.wait()
out, err = result.communicate()
line = out.split('\n')
line[3].strip()
sb.push(0, line[3])

# START A THREAD THAT GETS THE NORDVPN STATUS EVERY 4 SECONDS
thread = Thread(target=Get_Nordvpn_Status)
thread.daemon = True
thread.start()

# START THE APPLICATION
win.show_all()
Gtk.main()
