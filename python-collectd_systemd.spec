# Created by pyp2rpm-3.3.0
%global pypi_name collectd_systemd

%global commit a7018ec32245abc2828a9bcd4cd0d216fde8a021
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global snapinfo 20180516git%{shortcommit}

Name:           python-%{pypi_name}
Version:        0.0.1
Release:        0.2.%{snapinfo}%{?dist}.3
Summary:        Collectd plugin to monitor systemd services

License:        MIT
URL:            https://github.com/mbachry/collectd-systemd/
Source0:        https://github.com/mbachry/collectd-systemd/archive/%{commit}/collectd-system-%{shortcommit}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
BuildRequires:  pytest
BuildRequires:  python2-mock

 
%description
collectd-systemd A collectd plugin which checks if given systemd services
are in "running" state and sends metrics with 1.0 or 0.0.
%package -n     python2-%{pypi_name}
Summary:        %{summary}
Requires:       dbus-python
Requires:       collectd-python

%description -n python2-%{pypi_name}
collectd-systemd A collectd plugin which checks if given systemd services
are in "running" state and sends metrics with 1.0 or 0.0.

%prep
%autosetup -n collectd-systemd-%{commit}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py2_build

%install
# Must do the default python version install last because
# the scripts in /usr/bin are overwritten with every setup.py install.
%py2_install

%files -n python2-%{pypi_name}
%doc README.rst
%license LICENSE
%{python2_sitelib}/%{pypi_name}.py*
%{python2_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%check
PYTHONPATH=. py.test

%changelog
* Thu May 17 2018 Steve Traylen <steve.traylen@cern.ch> - 0.0.1-0.2.20180516gita7018ec 3
- Correct python-dbus package name for el7.

* Thu May 17 2018 Steve Traylen <steve.traylen@cern.ch> - 0.0.1-0.2.20180516gita7018ec 2
- Use new build of pytest.

* Thu May 17 2018 Steve Traylen <steve.traylen@cern.ch> - 0.0.1-0.2.20180516gita7018ec 1
- Backport to el7.

* Thu May 17 2018 Steve Traylen <steve.traylen@cern.ch> - 0.0.1-0.2.20180516gita7018ec
- Correct snapshot in string.

* Wed May 16 2018 Steve Traylen <steve.traylen@cern.ch> - 0.0.1-0.1.20180516gita7018ec
- Initial package.
