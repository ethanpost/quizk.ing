## [How to Design a CAD Lid with Joints, Ventilation & Access Features - Education Chapter 2 Lesson 6](https://www.youtube.com/watch?v=1d8ZCIBnA1A)

### Take the quiz [here](https://ethanpost.github.io/quizk.ing) by searching for the title.

## Designing CAD Lid with Joints, Ventilation & Access Features Overview

### Purpose and Context
- Creating components with reference to other components
- Designing lid for Arduino enclosure assembly
- Addressing design considerations for functional enclosure
- Implementing joints to lock components together

### Design Considerations
- PCBs create heat that needs ventilation
- Need reset button access hole
- Require wire out options for functionality
- Components must be properly connected and located

### Lid Creation Process
- Use top of bottom box as reference
- Create sketch on top surface
- Automatically get projection of box outline
- Select outer and inner ring profiles
- Extrude up 0.125 inches for consistent wall thickness

### Component vs Body Selection
- Choose "New Component" instead of "New Body"
- Important distinction for file organization
- Reference Chapter 1 for component vs body explanation
- Maintains proper assembly structure

### Locator Feature Creation
- Lid needs internal locator to prevent floating
- Create locator extrusion on inside of lid
- Use existing sketch for quick creation
- Extrude down 0.050 inches for locator leg
- Hide bottom box to prevent joining both assemblies

### Joint Creation for Positioning
- Components are not connected without joints
- Lid can be dragged anywhere without joint
- Create joint between lid and bottom box
- Select two surfaces and two points for contact
- Use "Flip" option to correct orientation if needed

### Slip Fit Adjustment
- Locator leg same size as hole creates tight fit
- Use Press Pull tool to create clearance
- Select locator faces and apply -0.020 inch offset
- Creates slip fit for easier assembly
- Allows proper lid positioning

### Ventilation Design
- Solid box traps heat from PCB
- Create ventilation slots in lid
- Use center point slot tool for easy creation
- Position at origin for automatic centering
- Radius: 0.125 inches, Length: 1.75 inches

### Pattern Creation Strategy
- Pattern extrusion instead of sketch
- Avoids selecting multiple times for large arrays
- Example: 10x10 array = 100 selections vs 1 selection
- More efficient workflow for complex patterns
- Use rectangular pattern with symmetric option

### Reset Button Access
- Create hole for reset button access
- Hide lid, show Arduino sketches
- Project reset button hole from Arduino
- Extrude through lid for access
- Allows wire or screwdriver access

### Wire Access Slot
- Create slot on back for wire routing
- Sketch overlaps both components
- Use center slot with midpoint constraint
- Radius: 0.125 inches, Length: 1 inch
- Demonstrates multi-component cutting

### Multi-Component Operations
- "Objects to Cut" dropdown controls which components are affected
- Can select/deselect specific components
- Hide components to protect from cutting
- Useful for complex assembly operations
- Provides precise control over cutting operations

### Manufacturing Considerations
- Wire slot not machinable but 3D printable
- Demonstrates Design for Manufacturing (DFM) principles
- Considers manufacturing method capabilities
- Optimizes design for chosen production method

### Final Assembly
- Complete 3D printable enclosure
- All components properly joined
- Ventilation and access features included
- Ready for 3D printing
- Foundation for troubleshooting lessons

### Terms
- Locator - A feature that positions and aligns components in assemblies
- Slip Fit - A clearance fit that allows easy assembly while maintaining alignment
- Press Pull - CAD tool that allows direct manipulation of faces and features
- Center Point Slot - Slot tool that creates slots centered on a specified point
- Pattern - CAD feature that creates multiple copies of geometry in regular arrangements
- Symmetric Pattern - Pattern that creates copies on both sides of a center point
- Multi-Component Operations - CAD operations that affect multiple components simultaneously
- Objects to Cut - Dropdown menu that specifies which components will be affected by cut operations
- Design for Manufacturing (DFM) - Design principles that consider manufacturing capabilities and limitations
- Ventilation - Openings designed to allow heat to escape from enclosed components

///

What is the main purpose of creating a lid component?

---

A) To improve aesthetics

B) To create a component with reference to another component

C) To reduce material usage

D) To reduce manufacturing time

---

To create a component with reference to another component

///

What design consideration is addressed by creating ventilation?

---

A) Weight reduction

B) Cost savings

C) PCBs create heat that needs to escape

D) Aesthetics

---

PCBs create heat that needs to escape

///

What operation type should be selected when creating the lid?

---

A) Join

B) Cut

C) New Component

D) New Body

---

New Component

///

Why is a locator feature needed for the lid?

---

A) To improve aesthetics

B) To reduce cost

C) To prevent the lid from floating around

D) To reduce weight

---

To prevent the lid from floating around

///

What tool is used to create slip fit clearance?

---

A) Shell

B) Press Pull

C) Extrude

D) Fillet

---

Press Pull

///

How much clearance is created for the slip fit?

---

A) 0.040 inches

B) 0.010 inches

C) 0.020 inches

D) 0.030 inches

---

0.020 inches

///

What is the recommended approach for creating multiple ventilation slots?

---

A) Create each slot individually

B) Pattern the extrusion

C) Use mirror feature

D) Pattern the sketch

---

Pattern the extrusion

///

Why is patterning the extrusion preferred over patterning the sketch?

---

A) It uses less memory

B) It looks better

C) It's faster to calculate

D) It avoids selecting multiple times for large arrays

---

It avoids selecting multiple times for large arrays

///

What type of slot is used for ventilation?

---

A) Three point slot

B) Center point slot

C) Two point slot

D) Arc slot

---

Center point slot

///

What are the dimensions of the ventilation slot?

---

A) Radius: 0.200", Length: 2.25"

B) Radius: 0.150", Length: 2.00"

C) Radius: 0.125", Length: 1.75"

D) Radius: 0.100", Length: 1.50"

---

Radius: 0.125", Length: 1.75"

///

How is the reset button hole created?

---

A) Created with offset

B) Manually drawn

C) Projected from Arduino

D) Copied from another part

---

Projected from Arduino

///

What constraint is used for the wire access slot?

---

A) Tangent constraint

B) Midpoint constraint

C) Parallel constraint

D) Perpendicular constraint

---

Midpoint constraint

///

What dropdown menu controls which components are cut?

---

A) Direction

B) Distance

C) Objects to Cut

D) Operation Type

---

Objects to Cut

///

Is the wire access slot machinable?

---

A) Yes, but expensive

B) No, but it's 3D printable

C) Yes, easily machinable

D) No, not manufacturable

---

No, but it's 3D printable

///

What does DFM stand for?

---

A) Design for Materials

B) Design for Manufacturing

C) Design for Marketing

D) Design for Maintenance

---

Design for Manufacturing

///

## Master Answer Key

1. **B** - The main purpose is to create a component with reference to another component, building on the existing bottom box.

2. **C** - Ventilation is created because PCBs generate heat that needs to escape from the enclosed space.

3. **C** - "New Component" should be selected to maintain proper assembly structure and organization.

4. **C** - A locator feature prevents the lid from floating around by providing internal positioning.

5. **B** - The Press Pull tool is used to create slip fit clearance by directly manipulating faces.

6. **C** - 0.020 inches of clearance is created for the slip fit, allowing easier assembly.

7. **B** - Patterning the extrusion is recommended because it avoids having to select multiple times for large arrays.

8. **D** - Patterning the extrusion is preferred because it avoids selecting multiple times for large arrays (e.g., 10x10 = 100 selections vs 1 selection).

9. **B** - A center point slot is used for ventilation, which creates slots centered on a specified point.

10. **C** - The ventilation slot has a radius of 0.125 inches and length of 1.75 inches.

11. **C** - The reset button hole is created by projecting the hole from the Arduino reference.

12. **B** - A midpoint constraint is used to position the wire access slot at the midpoint of a line.

13. **C** - The "Objects to Cut" dropdown menu controls which components will be affected by cut operations.

14. **B** - The wire access slot is not machinable but is 3D printable, demonstrating DFM principles.

15. **B** - DFM stands for Design for Manufacturing, which considers manufacturing capabilities and limitations.
