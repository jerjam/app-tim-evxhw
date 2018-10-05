Name:       app-tim-evxhw
Version:    1.0.0
Release:    2
Summary:    Expert GUIs to control MRF cPCI EVG/EVR locally.

Group:      Development/Tools
License:    GPLv2
URL:        www.maxiv.lu.se
#Source0:   %{name}-%{version}.tar.gz
Source0:    %{name}.tar.gz

Requires:   numpy
Requires:   PyQt
#Requires:  kmod-mrf-tim-evx

BuildArch:  i386

Packager:   jerzy.jamroz@maxiv.lu.se
Vendor:     MAXIV

#Package install directory
%define homedir /opt/%{name}

%description
%(cat %{_specdir}/../README.md)

%pre
echo "PyQt rpm download site: https://github.com/jerjam/rpms-rare/raw/master/"

%prep
#%setup -q
%setup -n %{name}

%install
rm -rf "$RPM_BUILD_ROOT"
mkdir -p "$RPM_BUILD_ROOT%{homedir}"
cp -R * "$RPM_BUILD_ROOT%{homedir}"

%post
ln -s %{homedir}/cttihw/cttievghw /sbin/evghw
ln -s %{homedir}/cttihw/cttievrhw /sbin/evrhw

%files
#%{homedir}
#%attr(<mode>, <user>, <group>) <file>
%attr(0775, root, mrf) %{homedir}
#%attr(0775, root, mrf) %{homedir}/*

%clean
rm -rf $RPM_BUILD_ROOT

%postun
rm /sbin/evghw
rm /sbin/evrhw
rm -rf %{homedir}

