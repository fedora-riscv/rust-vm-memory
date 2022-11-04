# Generated by rust2rpm 23
%bcond_without check
%global debug_package %{nil}

%global crate vm-memory

Name:           rust-vm-memory
Version:        0.8.0
Release:        3%{?dist}
Summary:        Safe abstractions for accessing the VM physical memory

License:        Apache-2.0 OR BSD-3-Clause
URL:            https://crates.io/crates/vm-memory
Source:         %{crates_source}
# Automatically generated patch to strip foreign dependencies
Patch:          vm-memory-fix-metadata-auto.diff
# Manually created patch for downstream crate metadata changes
# * drop unused, benchmark-only criterion dev-dependency to speed up builds
Patch:          vm-memory-fix-metadata.diff
# Enable 64 bit atomics on ppc64le and s390x
# https://github.com/rust-vmm/vm-memory/pull/198
Patch:          vm-memory-fix-atomics.diff

# vm-memory does not support 32 bit targets
ExcludeArch:    i686

BuildRequires:  rust-packaging >= 21

%global _description %{expand:
Safe abstractions for accessing the VM physical memory.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%license %{crate_instdir}/LICENSE-APACHE
%license %{crate_instdir}/LICENSE-BSD-3-Clause
%doc %{crate_instdir}/CHANGELOG.md
%doc %{crate_instdir}/DESIGN.md
%doc %{crate_instdir}/README.md
%doc %{crate_instdir}/TODO.md
%{crate_instdir}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+arc-swap-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+arc-swap-devel %{_description}

This package contains library source intended for building other packages which
use the "arc-swap" feature of the "%{crate}" crate.

%files       -n %{name}+arc-swap-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+backend-atomic-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+backend-atomic-devel %{_description}

This package contains library source intended for building other packages which
use the "backend-atomic" feature of the "%{crate}" crate.

%files       -n %{name}+backend-atomic-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+backend-bitmap-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+backend-bitmap-devel %{_description}

This package contains library source intended for building other packages which
use the "backend-bitmap" feature of the "%{crate}" crate.

%files       -n %{name}+backend-bitmap-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+backend-mmap-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+backend-mmap-devel %{_description}

This package contains library source intended for building other packages which
use the "backend-mmap" feature of the "%{crate}" crate.

%files       -n %{name}+backend-mmap-devel
%ghost %{crate_instdir}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif

%changelog
* Fri Nov 04 2022 Fabio Valentini <decathorpe@gmail.com> - 0.8.0-3
- Drop unused, benchmark-only criterion dev-dependency.
- Regenerate with rust2rpm 23.

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue May 31 2022 Sergio Lopez <slp@redhat.com> - 0.8.0-1
- Update to 0.8.0
- Enable tests now that BZ#1902663 is fixed
- Enable all rust_arches except i686 (32 bits targets are not supported)

* Thu Mar 03 2022 Sergio Lopez <slp@redhat.com> - 0.7.0-4
- Add missing rust-vm-memory+backend-bitmap-devel subpackage

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Dec 24 2021 Sergio Lopez <slp@redhat.com> - 0.7.0-1
- Update to 0.7.0

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon May 03 2021 Sergio Lopez <slp@redhat.com> - 0.5.0-1
- Initial package
