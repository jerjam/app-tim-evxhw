PKG=app-tim-evxhw
PKGDIR=$(PWD)

$(info $(PKGDIR))
all:
	cd ${PKGDIR}/SOURCES/ && tar -czvf $(PKG).tar.gz $(PKG)
	rpmbuild --define "_topdir ${PKGDIR}" -v -bb ${PKGDIR}/SPECS/$(PKG).spec
	# cp -R ${PKGDIR}/RPMS/*/* RPMS/

clean:
	cd ${PKGDIR}/SOURCES/ && rm -f *.tar.gz
	rm -fR ${PKGDIR}/BUILD/*
