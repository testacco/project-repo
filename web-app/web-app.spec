%define PYTHON /usr/bin/python
%define pkgname pika

Name:          python-pika
Summary:       Pika Python AMQP Client Library
Version:       0.11.0
Release:       1%{?dist}
License:       BSD
Group:         System Environment/Libraries
Vendor:        python.org
URL:           https://pika.readthedocs.org
Source:        https://pypi.python.org/packages/26/10/0493cb0579b34e453fcd9c56fbf4504a5e4a9d9c8db80cece3fbc92e06d2/%{pkgname}-%{version}.tar.gz

BuildRequires: python >= 2.7
Requires:      python >= 2.7

BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:     noarch

%description
Simple web-app

%prep
%setup -q -c -n %{name}-%{version}.%{release}

%build
cd %{pkgname}-%{version}
%{PYTHON} setup.py build

%install
cd %{pkgname}-%{version}
%{__rm} -rf %{buildroot}
%{PYTHON} setup.py install --root=$RPM_BUILD_ROOT

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root)
/usr/lib/python2.7/site-packages/

%changelog
* Mon Mar 26 2018 Mariia Tartachna <mtartachna@gmail.com>
- Initial spec
