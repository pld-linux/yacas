Summary:	Yacas, a computer algebra language
Summary(pl):	Yacas, jêzyk algebry komputerowej
Name:		yacas
Version:	1.0.47
Release:	3
License:	GPL
Group:		Applications/Math
Source0:	http://www.xs4all.nl/~apinkus/%{name}-%{version}.tar.gz
Patch0:		%{name}-automake.patch
Patch1:		%{name}-gmp.patch
URL:		http://www.xs4all.nl/~apinkus/yacas.html 
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gmp-devel
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
%patch1 -p1

%build
rm -rf missing
aclocal
autoconf
automake -a -c
%configure \
	--enable-gmp
%{__make} 

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C src install DESTDIR=$RPM_BUILD_ROOT
%{__make} -C scripts install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf AUTHORS README

rm -rf manualmaker/{in,*.c,Makefile*,manualmaker,newhelp,styleplain,yacasinit.ys} \
	docs/Makefile*
 
%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz manualmaker docs
%attr(755,root,root) %{_bindir}/*
%{_datadir}/yacas
