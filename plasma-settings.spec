#define snapshot 20200901
#define commit 08fa0c465ba93f6621529897bfaa844f0f58b066

Name:		plasma-settings
Version:	25.12.0
Release:	%{?snapshot:1.%{snapshot}.}3
Summary:	Settings application for Plasma Mobile
%if 0%{?snapshot}
Source0:	https://invent.kde.org/plasma-mobile/plasma-settings/-/archive/master/plasma-settings-master.tar.bz2
%else
Source0:	https://invent.kde.org/plasma-mobile/plasma-settings/-/archive/v%{version}/plasma-settings-v%{version}.tar.bz2
%endif
License:	GPLv3
Group:		Applications/Productivity
BuildSystem:	cmake
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6Quick)
BuildRequires:	cmake(Qt6Test)
BuildRequires:	cmake(KF6WindowSystem)
BuildRequires:	cmake(KF6CoreAddons)
BuildRequires:	cmake(KF6Solid)
BuildRequires:	cmake(KF6Config)
BuildRequires:	cmake(KF6Auth)
BuildRequires:	cmake(KF6DBusAddons)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6Declarative)
BuildRequires:	cmake(KF6KIO)
BuildRequires:	cmake(KF6ModemManagerQt)
BuildRequires:	cmake(KF6NetworkManagerQt)
BuildRequires:	cmake(KF6KirigamiAddons)
BuildRequires:	pkgconfig(gobject-2.0)

%description
Settings application for Plasma Mobile

%files -f %{name}.lang
%{_bindir}/plasma-settings
%{_datadir}/applications/org.kde.mobile.plasmasettings.desktop
%{_datadir}/icons/hicolor/scalable/apps/org.kde.mobile.plasmasettings.svg
%{_datadir}/metainfo/org.kde.mobile.plasmasettings.metainfo.xml
%{_datadir}/plasma-settings
