Name:		wallpapoz
Version:	0.5
Release:	%mkrel 1
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
BuildRequires:	python-devel
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



%changelog
* Wed Mar 09 2011 Stéphane Téletchéa <steletch@mandriva.org> 0.5-1mdv2011.0
+ Revision: 643139
- update to new version 0.5

* Sun Oct 31 2010 Funda Wang <fwang@mandriva.org> 0.4.1-6mdv2011.0
+ Revision: 590859
- BR p-devel
- rebuild for py2.7

* Sun Sep 20 2009 Thierry Vignaud <tv@mandriva.org> 0.4.1-5mdv2010.0
+ Revision: 445731
- rebuild

* Sun Mar 15 2009 Emmanuel Andry <eandry@mandriva.org> 0.4.1-4mdv2009.1
+ Revision: 355454
- rebuild for python 2.6

* Tue Nov 25 2008 Adam Williamson <awilliamson@mandriva.org> 0.4.1-3mdv2009.1
+ Revision: 306794
- All Caps In Summary Looks Weird
- requires xwininfo - http://forum.mandriva.com/viewtopic.php?t=100494

* Sat Aug 09 2008 Thierry Vignaud <tv@mandriva.org> 0.4.1-2mdv2009.0
+ Revision: 269669
- rebuild early 2009.0 package (before pixel changes)

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Sun Jun 08 2008 Funda Wang <fwang@mandriva.org> 0.4.1-1mdv2009.0
+ Revision: 216986
- add more br
- list files
- import source and spec
- Created package structure for wallpapoz.

