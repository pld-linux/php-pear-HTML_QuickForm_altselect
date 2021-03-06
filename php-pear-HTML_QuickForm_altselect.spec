%define		_status		stable
%define		_pearname	HTML_QuickForm_altselect
Summary:	%{_pearname} - An alternative to HTML_QuickForm_select using radio buttons and checkboxes
Summary(pl.UTF-8):	%{_pearname} - alternatywa dla HTML_QuickForm_select wykorzystująca przyciski radio oraz pola wyboru
Name:		php-pear-%{_pearname}
Version:	1.1.1
Release:	2
License:	LGPL
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	ddcca5ec53e5584b83782fd1d37bac71
URL:		http://pear.php.net/package/HTML_QuickForm_altselect/
BuildRequires:	php-pear-PEAR >= 1:1.4.0-0.b1
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear
Requires:	php-pear-HTML_Common >= 1.2.1
Requires:	php-pear-HTML_QuickForm >= 3.2.5
Obsoletes:	php-pear-HTML_QuickForm_altselect-tests
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A QuickForm plugin that extends the select element and turns its
options into checkboxes or radio buttons depending on whether the
multiple html attribute was set or not. For extra options not listed,
you can also render an 'Other' textfield.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Pakiet ten to wtyczka dla HTML_QuickForm rozszerzająca element select
o pola wyboru lub przyciski radio w zależności od tego, czy atrybut
multiple został ustawiony. Dodatkowe, nie opisane opcje, są dostępne
podczas renderowania pola tekstowego 'Other'.

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
%doc install.log docs/HTML_QuickForm_altselect/docs/examples
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/HTML/QuickForm/altselect.php
