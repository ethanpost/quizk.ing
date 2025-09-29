## [The Secret Life of Components - PLCs](https://www.youtube.com/watch?v=heDQbZc8aX0)

> Import this file into [Mochi](https://mochi.cards/) or give it to your favorite AI tool and have it proxy a quiz and check your answers. When importing make sure you select Markdown as the format, "Multiple cards per .md file", and a ```triple backslash``` as the string delimiter. You can use the link to the raw file in GitHub instead of downloading and importing if you prefer.


### Introduction and Background
- PLCs are programmable logic controllers used in industrial automation
- Tim Hunkin uses Mitsubishi PLCs in his arcade machines
- Over 50 PLCs running daily, some for 20+ years without problems
- Main advantages: robust, reliable, long-lasting, backward compatible
- Main disadvantage: expensive compared to microcontrollers like Arduino
- Built for industrial automation where quality matters more than price

### Early Experience and Learning
- First PLC experience in 1991 on theme park ride project
- 24 different scenes controlled by Mitsubishi PLCs
- Initial struggle with misprinted manual code
- Learned ladder programming through this project
- Early arcade machines used linear sequences of motor events

### Cam Timers to PLCs Transition
- Originally used cam timers (drum sequences) for motor control
- Cam timers: mechanical devices with adjustable cams controlling switches
- Transparent operation - could see exactly what was happening
- PLCs can do same job as cam timers
- PLC advantages: LED indicators for troubleshooting, easier fault finding
- Industrial automation designed around quick fault resolution

### Getting Started with PLCs
- Recommended: buy second-hand PLCs on eBay
- Automation engineers upgrade systems, old PLCs become available
- Second-hand PLCs are well-made and reliable
- Mitsubishi chosen due to initial project experience
- Software cost can be expensive (£1300+)
- Student versions and helplines available from suppliers
- Cheaper alternatives exist online

### Basic PLC Layout and Components
- Inputs at top, outputs at bottom
- LED indicators for inputs and outputs
- Power, run, and error lights
- 24V power supply with stabilized output
- Enough power for sensors and relays
- SS terminals for sink/source configuration
- USB or proprietary connector for programming
- Run/stop switch
- Potentiometer for adjustable timers
- Internal processor, relays, and power supply

### Stepladder Programming
- Called "stepladder" because it's graphical like a ladder
- Each rung has input on left, output on right
- Inputs/outputs can be physical or internal (relays, counters, timers)
- Logic gates can be added in middle of rungs
- Program runs through rungs continuously (hundreds of times per second)
- Simple example: timer delay between input and output
- Monitoring function allows watching program execution
- Instructionalist method: text-based programming alternative

### Choosing a PLC
- Intelligent relays: simplest option, programmable on device itself
- Basic PLC range: FX3S series recommended (uses USB)
- Older PLCs work well but need dedicated connectors
- Speed differences don't affect most applications
- Pay for number of outputs (2-14 in budget series)
- No extension blocks available on basic models
- Avoid FX1 series (dim LEDs)
- 24V DC or mains power options
- Relay or transistor outputs available

### Inputs and Outputs
- Outputs: completely isolated, can use any voltage
- Different COM terminals allow variety of voltages
- Inputs: more complicated, PLC is 24V device
- Problem with 12V sensors (need relay conversion)
- PNP vs NPN sensor compatibility issues
- Sink/source configuration affects sensor compatibility
- Converter modules available for mixed sensor types
- Keep power supplies isolated for easier fault finding

### Processing Speed
- Modern PLCs: 0.2 microseconds per simple instruction
- Speed test with shaft encoder (400 steps per revolution)
- High-speed counters and pulse catch functions
- Speed adequate for most arcade machine applications
- Motion control extension blocks available for complex applications

### Extension Blocks
- Extra output blocks: cheapest way to get more outputs
- 8 or 16 extra outputs available
- FX2 range has connector for extension blocks
- FX3S doesn't support extension blocks
- Applied instructions: software-based extensions
- Compare function commonly used
- Pulse catch: interrupts to catch brief sensor pulses
- Avoid complex extension blocks when possible

### Programming States
- States: parts of program active at any one time
- Essential for complex games with branching logic
- One state can trigger different states based on conditions
- Makes complex programs manageable (2000+ lines)
- Easier fault finding by identifying which state is stuck
- Example: Mobility Master Class game with 25 different states

### Adding Arduinos
- Arduino used for specialized functions (stepper motor control)
- PLC switches Arduino on/off, Arduino handles complex calculations
- Separates concerns for easier fault finding
- Could be done entirely in PLC but separation helps troubleshooting

### Adding Video
- Early video: CD player with PLC controlling play/next track
- Modern approach: BrightSign players with script programming
- Up to 8 PLC outputs converted to binary for 256 different tracks
- Very fast switching between video tracks
- Reliable but expensive solution

### Simplicity and Reliability
- PLCs simpler than ordinary computers
- No updates, startup/shutdown routines, or internet connection
- Basic simplicity is why they remain widely used
- Suitable for bespoke industrial automation projects
- Similar to arcade machines: prototypes needing tweaking

### Terms
- PLC (Programmable Logic Controller) - A computer designed for industrial automation that controls machinery through programmable logic
- Cam Timer - A mechanical device with rotating drum and adjustable cams that control switches for timed motor sequences
- Stepladder Programming - A graphical programming method that resembles a ladder with rungs containing inputs, logic, and outputs
- Sink/Source - Two different ways of connecting sensors to PLC inputs, affecting compatibility with PNP and NPN sensors
- Extension Block - Additional hardware modules that can be added to PLCs to provide more inputs, outputs, or specialized functions
- Applied Instructions - Advanced software functions built into PLC programming software for complex operations
- States - Programming concept where different parts of a program are active at different times, allowing for complex branching logic
- Pulse Catch - A high-speed interrupt function that captures brief sensor pulses that might be missed in normal scanning
- BrightSign Player - A specialized video player used for reliable video playback in industrial and commercial applications

///

## According to the video, what is the main advantage of PLCs over microcontrollers like Arduino?

---

A) They have more memory capacity

B) They are more robust, reliable, and long-lasting

C) They are easier to program

D) They are cheaper to purchase

---

B) They are more robust, reliable, and long-lasting

///

## What was Tim Hunkin's first experience with PLCs?

---

A) Teaching PLC programming

B) Programming industrial automation systems 

C) Working on a theme park ride project in 1991

D) Building arcade machines

---

C) Working on a theme park ride project in 1991

///

## What did Tim Hunkin use to control his early arcade machines before PLCs?

---

A) Computer programs

B) Manual switches

C) Microcontrollers

D) Cam timers or drum sequences

---

D) Cam timers or drum sequences

///

## Why are PLCs designed with LED indicators?

---

A) To indicate programming status

B) To save power

C) To help with quick fault finding in industrial automation

D) To make them look more professional

---

C) To help with quick fault finding in industrial automation

///

## What does Tim Hunkin recommend for getting started with PLCs?

---

A) Start with Arduino instead

B) Use only intelligent relays

C) Buy second-hand PLCs on eBay

D) Buy new PLCs from manufacturers

---

C) Buy second-hand PLCs on eBay

///

## What is stepladder programming called because of its appearance?

---

A) It uses step-by-step logic

B) It has vertical lines

C) It resembles a ladder with rungs

D) It looks like steps

---

C) It resembles a ladder with rungs

///

## In stepladder programming, how often does the program run through the rungs?

---

A) Only when inputs change

B) Once per minute

C) Once per second

D) Hundreds of times per second

---

D) Hundreds of times per second

///

## What is the simplest type of PLC for basic applications?

---

A) Motion control PLCs

B) FX3S series

C) Intelligent relays

D) FX2 range

---

C) Intelligent relays

///

## What is the main limitation of basic PLC models like FX3S?

---

A) They only work with 12V sensors

B) They cannot have extension blocks added

C) They are too slow

D) They cannot use USB connections

---

B) They cannot have extension blocks added

///

## What voltage do PLCs typically operate on?

---

A) 240V AC

B) 110V AC

C) 24V DC

D) 12V DC

---

C) 24V DC

///

## What are the two types of transistor output sensors that can cause compatibility issues?

---

A) Digital and analog sensors

B) High and low voltage sensors

C) AC and DC sensors

D) PNP and NPN sensors

---

D) PNP and NPN sensors

///

## What are the mysterious terminals called that affect sensor compatibility?

---

A) COM terminals

B) Output terminals

C) Input terminals

D) SS (sink/source) terminals

---

D) SS (sink/source) terminals

///

## How fast can modern PLCs process a simple instruction?

---

A) 200 microseconds

B) 20 microseconds

C) 2 microseconds

D) 0.2 microseconds

---

D) 0.2 microseconds

///

## What type of counter did Tim Hunkin use to test PLC speed?

---

A) High-speed counter

B) A/B counter

C) Simple counter

D) Pulse counter

---

B) A/B counter

///

## What are extension blocks primarily used for?

---

A) Reducing power consumption

B) Improving reliability

C) Adding more inputs and outputs

D) Increasing processing speed

---

C) Adding more inputs and outputs

///

## What programming concept allows different parts of a program to be active at different times?

---

A) Variables

B) Functions

C) States

D) Loops

---

C) States

///

## How many different states were in the Mobility Master Class game?

---

A) 50 states

B) 15 states

C) 10 states

D) 25 states

---

D) 25 states

///

## What is pulse catch used for?

---

A) Storing data

B) Timing motor operations

C) Catching programming errors

D) Capturing brief sensor pulses

---

D) Capturing brief sensor pulses

///

## What did Tim Hunkin use Arduino for in his machines?

---

A) Video playback

B) Sensor input processing

C) Controlling stepper motors with complex calculations

D) Replacing PLCs entirely

---

C) Controlling stepper motors with complex calculations

///

## What type of video players does Tim Hunkin use in his recent machines?

---

A) Computer monitors

B) BrightSign players

C) DVD players

D) CD players

---

B) BrightSign players

///

## How many different video tracks can Tim Hunkin's system play?

---

A) 256 tracks

B) 128 tracks

C) 8 tracks

D) 64 tracks

---

A) 256 tracks

///

## What makes PLCs simpler than ordinary computers?

---

A) They use less power

B) They are smaller in size

C) They don't need updates, startup routines, or internet connections

D) They have fewer components

---

C) They don't need updates, startup routines, or internet connections

///

## What is a cam timer?

---

A) A computer program

B) A type of sensor

C) A mechanical device with rotating drum and adjustable cams controlling switches

D) A digital timer device

---

C) A mechanical device with rotating drum and adjustable cams controlling switches

///

## What does "applied instructions" refer to in PLC programming?

---

A) Hardware components

B) User manuals

C) Basic programming commands

D) Advanced software functions built into PLC programming software

---

D) Advanced software functions built into PLC programming software

///

## What is the main reason Tim Hunkin keeps power supplies isolated in his machines?

---

A) To improve performance

B) To make fault finding easier

C) To reduce costs

D) To save space

---

B) To make fault finding easier

///

## What programming method does Tim Hunkin prefer over stepladder programming?

---

A) Block programming

B) Instructionalist method

C) Visual programming

D) C++ programming

---

B) Instructionalist method

///

## What is the main advantage of using states in PLC programming?

---

A) It reduces memory usage

B) It makes programs run faster

C) It allows complex branching logic and easier fault finding

D) It simplifies hardware requirements

---

C) It allows complex branching logic and easier fault finding

///

## Master Answer Key

**Question 1:** B - PLCs are designed for industrial automation where reliability and longevity are more important than cost.

**Question 2:** C - Tim's first PLC experience was in 1991 working on a theme park ride project.

**Question 3:** D - Before PLCs, Tim used cam timers (drum sequences) for mechanical control.

**Question 4:** C - Industrial automation prioritizes quick fault finding through LED indicators.

**Question 5:** C - Tim recommends buying second-hand PLCs on eBay for getting started.

**Question 6:** C - Stepladder programming resembles a ladder with rungs containing program logic.

**Question 7:** D - The program scans through rungs hundreds of times per second.

**Question 8:** C - Intelligent relays are the simplest option for basic applications.

**Question 9:** B - Basic models like FX3S can't use extension blocks.

**Question 10:** C - PLCs operate on 24V DC, standard for industrial automation.

**Question 11:** D - PNP and NPN transistor configurations require different wiring approaches.

**Question 12:** D - SS (sink/source) terminals control sensor connection configuration.

**Question 13:** D - Modern PLCs process instructions in 0.2 microseconds.

**Question 14:** B - A/B counters were used for position tracking in speed tests.

**Question 15:** C - Extension blocks add more inputs and outputs to PLCs.

**Question 16:** C - States enable different parts of programs to be active at different times.

**Question 17:** D - The Mobility Master Class game had 25 different states.

**Question 18:** D - Pulse catch captures brief sensor pulses during scanning.

**Question 19:** C - Arduino handled complex stepper motor calculations.

**Question 20:** B - BrightSign players replaced earlier CD player systems.

**Question 21:** A - The system can handle 256 different video tracks.

**Question 22:** C - PLCs are simpler by not needing updates, startup routines, or internet.

**Question 23:** C - Cam timers use rotating drums with adjustable cams for switch control.

**Question 24:** D - Applied instructions are advanced software functions in PLC programming.

**Question 25:** B - Isolated power supplies make fault finding easier.

**Question 26:** B - Tim prefers the instructionalist method over stepladder programming.

**Question 27:** C - States enable complex branching logic and easier fault finding.
