Summary:	Yacas, a computer algebra language
Summary(pl):	Yacas, j�zyk algebry komputerowej
Name:		yacas
Version:	1.0.57
Release:	1
License:	GPL
Group:		Applications/Math
Source0:	http://yacas.sourceforge.net/backups/%{name}-%{version}.tar.gz
# Source0-md5:	0e5161457cb7d818aa8009676998696b
Source1:	%{name}.desktop
URL:		http://yacas.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gsl-devel
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Yacas (Yet Another Computer Algebra System) is a small and highly
flexible computer algebra language. The syntax uses a infix-operator
grammar parser. The distribution contains a small library of
mathematical functions, but its real strength is in the language in
which you can easily write your own symbolic manipulation algorithms.
It supports arbitrary precision arithmetic.

%description -l pl
Yacas (Yet Another Computer Algebra System - jeszcze jeden system
algebry komputerowej) jest ma�ym i bardzo elastycznym j�zykiem algebry
komputerowej. Sk�adnia u�ywa parsera gramatyki infix-operator.
Dystrybucja zawiera ma�� bibliotek� funkcji matematycznych, ale jej
prawdziwa si�a le�y w j�zyku, w kt�rym mo�esz �atwo napisa� swoje
algorytmy oblicze� na symbolach. Obs�uguje arytmetyk� o dowolnej
precyzji.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C src install \
	DESTDIR=$RPM_BUILD_ROOT
%{__make} -C scripts install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

rm -rf manualmaker/{in,*.c,Makefile*,manualmaker,newhelp,styleplain,yacasinit.ys} \
	docs/Makefile*

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS README docs
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
%{_libdir}/lib*.la
%dir %{_libdir}/yacas
%attr(755,root,root) %{_libdir}/yacas/lib*.so*
%{_libdir}/yacas/lib*.la
%{_datadir}/yacas
%{_desktopdir}/*.desktop
