# Realtek RTL8852AU USB Wi-Fi adapter – akmod packaging for Fedora / Bazzite

# This spec file packages the driver contained in this very repository as an
# akmod so that immutable Fedora variants (Silverblue, Bazzite, Aurora, …)
# can build and load the module automatically for every kernel update.

%global kmod_name        rtl8852au

# Pin to a known-good commit (HEAD at creation time). Update to pull newer
# driver revisions.
%global up_commit        865ab0fa91471d595c283d2f3db323f7f15455f5
%global up_version       1

Name:           akmod-%{kmod_name}
Version:        %{up_version}
Release:        1%{?dist}
Summary:        Realtek RTL8852AU USB Wi-Fi driver (akmod)

License:        GPLv2
URL:            https://github.com/GiveMeDaTaco/rtl8852au
Source0:        %{url}/archive/%{up_commit}/%{kmod_name}-%{up_commit}.tar.gz

# Build deps for an out-of-tree kernel module
BuildRequires:  akmods >= 0.5
BuildRequires:  kmodtool gcc make elfutils-libelf-devel
BuildRequires:  kernel-devel kernel-headers

%description
Akmod package that builds the `%{kmod_name}` (`8852au.ko`) kernel module for
Realtek RTL8852AU adapters on Fedora-based immutable systems.  `akmods` will
rebuild the module automatically after every kernel update.

%prep
%autosetup -n %{kmod_name}-%{up_commit}

%build
%{akmod_build}

%install
%{akmod_install}

%files
%{akmod_files}

%changelog
* Fri Aug 22 2025 Your Name <you@example.com> - 1-1
- Initial akmod packaging for rtl8852au
