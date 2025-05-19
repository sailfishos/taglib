Name:       taglib
Summary:    Audio Meta-Data Library
Version:    2.0.2
Release:    1
License:    LGPLv2 or MPLv1.1
URL:        https://github.com/sailfishos/taglib
Source0:    %{name}-%{version}.tar.gz
Patch0:     taglib-2.0.2-multilib.patch
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  pkgconfig(zlib)
BuildRequires:  cmake

%description
TagLib is a library for reading and editing the meta-data of several
popular audio formats. Currently it supports both ID3v1 and ID3v2 for
MP3 files, Ogg Vorbis comments and ID3 tags and Vorbis comments in
FLAC files.

%package devel
Summary:    Development files for %{name}
Requires:   %{name} = %{version}-%{release}

%description devel
%{summary}.

%package doc
Summary:   Documentation for %{name}
Requires:  %{name} = %{version}-%{release}

%description doc
%{summary}.

%prep
%autosetup -p1 -n %{name}-%{version}/%{name}

%build
%cmake

%cmake_build

%install
%cmake_install

rm -fr examples/.deps
rm -fr examples/Makefile*
rm -f %{buildroot}%{_libdir}/lib*.la

mkdir -p %{buildroot}%{_docdir}/%{name}-%{version}/examples
install -m0644 AUTHORS %{buildroot}%{_docdir}/%{name}-%{version}
install -m0644 -t %{buildroot}%{_docdir}/%{name}-%{version}/examples \
        examples/*

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%license COPYING.LGPL
%{_libdir}/lib*.so.*

%files devel
%{_bindir}/*-config
%{_includedir}/*
%{_libdir}/lib*.so
%{_libdir}/cmake/*
%{_libdir}/pkgconfig/*.pc

%files doc
%{_docdir}/%{name}-%{version}
