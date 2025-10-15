## [How to Create Assemblies in CAD with Joints - Education Chapter 2 Lesson 2](https://www.youtube.com/watch?v=9N2CZciWCTo)

### Take the quiz [here](https://ethanpost.github.io/quizk.ing) by searching for the title.

## Creating Assemblies in CAD with Joints Overview

### Purpose and Context
- Multi-part assemblies don't automatically reference each other in CAD
- Need to create references using assembly tools called joints
- Building on previous lesson's reverse-engineered Arduino Uno
- Creating new main file for assembly construction

### File Organization Strategy
- Create separate main file for assembly instead of building around original Arduino
- Allows sharing Arduino across multiple different assemblies
- Prevents creating different boxes around the same component
- Keeps files clean and organized
- Enables reuse of components in other projects

### Component Insertion Process
- Use Insert > Insert Component from ribbon menu
- Opens file browser to select reverse-engineered Arduino file
- Component appears in assembly with bodies and sketches visible
- Can show or hide related elements in component tree
- Right-click reveals chain link to original file

### File Linking and Management
- Components maintain link to original file
- Changes in original file propagate to assembly
- Break link option severs connection between files
- Unground from parent removes initial positioning constraints
- Prevents floating objects that could crash the file

### Joint Feature Overview
- Found in Assemble > Joint in ribbon menu
- Quick key shortcut: J
- Creates relationships between components
- Two main tabs: Motion and Position
- Motion tab dictates type of joint behavior

### Joint Types and Motion
- Rigid joint: Like super glue, no motion between objects
- Slider joints: Allow linear motion
- Ball joints: Allow rotational motion
- Complex joints provide flexibility while maintaining relationships
- Rigid joint used for Arduino positioning

### Joint Positioning Process
- Select two points and plane combinations
- First selection: bottom of Arduino board (bottom center)
- Second selection: origin plane and center point
- Arduino grays out after first selection (prevents self-reference)
- Origin must be visible for proper selection

### Assembly Benefits
- Creates solid, controlled component positioning
- Joint appears in history and component tree
- All relationships can be edited later
- Provides robust foundation for further design
- Ready for referencing and box creation

### Next Steps Preparation
- Assembly ready for offset plane creation
- Foundation set for bottom box construction
- Component properly positioned and constrained
- Ready to begin enclosure design process

### Terms
- Assembly - A collection of multiple parts brought together in CAD with defined relationships
- Joint - A CAD tool that creates relationships and constraints between components in an assembly
- Rigid Joint - A joint type that locks components together with no relative motion
- Component Tree - The hierarchical structure showing all parts, bodies, and sketches in an assembly
- Chain Link - Visual indicator showing connection between inserted component and original file
- Unground from Parent - Removing initial positioning constraints from an inserted component
- Origin - The reference point (0,0,0) used as the base coordinate system in CAD
- Insert Component - CAD command to bring external parts into an assembly file
- Motion Tab - Interface section in joint tool that controls how components can move relative to each other
- Position Tab - Interface section in joint tool that defines where components are located relative to each other

///

What is the main purpose of using joints in CAD assemblies?

---

A) To reduce file size

B) To create references between components

C) To improve rendering quality

D) To speed up calculations

---

B) To create references between components

///

Why is it recommended to create a separate main file for the assembly instead of building around the original Arduino?

---

A) To improve performance

B) To save disk space

C) To allow sharing the Arduino across multiple assemblies

D) To reduce file complexity

---

C) To allow sharing the Arduino across multiple assemblies

///

Where is the Insert Component command located in Fusion 360?

---

A) Create menu

B) Insert menu

C) Modify menu

D) Assemble menu

---

B) Insert menu

///

What does the chain link icon indicate when right-clicking on a component?

---

A) The component is hidden

B) The component has a link back to the original file

C) The component is locked

D) The component is corrupted

---

B) The component has a link back to the original file

///

What happens when you click "Break Link" on a component?

---

A) The component is moved to a new location

B) The two files are severed and changes won't propagate

C) The component is deleted

D) The component is duplicated

---

B) The two files are severed and changes won't propagate

///

What does "Unground from Parent" do?

---

A) Creates a copy of the component

B) Removes initial positioning constraints

C) Deletes the component

D) Hides the component

---

B) Removes initial positioning constraints

///

What is the quick key shortcut for the Joint command?

---

A) K

B) J

C) M

D) L

---

B) J

///

What does a Rigid joint do?

---

A) Creates flexible connections

B) Allows sliding motion

C) Locks components together with no motion

D) Allows free rotation

---

C) Locks components together with no motion

///

What are the two main tabs in the Joint dialog box?

---

A) Size and Shape

B) Motion and Position

C) Speed and Direction

D) Color and Material

---

B) Motion and Position

///

What happens to the Arduino after selecting the first point for a joint?

---

A) It turns red

B) It grays out

C) It disappears

D) It doubles in size

---

B) It grays out

///

Why does the Arduino gray out after the first joint selection?

---

A) It's being deleted

B) It's being copied

C) You can't select another point on the same component

D) It's being processed

---

C) You can't select another point on the same component

///

What must be visible to properly select the origin for joint positioning?

---

A) The browser

B) The timeline

C) The origin

D) The component tree

---

C) The origin

///

What appears in the history after creating a joint?

---

A) A component

B) A joint entry

C) A sketch

D) A body

---

B) A joint entry

///

What appears in the component tree after creating a joint?

---

A) A material

B) A new body

C) A relationship entry

D) A sketch

---

C) A relationship entry

///

What is the next step after successfully creating the joint?

---

A) Add more components

B) Create offset planes and start building the box

C) Delete the Arduino

D) Render the assembly

---

B) Create offset planes and start building the box

///

## Master Answer Key

1. **B** - Joints are specifically used to create references and relationships between components in CAD assemblies.

2. **C** - Creating a separate main file allows the Arduino to be shared across multiple different assemblies without conflicts.

3. **B** - The Insert Component command is located in the Insert menu of the ribbon interface.

4. **B** - The chain link icon indicates that the component maintains a connection to its original source file.

5. **B** - Breaking the link severs the connection between files, preventing changes from propagating between them.

6. **B** - "Unground from Parent" removes the initial positioning constraints that lock the component in place.

7. **B** - The quick key shortcut for the Joint command is "J" as mentioned in the lesson.

8. **C** - A Rigid joint is described as being "like super glue" that locks components together with no relative motion.

9. **B** - The Joint dialog box has two main tabs: Motion (which controls joint type) and Position (which controls placement).

10. **B** - The Arduino grays out after the first selection to prevent selecting another point on the same component.

11. **C** - The Arduino grays out because you cannot select another point on the same component for joint creation.

12. **C** - The origin must be visible to properly select it as the reference point for joint positioning.

13. **B** - A joint entry appears in the history timeline after successfully creating a joint.

14. **C** - A relationship entry appears in the component tree showing the joint constraint.

15. **B** - The next step is to create offset planes and begin building the enclosure box around the Arduino.
