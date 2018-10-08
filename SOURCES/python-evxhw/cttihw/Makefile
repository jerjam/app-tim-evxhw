
all: all-evr all-evg

all-evg: eventgeneratorform.py sequenceeditorform.py 

all-evr: eventreceiverform.py pulsemapform.py pulseeditorform.py 


eventgeneratorform.py: ui/eventgeneratorform.ui
	pyuic $? -o $@

sequenceeditorform.py: ui/sequenceeditorform.ui
	pyuic $? -o $@

eventreceiverform.py: ui/eventreceiverform.ui
	pyuic $? -o $@

pulsemapform.py: ui/pulsemapform.ui
	pyuic $? -o $@

pulseeditorform.py: ui/pulseeditorform.ui
	pyuic $? -o $@

clean:
	rm -f *form.py *.pyc *~ 
	rm -f ui/*~
	cd access/ && rm -f *~ *.pyc
	rm -f evgcontrols/*.pyc evgcontrols/*~
	rm -f evrcontrols/*.pyc evrcontrols/*~

TODO:
	grep --color TODO `find . | grep .py$$`


