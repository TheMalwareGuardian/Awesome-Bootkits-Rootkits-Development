# Awesome Bootkits & Rootkits Development

A curated compilation of extensive resources dedicated to bootkit and rootkit development.

Discover more awesome lists at [sindresorhus/awesome](https://github.com/sindresorhus/awesome).

<p align="center">
  <img src="images/Logo.png">
</p>

## ***Table of Contents***
- [UEFI](#uefi)
- [Bootkits](#bootkits)
- [Windows](#windows)
- [Rootkits](#rootkits)
- [Books](#books)
- [Awesome](#awesome)
- [Master's Degree](#mastersdegree)



<div id='uefi'/>

## ***UEFI***


<div id='uefi-basics'/>

### ***Basics***

* [Web UEFI: UEFI Specifications](https://uefi.org/specifications)
* [Web UEFI: UEFI Specification Version 2.10](https://uefi.org/specs/UEFI/2.10/) -> This Unified Extensible Firmware Interface (UEFI) Specification describes an interface between the operating system (OS) and the platform firmware.
* [Web UEFI: UEFI Platform Initialization Specification 1.8](https://uefi.org/specs/PI/1.8/) -> This specification defines the core code and services that are required for an implementation of the Pre-EFI Initialization (PEI) phase of the Platform Initialization (PI) specifications (hereafter referred to as the “PI Architecture”).
* [Web OsDev: UEFI](https://wiki.osdev.org/UEFI)
* [Web Wikipedia: Booting Sequence](https://en.wikipedia.org/wiki/Booting#Boot_sequence)


<div id='uefi-videos'/>

### ***Videos***

* [Youtube Video: BIOS and UEFI As Fast As Possible](https://www.youtube.com/watch?v=zIYkol851dU) -> What fundamental things does a computer BIOS do, and what are the important differences between the traditional BIOS and the newer UEFI?
* [Youtube Video: BIOS, CMOS, UEFI](https://www.youtube.com/watch?v=LGz0Io_dh_I) -> This video explains the difference between the BIOS, CMOS, and UEFI.  It also explains what the purpose of the CMOS battery.  What is the BIOS?  What is UEFI?  What is CMOS?
* [Youtube Video: PC BIOS Settings](https://www.youtube.com/watch?v=ezubjTO7rRI&t=10s) -> BIOS / UEFI settings, including boot options, secure boot, enabling XMP memory profiles, and BIOS passwords. Also information on the differences between a legacy BIOS and a UEFI BIOS, and how to enter the BIOS.
* [Youtube Video: ThatOsDev - EFI based Bootloader](https://www.youtube.com/watch?v=_98PUTJc9Yk&list=PLwH94sFU_ljPi2ClIcWIvuc1GdLT81uuH&index=4) -> EFI Explained.
* [Youtube Video: UEFIForum - Best Practices for UEFI Secure Boot Customization](https://www.youtube.com/watch?v=WBemkwMHLJM) -> UEFI Secure Boot helps provide an effective defense against boot malware, but following today’s best practices in its implementation, deployment and configurability can help its increase its effectiveness against increasingly sophisticated exploits.


<div id='uefi-attacks'/>

### ***Attacks***


<div id='uefi-attacks-videos'/>

#### ***Videos***

* [Youtube Video: BlackHat USA 2009 - Attacking Intel Bios](https://www.youtube.com/watch?v=CRjcKv-xiqw) -> We demonstrate how to permanently reflash Intel BIOSes on the latest Intel Q45-based systems. In contrast to a previous work done by other researches a few months earlier, who targeted totally unprotected low-end BIOSes, we focus on how to permanently reflash one of the most secure BIOSes out there, that normally only allow a vendor's digitally signed firmware to be flashed.
* [Youtube Video: REcon 2015 - Attacking and Defending BIOS](https://www.youtube.com/watch?v=rGkymhurzM8)
* [Youtube Video: Defcon 22 - Summary of Attacks Against BIOS](https://www.youtube.com/watch?v=QDSlWa9xQuA) -> A variety of attacks targeting platform firmware have been discussed publicly, drawing attention to the pre-boot and firmware components of the platform such as secure boot, OS loaders, and SMM. Windows 8 Secure Boot provides an important protection against bootkits by enforcing a signature check on each boot component.
* [Youtube Video: BlackHat USA 2017 - Betraying the BIOS, Where the Guardians of the BIOS are Failing](https://www.youtube.com/watch?v=Dfl2JI2eLc8) -> For UEFI firmware, the barbarians are at the gate -- and the gate is open. On the one hand, well-intentioned researchers are increasingly active in the UEFI security space; on the other hand, so are attackers. Information about UEFI implants -- by HackingTeam and state-sponsored actors alike -- hints at the magnitude of the problem, but are these isolated incidents, or are they indicative of a more dire lapse in security? 


<div id='uefi-attacks-presentations'/>

#### ***Presentations***

* [Presentation: BlackHat USA 2009 - Attacking Intel Bios](https://www.blackhat.com/presentations/bh-usa-09/WOJTCZUK/BHUSA09-Wojtczuk-AtkIntelBios-SLIDES.pdf) -> We demonstrate how to permanently reflash Intel BIOSes on the latest Intel Q45-based systems. In contrast to a previous work done by other researches a few months earlier, who targeted totally unprotected low-end BIOSes, we focus on how to permanently reflash one of the most secure BIOSes out there, that normally only allow a vendor's digitally signed firmware to be flashed.
* [Presentation: REcon 2015 - Attacking and Defending BIOS](https://recon.cx/2015/slides/recon2015-09-yuriy-bulygin-oleksandr-bazhaniuk-Attacking-and-Defending-BIOS-in-2015.pdf)
* [Presentation: Defcon 22 - Summary of Attacks Against BIOS](https://defcon.org/images/defcon-22/dc-22-presentations/Bulygin-Bazhaniul-Furtak-Loucaides/DEFCON-22-Bulygin-Bazhaniul-Furtak-Loucaides-Summary-of-attacks-against-BIOS-UPDATED.pdf) -> A variety of attacks targeting platform firmware have been discussed publicly, drawing attention to the pre-boot and firmware components of the platform such as secure boot, OS loaders, and SMM. Windows 8 Secure Boot provides an important protection against bootkits by enforcing a signature check on each boot component.
* [Presentation: BlackHat USA 2017 - Betraying the BIOS, Where the Guardians of the BIOS are Failing](https://www.blackhat.com/docs/us-17/wednesday/us-17-Matrosov-Betraying-The-BIOS-Where-The-Guardians-Of-The-BIOS-Are-Failing.pdf) -> For UEFI firmware, the barbarians are at the gate -- and the gate is open. On the one hand, well-intentioned researchers are increasingly active in the UEFI security space; on the other hand, so are attackers. Information about UEFI implants -- by HackingTeam and state-sponsored actors alike -- hints at the magnitude of the problem, but are these isolated incidents, or are they indicative of a more dire lapse in security? 


<div id='uefi-edk2'/>

### ***EDK2***


<div id='uefi-edk2-basics'/>

#### ***Basics***

* [Github: EDK II Project](https://github.com/tianocore/edk2) -> A modern, feature-rich, cross-platform firmware development environment for the UEFI and PI specifications from www.uefi.org.


<div id='uefi-edk2-videos'/>

#### ***Videos***

* [Youtube Video: UEFIForum - Driver Development with EDKII](https://www.youtube.com/watch?v=PX4HaWQNrlo) -> The world of UEFI is unlike OS-based software ecosystems in several aspects and the difference can be daunting to a developer who is starting to write UEFI device drivers.


<div id='uefi-edk2-develop'/>

#### ***Develop***

* [Github: Getting Started with EDK II](https://github.com/tianocore/tianocore.github.io/wiki/Getting-Started-with-EDK-II) -> Steps for downloading EDK II from GitHub and compiling projects under various OS/compiler environments.
* [Web Basic Input/Output: "Hello World" Quick Start with EDK II](https://www.basicinputoutput.com/2019/10/hello-world-quick-start-with-edk2.html) -> Setup the EDK on a system and configure it to build a basic "Hello, World" type program.
* [Github: Getting Started Writing Simple Application with EDK II](https://github.com/tianocore/tianocore.github.io/wiki/Getting-Started-Writing-Simple-Application)
* [Github: VisualUEFI](https://github.com/ionescu007/VisualUefi) -> A Solution and set of Visual Studio Project Files to allow building the official EDK-II without the use of inf files and other build tools.



<div id='bootkits'/>

## ***Bootkits***


<div id='bootkits-basics'/>

### ***Basics***

* [Web CrowdStrike: Bootkit](https://www.crowdstrike.com/cybersecurity-101/malware/bootkit/) -> Definition, Prevention, and Removal
* [Blog: Bootkitting Windows Sandbox](https://secret.club/2022/08/29/bootkitting-windows-sandbox.html)


<div id='bootkits-videos'/>

### ***Videos***

* [Youtube Video: BlackHat USA 2013 - Detecting OSX and Windows bootkits with RDFU](https://www.youtube.com/watch?v=7UsdRzsue-g) -> UEFI has recently become a very public target for rootkits and malware. To combat this new threat, we developed a Rootkit Detection Framework for UEFI ("RDFU") that incorporates a unified set of tools that address this problem across a wide spectrum of UEFI implementations.
* [Youtube Video: Virus Bulletin 2014 - Bootkits past, present & future](https://www.youtube.com/watch?v=jN34P4EdIUw) -> Bootkit threats have always been a powerful weapon in the hands of cybercriminals, allowing them to establish persistent and stealthy presence in their victims' systems. The most recent notable spike in bootkit infections was associated with attacks on 64-bit versions of the Microsoft Windows platform, which restrict the loading of unsigned kernel-mode drivers. However, these bootkits aren't effective against UEFI-based platforms. So, are UEFI-based machines immune against bootkit threats (or would they be)?
* [Youtube Video: BlackHat USA 2014 - Exposing Bootkits with BIOS Emulation](https://www.youtube.com/watch?v=siMj4bFx5nI) -> Stealth and persistency are invaluable assets to an intruder. You cannot defend against what you cannot see. This talk discusses techniques to counter attempts at subverting modern security features, and regain control of compromised machines, by drilling down deep into internal structures of the operating system to battle the threat of bootkits.
* [Youtube Video:  Nullcon 2022 - A UEFI firmware bootkit in the wild](https://www.youtube.com/watch?v=lSpOFUCzFdk) -> Despite the advanced capabilities they provide, low-level implants such as bootkits and rootkits are only deployed by the most sophisticated attackers due to the risk they pose to the victim system’s stability. In recent years, Kaspersky has however observed a number of new low-level malware, such as MosaicRegressor, MoonBounce, and the object of this talk, CosmicStrand.
* [Youtube Video:  OffensiveCon18 - Alex Ionescu Advancing the State of UEFI Bootkits](https://www.youtube.com/watch?v=dpG97TBR3Ys) -> Persistence in the Age of PatchGuard and Windows 10.


<div id='bootkits-presentations'/>

### ***Presentations***

* [Presentation: BlackHat USA 2013 - Detecting OSX and Windows bootkits with RDFU](https://cdn2.hubspot.net/hubfs/3375217/Reversing_Labs_November%202018/File/Presentation-BlackHat-Vegas-2013.pdf) -> UEFI has recently become a very public target for rootkits and malware. To combat this new threat, we developed a Rootkit Detection Framework for UEFI ("RDFU") that incorporates a unified set of tools that address this problem across a wide spectrum of UEFI implementations.
* [Paper: Virus Bulletin 2014 - Bootkits past, present & future](https://www.virusbulletin.com/virusbulletin/2014/11/paper-bootkits-past-present-amp-future) -> Bootkit threats have always been a powerful weapon in the hands of cybercriminals, allowing them to establish persistent and stealthy presence in their victims' systems. The most recent notable spike in bootkit infections was associated with attacks on 64-bit versions of the Microsoft Windows platform, which restrict the loading of unsigned kernel-mode drivers. However, these bootkits aren't effective against UEFI-based platforms. So, are UEFI-based machines immune against bootkit threats (or would they be)?
* [Paper: BlackHat USA 2014 - Exposing Bootkits with BIOS Emulation](https://www.blackhat.com/docs/us-14/materials/us-14-Haukli-Exposing-Bootkits-With-BIOS-Emulation-WP.pdf) -> Stealth and persistency are invaluable assets to an intruder. You cannot defend against what you cannot see. This talk discusses techniques to counter attempts at subverting modern security features, and regain control of compromised machines, by drilling down deep into internal structures of the operating system to battle the threat of bootkits.
* [Presentation:  OffensiveCon18 - Alex Ionescu Advancing the State of UEFI Bootkits](http://publications.alex-ionescu.com/OffensiveCon/OffensiveCon%202018%20-%20Advancing%20the%20state%20of%20UEFI%20Boot%20Kits.pdf) -> Persistence in the Age of PatchGuard and Windows 10.


<div id='bootkits-analysis'/>

### ***Analysis***

* [Web WeLiveSecurity: UEFI threats moving to the ESP](https://www.welivesecurity.com/2021/10/05/uefi-threats-moving-esp-introducing-especter-bootkit/) -> Introducing ESPecter bootkit
* [Web WeLiveSecurity: BlackLotus UEFI bootkit](https://www.welivesecurity.com/2023/03/01/blacklotus-uefi-bootkit-myth-confirmed/) -> The first in-the-wild UEFI bootkit bypassing UEFI Secure Boot on fully updated UEFI systems is now a reality


<div id='bootkits-examples'/>

### ***Examples***

* [Github: BlackLotus](https://github.com/ldpreload/BlackLotus) -> innovative UEFI Bootkit designed specifically for Windows. It incorporates a built-in Secure Boot bypass and Ring0/Kernel protection to safeguard against any attempts at removal. This software serves the purpose of functioning as an HTTP Loader.
* [Github: EfiGuard](https://github.com/Mattiwatti/EfiGuard) -> Portable x64 UEFI bootkit that patches the Windows boot manager, boot loader and kernel at boot time in order to disable PatchGuard and Driver Signature Enforcement (DSE).
* [Github: Bootlicker](https://github.com/realoriginal/bootlicker) -> A generic UEFI bootkit used to achieve initial usermode execution.
* [Github: DmaBackdoorBoot](https://github.com/Cr4sh/s6_pcie_microblaze/tree/master/python/payloads/DmaBackdoorBoot) -> UEFI DXE driver intended for executing of kernel mode and user mode payloads under the Windows operating system by having an arbitrary code execution at early boot stage during DXE phase of the platform initialization.
* [Github: RedLotus](https://github.com/memN0ps/bootkit-rs) -> Windows UEFI Bootkit in Rust designed to facilitate the manual mapping of a driver manual mapper before the kernel (ntoskrnl.exe) is loaded, effectively bypassing Driver Signature Enforcement (DSE).
* [Github: Bootkit Showcase](https://github.com/hardenedvault/bootkit-samples) -> Real-World Examples of Infrastructure Security Threats
* [Github: SandboxBootkit](https://github.com/thesecretclub/SandboxBootkit) -> Bootkit tested on Windows Sandbox to patch ntoskrnl.exe and disable DSE/PatchGuard.
* [Github: Umap](https://github.com/btbd/umap/) -> Windows UEFI bootkit that loads a generic driver manual mapper without using a UEFI runtime driver.
* [Github: UEFI-Bootkit](https://github.com/ajkhoury/UEFI-Bootkit) -> A small bootkit designed to use zero assembly.
* [Github: PeiBackdoor](https://github.com/Cr4sh/PeiBackdoor) -> This project implements early stage firmware backdoor for UEFI based firmware. It allows to execute arbitrary code written in C during Pre EFI Init (PEI) phase of Platform Initialization (PI).
* [Github: Rovnix](https://github.com/m0n0ph1/Win64-Rovnix-VBR-Bootkit) -> Volume Boot Record Bootkit.
* [Github: Dreamboot](https://github.com/quarkslab/dreamboot) -> UEFI bootkit.



<div id='windows'/>

## ***Windows***


<div id='windows-boot'/>

### ***Boot***


<div id='windows-boot-basics'/>

#### ***Basics***

* [Presentation: UEFI Plugfest - Windows Boot Environment](https://uefi.org/sites/default/files/resources/UEFI-Plugfest-WindowsBootEnvironment.pdf) -> High-level description of Windows boot process and Windows UEFI services usage.
* [Microsoft: Secure the Windows boot process](https://learn.microsoft.com/en-us/windows/security/operating-system-security/system-security/secure-the-windows-10-boot-process) -> Windows has many features to help protect you from malware, and it does an amazingly good job.


<div id='windows-boot-videos'/>

#### ***Videos***

* [Youtube Video: Boot Up with Confidence Windows 10/11 Secure Boot Demystified](https://www.youtube.com/watch?v=ZF1xGdhyUyw&t=45s) -> How secure boot works in Windows 10/11. Secure boot allows protection from "root-kit" attacks on both clients and servers.
* [Youtube Video: Compare Windows 7 and Windows 8-10 boot process](https://www.youtube.com/watch?v=_DQlaFUhCyM) -> A comparison of the boot process of Windows 7 and Windows 8/10.


<div id='windows-kernel'/>

### ***Kernel***

* [Web RedTeamNotes: Internals](https://www.ired.team/miscellaneous-reversing-forensics/windows-kernel-internals)
* [Web CodeMachine: Windows kernel data structures](https://codemachine.com/articles/kernel_structures.html) -> Catalog of key Windows kernel data structures.
* [Web Vergilius: Windows kernel](https://www.vergiliusproject.com/) -> Take a look into the depths of Windows kernels and reveal more than 60000 undocumented structures.
* [Web Geoff Chappell: Windows kernel](https://www.geoffchappell.com/)


<div id='windows-drivers'/>

### ***Drivers***


<div id='windows-drivers-basics'/>

#### ***Basics***

* [Microsoft: Get started with drivers on Windows](https://learn.microsoft.com/en-us/windows-hardware/drivers/gettingstarted/) -> General overview of Windows components, types of device drivers used in Windows, goals of Windows device drivers, generic sample device drivers.
* [Microsoft: Kernel-Mode Driver Architecture Design Guide](https://learn.microsoft.com/en-us/windows-hardware/drivers/kernel/) -> This section includes general concepts to help you understand kernel-mode programming and describes specific techniques of kernel programming.
* [Github: Windows driver samples](https://github.com/Microsoft/Windows-driver-samples) -> This repo contains driver samples prepared for use with Microsoft Visual Studio and the Windows Driver Kit (WDK). It contains both Universal Windows Driver and desktop-only driver samples.


<div id='windows-drivers-environment'/>

#### ***Environment***

* [Microsoft: Windows Driver Kit (WDK)](https://learn.microsoft.com/en-us/windows-hardware/drivers/other-wdk-downloads) -> This is used to develop, test, and deploy Windows Drivers.
* [Microsoft: DebugView](https://learn.microsoft.com/en-us/sysinternals/downloads/debugview) -> It is an application that lets you monitor debug output on your local system, or any computer on the network that you can reach via TCP/IP. It is capable of displaying both kernel-mode and Win32 debug output, so you don't need a debugger to catch the debug output your applications or device drivers generate, nor do you need to modify your applications or drivers to use non-standard debug output APIs.


<div id='windows-drivers-develop'/>

#### ***Develop***

* [Microsoft: Write a Hello World Windows Driver (KMDF)](https://learn.microsoft.com/en-us/windows-hardware/drivers/gettingstarted/writing-a-very-small-kmdf--driver) -> This article describes how to write a small Universal Windows driver using Kernel-Mode Driver Framework (KMDF) and then deploy and install your driver on a separate computer.
* [Microsoft: Development & Demo of Windows Kernel Driver](https://apchavan.medium.com/development-demo-of-windows-kernel-driver-47fc2150e128) -> The Kernel mode driver can run in highest privileged ring 0. It means the kernel driver mostly have highest level of permissions (like kernel) while executing.
* [Microsoft: DriverEntry for WDF Drivers routine](https://learn.microsoft.com/en-us/windows-hardware/drivers/wdf/driverentry-for-kmdf-drivers) -> DriverEntry is the first driver-supplied routine that is called after a driver is loaded. It is responsible for initializing the driver.
* [Microsoft: DriverUnload callback function](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_unload) -> The Unload routine performs any operations that are necessary before the system unloads the driver.
* [Microsoft: Windows driver documentation](https://github.com/MicrosoftDocs/windows-driver-docs) -> The official Windows Driver Kit documentation sources.
* [GitHub: EDK II Driver Writer's Guide](https://github.com/tianocore-docs/edk2-UefiDriverWritersGuide/blob/master/EXAMPLES.md)
* [Course ZeroPointSecurity: Offensive Driver Development](https://training.zeropointsecurity.co.uk/courses/offensive-driver-development) -> Learn how to set up a development testing environment for writing Windows kernel-mode drivers using Hyper-V, WinDbg, and Visual Studio.  Cover the basic anatomy of a driver from loading and unloading, I/O control codes, interaction from userland, and kernel debugging.



<div id='windows-patchguard'/>

### ***PatchGuard***


<div id='windows-patchguard-basics'/>

#### ***Basics***

* [Web Windows-Internals: Secure Kernel Patch Guard](https://windows-internals.com/hyperguard-secure-kernel-patch-guard-part-1-skpg-initialization/) -> SKPG Initialization
* [Web Windows-Internals: Secure Kernel Patch Guard](https://windows-internals.com/hyperguard-secure-kernel-patch-guard-part-2-skpg-extents/) -> SKPG Extents


<div id='windows-patchguard-videos'/>

#### ***Videos***

* [Youtube Video: RSA Conference - Windows Kernel Patch Protection](https://www.youtube.com/watch?v=wXRLnp2JoWU) -> This session will look at a critical flaw in the design of Windows Kernel Patch Protection (PatchGuard), a system used to prevent modification to kernel code and other critical structure. The design of PatchGuard will be discussed, along with the design of an attack which uses the flaw in PatchGuard to disable the PatchGuard response entirely.


<div id='windows-patchguard-bypass'/>

#### ***Bypass***

* [Web Uninformed: Bypassing Patchguard on Windows](https://web.archive.org/web/20160817134601/http://uninformed.org/index.cgi?v=3&a=3&p=1)
* [GitHub: PatchGuardBypass](https://github.com/AdamOron/PatchGuardBypass) -> Bypassing PatchGuard on modern x64 systems.
* [Web CyberArk: GhostHook](https://www.cyberark.com/resources/threat-research-blog/ghosthook-bypassing-patchguard-with-processor-trace-based-hooking) -> Bypassing PatchGuard with Processor Trace Based Hooking.
* [GitHub: InfinityHook](https://github.com/everdox/InfinityHook) -> Kernel driver that will hook system calls.
* [Blog: New bypass disclosed in Microsoft PatchGuard (KPP)](https://www.zdnet.com/article/new-bypass-disclosed-in-microsoft-patchguard-kpp/) -> After GhostHook and InfinityHook, we now have ByePg.
* [Blog: ByePg](https://blog.can.ac/2019/10/19/byepg-defeating-patchguard-using-exception-hooking/) -> Defeating Patchguard Using Exception - Hooking.
* [Github: Shark](https://github.com/9176324/Shark) -> Turn off PatchGuard in real time for win7 (7600) ~ later.
* [Github: UPGDSED](https://github.com/hfiref0x/UPGDSED) -> Universal PatchGuard and Driver Signature Enforcement Disable.
* [Github: PgResarch](https://github.com/tandasat/PgResarch) -> PatchGuard Research.



<div id='rootkits'/>

## ***Rootkits***


<div id='rootkits-basics'/>

### ***Basics***

* [Web Kaspersky: What is a Rootkit?](https://www.kaspersky.com/resource-center/definitions/what-is-rootkit) -> Definition and Explanation
* [Web CyberArk: Fantastic Rootkits](https://www.cyberark.com/resources/threat-research-blog/fantastic-rootkits-and-where-to-find-them-part-1) -> Where to find them part 1
* [Web CyberArk: Fantastic Rootkits](https://www.cyberark.com/resources/threat-research-blog/fantastic-rootkits-and-where-to-find-them-part-2) -> Where to find them part 2
* [Web CyberArk: Fantastic Rootkits](https://www.cyberark.com/resources/threat-research-blog/fantastic-rootkits-and-where-to-find-them-part-3-arm-edition) -> Where to find them part 3 - ARM Edition
* [Web JumpSec Labs: A Defender's Guide For Rootkit Detection](https://labs.jumpsec.com/a-defenders-guide-for-rootkit-detection-episode-1-kernel-drivers/)
* [Web OpenSecurityTraining: Rootkits](https://opensecuritytraining.info/Rootkits_files/Rootkits-Part1.ppt.pdf) -> What they are and how to find them part 1
* [Web OpenSecurityTraining: Rootkits](https://opensecuritytraining.info/Rootkits_files/Rootkits-Part2.ppt.pdf) -> What they are and how to find them part 2
* [Web OpenSecurityTraining: Rootkits](https://opensecuritytraining.info/Rootkits_files/Rootkits-Part3.ppt.pdf) -> What they are and how to find them part 3
* [Web Gmer: Gmer](http://www.gmer.net/) -> It is an application that detects and removes rootkits.


<div id='rootkits-videos'/>

### ***Videos***

* [Youtube Video: GuidedHacking - How to make a Kernel Driver](https://www.youtube.com/watch?v=9h1FsOISwX0) -> This tutorial series will teach you everything you need to make a kernel driver on Windows.
* [Youtube Video: Sourcefire - Defense via Hook Detection](https://www.youtube.com/watch?v=CWZ-dShnBFA) -> Since both kernel-mode and user-mode rootkits use hooking as a vehicle for hiding their presence on a system, it seems only natural that looking for system hooks could itself be used to identify the presence of a rootkit on a system.
* [Youtube Video: Bsides Lisbon 2022 - Windows kernel rootkits for red teams](https://www.youtube.com/watch?v=GM9WQMrSkWk) -> In this talk, the focus is on key aspects of developing within the kernel environment, with a particular emphasis on considerations for creating malware targeting the Windows kernel.
* [Youtube Video: BlackHat USA 2020 - Demystifying Modern Windows Rootkits](https://www.youtube.com/watch?v=ZASsIpdumcY) -> This talk will demystify the process of writing a rootkit, moving past theory and instead walking the audience through the process of going from a driver that says "Hello World" to a driver that abuses never-before-seen hooking methods to control the user-mode network stack.
* [Youtube Video: BlackHat USA 2020 - The Art of Emulating Kernel Rootkits](https://www.youtube.com/watch?v=Zh_Dfd-ukEQ) -> Kernel rootkit is considered the most dangerous malware that may infect computers. Operating at ring 0, the highest privilege level in the system, this super malware has unrestricted power to control the whole machine, thus can defeat all the defensive and monitoring mechanisms.


<div id='rootkits-presentations'/>

### ***Presentations***

* [Presentation: Bsides Lisbon 2022 - Windows kernel rootkits for red teams](https://bsideslisbon.org/assets/2022/materials/Andre_Lima_Windows_Kernel_Rootkits.pdf) -> In this talk, the focus is on key aspects of developing within the kernel environment, with a particular emphasis on considerations for creating malware targeting the Windows kernel.
* [Presentation: BlackHat USA 2020 - Demystifying Modern Windows Rootkits](https://i.blackhat.com/USA-20/Wednesday/us-20-Demirkapi-Demystifying-Modern-Windows-Rootkits.pdf) -> This talk will demystify the process of writing a rootkit, moving past theory and instead walking the audience through the process of going from a driver that says "Hello World" to a driver that abuses never-before-seen hooking methods to control the user-mode network stack.


<div id='rootkits-examples'/>

### ***Examples***


<div id='rootkits-examples-generic'/>

#### ***Generic***

* [Github: Nidhogg](https://github.com/Idov31/Nidhogg) -> Multi-functional rootkit for red teams.
* [Github: Black Angel](https://github.com/XaFF-XaFF/Black-Angel-Rootkit) -> Windows 11/10 x64 kernel mode rootkit.
* [Github: Cronos](https://github.com/XaFF-XaFF/Cronos-Rootkit) -> Windows 10/11 x64 ring 0 rootkit
* [Github: Spectre](https://github.com/D4stiny/spectre) -> Windows kernel-mode rootkit that abuses legitimate communication channels to control a machine. Hiding Processes, token manipulation , hiding tcp network connections by port...
* [Blog: Eagle](https://memn0ps.github.io/rusty-windows-kernel-rootkit/) -> Windows Kernel Rookit in Rust.
* [Github: Eagle](https://github.com/memN0ps/rootkit-rs/) -> Windows Kernel Rookit in Rust.
* [Github: ZwHawk](https://github.com/eLoopWoo/zwhawk) -> A kernel rootkit with remote command and control interface for windows.
* [Github: www.rootkit.com mirror](https://github.com/skykami/www.rootkit.com) -> www.rootkit.com users section mirror, sql database dump, and a few other files/rootkits.
* [Github: TDL (Turla Driver Loader)](https://github.com/hfiref0x/TDL) -> Driver loader for bypassing Windows x64 Driver Signature Enforcement.
* [Github: Hooking)](https://github.com/alphaSeclab/hooking) -> Resources About Hooking. For All Platforms. Currently 300+ Tools And 600+ Posts.


<div id='rootkits-examples-dkom'/>

#### ***DKOM***


<div id='rootkits-examples-dkom-basics'/>

##### ***Basics***

* [Web RedTeamNotes: Manipulating ActiveProcessLinks to Hide Processes in Userland](https://www.ired.team/miscellaneous-reversing-forensics/windows-kernel-internals/manipulating-activeprocesslinks-to-unlink-processes-in-userland)
* [Youtube Video: Sourcefire - Direct Kernel Object Manipulation](https://www.youtube.com/watch?v=dUAV9Vrwkow)
* [Presentation: BlackHat USA 2004 - DKOM (Direct Kernel Object Manipulation)](https://www.blackhat.com/presentations/bh-europe-04/bh-eu-04-butler.pdf)
* [Web NixHacker: Understanding Windows DKOM techniques](https://nixhacker.com/understanding-windows-dkom-direct-kernel-object-manipulation-attacks-eprocess/) -> EPROCESS
* [Blog: Direct Kernel Object Manipulation and Processes](https://bsodtutorials.wordpress.com/2014/01/27/rootkits-direct-kernel-object-manipulation-and-processes/) -> DKOM is one of the methods commonly used and implemented by Rootkits, in order to remain undetected, since this the main purpose of a roottkit. To be able to access Kernel-Mode code and data structures without detection from security programs or tools used by security analysts and researchers. 


<div id='rootkits-examples-dkom-pocs'/>

##### ***POCs***

* [Github: DKOM](https://github.com/slava-aes/DKOM) -> Windows 10 Direct Kernel Object Manipulation.
* [Github: Win_Rootkit](https://github.com/alal4465/Win_Rootkit) -> A kernel-mode rootkit with remote control that utilizes C++ Runtime in it's driver. Uses DKOM and IRP Hooks.
* [Github: HideProcess](https://github.com/landhb/HideProcess) -> A basic Direct Kernel Object Manipulation rootkit that removes a process from the EPROCESS list, hiding it from the Task Manager.
* [Github: HideDriver](https://github.com/nbqofficial/HideDriver) -> Using DKOM to hide kernel mode drivers.
* [Github: Rootkit DKOM](https://github.com/YuriFA/DKOM) -> Direct Kernel Object Manipulationon _EPROCESS internal structure.


<div id='rootkits-examples-idthooking'/>

#### ***IDT Hooking***


<div id='rootkits-examples-idthooking-basics'/>

##### ***Basics***

* [Web RedTeamNotes: Interrupt Descriptor Table (IDT)](https://www.ired.team/miscellaneous-reversing-forensics/windows-kernel-internals/interrupt-descriptor-table-idt)
* [Web MIT: Interrupt Descriptor Table](https://pdos.csail.mit.edu/6.828/2008/readings/i386/s09_04.htm) -> The interrupt descriptor table (IDT) associates each interrupt or exception identifier with a descriptor for the instructions that service the associated event. Like the GDT and LDTs, the IDT is an array of 8-byte descriptors. Unlike the GDT and LDTs, the first entry of the IDT may contain a descriptor.
* [Youtube Video OpenSecurityTraining: Interrupt Descriptor Table](https://www.youtube.com/watch?v=cFdOJ6coVvQ)


<div id='rootkits-examples-idthooking-pocs'/>

##### ***POCs***

* [Github: Windows x86 Interrupt Descriptor Table (IDT) hooking driver](https://gist.github.com/Barakat/89002a26937a2da353868fc5130812a5)
* [Github: IDTHOOK](https://github.com/LLLZed/IDTHOOK)
* [Github: x64-IDT-HOOK](https://github.com/haidragon/x64-IDT-HOOK)
* [Github: IDTHook_X64](https://github.com/DOGSHITD/IDTHook_X64) - > Hook IDT vector 0xb2 to detect SCI in 64bit windows. 


<div id='rootkits-examples-ssdthooking'/>

#### ***SSDT Hooking***


<div id='rootkits-examples-ssdthooking-basics'/>

##### ***Basics***

* [Web RedTeamNotes: System Service Descriptor Table (SSDT)](https://www.ired.team/miscellaneous-reversing-forensics/windows-kernel-internals/glimpse-into-ssdt-in-windows-x64-kernel)
* [Web Infosec: Hooking the System Service Dispatch Table (SSDT)](https://resources.infosecinstitute.com/topics/hacking/hooking-system-service-dispatch-table-ssdt/) -> In this article we'll present how we can hook the System Service Dispatch Table, but first we have to establish what the SSDT actually is and how it is used by the operating system.
* [Web AppsVoid: SSDT View](https://www.appsvoid.com/products/ssdt-view/) -> SSDT View is a Windows OS utility designed to list the most significant aspects of the System Service Descriptor Table (SSDT) including system service indexes, system service addresses, system service names and the module name which corresponds to the system service address.


<div id='rootkits-examples-ssdthooking-pocs'/>

##### ***POCs***

* [Github: MasterHide](https://github.com/crvvdev/MasterHide) -> A x64 Windows Driver created to monitor/hide or block access from processes, objects, files ( whatever you want, your imagination is the limit here ) using SSDT/Shadow SSDT hooks.
* [Github: TitanHide](https://github.com/mrexodia/TitanHide) -> A driver intended to hide debuggers from certain processes. The driver hooks various Nt* kernel functions (using SSDT table hooks) and modifies the return values of the original functions.
* [Github: STrace](https://github.com/mandiant/STrace) ->A DTrace on windows syscall hook reimplementation. Think of this like a patchguard compatible SSDT hook, but without hacks.


<div id='books'/>

## ***Books***

* [Windows Internals - Russinovich, M., Solomon, D., Ionescu, A. & Yosifovich, P. - Microsoft Press. - (Parte 1: 50€, Parte 2: 55€)](https://learn.microsoft.com/en-us/sysinternals/resources/windows-internals) -> Architecture and core internals of Windows.
* [Beyond BIOS: Developing with the Unified Extensible Firmware Interface - Marisetty, S., Rothman, M., & Zimmer, V. - Intel Press. - (66,55€)](https://www.amazon.es/Beyond-BIOS-Developing-Extensible-Interface/dp/1501514784) -> This book provides an overview of modern boot firmware, including the Unified Extensible Firmware Interface (UEFI) and its associated EFI Developer Kit II (EDKII) firmware.
* [Rootkits and Bootkits: Reversing Modern Malware and Next Generation Threats - Matrosov, A., Rodionov, E., & Bratus, S. - No Starch Press. - (40€)](https://www.amazon.es/Rootkits-Bootkits-Reversing-Malware-Generation/dp/1593277164) -> Rootkits and Bootkits will teach you how to understand and counter sophisticated, advanced threats buried deep in a machine’s boot process or UEFI firmware.
* [The Rootkit Arsenal: Escape and Evasion in the Dark Corners of the System - Blunden, B. - Jones & Bartlett Learning. - (85€)](https://www.amazon.es/Rootkit-Arsenal-Escape-Evasion-Corners/dp/144962636X) -> While forensic analysis has proven to be a valuable investigative tool in the field of computer security, utilizing anti-forensic technology makes it possible to maintain a covert operational foothold for extended periods, even in a high-security environment. Adopting an approach that favors full disclosure, the updated Second Edition of The Rootkit Arsenal presents the most accessible, timely, and complete coverage of forensic countermeasures.
* [Rootkits: Subverting the Windows Kernel - Hoglund, G., & Butler, J. - Addison-Wesley. - (50€)](https://www.amazon.es/Rootkits-Subverting-Windows-Greg-Hoglund/dp/0321294319) -> It's imperative that everybody working in the field of cyber-security read this book to understand the growing threat of rootkits.
<!-- https://libgen.unblockninja.com/ -->



<div id='awesome'/>

## ***Awesome***

* [Github: Advanced Windows exploit development resources](https://github.com/FULLSHADE/WindowsExploitationResources/) -> Some resources, links, books, and papers related to mostly Windows Internals and anything Windows kernel related.
* [Github: Awesome Windows Kernel Security Development](https://github.com/ExpLife0011/awesome-windows-kernel-security-development) -> Some resources related to Windows kernel development.



<div id='mastersdegree'/>

## ***Master's Degree***

If you wish to acquire this knowledge, along with other topics related to malware analysis, reversing, and bug hunting, under the guidance of top-notch professionals, do not hesitate to get in touch with the institution where I am an instructor, offering a [master's degree (Máster en Reversing, Análisis de Malware y Bug Hunting)](https://www.campusciberseguridad.com/masters/master-en-reversing) in this field.


<p align="center">
  <span style="vertical-align: middle;">
    <img width="200px" src="images/ENIIT.png" alt="ENIIT">
  </span>
  <span style="vertical-align: middle;">
    <img width="200px" src="images/UCAM.png" alt="UCAM">
  </span>
  <span style="vertical-align: middle;">
    <img width="140px" src="images/Campus_Internacional_de_Ciberseguridad.png" alt="Campus Internacional de Ciberseguridad">
  </span>
</p>
