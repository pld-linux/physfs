Summary:	PhysicsFS file abstraction layer for games
Summary(pl):	PhysicsFS - warstwa abstrakcji plików dla gier
Name:		physfs
Version:	0.1.9
Release:	1
License:	BSD-like (see LICENSE)
Group:		Libraries
Source0:	http://www.icculus.org/physfs/downloads/%{name}-%{version}.tar.gz
# Source0-md5:	ee61f31d15563a3f785adbd800933631
Patch0:		%{name}-link.patch
URL:		http://www.icculus.org/physfs/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	doxygen
BuildRequires:	libtool
BuildRequires:	ncurses-devel
BuildRequires:	readline-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PhysicsFS is a library to provide abstract access to various archives.
It is intended for use in video games, and the design was somewhat
inspired by Quake 3's file subsystem. The programmer defines a "write
directory" on the physical filesystem. No file writing done through
the PhysicsFS API can leave that write directory, for security. For
example, an embedded scripting language cannot write outside of this
path if it uses PhysFS for all of its I/O, which means that untrusted
scripts can run more safely. Symbolic links can be disabled as well,
for added safety. For file reading, the programmer lists directories
and archives that form a "search path". Once the search path is
defined, it becomes a single, transparent hierarchical filesystem.
This makes for easy access to ZIP files in the same way as you access
a file directly on the disk, and it makes it easy to ship a new
archive that will override a previous archive on a per-file basis.
Finally, PhysicsFS gives you platform-abstracted means to determine if
CD-ROMs are available, the user's home directory, where in the real
filesystem your program is running, etc.

%description -l pl
PhysicsFS to biblioteka udostêpniaj±ca abstrakcyjny dostêp do ró¿nych
archiwów. Zosta³a stworzona z my¶l± o grach video, a projekt by³
trochê wzorowany na podsystemie plików z Quake 3. Programista
definiuje "katalog zapisu" w fizycznym systemie plików. ¯aden zapis do
pliku poprzez API PhysicsFS nie mo¿e wyj¶æ poza ten katalog - ze
wzglêdu na bezpieczeñstwo. Na przyk³ad, wbudowany jêzyk skryptowy nie
mo¿e zapisywaæ poza t± ¶cie¿k±, je¿eli u¿ywa PhysicsFS do wszystkich
operacji wej¶cia/wyj¶cia, dziêki czemu mo¿na bezpiecznie uruchamiaæ
nie zaufane skrypty. Dowi±zania symboliczne tak¿e mog± byæ wy³±czone
dla poprawy bezpieczeñstwa. Do odczytu pliku programista podaje
katalogi i archiwa, które sk³adaj± siê na "¶cie¿kê poszukiwañ". Po
zdefiniowaniu tej ¶cie¿ki, staje siê ona pojedynczym, przezroczystym
hierarchicznym systemem plików. Pozwala to na ³atwy dostêp do plików
ZIP w taki sam sposób, jak do plików na dysku, a tak¿e u³atwia
dostarczenie nowego archiwum, które przykryje poprzednie na poziomie
plików. Ponadto PhysicsFS daje wyabstrahowane od platformy sposoby na
okre¶lenie, czy dostêpne s± CD-ROMy, katalog domowy u¿ytkownika, gdzie
w prawdziwym systemie plików dzia³a program itp.

%package devel
Summary:	Header files for PhysicsFS development
Summary(pl):	Pliki nag³ówkowe do programowania z u¿yciem PhysicsFS
Group:		Development/Libraries
Requires:	%{name} = %{version}
Requires:	zlib-devel

%description devel
PhysicsFS is a library to provide abstract access to various archives.
This package contains the development headers and documentaion to
build programs using PhysicsFS.

%description devel -l pl
PhysicsFS to biblioteka udostêpniaj±ca abstrakcyjny dostêp do ró¿nych
archiwów. Ten pakiet zawiera pliki nag³ówkowe i dokumentacjê do
budowania programów z u¿yciem PhysicsFS.

%package static
Summary:	Static PhysicsFS libraries
Summary(pl):	Statyczne biblioteki PhysicsFS
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
PhysicsFS is a library to provide abstract access to various archives.
This package contains the static PhysicsFS libraries.

%description static -l pl
PhysicsFS to biblioteka udostêpniaj±ca abstrakcyjny dostêp do ró¿nych
archiwów. Ten pakiet zawiera statyczne biblioteki PhysicsFS.

%package programs
Summary:	Program for testing PhysicsFS archives
Summary(pl):	Program do testowania archiwów PhysicsFS
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description programs
PhysicsFS is a library to provide abstract access to various archives.
This package contains the programs using for PhysicsFS archives
testing.

%description programs -l pl
PhysicsFS to biblioteka udostêpniaj±ca abstrakcyjny dostêp do ró¿nych
archiwów. Ten pakiet zawiera program u¿ywany do testowania archiwów
PhysicsFS.

%prep
%setup -q
%patch -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
# unused beos.cpp causes unnecessary using CXXLINK... workaround
%{__make} \
	CXXLINK="\$(LINK)"

doxygen

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_mandir}/man3

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install docs/man/man3/{PHYS*,phys*} $RPM_BUILD_ROOT%{_mandir}/man3

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc CHANGELOG CREDITS LICENSE TODO
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc docs/html
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/physfs.h
%{_mandir}/man3/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

%files programs
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/test_physfs
