Summary: Implementation of ubutils
Name: ubutils
Version: 1.0.2
Release: 7
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

%package devel
Summary:  Implementation of ubutils(UB) - Tools and header files for developers
Group:    Development/Libraries/C
BuildRequires: pkgconfig
Requires: ubutils = %{version}-%{release}

%description devel
This package is required to develop alternate clients for ubutils.

Ubutils is the basic debug tool of ubus, including setub and lsub.

%prep
%setup -q -n ubutils-%{version}
%autopatch -p1

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
M=`echo $DATE | sed 's/-01-/-January-/;s/-02-/-February-/;s/-03-/-March-/;s/-04-/-April-/;s/-05-/-May-/;s/-06-/-June-/;s/-07-/-July-/;s/-08-/-August-/;s/-09-/-September-/;s/-10-/-October-/;s/-11-/-November-/;s/-12-/-December-/;s/\(.*\)-\(.*\)-\(.*\)/\3 \2 \1/'` ; sed <setub.man >setub.8 "s/@TODAY@/$M/;s/@VERSION@/ubutils-1.0.1/;s#@IDSDIR@#/usr/share/hwdata#"
M=`echo $DATE | sed 's/-01-/-January-/;s/-02-/-February-/;s/-03-/-March-/;s/-04-/-April-/;s/-05-/-May-/;s/-06-/-June-/;s/-07-/-July-/;s/-08-/-August-/;s/-09-/-September-/;s/-10-/-October-/;s/-11-/-November-/;s/-12-/-December-/;s/\(.*\)-\(.*\)-\(.*\)/\3 \2 \1/'` ; sed <lsub.man >lsub.8 "s/@TODAY@/$M/;s/@VERSION@/ubutils-1.0.1/;s#@IDSDIR@#/usr/share/hwdata#"
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
* Fri Aug 28 2026 zhao-lichang <zhaolichang@huawei.com> - 1.0.2-7
- ub:ubutils: Change ubutils version
- ub:ubutils: Change ubutils version and fix setub write

* Wed May 20 2026 laz <lianzhe1@h-partners.com> - 1.0.2-6
- Change source package name

* Fri Mar 20 2026 Jianquan Lin <linjianquan2@huawei.com> - 1.0.2-5
- Change some code format

* Tue Mar 10 2026 Jianquan Lin <linjianquan2@huawei.com> - 1.0.2-4
- Resubmit "Delete mode number for FEC"

* Tue Mar 10 2026 Jianquan Lin <linjianquan2@huawei.com> - 1.0.2-3
- Revert "Delete mode number for FEC"

* Sat Jan 31 2026 laz <lianzhe1@h-partners.com> - 1.0.2-2
- Delete mode number for FEC

* Wed Dec 24 2025 laz <lianzhe1@h-partners.com> - 1.0.2-1
- Change lsub print format.

* Tue Nov 4 2025 laz <lianzhe1@h-partners.com> - 1.0.1.rc1-1
- Add ubutils document and fix setub write.

* Tue Aug 12 2025 laz <lianzhe1@h-partners.com> - 1.0.0-1
- Support the basic debug tool(Ubutils) of ubus, including setub, lsub and ub.ids.
