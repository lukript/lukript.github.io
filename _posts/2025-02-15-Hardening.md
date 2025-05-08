---
title: "Hardening Workstations and Servers"
date: 2025-02-15
categories: [Endpoint Security]
permalink: /wql9bfhy/
tags: [Endpoint Security, Hardening]
mermaid: true
image: /assets/img/posts/20250215/Hardening.jpeg
---

It may seem self-evident, but the most secure systems are inherently those least susceptible to compromise. This principle underpins why organizations invest heavily in layered security measures to safeguard their infrastructure.

## Implementing Secure Systems

Today, we’ll briefly review several fundamental system hardening techniques.

One of the core principles is least privilege—a concept that applies broadly across both endpoint security and secure system architecture. By ensuring that users and services operate with only the permissions they need, we significantly reduce potential attack vectors.

**Note:** Only applications, services, and protocols essential to the system’s core functionality should be active. This minimizes the attack surface and improves overall security posture.

To start, let’s take a closer look at endpoint security solutions.

### 1. Endpoint Security Software

Enpoints are any device that is used to access the system. This includes laptops, desktops, and mobile devices, virtual machines, IoT devices, etc.

Endpoint security software is designed to protect endpoints from malware, viruses, and other malicious software.

### 2. Types of Endpoint Security Software

- Antivirus Software
- Endpoint detection and response (EDR)
- Host intrusion detection and response (XDR)
- Host intrusion prevention systems (HIPS)

## Hardening Workstations

- Disable unnecessary ports
- Enable PowerShell logging
- Disk encryption
  - Full Disk Encryption (FDE)
  - BitLocker
