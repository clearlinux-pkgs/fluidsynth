#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
#
Name     : fluidsynth
Version  : 2.3.3
Release  : 32
URL      : https://github.com/FluidSynth/fluidsynth/archive/v2.3.3/fluidsynth-2.3.3.tar.gz
Source0  : https://github.com/FluidSynth/fluidsynth/archive/v2.3.3/fluidsynth-2.3.3.tar.gz
Summary  : A Real-Time Software Synthesizer That Uses Soundfont(tm)
Group    : Development/Tools
License  : LGPL-2.1 LGPL-2.1+
Requires: fluidsynth-bin = %{version}-%{release}
Requires: fluidsynth-lib = %{version}-%{release}
Requires: fluidsynth-license = %{version}-%{release}
Requires: fluidsynth-man = %{version}-%{release}
BuildRequires : alsa-lib-dev
BuildRequires : buildreq-cmake
BuildRequires : buildreq-gnome
BuildRequires : buildreq-kde
BuildRequires : doxygen
BuildRequires : glibc-dev
BuildRequires : libxslt-bin
BuildRequires : pkg-config
BuildRequires : pkgconfig(flac)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(gmodule-2.0)
BuildRequires : pkgconfig(gobject-2.0)
BuildRequires : pkgconfig(gthread-2.0)
BuildRequires : pkgconfig(libffi)
BuildRequires : pkgconfig(libinstpatch-1.0)
BuildRequires : pkgconfig(libmpg123)
BuildRequires : pkgconfig(libout123)
BuildRequires : pkgconfig(libpipewire-0.3)
BuildRequires : pkgconfig(libsyn123)
BuildRequires : pkgconfig(libsystemd)
BuildRequires : pkgconfig(ogg)
BuildRequires : pkgconfig(opus)
BuildRequires : pkgconfig(portaudio-2.0)
BuildRequires : pkgconfig(readline)
BuildRequires : pkgconfig(sndfile)
BuildRequires : pkgconfig(vorbis)
BuildRequires : pkgconfig(vorbisenc)
BuildRequires : pkgconfig(vorbisfile)
BuildRequires : pulseaudio-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
FluidSynth (formerly IIWU Synth) is a real-time software synthesizer
based on the SoundFont(tm) 2 specifications. It can read MIDI events
from the MIDI input device and render them to the audio device. It
can also play MIDI files.

%package bin
Summary: bin components for the fluidsynth package.
Group: Binaries
Requires: fluidsynth-license = %{version}-%{release}

%description bin
bin components for the fluidsynth package.


%package dev
Summary: dev components for the fluidsynth package.
Group: Development
Requires: fluidsynth-lib = %{version}-%{release}
Requires: fluidsynth-bin = %{version}-%{release}
Provides: fluidsynth-devel = %{version}-%{release}
Requires: fluidsynth = %{version}-%{release}

%description dev
dev components for the fluidsynth package.


%package lib
Summary: lib components for the fluidsynth package.
Group: Libraries
Requires: fluidsynth-license = %{version}-%{release}

%description lib
lib components for the fluidsynth package.


%package license
Summary: license components for the fluidsynth package.
Group: Default

%description license
license components for the fluidsynth package.


%package man
Summary: man components for the fluidsynth package.
Group: Default

%description man
man components for the fluidsynth package.


%prep
%setup -q -n fluidsynth-2.3.3
cd %{_builddir}/fluidsynth-2.3.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1689811986
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
%cmake ..
make  %{?_smp_mflags}
popd
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export FCFLAGS="$FFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export FFLAGS="$FFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export CFLAGS="$CFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export CXXFLAGS="$CXXFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export FFLAGS="$FFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export FCFLAGS="$FCFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
%cmake ..
make  %{?_smp_mflags}
popd
mkdir -p clr-build-avx512
pushd clr-build-avx512
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -O3 -Wl,-z,x86-64-v4 -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86_64-v4 -mprefer-vector-width=512 "
export FCFLAGS="$FFLAGS -O3 -Wl,-z,x86-64-v4 -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86_64-v4 -mprefer-vector-width=512 "
export FFLAGS="$FFLAGS -O3 -Wl,-z,x86-64-v4 -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86_64-v4 -mprefer-vector-width=512 "
export CXXFLAGS="$CXXFLAGS -O3 -Wl,-z,x86-64-v4 -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86_64-v4 -mprefer-vector-width=512 "
export CFLAGS="$CFLAGS -march=x86-64-v4 -m64 -Wl,-z,x86-64-v4 -mprefer-vector-width=512"
export CXXFLAGS="$CXXFLAGS -march=x86-64-v4 -m64 -Wl,-z,x86-64-v4 -mprefer-vector-width=512"
export FFLAGS="$FFLAGS -march=x86-64-v4 -m64 -Wl,-z,x86-64-v4 -mprefer-vector-width=512"
export FCFLAGS="$FCFLAGS -march=x86-64-v4 -m64 "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1689811986
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/fluidsynth
cp %{_builddir}/fluidsynth-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/fluidsynth/731a8eff333b8f7053ab2220511b524c87a75923 || :
pushd clr-build-avx2
%make_install_v3  || :
popd
pushd clr-build-avx512
%make_install_v4  || :
popd
pushd clr-build
%make_install
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py avx512 %{buildroot}-v4 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/fluidsynth
/V4/usr/bin/fluidsynth
/usr/bin/fluidsynth

%files dev
%defattr(-,root,root,-)
/usr/include/fluidsynth.h
/usr/include/fluidsynth/audio.h
/usr/include/fluidsynth/event.h
/usr/include/fluidsynth/gen.h
/usr/include/fluidsynth/ladspa.h
/usr/include/fluidsynth/log.h
/usr/include/fluidsynth/midi.h
/usr/include/fluidsynth/misc.h
/usr/include/fluidsynth/mod.h
/usr/include/fluidsynth/seq.h
/usr/include/fluidsynth/seqbind.h
/usr/include/fluidsynth/settings.h
/usr/include/fluidsynth/sfont.h
/usr/include/fluidsynth/shell.h
/usr/include/fluidsynth/synth.h
/usr/include/fluidsynth/types.h
/usr/include/fluidsynth/version.h
/usr/include/fluidsynth/voice.h
/usr/lib64/cmake/fluidsynth/FluidSynthConfig.cmake
/usr/lib64/cmake/fluidsynth/FluidSynthConfigVersion.cmake
/usr/lib64/cmake/fluidsynth/FluidSynthTargets-relwithdebinfo.cmake
/usr/lib64/cmake/fluidsynth/FluidSynthTargets.cmake
/usr/lib64/libfluidsynth.so
/usr/lib64/pkgconfig/fluidsynth.pc

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libfluidsynth.so.3.2.1
/V4/usr/lib64/libfluidsynth.so.3.2.1
/usr/lib64/libfluidsynth.so.3
/usr/lib64/libfluidsynth.so.3.2.1

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/fluidsynth/731a8eff333b8f7053ab2220511b524c87a75923

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/fluidsynth.1
