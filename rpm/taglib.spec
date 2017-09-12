Name:       taglib
Summary:    Audio Meta-Data Library
Version:    1.11.1
Release:    2
Group:      System/Libraries
License:    LGPLv2.1 or MPLv1.1
URL:        http://taglib.github.io/
Source0:    %{name}-%{version}.tar.gz
Patch0:     taglib-1.5rc1-multilib.patch
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
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}
Requires:   pkgconfig

%description devel
%{summary}.

%prep
%setup -q -n %{name}-%{version}/%{name}

# taglib-1.5rc1-multilib.patch
%patch0 -p1

%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
%{cmake} ..
popd

make %{?_smp_mflags} -C %{_target_platform}

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot} -C %{_target_platform}

rm -fr examples/.deps
rm -fr examples/Makefile*
rm -f %{buildroot}%{_libdir}/lib*.la

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING.LGPL
%{_libdir}/lib*.so.*

%files devel
%defattr(-,root,root,-)
%doc examples
%{_bindir}/*-config
%{_includedir}/*
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*.pc

