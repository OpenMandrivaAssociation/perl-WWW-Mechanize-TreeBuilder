%define upstream_name    WWW-Mechanize-TreeBuilder
%define upstream_version 1.10003

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	Combine WWW::Mechanize and HTML::TreeBuilder
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/WWW/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(HTML::TreeBuilder)
BuildRequires:	perl(Moose)
BuildRequires:	perl(MooseX::Role::Parameterized)
BuildRequires:	perl(Scalar::Util)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Test::WWW::Mechanize)

BuildArch:	noarch
Requires:	perl(HTML::TreeBuilder)

%description
This module combines the WWW::Mechanize manpage and the HTML::TreeBuilder
manpage. Why? Because I've seen too much code like the following:

 like($mech->content, qr{<p>some text</p>}, "Found the right tag");

Which is just all flavours of wrong - its akin to processing XML with
regexps.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 1.100.30-2mdv2011.0
+ Revision: 656978
- rebuild for updated spec-helper

* Fri Nov 12 2010 Jérôme Quelin <jquelin@mandriva.org> 1.100.30-1mdv2011.0
+ Revision: 596702
- update to 1.10003

* Sun Apr 18 2010 Jérôme Quelin <jquelin@mandriva.org> 1.100.20-1mdv2011.0
+ Revision: 536217
- update to 1.10002

* Mon Nov 30 2009 Jérôme Quelin <jquelin@mandriva.org> 1.100.10-2mdv2010.1
+ Revision: 472011
- adding missing requires:

* Sun Nov 29 2009 Jérôme Quelin <jquelin@mandriva.org> 1.100.10-1mdv2010.1
+ Revision: 471164
- import perl-WWW-Mechanize-TreeBuilder


* Sun Nov 29 2009 cpan2dist 1.10001-1mdv
- initial mdv release, generated with cpan2dist
