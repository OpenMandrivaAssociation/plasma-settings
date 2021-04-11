#define snapshot 20200901
#define commit 08fa0c465ba93f6621529897bfaa844f0f58b066

Name:		plasma-settings
Version:	0.1
Release:	%{?snapshot:0.%{snapshot}.}1
Summary:	Settings application for Plasma Mobile
%if 0%{?snapshot}
Source0:	https://invent.kde.org/plasma-mobile/plasma-settings/-/archive/master/plasma-settings-master.tar.bz2
%else
Source0:	https://invent.kde.org/plasma-mobile/plasma-settings/-/archive/v%{version}/plasma-settings-v%{version}.tar.bz2
%endif
License:	GPLv3
Group:		Applications/Productivity
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	cmake(Qt5Gui)
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(Qt5Quick)
BuildRequires:	cmake(Qt5Test)
BuildRequires:	cmake(KF5WindowSystem)
BuildRequires:	cmake(KF5CoreAddons)
BuildRequires:	cmake(KF5Solid)
BuildRequires:	cmake(KF5Config)
BuildRequires:	cmake(KF5Auth)
BuildRequires:	cmake(KF5DBusAddons)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5Plasma)
BuildRequires:	cmake(KF5PlasmaQuick)
BuildRequires:	cmake(KF5Declarative)
BuildRequires:	cmake(KF5KIO)
BuildRequires:	cmake(KF5KDELibs4Support)

%description
Settings application for Plasma Mobile

%prep
%if 0%{?snapshot}
%autosetup -p1 -n plasma-settings-master
%else
%autosetup -p1 -n plasma-settings-v%{version}
%endif
%cmake_kde5 -G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%files
%{_bindir}/plasma-settings
%{_libdir}/qt5/plugins/kcms/kcm_mobile_cellularnetwork.so
%{_libdir}/qt5/plugins/kcms/kcm_mobile_info.so
%{_libdir}/qt5/plugins/kcms/kcm_mobile_theme.so
%{_libdir}/qt5/plugins/kcms/kcm_mobile_time.so
%{_libdir}/qt5/plugins/kcms/kcm_mobile_virtualkeyboard.so
%{_libdir}/qt5/plugins/kcms/kcm_password.so
%{_datadir}/applications/org.kde.mobile.plasmasettings.desktop
%{_datadir}/kpackage/genericqml/org.kde.plasma.settings
%{_datadir}/kpackage/kcms/kcm_mobile_cellularnetwork
%{_datadir}/kpackage/kcms/kcm_mobile_info
%{_datadir}/kpackage/kcms/kcm_mobile_theme
%{_datadir}/kpackage/kcms/kcm_mobile_time
%{_datadir}/kservices5/cellularnetwork.desktop
%{_datadir}/kservices5/info.desktop
%{_datadir}/kservices5/kcm_mobile_virtualkeyboard.desktop
%{_datadir}/kservices5/kcm_password.desktop
%{_datadir}/kservices5/themesettings.desktop
%{_datadir}/kservices5/timesettings.desktop
%{_datadir}/kpackage/kcms/kcm_mobile_virtualkeyboard
%{_datadir}/kpackage/kcms/kcm_password

