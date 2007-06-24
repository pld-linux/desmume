Summary:	Nintendo DS emulator
Summary(pl.UTF-8):	Emulator Nintendo DS
Name:		desmume
Version:	0.6.0
Release:	1
License:	GPL v2+
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/desmume/%{name}-%{version}.tar.gz
# Source0-md5:	48f192b8839affc03b2b28e5eb509984
URL:		http://desmume.org/
BuildRequires:	SDL-devel
BuildRequires:	gtk+2-devel >= 1:2.0
BuildRequires:	libglade2-devel >= 2.0
BuildRequires:	pkgconfig
BuildRequires:	zlib-devel
BuildRequires:	zziplib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DeSmuME is a Nintendo DS emulator running demos and commercial games.

%description -l pl.UTF-8
DeSmuME jest emulatorem Nintendo DS, który uruchamia również wersje
demonstracyjne i gry komercyjne.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/*
