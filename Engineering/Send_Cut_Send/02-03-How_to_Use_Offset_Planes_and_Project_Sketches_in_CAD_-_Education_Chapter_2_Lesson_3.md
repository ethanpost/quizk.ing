## [How to Use Offset Planes and Project Sketches in CAD - Education Chapter 2 Lesson 3](https://www.youtube.com/watch?v=8-Fpv8QXc9Q)

### Take the quiz [here](https://ethanpost.github.io/quizk.ing) by searching for the title.

## Using Offset Planes and Project Sketches in CAD Overview

### Purpose and Context
- Creating space between parts in CAD assemblies
- Building bottom of enclosure box for Arduino
- Addressing clearance issues with Arduino pins
- Using offset planes for proper spacing

### Clearance Requirements
- Arduino pins make contact when board lays flat
- Need space or offset away from bottom of Arduino
- Measured approximately 0.080 inches with calipers
- Creating 1/8 inch spacing for proper clearance
- Ensures pins don't interfere with box bottom

### Offset Plane Creation
- Located in Construction menu of ribbon
- Multiple construction plane options available
- Offset plane specifically for creating spacing
- Click on flat object to create offset from
- Specify distance dimension (1/8 inch)
- Plane appears in construction category in tree

### Construction Plane Management
- Right-click to edit offset values later
- Construction planes appear in component tree
- Can be modified after creation
- Essential for maintaining proper spacing
- Provides reference for sketch creation

### Sketch Projection Process
- Use Create > Project command
- Projects image onto another object or plane
- References Arduino for proper hole placement
- Ensures box is correct size
- Creates duplication of Arduino features on offset plane
- Maintains accuracy of component positioning

### Box Design Process
- Create rectangle around projected Arduino outline
- Use Arduino edge for offset reference
- Apply 1/4 inch spacing around outside
- Create shell spacing around component
- Handle port side differently for cable access

### Port Side Considerations
- Charge ports and USB need to be flush
- Allows cables to pass through easily
- Easier hole cutting for connectors
- Use constraints to tie charge port corner to edge
- Maintains proper alignment for cable access

### Extrude Feature Application
- Select all profiles for extrusion
- Include mounting holes for later use
- Use multidirectional extrude (two-sided)
- Two independent arrows for different directions
- Down: 1/8 inch for bottom clearance
- Up: 1 inch for lid space and room

### Component Organization
- Set operation to "Component" for cleanliness
- Maintains organization in drawings
- Important principle from Chapter 1
- Name component "ARD bottom box"
- Prepares for additional components
- Keeps file structure clean

### Next Steps Preparation
- Ready for shell feature introduction
- Will create internal void for Arduino
- Analysis feature to view internal structure
- Foundation set for complete enclosure

### Terms
- Offset - Space or distance between two parts in CAD
- Offset Plane - A construction plane created at a specified distance from another surface
- Project - CAD command that copies geometry from one object onto another plane or surface
- Construction Plane - Reference planes used for creating geometry in CAD
- Clearance - Space provided to prevent interference between components
- Multidirectional Extrude - Extrusion feature that extends in two opposite directions
- Two-sided Extrude - Extrusion that creates geometry in both positive and negative directions
- Component - Organized grouping of CAD geometry for better file management
- Shell - CAD feature that creates hollow interior by removing material from inside
- Analysis Feature - CAD tool for examining internal structure and geometry

///

What is the main purpose of creating an offset in CAD?

---

A) To improve rendering

B) To create space between two parts 

C) To reduce file size

D) To speed up calculations

---

To create space between two parts

///

Why do we need clearance for the Arduino pins?

---

A) To improve aesthetics

B) To reduce manufacturing costs

C) The pins make contact when the board lays flat

D) To make the board lighter

---

The pins make contact when the board lays flat

///

What measurement tool is used to determine the pin clearance?

---

A) Tape measure

B) Caliper

C) Micrometer

D) Ruler

---

Caliper

///

How much clearance is created for the Arduino pins?

---

A) 1/4 inch

B) 1/2 inch

C) 1/8 inch

D) 1/16 inch

---

1/8 inch

///

Where is the Offset Plane command located in Fusion 360?

---

A) Modify menu

B) Construction menu

C) Create menu

D) Assemble menu

---

Construction menu

///

What appears in the component tree after creating an offset plane?

---

A) A sketch

B) A construction category with plane

C) A component

D) A new body

---

A construction category with plane

///

How can you modify an offset plane after creation?

---

A) Use the timeline

B) Delete and recreate it

C) Right-click and edit

D) Double-click the plane

---

Right-click and edit

///

What does the Project command do?

---

A) Creates new geometry

B) Takes an image and projects it onto another object

C) Deletes existing geometry

D) Modifies existing features

---

Takes an image and projects it onto another object

///

Why is it important to reference the Arduino when creating the box?

---

A) To make it look better

B) To reduce file size

C) To ensure holes are in proper place and box is correct size

D) To improve performance

---

To ensure holes are in proper place and box is correct size

///

How much spacing is created around the outside of the Arduino?

---

A) 1/2 inch

B) 1/8 inch

C) 1/4 inch

D) 1 inch

---

1/4 inch

///

Why are the charge ports and USB handled differently?

---

A) They look better flush

B) They need to be flush for cable access

C) They are more expensive

D) They are harder to manufacture

---

They need to be flush for cable access

///

What constraint is used to tie the charge port to the edge?

---

A) Tangent constraint

B) Parallel constraint

C) Corner constraint

D) Perpendicular constraint

---

Corner constraint

///

What type of extrude is used for the box bottom?

---

A) Sweep

B) One-directional

C) Multidirectional (two-sided)

D) Radial

---

Multidirectional (two-sided)

///

How far does the extrude go downward?

---

A) 1/2 inch

B) 1/8 inch

C) 1/16 inch

D) 1/4 inch

---

1/8 inch

///

What operation type is selected for the extrude?

---

A) Join

B) Intersect

C) Cut

D) Component

---

Component

///

## Master Answer Key

1. **B** - The main purpose of creating an offset in CAD is to create space between two parts, preventing interference.

2. **C** - Arduino pins make contact when the board lays flat, so clearance is needed to prevent this interference.

3. **B** - A caliper is used to measure the pin clearance, showing approximately 0.080 inches.

4. **C** - 1/8 inch clearance is created for the Arduino pins to provide proper spacing.

5. **B** - The Offset Plane command is located in the Construction menu of the ribbon interface.

6. **B** - A construction category with plane appears in the component tree after creating an offset plane.

7. **C** - You can right-click on the offset plane to edit and modify its values after creation.

8. **B** - The Project command takes an image and projects it onto another object, like a plane for sketching.

9. **C** - Referencing the Arduino ensures that holes are positioned correctly and the box is the proper size.

10. **C** - 1/4 inch spacing is created around the outside of the Arduino for the box shell.

11. **B** - Charge ports and USB need to be flush with the box edge to allow proper cable access.

12. **C** - A corner constraint is used to tie the charge port corner to the edge of the part.

13. **C** - A multidirectional (two-sided) extrude is used, allowing extension in both directions.

14. **B** - The extrude goes downward 1/8 inch to provide bottom clearance.

15. **D** - The operation type is set to "Component" to maintain cleanliness and organization in the drawings.
