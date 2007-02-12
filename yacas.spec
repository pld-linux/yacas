Summary:	Yacas, a computer algebra language
Summary(pl.UTF-8):   Yacas, język algebry komputerowej
Name:		yacas
Version:	1.0.58
Release:	1
License:	GPL
Group:		Applications/Math
Source0:	http://yacas.sourceforge.net/backups/%{name}-%{version}.tar.gz
# Source0-md5:	fd7fa942789fdac8fa363e555c86cae9
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

%description -l pl.UTF-8
Yacas (Yet Another Computer Algebra System - jeszcze jeden system
algebry komputerowej) jest małym i bardzo elastycznym językiem algebry
komputerowej. Składnia używa parsera gramatyki infix-operator.
Dystrybucja zawiera małą bibliotekę funkcji matematycznych, ale jej
prawdziwa siła leży w języku, w którym możesz łatwo napisać swoje
algorytmy obliczeń na symbolach. Obsługuje arytmetykę o dowolnej
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
