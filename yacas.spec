Summary:	Yacas, a computer algebra language
Summary(pl):	Yacas, jêzyk algebry komputerowej
Name:		yacas
Version:	1.0.54
Release:	1
License:	GPL
Group:		Applications/Math
Source0:	http://yacas.sourceforge.net/backups/%{name}-%{version}.tar.gz
# Source0-md5:	282e705b3a7466d31dc7ee6a76158d21
Source1:	%{name}.desktop
Patch0:		%{name}-DESTDIR.patch
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
algebry komputerowej) jest ma³ym i bardzo elastycznym jêzykiem algebry
komputerowej. Sk³adnia u¿ywa parsera gramatyki infix-operator.
Dystrybucja zawiera ma³± bibliotekê funkcji matematycznych, ale jej
prawdziwa si³a le¿y w jêzyku, w którym mo¿esz ³atwo napisaæ swoje
algorytmy obliczeñ na symbolach. Obs³uguje arytmetykê o dowolnej
precyzji.

%prep
%setup -q
%patch0 -p1

%build
rm -rf missing
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C src install DESTDIR=$RPM_BUILD_ROOT
%{__make} -C scripts install DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_applnkdir}/Scientific/Mathematics
install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Scientific/Mathematics/%{name}.desktop

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
%attr(755,root,root) %{_libdir}/lib*.so.*
%{_libdir}/lib*.la
%{_datadir}/yacas
%{_applnkdir}/Scientific/Mathematics/*
