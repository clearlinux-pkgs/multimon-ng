#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : multimon-ng
Version  : 1.1.6
Release  : 7
URL      : https://github.com/EliasOenal/multimon-ng/archive/1.1.6.tar.gz
Source0  : https://github.com/EliasOenal/multimon-ng/archive/1.1.6.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: multimon-ng-bin = %{version}-%{release}
Requires: multimon-ng-license = %{version}-%{release}
Requires: sox
BuildRequires : buildreq-cmake
BuildRequires : buildreq-qmake
BuildRequires : pulseaudio
BuildRequires : pulseaudio-dev

%description
multimon-ng is the successor of multimon. It decodes the following digital transmission modes:

%package bin
Summary: bin components for the multimon-ng package.
Group: Binaries
Requires: multimon-ng-license = %{version}-%{release}

%description bin
bin components for the multimon-ng package.


%package license
Summary: license components for the multimon-ng package.
Group: Default

%description license
license components for the multimon-ng package.


%prep
%setup -q -n multimon-ng-1.1.6

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1539783945
mkdir -p clr-build
pushd clr-build
%cmake ..
make  %{?_smp_mflags} VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1539783945
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/multimon-ng
cp COPYING %{buildroot}/usr/share/package-licenses/multimon-ng/COPYING
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/multimon-ng

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/multimon-ng/COPYING
