# Realtek RTL8852AU USB Wi-Fi adapter – akmod packaging for Fedora / Bazzite

# This spec file follows the pattern used in the upstream
# https://github.com/ublue-os/akmods repository.  It deliberately contains
# only the metadata and build/install macros; the full driver sources are
# fetched as an external tarball so that the resulting SRPM remains small
# and reproducible.

%global kmod_name        rtl8852au

# Pin to a known-good upstream commit to make builds reproducible.  Update
# this when you want to pull newer driver changes.
%global up_commit        865ab0fa91471d595c283d2f3db323f7f15455f5
# The driver project does not tag formal releases; we expose a fake version
# constant.  Only bump it when the exported kernel interface changes in an
# incompatible way – otherwise just update the commit hash & Release.
%global up_version       1

Name:           akmod-%{kmod_name}
Version:        %{up_version}
Release:        1%{?dist}
Summary:        Realtek RTL8852AU USB Wi-Fi driver (akmod)

License:        GPLv2
URL:            https://github.com/lwfinger/rtl8852au
Source0:        %{url}/archive/%{up_commit}/%{kmod_name}-%{up_commit}.tar.gz

#---- build requirements ------------------------------------------------------
BuildRequires:  akmods >= 0.5
BuildRequires:  kmodtool
BuildRequires:  gcc make elfutils-libelf-devel
BuildRequires:  kernel-devel kernel-headers

#---- description -------------------------------------------------------------
%description
Akmod package that builds the out-of-tree `%{kmod_name}` kernel module
(`8852au.ko`) for Realtek RTL8852AU wireless adapters on Fedora-family
immutable images such as Silverblue, Bazzite and Aurora.  The module is
automatically rebuilt by `akmods` whenever the kernel is updated.

#-------------------------------------------------------------------------------
# prep / build / install – leverage akmods helper macros
#-------------------------------------------------------------------------------

%prep
%autosetup -n %{kmod_name}-%{up_commit}

%build
# The akmods macro runs the standard kmodtool logic and prepares the kABI
# compatible sub-RPMs.
%{akmod_build}

%install
%{akmod_install}

#-------------------------------------------------------------------------------
# files / changelog
#-------------------------------------------------------------------------------

%files
%{akmod_files}

%changelog
* Fri Aug 22 2025 Your Name <you@example.com> - 1-1
- Initial Fedora akmod packaging for rtl8852au
