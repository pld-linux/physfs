Summary:	PhysicsFS file abstraction layer for games
Summary(pl):	PhysicsFS - warstwa abstrakcji plik�w dla gier
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
PhysicsFS to biblioteka udost�pniaj�ca abstrakcyjny dost�p do r�nych
archiw�w. Zosta�a stworzona z my�l� o grach video, a projekt by�
troch� wzorowany na podsystemie plik�w z Quake 3. Programista
definiuje "katalog zapisu" w fizycznym systemie plik�w. �aden zapis do
pliku poprzez API PhysicsFS nie mo�e wyj�� poza ten katalog - ze
wzgl�du na bezpiecze�stwo. Na przyk�ad, wbudowany j�zyk skryptowy nie
mo�e zapisywa� poza t� �cie�k�, je�eli u�ywa PhysicsFS do wszystkich
operacji wej�cia/wyj�cia, dzi�ki czemu mo�na bezpiecznie uruchamia�
nie zaufane skrypty. Dowi�zania symboliczne tak�e mog� by� wy��czone
dla poprawy bezpiecze�stwa. Do odczytu pliku programista podaje
katalogi i archiwa, kt�re sk�adaj� si� na "�cie�k� poszukiwa�". Po
zdefiniowaniu tej �cie�ki, staje si� ona pojedynczym, przezroczystym
hierarchicznym systemem plik�w. Pozwala to na �atwy dost�p do plik�w
ZIP w taki sam spos�b, jak do plik�w na dysku, a tak�e u�atwia
dostarczenie nowego archiwum, kt�re przykryje poprzednie na poziomie
plik�w. Ponadto PhysicsFS daje wyabstrahowane od platformy sposoby na
okre�lenie, czy dost�pne s� CD-ROMy, katalog domowy u�ytkownika, gdzie
w prawdziwym systemie plik�w dzia�a program itp.

%package devel
Summary:	Header files for PhysicsFS development
Summary(pl):	Pliki nag��wkowe do programowania z u�yciem PhysicsFS
Group:		Development/Libraries
Requires:	%{name} = %{version}
Requires:	zlib-devel

%description devel
PhysicsFS is a library to provide abstract access to various archives.
This package contains the development headers and documentaion to
build programs using PhysicsFS.

%description devel -l pl
PhysicsFS to biblioteka udost�pniaj�ca abstrakcyjny dost�p do r�nych
archiw�w. Ten pakiet zawiera pliki nag��wkowe i dokumentacj� do
budowania program�w z u�yciem PhysicsFS.

%package static
Summary:	Static PhysicsFS libraries
Summary(pl):	Statyczne biblioteki PhysicsFS
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
PhysicsFS is a library to provide abstract access to various archives.
This package contains the static PhysicsFS libraries.

%description static -l pl
PhysicsFS to biblioteka udost�pniaj�ca abstrakcyjny dost�p do r�nych
archiw�w. Ten pakiet zawiera statyczne biblioteki PhysicsFS.

%package programs
Summary:	Program for testing PhysicsFS archives
Summary(pl):	Program do testowania archiw�w PhysicsFS
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description programs
PhysicsFS is a library to provide abstract access to various archives.
This package contains the programs using for PhysicsFS archives
testing.

%description programs -l pl
PhysicsFS to biblioteka udost�pniaj�ca abstrakcyjny dost�p do r�nych
archiw�w. Ten pakiet zawiera program u�ywany do testowania archiw�w
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
