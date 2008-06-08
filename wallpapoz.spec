Name:		wallpapoz
Version:	0.4.1
Release:	%mkrel 1
Group:		Graphical desktop/GNOME
License:	GPLv2+
Source0:        http://wallpapoz.akbarhome.com/files/%name-%version.tar.bz2
URL:		http://kmess.sourceforge.net
Buildroot:	%{_tmppath}/%{name}-%{version}-buildroot
%py_requires
BuildRequires:	pygtk2.0
BuildRequires:	gnome-python
BuildRequires:	python-imaging
Summary:	Gnome Desktop Wallpapers Configuration Tool

%description
Wallpapoz application enables you to configure Gnome desktop wallpapers
in unique way. You could have Gnome desktop wallpaper changes when the
specified time has passed.

%files -f %name.lang
%defattr(-,root,root)

%prep
%setup -q

%install
rm -fr %buildroot
mkdir -p %buildroot%_prefix
./setup.py install --installdir %buildroot%_prefix

%clean
rm -fr %buildroot
