%define name yacas
%define version 1.0.19
%define release 2mdk

Name: %{name}
Summary: Yacas, a computer algebra language
Version: %{version}
Release: %{release}
Source: %{name}-%{version}.tar.bz2
Group: Development/Other
URL: http://www.xs4all.nl/~apinkus/yacas.html 
BuildRoot: /var/tmp/%{name}-buildroot
Copyright: Freeware
Prefix: /usr

%description
Yacas (Yet Another Computer Algebra System) is a small and highly
flexible computer algebra language. The syntax uses a infix-operator
grammar parser. The distribution contains a small library of
mathematical functions, but its real strength is in the language in
which you can easily write your own symbolic manipulation algorithms.
It supports arbitrary precision arithmetic.

%prep
rm -rf $RPM_BUILD_ROOT

%setup -q

%build
#CFLAGS="$RPM_OPT_FLAGS" CXXFLAGS="$RPM_OPT_FLAGS"
 ./configure \	--prefix=%{prefix}
make 
#-j 2

%install
make install prefix=$RPM_BUILD_ROOT/%{prefix}
install -m 755 -d $RPM_BUILD_ROOT/usr/doc/%{name}-%{version}
install -m 644 docs/* $RPM_BUILD_ROOT/usr/doc/%{name}-%{version}

cd $RPM_BUILD_ROOT

find . -type d | sed -e '1,2d;s,^\.,\%attr(-\,root\,root) \%dir ,' > \
    $RPM_BUILD_DIR/file.list.%{name}

find . -type f | sed -e 's,^\.,\%attr(-\,root\,root) ,' \
       -e '/\/etc\//s|^|%config|' \
       -e '/\/config\//s|^|%config|' \
	   -e '/\/doc\//s|^|%doc|' \
       >> $RPM_BUILD_DIR/file.list.%{name}

find . -type l | sed -e 's,^\.,\%attr(-\,root\,root) ,' >> \
    $RPM_BUILD_DIR/file.list.%{name}


%clean
rm -rf $RPM_BUILD_ROOT $RPM_BUILD_DIR/file.list.%{name}

%files -f ../file.list.%{name}
%defattr(-,root,root,0755)

%changelog
* Thu May 04 2000 Lenny Cartier <lenny@mandrakesoft.com> 1.0.19-2mdk
- fix group

* Thu Dec 02 1999 Lenny Cartier <lenny@mandrakesoft.com>
- New in contribs
- specfile adaptations
- added docs
