%define upstream_name    Module-Metadata
%define upstream_version 1.000004

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	6

Summary:	Gather package and POD information from perl module files
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Module/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(version)
BuildArch:	noarch

%description
The *Tie::CPHash* module provides a hash table that is case preserving but
case insensitive. This means that

    $cphash{KEY}    $cphash{key}
    $cphash{Key}    $cphash{keY}

all refer to the same entry. Also, the hash remembers which form of the key
was last used to store the entry. The 'keys' and 'each' functions will
return the key that was used to set the value.

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
%doc Changes META.yml
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sat Jul 23 2011 Shlomi Fish <shlomif@mandriva.org> 1.0.4-5mdv2012.0
+ Revision: 691279
- Fix the perl-version buildrequires to be 1:0.870. Thanks to proyvind.
- Add a dependency on perl-version. Sigh.
- Fixed the perl(version) to 0.870 instead of 0.87
- Add an explicit version on perl(version)
- import perl-Module-Metadata

