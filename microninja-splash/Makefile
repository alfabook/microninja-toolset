# 18/01/2016 Alfabook srl
# Rebadged with microninja

#kano-get-start-time/* kano-get-start-time.c
# 
# Copyright (C) 2015 Kano Computing Ltd.
# License: http://opensource.org/licenses/MIT
# 
# Build file for kano-splash and related utilities.
#

# Copyright (C) 2016 Alfabook srl
# rebadged with microninja

OBJS=microninja-splash.o backgroundLayer.o imageLayer.o \
	 loadpng.o image.o get-start-time.o
BIN= microninja-splash microninja-get-start-time
CFLAGS+=-Wall -g -O3  $(shell libpng-config --cflags)
LDFLAGS+=-L/opt/vc/lib/ -lbcm_host -lm $(shell libpng-config --ldflags) -L../microninja-logging -lmicroninja-logging

INCLUDES+=-I/opt/vc/include/ -I/opt/vc/include/interface/vcos/pthreads -I/opt/vc/include/interface/vmcs_host/linux -I../microninja-logging 

all: $(BIN)

%.o: %.c
	@rm -f $@ 
	$(CC) $(CFLAGS) $(INCLUDES) -g -c $< -o $@ -Wno-deprecated-declarations

microninja-splash: $(OBJS)
	$(CC) -o $@ -Wl,--whole-archive $(OBJS) $(LDFLAGS) -Wl,--no-whole-archive -rdynamic

clean:
	@rm -f $(OBJS)
	@rm -f $(BIN)



microninja-get-start-time: microninja-get-start-time.c get-start-time.c
	$(CC) -g $^  -o $@
