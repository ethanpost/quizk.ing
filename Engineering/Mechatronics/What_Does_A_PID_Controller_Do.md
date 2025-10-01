## [What does a PID controller do?](https://www.youtube.com/watch?v=qC7hrYJVvD8)

### Take the quiz [here](https://ethanpost.github.io/quizk.ing) by searching for the title.

### You can also import this file into [Mochi](https://mochi.cards/).
- When importing make sure you select Markdown as the format.
- Select "Multiple cards per .md file", 
- Set a ```triple backslash``` as the string delimiter, like this ///
- Use the link to the raw file in GitHub instead of downloading and importing if you prefer.

### Components and Basic Function
- PID stands for Proportional, Integral, and Differential
- Used in control loops for motor control
- Compares target position to actual position
- Generates positional error for adjustment

### Proportional Control (P)
- Multiplies error by gain factor
- Acts like a spring system
- Higher gain increases stiffness
- Can lead to overshooting
- Primary control component

### Differential Control (D)
- Also called "Speed Gain"
- Considers rate of change of error
- Helps prevent overshooting
- Anticipates position changes
- Must be tuned based on inertial load

### Integral Control (I)
- Accumulates error over time
- Compensates for static loads
- Helps achieve exact target position
- Too high settings cause instability
- Should be used cautiously

### S-Curve Motion Control
- Separate from PID control
- Creates smooth motion profiles
- Uses controlled acceleration/deceleration
- Useful for pick-and-place operations
- Prevents jerky movements

### Terms
- PID Controller - A control system using Proportional, Integral, and Differential terms to maintain precise motor position
- Proportional Gain - The main control parameter that determines how strongly the system responds to position errors
- Differential Term - Component that considers rate of change to prevent overshooting
- Integral Term - Component that accumulates error over time to eliminate steady-state errors
- S-Curve - A motion profile that smoothly accelerates and decelerates to reduce jerkiness
- Servo Motor - A motor with position feedback used in precise motion control
- Overshoot - When a system goes beyond its target position before settling
- Oscillation - Back-and-forth movement around a target position

///

## What does PID stand for in PID Controller?

---

A) Proportional, Integral, Differential

B) Position, Integration, Direction

C) Power, Inertia, Displacement

D) Precision, Input, Drive

---

Proportional, Integral, Differential

///

## How does the proportional term in a PID controller behave?

---

A) It looks at rate of change

B) It smooths acceleration curves

C) It accumulates error over time

D) It acts like a spring system

---

It acts like a spring system

///

## What is the primary purpose of the differential term?

---

A) To accumulate position errors

B) To eliminate steady-state errors

C) To prevent overshooting

D) To increase overall gain

---

To prevent overshooting

///

## What happens when the integral gain is set too high?

---

A) The position feedback stops working

B) The motor becomes too sluggish

C) The motor loses all torque

D) The system becomes unstable and oscillates

---

The system becomes unstable and oscillates

///

## What is an S-curve in motion control?

---

A) A type of PID algorithm

B) A measurement of motor torque

C) A graph showing system errors

D) A smooth motion profile with controlled acceleration and deceleration

---

A smooth motion profile with controlled acceleration and deceleration

///

## True or False: The integral term should be the first parameter adjusted in a PID controller.

---

A) False

B) True

---

False

///

## What happens when proportional gain is set very low?

---

A) The position feedback fails

B) The motor acts like a weak spring

C) The system becomes unstable

D) The motor becomes extremely stiff

---

The motor acts like a weak spring

///

## What is the purpose of the integral term in a PID controller?

---

A) To prevent overshooting

B) To smooth out motion profiles

C) To increase motor speed

D) To eliminate steady-state errors

---

To eliminate steady-state errors
