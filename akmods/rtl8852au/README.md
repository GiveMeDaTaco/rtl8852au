# rtl8852au – Realtek RTL8852AU USB Wi-Fi adapter (akmods package)

This directory contains the **akmod** packaging files that allow the
`rtl8852au` out-of-tree kernel module to be built automatically on
Fedora-family immutable operating systems such as Silverblue, Bazzite and
Aurora.

## How it works

1. The accompanying `akmod-rtl8852au.spec` file fetches a fixed upstream
   commit of the driver from GitHub and uses the Fedora `akmods` macros to
   build a `kmod-rtl8852au` RPM for the currently running kernel.
2. The GitHub Actions workflow shipped at the repository root (inherited
   from `ublue-os/akmods`) pre-builds and caches the resulting module for
   every kernel variant that Universal Blue publishes.
3. The produced container image (e.g. `ghcr.io/<user>/akmods:rtl8852au-f41`)
   can then be consumed by a custom Bazzite image via the *bluebuild*
   `akmods` module type.

## Updating the driver

If you need a newer driver revision, bump the `%global up_commit` value in
`akmod-rtl8852au.spec`, optionally increment `%{?release}`, run

```bash
spectool -g -R akmod-rtl8852au.spec
```

to refresh the `sources` file, then commit & push.

## Local test build

```bash
sudo dnf install fedpkg rpmdevtools @development-tools
fedpkg --release rawhide srpm      # produces an SRPM
mockbuild path/to/*.src.rpm         # or `fedpkg mockbuild` if configured
```

---

*Maintained by <your name>.*
