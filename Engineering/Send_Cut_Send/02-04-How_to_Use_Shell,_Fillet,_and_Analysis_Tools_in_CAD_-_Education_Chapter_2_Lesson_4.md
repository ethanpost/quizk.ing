## [How to Use Shell, Fillet, and Analysis Tools in CAD - Education Chapter 2 Lesson 4](https://www.youtube.com/watch?v=t23gqRdv8B0)

### Take the quiz [here](https://ethanpost.github.io/quizk.ing) by searching for the title.

## Using Shell, Fillet, and Analysis Tools in CAD Overview

### Purpose and Context
- Understanding how multiple objects interact in CAD assemblies
- Creating void space for Arduino to live in
- Using advanced modification techniques
- Implementing visual analysis tools for better understanding

### Advanced Modification Tools
- Shell technique for creating thin web around inside of box
- Corner radius (fillet) for visual appeal
- Analysis tool for X-ray vision of object interactions
- Multiple modification options available in CAD

### Shell Feature Process
- Located in Modify menu of ribbon
- Select face or body to create void
- Choose top of box for void creation
- Specify wall thickness (0.125 inches)
- Creates internal void for component placement
- Appears in history as shell feature

### Shell Feature Management
- Right-click to edit feature
- Can modify wall thickness after creation
- Example: change from 0.125 to 0.1 for thinner walls
- Alternative method: use offset plane and sketch with offset
- Shell method is more efficient than manual approach

### Fillet Feature Application
- Also known as corner radius
- Located in Modify menu
- Creates round radius on inside lines
- Improves visual appearance
- Can select through walls in Fusion 360
- Don't need to rotate part to select all lines

### Fillet Design Considerations
- Start with 0.125 inch radius (1/8 inch)
- Nice round number, easy to work with
- Must avoid interference with Arduino
- Larger radius (0.5 or 0.75) causes interference
- Arduino hits radius corners with larger values
- Circuit board won't drop into box with interference

### Analysis Tool Introduction
- Located in Utilities menu
- Section analysis provides X-ray vision
- Creates cut plane to see internal structure
- Helps understand object interactions
- Essential for checking clearances and interference

### Section Analysis Process
- Select plane for cut location
- Move cut plane back and forth
- Two colors represent different objects
- Orange: bottom box component
- Yellow: Arduino component
- Appears in analysis tree as sectional

### Analysis Tool Features
- Turn analysis on and off
- No actual part modification
- Pure visualization tool
- Create multiple sectional analyses
- See different angles (90 degrees each way)
- Only one section visible at a time
- Right-click to edit sections

### Design Validation
- Check pin clearance at bottom
- Ensure Arduino floats inside box
- Verify no interference with walls
- Confirm proper spacing for assembly
- Validate design before finalizing

### Next Steps Preparation
- Ready to modify bottom box further
- Add USB ports and mounting holes
- Complete enclosure design
- Foundation set for final assembly

### Terms
- Shell - CAD feature that creates a thin wall around the inside of a solid, creating a void
- Fillet - A rounded corner or edge created by adding radius to sharp edges
- Corner Radius - Another term for fillet, creates rounded corners
- Analysis Tool - CAD feature that provides cross-sectional views for examining internal geometry
- Section Analysis - Tool that creates cut planes to see inside objects like X-ray vision
- Wall Thickness - The thickness of material remaining after shell operation
- Void - Empty space created inside a solid object
- Interference - When two objects occupy the same space, causing conflicts
- Cut Plane - Imaginary surface used in section analysis to slice through objects
- X-ray Vision - Ability to see through solid objects using analysis tools

///

What is the main challenge when designing multiple objects in CAD?

---

A) Understanding how objects interact with each other

B) File size limitations

C) Rendering speed

D) Memory usage

---

Understanding how objects interact with each other

///

What does the shell technique do?

---

A) Changes the color of the object

B) Creates a thin web around the inside of the box

C) Adds material to the outside

D) Deletes the entire object

---

Creates a thin web around the inside of the box

///

Where is the shell feature located in Fusion 360?

---

A) Utilities menu

B) Create menu

C) Modify menu

D) Assemble menu

---

Modify menu

///

What face should you select when using the shell feature?

---

A) The side face

B) Any face

C) The top face

D) The bottom face

---

The top face

///

What wall thickness is used for the shell feature?

---

A) 0.5 inches

B) 0.125 inches

C) 0.25 inches

D) 0.1 inches

---

0.125 inches

///

How can you modify the shell feature after creation?

---

A) Use the timeline

B) Delete and recreate it

C) Right-click and edit feature

D) Double-click the feature

---

Right-click and edit feature

///

What is another name for corner radius?

---

A) Round

B) Chamfer

C) Bevel

D) Fillet

---

Fillet

///

What is the purpose of adding fillets to the inside corners?

---

A) To reduce manufacturing time

B) To make it more visually appealing

C) To reduce material usage

D) To increase strength

---

To make it more visually appealing

///

What radius value causes interference with the Arduino?

---

A) 0.75 inches

B) 0.125 inches

C) 0.5 inches

D) 0.25 inches

---

0.5 inches

///

Where is the analysis tool located?

---

A) Assemble menu

B) Create menu

C) Utilities menu

D) Modify menu

---

Utilities menu

///

What does the section analysis tool provide?

---

A) Manufacturing information

B) X-ray vision of object interactions

C) Cost analysis

D) Material properties

---

X-ray vision of object interactions

///

What color represents the bottom box in section analysis?

---

A) Red

B) Orange

C) Blue

D) Green

---

Orange

///

What color represents the Arduino in section analysis?

---

A) Green

B) Blue

C) Yellow

D) Red

---

Yellow

///

Can you see multiple sections at the same time?

---

A) Yes, up to four

B) Yes, but only two

C) No, only one at a time

D) Yes, always

---

No, only one at a time

///

What is the next step after completing the shell and fillet operations?

---

A) Change the material

B) Add USB ports and mounting holes

C) Delete the Arduino

D) Render the part

---

Add USB ports and mounting holes

///

## Master Answer Key

1. **A** - The main challenge is understanding how multiple objects interact with each other in CAD assemblies.

2. **B** - The shell technique creates a thin web around the inside of the box, creating a void for the Arduino.

3. **C** - The shell feature is located in the Modify menu of the ribbon interface.

4. **C** - You should select the top face of the box to create the void using the shell feature.

5. **B** - A wall thickness of 0.125 inches is used for the shell feature.

6. **C** - You can right-click on the shell feature and select "edit feature" to modify it after creation.

7. **D** - Fillet is another name for corner radius, which creates rounded edges.

8. **B** - Fillets are added to inside corners to make the design more visually appealing.

9. **C** - A radius of 0.5 inches causes interference with the Arduino, preventing it from fitting properly.

10. **C** - The analysis tool is located in the Utilities menu of the top toolbar.

11. **B** - Section analysis provides X-ray vision to see how objects interact inside assemblies.

12. **B** - Orange color represents the bottom box component in section analysis.

13. **C** - Yellow color represents the Arduino component in section analysis.

14. **C** - You can only see one section at a time, though you can create multiple sections.

15. **B** - The next step is to add USB ports and mounting holes to complete the bottom box design.
