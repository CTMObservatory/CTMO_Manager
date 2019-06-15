# Find out the operating system
UNAME := $(shell uname)

all: py_scripts telescope scheduler

ifeq ($(UNAME), Linux)
telescope: telescoped.service
scheduler: schedulerd.service
uninstall: uninstall_linux
services=telescoped.service schedulerd.service
service_dir=/etc/systemd/system
endif
ifeq ($(UNAME), Darwin)
telescope: org.ctmo.telescope.plist
scheduler: org.ctmo.scheduler.plist
uninstall: uninstall_osx
services=org.ctmo.scheduler.plist org.ctmo.telescope.plist
service_dir=/Library/LaunchAgents
endif
conf_dir=/etc/ctmo

.PHONY: all telescope scheduler py_scripts install uninstall clean

py_scripts: $(wildcard *.py)
	pip install .

%d.service: templates/%d.service.template ctmomanager/%.py
# sed is needed to replace the absolute path of the scheduler script in the .service file
	sed 's,scriptname,$(shell which $(*)),' $< > $@

org.ctmo.%.plist: templates/org.ctmo.%.plist.template
# sed is needed to replace the absolute path of the scheduler script in the .service file
	sed 's,scriptname,$(shell which $(*)),' $< > $@

$(conf_dir):
	mkdir -p $@

install: $(service_dir) $(conf_dir) scheduler telescope ctmo.conf.yaml
	cp $(services) $(service_dir)
	cp ctmo.conf.yaml $(conf_dir)/ctmo.conf.yaml

uninstall_linux:
	-systemctl stop schedulerd
	-systemctl stop telescoped
	-pip uninstall -y ctmomanager
	-rm $(service_dir)/schedulerd.service
	-rm $(service_dir)/telescoped.service
	rm -r $(conf_dir)

uninstall_osx:
	-launchctl unload $(service_dir)/org.ctmo.*.plist
	-pip uninstall -y ctmomanager
	-rm $(service_dir)/org.ctmo.*.plist
	rm -r $(conf_dir)

clean:
	-rm *.service
	-rm *.plist
