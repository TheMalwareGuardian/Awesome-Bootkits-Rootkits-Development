# 🖥️ PowerShell Script for Automating Bootkits/Rootkits Development Environment Setup in Windows

This PowerShell script is meticulously crafted to automate the setup of a development environment specifically tailored for creating [UEFI](https://wiki.osdev.org/UEFI) Bootkits and [Kernel](https://learn.microsoft.com/en-us/windows-hardware/drivers/kernel/) Rootkits on Windows. It streamlines the otherwise manual and time-consuming tasks of installing necessary tools and configuring [TianoCore](https://www.tianocore.org/) [EDK2](https://github.com/tianocore/edk2) (EFI Development Kit) and [WDK](https://learn.microsoft.com/en-us/windows-hardware/drivers/download-the-wdk) (Windows Driver Kit), allowing developers to focus more on bootkits/rootkits innovation and less on setup 😉.

## How to Execute

To automate your development environment setup, follow these steps:

1. Open PowerShell.
2. Navigate to the folder containing the script.
3. Execute the script by entering: `.\Setup_Development_Environment.ps1`
4. Respond to the on-screen prompts to select your desired action.


## Usage Example

The script simplifies the following steps:

```
=== Options ===
1a. Bootkits   - Requirements          -> Visual Studio 2019 Community + Git + Python + NASM + ASL
1b. Bootkits   - Set Up Environment    -> EDK2
1c. Bootkits   - Tools                 -> UEFI Scanners
1d. Bootkits   - PoCs                  -> UEFI Applications
2a. Debugging  - Requirements          -> WinDbg
2b. Debugging  - Set Up Environment    -> Enable Debugging
2c. Debugging  - Tools                 -> IDA + Process Hacker
2d. Debugging  - Scripting             -> PoCs - WinDbg Classic + JavaScript + Python PYKD + WinDbg Extensions
3a. Rootkits   - Requirements          -> Visual Studio 2022 Community + SDK + WDK
3b. Rootkits   - Set Up Environment    -> Enable Test Mode
3c. Rootkits   - Tools                 -> Microsoft Sysinternals Suite + OSR Driver Loader
3d. Rootkits   - PoCs                  -> Kernel Mode Drivers
Q. Exit
============
Choose an option:
```