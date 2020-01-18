Name:           perl-File-Path
Version:        2.09
Release:        1%{?dist}
Summary:        Create or remove directory trees
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/File-Path/
Source0:        http://www.cpan.org/authors/id/D/DL/DLAND/File-Path-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(strict)
# ExtUtils::MakeMaker::Coverage not needed
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Spec)
# Symbol not used
BuildRequires:  perl(vars)
# Tests:
BuildRequires:  perl(Config)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(Test::More)
%if !%{defined perl_bootstrap}
# Optional tests:
BuildRequires:  perl(Test::Output)
%endif
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       perl(Carp)

%description
This module provides a convenient way to create directories of arbitrary
depth and to delete an entire directory subtree from the file system.

%prep
%setup -q -n File-Path-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README TODO
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Fri Mar 22 2013 Petr Pisar <ppisar@redhat.com> 2.09-1
- Specfile autogenerated by cpanspec 1.78.
