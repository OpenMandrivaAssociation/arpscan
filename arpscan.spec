Summary:	Very simple ARP scanner
Name:           arpscan
Version:        0.10
Release:        %mkrel 2
License:	GPLv2
Group:		Networking/Other
URL:		http://wizard.ae.krakow.pl/~jb/arpscan/
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
