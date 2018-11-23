#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Socket-MsgHdr
Version  : 0.04
Release  : 3
URL      : https://cpan.metacpan.org/authors/id/M/MJ/MJP/Socket-MsgHdr-0.04.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/M/MJ/MJP/Socket-MsgHdr-0.04.tar.gz
Summary  : sendmsg, recvmsg and ancillary data operations
Group    : Development/Tools
License  : Artistic-1.0-Perl GPL-1.0+
Requires: perl-Socket-MsgHdr-lib = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
Socket/MsgHdr version 0.02
==========================
Advanced socket messaging operations:  sendmsg, recvmsg and cmsghdr
manipulation.  Available as plain functions or IO::Socket methods.

%package dev
Summary: dev components for the perl-Socket-MsgHdr package.
Group: Development
Requires: perl-Socket-MsgHdr-lib = %{version}-%{release}
Provides: perl-Socket-MsgHdr-devel = %{version}-%{release}

%description dev
dev components for the perl-Socket-MsgHdr package.


%package lib
Summary: lib components for the perl-Socket-MsgHdr package.
Group: Libraries

%description lib
lib components for the perl-Socket-MsgHdr package.


%prep
%setup -q -n Socket-MsgHdr-0.04

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
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
/usr/lib/perl5/vendor_perl/5.28.0/x86_64-linux-thread-multi/Socket/MsgHdr.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Socket::MsgHdr.3

%files lib
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.0/x86_64-linux-thread-multi/auto/Socket/MsgHdr/MsgHdr.so
