
all: libmicroninja-logging.a

microninja-log.o:
	gcc -std=c99 -D_BSD_SOURCE -gdwarf-2 -c microninja-log.c -o microninja-log.o

libmicroninja-logging.a: microninja-log.o
	ar -r $@ $^

clean: 
	rm -f *.a *.o *~
