%include	/usr/lib/rpm/macros.php
%define		_class		Net
%define		_subclass	Cyrus
%define		_status		beta
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - an API for the administration of Cyrus IMAP servers
Summary(pl.UTF-8):	%{_pearname} - API do administrowania serwerami Cyrus IMAP
Name:		php-pear-%{_pearname}
Version:	0.3.2
Release:	2
Epoch:		0
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	1fe34ead63b373ce3a073b629d324c57
URL:		http://pear.php.net/package/Net_Cyrus/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear
Requires:	php-pear-Net_IMAP >= 1.0
Requires:	php-pear-Net_Socket >= 1.0
Obsoletes:	php-pear-Net_Cyrus-tests
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
API for the administration of Cyrus IMAP servers. It can be used to
create,delete and modify users and it's properties (Quota and ACL)

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Ta klasa dostarcza API do administrowania serwerami Cyrus IMAP. Może
być użyte do tworzenia, usuwania oraz modyfikowania użytkowników oraz
ich właściwości (Quota oraz ACL).

Ta klasa ma w PEAR status: %{_status}.

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
