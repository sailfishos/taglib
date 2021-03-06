Name:       taglib
Summary:    Audio Meta-Data Library
Version:    1.12
Release:    1
License:    LGPLv2 or MPLv1.1
URL:        https://github.com/sailfishos/taglib
Source0:    %{name}-%{version}.tar.gz
Patch0:     taglib-1.12-multilib.patch
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
mkdir -p %{_target_platform}
pushd %{_target_platform}
%{cmake} ..
popd

%make_build -C %{_target_platform}

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot} -C %{_target_platform}

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
%defattr(-,root,root,-)
%license COPYING.LGPL
%{_libdir}/lib*.so.*

%files devel
%defattr(-,root,root,-)
%{_bindir}/*-config
%{_includedir}/*
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*.pc

%files doc
%defattr(-,root,root,-)
%{_docdir}/%{name}-%{version}
