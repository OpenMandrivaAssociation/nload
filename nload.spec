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

