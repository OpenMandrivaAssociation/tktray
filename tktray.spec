Summary:	System Tray Icon Support for Tk on X11
Name:		tktray
Version:	1.3.9
Release:	1
License:	BSD
Group:		System/Libraries
Url:		https://code.google.com/p/tktray/
Source0:	http://tktray.googlecode.com/files/%{name}%{version}.tar.gz
BuildRequires:	tcl-devel
BuildRequires:	pkgconfig(tk)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xext)
Requires:	tk
Requires:	tcl

%description
Tktray is an extension that is able to create system tray icons.
It follows http://www.freedesktop.org specifications when looking 
up the system tray manager.

%files
%doc ChangeLog license.terms docs/tktray.html
%{tcl_sitearch}/%{name}%{version}
%{_libdir}/*.so
%{_mandir}/mann/%{name}.n.*

#----------------------------------------------------------------------------

%prep
%setup -q -n %{name}%{version}

chmod 0644 ChangeLog license.terms docs/*

%build
%configure2_5x \
	--libdir=%{tcl_sitearch} \
	--with-tcl=%{_libdir} \
	--with-tk=%{_libdir}

%make CFLAGS_DEFAULT="%{optflags}" CFLAGS_WARNING="-Wall"

%install
%makeinstall_std

ln -s tcl%{tcl_version}/%{name}%{version}/lib%{name}%{version}.so %{buildroot}%{_libdir}/lib%{name}%{version}.so

