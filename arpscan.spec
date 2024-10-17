Summary:	Very simple ARP scanner
Name:           arpscan
Version:        0.10
Release:        3
License:	GPLv2
Group:		Networking/Other
URL:		https://wizard.ae.krakow.pl/~jb/arpscan/
Source0:	http://wizard.ae.krakow.pl/~jb/arpscan/%{name}-%{version}.tar.gz
Source1:	http://standards.ieee.org/regauth/oui/oui.txt.bz2
BuildRequires:	gawk
BuildRoot:      %{_tmppath}/%{name}-%{version}-root

%description
Arpscan is a utility that scans local network using ARP protocol
and reports alive hosts. Program is designed for Linux.

%prep
%setup -q
bzcat %{SOURCE1} > oui.txt

%build
%make \
    CC=%{__cc} \
    CFLAGS="%{optflags} -DVER=\$(VERSION) -DOUI=\$(OUI)" \
    OUI=%{_datadir}/%{name}/oui
gawk -f oui.awk oui.txt > oui

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}
install -d %{buildroot}%{_sbindir}
install -d %{buildroot}%{_datadir}/%{name}/
install -m0755 %{name} %{buildroot}%{_sbindir}/%{name}
install -m0644 oui %{buildroot}%{_datadir}/%{name}/oui

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(-,root,root)
%attr(0755,root,root) %{_sbindir}/*
%{_datadir}/%{name}


%changelog
* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 0.10-2mdv2011.0
+ Revision: 609993
- rebuild

* Tue Feb 23 2010 Sandro Cazzaniga <kharec@mandriva.org> 0.10-1mdv2010.1
+ Revision: 510105
- New release 0.10

* Tue Jun 16 2009 Jérôme Brenier <incubusss@mandriva.org> 0.9-1mdv2010.0
+ Revision: 386369
- update to new version 0.9
- fix license tag

* Thu Jun 19 2008 Thierry Vignaud <tv@mandriva.org> 0.8-3mdv2009.0
+ Revision: 226173
- rebuild

* Thu Dec 20 2007 Olivier Blin <oblin@mandriva.com> 0.8-2mdv2008.1
+ Revision: 135823
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sun Sep 09 2007 Oden Eriksson <oeriksson@mandriva.com> 0.8-2mdv2008.0
+ Revision: 83861
- rebuild


* Fri Dec 22 2006 Oden Eriksson <oeriksson@mandriva.com> 0.8-1mdv2007.0
+ Revision: 101569
- Import arpscan

* Fri Feb 03 2006 Oden Eriksson <oeriksson@mandriva.com> 0.8-1mdk
- 0.8

* Sat Jan 08 2005 Oden Eriksson <oeriksson@mandrakesoft.com> 0.5-1mdk
- initial pld import

