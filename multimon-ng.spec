#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : multimon-ng
Version  : 1.1.4
Release  : 1
URL      : https://github.com/EliasOenal/multimon-ng/archive/1.1.4.tar.gz
Source0  : https://github.com/EliasOenal/multimon-ng/archive/1.1.4.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: multimon-ng-bin
BuildRequires : cmake

%description
multimon-ng is the successor of multimon. It decodes the following digital transmission modes:

%package bin
Summary: bin components for the multimon-ng package.
Group: Binaries

%description bin
bin components for the multimon-ng package.


%prep
%setup -q -n multimon-ng-1.1.4

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1510615678
mkdir clr-build
pushd clr-build
cmake .. -G "Unix Makefiles" -DCMAKE_INSTALL_PREFIX=/usr -DBUILD_SHARED_LIBS:BOOL=ON -DLIB_INSTALL_DIR:PATH=/usr/lib64 -DCMAKE_AR=/usr/bin/gcc-ar -DLIB_SUFFIX=64 -DCMAKE_BUILD_TYPE=RelWithDebInfo -DCMAKE_RANLIB=/usr/bin/gcc-ranlib
make VERBOSE=1  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1510615678
rm -rf %{buildroot}
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/multimon-ng
