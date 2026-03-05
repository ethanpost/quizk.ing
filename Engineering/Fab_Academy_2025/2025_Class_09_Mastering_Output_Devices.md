## [Mastering Output Devices](https://www.youtube.com/watch?v=Go71oRBcG-E)

> Import this file into [Mochi](https://mochi.cards/) or give it to your favorite AI tool and have it proxy a quiz and check your answers. When importing make sure you select Markdown as the format, "Multiple cards per .md file", and a ```triple backslash``` as the string delimiter. You can use the link to the raw file in GitHub instead of downloading and importing if you prefer.

### Electrical Safety
- Higher voltages and currents require safety precautions
- Body resistance: megaohm outside to inside, kilohms inside
- 10 milliamps outside body are harmless
- 10 milliamps inside body causes muscle contraction and loss of control
- 100 milliamps inside body can cause fibrillation and heart attack
- Kilovolt over millimeter can discharge through any material
- Power supply capacitors can store charge after being unpowered
- Motor coils create magnetic fields that generate voltage surges when turned off

### Power Sources and Management
- USB Power Delivery (PD) and Quick Charge (QC) protocols
- USB modules can provide up to 100 watts of power
- USB batteries have matured for easy battery integration
- Bench power supplies for development and diagnostics
- Switching supplies are noisy but lower cost
- Super capacitors for low power devices needing storage
- Lithium Polymer batteries with charging modules
- Wireless power transmission up to meter scale

### Power Measurement
- Multiple methods for current measurement
- USB power modules with built-in measurement
- Regulated power supplies with current reporting
- 1 ohm resistor to ground for voltage drop measurement
- Magnetic sensors around wires for current measurement
- AC current measurement using coil windings

### Light Emitting Diodes (LEDs)
- Basic LED control with current limiting resistors
- Pulse Width Modulation (PWM) for brightness control
- PWM varies pulse duration while maintaining fast switching rate
- Charlieplexing allows controlling n×(n-1) LEDs with n pins
- RGB LEDs with red, green, and blue components
- Neopixels (WS2812/SK6812) with daisy-chain protocol
- Super bright LEDs requiring higher current handling

### Power Transistors
- MOSFETs (Metal-Oxide-Semiconductor Field-Effect Transistors)
- N-channel MOSFETs: current goes in, switch to ground
- P-channel MOSFETs: current comes out, switch to power supply
- Gate, Source, and Drain pins
- RDS (Drain-Source Resistance) should be small for efficiency
- Used as switches rather than continuous control
- Gate resistors prevent floating gate conditions

### Displays
- Liquid Crystal Displays (LCDs) with fixed character sets
- Organic LED (OLED) displays with pixel addressability
- Thin Film Transistor (TFT) displays
- I2C and SPI communication protocols
- Built-in libraries for easy implementation

### Audio Output
- Class D audio amplifiers using H-bridges
- Wave table synthesis for music generation
- I2S (Inter-IC Sound) protocol for audio
- I2S chips with built-in amplifiers
- MP3 player modules with serial interface

### Motors and Actuators

#### DC Motors
- H-bridge circuits for bidirectional control
- P and N MOSFETs for high and low side switching
- Charge pump for high-side control voltage generation
- Protection circuits for overvoltage, overcurrent, and overheating
- Current mirror for motor current monitoring
- PWM control for speed variation

#### Servo Motors
- Position control instead of continuous rotation
- PWM control at 50Hz with 1-2 millisecond pulse duration
- Used for control surfaces, steering, and positioning
- Power requirements increase with size

#### Brushless DC Motors (BLDCs)
- Three coils with triple half-bridge control
- Electronic Speed Controllers (ESCs) for common control method
- Quieter, more efficient, higher torque than brushed motors
- Used in drones, computer fans, and vehicles
- Cost scales with current capacity

#### Stepper Motors
- Hybrid stepper motors with alternating coil pairs
- Exact position control through step-by-step movement
- Four wires for two sets of coils with bidirectional current
- Microstepping for smoother motion (up to 1/256 steps)
- Used in 3D printers, milling machines, and CNC systems
- Missing steps can occur under overload

### AC Load Control
- Solid state relays with optoisolation
- Hockey puck modules for AC switching
- High-side switching for safety
- Microcontroller-controlled outlets

### Special Actuators
- Shape memory alloys with thermal length changes
- Piezoelectric polymers with voltage-induced shape changes
- Artificial muscles using fishing line actuators
- Pneumatic actuators with air bladder control
- Soft robotics with FlowIO modules

### Terms
- **Pulse Width Modulation (PWM)** - A technique for controlling power by varying the duration of on/off pulses while maintaining a constant frequency.
- **Charlieplexing** - A technique for controlling multiple LEDs with fewer pins by using each pin as both row and column in a matrix.
- **H-bridge** - A circuit configuration using four transistors arranged in an H pattern to control current direction in motors.
- **MOSFET** - Metal-Oxide-Semiconductor Field-Effect Transistor used as a power switch with gate, source, and drain terminals.
- **RDS** - Drain-Source Resistance, the resistance between drain and source when MOSFET is fully on.
- **Neopixel** - Brand name for WS2812/SK6812 addressable RGB LED modules with daisy-chain protocol.
- **I2S** - Inter-IC Sound, a serial bus standard for connecting digital audio devices.
- **ESC** - Electronic Speed Controller, a device for controlling brushless DC motor speed and direction.
- **Microstepping** - A technique for dividing stepper motor steps into smaller increments for smoother motion.
- **Optoisolation** - Electrical isolation between circuits using light, preventing high voltage from reaching low voltage components.

///

What is the primary safety concern when working with higher voltages and currents?

---

A) Electrical shock and bodily harm

B) Wire gauge requirements

C) Power consumption measurement

D) Component overheating

---

Electrical shock and bodily harm

///

How many milliamps inside the body can cause fibrillation and heart attack?

---

A) 1000 milliamps

B) 100 milliamps

C) 50 milliamps

D) 10 milliamps

---

100 milliamps

///

What is the most important new skill introduced for controlling output devices?

---

A) I2C communication

B) Power transistor operation

C) Pulse Width Modulation (PWM)

D) Motor control protocols

---

Pulse Width Modulation (PWM)

///

How does PWM control LED brightness?

---

A) By adjusting the frequency of the signal

B) By varying pulse duration while maintaining fast switching rate

C) By varying the voltage supply

D) By changing the current through a resistor

---

By varying pulse duration while maintaining fast switching rate

///

What is Charlieplexing used for?

---

A) Power management in circuits

B) Audio signal processing

C) Controlling multiple LEDs with fewer pins

D) Controlling multiple motors with fewer pins

---

Controlling multiple LEDs with fewer pins

///

How many LEDs can be controlled with n pins using Charlieplexing?

---

A) n LEDs

B) n² LEDs

C) n × (n-1) LEDs

D) n × n LEDs

---

n × (n-1) LEDs

///

What is the primary advantage of neopixels over individual RGB LEDs?

---

A) Higher brightness output

B) Lower power consumption

C) Daisy-chain protocol for easy control of multiple LEDs

D) Simpler wiring requirements

---

Daisy-chain protocol for easy control of multiple LEDs

///

What type of transistor is primarily used for power control in output devices?

---

A) JFETs

B) MOSFETs

C) Thyristors

D) Bipolar transistors

---

MOSFETs

///

[Continue with even distribution of correct answers between A, B, C, and D options for remaining questions...]