%define name libsexymm
%define version 0.1.9
%define release %mkrel 1
%define major 2
%define libname %mklibname sexymm %major

Summary: Collection of widgets for gtkmm
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://releases.chipx86.com/libsexy/%name/%{name}-%{version}.tar.bz2
License: LGPL
Group: System/Libraries
Url: http://www.chipx86.com/wiki/Libsexy
BuildRequires: libsexy-devel
BuildRequires: gtkmm2.4-devel

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
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%post -n %libname -p /sbin/ldconfig
%postun -n %libname -p /sbin/ldconfig

%files -n %libname
%defattr(-,root,root)
%_libdir/*.so.%{major}*

%files -n %libname-devel
%defattr(-,root,root)
%doc ChangeLog AUTHORS NEWS
%_includedir/*
%_libdir/*.so
%_libdir/*.a
%_libdir/%name
%attr(644,root,root) %_libdir/*.la
%_libdir/pkgconfig/*
