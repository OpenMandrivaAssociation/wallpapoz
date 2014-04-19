Name:		wallpapoz
Version:	0.6.2
Release:	1
Group:		Graphical desktop/GNOME
License:	GPLv2+
Source0:        http://wallpapoz.akbarhome.com/files/%name-%version.tar.bz2
URL:		http://wallpapoz.akbarhome.com
Buildroot:	%{_tmppath}/%{name}-%{version}-buildroot
%py_requires
BuildRequires:	pygtk2.0
BuildRequires:	python-imaging
BuildRequires:	pygtk2.0-libglade
BuildRequires:	python-devel
Requires:	pygtk2.0
Requires:	python-imaging
Requires:	pygtk2.0-libglade
Requires:	xwininfo
BuildArch:	noarch
Summary:	Gnome Desktop wallpaper configuration tool

%description
Wallpapoz application enables you to configure Gnome desktop wallpapers
in unique way. You could have Gnome desktop wallpaper changes when the
specified time has passed.

%files -f %name.lang
%doc README CHANGELOG
%_bindir/daemon_wallpapoz
%_bindir/wallpapoz
%_bindir/launcher_wallpapoz.sh
%_datadir/wallpapoz
%_datadir/pixmaps/wallpapoz.png
%_datadir/applications/wallpapoz.desktop

%prep
%setup -q

%install
mkdir -p %buildroot%_prefix
./setup.py install --installdir %buildroot%_prefix

%find_lang %name --with-gnome

