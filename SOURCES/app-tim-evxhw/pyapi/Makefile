
ASTYLE=`if [ \`which astyle\` ]; then which astyle; fi`
PYLIBVERSIONID=lib.`python -c "import sys,distutils.util; print distutils.util.get_platform()+'-'+('.'.join(map(str, sys.version_info[:2])))"`
BUILDDIR=$(shell uname -r)
PYTHONPATH=$(shell pwd)

$(info PYTHONPATH=$(PYTHONPATH))
#$(info $(ASTYLE))
#$(info $(PYLIBVERSIONID))

all: evg.so evr.so
	mkdir -p ../build/$(BUILDDIR)/
	cp -v ev?.so ../build/$(BUILDDIR)/
#	rm -f erapi.c erapi.h egapi.c egapi.h egcpci.h
#	rm -f *~ *.so

evg.so: evgmodule.c evgmodule.h egapi.c egapi.h egcpci.h traducg.c
	python setup-evg.py build
	cp build/$(PYLIBVERSIONID)/evg.so .

evr.so: evrmodule.c evrmodule.h erapi.c erapi.h traducr.c
	python setup-evr.py build
	cp build/$(PYLIBVERSIONID)/evr.so .

traducg.c: egapi.c egapi.h
#	if [ ${ASTYLE} ]; then  ../pyparse/evg-parse.py | ${ASTYLE} > traducg.c ; else ../pyparse/evg-parse.py > traducg.c; fi
#	python ../pyparse/evg-parse.py > traducg.c
	pyparse/evg-parse.py > traducg.c

traducr.c: erapi.c erapi.h
#	if [ ${ASTYLE} ]; then  ../pyparse/evr-parse.py | ${ASTYLE} > traducr.c ; else ../pyparse/evr-parse.py > traducr.c; fi
#	python ../pyparse/evr-parse.py > traducr.c
	pyparse/evr-parse.py > traducr.c

egapi.c: ../capi/egapi.c
	cp ../capi/egapi.c .
#	echo $(PWD)

egapi.h: ../capi/egapi.h
	cp ../capi/egapi.h .

egcpci.h: ../capi/egcpci.h
	cp ../capi/egcpci.h .

erapi.c: ../capi/erapi.c
	cp ../capi/erapi.c .

erapi.h: ../capi/erapi.h
	cp ../capi/erapi.h .

clean: pyclean testclean rmbuild
	rm -f erapi.c erapi.h egapi.c egapi.h egcpci.h
	rm -f traducr.c traducg.c
	rm -f *~ *.so

rmbuild:
	rm build -fr

pyclean:
	rm -f *.pyc

testclean:
	rm -f test/*.pyc test/*~
	rm -f test_*

TODO:
	grep --color TODO *

wipe: rmbuild
