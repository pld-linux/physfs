Summary:	PhysicsFS file abstraction layer for games
Name:		physfs
Version:	0.1.8
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://www.icculus.org/physfs/downloads/%{name}-%{version}.tar.gz
URL:		http://www.icculus.org/physfs/
BuildRequires:	doxygen
BuildRequires:	ncurses-devel
BuildRequires:	readline-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PhysicsFS is a library to provide abstract access to various archives.
It is intended for use in video games, and the design was somewhat inspired
by Quake 3's file subsystem. The programmer defines a "write directory" on
the physical filesystem. No file writing done through the PhysicsFS API can
leave that write directory, for security. For example, an embedded scripting
language cannot write outside of this path if it uses PhysFS for all of its
I/O, which means that untrusted scripts can run more safely. Symbolic links
can be disabled as well, for added safety. For file reading, the programmer
lists directories and archives that form a "search path". Once the search
path is defined, it becomes a single, transparent hierarchical filesystem.
This makes for easy access to ZIP files in the same way as you access a file
directly on the disk, and it makes it easy to ship a new archive that will
override a previous archive on a per-file basis. Finally, PhysicsFS gives
you platform-abstracted means to determine if CD-ROMs are available, the
user's home directory, where in the real filesystem your program is running,
etc. 

%package devel
Summary:	Header files for PhysicsFS development
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
PhysicsFS is a library to provide abstract access to various archives.
This package contains the development headers, libraries, and documentaion to
build programs using PhysicsFS.

%package static
Summary:	Static libraries for PhysicsFS development
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
PhysicsFS is a library to provide abstract access to various archives.
This package contains the static libraries to build programs using PhysicsFS.

%package programs
Summary:	Program for testing PhysicsFS archives
Group:		Development/Libraries

%description programs
PhysicsFS is a library to provide abstract access to various archives.
This package contains the programs using for PhysicsFS archives testing.

%prep
%setup

%build
%configure
%{__make}

doxygen

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_mandir}/man3

make install DESTDIR=${RPM_BUILD_ROOT}

install docs/man/man3/{PHYS*,phys*} $RPM_BUILD_ROOT%{_mandir}/man3

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc CHANGELOG CREDITS
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc docs/html
%{_libdir}/lib*.la
%{_libdir}/lib*.so
%{_includedir}/physfs.h
%{_mandir}/man3/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

%files programs
%defattr(644,root,root,755)
%{_bindir}/test_physfs
