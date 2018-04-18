#
# Placeholder makefile so "debuild" can be gently persuaded to work
#

.PHONY: microninja-keys-pressed microninja-splash microninja-launcher microninja-logging

all: microninja-keys-pressed microninja-splash microninja-launcher

microninja-keys-pressed:
	cd microninja-keys-pressed && make

microninja-splash: microninja-logging
	cd microninja-splash && make

microninja-launcher: microninja-logging
	cd microninja-launcher && make

microninja-logging:
	cd microninja-logging && make
