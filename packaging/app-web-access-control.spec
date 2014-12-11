
Name: app-web-access-control
Epoch: 1
Version: 2.0.5
Release: 1%{dist}
Summary: Web Access Control
License: GPLv3
Group: ClearOS/Apps
Source: %{name}-%{version}.tar.gz
Buildarch: noarch
Requires: %{name}-core = 1:%{version}-%{release}
Requires: app-base
Requires: app-web-proxy

%description
Web Access Control allows an administrator to enforce time-of-day web access to groups or computers (IP or MAC address) using the web proxy.

%package core
Summary: Web Access Control - Core
License: LGPLv3
Group: ClearOS/Libraries
Requires: app-base-core
Requires: app-web-proxy-core
Requires: app-accounts

%description core
Web Access Control allows an administrator to enforce time-of-day web access to groups or computers (IP or MAC address) using the web proxy.

This package provides the core API and libraries.

%prep
%setup -q
%build

%install
mkdir -p -m 755 %{buildroot}/usr/clearos/apps/web_access_control
cp -r * %{buildroot}/usr/clearos/apps/web_access_control/


%post
logger -p local6.notice -t installer 'app-web-access-control - installing'

%post core
logger -p local6.notice -t installer 'app-web-access-control-core - installing'

if [ $1 -eq 1 ]; then
    [ -x /usr/clearos/apps/web_access_control/deploy/install ] && /usr/clearos/apps/web_access_control/deploy/install
fi

[ -x /usr/clearos/apps/web_access_control/deploy/upgrade ] && /usr/clearos/apps/web_access_control/deploy/upgrade

exit 0

%preun
if [ $1 -eq 0 ]; then
    logger -p local6.notice -t installer 'app-web-access-control - uninstalling'
fi

%preun core
if [ $1 -eq 0 ]; then
    logger -p local6.notice -t installer 'app-web-access-control-core - uninstalling'
    [ -x /usr/clearos/apps/web_access_control/deploy/uninstall ] && /usr/clearos/apps/web_access_control/deploy/uninstall
fi

exit 0

%files
%defattr(-,root,root)
/usr/clearos/apps/web_access_control/controllers
/usr/clearos/apps/web_access_control/htdocs
/usr/clearos/apps/web_access_control/views

%files core
%defattr(-,root,root)
%exclude /usr/clearos/apps/web_access_control/packaging
%dir /usr/clearos/apps/web_access_control
/usr/clearos/apps/web_access_control/deploy
/usr/clearos/apps/web_access_control/language
