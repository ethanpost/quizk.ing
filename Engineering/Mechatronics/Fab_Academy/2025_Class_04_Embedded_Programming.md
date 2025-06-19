## [Embedded Programming](https://www.youtube.com/watch?v=saGrn6gVon8)

> Import this file into [Mochi](https://mochi.cards/) or give it to your favorite AI tool and have it proxy a quiz and check your answers. When importing make sure you select Markdown as the format, "Multiple cards per .md file", and a ```triple backslash``` as the string delimiter. You can use the link to the raw file in GitHub instead of downloading and importing if you prefer.

### Microcontroller Families
- AVR Family
  - Developed by Norwegian students for modern compilers
  - 8-bit architecture, inexpensive, easy to program
  - 20 MHz instruction speed, one cycle per instruction
  - Can run at wide range of voltages
  - Examples: ATtiny 412, ATtiny 1624
  - Very easy to program with single pin interface

- ARM Family
  - 32-bit architecture, larger word size
  - Somewhat faster clock (48 MHz)
  - More peripheral options
  - Requires larger code libraries
  - Examples: SAMD11, SAMD21, SAMD51
  - Spans from small microcontrollers to powerful processors

- Raspberry Pi RP2040
  - ARM-based with special features
  - Runs at 133 MHz (can be overclocked to 250 MHz)
  - Contains PIOs (Programmable I/O) for custom peripherals
  - Popular for more complex applications

- ESP Family (Espressif)
  - Based on MIPS or RISC-V architectures
  - Includes built-in WiFi and Bluetooth radios
  - Examples: ESP8266, ESP32
  - Good for networked applications

### Processor Architecture Considerations
- Von Neumann vs. Harvard architecture
  - Harvard separates program and data memory (more efficient)
- RISC (Reduced Instruction Set Computing)
  - Small set of instructions that execute quickly
- Microprocessor vs. Microcontroller
  - Microcontrollers have everything built-in
- Word size options: 8-bit, 16-bit, 32-bit, 64-bit
  - Larger word size can address more memory

### Memory Types
- Registers: Fastest access, where program executes operations
- Static RAM: Quick access but uses more transistor space
- Dynamic RAM: Slower access but stores more data
- EEPROM: Non-volatile storage for configuration
- Flash: Non-volatile storage for programs
- Fuses: Special configuration memory

### Peripherals
- Digital pins with various configuration options
- A/D (Analog to Digital) converters
- Comparators for voltage comparison
- D/A (Digital to Analog) converters
- Timers and counters for measuring events
- Pulse-width modulators (PWM)
- USART and USB communication interfaces
- Specialized peripherals for math or cryptography

### Programming Languages
- Assembly Language
  - Lowest level, direct mapping to processor instructions
  - Rarely used directly today
- C/C++
  - Most common language for microcontrollers
  - Efficient, fast execution
  - Widely supported across all processor families
- Rust
  - Modern language with memory safety features
  - Growing support but more complex setup for embedded
- Python (MicroPython)
  - Higher-level language, easier to read and write
  - Interactive development via REPL
  - Much slower (100x) and needs more memory (100x)
  - Great for complex tasks, multitasking, data analysis

### Programming Tools
- Microchip Studio
- Eclipse
- VS Code
- Thonny (for Python)
- PlatformIO
- Arduino IDE

### Arduino Clarification
- Arduino refers to several distinct things:
  - Commercial boards
  - Toolchain installation system
  - Library collection (varying quality)
  - Development environment
  - Bootloader family
  - Header standard

### Programming Interfaces
- JTAG (for ARM processors)
- UPDI (one-pin programming for AVR)
- Bootloaders for USB or serial programming
- Serial communication (RS-232)
- Terminal programs for communication

### Development Boards
- Commercial options: Arduino, Raspberry Pi Pico, Adafruit, SparkFun
- Lab-fabricated options

### Simulators
- Wokwi - Simulates AVRs, ESPs, STM, RP2040
- AVR8js - Mixed signal simulator for AVR + circuit simulation
- TinkerCircuit

### Debugging Techniques
- Blinking LEDs for feedback
- Print statements
- Embedded debuggers (stop execution, read/modify state)
- Hardware testing with multimeters and oscilloscopes

### Terms
- Von Neumann Architecture - Computer design where program and data memory share the same space
- Harvard Architecture - Computer design with separate program and data memory
- RISC - Reduced Instruction Set Computing, using a small set of simple instructions
- Microcontroller - A complete computer system on a single chip, including processor, memory, and I/O
- Registers - Fast, small storage locations within the processor for immediate operations
- Flash - Non-volatile memory used to store program code
- EEPROM - Electrically Erasable Programmable Read-Only Memory for storing data when power is off
- PWM - Pulse Width Modulation, varying duration of pulses to control power or create analog-like signals
- Bootloader - Small program that allows loading larger programs without special hardware
- JTAG - Joint Test Action Group, standard for testing and programming integrated circuits
- UPDI - Unified Program and Debug Interface, one-pin programming interface for AVR
- PIO - Programmable I/O block in RP2040 that can be used to create custom peripherals
- Arduino - Ecosystem including hardware, software libraries, IDE, and programming standard
- IDE - Integrated Development Environment for writing, compiling, and debugging code
- REPL - Read-Evaluate-Print Loop, interactive programming environment

///

## According to the material, what is the most basic way to communicate between a processor and your computer?

---

A) RS-232

B) USB

C) Bluetooth

D) Wi-Fi

---

RS-232

///

## Which architecture separates program and data memory?

---

A) Von Neumann

B) Harvard

C) RISC

D) ARM

---

Harvard

///

## What is the speed difference between Python and C according to the transcript?

---

A) Python is 20x slower

B) Python is 10x slower

C) Python is 100x slower

D) They have similar speed

---

Python is 100x slower

///

## What is the smallest AVR package mentioned in the transcript?

---

A) Through-hole package

B) Surface mount package

C) Size of a grain of rice

D) Ball grid array

---

Size of a grain of rice

///

## What does PWM stand for?

---

A) Power Width Management

B) Pin Wireless Management

C) Processor Work Module

D) Pulse Width Modulator

---

Pulse Width Modulator

///

## According to the transcript, how fast does the ATtiny 412 run?

---

A) 48 MHz

B) 20 MHz

C) 10 MHz

D) 133 MHz

---

20 MHz

///

## Which processor family includes built-in WiFi and Bluetooth radios?

---

A) ARM

B) RISC-V

C) ESP

D) AVR

---

ESP

///

## What is a "bootloader"?

---

A) A hardware device that connects to processors

B) A type of processor architecture

C) A program that loads programs

D) A circuit simulator

---

A program that loads programs

///

## What is Arduino according to the transcript?

---

A) Just a microcontroller board

B) Just a development environment

C) A programming language

D) Six different things (boards, toolchain, libraries, IDE, bootloaders, header standard)

---

Six different things (boards, toolchain, libraries, IDE, bootloaders, header standard)

///

## What is special about the RP2040 compared to other ARM processors?

---

A) It can only be programmed in Python

B) It has WiFi built in

C) It has a series of extra processors (PIOs) for custom peripherals

D) It's the only ARM processor that supports C++

---

It has a series of extra processors (PIOs) for custom peripherals

///

## Which memory type stores data when power is removed?

---

A) Static RAM

B) Dynamic RAM

C) Registers

D) Flash

---

Flash

///

## What word size do AVR processors typically use?

---

A) 32-bit

B) 8-bit

C) 16-bit

D) 4-bit

---

8-bit

///

## What is mixed signal simulation?

---

A) Using multiple programming languages in one project

B) Simulating both digital code and analog circuits

C) Programming multiple processors simultaneously

D) Mixing audio signals in embedded systems

---

Simulating both digital code and analog circuits

///

## What is the importance of a current limiting resistor with an LED?

---

A) It's only needed for digital simulations

B) It prevents taking too much current and damaging components

C) It makes the LED brighter

D) It's required by the Arduino IDE

---

It prevents taking too much current and damaging components

///

## According to the transcript, what was one of the first computer bugs?

---

A) A design flaw in processor architecture

B) A faulty memory circuit

C) An actual insect trapped in a computer

D) A coding error in early software

---

An actual insect trapped in a computer

///

## What is the recommended order for embedded development in this class?

---

A) Design circuits first, then choose processors

B) Download code examples first, then adapt to hardware

C) Simulate and model first, then design schematics, then fabricate

D) Build hardware first, then program it

---

Simulate and model first, then design schematics, then fabricate

///

## What is UPDI?

---

A) USB Protocol for Device Integration

B) A type of memory storage

C) Universal Programming Debug Interface

D) One-pin programming interface for AVR

---

One-pin programming interface for AVR

///

## What happens if you put a 5V voltage into a 3V processor?

---

A) The program will execute incorrectly

B) You'll kill the processor

C) The processor will run faster

D) Nothing, processors are voltage-tolerant

---

You'll kill the processor

///

## What does the "REPL" in Python refer to?

---

A) Runtime Environment for Python Libraries

B) Robust Embedded Programming Language

C) Read-Evaluate-Print Loop

D) Read-Execute-Program-Loop

---

Read-Evaluate-Print Loop
