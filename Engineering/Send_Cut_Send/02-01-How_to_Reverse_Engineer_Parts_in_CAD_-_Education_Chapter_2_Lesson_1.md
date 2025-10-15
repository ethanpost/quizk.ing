## [How to Reverse Engineer Parts in CAD - Education Chapter 2 Lesson 1](https://www.youtube.com/watch?v=txfu_dvbf-Q)

### Take the quiz [here](https://ethanpost.github.io/quizk.ing) by searching for the title.

## Reverse Engineering Parts in CAD Overview

### Purpose and Context
- Designing with intention of creating real parts using CAD
- Building on Chapter 1 CAD tools knowledge
- Focus on reverse engineering existing parts
- Creating multi-part assembly for circuit board enclosure

### Project Details
- Arduino Uno circuit board as reference part
- 3D printing manufacturing method
- Less manufacturing rules compared to other methods
- Focus on design rather than manufacturing techniques

### Reverse Engineering Process
- Identify key features of existing parts
- Avoid getting caught up in intricate details
- Focus on essential measurements only
- Use measurement tools like calipers

### Measurement Tools and Techniques
- Digital caliper for precise measurements
- Switch between inches and millimeters
- Measure outer rectangular shape dimensions
- Identify mounting hole positions and diameters
- Measure distances from edges to hole centers

### Hole Measurement Methods
- Measure from edge to hole edge, then add radius for center position
- Measure between holes: inside-to-inside plus both radii equals center-to-center distance
- Alternative: measure outside-to-outside minus both radii
- Works for same or different sized holes

### Key Components to Identify
- Outer rectangular shape (length and width)
- Four mounting holes with positions and diameters
- USB port location and dimensions
- Charge port location and dimensions
- Reset button location and dimensions

### CAD Implementation
- Create robust sketch with all dimensions
- Ensure all features are black and defined
- Include height, width, length measurements
- Include mounting hole requirements

### Alternative Approaches
- Manual detailed measurement for all features
- Use online resources like GrabCAD and Thingiverse
- Download existing STEP files
- Upload files to Fusion 360 data panel

### Best Practices
- Keep it simple - focus on essential features only
- Don't overthink the process
- Use precision tools appropriately
- Consider online resources for complex parts

### Terms
- Reverse Engineering - The process of analyzing an existing part to understand its design and recreate it in CAD
- Caliper - A precision measurement tool used to measure dimensions of parts
- Mounting Holes - Holes in a part used to attach it to other components
- STEP File - A standardized file format for 3D CAD data exchange
- GrabCAD - Online platform for sharing CAD models and engineering resources
- Thingiverse - Online community for sharing 3D printable designs
- Arduino Uno - A popular microcontroller development board
- Fusion 360 - Autodesk's cloud-based CAD software
- Data Panel - Interface in Fusion 360 for managing files and projects

///

What is the main purpose of reverse engineering in CAD?

---

A) To improve manufacturing processes

B) To analyze existing parts and recreate them in CAD

C) To create entirely new designs from scratch

D) To reduce material costs

---

To analyze existing parts and recreate them in CAD

///

What type of circuit board is used as the reference part in this lesson?

---

A) ESP32

B) Arduino Mega

C) Arduino Uno

D) Raspberry Pi

---

Arduino Uno

///

What manufacturing method is chosen for this project?

---

A) Injection molding

B) 3D printing

C) Laser cutting

D) CNC machining

---

3D printing

///

What is the primary reason for choosing 3D printing for this project?

---

A) It's the fastest manufacturing method

B) It produces the highest quality parts

C) It has fewer manufacturing rules and constraints

D) It's the cheapest manufacturing method

---

It has fewer manufacturing rules and constraints

///

What measurement tool is primarily used in this lesson?

---

A) Micrometer

B) Tape measure

C) Caliper

D) Ruler

---

Caliper

///

How many mounting holes does the Arduino Uno have?

---

A) Six

B) Four

C) Three

D) Two

---

Four

///

When measuring hole positions, what should you add to the edge-to-hole measurement to find the center?

---

A) Half the diameter

B) The circumference

C) The diameter

D) The radius

---

The radius

///

What is the correct method for measuring center-to-center distance between two holes?

---

A) Measure from center to center directly

B) Measure from inside edge to inside edge and add both radii

C) Estimate by eye

D) Measure from outside edge to outside edge

---

Measure from inside edge to inside edge and add both radii

///

Which online platforms are mentioned for finding existing CAD models?

---

A) Fusion 360 and Inventor

B) AutoCAD and SolidWorks

C) GrabCAD and Thingiverse

D) GitHub and Stack Overflow

---

GrabCAD and Thingiverse

///

What file format is typically downloaded from online CAD repositories?

---

A) PDF file

B) DWG file

C) STEP file

D) STL file

---

STEP file

///

In Fusion 360, where do you upload downloaded CAD files?

---

A) Browser panel

B) Data panel

C) Timeline panel

D) Sketch panel

---

Data panel

///

What does the instructor recommend regarding detailed measurements?

---

A) Use automated scanning tools

B) Always measure every single detail

C) Only measure when absolutely necessary

D) Hire professional measurement services

---

Only measure when absolutely necessary

///

What is the key advice given about the reverse engineering process?

---

A) Use only digital tools

B) Always use the most expensive tools

C) Measure everything multiple times

D) Don't overthink the process

---

Don't overthink the process

///

What color should all features be in a properly defined CAD sketch?

---

A) Green

B) Black

C) Red

D) Blue

---

Black

///

What are the essential measurements needed for the Arduino Uno board?

---

A) Only the mounting holes

B) Every component on the board

C) Outer dimensions and mounting hole details

D) Only the outer dimensions

---

Outer dimensions and mounting hole details

///

## Master Answer Key

1. **B** - Reverse engineering is specifically about analyzing existing parts to understand their design and recreate them in CAD software.

2. **C** - The Arduino Uno is explicitly mentioned as the reference circuit board used throughout the lesson.

3. **B** - 3D printing is chosen as the manufacturing method for this project.

4. **C** - 3D printing is selected because it has fewer manufacturing rules and constraints, allowing focus on design rather than manufacturing techniques.

5. **C** - A digital caliper is the primary measurement tool demonstrated and used throughout the lesson.

6. **B** - The Arduino Uno has four mounting holes that need to be measured and positioned.

7. **D** - To find the center of a hole, you measure from the edge to the hole edge, then add the radius of the hole.

8. **B** - The correct method is to measure from inside edge to inside edge of two holes, then add both radii to get the center-to-center distance.

9. **C** - GrabCAD and Thingiverse are the two online platforms specifically mentioned for finding existing CAD models.

10. **C** - STEP files are the standard file format for CAD data exchange that can be downloaded from online repositories.

11. **B** - The data panel in Fusion 360 is where you upload downloaded CAD files.

12. **C** - The instructor recommends only doing detailed measurements when absolutely necessary, as it can be time-consuming.

13. **D** - The key advice is to not overthink the reverse engineering process and keep it simple.

14. **B** - In a properly defined CAD sketch, all features should be black, indicating they are fully constrained.

15. **C** - The essential measurements include the outer rectangular dimensions and the mounting hole positions and diameters.
