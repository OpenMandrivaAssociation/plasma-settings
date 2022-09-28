#define snapshot 20200901
#define commit 08fa0c465ba93f6621529897bfaa844f0f58b066

Name:		plasma-settings
Version:	22.09
Release:	%{?snapshot:1.%{snapshot}.}2
Summary:	Settings application for Plasma Mobile
%if 0%{?snapshot}
Source0:	https://invent.kde.org/plasma-mobile/plasma-settings/-/archive/master/plasma-settings-master.tar.bz2
%else
Source0:	https://download.kde.org/stable/plasma-mobile/%{version}/%{name}-%{version}.tar.xz
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
BuildRequires:	cmake(KF5ModemManagerQt)
BuildRequires:	cmake(KF5NetworkManagerQt)
BuildRequires:	pkgconfig(gobject-2.0)

%description
Settings application for Plasma Mobile

%prep
%if 0%{?snapshot}
%autosetup -p1 -n plasma-settings-master
%else
%autosetup -p1
%endif
%cmake_kde5 -G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build
%find_lang kcm_cellular_network
%find_lang kcm_mobile_info
%find_lang kcm_mobile_powermanagement
%find_lang kcm_mobile_time
%find_lang kcm_mobile_virtualkeyboard
%find_lang kcm_password
%find_lang mobile.plasmasettings

%files -f kcm_cellular_network.lang -f kcm_mobile_info.lang -f kcm_mobile_powermanagement.lang -f kcm_mobile_time.lang -f kcm_mobile_virtualkeyboard.lang -f kcm_password.lang -f mobile.plasmasettings.lang
%{_bindir}/plasma-settings
%{_libdir}/qt5/plugins/kcms/kcm_mobile_info.so
%{_libdir}/qt5/plugins/kcms/kcm_mobile_time.so
%{_libdir}/qt5/plugins/kcms/kcm_password.so
%{_libdir}/qt5/plugins/kcms/kcm_mobile_onscreenkeyboard.so
%{_datadir}/applications/org.kde.mobile.plasmasettings.desktop
%{_datadir}/kpackage/kcms/kcm_mobile_info
%{_datadir}/kpackage/kcms/kcm_mobile_time
%{_datadir}/kpackage/kcms/kcm_mobile_virtualkeyboard
%{_datadir}/kpackage/kcms/kcm_password
%{_libdir}/qt5/plugins/kcms/kcm_mobile_power.so
%{_datadir}/kpackage/kcms/kcm_mobile_power
%{_libdir}/qt5/plugins/kcms/kcm_cellular_network.so
%{_datadir}/kpackage/kcms/kcm_cellular_network
