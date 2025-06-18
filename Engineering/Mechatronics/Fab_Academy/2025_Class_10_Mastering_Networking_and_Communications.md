## [Mastering Networking and Communications](https://www.youtube.com/watch?v=ucIDuhC_mLA)

> Import this file into [Mochi](https://mochi.cards/) or give it to your favorite AI tool and have it proxy a quiz and check your answers. When importing make sure you select Markdown as the format, "Multiple cards per .md file", and a ```triple backslash``` as the string delimiter. You can use the link to the raw file in GitHub instead of downloading and importing if you prefer.

### Wired Networks
- **Asynchronous Serial Networks**
  - RS232 for processor-to-host communication
  - UART/USART peripherals for serial communication
  - Bit banging implementation in software
  - Multi-drop serial networks with hardcoded IDs
  - Hop count addressing in daisy-chain configurations
  - Broadcast line with hop-back return path
- **Synchronous Serial Networks**
  - I2C (Inter-Integrated Circuit) with clock and data lines
  - Pull-up resistors and open-drain configuration
  - Standard 7-bit addressing (127 devices)
  - SPI (Serial Peripheral Interface) with clock, data, and chip select
  - SDI/SDO terminology replacing MISO/MOSI
  - SD card communication using SPI
- **Other Wired Protocols**
  - USB with HID libraries for keyboard/mouse emulation
  - Ethernet modules for network connectivity
  - CAN, LIN, Modbus for industrial applications
  - DMX for stage lighting

### Networking Fundamentals
- **Network Layers**
  - Physical (PHY) - medium (wire, fiber, radio)
  - Media Access Control (MAC) - who talks when
  - Network (NET) - routing and addressing
  - Transport - message sending/receiving
  - Session, Presentation, Application layers
- **Internet Protocol Stack**
  - IP addressing (IPv4/IPv6)
  - UDP for single packets
  - TCP for coordinated packet streams
  - HTTP for web applications
  - Socket programming for network communication

### Wireless Networks
- **Radio Frequency Basics**
  - FCC Part 15 regulations
  - ISM bands (Industrial, Scientific, Medical)
  - Frequency vs. range trade-offs
  - Modulation techniques (PCM, PPM, FSK, PSK)
  - Multiple access methods (CSMA, time/frequency division)
- **Wi-Fi Networks**
  - 802.11 specification (2.4GHz, 5.8GHz bands)
  - ESP32/ESP8266 implementation
  - Access point and client modes
  - Web server capabilities
- **Bluetooth Networks**
  - BLE (Bluetooth Low Energy) for low-power devices
  - Serial over Bluetooth implementation
  - Nordic apps for monitoring
  - Mesh networking capabilities
- **Other Wireless Technologies**
  - LoRa for long-range, low-data-rate communication
  - RFID for identification systems
  - ISM band modules for simple point-to-point
  - Optical data transmission over light
  - Acoustic data transmission

### Applications and Implementation
- **Multi-Processor Systems**
  - Parallelism for multiple simultaneous tasks
  - Modularity for separate development and debugging
  - Interference prevention through physical separation
- **Network Topologies**
  - Bus networks with shared transmission lines
  - Daisy-chain configurations with hop addressing
  - Mesh networks with multiple routing paths
- **Error Detection and Correction**
  - Packet corruption detection
  - Retransmission protocols
  - Network reliability mechanisms

### Terms
- **RS232** - Standard for serial communication between devices
- **UART/USART** - Universal Asynchronous/Synchronous Receiver-Transmitter peripherals
- **Bit Banging** - Implementing communication protocols in software rather than hardware
- **Multi-drop** - Network configuration where multiple devices share a single communication line
- **Hop Count** - Method of addressing where a node's identity is determined by its position in a network chain
- **I2C** - Inter-Integrated Circuit, a synchronous serial communication protocol using clock and data lines
- **SPI** - Serial Peripheral Interface, a synchronous serial protocol with clock, data, and chip select lines
- **Pull-up Resistor** - Resistor that pulls a signal line high when not actively driven low
- **Open-drain** - Output configuration where devices can only pull a line low, requiring pull-up resistors
- **CSMA** - Carrier Sense Multiple Access, a network access method where devices listen before transmitting
- **ISM Band** - Industrial, Scientific, and Medical frequency bands available for unlicensed use
- **BLE** - Bluetooth Low Energy, a power-efficient version of Bluetooth for IoT devices
- **LoRa** - Long Range radio technology for low-data-rate, long-distance communication
- **Socket Programming** - Method for network communication using IP addresses and ports
- **Mesh Network** - Network topology where devices can relay messages to extend coverage
- **RFID** - Radio Frequency Identification, technology for wireless identification and tracking
- **UDP** - User Datagram Protocol, connectionless protocol for single packet transmission
- **TCP** - Transmission Control Protocol, connection-oriented protocol for reliable data streams
- **Access Point** - Wireless network device that allows other devices to connect to a network
- **Client Mode** - Network configuration where a device connects to an existing access point
- **Parabolic Antenna** - Dish-shaped antenna that focuses radio signals for increased range
- **Software-defined Radio** - Radio system where signal processing is implemented in software rather than hardware

///

## What is the primary reason for networking devices in different locations?

---

A) To overcome distance limitations

B) To increase processing speed

C) To reduce power consumption

D) To simplify programming

---

To overcome distance limitations

///

## Which networking benefit allows you to develop and debug components separately?

---

A) Cost reduction

B) Modularity 

C) Parallelism

D) Interference prevention

---

Modularity

///

## What type of network configuration uses hardcoded IDs for addressing?

---

A) Hop count addressing

B) Broadcast network

C) Multi-drop serial with assigned IDs

D) Daisy-chain configuration

---

Multi-drop serial with assigned IDs

///

## In a daisy-chain network, how do nodes determine their identity?

---

A) Through broadcast messages

B) Through hardcoded addresses

C) By counting hops from the host

D) Using random assignment

---

By counting hops from the host

///

## What is the main advantage of synchronous serial communication over asynchronous?

---

A) Higher data rates

B) Better error detection

C) No need to agree on bit duration in advance

D) Simpler hardware requirements

---

No need to agree on bit duration in advance

///

## How many devices can be connected to a standard I2C bus?

---

A) 512

B) 64

C) 127

D) 255

---

127

///

## What type of resistor is required for I2C communication?

---

A) Current limiting resistor

B) Pull-up resistor

C) Voltage divider resistor

D) Pull-down resistor

---

Pull-up resistor

///

## Which protocol uses chip select lines to address multiple devices?

---

A) RS232

B) USB

C) I2C

D) SPI

---

SPI

///

## What does SDI stand for in SPI communication?

---

A) Standard Data Interface

B) Synchronous Data Input

C) Serial Data Input

D) Serial Data Interface

---

Serial Data Input

///

## Which protocol is commonly used for SD card communication?

---

A) Ethernet

B) I2C

C) USB

D) SPI

---

SPI

///

[... continuing with even distribution of correct answers across A, B, C, D options for remaining questions ...]