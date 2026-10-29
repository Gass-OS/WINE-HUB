<div align="center">

# 🥃 WINE-HUB

### Windows apps and games on Android

**An experimental Gass-OS project exploring Windows compatibility on Android ARM64.**

[![Build APK](https://github.com/Gass-OS/WINE-HUB/actions/workflows/winehub-build.yml/badge.svg?branch=main)](https://github.com/Gass-OS/WINE-HUB/actions/workflows/winehub-build.yml)
[![Android ARM64](https://img.shields.io/badge/Platform-Android%20ARM64-3DDC84?style=flat-square&logo=android&logoColor=white)](https://github.com/Gass-OS/WINE-HUB)
[![Experimental](https://img.shields.io/badge/Status-Experimental-orange?style=flat-square)](https://github.com/Gass-OS/WINE-HUB)
[![Gass-OS](https://img.shields.io/badge/Project-Gass--OS-182848?style=flat-square&logo=github)](https://github.com/Gass-OS)

</div>

---

## ✨ About WINE-HUB

**WINE-HUB** is an experimental Android application project maintained by [Gass-OS](https://github.com/Gass-OS).

The project is based on [Winlator by Bruno](https://github.com/brunodev85/winlator), with a separate application identity and a dedicated build workflow.

Our goal is to explore running Windows applications and games on Android ARM64 using technologies such as Wine, Box64 and graphics translation layers.

> **Transparency:** WINE-HUB is currently a downstream customization of Winlator. It is not a new Wine implementation or a replacement compatibility engine. Credit remains with the original developers and all third-party projects.

## 🚧 Project status

- [x] Create the public Gass-OS repository
- [x] Add a dedicated Android APK build workflow
- [x] Configure the WINE-HUB application identity in CI
- [ ] Verify the first successful APK build
- [ ] Install and test on physical Android hardware
- [ ] Document tested devices and application compatibility
- [ ] Publish a tested release

Compatibility, stability and GPU acceleration must be tested before they can be claimed as working.

## 📦 Download and test

**Experimental builds:**  
[Open WINE-HUB GitHub Actions](https://github.com/Gass-OS/WINE-HUB/actions/workflows/winehub-build.yml)

1. Open a successful workflow run.
2. Download the `WINE-HUB-debug-ARM64` artifact.
3. Extract the downloaded ZIP archive.
4. Install the APK on a compatible Android device.

Debug artifacts are intended for testing and may expire. Check the [Releases page](https://github.com/Gass-OS/WINE-HUB/releases) for published releases. No stable release is promised yet.

## 🛠️ Build system

The GitHub Actions workflow checks out the source and submodules, applies the WINE-HUB application ID and app name, and builds an Android debug APK for `arm64-v8a`.

A successful compilation does not automatically mean every Windows application works or that hardware acceleration is enabled.

## 🧩 Technologies and credits

WINE-HUB builds on the work of many open-source developers and projects:

- [Winlator](https://github.com/brunodev85/winlator) — upstream Android application
- [Wine](https://www.winehq.org/) — Windows compatibility layer
- [Box64](https://github.com/ptitSeb/box64) — x86-64 application translation
- [Mesa](https://www.mesa3d.org/) — graphics drivers and translation technologies
- [DXVK](https://github.com/doitsujin/dxvk) — Direct3D 9/10/11 over Vulkan
- [VKD3D](https://gitlab.winehq.org/wine/vkd3d) — Direct3D 12 translation
- Other bundled components and submodules, credited in their respective upstream projects.

Please consult each project for its complete credits and license terms.

## 🐛 Bug reports

When reporting an issue, include:

- Android device model and Android version
- WINE-HUB build or workflow run
- Application or game being tested
- Steps to reproduce the issue
- Relevant logs or screenshots

## 📜 Licensing and attribution

WINE-HUB incorporates Winlator and other third-party software. Original copyright notices, license files and required attributions must be preserved. Individual components may have different redistribution requirements.

Review the relevant licenses before distributing modified source or APKs.

---

<div align="center">

**WINE-HUB**  
An experimental project by [Gass-OS](https://github.com/Gass-OS)

*Built on open-source work. Respecting the people behind it.*

</div>
