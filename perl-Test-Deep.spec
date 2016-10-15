#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Test-Deep
Version  : 1.123
Release  : 13
URL      : http://search.cpan.org/CPAN/authors/id/R/RJ/RJBS/Test-Deep-1.123.tar.gz
Source0  : http://search.cpan.org/CPAN/authors/id/R/RJ/RJBS/Test-Deep-1.123.tar.gz
Summary  : unknown
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-Test-Deep-doc

%description
This module gives you lots of flexibility when testing deep structres.
Install as usual - untar it the

%package doc
Summary: doc components for the perl-Test-Deep package.
Group: Documentation

%description doc
doc components for the perl-Test-Deep package.


%prep
%setup -q -n Test-Deep-1.123

%build
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make V=1  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot}
else
./Build install --installdirs=site --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/site_perl/5.24.0/Test/Deep.pm
/usr/lib/perl5/site_perl/5.24.0/Test/Deep/All.pm
/usr/lib/perl5/site_perl/5.24.0/Test/Deep/Any.pm
/usr/lib/perl5/site_perl/5.24.0/Test/Deep/Array.pm
/usr/lib/perl5/site_perl/5.24.0/Test/Deep/ArrayEach.pm
/usr/lib/perl5/site_perl/5.24.0/Test/Deep/ArrayElementsOnly.pm
/usr/lib/perl5/site_perl/5.24.0/Test/Deep/ArrayLength.pm
/usr/lib/perl5/site_perl/5.24.0/Test/Deep/ArrayLengthOnly.pm
/usr/lib/perl5/site_perl/5.24.0/Test/Deep/Blessed.pm
/usr/lib/perl5/site_perl/5.24.0/Test/Deep/Boolean.pm
/usr/lib/perl5/site_perl/5.24.0/Test/Deep/Cache.pm
/usr/lib/perl5/site_perl/5.24.0/Test/Deep/Cache/Simple.pm
/usr/lib/perl5/site_perl/5.24.0/Test/Deep/Class.pm
/usr/lib/perl5/site_perl/5.24.0/Test/Deep/Cmp.pm
/usr/lib/perl5/site_perl/5.24.0/Test/Deep/Code.pm
/usr/lib/perl5/site_perl/5.24.0/Test/Deep/Hash.pm
/usr/lib/perl5/site_perl/5.24.0/Test/Deep/HashEach.pm
/usr/lib/perl5/site_perl/5.24.0/Test/Deep/HashElements.pm
/usr/lib/perl5/site_perl/5.24.0/Test/Deep/HashKeys.pm
/usr/lib/perl5/site_perl/5.24.0/Test/Deep/HashKeysOnly.pm
/usr/lib/perl5/site_perl/5.24.0/Test/Deep/Ignore.pm
/usr/lib/perl5/site_perl/5.24.0/Test/Deep/Isa.pm
/usr/lib/perl5/site_perl/5.24.0/Test/Deep/ListMethods.pm
/usr/lib/perl5/site_perl/5.24.0/Test/Deep/MM.pm
/usr/lib/perl5/site_perl/5.24.0/Test/Deep/Methods.pm
/usr/lib/perl5/site_perl/5.24.0/Test/Deep/NoTest.pm
/usr/lib/perl5/site_perl/5.24.0/Test/Deep/None.pm
/usr/lib/perl5/site_perl/5.24.0/Test/Deep/Number.pm
/usr/lib/perl5/site_perl/5.24.0/Test/Deep/Obj.pm
/usr/lib/perl5/site_perl/5.24.0/Test/Deep/Ref.pm
/usr/lib/perl5/site_perl/5.24.0/Test/Deep/RefType.pm
/usr/lib/perl5/site_perl/5.24.0/Test/Deep/Regexp.pm
/usr/lib/perl5/site_perl/5.24.0/Test/Deep/RegexpMatches.pm
/usr/lib/perl5/site_perl/5.24.0/Test/Deep/RegexpOnly.pm
/usr/lib/perl5/site_perl/5.24.0/Test/Deep/RegexpRef.pm
/usr/lib/perl5/site_perl/5.24.0/Test/Deep/RegexpRefOnly.pm
/usr/lib/perl5/site_perl/5.24.0/Test/Deep/RegexpVersion.pm
/usr/lib/perl5/site_perl/5.24.0/Test/Deep/ScalarRef.pm
/usr/lib/perl5/site_perl/5.24.0/Test/Deep/ScalarRefOnly.pm
/usr/lib/perl5/site_perl/5.24.0/Test/Deep/Set.pm
/usr/lib/perl5/site_perl/5.24.0/Test/Deep/Shallow.pm
/usr/lib/perl5/site_perl/5.24.0/Test/Deep/Stack.pm
/usr/lib/perl5/site_perl/5.24.0/Test/Deep/String.pm

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man3/*
