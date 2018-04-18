
all: microninja-launcher microninja-kill-ns

LIBS=-L../microninja-logging -lmicroninja-logging
INCLUDES=-I../microninja-logging 
microninja-launcher:
	gcc -std=c99 -D_BSD_SOURCE -gdwarf-2 $(INCLUDES) microninja-launcher.c $(LIBS) -o microninja-launcher 

microninja-kill-ns:
	gcc -std=c99 -D_BSD_SOURCE -gdwarf-2 $(INCLUDES) microninja-kill-ns.c $(LIBS) -o microninja-kill-ns

clean: 
	rm -f *.a *.o *~ microninja-kill-ns microninja-launcher 
