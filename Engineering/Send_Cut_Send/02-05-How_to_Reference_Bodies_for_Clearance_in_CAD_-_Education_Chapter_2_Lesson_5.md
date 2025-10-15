## [How to Reference Bodies for Clearance in CAD - Education Chapter 2 Lesson 5](https://www.youtube.com/watch?v=ORRdr33D0_w)

### Take the quiz [here](https://ethanpost.github.io/quizk.ing) by searching for the title.

## Referencing Bodies for Clearance in CAD Overview

### Purpose and Context
- Ensuring proper clearance for assembly of multiple bodies
- Adding holes for charge port, USB, and standoff pads
- Using insert and project tools for referencing
- Finalizing bottom box preparation for lid

### Missing Components
- No holes for charge port
- No holes for USB port
- No standoff pads for Arduino mounting
- Need to add and subtract from bodies using referencing

### Mounting Pad Creation Process
- Hide Arduino to start
- Click on bottom of box to create sketch
- Reshow Arduino for reference
- Change line type to construction
- Use Create > Project to transfer Arduino holes to bottom surface
- Rehide Arduino to work on sketch

### Construction Lines Purpose
- Construction lines won't affect extrusion process
- Used for reference geometry only
- Can be converted back to solid lines later
- Provides clean separation between reference and final geometry

### Offset Process for Mounting Holes
- Offset each of the four mounting holes
- Use 0.025 inch offset
- Apply to all four mounting holes on bottom
- One hole is push button reference for lid portion
- Convert construction lines back to solid lines

### Line Type Management
- Select all offset lines (hold Shift)
- Right-click on line type
- Change back to solid line
- Creates surfaces for extrusion
- Prepares for mounting pad creation

### Extrusion with Object Reference
- Select all mounting hole profiles
- Use Extrude command
- Hide bottom box, show Arduino
- Change extend type to "To Object"
- Select bottom of Arduino as target
- Creates reference to Arduino bottom

### Reference Benefits
- Pads automatically adjust if Arduino height changes
- Maintains proper clearance relationships
- Joins pads to bottom of box
- Creates adaptive mounting system

### USB and Charge Port Cutouts
- Follow similar process to mounting pads
- Use cut feature instead of join
- Sketch on surface where ports come through
- Hide box, show Arduino
- Change line type to construction
- Project the two port surfaces

### Port Clearance Considerations
- Offset to clearance size for cutouts
- Recommend at least 0.020 inch clearance
- Ensures manufacturing capability
- Provides proper fit for connectors
- USB port and charge port both get 0.020 inch clearance

### Cut Feature Application
- Select both port profiles
- Use Extrude command
- Automatically changes to cut feature
- Important: "Objects to Cut" dropdown menu
- Can accidentally cut multiple bodies
- Hide other bodies to protect them

### Safety Considerations
- Different components provide some protection
- Single drawing can cut multiple bodies
- Hide bodies to prevent accidental cutting
- Use "Objects to Cut" menu carefully
- Maintain component separation

### Final Assembly Preparation
- Bottom box now complete
- Mounting pads in place
- USB and charge ports cut out
- Ready for top lid addition
- Foundation set for complete enclosure

### Terms
- Clearance - Space provided between components to ensure proper fit and prevent interference
- Standoff Pads - Small mounting surfaces that provide support and spacing for components
- Construction Lines - Reference geometry that doesn't affect final extrusion or cutting operations
- Project - CAD command that transfers geometry from one object to another surface
- Offset - Creating parallel geometry at a specified distance from existing features
- Extend Type - Option in extrude command that controls how far the extrusion extends
- To Object - Extrusion method that extends geometry until it reaches a specified target object
- Cut Feature - CAD operation that removes material from existing bodies
- Objects to Cut - Dropdown menu that specifies which bodies will be affected by cut operations
- Reference - CAD relationship that maintains connections between different components

///

What is the main purpose of referencing bodies in CAD?

---

A) To improve rendering

B) To ensure proper clearance for assembly 

C) To reduce file size

D) To speed up calculations

---

To ensure proper clearance for assembly

///

What components are missing from the bottom box?

---

A) Only USB holes

B) Only mounting holes

C) Charge port holes, USB holes, and standoff pads

D) Only charge port holes

---

Charge port holes, USB holes, and standoff pads

///

What line type is used initially when creating mounting pads?

---

A) Hidden lines

B) Construction lines

C) Solid lines

D) Dashed lines

---

Construction lines

///

Why are construction lines used for mounting pad creation?

---

A) They are required by the software

B) They won't affect the extrusion process

C) They look better

D) They are easier to see

---

They won't affect the extrusion process

///

How many mounting holes are offset for the Arduino?

---

A) Six

B) Two

C) Four

D) Three

---

Four

///

What offset distance is used for the mounting holes?

---

A) 0.250 inches

B) 0.025 inches

C) 0.020 inches

D) 0.125 inches

---

0.025 inches

///

What is one of the mounting holes actually used for?

---

A) Reset button

B) USB port

C) Push button reference for lid

D) Charge port

---

Push button reference for lid

///

What key is held while selecting multiple lines?

---

A) Tab

B) Alt

C) Shift

D) Ctrl

---

Shift

///

What extend type is used for mounting pad extrusion?

---

A) Through All

B) Distance

C) To Object

D) To Next

---

To Object

///

What happens if the Arduino height changes?

---

A) The pads disappear

B) The pads automatically adjust

C) The pads break

D) The pads become misaligned

---

The pads automatically adjust

///

What clearance is recommended for USB and charge ports?

---

A) 0.040 inches

B) 0.010 inches

C) 0.020 inches

D) 0.030 inches

---

0.020 inches

///

What feature is used to create the port cutouts?

---

A) Combine

B) Cut

C) Join

D) Intersect

---

Cut

///

What dropdown menu is important when using cut features?

---

A) Objects to Cut

B) Operation Type

C) Direction

D) Distance

---

Objects to Cut

///

How can you protect other bodies from being accidentally cut?

---

A) Move them

B) Delete them

C) Hide them

D) Lock them

---

Hide them

///

What is the next step after completing the bottom box?

---

A) Change the material

B) Add the top lid to the assembly

C) Delete the Arduino

D) Render the part

---

Add the top lid to the assembly

///

## Master Answer Key

1. **B** - Referencing bodies in CAD ensures proper clearance for assembly, preventing interference between components.

2. **C** - The missing components are charge port holes, USB holes, and standoff pads for proper Arduino mounting.

3. **B** - Construction lines are used initially when creating mounting pads to provide reference geometry.

4. **B** - Construction lines are used because they won't affect the extrusion process, keeping reference separate from final geometry.

5. **C** - Four mounting holes are offset for the Arduino, corresponding to its four mounting points.

6. **B** - An offset distance of 0.025 inches is used for the mounting holes to create proper clearance.

7. **C** - One of the mounting holes is actually used as a push button reference for the lid portion of the build.

8. **C** - The Shift key is held while selecting multiple lines to create a multi-selection.

9. **C** - The "To Object" extend type is used, which extends the extrusion until it reaches the Arduino bottom.

10. **B** - If the Arduino height changes, the pads automatically adjust because they reference the Arduino bottom.

11. **C** - A clearance of 0.020 inches is recommended for USB and charge ports to ensure manufacturing capability.

12. **B** - The Cut feature is used to create the port cutouts, removing material from the box.

13. **A** - The "Objects to Cut" dropdown menu is important as it specifies which bodies will be affected by cut operations.

14. **C** - You can hide other bodies to protect them from being accidentally cut during cut operations.

15. **B** - The next step is to add the top lid to the assembly to complete the enclosure design.
