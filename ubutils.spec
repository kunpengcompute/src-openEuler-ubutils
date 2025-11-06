Summary: Implementation of ubutils
Name: ubutils
Version: 1.0.0
Release: 1
License: MIT
URL: https://gitee.com/openeuler/ubutils
Source0: %{name}.tar.gz

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: make

BuildRoot:      %{name}-%{version}-%{release}

%description
This implementation provides ubutils sending and reception.

%package devel
Summary:  Implementation of ubutils(UB) - Tools and header files for developers
Group:    Development/Libraries/C
BuildRequires: pkgconfig
Requires: ubutils = %{version}-%{release}

%description devel
This package is required to develop alternate clients for ubutils.

Ubutils is the basic DFX tool of ubus, including setub and lsub.

%prep
%setup -q -n ubutils

%build
rm -rf build
cmake -S . -B build \
      -DCMAKE_INSTALL_PREFIX=%{_prefix} \
      -DCMAKE_BUILD_TYPE=RelWithDebInfo
cmake --build build --config Release -- -j$(nproc)

%install
rm -rf %{buildroot}
cmake --install build --prefix=%{buildroot}%{_prefix}

%files
%{_bindir}/lsub
%{_bindir}/setub

%clean
rm -rf %{buildroot}

%changelog
* Tue Aug 12 2025 laz <lianzhe1@h-partners.com> - 1.0.0-1
- Support the basic DFX tool(Ubutils) of ubus, including setub, lsub and ub.ids
