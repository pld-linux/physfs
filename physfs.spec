Summary:	PhysicsFS file abstraction layer for games
Summary(pl.UTF-8):	PhysicsFS - warstwa abstrakcji plików dla gier
Name:		physfs
Version:	3.2.0
Release:	1
License:	BSD-like (see LICENSE)
Group:		Libraries
#Source0Download: https://github.com/icculus/physfs/releases
Source0:	https://github.com/icculus/physfs/archive/release-%{version}/%{name}-release-%{version}.tar.gz
# Source0-md5:	df43675566d86f795f0fe179087b231b
URL:		https://www.icculus.org/physfs/
BuildRequires:	cmake >= 3.0
BuildRequires:	doxygen
BuildRequires:	ncurses-devel
BuildRequires:	readline-devel
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(macros) >= 1.605
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

%description -l pl.UTF-8
PhysicsFS to biblioteka udostępniająca abstrakcyjny dostęp do różnych
archiwów. Została stworzona z myślą o grach video, a projekt był
trochę wzorowany na podsystemie plików z Quake 3. Programista
definiuje "katalog zapisu" w fizycznym systemie plików. Żaden zapis do
pliku poprzez API PhysicsFS nie może wyjść poza ten katalog - ze
względu na bezpieczeństwo. Na przykład, wbudowany język skryptowy nie
może zapisywać poza tą ścieżką, jeżeli używa PhysicsFS do wszystkich
operacji wejścia/wyjścia, dzięki czemu można bezpiecznie uruchamiać
nie zaufane skrypty. Dowiązania symboliczne także mogą być wyłączone
dla poprawy bezpieczeństwa. Do odczytu pliku programista podaje
katalogi i archiwa, które składają się na "ścieżkę poszukiwań". Po
zdefiniowaniu tej ścieżki, staje się ona pojedynczym, przezroczystym
hierarchicznym systemem plików. Pozwala to na łatwy dostęp do plików
ZIP w taki sam sposób, jak do plików na dysku, a także ułatwia
dostarczenie nowego archiwum, które przykryje poprzednie na poziomie
plików. Ponadto PhysicsFS daje wyabstrahowane od platformy sposoby na
określenie, czy dostępne są CD-ROMy, katalog domowy użytkownika, gdzie
w prawdziwym systemie plików działa program itp.

%package devel
Summary:	Header files for PhysicsFS development
Summary(pl.UTF-8):	Pliki nagłówkowe do programowania z użyciem PhysicsFS
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	zlib-devel

%description devel
PhysicsFS is a library to provide abstract access to various archives.
This package contains the development headers and documentaion to
build programs using PhysicsFS.

%description devel -l pl.UTF-8
PhysicsFS to biblioteka udostępniająca abstrakcyjny dostęp do różnych
archiwów. Ten pakiet zawiera pliki nagłówkowe i dokumentację do
budowania programów z użyciem PhysicsFS.

%package static
Summary:	Static PhysicsFS libraries
Summary(pl.UTF-8):	Statyczne biblioteki PhysicsFS
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
PhysicsFS is a library to provide abstract access to various archives.
This package contains the static PhysicsFS libraries.

%description static -l pl.UTF-8
PhysicsFS to biblioteka udostępniająca abstrakcyjny dostęp do różnych
archiwów. Ten pakiet zawiera statyczne biblioteki PhysicsFS.

%package apidocs
Summary:	API documentation for PhysicsFS library
Summary(pl.UTF-8):	Dokumentacja API biblioteki PhysicsFS
Group:		Documentation
BuildArch:	noarch

%description apidocs
API documentation for PhysicsFS library.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki PhysicsFS.

%package programs
Summary:	Program for testing PhysicsFS archives
Summary(pl.UTF-8):	Program do testowania archiwów PhysicsFS
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description programs
PhysicsFS is a library to provide abstract access to various archives.
This package contains the programs using for PhysicsFS archives
testing.

%description programs -l pl.UTF-8
PhysicsFS to biblioteka udostępniająca abstrakcyjny dostęp do różnych
archiwów. Ten pakiet zawiera program używany do testowania archiwów
PhysicsFS.

%prep
%setup -q -n %{name}-release-%{version}

%build
install -d build
cd build
%cmake .. \
	-DCMAKE_CXX_COMPILER_WORKS=1 \
	-DCMAKE_CXX_COMPILER="%{__cc}"

%{__make}

cd ..
doxygen build/Doxyfile

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_mandir}/man3

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

cp -p build/docs/man/man3/{PHYS*,phys*} $RPM_BUILD_ROOT%{_mandir}/man3

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc docs/{CHANGELOG.txt,CREDITS.txt,TODO.txt} LICENSE.txt
%attr(755,root,root) %{_libdir}/libphysfs.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libphysfs.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libphysfs.so
%{_includedir}/physfs.h
%{_pkgconfigdir}/physfs.pc
%{_libdir}/cmake/PhysFS
%{_mandir}/man3/PHYSFS_*.3*
%{_mandir}/man3/physfs.h.3*

%files static
%defattr(644,root,root,755)
%{_libdir}/libphysfs.a

%files apidocs
%defattr(644,root,root,755)
%doc build/docs/html/*

%files programs
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/test_physfs
