%include	/usr/lib/rpm/macros.php
%define		_class		Net
%define		_subclass	Cyrus
%define		_status		beta
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - an API for the administration of Cyrus IMAP servers
Summary(pl):	%{_pearname} - API do administrowania serwerami Cyrus IMAP
Name:		php-pear-%{_pearname}
Version:	0.3.1
Release:	3
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	7deb75ce29b9acdbb4fb34c5ba9b5384
URL:		http://pear.php.net/package/Net_Cyrus/
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-pear
Requires:	php-pear-Net_Socket >= 1.0
Requires:	php-pear-Net_IMAP >= 1.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
API for the administration of Cyrus IMAP servers. It can be used to
create,delete and modify users and it's properties (Quota and ACL)

In PEAR status of this package is: %{_status}.

%description -l pl
Ta klasa dostarcza API do administrowania serwerami Cyrus IMAP. Mo�e
by� u�yte do tworzenia, usuwania oraz modyfikowania u�ytkownik�w oraz
ich w�a�ciwo�ci (Quota oraz ACL).

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl):	Testy dla PEAR::%{_pearname}
Group:		Development
Requires:	%{name} = %{epoch}:%{version}-%{release}
AutoReq:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl
Testy dla PEAR::%{_pearname}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/*.php

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/*
