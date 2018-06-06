Name:       jsoncpp
Version:    %{VERSION}
Release:    1
Summary:    JSON library implemented in C++
Group:      System Environment/Libraries
License:    Public Domain or MIT
URL:        https://github.com/open-source-parsers/jsoncpp
Source0:    jsoncpp-%{version}.tar.gz

BuildRequires:  python doxygen cmake3
BuildRequires:  graphviz
Provides:	libjsoncpp.so.0()(64bit)

%description
%{name} is an implementation of a JSON (http://json.org) reader and writer in
C++. JSON (JavaScript Object Notation) is a lightweight data-interchange format.
It is easy for humans to read and write. It is easy for machines to parse and
generate.

%package devel
Summary:    Development headers and library for %{name}
Group:      Development/Libraries
Requires:   %{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains the development headers and library for %{name}.

%package doc
Summary:    Documentation for %{name}
Group:      Documentation
BuildArch:  noarch

%description doc
This package contains the documentation for %{name}

%prep
%setup -qn %{name}-%{version}

%build
cmake3 . -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=/usr -DBUILD_STATIC_LIBS=OFF -DBUILD_SHARED_LIBS=ON -DCMAKE_INSTALL_INCLUDEDIR=include/jsoncpp
make %{?_smp_mflags}
python doxybuild.py --doxygen=$(which doxygen) --open --with-dot

%check

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_docdir}/%{name}/html
install -p -m 0644 dist/doxygen/*/*.{html,png} $RPM_BUILD_ROOT%{_docdir}/%{name}/html

%post
ldconfig

%postun
ldconfig

%files
%defattr(-,root,root,-)
%doc LICENSE README.md
%{_libdir}/lib%{name}.so.*

%files devel
%defattr(-,root,root,-)
%{_libdir}/lib%{name}.so
%{_includedir}/%{name}/
%{_libdir}/pkgconfig/jsoncpp.pc

%files doc
%defattr(-,root,root,-)
%{_docdir}/%{name}/

%changelog
* Fri Mar 27 2015 Matthew Miller <mattdm@fedoraproject.org> - 0.10.0-1
- update to 0.10.0 released version
- upstream notes "Based on 1.6.0. Binary-compatible with the old 0.6.0-rc2 from sourceforge."

* Sat Feb 21 2015 Matthew Miller <mattdm@fedoraproject.org>
- update to 0.8.3 released version

* Wed Sep 17 2014 Matthew Miller <mattdm@fedoraproject.org>
- update to df26dae40ffecb8596dfef04fc73b7a8175ea05b snapshot (to fix Minetest!)

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-0.13.rc2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-0.12.rc2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Sep 10 2013 Sébastien Willmann <sebastien.willmann@gmail.com> - 0.6.0-0.11.rc2
- https://bugzilla.redhat.com/show_bug.cgi?id=998149 : applied Michael Schwendt's
  patch to fix duplicated documentation

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-0.10.rc2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Mar 15 2013 Sébastien Willmann <sebastien.willmann@gmail.com> - 0.6.0-0.9.rc2
- Changed Summary
- Added %%doc files to the doc package
- Added python as an explicit BuildRequires

* Fri Feb 15 2013 Sebastien Willmann <sebastien.willmann@gmail.com> - 0.6.0-0.8.rc2
- Added documentation sub-package

* Sun Jan 20 2013 Sebastien Willmann <sebastien.willmann@gmail.com> - 0.6.0-0.7.rc2
- Added graphviz as a BuildRequire

* Sat Jan 19 2013 Sebastien Willmann <sebastien.willmann@gmail.com> - 0.6.0-0.6.rc2
- Install the corrected library

* Sat Dec 22 2012 Sebastien Willmann <sebastien.willmann@gmail.com> - 0.6.0-0.5.rc2
- Added libjsoncpp.so.0
- Moved the shared lib build to the correct section

* Fri Dec 21 2012 Sebastien Willmann <sebastien.willmann@gmail.com> - 0.6.0-0.4.rc2
- Removed doc subpackage
- Added .pc file
- Fixed shared lib

* Wed Dec 12 2012 Sebastien Willmann <sebastien.willmann@gmail.com> - 0.6.0-0.3.rc2
- Removed static package
- Preserving timestamp on installed files
- Added guard grep to the sed expression
- Removed duplicated doc files
- Removed dependency on pkgconfig
- Changed base package group

* Sun Dec 02 2012 Sébastien Willmann <sebastien.willmann@gmail.com> - 0.6.0-0.2.rc2
- Changed license field to Public Domain or MIT

* Tue Nov 27 2012 Sébastien Willmann <sebastien.willmann@gmail.com> 0.6.0-0.1.rc2
- Creation of the spec file

