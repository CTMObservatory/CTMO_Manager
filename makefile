all: scheduler_script schedulerd.service
.PHONY: all scheduler_script install uninstall clean

service_dir=/etc/systemd/system
conf_dir=/etc/torosd
awk_script='BEGIN {FS="="; OFS="="}{if ($$1=="ExecStart") {$$2=exec_path} if (substr($$1,1,1) != "\#") {print $$0}}'

scheduler_script: scheduler.py setup.py
	pip install .

schedulerd.service: scheduler.py
# awk is needed to replace the absolute path of the scheduler script in the .service file
	awk -v exec_path=$(shell which scheduler) $(awk_script) schedulerd.service.template > schedulerd.service

$(conf_dir):
	mkdir -p $@

install: $(service_dir) $(conf_dir) schedulerd.service scheduler.conf.yaml
	cp schedulerd.service $(service_dir)
	cp scheduler.conf.yaml $(conf_dir)/scheduler.conf.yaml

uninstall:
	-systemctl stop schedulerd
	-pip uninstall scheduler
	rm $(service_dir)/schedulerd.service
	rm -r $(conf_dir)

clean:
	-rm schedulerd.service
