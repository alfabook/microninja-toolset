#
# kano-keys-pressed
#
#  A tool to detect key modifers being pressed (Shift, Ctrl, Alt, ...)
#

all: microninja-keys-pressed

microninja-keys-pressed: microninja-keys-pressed.o hid.o
	g++ -g microninja-keys-pressed.o hid.o -o microninja-keys-pressed

hid.o: hid.cpp
	g++ -c -g hid.cpp

microninja-keys-pressed.o: microninja-keys-pressed.cpp
	g++ -c microninja-keys-pressed.cpp
