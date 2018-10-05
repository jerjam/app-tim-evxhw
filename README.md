# Introduction
The source code initially was developt at Cells-Alba and has been wrapped into .rpm package which this repository provides. It delivers an expert GUI control over EVR230/EVR300 and EVG230/EVG300 event receiver from MRF (http://www.mrf.fi/).

# Requirements
It is developed to be platform intependent but the usage and tests always were done on 32bit Linux (Centos6). The dependencies can be downloaded from: https://github.com/jerjam/rpms-rare

 # Dependencies
* 32 bit MRF kernel modules for EVR/EVG (kmod-pci_mrfevx*.rpm) or any other package provided by MRF (the kernel modules have to be loaded).
* Shared 32bit objects which bind the C API of EVR/EVG to python (python-libcellstimevx*.rpm)
* numpy
* PyQt (PyQt*.rpm)
