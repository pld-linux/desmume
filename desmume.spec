Summary:	Nintendo DS emulator
Summary(pl.UTF-8):	Emulator Nintendo DS
Name:		desmume
Version:	0.9.2
Release:	1
License:	GPL v2+
Group:		Applications/Emulators
Source0:	http://dl.sourceforge.net/desmume/%{name}-%{version}.tar.gz
# Source0-md5:	51482de785dce04590532b946321196d
Patch0:		%{name}-desktop.patch
URL:		http://desmume.org/
BuildRequires:	SDL-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+2-devel >= 1:2.0
BuildRequires:	gtkglext-devel
BuildRequires:	libglade2-devel >= 2.0
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.197
BuildRequires:	zlib-devel
BuildRequires:	zziplib-devel >= 0.13.49
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DeSmuME is a Nintendo DS emulator running demos and commercial games.

%description -l pl.UTF-8
DeSmuME jest emulatorem Nintendo DS, który uruchamia również wersje
demonstracyjne i gry komercyjne.

%prep
%setup -q
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/%{name}.desktop
%{_mandir}/man1/desmume*.1*
%{_pixmapsdir}/DeSmuME.xpm
