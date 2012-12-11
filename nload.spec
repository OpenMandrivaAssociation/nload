%define	name	nload
%define	version	0.7.4
%define	release 1

Name:		%{name} 
Summary:	Ncurses network traffic and bandwidth monitor
Version:	%{version} 
Release:	%{release} 
Source0:	http://www.roland-riegel.de/nload/%{name}-%{version}.tar.gz
URL:		http://www.roland-riegel.de/nload/index.html?lang=en
Group:		Monitoring
License:	GPL
BuildRequires:	ncurses-devel

%description
nload is a console application which monitors network traffic and 
bandwidth usage in real time. It visualizes the in- and outgoing
traffic using two graphs and provides additional info like total
amount of transfered data and min/max network usage.

%prep
%setup -q

%build
%configure2_5x
%make

%install
%makeinstall_std

%files 
%doc AUTHORS COPYING ChangeLog NEWS README
%{_mandir}/man1/nload*
%{_bindir}/nload



%changelog
* Tue Feb 07 2012 Alexander Khrukin <akhrukin@mandriva.org> 0.7.4-1
+ Revision: 771609
- version update 0.7.4

* Mon Dec 06 2010 Oden Eriksson <oeriksson@mandriva.com> 0.7.2-3mdv2011.0
+ Revision: 613070
- the mass rebuild of 2010.1 packages

* Fri Apr 30 2010 Funda Wang <fwang@mandriva.org> 0.7.2-2mdv2010.1
+ Revision: 541198
- rebuild
- update to new version 0.7.2

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Sun Mar 02 2008 Michael Scherer <misc@mandriva.org> 0.7.1-1mdv2008.1
+ Revision: 177657
- update to new version 0.7.1

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 0.6.0-2mdv2008.1
+ Revision: 130657
- kill re-definition of %%buildroot on Pixel's request
- import nload

