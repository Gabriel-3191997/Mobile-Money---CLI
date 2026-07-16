# Orange Money USSD CLI
This document outlines the architectural design, user journey, and operational instructions for the CLI-based **Orange Money USSD Simulation Engine**. This system acts as a high-fidelity, zero-dependency sandbox for testing, training, and demonstrating the USSD mobile financial transaction flow without connecting to live carrier infrastructure.



## 1. Introduction

USSD (Unstructured Supplementary Service Data) remains a critical gateway for digital financial inclusion, especially across emerging markets. Because testing directly on live GSM networks during early-stage development is costly and logistically complex, this simulation engine replicates the precise behavior, timings, and navigation matrix of the **Orange Money Liberia (`*144#`)** ecosystem. It provides an immediate feedback loop for developers, customer experience (CX) designers, and QA teams.


## 2. Project Overview & Scope

### In-Scope
*   **Protocol Dialing Emulation:** Capturing initial MMI codes (`*144#`) via a terminal-based Dialer.
*   **Network Latency Simulation:** Simulating packet travel delays with synchronous time-blocked output loops (`USSD code running....`).
*   **State-Preserving Session Navigation:** Implementing a LIFO (Last-In, First-Out) stack structure to preserve historical navigation context, allowing bidirectional traversing using the standard `0` (back) action.
*   **Transaction Flow Validation:** Mimicking dynamic state checks (currency selection, recipient input, amount specifications, PIN entry checks).

### Out-of-Scope
*   Integration with actual GSM gateway hardware or SMPP servers.
*   Persistent database storage (all sessions are memory-bound and transient).
*   Live SMS confirmation generation.


## 4. How to Run the Code

The application is written in vanilla Python and requires no external third-party installations or configurations.

### Command to Execute the Code

Open your system terminal or command prompt inside the project directory and run:

```bash
python main.py
```

*Note: Ensure you are running Python 3.6+ to support modern formatting and terminal buffer flushes.*



## 5. Code Output

Below is a standard stdout transcript demonstrating a successful transaction end-to-end:

```text

 Dial *144# to access Orange Money
 Type 'exit' to close the app.


*144#

USSD code running....

Welcome to Orange Money
1:Send Money
2:Buy Airtime
3:Buy Bundles
4:Energy
5:Pay Taxes and Fees
6:Pay with Orange Money
7:Cash Out
8:Bank Services
9:My Account
10:Help
---
0:back

Enter choice: 1

1:USD
2:LRD
3:My Status
4:New Tariff
5:OM Lifeline Bundle
6:Buy bundle commison
7:Reactivation Service
8:Free 2 mins
9:Self PIN Reset
10:New Sim Offer
---
0:back

Enter choice: 1

1: To Orange Money
2: To MTN Momo
3: International transfer
---
0:back

Enter choice: 1

Enter receiver phone number
---
0:back

Enter phone: 0777001122

Enter amount in USD
---
0:back

Enter amount: 15

You will transfer 15 USD to 0777001122
Kun.
Charge: 0.02
Enter PIN to confirm.
2.If you want Kun to received in LRD
3.To Cancel
---
0:back

Enter PIN or option: 1234

Sending request...
Success! You have sent 15 USD to 0777001122.
```
