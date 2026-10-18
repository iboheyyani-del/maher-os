
# Maher OS — System Specification

## Project Status
Prototype — under development.
This project is not yet a bootable operating system.

## Vision
Build an independent mobile operating system
for a future custom Maher Phone.

## Target Architecture
ARM64 (AArch64).

## Kernel
Linux kernel — planned, not integrated.

## System Components
- Boot: boot process and hardware initialization.
- Kernel: memory, processes, and device drivers.
- Core: essential system services.
- UI: Maher user interface.
- Apps: native Maher applications.
- Security: verified boot and signed updates.

## Android Compatibility
Future goal: support Android applications
through compatible Android runtime components.

Compatibility is not implemented yet.

## Hardware
Target: custom smartphone.
Processor model: not selected.
Board design: not selected.

## Development Rules
- Test every component before integration.
- Never claim hardware compatibility without testing.
- Never flash experimental images onto a daily-use phone.
- Document known limitations and test results.

## First Milestone
Validate project configuration and documentation.
