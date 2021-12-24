# Generated by rust2rpm 17

# We need to disable tests until BZ#1902663 is fixed
# % bcond_without check
%bcond_with check

%global debug_package %{nil}

%global crate vm-memory

Name:           rust-%{crate}
Version:        0.7.0
Release:        2%{?dist}
Summary:        Safe abstractions for accessing the VM physical memory

# Upstream license specification: Apache-2.0 OR BSD-3-Clause
License:        ASL 2.0 or BSD
URL:            https://crates.io/crates/vm-memory
Source:         %{crates_source}
# Initial patched metadata
# * No windows
# * Exclude unneeded files
Patch0:         vm-memory-fix-metadata.diff

ExclusiveArch:  x86_64 aarch64 ppc64le
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Safe abstractions for accessing the VM physical memory.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE-APACHE LICENSE-BSD-3-Clause
%doc README.md
%{cargo_registry}/%{crate}-%{version_no_tilde}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+arc-swap-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+arc-swap-devel %{_description}

This package contains library source intended for building other packages
which use "arc-swap" feature of "%{crate}" crate.

%files       -n %{name}+arc-swap-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+backend-atomic-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+backend-atomic-devel %{_description}

This package contains library source intended for building other packages
which use "backend-atomic" feature of "%{crate}" crate.

%files       -n %{name}+backend-atomic-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+backend-mmap-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+backend-mmap-devel %{_description}

This package contains library source intended for building other packages
which use "backend-mmap" feature of "%{crate}" crate.

%files       -n %{name}+backend-mmap-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

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
* Fri Dec 24 2021 Sergio Lopez <slp@redhat.com> - 0.7.0-1
- Update to 0.7.0

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon May 03 2021 Sergio Lopez <slp@redhat.com> - 0.5.0-1
- Initial package
