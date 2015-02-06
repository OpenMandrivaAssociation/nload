Summary:	Ncurses network traffic and bandwidth monitor
Name:		nload
Version:	0.7.4
Release:	3
License:	GPLv2+
Group:		Monitoring
Url:		http://www.roland-riegel.de/nload/index.html?lang=en
Source0:	http://www.roland-riegel.de/nload/%{name}-%{version}.tar.gz
BuildRequires:	ncurses-devel

%description
nload is a console application which monitors network traffic and bandwidth
usage in real time. It visualizes the in- and outgoing traffic using two
graphs and provides additional info like total amount of transfered data and
min/max network usage.

%files
%doc AUTHORS COPYING ChangeLog NEWS README
%{_mandir}/man1/nload*
%{_bindir}/nload

#----------------------------------------------------------------------------

%prep
%setup -q

%build
%configure2_5x --enable-debug
%make

%install
%makeinstall_std

