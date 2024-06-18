# Awesome Bootkits & Rootkits Development

A curated compilation of extensive resources dedicated to bootkit and rootkit development.

<p align="center">
  <img src="images/Logo.png">
</p>


---
---
---


## ***Table of Contents***
- [TheMalwareGuardian](#themalwareguardian)
- [BIOS UEFI](#bios-uefi)
- [EDK2](#edk2)
- [Bootkits](#bootkits)
- [Windows Kernel](#windows-kernel)
- [Rootkits](#rootkits)
- [Exploits](#exploits)
- [Lab](#lab)
- [Books](#books)
- [Cybersecurity resources](#cybersecurity-resources)
- [Master's Degree](#mastersdegree)


---
---
---


<div id='themalwareguardian'/>

## ***TheMalwareGuardian***

Whoami

* [Web Linkedin: Alejandro Vázquez Vázquez](https://www.linkedin.com/in/vazquez-vazquez-alejandro/) -> My Linkedin profile.
* [Web Campus Internacional de Ciberseguridad: Máster en Reversing, Análisis de Malware y Bug Hunting](https://www.campusciberseguridad.com/masters/master-en-reversing) -> Master's degree professor (Reverse Engineering, Malware Analysis and Bug Hunting).
* [Github: Awesome Bootkits & Rootkits Development](https://github.com/TheMalwareGuardian/Awesome-Bootkits-Rootkits-Development) -> A curated compilation of extensive resources dedicated to bootkit and rootkit development.
* [Github: UEFI Windows Bootkit](https://github.com/TheMalwareGuardian/Abismo) -> Abismo is a comprehensive project thoroughly designed with the explicit goal of establishing a robust foundation for the development of bootkits.
* [Github: Windows Kernel Mode Rootkit](https://github.com/TheMalwareGuardian/Bentico) -> Bentico is a comprehensive project thoroughly designed with the explicit goal of establishing a robust foundation for the development of rootkits.


---
---
---


<div id='bios-uefi'/>

## ***BIOS UEFI***

Deep dive into BIOS UEFI.


<div id='bios-uefi-specification'/>

### ***Specification***

Return here once you have developed a better grasp of the subject.

* [Web UEFI: Specifications](https://uefi.org/specifications) -> Unified Extensible Firmware Interface Forum.
* [Web UEFI: UEFI Specification Version 2.10](https://uefi.org/specs/UEFI/2.10/) -> This Unified Extensible Firmware Interface (UEFI) Specification describes an interface between the operating system (OS) and the platform firmware.
* [Web UEFI: UEFI Platform Initialization Specification 1.8](https://uefi.org/specs/PI/1.8/) -> This specification defines the core code and services that are required for an implementation of the Pre-EFI Initialization (PEI) phase of the Platform Initialization (PI) specifications (hereafter referred to as the "PI Architecture").


<div id='bios-uefi-basics'/>

### ***Basics***

This should be your starting point.

* [Web Wikipedia: Booting](https://en.wikipedia.org/wiki/Booting) -> In computing, booting is the process of starting a computer as initiated via hardware such as a button on the computer or by a software command
* [Web OsDev: UEFI](https://wiki.osdev.org/UEFI) -> UEFI is a specification for x86, x86-64, ARM, and Itanium platforms that defines a software interface between the operating system and the platform firmware/BIOS.
* [Blog: Programming for EFI](https://www.rodsbooks.com/) -> Tech-savvy individuals know the Extensible Firmware Interface (EFI) and its newer variant, the Unified EFI (UEFI) as a replacement for the older Basic Input/Output System (BIOS) on PCs and other computers. What you may not be aware of is that EFI is a complex software environment, comparable in size and features to a simple OS such as DOS. As such, EFI can host a variety of programs—but those programs can't spring into existence fully-formed, like Athena from Zeus' head. Rather, they must be written by individuals.


<div id='bios-uefi-videos'/>

### ***Videos***

Familiarize yourself with UEFI watching these videos.

* [Youtube Video: BIOS and UEFI As Fast As Possible](https://www.youtube.com/watch?v=zIYkol851dU) -> What fundamental things does a computer BIOS do, and what are the important differences between the traditional BIOS and the newer UEFI?
* [Youtube Video: BIOS, CMOS, UEFI](https://www.youtube.com/watch?v=LGz0Io_dh_I) -> This video explains the difference between the BIOS, CMOS, and UEFI. It also explains what the purpose of the CMOS battery. What is the BIOS? What is UEFI? What is CMOS?
* [Youtube Video: PC BIOS Settings](https://www.youtube.com/watch?v=ezubjTO7rRI&t=10s) -> BIOS / UEFI settings, including boot options, secure boot, enabling XMP memory profiles, and BIOS passwords. Also information on the differences between a legacy BIOS and a UEFI BIOS, and how to enter the BIOS.
* [Youtube Video: ThatOsDev - EFI based Bootloader](https://www.youtube.com/watch?v=_98PUTJc9Yk&list=PLwH94sFU_ljPi2ClIcWIvuc1GdLT81uuH&index=4) -> EFI Explained.
* [Youtube Video: UEFIForum - Best Practices for UEFI Secure Boot Customization](https://www.youtube.com/watch?v=WBemkwMHLJM) -> UEFI Secure Boot helps provide an effective defense against boot malware, but following today's best practices in its implementation, deployment and configurability can help its increase its effectiveness against increasingly sophisticated exploits.


<div id='bios-uefi-windows-boot'/>

### ***Windows Boot***

Gain an understanding of the Windows boot process and the existing protection mechanisms at startup.

* [Presentation: UEFI Plugfest - Windows Boot Environment](https://uefi.org/sites/default/files/resources/UEFI-Plugfest-WindowsBootEnvironment.pdf) -> High-level description of Windows boot process and Windows UEFI services usage.
* [Web Microsoft: Secure boot](https://learn.microsoft.com/en-us/windows-hardware/design/device-experiences/oem-secure-boot) -> Secure boot is a security standard developed by members of the PC industry to help make sure that a device boots using only software that is trusted by the Original Equipment Manufacturer (OEM).
* [Web Microsoft: Secure the Windows boot process](https://learn.microsoft.com/en-us/windows/security/operating-system-security/system-security/secure-the-windows-10-boot-process) -> Running Windows 10 or Windows 11 on a PC with Unified Extensible Firmware Interface (UEFI) support ensures that Trusted Boot safeguards your PC against malware right from the moment you power it on.
* [Youtube Video: Boot Up with Confidence Windows 10/11 Secure Boot Demystified](https://www.youtube.com/watch?v=ZF1xGdhyUyw&t=45s) -> How secure boot works in Windows 10/11. Secure boot allows protection from "root-kit" attacks on both clients and servers.
* [Youtube Video: Compare Windows 7 and Windows 8-10 boot process](https://www.youtube.com/watch?v=_DQlaFUhCyM) -> A comparison of the boot process of Windows 7 and Windows 8/10.


<div id='bios-uefi-vulnerabilities'/>

### ***Vulnerabilities***

Explore BIOS vulnerabilities, it's fine if it appears challenging at this moment.

* [Presentation: BlackHat USA 2009 - Attacking Intel Bios](https://www.blackhat.com/presentations/bh-usa-09/WOJTCZUK/BHUSA09-Wojtczuk-AtkIntelBios-SLIDES.pdf)
* [Youtube Video: BlackHat USA 2009 - Attacking Intel Bios](https://www.youtube.com/watch?v=CRjcKv-xiqw) -> We demonstrate how to permanently reflash Intel BIOSes on the latest Intel Q45-based systems. In contrast to a previous work done by other researches a few months earlier, who targeted totally unprotected low-end BIOSes, we focus on how to permanently reflash one of the most secure BIOSes out there, that normally only allow a vendor's digitally signed firmware to be flashed.
* [Presentation: REcon 2015 - Attacking and Defending BIOS](https://recon.cx/2015/slides/recon2015-09-yuriy-bulygin-oleksandr-bazhaniuk-Attacking-and-Defending-BIOS-in-2015.pdf)
* [Youtube Video: REcon 2015 - Attacking and Defending BIOS](https://www.youtube.com/watch?v=rGkymhurzM8) -> In this presentation we will demonstrate multiple types of recently discovered BIOS vulnerabilities. We will detail how hardware configuration is restored upon resume from sleep and how BIOS can be attacked when waking up from sleep using "S3 resume boot script" vulnerabilities. Similarly, we will discuss the impact of insufficient protection of persistent configuration data in non-volatile storage and more.
* [Presentation: Defcon 22 - Summary of Attacks Against BIOS](https://defcon.org/images/defcon-22/dc-22-presentations/Bulygin-Bazhaniul-Furtak-Loucaides/DEFCON-22-Bulygin-Bazhaniul-Furtak-Loucaides-Summary-of-attacks-against-BIOS-UPDATED.pdf)
* [Youtube Video: Defcon 22 - Summary of Attacks Against BIOS](https://www.youtube.com/watch?v=QDSlWa9xQuA) -> A variety of attacks targeting platform firmware have been discussed publicly, drawing attention to the pre-boot and firmware components of the platform such as secure boot, OS loaders, and SMM. Windows 8 Secure Boot provides an important protection against bootkits by enforcing a signature check on each boot component.
* [Presentation: BlackHat USA 2017 - Betraying the BIOS, Where the Guardians of the BIOS are Failing](https://www.blackhat.com/docs/us-17/wednesday/us-17-Matrosov-Betraying-The-BIOS-Where-The-Guardians-Of-The-BIOS-Are-Failing.pdf)
* [Youtube Video: BlackHat USA 2017 - Betraying the BIOS, Where the Guardians of the BIOS are Failing](https://www.youtube.com/watch?v=Dfl2JI2eLc8) -> For UEFI firmware, the barbarians are at the gate -- and the gate is open. On the one hand, well-intentioned researchers are increasingly active in the UEFI security space; on the other hand, so are attackers. Information about UEFI implants -- by HackingTeam and state-sponsored actors alike -- hints at the magnitude of the problem, but are these isolated incidents, or are they indicative of a more dire lapse in security?
* [Presentation: BlackHat Europe 2023 - LogoFAIL - Security Implications of Image Parsing During System Boot](https://i.blackhat.com/EU-23/Presentations/EU-23-Pagani-LogoFAIL-Security-Implications-of-Image_REV2.pdf)
* [Youtube Video: BlackHat Europe 2023 - LogoFAIL - Security Implications of Image Parsing During System Boot](https://www.youtube.com/watch?v=ch0t2_yjQJQ) -> Enter LogoFAIL, our latest research revealing significant security vulnerabilities in the image parsing libraries used by nearly all BIOS vendors to display logo images during boot. Our research highlights the risks associated with parsing complex file formats at such a delicate stage of the platform startup. During this talk, we will show how some UEFI BIOSes allow attackers to store custom logo images, which are parsed during boot, on the EFI system partition (ESP) or inside unsigned sections of a firmware update. We also shed light on the implications of these vulnerabilities, which extend beyond mere graphical rendering. In fact, successful exploitation of these vulnerabilities allows attackers to hijack the execution flow and achieve arbitrary code execution. LogoFAIL vulnerabilities can compromise the security of the entire system rendering "below-the-OS" security measures completely ineffective (e.g., Secure Boot). Finally, our talk will include a detailed explanation of how we successfully escalate privileges from OS to firmware level by exploiting a real device vulnerable to LogoFAIL...


<div id='bios-uefi-tools'/>

### ***Tools***

Analyze, test, and modify UEFI firmware.

* [Github: UEFITool - UEFI firmware image viewer and editor](https://github.com/LongSoft/UEFITool) -> UEFITool is a cross-platform open source application written in C++/Qt, that parses UEFI-compatible firmware image into a tree structure, verifies image's integrity and provides a GUI to manipulate image's elements. Project development started in the middle of 2013 because of the lack of cross-platform open source utilities for tinkering with UEFI images.
* [Github: CHIPSEC - Platform Security Assessment Framework](https://github.com/LongSoft/UEFITool) -> CHIPSEC is a framework for analyzing the security of PC platforms including hardware, system firmware (BIOS/UEFI), and platform components. It includes a security test suite, tools for accessing various low level interfaces, and forensic capabilities. It can be run on Windows, Linux, Mac OS X and UEFI shell. Instructions for installing and using CHIPSEC can be found in the manual.
* [Github: FwHunt](https://github.com/binarly-io/FwHunt) -> The Binarly Firmware Hunt (FwHunt) rule format was designed to scan for known vulnerabilities in UEFI firmware.
* [Github: Kraft Dinner](https://github.com/tandasat/kraft_dinner) -> Tool to dump UEFI runtime drivers implementing runtime services for Windows


---
---
---


<div id='edk2'/>

## ***EDK2***

Study the development of applications and drivers (bootkit components) in the UEFI environment.


<div id='edk2-basics'/>

#### ***Basics***

Configure the required development environment.

* [Github: EDK II Project](https://github.com/tianocore/edk2) -> A modern, feature-rich, cross-platform firmware development environment for the UEFI and PI specifications from www.uefi.org.
* [Github: Getting Started with EDK II](https://github.com/tianocore/tianocore.github.io/wiki/Getting-Started-with-EDK-II) -> Steps for downloading EDK II from GitHub and compiling projects under various OS/compiler environments.
* [Github: Getting Started Writing Simple Application with EDK II](https://github.com/tianocore/tianocore.github.io/wiki/Getting-Started-Writing-Simple-Application) -> How to Write a Simple EDK II UEFI Application.
* [Web Basic Input/Output: "Hello World" Quick Start with EDK II](https://www.basicinputoutput.com/2019/10/hello-world-quick-start-with-edk2.html) -> Setup the EDK on a system and configure it to build a basic "Hello, World" type program.
* [Github: UEFI Pratical Programming](https://github.com/luobing/uefi-practical-programming)
* [GitHub: EDK II Driver Writer's Guide](https://github.com/tianocore-docs/edk2-UefiDriverWritersGuide/blob/master/EXAMPLES.md)
* [Web Linkedin: Understanding and Exploiting UEFI Secure Boot with Intel's EDK2](https://medium.com/@pepitoscrespo/understanding-and-exploiting-uefi-secure-boot-with-intels-edk2-a1019294f9cd)


<div id='edk2-videos'/>

#### ***Videos***

Check out these videos to learn advanced development techniques.

* [Youtube Video: UEFIForum - Driver Development with EDKII](https://www.youtube.com/watch?v=PX4HaWQNrlo) -> The world of UEFI is unlike OS-based software ecosystems in several aspects and the difference can be daunting to a developer who is starting to write UEFI device drivers.
* [Youtube Video: Queso Fuego - UEFI Programming in C](https://www.youtube.com/watch?v=t3iwBQg_Gik&list=PLT7NbkyNWaqZYHNLtOZ1MNxOt8myP5K0p) -> Intro, setup, and hello world program to start programming for x86_64 EFI applications. We'll be writing a program to make GPT disk images with an EFI system partition and basic data partition, and an OS loader EFI application for an operating system bootloader. Everything will follow official specifications and documentation for UEFI, ACPI, FAT32, etc. as much as possible.


<div id='edk2-source-pocs'/>

#### ***PoCs***

UEFI applications and drivers.

* [Github: Shim - A first-stage UEFI bootloader](https://github.com/rhboot/shim) -> Shim is a trivial EFI application that, when run, attempts to open and execute another application. It will initially attempt to do this via the standard EFI LoadImage() and StartImage() calls. If these fail (because Secure Boot is enabled and the binary is not signed with an appropriate key, for instance) it will then validate the binary against a built-in certificate. If this succeeds and if the binary or signing key are not forbidden then shim will relocate and execute the binary.
* [Github: Efi-Memory - PoC EFI runtime driver for memory r/w & kdmapper fork](https://github.com/SamuelTulach/efi-memory) -> Efi-memory is a proof-of-concept EFI runtime driver for reading and writing to virtual memory. It uses EfiGuards method of hooking SetVariable to communicate with the user-mode process.
* [Github: EFI Driver Access](https://github.com/TheCruZ/EFI_Driver_Access) -> Efi Driver Access is a simply project to load a driver during system boot with the idea to give the user kernel access for read/write memory without restrictions.
* [Github: TcpTransport](https://github.com/vinxue/TcpTransport) -> A UEFI application to receive TCP network packets.


---
---
---


<div id='bootkits'/>

## ***Bootkits***

The most advanced malware that infects the boot process, which remains undetectable.


<div id='bootkits-basics'/>

### ***Basics***

What is a bootkit exactly? Are they the elements you can develop with EDK2?

* [Web CrowdStrike: Bootkit - Definition, Prevention, and Removal](https://www.crowdstrike.com/cybersecurity-101/malware/bootkit/) -> A strong cybersecurity strategy should not only include reactive approaches to cyberattacks, but should also include proactive prevention methods for infections such as bootkit. Mitigating the consequences of a bootkit infection and removing the infection are valuable tools for your cybersecurity team. Bootkits are stealthy, and understanding how they work and how to combat them can help keep your business safe from threat actors.


<div id='bootkits-videos'/>

### ***Videos***

Watch these videos to learn what a bootkit is and the techniques used in its development.

* [Presentation: BlackHat USA 2013 - Detecting OSX and Windows bootkits with RDFU](https://cdn2.hubspot.net/hubfs/3375217/Reversing_Labs_November%202018/File/Presentation-BlackHat-Vegas-2013.pdf)
* [Youtube Video: BlackHat USA 2013 - Detecting OSX and Windows bootkits with RDFU](https://www.youtube.com/watch?v=7UsdRzsue-g) -> UEFI has recently become a very public target for rootkits and malware. To combat this new threat, we developed a Rootkit Detection Framework for UEFI ("RDFU") that incorporates a unified set of tools that address this problem across a wide spectrum of UEFI implementations.
* [Presentation: HackInTheBox 2013 - Dreamboot](https://archive.conference.hitb.org/hitbsecconf2013ams/materials/D2T1%20-%20Sebastien%20Kaczmarek%20-%20Dreamboot%20UEFI%20Bootkit.pdf)
* [Youtube Video: HackInTheBox 2013 - Dreamboot](https://www.youtube.com/watch?v=KvTUE5P-Yhs) -> This presentation is a study of the overall architecture of UEFI from a security point of view with a focus on a bootkit implementation for Windows 8 x64 which exploits the UEFI firmware: Dreamboot. Dreamboot has two specific payloads: Privilege escalation and Windows local authentication bypass. DreamBoot comes in the form of a bootable ISO, to use preferably as part of a physical attack (i.e. when the attacker has physical access to the machine peripherals: DVD or USB ports). It is also fully functional in virtualized environments like VMWare Workstation or ESX.
* [Paper: Virus Bulletin 2014 - Bootkits past, present & future](https://www.virusbulletin.com/virusbulletin/2014/11/paper-bootkits-past-present-amp-future)
* [Youtube Video: Virus Bulletin 2014 - Bootkits past, present & future](https://www.youtube.com/watch?v=jN34P4EdIUw) -> Bootkit threats have always been a powerful weapon in the hands of cybercriminals, allowing them to establish persistent and stealthy presence in their victims' systems. The most recent notable spike in bootkit infections was associated with attacks on 64-bit versions of the Microsoft Windows platform, which restrict the loading of unsigned kernel-mode drivers. However, these bootkits aren't effective against UEFI-based platforms. So, are UEFI-based machines immune against bootkit threats (or would they be)?
* [Paper: BlackHat USA 2014 - Exposing Bootkits with BIOS Emulation](https://www.blackhat.com/docs/us-14/materials/us-14-Haukli-Exposing-Bootkits-With-BIOS-Emulation-WP.pdf)
* [Youtube Video: BlackHat USA 2014 - Exposing Bootkits with BIOS Emulation](https://www.youtube.com/watch?v=siMj4bFx5nI) -> Stealth and persistency are invaluable assets to an intruder. You cannot defend against what you cannot see. This talk discusses techniques to counter attempts at subverting modern security features, and regain control of compromised machines, by drilling down deep into internal structures of the operating system to battle the threat of bootkits.
* [Youtube Video: Nullcon 2022 - A UEFI firmware bootkit in the wild](https://www.youtube.com/watch?v=lSpOFUCzFdk) -> Despite the advanced capabilities they provide, low-level implants such as bootkits and rootkits are only deployed by the most sophisticated attackers due to the risk they pose to the victim system's stability. In recent years, Kaspersky has however observed a number of new low-level malware, such as MosaicRegressor, MoonBounce, and the object of this talk, CosmicStrand.
* [Presentation: OffensiveCon18 - Alex Ionescu Advancing the State of UEFI Bootkits](http://publications.alex-ionescu.com/OffensiveCon/OffensiveCon%202018%20-%20Advancing%20the%20state%20of%20UEFI%20Boot%20Kits.pdf)
* [Youtube Video: OffensiveCon18 - Alex Ionescu Advancing the State of UEFI Bootkits](https://www.youtube.com/watch?v=dpG97TBR3Ys) -> Persistence in the Age of PatchGuard and Windows 10.


<div id='bootkits-analysis'/>

### ***Analysis***

Gain a true understanding of this malware by reading its analyses.

* [Web WeLiveSecurity: BlackLotus UEFI bootkit - Myth confirmed](https://www.welivesecurity.com/2023/03/01/blacklotus-uefi-bootkit-myth-confirmed/) -> The first in-the-wild UEFI bootkit bypassing UEFI Secure Boot on fully updated UEFI systems is now a reality.
* [Web Binarly: The Untold Story of the BlackLotus UEFI Bootkit](https://www.binarly.io/blog/the-untold-story-of-the-blacklotus-uefi-bootkit) -> My experience with the analysis and detection of rootkits and bootkits goes back more than 20 years. In the early 2000s, the main challenge was dealing with infected machines when rootkits and bootkits modified the operating system kernel to conceal malicious components. It was such a fun time reverse engineering advanced threats in the good old days that I co-wrote "Rootkits and Bootkits: Reversing Modern Malware and Next Generation Threats", a book full of the most interesting stories of our time going down the rabbit hole of advanced malware.
* [Web WeLiveSecurity: UEFI threats moving to the ESP - Introducing ESPecter bootkit](https://www.welivesecurity.com/2021/10/05/uefi-threats-moving-esp-introducing-especter-bootkit/) -> ESET research discovers a previously undocumented UEFI bootkit with roots going back all the way to at least 2012.
* [Web Palo Alto: Diving Into Glupteba's UEFI Bootkit](https://unit42.paloaltonetworks.com/glupteba-malware-uefi-bootkit/) -> Glupteba is advanced, modular and multipurpose malware that, for over a decade, has mostly been seen in financially driven cybercrime operations. This article describes the infection chain of a new campaign that took place around November 2023. We will focus on one intriguing and previously undocumented feature: a Unified Extensible Firmware Interface (UEFI) bootkit.
* [Web SecureList: FinSpy - Unseen findings](https://securelist.com/finspy-unseen-findings/104322/) -> FinSpy, also known as FinFisher or Wingbird, is an infamous surveillance toolset. Kaspersky has been tracking deployments of this spyware since 2011.
* [Web SecureList: MosaicRegressor - Lurking in the Shadows of UEFI](https://securelist.com/mosaicregressor/98849/) -> UEFI has become a prominent technology that is embedded within designated chips on modern day computer systems. Replacing the legacy BIOS, it is typically used to facilitate the machine's boot sequence and load the operating system, while using a feature-rich environment to do so. At the same time, it has become the target of threat actors to carry out exceptionally persistent attacks.
* [Web WeLiveSecurity: LoJax - First UEFI rootkit found in the wild, courtesy of the Sednit group](https://www.welivesecurity.com/2018/09/27/lojax-first-uefi-rootkit-found-wild-courtesy-sednit-group/) -> ESET researchers have shown that the Sednit operators used different components of the LoJax malware to target a few government organizations in the Balkans as well as in Central and Eastern Europe.
* [Web Twitter X: ESETresearch - Malicious EFI samples](https://x.com/ESETresearch/status/1275770256389222400) -> ESETresearch identified multiple malicious EFI bootloader samples. The malware displays a ransom message and prevents the computer from booting. It can compromise computers with disabled UEFI Secure Boot feature.
* [Web VMWare: Detecting UEFI Bootkits in the Wild](https://blogs.vmware.com/security/2021/06/detecting-uefi-bootkits-in-the-wild-part-1.html) -> Threat actors are continually looking for ways to improve the persistence of their malware and implants. Bootkits, meaning rootkits running at the firmware level, have been utilized for this purpose. Once bootkits are installed, it can be extremely difficult to detect or remove versus OS-level rootkits as they are executed prior to the actual OS boot process.


<div id='bootkits-source-code'/>

### ***Source Code***

Observe that the components shown in the source code are the applications and drivers you can develop with EDK2.

* [Github: Abismo](https://github.com/TheMalwareGuardian/Abismo) -> Abismo is a comprehensive project thoroughly designed with the explicit goal of establishing a robust foundation for the development of bootkits. By offering a centralized repository of knowledge, Abismo stands as a valuable initiative for anyone looking to contribute to and benefit from the collective understanding of this field.
* [Github: BlackLotus](https://github.com/ldpreload/BlackLotus) -> An innovative UEFI Bootkit designed specifically for Windows. It incorporates a built-in Secure Boot bypass and Ring0/Kernel protection to safeguard against any attempts at removal. This software serves the purpose of functioning as an HTTP Loader.
* [Github: EfiGuard](https://github.com/Mattiwatti/EfiGuard) -> Portable x64 UEFI bootkit that patches the Windows boot manager, boot loader and kernel at boot time in order to disable PatchGuard and Driver Signature Enforcement (DSE).
* [Github: DmaBackdoorBoot](https://github.com/Cr4sh/s6_pcie_microblaze/tree/master/python/payloads/DmaBackdoorBoot) -> UEFI DXE driver intended for executing of kernel mode and user mode payloads under the Windows operating system by having an arbitrary code execution at early boot stage during DXE phase of the platform initialization.
* [Github: Bootlicker](https://github.com/realoriginal/bootlicker) -> A generic UEFI bootkit used to achieve initial usermode execution.
* [Github: RedLotus](https://github.com/memN0ps/bootkit-rs) -> Windows UEFI Bootkit in Rust designed to facilitate the manual mapping of a driver manual mapper before the kernel (ntoskrnl.exe) is loaded, effectively bypassing Driver Signature Enforcement (DSE).
* [Github: Bootkit Showcase](https://github.com/hardenedvault/bootkit-samples) -> Real-World Examples of Infrastructure Security Threats.
* [Github: SandboxBootkit](https://github.com/thesecretclub/SandboxBootkit) -> Bootkit tested on Windows Sandbox to patch ntoskrnl.exe and disable DSE/PatchGuard.
* [Github: Umap](https://github.com/btbd/umap/) -> Windows UEFI bootkit that loads a generic driver manual mapper without using a UEFI runtime driver.
* [Github: UEFI-Bootkit](https://github.com/ajkhoury/UEFI-Bootkit) -> A small bootkit designed to use zero assembly.
* [Github: PeiBackdoor](https://github.com/Cr4sh/PeiBackdoor) -> This project implements early stage firmware backdoor for UEFI based firmware. It allows to execute arbitrary code written in C during Pre EFI Init (PEI) phase of Platform Initialization (PI).
* [Github: Rovnix](https://github.com/m0n0ph1/Win64-Rovnix-VBR-Bootkit) -> Volume Boot Record Bootkit.
* [Github: Vector EDK](https://github.com/hackedteam/vector-edk) -> EFI Development Kit.
* [Github: Dreamboot](https://github.com/quarkslab/dreamboot) -> UEFI bootkit.
* [Github: UEFIBootkit](https://github.com/gfoudree/UEFIBootkit) -> Simple PoC for a bootkit written as a UEFI Option ROM Driver.
* [Web Back Engineering: Voyager - A Hyper-V Hacking Framework For Windows 10 x64 (AMD & Intel)](https://git.back.engineering/_xeroxz/voyager) -> Voyager is a project designed to offer module injection and vmexit hooking for both AMD & Intel versions of Hyper-V. This project works on all versions of Windows 10-x64 (2004-1507).


---
---
---


<div id='windows-kernel'/>

## ***Windows Kernel***

Explore the heart of Windows.


<div id='windows-kernel-basics'/>

### ***Basics***

The essentials for learning how Windows operates beneath the surface.

* [Web Microsoft: User mode and kernel mode](https://learn.microsoft.com/en-us/windows-hardware/drivers/gettingstarted/user-mode-and-kernel-mode) -> A processor in a computer running Windows operates in two different modes: user mode and kernel mode. The processor switches between these modes depending on the type of code it's executing. Applications operate in user mode, while core operating system components function in kernel mode. Although many drivers operate in kernel mode, some can function in user mode.
* [Github: System Internals of Windows](https://github.com/rmusser01/Infosec_Reference/blob/master/Draft/sysinternals.md#windows-internals) -> System architecture, processes, threads, memory management, and more.
* [Web RedTeamNotes: Internals](https://www.ired.team/miscellaneous-reversing-forensics/windows-kernel-internals) -> Everything you need to know about Windows kernel.
* [Web SamsClass Info: Windows Internals CTF](https://samsclass.info/126/WI2021.htm) -> Sam Bowne.


<div id='windows-kernel-videos'/>

### ***Videos***

Watch these videos to gain a deeper understanding of Windows' core components.

* [Youtube Video: Pavel Yosifovich - Native Applications What, Why, and How?](https://www.youtube.com/watch?v=EKBvLTuI2Mo) -> Normally, native applications are built by Microsoft only. Examples include Smss.exe (the session manager), CSrss.exe (the Windows subsystem process), and UserInit.exe (normally executed by WinLogon.exe on a successful login).
* [Youtube Video: ACCU 2019 - Windows Native API](https://www.youtube.com/watch?v=a0KozcRhotM) -> Many programmers are familiar with the Windows "Win32" API that provides access to a large variety of services, from user interface to memory management; but far fewer have much idea about the Windows "Native" API which is the mechanism used to access the operating system services located in the kernel.
* [Youtube Video: BlackhHat 2015 - Battle Of The SKM And IUM, How Windows 10 Rewrites OS Architecture](https://www.youtube.com/watch?v=LqaWIn4y26E) -> In Windows 10, Microsoft is introducing a radical new concept to the underlying OS architecture, and likely the biggest change to the NT design since the decision to move the GUI in kernel-mode. In this new model, the Viridian Hypervisor Kernel now becomes a core part of the operating system and implements Virtual Secure Machines (VSMs) by loading a true microkernel - a compact (200kb) NT look-alike with its own drivers called the Secure Kernel Mode (SKM) environment, which then uses the Hypervisor to hook and intercept execution of the true NT kernel. This creates a new paradigm where the NT Kernel, executing in Ring 0, now runs below the Secure Kernel, at Ring ~0 (called Virtual Trust Level 1).
* [Youtube Video: Windows IT Pro - Sysinternals Overview (Microsoft, tools, utilities, demos)](https://www.youtube.com/watch?v=6RqFPrCcWfY) -> Learn about the tools that security, developer, and IT professionals rely on to analyze, diagnose, troubleshoot, and optimize Windows from creator Mark Russinovich. Find out which utilities will help you optimize any Windows system's reliability, efficiency, performance, and security.
* [Youtube Video: DotNext - Pavel Yosifovich, Windows 10 internals for .NET developers](https://www.youtube.com/watch?v=h6BXMcRqYhA) -> The .NET Framework provides some level of abstraction over the Windows OS, but understanding the way Windows works can make you a better .NET developer. Windows 10 is progressing at a faster cadence than in the past. Some of its features are not exposed to .NET developers directly.
* [Youtube Video: REcon 2019 - The Last Generic Win32K KASLR Defeat in Windows](https://www.youtube.com/watch?v=PTnuwchEci0) -> This talk will describe the final mistake that Microsoft made when 'fixing' the shared heap (desktop heap and session heap) structures that are shared by User and GDI objects in Win32k.sys, which have leaked kernel pointers for over 2 decades to user-mode. I will cover how existing techniques were broken in Fall Creator's Update (RS4), and how this build, and the subsequent (RS5 and 19H1) had a critical implementation flaw which still made KASLR bypasses possible.
* [Youtube Video: TryHackMe - Windows Internals](https://www.youtube.com/watch?v=k7UDasbkLJw) -> In this video, we begin working through the "Host Evasion" module on TryHackMe which is part of the Red Team path.


<div id='windows-kernel-structures'/>

### ***Structures***

Learn about the opaque structures of Windows, the core code of the kernel.

* [Web CodeMachine: Windows kernel data structures](https://codemachine.com/articles/kernel_structures.html) -> Catalog of key Windows kernel data structures.
* [Web Vergilius Project: Windows kernel](https://www.vergiliusproject.com/) -> Take a look into the depths of Windows kernels and reveal more than 60000 undocumented structures.
* [Web Geoff Chappell: Windows kernel](https://www.geoffchappell.com/) -> Because kernel-mode programming, e.g., of device drivers and file system filter drivers, is the commercial specialty that funded this website's early development as a free public resource, it could not easily itself be a subject for the free public resource. Not until 2016 did it start getting serious attention at this website, not even to publish old notes whose commercial value had long passed. Now, however, the Kernel study is well on its way to becoming a resource to reckon with for the functions and structures exposed by the kernel and the HAL.
* [Web ReactOS](https://www.geoffchappell.com/) -> Imagine running your favorite Windows applications and drivers in an open-source environment you can trust. That's the mission of ReactOS! 


<div id='windows-kernel-debugging'/>

### ***Debugging***

Analyze and debug critical structures along with the entire kernel.


<div id='windows-kernel-debugging-basics'/>

#### ***Basics***

Debug the Windows OS.

* [Web Microsoft: WinDbg](https://learn.microsoft.com/en-us/windows-hardware/drivers/debugger/) -> WinDbg is a debugger that can be used to analyze crash dumps, debug live user-mode and kernel-mode code, and examine CPU registers and memory.
* [Web WinDbg Org](http://windbg.org/) -> WinDbg Quick Links, Extensions, Scripts.
* [Web Microsoft: Setting Up Kernel-Mode Debugging](https://learn.microsoft.com/en-us/windows-hardware/drivers/debugger/setting-up-kernel-mode-debugging-in-windbg--cdb--or-ntsd) -> How to start debugging Windows kernel.
* [Web Microsoft: Local Kernel-Mode Debugging](https://learn.microsoft.com/en-us/windows-hardware/drivers/debugger/performing-local-kernel-debugging) -> Debugging Tools for Windows supports local kernel debugging. This is kernel-mode debugging on a single computer. In other words, the debugger runs on the same computer that is being debugged.
* [Web Microsoft: Remote Debugging Using WinDbg](https://learn.microsoft.com/en-us/windows-hardware/drivers/debugger/remote-debugging-using-windbg) -> Remote debugging involves two debuggers running at two different locations. The debugger that performs the debugging is called the debugging server. The second debugger, called the debugging client, controls the debugging session from a remote location. To establish a remote session, you must set up the debugging server first and then activate the debugging client.
* [Github: Modern Debugging with WinDbg Preview DEFCON 27 workshop](https://github.com/hugsy/defcon_27_windbg_workshop) -> It's 2019 and yet too many Windows developers and hackers alike rely on (useful but rather) old school tools for debugging Windows binaries (OllyDbg, Immunity Debugger). What they don't realize is that they are missing out on invaluable tools and functionalities that come with Microsoft newest WinDbg Preview edition. This hands-on workshop will attempt to level the field, by practically showing how WinDbg has changed to a point where it should be the first tool to be installed on any Windows (10) for binary analysis machine: after a brief intro to the most basic (legacy) commands, this workshop will focus around debugging modern software (vulnerability exploitation, malware reversing, DKOM-based rootkit, JS engine) using modern techniques provided by WinDbg Preview (spoiler alert to name a few, JavaScript, LINQ, TTD).


<div id='windows-kernel-debugging-basics'/>

#### ***Commands***

Key commands to use in the official Microsoft debugger, WinDbg.

* [Web Microsoft: lm (List Loaded Modules)](https://learn.microsoft.com/en-us/windows-hardware/drivers/debugger/lm--list-loaded-modules-) -> The lm command displays the specified loaded modules. The output includes the status and the path of the module.
* [Web Microsoft: x (Examine Symbols)](https://learn.microsoft.com/en-us/windows-hardware/drivers/debugger/x--examine-symbols-) -> The x command displays the symbols in all contexts that match the specified pattern.
* [Web Microsoft: !process](https://learn.microsoft.com/en-us/windows-hardware/drivers/debuggercmds/-process) -> The !process extension displays information about the specified process, or about all processes, including the EPROCESS block. This extension can be used only during kernel-mode debugging.
* [Web Microsoft: .block](https://learn.microsoft.com/en-us/windows-hardware/drivers/debuggercmds/-block) -> The .block token performs no action; it is used solely to introduce a block of statements.
* [Web Microsoft: .if](https://learn.microsoft.com/en-us/windows-hardware/drivers/debuggercmds/-if) -> The .if token behaves like the if keyword in C.
* [Web Microsoft: .for](https://learn.microsoft.com/en-us/windows-hardware/drivers/debuggercmds/-for) -> The .for token behaves like the for keyword in C, except that multiple increment commands must be separated by semicolons, not by commas.
* [Web Microsoft: .while](https://learn.microsoft.com/en-us/windows-hardware/drivers/debuggercmds/-while) -> The .while token behaves like the while keyword in C.
* [Web Microsoft: .printf](https://learn.microsoft.com/en-us/windows-hardware/drivers/debuggercmds/-printf) -> The .printf token behaves like the printf statement in C.
* [Web Microsoft: dt (Display Type)](https://learn.microsoft.com/en-us/windows-hardware/drivers/debuggercmds/dt--display-type-) -> The dt command displays information about a local variable, global variable or data type. This can display information about simple data types, as well as structures and unions.
* [Web Microsoft: d, da, db, dc, dd, dD, df, dp, dq, du, dw (Display Memory)](https://learn.microsoft.com/en-us/windows-hardware/drivers/debugger/d--da--db--dc--dd--dd--df--dp--dq--du--dw--dw--dyb--dyd--display-memor) -> The d* commands display the contents of memory in the given range.
* [Web Microsoft: e, ea, eb, ed, eD, ef, ep, eq, eu, ew, eza (Enter Values)](https://learn.microsoft.com/en-us/windows-hardware/drivers/debugger/e--ea--eb--ed--ed--ef--ep--eq--eu--ew--eza--ezu--enter-values-) -> The *e* commands enter into memory the values that you specify.
* [Web Microsoft: bp, bu, bm (Set Breakpoint)](https://learn.microsoft.com/en-us/windows-hardware/drivers/debugger/bp--bu--bm--set-breakpoint-) -> The bp, bu, and bm commands set one or more software breakpoints. You can combine locations, conditions, and options to set different kinds of software breakpoints.
* [Web Microsoft: u, ub, uu (Unassemble)](https://learn.microsoft.com/en-us/windows-hardware/drivers/debugger/u--unassemble-) -> The u* commands display an assembly translation of the specified program code in memory.


<div id='windows-kernel-debugging-scripting'/>

#### ***Scripting***

Create a script to automate the debugging process.


<div id='windows-kernel-debugging-scripting-classic'/>

##### ***Classic***

* [Web Microsoft: Debugger Commands](https://learn.microsoft.com/en-us/windows-hardware/drivers/debuggercmds/debugger-commands) -> WinDbg Scripting.
* [Web Microsoft: $<, $><, $$<, $$><, $$ >a< (Run Script File)](https://learn.microsoft.com/en-us/windows-hardware/drivers/debuggercmds/debugger-commands) -> The $<, $><, $$<, $$><, and $$>a< commands read the contents of the specified script file and use its contents as debugger command input.
* [Web KeySight: Debugging Malware with WinDbg](https://www.keysight.com/blogs/tech/nwvs/2020/07/27/debugging-malware-with-windbg) -> We present practical techniques for finding information you may be interested in by stepping through a Locky Ransomware Sample using WinDbg. WinDbg is the debugger of choice by Microsoft, so it should be for us too.
* [Web DumpAnalysis: Introduction to WinDbg Scripts for C/C++ Users](https://www.dumpanalysis.org/WCDA/WCDA-Sample-Chapter.pdf) -> All debuggers from Debugging Tools for Windows package use the same engine dbgeng.dll. It contains a script interpreter for a special language we call WinDbg scripting language for convenience and we use WDS file extension for WinDbg script files.
* [Github: WinDbg_Scripts](https://github.com/yardenshafir/WinDbg_Scripts) -> Useful scripts for WinDbg using the debugger data model.


<div id='windows-kernel-debugging-scripting-javascript'/>

##### ***JavaScript***

* [Web Microsoft: JavaScript Debugger Scripting](https://learn.microsoft.com/en-us/windows-hardware/drivers/debugger/javascript-debugger-scripting) -> This topic describes how to use JavaScript to create scripts that understand debugger objects and extend and customize the capabilities of the debugger.
* [Web Microsoft: Microsoft Github Repo Example Scripts](https://learn.microsoft.com/en-us/windows-hardware/drivers/debugger/javascript-debugger-example-scripts) -> This is a collection of extensions and sample scripts for extending WinDbg. We'll be adding more samples and extensions over time.
* [Github: WinDbg-Scripts](https://github.com/0vercl0k/windbg-scripts) -> A bunch of JavaScript extensions for WinDbg.
* [GitHub: WinDbg JavaScript Scripts](https://github.com/hugsy/windbg_js_scripts) -> Toy scripts for playing with WinDbg JS API.
* [GitHub: KasperskyLab - JS scripts for WinDbg](https://github.com/KasperskyLab/WinDbg-JS-Scripts) -> This is a collection of WinDbg JS scripts useful for dumps analysis.


<div id='windows-kernel-debugging-scripting-python'/>

##### ***Python***

* [Web PyPI: PYKD](https://pypi.org/project/pykd/) -> Python Extension for WinDbg.
* [Blog: PYKD Tutorial Part 1](https://rayanfam.com/topics/pykd-tutorial-part1/) -> Using windbg script syntax is such annoying thing that almost all reverse engineers have problems dealing with it but automating debugging gives such a power that can't be easily ignored. A good solution to solve this problem is using the power and simplicity of Python and Windbg together.
* [Blog: PYKD Tutorial Part 2](https://rayanfam.com/topics/pykd-tutorial-part2/) -> Using windbg script syntax is such annoying thing that almost all reverse engineers have problems dealing with it but automating debugging gives such a power that can't be easily ignored. A good solution to solve this problem is using the power and simplicity of Python and Windbg together.


<div id='windows-kernel-debugging-scripting-extensions'/>

##### ***Extensions***

* [GitHub: Awesome WinDbg Extensions](https://github.com/anhkgg/awesome-windbg-extensions)
* [Github: WDBGARK](https://github.com/swwwolf/wdbgark) -> WinDBG Anti-RootKit extension.
* [Github: SwishDbgExt](https://github.com/comaeio/SwishDbgExt) -> Incident Response Debugging Extension.
* [Youtube Video: Creating our first WinDbg extension from scratch](https://www.youtube.com/watch?v=d1uT8tmnhZI) -> In this video I create my very first native WinDbg extension, ever.
* [Youtube Video: Extend WinDbg to build your own dream debugging tool](https://www.youtube.com/watch?v=tSlFd0CIo0g) -> It's the beginning of a new era. After all those years, Microsoft has finally done what we stopped hoping for: WinDbg has been updated with a brand new UI! Past the "wow!" effect, it looks like many of the old WinDbg flaws are still there: a single command window, no history, limited scripting… But fear not, for something has changed: WinDbg now provides a number of extension points (undocumented at this time) that can be used to fully customize the UI and drive the debugging engine. It's up to us to turn this application into our own dream debugging tool!


<div id='windows-kernel-security'/>

### ***Protection Mechanisms***

How the core of Windows is secured.


<div id='windows-kernel-security-dse'/>

#### ***Driver Signature Enforcement***

Prevent the use of unsigned drivers.


<div id='windows-kernel-security-dse-basics'/>

##### ***Basics***

* [Web Microsoft: Signing a Driver](https://learn.microsoft.com/en-us/windows-hardware/drivers/develop/signing-a-driver) -> All drivers running on 64-bit versions of Windows must be signed before Windows will load them. However, driver signing is not required on 32-bit versions of Windows. In order to sign a driver, a certificate is required. You can create your own certificate to sign your driver with during development and testing. However, for a public release you must sign your driver with a certificate issued by a trusted root authority.
* [Web Microsoft: Introduction to Test-Signing](https://learn.microsoft.com/en-us/windows-hardware/drivers/install/introduction-to-test-signing) -> Drivers should be test-signed with a digital signature during development and test for the following reasons: To facilitate and automate installation, To be able to load kernel-mode drivers on 64-bit versions of Windows Vista and later versions of Windows, To play back certain types of next-generation premium content, all kernel-mode components in Windows Vista and later versions of Windows must be signed.
* [Web Driver Easy: Disable Driver Signature Enforcement on Windows 10 Easily!](https://www.drivereasy.com/knowledge/disable-driver-signature-enforcement-windows-10-easily/) -> On Windows 8 and Windows 10 (64-bit), Microsoft has included a feature, driver signature enforcement. It is a feature that is designed to ensure that users of Microsoft can only load drivers that have been signed by Microsoft. 
* [Web Make Use Of: How to Disable Driver Signature Enforcement and Install Unsigned Drivers on Windows](https://www.makeuseof.com/disable-driver-signature-enforcement-windows/) -> Sometimes, Windows will block you from installing an unsigned driver, which is a driver you've downloaded elsewhere other than through a Windows Update or the device manufacturer's website. But if you need the driver, and you know it is perfectly safe, you can turn off driver signature enforcement and let it through.
* [Web How To Geek: How to Disable Driver Signature Verification on 64-Bit Windows 8 or 10](https://www.howtogeek.com/167723/how-to-disable-driver-signature-verification-on-64-bit-windows-8.1-so-that-you-can-install-unsigned-drivers/) -> 64-bit versions of Windows 10 and 8 include a "driver signature enforcement" feature. They'll only load drivers that have been signed by Microsoft. To install less-than-official drivers, old unsigned drivers, or drivers you're developing yourself, you'll need to disable driver signature enforcement. 
* [Web Code Project: Disable Driver Signature Enforcement with DSE-Patcher](https://www.codeproject.com/Articles/5348168/Disable-Driver-Signature-Enforcement-with-DSE-Patc) -> Driver Signature Enforcement (DSE) was introduced by Microsoft starting with Windows Vista x64. DSE is a security feature of the operating system, which ensures that only valid signed drivers are loaded. To install unsigned drivers, the DSE security feature has to be disabled. DSE-Patcher can be used to disable DSE on all 64-bit operating systems starting with Windows Vista and later. We developed DSE-Patcher to show the interested coder how easy it is to use known vulnerabilities and change memory in kernel address space.


<div id='windows-kernel-security-vbs'/>

#### ***Virtualization Based Security (VBS)***

Assume the kernel can be compromised and create an isolated virtual environment.


<div id='windows-kernel-security-vbs-basics'/>

##### ***Basics***

* [Web Microsoft: Virtualization-based Security (VBS)](https://learn.microsoft.com/en-us/windows-hardware/design/device-experiences/oem-vbs) -> Virtualization-based security, or VBS, uses hardware virtualization and the Windows hypervisor to create an isolated virtual environment that becomes the root of trust of the OS that assumes the kernel can be compromised. Windows uses this isolated environment to host a number of security solutions, providing them with greatly increased protection from vulnerabilities in the operating system, and preventing the use of malicious exploits which attempt to defeat protections. VBS enforces restrictions to protect vital system and operating system resources, or to protect security assets such as authenticated user credentials.


<div id='windows-kernel-security-vbs-videos'/>

##### ***Videos***

* [Presentation: BlackHat USA 2016: Analysis of the Attack Surface of Windows 10 Virtualization-Based Security](https://www.blackhat.com/docs/us-16/materials/us-16-Wojtczuk-Analysis-Of-The-Attack-Surface-Of-Windows-10-Virtualization-Based-Security.pdf)
* [Youtube Video: BlackHat USA 2016: Analysis of the Attack Surface of Windows 10 Virtualization-Based Security](https://www.youtube.com/watch?v=_646Gmr_uo0) -> In Windows 10, Microsoft introduced virtualization-based security (VBS), the set of security solutions based on a hypervisor. In this presentation, we will talk about details of VBS implementation and assess the attack surface - it is very different from other virtualization solutions. We will focus on the potential issues resulting from the underlying platform complexity (UEFI firmware being a primary example).
* [Youtube Video: BSidesKC 2022 - No Code Execution? No Problem! - Living The Age of Virtualization-Based Security](https://www.youtube.com/watch?v=OBreVsVK-L8) -> Windows 11 saw the default enablement of some of the most powerful exploit mitigations on the market - many of them falling under the purview of Virtualization-Based Security, or VBS. These exploit mitigations are instrumented through Microsoft's hypervisor, Hyper-V, which provides a "higher root of trust" than the Windows kernel itself. With the advent of the default enablement of these mitigations - simply put - the "old" way of doing things won't suffice when it comes to kernel exploitation. Hypervisor-Protected Code Integrity (HVCI), one of these hypervisor-based mitigations, works by outright preventing any malicious, unsigned shellcode from running within the Windows kernel. Does this now mean "game over" for attackers? This talk investigates how these new, modern mitigations work and how today's attackers must and can adapt to the new bar set by these exploit mitigations.


#### ***Kernel Patch Protection (KPP) or PatchGuard***

Prevent alterations to critical components and structures.


<div id='windows-kernel-security-patchguard-basics'/>

##### ***Basics***

* [Web Windows-Internals: Secure Kernel Patch Guard - SKPG Initialization](https://windows-internals.com/hyperguard-secure-kernel-patch-guard-part-1-skpg-initialization/) -> This first part will focus on what SKPG is and how it's being initialized.
* [Web Windows-Internals: Secure Kernel Patch Guard - SKPG Extents](https://windows-internals.com/hyperguard-secure-kernel-patch-guard-part-2-skpg-extents/) -> This part will start describing the data structure and components of SKPG, and more specifically the way it's activated.


<div id='windows-kernel-security-patchguard-videos'/>

##### ***Videos***

* [Youtube Video: RSA Conference - Windows Kernel Patch Protection](https://www.youtube.com/watch?v=wXRLnp2JoWU) -> This session will look at a critical flaw in the design of Windows Kernel Patch Protection (PatchGuard), a system used to prevent modification to kernel code and other critical structure. The design of PatchGuard will be discussed, along with the design of an attack which uses the flaw in PatchGuard to disable the PatchGuard response entirely.


<div id='windows-kernel-security-patchguard-bypass'/>

##### ***Bypass***

* [Web Uninformed: Bypassing Patchguard on Windows](https://web.archive.org/web/20160817134601/http://uninformed.org/index.cgi?v=3&a=3&p=1) -> In the caste system of operating systems, the kernel is king. And like most kings, the kernel is capable of defending itself from the lesser citizens, such as user-mode processes, through the castle walls of privilege separation. However, unlike most kings, the kernel is typically unable to defend itself from the same privilege level at which it operates. Without the kernel being able to protect its vital organs at its own privilege level, the entire operating system is left open to modification and subversion if any code is able to run with the same privileges as the kernel itself.
* [GitHub: PatchGuardBypass](https://github.com/AdamOron/PatchGuardBypass) -> Bypassing PatchGuard on modern x64 systems.
* [Web CyberArk: GhostHook](https://www.cyberark.com/resources/threat-research-blog/ghosthook-bypassing-patchguard-with-processor-trace-based-hooking) -> Bypassing PatchGuard with Processor Trace Based Hooking.
* [GitHub: InfinityHook](https://github.com/everdox/InfinityHook) -> Kernel driver that will hook system calls.
* [Blog: New bypass disclosed in Microsoft PatchGuard (KPP)](https://www.zdnet.com/article/new-bypass-disclosed-in-microsoft-patchguard-kpp/) -> After GhostHook and InfinityHook, we now have ByePg.
* [Blog: ByePg](https://blog.can.ac/2019/10/19/byepg-defeating-patchguard-using-exception-hooking/) -> Defeating Patchguard Using Exception - Hooking.
* [Github: Shark](https://github.com/9176324/Shark) -> Turn off PatchGuard in real time for win7 (7600) ~ later.
* [Github: UPGDSED](https://github.com/hfiref0x/UPGDSED) -> Universal PatchGuard and Driver Signature Enforcement Disable.
* [Github: PgResarch](https://github.com/tandasat/PgResarch) -> PatchGuard Research.


<div id='windows-kernel-drivers'/>

### ***Drivers***

Components linked to malware that targets the core of Windows.


<div id='windows-kernel-drivers-basics'/>

#### ***Basics***

Learn the basics of creating kernel mode drivers.

* [Web Microsoft: Get started with drivers on Windows](https://learn.microsoft.com/en-us/windows-hardware/drivers/gettingstarted/) -> General overview of Windows components, types of device drivers used in Windows, goals of Windows device drivers, generic sample device drivers.
* [Web Microsoft: Kernel-Mode Driver Architecture Design Guide](https://learn.microsoft.com/en-us/windows-hardware/drivers/kernel/) -> This section includes general concepts to help you understand kernel-mode programming and describes specific techniques of kernel programming.
* [Blog: Red Team Tactics - Writing Windows Kernel Drivers for Advanced Persistence (Part 1)](https://v3ded.github.io/redteam/red-team-tactics-writing-windows-kernel-drivers-for-advanced-persistence-part-1) -> This post, as indicated by the title, will cover the topic of writing Windows kernel drivers for advanced persistence. Because the subject matter is relatively complex, I have decided to divide the project into a three or a four part series. This being the first post in the series, it will cover the fundamental information you need to know to get started with kernel development. This includes setting up a development environment, configuring remote kernel debugging and writing your first "Hello World" driver.
* [Blog: Red Team Tactics - Writing Windows Kernel Drivers for Advanced Persistence (Part 2)](https://v3ded.github.io/redteam/red-team-tactics-writing-windows-kernel-drivers-for-advanced-persistence-part-2) -> In today's post, we will be covering the Windows Filtering Platform (WFP) and how it can be used to process network packets via our driver. Specifically, we will be focusing on ICMP packets. Given the basic nature of this protocol, we will also delve into creating a custom "protocol" within ICMP itself that will enable us to issue commands to the machines that have our driver installed.
* [Blog: Loading unsigned Windows drivers without reboot](https://v1k1ngfr.github.io/loading-windows-unsigned-driver/) -> How can we load this unsigned drivers into the Windows kernel bypassing Driver Signing Enforcement (DSE)?


<div id='windows-kernel-drivers-wdk'/>

#### ***WDK***

Configure the workspace to develop those unique drivers.

* [Web Microsoft: Windows Driver Kit (WDK)](https://learn.microsoft.com/en-us/windows-hardware/drivers/other-wdk-downloads) -> This is used to develop, test, and deploy Windows Drivers.
* [Web Microsoft: Windows Driver Documentation](https://github.com/MicrosoftDocs/windows-driver-docs) -> The official Windows Driver Kit documentation sources.
* [Web Microsoft: Write a Hello World Windows Driver (KMDF)](https://learn.microsoft.com/en-us/windows-hardware/drivers/gettingstarted/writing-a-very-small-kmdf--driver) -> This article describes how to write a small Universal Windows driver using Kernel-Mode Driver Framework (KMDF) and then deploy and install your driver on a separate computer.
* [Web Microsoft: Development & Demo of Windows Kernel Driver](https://apchavan.medium.com/development-demo-of-windows-kernel-driver-47fc2150e128) -> The Kernel mode driver can run in highest privileged ring 0. It means the kernel driver mostly have highest level of permissions (like kernel) while executing.
* [Web Microsoft: DriverEntry for WDF Drivers routine](https://learn.microsoft.com/en-us/windows-hardware/drivers/wdf/driverentry-for-kmdf-drivers) -> DriverEntry is the first driver-supplied routine that is called after a driver is loaded. It is responsible for initializing the driver.
* [Web Microsoft: DriverUnload callback function](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_unload) -> The Unload routine performs any operations that are necessary before the system unloads the driver.


<div id='windows-kernel-drivers-videos'/>

#### ***Videos***

Learn with visual examples how to develop those drivers.

* [Youtube Video: GuidedHacking - How to make a Kernel Driver](https://www.youtube.com/watch?v=9h1FsOISwX0) -> This tutorial series will teach you everything you need to make a kernel driver on Windows.
* [Youtube Video: Nir Lichtman - Making Simple Windows Driver in C](https://www.youtube.com/watch?v=GTrekHE8A00) -> In this video I will demonstrate how you can write a simple "Hello, World" driver for Microsoft Windows 10 using the C Programming Language.
* [Youtube Video: Your first kernel driver (Full Guide)](https://www.youtube.com/watch?v=n463QJ4cjsU) -> In this video we use Visual Studio to code an IOCTL driver for any version of Windows. The driver itself implements a custom way to read/write process memory. Alongside this we program a "user mode" application which can communicate with the driver to send it requests. This combination will effectively bypass most user mode anti-cheats out there.


<div id='windows-kernel-drivers-source-code'/>

#### ***Source Code***

Samples of kernel mode drivers.

* [Github: Windows driver samples](https://github.com/Microsoft/Windows-driver-samples) -> This repo contains driver samples prepared for use with Microsoft Visual Studio and the Windows Driver Kit (WDK). It contains both Universal Windows Driver and desktop-only driver samples.
* [Github: VectorKernel](https://github.com/daem0nc0re/VectorKernel) -> PoCs for Kernelmode rootkit techniques research or education. Currently focusing on Windows OS. All modules support 64bit OS only.
* [Github: Hidden](https://github.com/hfiref0x/TDL) -> Hidden has been developed like a solution for reverse engineering and researching tasks. This is a windows driver with a usermode interface which is used for hiding specific environment on your windows machine, like installed RCE programs (ex. procmon, wireshark), vm infrastructure (ex. vmware tools) and etc.
* [Web Back Engineering: Physmeme - Windows Unsigned Kernel Driver Mapper](https://blog.back.engineering/19/04/2020/) -> Physmeme is a driver mapper that works with any form of read and write to physical memory. It is highly modular code that allows a reverse engineer to easily integrate their own vulnerable driver. If you are able to read and write to physical memory you can now map an unsigned driver into your kernel just by coding four functions.
* [Github: Anti-Delete](https://github.com/NtRaiseHardError/Anti-Delete) -> Protects deletion of files with a specified extension using a kernel-mode driver.
* [Github: DisplayMiniportHooking](https://github.com/SHA-MRIZ/DisplayMiniportHooking) -> Port and miniport drivers are a concept that Microsoft uses to simplify the development of kernel code by different vendors. The port driver (Supplied by Microsoft) is responsible of performing common tasks and by that it helps vendors to avoid writing a lot of boilerplate code. Miniport drivers, supplied by third party vendors, are responsible for the execution tasks for a specific device. The miniport registers its callback functions with the port driver, which triggers them when needed.
* [Github: Blackout](https://github.com/ZeroMemoryEx/Blackout) -> Kill anti-malware protected processes (BYOVD) (Microsoft Won).


<div id='windows-kernel-drivers-reversing'/>

#### ***Reversing***

Explore the functional behavior of official drivers.


<div id='windows-kernel-drivers-reversing-basics'/>

##### ***Basics***

* [Blog: Mimidrv In Depth: Exploring Mimikatz's Kernel Driver](https://medium.com/@matterpreter/mimidrv-in-depth-4d273d19e148) -> Mimikatz provides the opportunity to leverage kernel mode functions through the included driver, Mimidrv. Mimidrv is a signed Windows Driver Model (WDM) kernel mode software driver meant to be used with the standard Mimikatz executable by prefixing relevant commands with an exclamation point (!). Mimidrv is undocumented and relatively underutilized, but provides a very interesting look into what we can do while operating at ring 0.
* [Blog: Methodology for Static Reverse Engineering of Windows Kernel Drivers](https://medium.com/@matterpreter/methodology-for-static-reverse-engineering-of-windows-kernel-drivers-3115b2efed83) -> Attacks against Windows kernel mode software drivers, especially those published by third parties, have been popular with many threat groups for a number of years. Popular and well-documented examples of these vulnerabilities are the CAPCOM.sys arbitrary function execution, Win32k.sys local privilege escalation, and the EternalBlue pool corruption. Exploiting drivers offers interesting new perspectives not available to us in user mode, both through traditional exploit primitives and abusing legitimate driver functionalities.
* [Blog: Windows kernel driver static reverse using IDA and GHIDRA](https://v1k1ngfr.github.io/winkernel-reverse-ida-ghidra/) -> Here are some notes for Windows drivers reverse enginering noob. This topic is already covered and you can find many resources on Internet, here we will use IDA and GHIDRA and observe differences.


<div id='windows-kernel-drivers-reversing-videos'/>

##### ***Videos***

* [Youtube Video: Nir Lichtman - Reverse Engineering Simple Windows Driver](https://www.youtube.com/watch?v=cabuolISweY) -> In this video I will demonstrate how you can reverse engineer a simple "Hello, World" driver on Windows 10.
* [Presentation: REcon 2015 - Reverse Engineering Windows AFD.sys (Steven Vittitoe)](https://recon.cx/2015/slides/recon2015-20-steven-vittitoe-Reverse-Engineering-Windows-AFD-sys.pdf)
* [Youtube Video: REcon 2015 - Reverse Engineering Windows AFD.sys (Steven Vittitoe)](https://www.youtube.com/watch?v=2sPNUpfTJ5A) -> What happens when you make a socket() call in Windows? This presentation will briefly walk through the rather well documented winsock user mode framework before diving into the turmoil of ring 0. There is no map to guide us here. Our adventure will begin where MSDN ends and our first stop along the way is with an IOCTL to AFD.sys, or the awkwardly named ancillary function driver. This driver is of particular interest because it is so widely used and yet most people that use it do not even know it exists. Nearly every Windows program managing sockets depends on this driver. Even more interesting is that the device created by AFD.sys is accessible from every sandbox Google Project Zero looked at. In fact, there isn't even support to restrict access to this device until Windows 8.1. Staying true to Windows style AFD.sys is a complex driver with over 70 reachable IOCTL's and support for everything from SAN to TCP. It is no wonder that this driver weighs in at 500KB. This complexity combined with accessibility breed a robust ring 0 attack surface. Current fuzzing efforts will also be shared in this presentation and the time we are done you should have a good idea of what happens when making a socket() call without having to spend hours in IDA to figure it out.


<div id='windows-kernel-drivers-fuzzing'/>

#### ***Fuzzing***

Identify vulnerabilities in those drivers.


<div id='windows-kernel-drivers-fuzzing-basics'/>

##### ***Basics***

* [Web Check Point: Bugs on the Windshield - Fuzzing the Windows Kernel](https://research.checkpoint.com/2020/bugs-on-the-windshield-fuzzing-the-windows-kernel/) -> In our previous research, we used WinAFL to fuzz user-space applications running on Windows, and found over 50 vulnerabilities in Adobe Reader and Microsoft Edge. For our next challenge, we decided to go after something bigger: fuzzing the Windows kernel. As an added bonus, we can take our user-space bugs and use them together with any kernel bugs we find to create a full chain – because RCEs without a sandbox escape/privilege escalation are pretty much worthless nowadays.
* [Web CyberArk: Finding Bugs in Windows Drivers, Part 1 – WDM](https://www.cyberark.com/resources/threat-research-blog/finding-bugs-in-windows-drivers-part-1-wdm) -> Finding vulnerabilities in Windows drivers was always a highly sought-after prize by sophisticated threat actors, game cheat writers and red teamers. As you probably know, every bug in a driver is, in essence, a bug in the Windows kernel, as every driver shares the memory space of the kernel. Don't get me started about user-mode drivers, as they are not interesting. Thus, having the capability to either run code in the kernel, read and write from the model registers, or duplicate privileged access tokens is really all you need to own the system. This two-part blog series will go through the methodology of finding vulnerabilities in WDM drivers, followed by utilizing kernel fuzzing via kAFL. We won't go through other frameworks and models since they are either too niche (looking at your WIA mini driver) or too complicated (looking at you, NDIS). Most bugs seem to be in WDM or in KMDF (might visit KMDF in a future blogpost). In the second blog, timed for RSA Conference in San Francisco, we will talk about kernel fuzzing via kAFL and Intel PT, combining the expertise of low-level reversing, manual vulnerability research with the strong engine of kAFL, alongside using grammar-based fuzzing, which results in finding multiple vulnerabilities.


<div id='windows-kernel-drivers-fuzzing-videos'/>

##### ***Videos***

* [Youtube Video: HackInTheBox 2019 - The Art Of The Windows Kernel Fuzzing](https://www.youtube.com/watch?v=9FPuKfwucsw) -> Over the year, the Windows kernel has been enhanced through a variety of kernel security additions making it harder for security researchers to find kernel issues, bugs, and exploits. This talk will cover the art of the kernel fuzzing and a tool I developed to aid security researchers in kernel fuzzing. I will introduce a new method of fuzzing Windows kernels, demonstrate the fuzzing framework and how it works.


<div id='windows-kernel-drivers-fuzzing-tools'/>

##### ***Tools***

* [Github: MS Fuzz - Targeting Windows Kernel Driver Fuzzer](https://github.com/0dayResearchLab/msFuzz) -> MS Fuzzer is coverage-guided Fuzzer that is targeting Windows Kernel Driver.
* [Github: kAFL - A fuzzer for full VM kernel/driver targets](https://github.com/IntelLabs/kAFL) -> kAFL/Nyx is a fast guided fuzzer for the x86 VM. It is great for anything that executes as QEMU/KVM guest, in particular x86 firmware, kernels and full-blown operating systems.
* [Web Ssdeep Project: Ssdeep - Fuzzy hashing program](https://ssdeep-project.github.io/ssdeep/index.html) -> Ssdeep is a program for computing context triggered piecewise hashes (CTPH). Also called fuzzy hashes, CTPH can match inputs that have homologies. Such inputs have sequences of identical bytes in the same order, although bytes in between these sequences may be different in both content and length.


<div id='windows-kernel-drivers-exploitation'/>

#### ***Exploitation***

Take advantage of the vulnerabilities.


<div id='windows-kernel-drivers-exploitation-basics'/>

##### ***Basics***

* [Web CrowdStrike: The Current State of Exploit Development, Part 1](https://www.crowdstrike.com/blog/state-of-exploit-development-part-1/) -> In Part 1, we addressed binary exploitation on Windows systems, including some legacy and contemporary mitigations that exploit writers and adversaries must deal with in today's cyber landscape.
* [Web CrowdStrike: The Current State of Exploit Development, Part 2](https://www.crowdstrike.com/blog/state-of-exploit-development-part-2/) -> In Part 2, we will walk through more of the many mitigations Microsoft has put in place.
* [Web VMWare: Hunting Vulnerable Kernel Drivers](https://blogs.vmware.com/security/2023/10/hunting-vulnerable-kernel-drivers.html) -> In information security, even seemingly insignificant issues could pose a significant threat. One notable vector of attack is through device drivers used by legitimate software developers. There are numerous available drivers to support legacy hardware in every industry, some of which are from businesses that have long stopped supporting the device. To continue operations, organizations rely upon these deprecated device drivers.
* [Web Vuln Dev: Windows Kernel Exploitation – Arbitrary Memory Mapping (x64)](https://vuln.dev/2022/09/24/windows-kernel-exploitation-arbitrary-memory-mapping-x64/) -> In this post, we will develop an exploit for the HW driver. I picked this one because I looked for some real-life target to practice on and saw a post by Avast that mentioned vulnerabilities in an old version of this driver (Version 4.8.2 from 2015), that was used as part of a bigger exploit chain. Unfortunately, I could not find this one available for download so I ended up using the most recent version, 4.9.8 at the time of writing this post. This driver is signed by Microsoft so we can load it even without a kernel debugger attached (the certificate is expired since 2021 but that does not really prevent loading).
* [Web Connor McGarr: Exploit Development CVE-2021-21551 - Dell 'dbutil_2_3.sys' Kernel Exploit Writeup](https://connormcgarr.github.io/cve-2020-21551-sploit/) -> I stumbled across this SentinelOne blog post the other day, which outlined a few vulnerabilities in Dell's dbutil_2_3.sys driver, including a memory corruption vulnerability. Although this vulnerability was attributed to Kasif Dekel, it apparently was discovered earlier by Yarden Shafir and Staoshi Tanda, coworkers of mine at CrowdStrike.
* [Blog: Windows Kernel Exploitation HEVD on Windows 10 22H2](https://medium.com/@ommadawn46/windows-kernel-exploitation-hevd-on-windows-10-22h2-b407c6f5b8f7) -> In this article, I'll share the insights I've gained from self-studying Windows kernel exploitation.
* [Web Fluid Attacks: HEVD - kASLR + SMEP Bypass](https://fluidattacks.com/blog/hevd-smep-bypass/) -> During the last posts, we've been dealing with exploitation in Windows Kernel space. We are using HackSys Extremely Vulnerable Driver or HEVD as the target which is composed of several vulnerabilities to let practitioners sharpen the Windows Kernel exploitation skills.


<div id='windows-kernel-drivers-exploitation-videos'/>

##### ***Videos***

* [Youtube Video: Off By One Security - A Look at Modern Windows Kernel Exploitation/Hacking](https://www.youtube.com/watch?v=7Trgnw7HkeE) -> Connor McGarr takes us through the state of exploitation and exploit mitigations on modern Windows systems.
* [Presentation: HackInTheBox 2023 - A Deep Dive Into Two Windows Exploits Demonstrated At Pwn2Own](https://conference.hitb.org/hitbsecconf2023hkt/materials/D2T1%20-%20Windows%20Kernel%20Security%20-%20A%20Deep%20Dive%20into%20Two%20Exploits%20Demonstrated%20at%20Pwn2Own%20-%20Thomas%20Imbert.pdf)
* [Youtube Video: HackInTheBox 2023 - A Deep Dive Into Two Windows Exploits Demonstrated At Pwn2Own](https://www.youtube.com/watch?v=d0I-UOQHCVs) -> Windows kernel exploitation is a fascinating and challenging field of research that draws the attention of security researchers and attackers alike. The Windows kernel and its drivers are a vast and complex code base that offers many opportunities for discovering and exploiting vulnerabilities that can lead to system compromise and security mechanisms bypasses. This talk will explore the current state and evolution of Windows kernel security by analyzing and revealing two new exploits that were demonstrated at Pwn2Own this year, showing how kernel code execution was achieved on the latest versions of Windows.
* [Youtube Video: Off By One Security - Windows Device Drivers Internals and some Reversing](https://www.youtube.com/watch?v=7Trgnw7HkeE) -> In this session we'll look at how drivers and devices work in Windows, examine data structures and I/O requests. We'll use kernel debugging and other tools to figure out what a driver of interest is doing.


<div id='windows-kernel-drivers-exploitation-tools'/>

##### ***Tools***

* [Github: HackSys Extreme Vulnerable Driver](https://github.com/hacksysteam/HackSysExtremeVulnerableDriver) -> The HackSys Extreme Vulnerable Driver (HEVD) is a Windows Kernel driver that is intentionally vulnerable. It has been developed for security researchers and enthusiasts to improve their skills in kernel-level exploitation. HEVD offers a range of vulnerabilities, from simple stack buffer overflows to more complex issues such as use-after-free, pool buffer overflows, and race conditions. This allows researchers to explore exploitation techniques for each implemented vulnerability.
* [Github: KDMapper - Exploits iqvw64e.sys Intel driver](https://github.com/TheCruZ/kdmapper) -> KDMapper is a simple tool that exploits iqvw64e.sys Intel driver to manually map non-signed drivers in memory.


<div id='windows-kernel-tools'/>

### ***Tools***

Study and examine kernel components.

* [Web Microsoft: WinDbg](https://learn.microsoft.com/en-us/windows-hardware/drivers/debugger/) -> WinDbg is a debugger that can be used to analyze crash dumps, debug live user-mode and kernel-mode code, and examine CPU registers and memory.
* [Github: DumpScan](https://github.com/daddycocoaman/dumpscan) -> Finding secrets in kernel and user memory.
* [Web Microsoft: Sysinternals Suite](https://learn.microsoft.com/en-us/sysinternals/downloads/sysinternals-suite) -> The Sysinternals Troubleshooting Utilities have been rolled up into a single Suite of tools. This file contains the individual troubleshooting tools and help files. It does not contain non-troubleshooting tools like the BSOD Screen Saver.
* [Web SourceForge: Process Hacker](https://processhacker.sourceforge.io/) -> A free, powerful, multi-purpose tool that helps you monitor system resources, debug software and detect malware.
* [Github: Capa - The FLARE team's open-source tool to identify capabilities in executable files](https://github.com/mandiant/capa) -> Capa detects capabilities in executable files. You run it against a PE, ELF, .NET module, shellcode file, or a sandbox report and it tells you what it thinks the program can do. For example, it might suggest that the file is a backdoor, is capable of installing services, or relies on HTTP to communicate.


---
---
---


<div id='rootkits'/>

## ***Rootkits***

The most advanced malware that infects the operating system kernel, which remains undetectable.


<div id='rootkits-basics'/>

### ***Basics***

What is a rootkit exactly? Are they Kernel Mode Drivers?

* [Web Kaspersky: What is a Rootkit - Definition and Explanation](https://www.kaspersky.com/resource-center/definitions/what-is-rootkit) -> A rootkit is a type of malware designed to give hackers access to and control over a target device. Although most rootkits affect the software and the operating system, some can also infect your computer's hardware and firmware. Rootkits are adept at concealing their presence, but while they remain hidden, they are active.
* [Web CyberArk: Fantastic Rootkits - And where to find them part 1](https://www.cyberark.com/resources/threat-research-blog/fantastic-rootkits-and-where-to-find-them-part-1) -> We will focus on some implementation examples of basic rootkit functionality and the basics of kernel driver development, as well as Windows Internals background needed to understand the inner workings of rootkits.
* [Web CyberArk: Fantastic Rootkits - And where to find them part 2](https://www.cyberark.com/resources/threat-research-blog/fantastic-rootkits-and-where-to-find-them-part-2) -> We will focus on kernel rootkit analysis, looking at two case studies of rootkits found in the wild: Husky Rootkit and Mingloa/CopperStealer Rootkit. Through these case studies, we'll share our insights about rootkit analysis techniques and methodology.
* [Web CyberArk: Fantastic Rootkits - And where to find them part 3](https://www.cyberark.com/resources/threat-research-blog/fantastic-rootkits-and-where-to-find-them-part-3-arm-edition) -> In this blog, we will discuss innovative rootkit techniques on a non-traditional architecture, Windows 11 on ARM64.
* [Web JumpSec Labs: A Defender's Guide For Rootkit Detection](https://labs.jumpsec.com/a-defenders-guide-for-rootkit-detection-episode-1-kernel-drivers/) -> Rootkits have been one of the most sophisticated and successful ways of obtaining persistence on a machine, and now in 2020 there are ever more trivial ways of escalating from system to kernel.
* [Web OpenSecurityTraining: Rootkits - What they are and how to find them part 1](https://opensecuritytraining.info/Rootkits_files/Rootkits-Part1.ppt.pdf) -> Hooking.
* [Web OpenSecurityTraining: Rootkits - What they are and how to find them part 2](https://opensecuritytraining.info/Rootkits_files/Rootkits-Part2.ppt.pdf) -> System Calls.
* [Web OpenSecurityTraining: Rootkits - What they are and how to find them part 3](https://opensecuritytraining.info/Rootkits_files/Rootkits-Part3.ppt.pdf) -> Forensic Analysis.


<div id='rootkits-videos'/>

### ***Videos***

Watch these videos to understand how to develop this malware with advanced features.

* [Youtube Video: GuidedHacking - How to make a Kernel Driver](https://www.youtube.com/watch?v=9h1FsOISwX0) -> This tutorial series will teach you everything you need to make a kernel driver on Windows.
* [Youtube Video: Sourcefire - Defense via Hook Detection](https://www.youtube.com/watch?v=CWZ-dShnBFA) -> Since both kernel-mode and user-mode rootkits use hooking as a vehicle for hiding their presence on a system, it seems only natural that looking for system hooks could itself be used to identify the presence of a rootkit on a system.
* [Presentation: Bsides Lisbon 2022 - Windows kernel rootkits for red teams](https://bsideslisbon.org/assets/2022/materials/Andre_Lima_Windows_Kernel_Rootkits.pdf)
* [Youtube Video: Bsides Lisbon 2022 - Windows kernel rootkits for red teams](https://www.youtube.com/watch?v=GM9WQMrSkWk) -> In this talk, the focus is on key aspects of developing within the kernel environment, with a particular emphasis on considerations for creating malware targeting the Windows kernel.
* [Presentation: BlackHat USA 2020 - Demystifying Modern Windows Rootkits](https://i.blackhat.com/USA-20/Wednesday/us-20-Demirkapi-Demystifying-Modern-Windows-Rootkits.pdf)
* [Youtube Video: BlackHat USA 2020 - Demystifying Modern Windows Rootkits](https://www.youtube.com/watch?v=ZASsIpdumcY) -> This talk will demystify the process of writing a rootkit, moving past theory and instead walking the audience through the process of going from a driver that says "Hello World" to a driver that abuses never-before-seen hooking methods to control the user-mode network stack.
* [Youtube Video: BlackHat USA 2020 - The Art of Emulating Kernel Rootkits](https://www.youtube.com/watch?v=Zh_Dfd-ukEQ) -> Kernel rootkit is considered the most dangerous malware that may infect computers. Operating at ring 0, the highest privilege level in the system, this super malware has unrestricted power to control the whole machine, thus can defeat all the defensive and monitoring mechanisms.


<div id='rootkits-source-code'/>

### ***Source Code***

Complex examples of this malware.

* [Github: Bentico](https://github.com/TheMalwareGuardian/Bentico) -> Bentico is a comprehensive project thoroughly designed with the explicit goal of establishing a robust foundation for the development of rootkits. By offering a centralized repository of knowledge, Bentico stands as a valuable initiative for anyone looking to contribute to and benefit from the collective understanding of this field.
* [Github: Nidhogg](https://github.com/Idov31/Nidhogg) -> Nidhogg is a multi-functional rootkit to showcase the variety of operations that can be done from kernel space. The goal of Nidhogg is to provide an all-in-one and easy-to-use rootkit with multiple helpful functionalities for operations. Besides that, it can also easily be integrated with your C2 framework.
* [Github: Black Angel](https://github.com/XaFF-XaFF/Black-Angel-Rootkit) -> lack Angel is a Windows 11/10 x64 kernel mode rootkit. Rootkit can be loaded with enabled DSE while maintaining its full functionality.
* [Github: Cronos](https://github.com/XaFF-XaFF/Cronos-Rootkit) -> Cronos is Windows 10/11 x64 ring 0 rootkit. Cronos is able to hide processes, protect and elevate them with token manipulation.
* [Github: Spectre](https://github.com/D4stiny/spectre) -> Windows kernel-mode rootkit that abuses legitimate communication channels to control a machine. Hiding Processes, token manipulation , hiding tcp network connections by port...
* [Blog: Eagle](https://memn0ps.github.io/rusty-windows-kernel-rootkit/) -> This post will go through some of the basic rootkit techniques, using one of the first publicly available rootkits made in Rust as a proof of concept. Many anti-cheats and EDRs are utilizing Windows kernel drivers using rootkit-like techniques to detect game hackers or adversaries. However, this is a cat and mouse game, and the game hackers and malware authors have been years ahead of the industry. Why was this made? For fun, learning, to demonstrate the power of Rust and because Rust is awesome. This post assumes that the reader understands the basics of how Windows Kernel programming and how device drivers work.
* [Github: Eagle](https://github.com/memN0ps/rootkit-rs/) -> Windows Kernel Rookit in Rust (Rusty Rootkit).
* [Github: ZwHawk](https://github.com/eLoopWoo/zwhawk) -> A kernel rootkit with remote command and control interface for windows.
* [Github: www.rootkit.com mirror](https://github.com/skykami/www.rootkit.com) -> www.rootkit.com users section mirror, sql database dump, and a few other files/rootkits.
* [Github: TDL (Turla Driver Loader)](https://github.com/hfiref0x/TDL) -> Driver loader for bypassing Windows x64 Driver Signature Enforcement.
* [Github: Autochk Rootkit](https://github.com/repnz/autochk-rootkit) -> Reverse engineered source code of the autochk rootkit.
* [Github: Reptile](https://github.com/f0rb1dd3n/Reptile) -> LKM Linux rootkit.


<div id='rootkits-techniques'/>

### ***Techniques***

Obfuscation and persistence techniques applied by this malware.


<div id='rootkits-techniques-dkom'/>

#### ***Direct Kernel Object Modification (DKOM)***


<div id='rootkits-techniques-dkom-basics'/>

##### ***Basics***

* [Web RedTeamNotes: Manipulating ActiveProcessLinks to Hide Processes in Userland](https://www.ired.team/miscellaneous-reversing-forensics/windows-kernel-internals/manipulating-activeprocesslinks-to-unlink-processes-in-userland) -> The purpose of this lab is to look into how Windows kernel rootkits hide / unlink (or used to) processes in the userland for utilities trying to list all running processes on the system such as Windows Task Manager, tasklist or Get-Process cmdlet in Powershell.
* [Youtube Video: Sourcefire - Direct Kernel Object Manipulation](https://www.youtube.com/watch?v=dUAV9Vrwkow)
* [Presentation: BlackHat USA 2004 - DKOM (Direct Kernel Object Manipulation)](https://www.blackhat.com/presentations/bh-europe-04/bh-eu-04-butler.pdf)
* [Youtube Video: BlackHat USA 2004 - DKOM (Direct Kernel Object Manipulation)](https://www.youtube.com/watch?v=1Ie20b5IGgY)

* [Web NixHacker: Understanding Windows DKOM techniques](https://nixhacker.com/understanding-windows-dkom-direct-kernel-object-manipulation-attacks-eprocess/) -> The Windows Kernel uses the EPROCESS structure to represent a process, and it contains all the information that the kernel needs to maintain about the process.
* [Blog: Direct Kernel Object Manipulation and Processes](https://bsodtutorials.wordpress.com/2014/01/27/rootkits-direct-kernel-object-manipulation-and-processes/) -> DKOM is one of the methods commonly used and implemented by Rootkits, in order to remain undetected, since this the main purpose of a roottkit. To be able to access Kernel-Mode code and data structures without detection from security programs or tools used by security analysts and researchers. 


<div id='rootkits-techniques-dkom-pocs'/>

##### ***POCs***

* [Github: DKOM](https://github.com/slava-aes/DKOM) -> Windows 10 Direct Kernel Object Manipulation.
* [Github: Win_Rootkit](https://github.com/alal4465/Win_Rootkit) -> A kernel-mode rootkit with remote control that utilizes C++ Runtime in it's driver. Uses DKOM and IRP Hooks.
* [Github: HideProcess](https://github.com/landhb/HideProcess) -> A basic Direct Kernel Object Manipulation rootkit that removes a process from the EPROCESS list, hiding it from the Task Manager.
* [Github: HideDriver](https://github.com/nbqofficial/HideDriver) -> Using DKOM to hide kernel mode drivers.
* [Github: Rootkit DKOM](https://github.com/YuriFA/DKOM) -> Direct Kernel Object Manipulationon _EPROCESS internal structure.


<div id='rootkits-techniques-idthooking'/>

#### ***Interrupt Descriptor Table (IDT) Hooking***


<div id='rootkits-techniques-idthooking-basics'/>

##### ***Basics***

* [Web RedTeamNotes: Interrupt Descriptor Table (IDT)](https://www.ired.team/miscellaneous-reversing-forensics/windows-kernel-internals/interrupt-descriptor-table-idt) -> Interrupts could be thought of as notifications to the CPU that tells it that some event happened on the system. Classic examples of interrupts are hardware interrupts such as mouse button or keyboard key presses, network packet activity and hardware generated exceptions such as a division by zero or a breakpoint - interrupts 0x00 and 0x03 respectively.
* [Web MIT: Interrupt Descriptor Table](https://pdos.csail.mit.edu/6.828/2008/readings/i386/s09_04.htm) -> The interrupt descriptor table (IDT) associates each interrupt or exception identifier with a descriptor for the instructions that service the associated event. Like the GDT and LDTs, the IDT is an array of 8-byte descriptors. Unlike the GDT and LDTs, the first entry of the IDT may contain a descriptor.
* [Youtube Video OpenSecurityTraining: Interrupt Descriptor Table](https://www.youtube.com/watch?v=cFdOJ6coVvQ)


<div id='rootkits-techniques-idthooking-pocs'/>

##### ***POCs***

* [Github: Windows x86 Interrupt Descriptor Table (IDT) hooking driver](https://gist.github.com/Barakat/89002a26937a2da353868fc5130812a5)
* [Github: IDTHOOK](https://github.com/LLLZed/IDTHOOK)
* [Github: x64-IDT-HOOK](https://github.com/haidragon/x64-IDT-HOOK)
* [Github: IDTHook_X64](https://github.com/DOGSHITD/IDTHook_X64) - > Hook IDT vector 0xb2 to detect SCI in 64bit windows. 


<div id='rootkits-techniques-ssdthooking'/>

#### ***System Service Descriptor Table (SSDT) Hooking***


<div id='rootkits-techniques-ssdthooking-basics'/>

##### ***Basics***

* [Web RedTeamNotes: System Service Descriptor Table (SSDT)](https://www.ired.team/miscellaneous-reversing-forensics/windows-kernel-internals/glimpse-into-ssdt-in-windows-x64-kernel) -> System Service Dispatch Table or SSDT, simply is an array of addresses to kernel routines for 32 bit operating systems or an array of relative offsets to the same routines for 64 bit operating systems. SSDT is the first member of the Service Descriptor Table kernel memory structure.
* [Web Infosec: Hooking the System Service Dispatch Table (SSDT)](https://resources.infosecinstitute.com/topics/hacking/hooking-system-service-dispatch-table-ssdt/) -> In this article we'll present how we can hook the System Service Dispatch Table, but first we have to establish what the SSDT actually is and how it is used by the operating system.
* [Web AppsVoid: SSDT View](https://www.appsvoid.com/products/ssdt-view/) -> SSDT View is a Windows OS utility designed to list the most significant aspects of the System Service Descriptor Table (SSDT) including system service indexes, system service addresses, system service names and the module name which corresponds to the system service address.


<div id='rootkits-techniques-ssdthooking-pocs'/>

##### ***POCs***

* [Github: MasterHide](https://github.com/crvvdev/MasterHide) -> A x64 Windows Driver created to monitor/hide or block access from processes, objects, files (whatever you want, your imagination is the limit here) using SSDT/Shadow SSDT hooks.
* [Github: TitanHide](https://github.com/mrexodia/TitanHide) -> A driver intended to hide debuggers from certain processes. The driver hooks various Nt* kernel functions (using SSDT table hooks) and modifies the return values of the original functions.
* [Github: STrace](https://github.com/mandiant/STrace) -> A DTrace on windows syscall hook reimplementation. Think of this like a patchguard compatible SSDT hook, but without hacks.


<div id='windows-kernel-tools'/>

### ***Tools***

Rootkit scanners.

* [Web Gmer: Rootkit Detector and Remover](http://www.gmer.net/) -> It is an application that detects and removes rootkits.
* [Web Microsoft: RootkitRevealer v1.71](https://learn.microsoft.com/en-us/sysinternals/downloads/rootkit-revealer) -> RootkitRevealer is an advanced rootkit detection utility. It runs on Windows XP (32-bit) and Windows Server 2003 (32-bit), and its output lists Registry and file system API discrepancies that may indicate the presence of a user-mode or kernel-mode rootkit. RootkitRevealer successfully detects many persistent rootkits including AFX, Vanquish and HackerDefender (note: RootkitRevealer is not intended to detect rootkits like Fu that don't attempt to hide their files or registry keys). If you use it to identify the presence of a rootkit please let us know!


---
---
---


<div id='lab'/>

## ***Lab***

Build a testing environment.


<div id='lab-bootkits-develop'/>

### ***Bootkits (Development)***

Build an environment to develop Bootkits (UEFI/DXE Applications and Drivers).

* [Web Microsoft: Visual Studio 2019 Community](https://download.visualstudio.microsoft.com/download/pr/190b8b27-9da7-49b4-bb27-75d3a5abe45e/7f99a0b51add7cef022790ca1bde2819acf0301e5566572a8b325218e1c6fad7/vs_Community.exe) -> Free, fully-featured IDE for students, open-source and individual developers.
* [Web Git](https://git-scm.com/download/win) -> Git is a free and open source distributed version control system designed to handle everything from small to very large projects with speed and efficiency.
* [Web Python: Python 3.9](https://www.python.org/downloads/release/python-390/) -> This is the stable release of Python 3.9.0.
* [Web NASM: Netwide Assembler](https://www.nasm.us/) -> This is the project webpage for the Netwide Assembler (NASM), an asssembler for the x86 CPU architecture portable to nearly every modern platform, and with code generation for many platforms old and new.
* [Web Intel: ACPI Component Architecture Downloads (Windows* Binary Tools)](https://www.intel.com/content/www/us/en/download/774881/acpi-component-architecture-downloads-windows-binary-tools.html) -> The Window* versions of the various tools are zipped in a single file.
* [Github: EDK II Project](https://github.com/tianocore/tianocore.github.io/wiki/Windows-systems) -> A modern, feature-rich, cross-platform firmware development environment for the UEFI and PI specifications from www.uefi.org.


<div id='lab-windows-kernel-debugging'/>

### ***Windows Kernel (Debugging)***

Build an environment to debug the Windows kernel.

* [Web Microsoft: Install the Windows debugger](https://learn.microsoft.com/en-us/windows-hardware/drivers/debugger/) -> WinDbg is a debugger that can be used to analyze crash dumps, debug live user-mode and kernel-mode code, and examine CPU registers and memory.
* [Web Microsoft: BCDEdit /debug](https://learn.microsoft.com/en-us/windows-hardware/drivers/devtest/bcdedit--debug) -> The /debug boot option enables or disables kernel debugging of the Windows operating system associated with the specified boot entry or the current boot entry.


<div id='lab-rootkits-develop'/>

### ***Rootkits (Development)***

Build an environment to develop Rootkits (Kernel Mode Drivers).

* [Web Microsoft: Visual Studio 2022 Community](https://c2rsetup.officeapps.live.com/c2r/downloadVS.aspx?sku=community&channel=Release&version=VS2022&source=VSLandingPage&cid=2030:0bb331a3920e45219dfb2d6b4fd8e0c0) -> Free, fully-featured IDE for students, open-source and individual developers.
* [Web Microsoft: Windows SDK](https://developer.microsoft.com/en-us/windows/downloads/windows-sdk/) -> The Windows SDK (10.0.26100) for Windows 11 provides the latest headers, libraries, metadata, and tools for building Windows applications. Use this SDK to build Universal Windows Platform (UWP) and Win32 applications for Windows 11, version 24H2 preview and previous Windows releases.
* [Web Microsoft: Download the Windows Driver Kit (WDK)](https://learn.microsoft.com/en-us/windows-hardware/drivers/download-the-wdk) -> The WDK is used to develop, test, and deploy drivers for Windows.
* [Web Microsoft: Other WDK downloads](https://learn.microsoft.com/en-us/windows-hardware/drivers/other-wdk-downloads) -> The Windows Driver Kit (WDK) is used to develop, test, and deploy Windows Drivers. This topic contains information about versions of the Windows Driver Kit (WDK), Enterprise WDK (EWDK), and additional downloads for support purposes. To develop drivers, use the latest public versions of the Windows Driver Kit (WDK) and tools, available for download on Download the Windows Driver Kit (WDK).
* [Web Visual Studio Marketplace: Windows Driver Kit Visual Studio Extension (WDKVsix)](https://marketplace.visualstudio.com/items?itemName=DriverDeveloperKits-WDK.WDKVsix) -> Welcome to the Windows Driver Kit (WDK) Visual Studio Extension package! This extension package includes essential Visual Studio extensions, Driver Project Templates, and MSBuild Toolset files designed to enable Driver Projects to build using the MSBuild toolset shipped with Visual Studio.


---
---
---


<div id='books'/>

## ***Books***

Key readings to excel in this field.

* [Windows Internals - Russinovich, M., Solomon, D., Ionescu, A. & Yosifovich, P. - Microsoft Press. - (Part 1: 50€, Part 2: 55€)](https://learn.microsoft.com/en-us/sysinternals/resources/windows-internals) -> Architecture and core internals of Windows.
* [Beyond BIOS: Developing with the Unified Extensible Firmware Interface - Marisetty, S., Rothman, M., & Zimmer, V. - Intel Press. - (66,55€)](https://www.amazon.es/Beyond-BIOS-Developing-Extensible-Interface/dp/1501514784) -> This book provides an overview of modern boot firmware, including the Unified Extensible Firmware Interface (UEFI) and its associated EFI Developer Kit II (EDKII) firmware.
* [Rootkits and Bootkits: Reversing Modern Malware and Next Generation Threats - Matrosov, A., Rodionov, E., & Bratus, S. - No Starch Press. - (40€)](https://www.amazon.es/Rootkits-Bootkits-Reversing-Malware-Generation/dp/1593277164) -> Rootkits and Bootkits will teach you how to understand and counter sophisticated, advanced threats buried deep in a machine's boot process or UEFI firmware.
* [The Rootkit Arsenal: Escape and Evasion in the Dark Corners of the System - Blunden, B. - Jones & Bartlett Learning. - (85€)](https://www.amazon.es/Rootkit-Arsenal-Escape-Evasion-Corners/dp/144962636X) -> While forensic analysis has proven to be a valuable investigative tool in the field of computer security, utilizing anti-forensic technology makes it possible to maintain a covert operational foothold for extended periods, even in a high-security environment. Adopting an approach that favors full disclosure, the updated Second Edition of The Rootkit Arsenal presents the most accessible, timely, and complete coverage of forensic countermeasures.
* [Rootkits: Subverting the Windows Kernel - Hoglund, G., & Butler, J. - Addison-Wesley. - (50€)](https://www.amazon.es/Rootkits-Subverting-Windows-Greg-Hoglund/dp/0321294319) -> It's imperative that everybody working in the field of cyber-security read this book to understand the growing threat of rootkits.
<!-- https://libgen.unblockninja.com/ -->


---
---
---


<div id='cybersecurity-resources'/>

## ***Cybersecurity resources***

Additional cybersecurity resources that will assist you in developing bootkits/rootkits.

* [Github: Awesome](https://github.com/sindresorhus/awesome) -> Awesome lists about all kinds of interesting topics.
* [Github: The Book of Secret Knowledge](https://github.com/trimstray/the-book-of-secret-knowledge) -> A collection of inspiring lists, manuals, cheatsheets, blogs, hacks, one-liners, cli/web tools and more.
* [Github: Advanced Windows Exploit Development Resources](https://github.com/FULLSHADE/WindowsExploitationResources) -> Some resources, links, books, and papers related to mostly Windows Internals and anything Windows kernel related.
* [Github: Awesome Windows Kernel Security Development](https://github.com/ExpLife0011/awesome-windows-kernel-security-development) -> Some resources related to Windows kernel development.
* [Github: Awesome Malware Analysis](https://github.com/rshipp/awesome-malware-analysis) -> A curated list of awesome malware analysis tools and resources.
* [Github: Awesome Reverse Engineering](https://github.com/alphaSeclab/awesome-reverse-engineering/blob/master/Readme_full_en.md) -> Reverse Engineering Resources About All Platforms(Windows/Linux/macOS/Android/iOS/IoT) And Every Aspect! (More than 3500 open source tools and 2300 posts&videos).
* [Github: Awesome Bootkits & Rootkits Development](https://github.com/TheMalwareGuardian/Awesome-Bootkits-Rootkits-Development) -> A curated compilation of extensive resources dedicated to bootkit and rootkit development.
* [Github: Awesome Infosec](https://github.com/onlurking/awesome-infosec) -> A curated list of awesome infosec courses and training resources.
* [Github: Awesome Hacking](https://github.com/Hack-with-Github/Awesome-Hacking) -> A collection of various awesome lists for hackers, pentesters and security researchers.
* [Github: Awesome Penetration Testing](https://github.com/enaqx/awesome-pentest) -> A collection of awesome penetration testing resources, tools and other shiny things.
* [InfoSec Reference](https://github.com/rmusser01/Infosec_Reference) -> An Information Security Reference That Doesn't Suck.
* [Github: Payloads All The Things](https://github.com/swisskyrepo/PayloadsAllTheThings) -> A list of useful payloads and bypass for Web Application Security and Pentest/CTF.
* [Web Red Team Notes](https://www.ired.team/) -> These are notes about all things focusing on, but not limited to, red teaming and offensive security.
* [Web Book HackTricks](https://book.hacktricks.xyz/) -> Welcome to the wiki where you will find each hacking trick/technique/whatever I have learnt from CTFs, real life apps, reading researches, and news.
* [Github: Awesome RedTeam Cheatsheet](https://github.com/RistBS/Awesome-RedTeam-Cheatsheet) -> Red Team Cheatsheet in constant expansion.
* [Github: Awesome UEFI Security](https://github.com/river-li/awesome-uefi-security) -> A collection of papers/tools/exploits for UEFI security.
* [Web SamsClass Info: Full-Stack Incident Response](https://samsclass.info/152/FSIR2021.htm) -> Sam Bowne.
* [Github: Awesome EDR Bypass](https://github.com/tkmru/awesome-edr-bypass) -> EDR bypass technology is not just for attackers. Many malware now have EDR bypass capabilities, knowledge that pentesters and incident responders should also be aware of. This repository is not intended to be used to escalate attacks. Use it for ethical hacking.
* [Github: Hooking](https://github.com/alphaSeclab/hooking/blob/master/Readme_en.md) -> Resources About Hooking. For All Platforms. Currently 300+ Tools And 600+ Posts.
* [Github: Awesome Industrial Control System Security](https://github.com/hslatman/awesome-industrial-control-system-security) -> A curated list of resources related to Industrial Control System (ICS) security.
* [Github: Awesome Honeypots](https://github.com/paralax/awesome-honeypots) -> A curated list of awesome honeypots, plus related components and much more, divided into categories such as Web, services, and others, with a focus on free and open source projects.
* [Github: Awesome OSINT](https://github.com/jivoi/awesome-osint) -> A curated list of amazingly awesome OSINT.
* [Github: Cyber Detective's OSINT tools collection](https://github.com/cipher387/osint_stuff_tool_collection) -> A collection of several hundred online tools for OSINT.
* [Github: Awesome AWS Security](https://github.com/jassics/awesome-aws-security) -> A common curated list of links, references, books videos, tutorials (Free or Paid), Exploit, CTFs, Hacking Practices etc. which are obviously related to AWS Security.
* [Github: Awesome Azure Penetration Testing](https://github.com/Kyuu-Ji/Awesome-Azure-Pentest) -> A collection of resources, tools and more for penetration testing and securing Microsofts cloud platform Azure.
* [Github: Awesome Pcap Tools](https://github.com/caesar0301/awesome-pcaptools) -> A collection of tools developed by other researchers in the Computer Science area to process network traces.
* [Github: Awesome Mac](https://github.com/jaywcjlove/awesome-mac) -> Here, we collect awesome macOS software and arrange them into various categories.
* [Github: Awesome Sysadmin](https://github.com/kahun/awesome-sysadmin) -> A curated list of amazingly awesome open source sysadmin resources inspired by Awesome PHP.
* [Github: Awesome Selfhosted](https://github.com/awesome-selfhosted/awesome-selfhosted) -> A list of Free Software network services and web applications which can be hosted on your own servers.
* [Github: Hacking Articles - Cyber Security Mindmaps](https://github.com/Ignitetechnologies/Mindmap) -> This repository will contain many mindmaps for cyber security technologies, methodologies, courses, and certifications in a tree structure to give brief details about them.
* [Github: How To Hunt](https://github.com/KathanP19/HowToHunt) -> Collection of methodology and test case for various web vulnerabilities.
* [Github: HackerOne Reports - Top disclosed reports from HackerOne](https://github.com/reddelexc/hackerone-reports) -> Tops of HackerOne reports. All reports' raw info stored in data.csv. Scripts to update this file are written in Python 3 and require chromedriver and Chromium executables at PATH. Every script contains some info about how it works.
* [Github: Awesome Interviews](https://github.com/DopplerHQ/awesome-interview-questions) -> A curated awesome list of lists of interview questions.


---
---
---


<div id='courses'/>

## ***Courses***

Courses related to this subject.

* [Course Zero2Auto: Malware Analysis](https://courses.zero2auto.com/adv-malware-analysis-course) -> Developed for those looking to further enhance their skills in the Malware Analysis/Reverse Engineering field.
* [Web Zero Day Engineering: Zero Day Vulnerability Research Training](http://zerodayengineering.com/training/universal-vulnerability-research.html) -> This 4-day intensive training will expose you to full stack essentials of vulnerability research and exploit development, starting from (almost) zero pre-requisites. The training system consolidates all the foundational knowledge and basic skills that you will need to build upon later as you advance and specialize in the field. Created and taught live by a top vulnerability researcher and binary hacker.
* [Web TrainSec: Windows Internals and Programming](https://training.trainsec.net/windows-internals-and-programming)
* [Course ZeroPointSecurity: Offensive Driver Development](https://training.zeropointsecurity.co.uk/courses/offensive-driver-development) -> Learn how to set up a development testing environment for writing Windows kernel-mode drivers using Hyper-V, WinDbg, and Visual Studio. Cover the basic anatomy of a driver from loading and unloading, I/O control codes, interaction from userland, and kernel debugging.
* [Web Maldev Academy](https://maldevacademy.com/) -> Maldev Academy is a comprehensive malware development course that focuses on x64 malware development, providing knowledge from basic to advanced level. The course is primarily designed for individuals in offensive security, but it also caters to beginners who have no prior experience in malware development. 


---
---
---


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
