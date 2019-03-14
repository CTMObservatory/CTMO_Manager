all: py_scripts schedulerd.service telescoped.service
telescope: telescoped.service
scheduler: schedulerd.service
.PHONY: all telescope scheduler py_scripts install uninstall clean

service_dir=/etc/systemd/system
conf_dir=/etc/ctmo
awk_script='BEGIN {FS="="; OFS="="}{if ($$1=="ExecStart") {$$2=exec_path} if (substr($$1,1,1) != "\#") {print $$0}}'

py_scripts: $(wildcard *.py)
	pip install .

%d.service: %d.service.template ctmomanager/%.py
# awk is needed to replace the absolute path of the scheduler script in the .service file
	awk -v exec_path=$(shell which $(*)) $(awk_script) $< > $@

$(conf_dir):
	mkdir -p $@

install: $(service_dir) $(conf_dir) schedulerd.service telescoped.service ctmo.conf.yaml
	cp *.service $(service_dir)
	cp ctmo.conf.yaml $(conf_dir)/ctmo.conf.yaml

uninstall:
	-systemctl stop schedulerd
	-systemctl stop telescoped
	-pip uninstall -y ctmomanager
	-rm $(service_dir)/schedulerd.service
	-rm $(service_dir)/telescoped.service
	rm -r $(conf_dir)

clean:
	-rm *.service
