all: epimetheus service
.PHONY: all epimetheus service install uninstall clean

service_dir=/etc/systemd/system/schedulerd
awk_script='BEGIN {FS="="; OFS="="}{if ($$1=="ExecStart") {$$2=exec_path} if (substr($$1,1,1) != "\#") {print $$0}}'

epimetheus:
	pip install .

service: epimetheus
	# awk is needed to replace the absolute path of the epimetheus executable in the .service file
	awk -v exec_path=$(shell which epimetheus) $(awk_script) schedulerd.service.template > schedulerd.service

service_dir:
	mkdir -p ${service_dir}

install: service_dir
	mv schedulerd.service $(service_dir)

uninstall:
	systemctl stop schedulerd
	pip uninstall scheduler
	rm -r $(service_dir)

clean:
	rm -f schedulerd.service
