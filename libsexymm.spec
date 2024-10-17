%define name libsexymm
%define version 0.1.9
%define release 6
%define major 2
%define libname %mklibname sexymm %major

Summary: Collection of widgets for gtkmm
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://releases.chipx86.com/libsexy/%name/%{name}-%{version}.tar.bz2
License: LGPL
Group: System/Libraries
Url: https://www.chipx86.com/wiki/Libsexy
BuildRequires: pkgconfig(libsexy)
BuildRequires: pkgconfig(gdkmm-2.4)

%description
This is a collection of widgets for gtkmm.

%package -n %libname
Group:System/Libraries
Summary: Collection of widgets for gtkmm

%description -n %libname
This is a collection of widgets for gtkmm.

%package -n %libname-devel
Group:Development/C++
Summary: Collection of widgets for gtkmm
Requires: %libname = %version
Provides: libsexymm-devel = %version-%release
%description -n %libname-devel
This is a collection of widgets for gtkmm.

%prep
%setup -q

%build
%configure2_5x
%make

%install
%makeinstall_std

%if %mdkversion < 200900
%post -n %libname -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libname -p /sbin/ldconfig
%endif

%files -n %libname
%_libdir/*.so.%{major}*

%files -n %libname-devel
%doc ChangeLog AUTHORS NEWS
%_includedir/*
%_libdir/*.so
%_libdir/*.a
%_libdir/%name
%_libdir/pkgconfig/*


%changelog
* Mon Sep 19 2011 Götz Waschk <waschk@mandriva.org> 0.1.9-5mdv2012.0
+ Revision: 700380
- rebuild

* Sun Sep 13 2009 Thierry Vignaud <tv@mandriva.org> 0.1.9-4mdv2011.0
+ Revision: 438740
- rebuild

* Sun Nov 09 2008 Oden Eriksson <oeriksson@mandriva.com> 0.1.9-3mdv2009.1
+ Revision: 301582
- rebuilt against new libxcb

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 0.1.9-2mdv2009.0
+ Revision: 268001
- rebuild early 2009.0 package (before pixel changes)

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Wed Jan 02 2008 Olivier Blin <blino@mandriva.org> 0.1.9-1mdv2009.0
+ Revision: 140928
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Jun 07 2007 Götz Waschk <waschk@mandriva.org> 0.1.9-1mdv2008.0
+ Revision: 36604
- Import libsexymm




* Thu Jun  7 2007 Götz Waschk <waschk@mandriva.org> 0.1.9-1mdv2008.0
- initial package
