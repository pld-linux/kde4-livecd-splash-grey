
Summary:	PLD-LiveCD KDE4 splash screen grey version
Summary(pl.UTF-8):	Splash do PLD-LiveCD z KDE4 wersja szara
Name:		kde4-livecd-splash-grey
Version:	0
Release:	1
License:	LGPLv3
Group:		X11/Libraries
Source0:	%{name}.tar.gz
# Source0-md5:	9d15e30d3dca6939cf1fc99908923a18
URL:		http://livecd.pld-linux.pl
BuildRequires:	rpmbuild(macros) >= 1.293
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PLD-LiveCD KDE4 splash screen grey version.

%description -l pl.UTF-8
Splash do PLD-LiveCD z KDE4 wersja szara.

%prep
%setup -qc

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/apps/ksplash/Themes
cp -a LiveCDgrey $RPM_BUILD_ROOT%{_datadir}/apps/ksplash/Themes

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/apps/ksplash/Themes/LiveCDgrey
