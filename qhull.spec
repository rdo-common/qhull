%define name qhull
%define version 2003.1
%define release 2

Summary: General dimension convex hull programs
Name: %{name}
Version: %{version}
Release: %{release}.2
License:  Distributable
Group: System Environment/Libraries
Source0: http://www.qhull.org/download/qhull-%{version}.tar.gz
URL: http://www.qhull.org
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig

%description
Qhull is a general dimension convex hull program that reads a set
of points from stdin, and outputs the smallest convex set that contains
the points to stdout.  It also generates Delaunay triangulations, Voronoi
diagrams, furthest-site Voronoi diagrams, and halfspace intersections
about a point.

%package devel
Group: Development/Libraries
Summary: Development files for qhull
Requires: %{name} = %{version}-%{release}

%description devel
Qhull is a general dimension convex hull program that reads a set
of points from stdin, and outputs the smallest convex set that contains
the points to stdout.  It also generates Delaunay triangulations, Voronoi
diagrams, furthest-site Voronoi diagrams, and halfspace intersections
about a point.

%prep
%setup -n %{name}-%{version}


%build
%configure
make

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT \
  docdir=%{_docdir}/%{name}-%{version} install

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%files
%defattr(-,root,root)
%doc %{_docdir}/%{name}-%{version}
%_bindir/*
%_libdir/*.so.*
%_mandir/man1/*

%files devel
%defattr(-,root,root)
%_libdir/*.*a
%_libdir/*.so
%_includedir/*

%changelog
* Sun Aug 08 2004 Ralf Corsepius <ralf[AT]links2linux.de>	- 2003.1-0.fdr.2
- Use default documentation installation scheme.

* Fri Jul 16 2004 Ralf Corsepius <ralf[AT]links2linux.de>	- 2003.1-0.fdr.1
- Initial Fedora RPM.
