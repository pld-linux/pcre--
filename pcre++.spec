Summary:	C++ wrapper around the PCRE library
Summary(pl):	Nak�adka na bibliotek� PCRE dla C++
Name:		pcre++
Version:	0.9.5
Release:	2
License:	LGPL
Group:		Libraries
Source0:	ftp://ftp.daemon.de/scip/Apps/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	1fe6ea8e23ece01fde2ce5fb4746acc2
Patch0:		%{name}-DESTDIR.patch
URL:		http://www.daemon.de/PCRE
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	pcre-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PCRE++ is a C++ wrapper-class for PCRE library (Perl Compatible
Regular Expressions). It allows you to use Perl-alike regular
expressions in your C++ applications. You can use it to search in
strings, to split strings into parts using expressions, or to search
and replace a part of a string with another part.

%description -l pl
PCRE++ jest klas�-nak�adk� dla C++ na bibliotek� PCRE (Perl Compatible
Regular Expressions - perlowych wyra�e� regularnych). Pozwala na
korzystanie ze sk�adni perlowych wyra�e� regularnych w aplikacjach
C++. Mo�na przeszukiwa� w tekstach, dzieli� tekst korzystaj�c z
r�nych wyra�e� lub wyszukiwa� i zamienia� fragmenty tekstu innymi
cz�ciami.

%package devel
Summary:	Header files for pcre++ library
Summary(pl):	Pliki nag��wkowe biblioteki pcre++
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libstdc++-devel
Requires:	pcre-devel

%description devel
Header files for pcre++ library.

%description devel -l pl
Pliki nag��wkowe biblioteki pcre++.

%package static
Summary:	Static pcre++ library
Summary(pl):	Statyczna biblioteka pcre++
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static pcre++ library.

%description static -l pl
Statyczna biblioteka pcre++.

%prep
%setup -q
%patch0

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make} \
	CXXFLAGS="%{rpmcflags} -Wall"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -rf lib%{name}-%{version}
mv $RPM_BUILD_ROOT%{_prefix}/doc/lib%{name}-%{version} .

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%doc lib%{name}-%{version}/*
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/%{name}.h
%{_mandir}/man3/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
