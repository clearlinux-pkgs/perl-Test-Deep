#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
#
Name     : perl-Test-Deep
Version  : 1.204
Release  : 62
URL      : https://cpan.metacpan.org/authors/id/R/RJ/RJBS/Test-Deep-1.204.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/R/RJ/RJBS/Test-Deep-1.204.tar.gz
Summary  : 'Extremely flexible deep comparison'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Test-Deep-license = %{version}-%{release}
Requires: perl-Test-Deep-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
This archive contains the distribution Test-Deep,
version 1.204:
Extremely flexible deep comparison

%package dev
Summary: dev components for the perl-Test-Deep package.
Group: Development
Provides: perl-Test-Deep-devel = %{version}-%{release}
Requires: perl-Test-Deep = %{version}-%{release}

%description dev
dev components for the perl-Test-Deep package.


%package license
Summary: license components for the perl-Test-Deep package.
Group: Default

%description license
license components for the perl-Test-Deep package.


%package perl
Summary: perl components for the perl-Test-Deep package.
Group: Default
Requires: perl-Test-Deep = %{version}-%{release}

%description perl
perl components for the perl-Test-Deep package.


%prep
%setup -q -n Test-Deep-1.204
cd %{_builddir}/Test-Deep-1.204

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Test-Deep
cp %{_builddir}/Test-Deep-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/perl-Test-Deep/c28bfbeb43b74cc0b97df0c59c4a40fc88400945 || :
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Test::Deep.3
/usr/share/man/man3/Test::Deep::All.3
/usr/share/man/man3/Test::Deep::Any.3
/usr/share/man/man3/Test::Deep::Array.3
/usr/share/man/man3/Test::Deep::ArrayEach.3
/usr/share/man/man3/Test::Deep::ArrayElementsOnly.3
/usr/share/man/man3/Test::Deep::ArrayLength.3
/usr/share/man/man3/Test::Deep::ArrayLengthOnly.3
/usr/share/man/man3/Test::Deep::Blessed.3
/usr/share/man/man3/Test::Deep::Boolean.3
/usr/share/man/man3/Test::Deep::Cache.3
/usr/share/man/man3/Test::Deep::Cache::Simple.3
/usr/share/man/man3/Test::Deep::Class.3
/usr/share/man/man3/Test::Deep::Cmp.3
/usr/share/man/man3/Test::Deep::Code.3
/usr/share/man/man3/Test::Deep::Hash.3
/usr/share/man/man3/Test::Deep::HashEach.3
/usr/share/man/man3/Test::Deep::HashElements.3
/usr/share/man/man3/Test::Deep::HashKeys.3
/usr/share/man/man3/Test::Deep::HashKeysOnly.3
/usr/share/man/man3/Test::Deep::Ignore.3
/usr/share/man/man3/Test::Deep::Isa.3
/usr/share/man/man3/Test::Deep::ListMethods.3
/usr/share/man/man3/Test::Deep::MM.3
/usr/share/man/man3/Test::Deep::Methods.3
/usr/share/man/man3/Test::Deep::NoTest.3
/usr/share/man/man3/Test::Deep::None.3
/usr/share/man/man3/Test::Deep::Number.3
/usr/share/man/man3/Test::Deep::Obj.3
/usr/share/man/man3/Test::Deep::Ref.3
/usr/share/man/man3/Test::Deep::RefType.3
/usr/share/man/man3/Test::Deep::Regexp.3
/usr/share/man/man3/Test::Deep::RegexpMatches.3
/usr/share/man/man3/Test::Deep::RegexpOnly.3
/usr/share/man/man3/Test::Deep::RegexpRef.3
/usr/share/man/man3/Test::Deep::RegexpRefOnly.3
/usr/share/man/man3/Test::Deep::RegexpVersion.3
/usr/share/man/man3/Test::Deep::ScalarRef.3
/usr/share/man/man3/Test::Deep::ScalarRefOnly.3
/usr/share/man/man3/Test::Deep::Set.3
/usr/share/man/man3/Test::Deep::Shallow.3
/usr/share/man/man3/Test::Deep::Stack.3
/usr/share/man/man3/Test::Deep::String.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Test-Deep/c28bfbeb43b74cc0b97df0c59c4a40fc88400945

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
