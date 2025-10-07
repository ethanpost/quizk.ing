## [Mastering Mechanical and Machine Design](https://www.youtube.com/watch?v=14I2-qX5a4g)

> Import this file into [Mochi](https://mochi.cards/) or give it to your favorite AI tool and have it proxy a quiz and check your answers. When importing make sure you select Markdown as the format, "Multiple cards per .md file", and a ```triple backslash``` as the string delimiter. You can use the link to the raw file in GitHub instead of downloading and importing if you prefer.

### Introduction to Machine Building
- Definition of a machine: mechanism + actuation + automation + application
- Fab Lab goal: labs can make labs (self-replicating capability)
- Group assignment for machine building
- Two main topics: mechanisms (mechanical) and machines (automation)

### Materials and Properties
- Stress-strain relationships in materials
- Linear vs. nonlinear material behavior
- Plastic deformation and material failure
- Material strength, stiffness, and toughness
- Common materials for machine building: plastic (HDPE), metal extrusions, rubber/foams, G10 (PCB stock), carbon fiber, wood, cement, ceramics

### Mechanical Design Principles
- Maxwell's constraint theory: structures have constraints and degrees of freedom
- Force loops and error stackup in machine design
- Kinematic couplings for precise positioning
- Accuracy vs. precision distinction
- Hysteresis and backlash in mechanical systems

### Fasteners and Joining Methods
- Types of nuts and bolts
- Lock washers and lock nuts for vibration resistance
- Heat set inserts for 3D printed parts
- Rivets for quick assembly
- Pins for constraining motion
- Adhesives (limited use due to disassembly difficulty)

### Machine Framing
- Metal extrusions with T-slots for modular construction
- T-slot fittings: captive nuts, bolts, corner brackets, wheels
- Self-aligning joints in HDPE
- Extrusion-based framing systems

### Power Transmission Systems
- Gears: involute (most common), cycloidal, helical, herringbone
- Planetary gear systems for speed reduction
- Harmonic drives for high reduction ratios
- Rack and pinion for linear motion
- Lead screws with anti-backlash nuts
- Ball screws with recirculating bearings
- Threadless linear drives
- Timing belts and capstan drives
- Chain drives for large forces

### Motion Guidance
- Guide shafts and linear bearings
- V-groove and tapered wheels
- Linear slides for non-precision applications

### Motor Coupling and Bearings
- Flexible couplers for misalignment compensation
- Types of bearings: rotary ball, thrust, linear, turntable, sleeve, pillow block
- Skateboard bearings for cost-effective solutions
- Bearing preload for reducing noise and rattling

### Mechanisms and Motion Systems
- Flexures for limited travel, smooth motion
- Series elastic actuation for force control
- Linkages for motion transformation
- Belt and drive systems
- Whipple tree mechanisms for force distribution
- Pantograph mechanisms for motion scaling
- Delta bots for 3D motion
- Hexapod systems for 6-degree freedom motion
- CoreXY mechanism (invented by Alan Moyer)
- Sorus folded sheet mechanisms
- Hanging printer systems

### Actuation and Control
- Types of actuators: motors, solenoids
- End effectors for machine functionality
- Power electronics for motor control
- Real-time networks for machine coordination
- Open vs. closed loop control systems
- Control theory: bang-bang, PID, model predictive control
- Machine learning for model predictive control

### Machine Control Systems
- G-code for machine commands
- G-code interpreters and controllers
- User interfaces: ChiliPeppr, UGS, Candle, CNCJS
- Path planning and toolpath generation
- MODS workflow for machine operations

### Network-Based Machine Control
- Virtual machine control concepts
- Data flow machines
- Real-time network coordination
- Modular machine systems
- A-RUMBU project for simplified machine control
- Modular Things system for higher-level commands

### Open Source Machine Examples
- Various open machine projects and vendors
- Commercial companies spun off from Fab Lab projects
- Examples: Shaper Tools, Ultimaker, Formlabs

### Terms
- **Stress** - Force applied to a material (sounds like "press")
- **Strain** - Material's response to stress (sounds like "pain")
- **Hysteresis** - Loss of energy in a system due to internal friction
- **Backlash** - Clearance between mating parts causing lost motion
- **Force Loop** - Complete path of forces through a machine structure
- **Kinematic Coupling** - Precision alignment system using balls and slots
- **Accuracy** - How close measurements are to true value
- **Precision** - How repeatable measurements are
- **Involute Gear** - Most common gear type with curved teeth for smooth contact
- **Harmonic Drive** - High reduction ratio gear system using flexible components
- **Capstan Drive** - Cable-based power transmission system
- **CoreXY** - Motion system where motors remain stationary while stage moves
- **PID Control** - Proportional-Integral-Derivative feedback control system
- **Model Predictive Control** - Advanced control using system models to predict future behavior
- **G-code** - Standard programming language for CNC machines
- **End Effector** - Tool or device attached to the end of a robotic arm or machine

///

## What is the primary goal of Fab Labs according to the transcript?

---

A) To obsolete themselves by enabling labs to make labs

B) To make expensive commercial machines

C) To replace traditional manufacturing

D) To create only 3D printers

---

To obsolete themselves by enabling labs to make labs

///

## What is the relationship between stress and strain in materials?

---

A) They are completely independent properties

B) Stress is the applied force, strain is the response

C) They are the same thing with different names

D) Stress is the response, strain is the applied force

---

Stress is the applied force, strain is the response

///

## What type of gear is most commonly used in machine building?

---

A) Helical gear

B) Herringbone gear

C) Involute gear

D) Cycloidal gear

---

Involute gear

///

## What is the purpose of a kinematic coupling?

---

A) To provide power transmission

B) To reduce vibration

C) To align parts to micron accuracy

D) To increase speed

---

To align parts to micron accuracy

///

## What is backlash in mechanical systems?

---

A) A type of bearing

B) A control system

C) Clearance between mating parts causing lost motion

D) A type of gear

---

Clearance between mating parts causing lost motion

///

## What material is NOT recommended for machine building due to swelling and deformation?

---

A) Metal extrusions

B) G10 (PCB stock)

C) Wood

D) HDPE plastic

---

Wood

///

## What is the difference between accuracy and precision?

---

A) They are the same thing

B) Accuracy measures closeness to true value, precision measures repeatability

C) Accuracy is for measurements, precision is for control systems

D) Accuracy measures repeatability, precision measures closeness to true value

---

Accuracy measures closeness to true value, precision measures repeatability

///

## What type of drive system uses recirculating ball bearings for smooth motion?

---

A) Capstan drive

B) Ball screw

C) Lead screw

D) Rack and pinion

---

Ball screw

///

## What is the purpose of bearing preload?

---

A) To increase speed

B) To reduce noise and rattling

C) To decrease friction

D) To increase load capacity

---

To reduce noise and rattling

///

## What mechanism was invented by Alan Moyer?

---

A) Harmonic drive

B) Hexapod

C) CoreXY

D) Delta bot

---

CoreXY

///

## What type of control system is considered better than PID for advanced applications?

---

A) Bang-bang control

B) Open loop control

C) Model predictive control

D) Proportional control only

---

Model predictive control

///

## What is the purpose of an end effector?

---

A) To provide power to the machine

B) To provide feedback

C) To perform the actual work or task

D) To control the machine

---

To perform the actual work or task

///

## What is G-code used for?

---

A) Programming microcontrollers

B) Network communication

C) Standard programming language for CNC machines

D) 3D modeling

---

Standard programming language for CNC machines

///

## What is the advantage of network-based machine control?

---

A) It's always cheaper

B) It's always faster

C) It allows for modular expansion and easier modification

D) It requires less programming

---

It allows for modular expansion and easier modification

///

## What is the purpose of a harmonic drive?

---

A) To increase speed

B) To provide high reduction ratios with smooth motion

C) To reduce noise

D) To increase torque

---

To provide high reduction ratios with smooth motion

///

## What type of bearing is commonly used for cost-effective solutions in machine building?

---

A) Thrust bearings

B) Linear bearings

C) Skateboard bearings

D) Sleeve bearings

---

Skateboard bearings

///

## What is the purpose of a capstan drive?

---

A) To provide rotary motion only

B) To provide linear motion only

C) To provide flexible power transmission in any shape

D) To provide high-speed motion

---

To provide flexible power transmission in any shape

///

## What is the difference between open loop and closed loop control?

---

A) Open loop is always better

B) Closed loop uses feedback, open loop does not

C) Open loop is more expensive

D) Closed loop is always digital

---

Closed loop uses feedback, open loop does not

///

## What is the purpose of T-slots in machine framing?

---

A) To reduce weight

B) To provide modular construction with captive nuts

C) To increase strength

D) To reduce cost

---

To provide modular construction with captive nuts

///

## What is the main advantage of using metal extrusions for machine framing?

---

A) They are always cheaper than other materials

B) They are stiff, modular, and can be quickly assembled

C) They are always lighter than other materials

D) They require no fasteners

---

They are stiff, modular, and can be quickly assembled

///

## What is the purpose of a lock washer?

---

A) To spread load from the nut

B) To add springiness that prevents the nut from loosening

C) To increase the strength of the bolt

D) To reduce friction

---

To add springiness that prevents the nut from loosening

///

## What is the primary advantage of using heat set inserts in 3D printed parts?

---

A) They are cheaper than other fasteners

B) They allow threading without deforming the 3D printed part

C) They are stronger than other fasteners

D) They are easier to install

---

They allow threading without deforming the 3D printed part

///

## What is the purpose of a flexible coupler in motor systems?

---

A) To increase torque

B) To compensate for misalignment between motor and shaft

C) To reduce speed

D) To increase efficiency

---

To compensate for misalignment between motor and shaft

///

## What is the main characteristic of a cycloidal gear compared to an involute gear?

---

A) It's more efficient at force transfer

B) It's easier to fabricate but less efficient

C) It's always quieter

D) It's always stronger

---

It's easier to fabricate but less efficient

///

## What is the purpose of a planetary gear system?

---

A) To increase speed

B) To reduce speed from high RPM motors to slower motion

C) To change direction only

D) To increase torque only

---

To reduce speed from high RPM motors to slower motion

///

## What is the main advantage of using timing belts over other drive systems?

---

A) They are always cheaper

B) They are internally reinforced and can't stretch

C) They are always quieter

D) They require no maintenance

---

They are internally reinforced and can't stretch

///

## What is the purpose of a thrust bearing?

---

A) To handle rotary forces

B) To handle normal (axial) forces

C) To handle linear motion

D) To handle angular motion

---

To handle normal (axial) forces

///

## What is the main advantage of the CoreXY mechanism?

---

A) It's always cheaper to build

B) It allows stage movement without moving motors or wires

C) It's always faster

D) It requires fewer parts

---

It allows stage movement without moving motors or wires

///

## What is the purpose of series elastic actuation?

---

A) To increase speed

B) To specify force rather than position for smoother motion

C) To reduce cost

D) To increase precision

---

To specify force rather than position for smoother motion

///

## What is the main advantage of network-based machine control over centralized control?

---

A) It's always faster

B) It allows for easier expansion and modification

C) It's always cheaper

D) It requires less programming

---

It allows for easier expansion and modification

///

## What is the purpose of a pantograph mechanism?

---

A) To increase force

B) To make small motion control big motion or vice versa

C) To change direction only

D) To increase speed only

---

To make small motion control big motion or vice versa

///

## What is the main characteristic of a delta bot?

---

A) It uses three rotary actuators

B) It uses three linear actuators to move anywhere in 3D space

C) It's always cheaper than other systems

D) It's always faster than other systems

---

It uses three linear actuators to move anywhere in 3D space

///

## What is the purpose of a hexapod system?

---

A) To provide 3D motion only

B) To provide 6-degree freedom motion (XYZ + tilt angles)

C) To provide only rotary motion

D) To provide only linear motion

---

To provide 6-degree freedom motion (XYZ + tilt angles)

///

## What is the main advantage of using G10 (PCB stock) for machine building?

---

A) It's always cheaper than other materials

B) It's friendly to machine and easily machined

C) It's always stronger than other materials

D) It requires no special tools

---

It's friendly to machine and easily machined

///

## What is the purpose of a threadless linear drive?

---

A) To provide rotary motion only

B) To provide smooth linear motion using three heads on a hardened rail

C) To provide high-speed motion

D) To provide high-torque motion

---

To provide smooth linear motion using three heads on a hardened rail

///

## What is the main advantage of using cement for machine building?

---

A) It's always cheaper than other materials

B) It provides good stiffness-to-mass ratio and can be cast

C) It's always lighter than other materials

D) It requires no curing time

---

It provides good stiffness-to-mass ratio and can be cast

///

## What is the purpose of a herringbone gear?

---

A) To increase speed

B) To provide self-aligning motion without external constraints

C) To reduce noise only

D) To increase torque only

---

To provide self-aligning motion without external constraints

///

## What is the main characteristic of a helical gear compared to a standard gear?

---

A) It's always quieter and smoother

B) It's always stronger

C) It's always cheaper

D) It's always more efficient

---

It's always quieter and smoother

///

## What is the purpose of a whipple tree mechanism?

---

A) To increase speed

B) To distribute varying forces to a structure

C) To change direction only

D) To increase torque only

---

To distribute varying forces to a structure

///

## What is the main advantage of using flexures in machine design?

---

A) They are always cheaper than other mechanisms

B) They provide smooth motion for limited travel

C) They are always stronger than other mechanisms

D) They require no maintenance

---

They provide smooth motion for limited travel

///

## What is the purpose of a sleeve bearing?

---

A) To handle high loads

B) To provide permanently lubricated bearings for low-force applications

C) To provide high-speed operation

D) To provide high-precision operation

---

To provide permanently lubricated bearings for low-force applications

///

## What is the main advantage of using anti-backlash nuts with lead screws?

---

A) They are always cheaper

B) They reduce the gap that causes lost motion

C) They are always stronger

D) They require no lubrication

---

They reduce the gap that causes lost motion

///

## What is the purpose of a turntable bearing?

---

A) To handle linear motion

B) To handle rotary motion of a load

C) To handle axial loads only

D) To handle radial loads only

---

To handle rotary motion of a load

///

## What is the main advantage of using V-groove wheels in machine design?

---

A) They are always cheaper than other bearings

B) They can be used to route filament or cable along a path

C) They are always stronger than other bearings

D) They require no maintenance

---

They can be used to route filament or cable along a path

///

## What is the purpose of a pillow block bearing?

---

A) To handle high loads

B) To provide simple sliding surfaces for low-force applications

C) To provide high-speed operation

D) To provide high-precision operation

---

To provide simple sliding surfaces for low-force applications

///

## What is the main advantage of using model predictive control over PID control?

---

A) It's always simpler to implement

B) It uses a model to predict future behavior and plan accordingly

C) It's always cheaper

D) It requires less computation

---

It uses a model to predict future behavior and plan accordingly

///

## What is the purpose of a linear bearing?

---

A) To handle rotary motion

B) To allow movement along a straight line

C) To handle axial loads only

D) To handle radial loads only

---

To allow movement along a straight line

///

## What is the main advantage of using a rack and pinion system?

---

A) It's always cheaper than other linear drives

B) It can run for any length as long as you make the rack

C) It's always more precise than other drives

D) It requires no maintenance

---

It can run for any length as long as you make the rack

///

## What is the purpose of a flexible coupler in motor systems?

---

A) To increase the torque output

B) To allow slight angular misalignment while maintaining rotational stiffness

C) To reduce the speed of the motor

D) To increase the efficiency of the system

---

To allow slight angular misalignment while maintaining rotational stiffness

///

## What is the main advantage of using sealed bearings?

---

A) They are always cheaper than unsealed bearings

B) They are internally lubricated and never need relubrication

C) They are always stronger than unsealed bearings

D) They are always more precise than unsealed bearings

---

They are internally lubricated and never need relubrication

///

## What is the purpose of a U-joint in power transmission?

---

A) To increase torque

B) To allow driving at an angle but with increased friction

C) To reduce speed

D) To increase efficiency

---

To allow driving at an angle but with increased friction

///

## What is the main advantage of using chain drives?

---

A) They are always cheaper than belt drives

B) They can handle very large forces

C) They are always quieter than belt drives

D) They require no maintenance

---

They can handle very large forces

///

## What is the purpose of a sorus mechanism?

---

A) To provide rotary motion only

B) To provide linear motion through folding and unfolding sheets

C) To provide high-speed motion

D) To provide high-torque motion

---

To provide linear motion through folding and unfolding sheets

///

## What is the main advantage of using a hanging printer system?

---

A) It's always cheaper than other 3D printers

B) It can move a printer anywhere in 3D space using multiple filament lines

C) It's always faster than other printers

D) It requires less material

---

It can move a printer anywhere in 3D space using multiple filament lines

///

## What is the purpose of a force loop in machine design?

---

A) To increase the strength of the machine

B) To understand how errors accumulate through the entire force path

C) To reduce the cost of the machine

D) To increase the speed of the machine

---

To understand how errors accumulate through the entire force path

///

## What is the main advantage of using ceramics in machine building?

---

A) They are always cheaper than other materials

B) They can be molded, fired, and made into custom parts

C) They are always lighter than other materials

D) They require no special processing

---

They can be molded, fired, and made into custom parts

///

## What is the purpose of a bang-bang control system?

---

A) To provide smooth motion

B) To simply turn the actuator on and off (generally not recommended)

C) To provide high-precision control

D) To provide high-speed control

---

To simply turn the actuator on and off (generally not recommended)

///

## What is the main advantage of using the A-RUMBU system for machine control?

---

A) It's always cheaper than other control systems

B) It eliminates embedded code and uses USB ports for coordination

C) It's always faster than other systems

D) It requires less programming

---

It eliminates embedded code and uses USB ports for coordination

///

## What is the purpose of a tapered wheel in machine design?

---

A) To provide rotary motion only

B) To fit into extrusion slots for carriage guidance

C) To increase speed

D) To increase torque

---

To fit into extrusion slots for carriage guidance

///

## What is the main advantage of using the Modular Things system?

---

A) It's always cheaper than other systems

B) It provides higher-level commands to nodes rather than just simple steps

C) It's always faster than other systems

D) It requires less hardware

---

It provides higher-level commands to nodes rather than just simple steps

///

## What is the purpose of cable management in machine design?

---

A) To make the machine look better

B) To prevent wires from getting tangled and snagged

C) To reduce the cost of the machine

D) To increase the speed of the machine

---

To prevent wires from getting tangled and snagged

///

## What is the main advantage of using open source machine designs?

---

A) They are always cheaper than commercial machines

B) They can be modified and adapted for specific needs

C) They are always better quality than commercial machines

D) They require no maintenance

---

They can be modified and adapted for specific needs
