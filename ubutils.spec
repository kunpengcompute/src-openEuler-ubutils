Summary: Implementation of ubutils
Name: ubutils
Version: 1.0.2
Release: 7%{?dist}
License: MIT
URL: https://gitee.com/openeuler/ubutils
Source0: %{name}-%{version}.tar.gz

Patch1: 0001-ub-ubutils-delete-mode-number-for-FEC.patch
Patch2: 0002-ub-ubutils-bugfix-some-issues-for-ubutils.patch
Patch3: 0003-ub-ubutils-Optimized-the-log-printing-and-spelling-o.patch
Patch4: 0004-ub-ubutils-Adding-the-device-ID-of-the-new-chip-vers.patch

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: make
ExclusiveArch: aarch64

BuildRoot:      %{name}-%{version}-%{release}

%description
This implementation provides ubutils sending and reception.

%prep
%autosetup -p1 -n ubutils-%{version}

%build
rm -rf build
cmake -S . -B build \
      -DCMAKE_INSTALL_PREFIX=%{_prefix} \
      -DCMAKE_BUILD_TYPE=RelWithDebInfo
cmake --build build --config Release -- -j$(nproc)

%install
rm -rf %{buildroot}
cmake --install build --prefix=%{buildroot}%{_prefix}
mkdir -p $RPM_BUILD_ROOT%{_prefix}/share/hwdata
install -m 644 ub.ids $RPM_BUILD_ROOT%{_prefix}/share/hwdata
if [ -n "${SOURCE_DATE_EPOCH:-}" ]; then
    M=$(LC_ALL=C date -u -d "@$SOURCE_DATE_EPOCH" '+%%d %%B %%Y')
else
    M=$(LC_ALL=C date -u '+%%d %%B %%Y')
fi
for man in setub lsub; do
    sed -e "s/@TODAY@/$M/" \
        -e "s/@VERSION@/%{name}-%{version}/" \
        -e "s#@IDSDIR@#%{_datadir}/hwdata#" \
        "$man.man" >"$man.8"
done
mkdir -p $RPM_BUILD_ROOT%{_prefix}/share/man/man8
install -m 644 lsub.8 setub.8 $RPM_BUILD_ROOT%{_prefix}/share/man/man8

%files
%{_bindir}/lsub
%{_bindir}/setub
%config %{_prefix}/share/hwdata/ub.ids
%attr(0644, root, man) %{_prefix}/share/man/man8/*

%clean
rm -rf %{buildroot}

%changelog
* Fri Nov 13 2026 zhao-lichang <zhaolichang@huawei.com> - 1.0.2-7
- [Type] sync
- [DESC] update to 0930
* Wed Jul 15 2026 qiushengming <846759657@qq.com> - 1.0.2-6
- [Type] sync
- [DESC] Package init
