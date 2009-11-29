%define upstream_name    WWW-Mechanize-TreeBuilder
%define upstream_version 1.10001

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    No summary found
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/WWW/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(HTML::TreeBuilder)
BuildRequires: perl(Moose)
BuildRequires: perl(MooseX::Role::Parameterized)
BuildRequires: perl(Scalar::Util)
BuildRequires: perl(Test::More)
BuildRequires: perl(Test::WWW::Mechanize)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
This module combines the WWW::Mechanize manpage and the HTML::TreeBuilder
manpage. Why? Because I've seen too much code like the following:

 like($mech->content, qr{<p>some text</p>}, "Found the right tag");

Which is just all flavours of wrong - its akin to processing XML with
regexps. Instead, do it like the following:

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%{make}

%check
%{make} test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes
%{_mandir}/man3/*
%perl_vendorlib/*


