Name:		wallpapoz
Version:	0.4.1
Release:	%mkrel 6
Group:		Graphical desktop/GNOME
License:	GPLv2+
Source0:        http://wallpapoz.akbarhome.com/files/%name-%version.tar.bz2
URL:		http://wallpapoz.akbarhome.com
Buildroot:	%{_tmppath}/%{name}-%{version}-buildroot
%py_requires
BuildRequires:	pygtk2.0
BuildRequires:	gnome-python
BuildRequires:	python-imaging
BuildRequires:	pygtk2.0-libglade
Requires:	pygtk2.0
Requires:	gnome-python
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
%defattr(-,root,root)
%doc README CHANGELOG
%_bindir/daemon_wallpapoz
%_bindir/wallpapoz
%_datadir/wallpapoz
%_datadir/pixmaps/wallpapoz.png
%_datadir/applications/wallpapoz.desktop

%prep
%setup -q

%install
rm -fr %buildroot
mkdir -p %buildroot%_prefix
./setup.py install --installdir %buildroot%_prefix

%find_lang %name --with-gnome

%clean
rm -fr %buildroot

%if %mdkversion < 200900
%post
%update_menus
%endif

%if %mdkversion < 200900
%postun
%clean_menus
%endif

