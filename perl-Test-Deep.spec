#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Test-Deep
Version  : 1.130
Release  : 49
URL      : https://cpan.metacpan.org/authors/id/R/RJ/RJBS/Test-Deep-1.130.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/R/RJ/RJBS/Test-Deep-1.130.tar.gz
Summary  : unknown
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-Test-Deep-perl = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
This module gives you lots of flexibility when testing deep structures.
Install as usual - untar it the

%package dev
Summary: dev components for the perl-Test-Deep package.
Group: Development
Provides: perl-Test-Deep-devel = %{version}-%{release}
Requires: perl-Test-Deep = %{version}-%{release}

%description dev
dev components for the perl-Test-Deep package.


%package perl
Summary: perl components for the perl-Test-Deep package.
Group: Default
Requires: perl-Test-Deep = %{version}-%{release}

%description perl
perl components for the perl-Test-Deep package.


%prep
%setup -q -n Test-Deep-1.130
cd %{_builddir}/Test-Deep-1.130

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
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
/usr/share/man/man3/Test::Deep::NoTest.3

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.34.0/Test/Deep.pm
/usr/lib/perl5/vendor_perl/5.34.0/Test/Deep/All.pm
/usr/lib/perl5/vendor_perl/5.34.0/Test/Deep/Any.pm
/usr/lib/perl5/vendor_perl/5.34.0/Test/Deep/Array.pm
/usr/lib/perl5/vendor_perl/5.34.0/Test/Deep/ArrayEach.pm
/usr/lib/perl5/vendor_perl/5.34.0/Test/Deep/ArrayElementsOnly.pm
/usr/lib/perl5/vendor_perl/5.34.0/Test/Deep/ArrayLength.pm
/usr/lib/perl5/vendor_perl/5.34.0/Test/Deep/ArrayLengthOnly.pm
/usr/lib/perl5/vendor_perl/5.34.0/Test/Deep/Blessed.pm
/usr/lib/perl5/vendor_perl/5.34.0/Test/Deep/Boolean.pm
/usr/lib/perl5/vendor_perl/5.34.0/Test/Deep/Cache.pm
/usr/lib/perl5/vendor_perl/5.34.0/Test/Deep/Cache/Simple.pm
/usr/lib/perl5/vendor_perl/5.34.0/Test/Deep/Class.pm
/usr/lib/perl5/vendor_perl/5.34.0/Test/Deep/Cmp.pm
/usr/lib/perl5/vendor_perl/5.34.0/Test/Deep/Code.pm
/usr/lib/perl5/vendor_perl/5.34.0/Test/Deep/Hash.pm
/usr/lib/perl5/vendor_perl/5.34.0/Test/Deep/HashEach.pm
/usr/lib/perl5/vendor_perl/5.34.0/Test/Deep/HashElements.pm
/usr/lib/perl5/vendor_perl/5.34.0/Test/Deep/HashKeys.pm
/usr/lib/perl5/vendor_perl/5.34.0/Test/Deep/HashKeysOnly.pm
/usr/lib/perl5/vendor_perl/5.34.0/Test/Deep/Ignore.pm
/usr/lib/perl5/vendor_perl/5.34.0/Test/Deep/Isa.pm
/usr/lib/perl5/vendor_perl/5.34.0/Test/Deep/ListMethods.pm
/usr/lib/perl5/vendor_perl/5.34.0/Test/Deep/MM.pm
/usr/lib/perl5/vendor_perl/5.34.0/Test/Deep/Methods.pm
/usr/lib/perl5/vendor_perl/5.34.0/Test/Deep/NoTest.pm
/usr/lib/perl5/vendor_perl/5.34.0/Test/Deep/None.pm
/usr/lib/perl5/vendor_perl/5.34.0/Test/Deep/Number.pm
/usr/lib/perl5/vendor_perl/5.34.0/Test/Deep/Obj.pm
/usr/lib/perl5/vendor_perl/5.34.0/Test/Deep/Ref.pm
/usr/lib/perl5/vendor_perl/5.34.0/Test/Deep/RefType.pm
/usr/lib/perl5/vendor_perl/5.34.0/Test/Deep/Regexp.pm
/usr/lib/perl5/vendor_perl/5.34.0/Test/Deep/RegexpMatches.pm
/usr/lib/perl5/vendor_perl/5.34.0/Test/Deep/RegexpOnly.pm
/usr/lib/perl5/vendor_perl/5.34.0/Test/Deep/RegexpRef.pm
/usr/lib/perl5/vendor_perl/5.34.0/Test/Deep/RegexpRefOnly.pm
/usr/lib/perl5/vendor_perl/5.34.0/Test/Deep/RegexpVersion.pm
/usr/lib/perl5/vendor_perl/5.34.0/Test/Deep/ScalarRef.pm
/usr/lib/perl5/vendor_perl/5.34.0/Test/Deep/ScalarRefOnly.pm
/usr/lib/perl5/vendor_perl/5.34.0/Test/Deep/Set.pm
/usr/lib/perl5/vendor_perl/5.34.0/Test/Deep/Shallow.pm
/usr/lib/perl5/vendor_perl/5.34.0/Test/Deep/Stack.pm
/usr/lib/perl5/vendor_perl/5.34.0/Test/Deep/String.pm
