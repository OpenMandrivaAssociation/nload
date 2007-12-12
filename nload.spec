%define	name	nload
%define	version	0.6.0
%define	release %mkrel 2 

Name:		%{name} 
Summary:	Ncurses network traffic and bandwidth monitor
Version:	%{version} 
Release:	%{release} 
Source:	http://prdownloads.sourceforge.net/nload/%{name}-%{version}.tar.bz2
URL:		http://www.roland-riegel.de/nload/index.html?lang=en
Group:		Monitoring
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
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
%configure
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%clean 
rm -rf $RPM_BUILD_ROOT 

%files 
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog NEWS README
%{_mandir}/man1/nload*
%{_bindir}/nload

