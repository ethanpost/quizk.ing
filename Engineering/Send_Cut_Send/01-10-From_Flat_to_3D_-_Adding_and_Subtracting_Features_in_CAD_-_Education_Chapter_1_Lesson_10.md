# [From Flat to 3D: Adding and Subtracting Features in CAD - Quiz](https://www.youtube.com/watch?v=QE1BqjvIQY4)

### Take the quiz [here](https://ethanpost.github.io/quizk.ing) by searching for the title.

### You can also import this file into [Mochi](https://mochi.cards/).
- When importing make sure you select Markdown as the format.
- Select "Multiple cards per .md file", 
- Set a ```triple backslash``` as the string delimiter, like this ///
- Use the link to the raw file in GitHub instead of downloading and importing if you prefer.

## Outline

### Introduction to 3D CAD Features
- Adding dimension to CAD parts is a multi-step process
- Not all CAD parts are flat - some require 3D features
- Example used: washer design with additional features

### Key Process Steps
- Create a sketch on the actual object surface (not origin planes)
- Choose to either add or subtract from the body
- Use extrude operation to apply changes

### Key Terms: Join and Cut Operations
- Join operation: adds material to the existing body
- Cut operation: subtracts material from the existing body
- These are the two main options in the extrude process

### Practical Demonstration: Creating Features on a Washer
- Starting with an existing washer body
- Creating a new sketch on the washer surface
- Drawing two circles of equal size
- Adding construction lines for proper dimensioning
- Setting constraints: equal circles, 90-degree angles, 45-degree angle
- Setting hole diameter to 12 mm
- Ensuring all lines turn black (fully constrained)

### Adding Material: Join Operation
- Selecting the first circle/profile
- Using extrude with join operation
- Adding 5 mm dimension
- Result: pin design added to washer
- Creates one unified body (not separate components)
- Sketch disappears after operation

### Subtracting Material: Cut Operation
- Re-showing the sketch using the eyeball icon
- Selecting the second circle/profile
- Using extrude with cut operation
- Direction matters: up switches to join, down/through switches to cut
- Red color indicates cut operation
- Result: hole created in the washer

### Important Concepts
- Multiple bodies can be selected for operations
- Direction of extrude determines operation type
- Sketches disappear after successful operations
- All features become part of one unified body
- Robust sketching requires all lines to be black (fully constrained)

### Terms
- Join - An extrude operation that adds material to an existing body
- Cut - An extrude operation that subtracts material from an existing body
- Extrude - A CAD operation that extends a 2D sketch into 3D space
- Construction lines - Reference lines used for dimensioning and constraints
- Fully constrained - When all sketch elements are properly dimensioned and constrained (appear black)
- Origin planes - The default reference planes (XY, XZ, YZ) in CAD software
- Surface sketch - A sketch created directly on a 3D object's surface rather than on origin planes

///

## Quiz

What is the main purpose of adding dimension to CAD parts?

---

A) To improve rendering speed

B) To reduce file size 

C) To create 3D features and complexity

D) To make them look more professional

---

C) To create 3D features and complexity

///

What are the two key operations available in the extrude process?

---

A) Create and delete

B) Join and cut

C) Build and destroy

D) Add and remove

---

B) Join and cut

///

What does the join operation do in CAD?

---

A) Creates a new sketch

B) Removes material from a body

C) Connects two separate bodies

D) Adds material to an existing body

---

D) Adds material to an existing body

///

What does the cut operation do in CAD?

---

A) Creates construction lines

B) Divides a body into two parts

C) Adds material to an existing body

D) Subtracts material from an existing body

---

D) Subtracts material from an existing body

///

Where should you create a sketch when adding 3D features to an existing part?

---

A) In a separate file

B) On construction lines

C) On the actual object surface

D) On the origin planes

---

C) On the actual object surface

///

What indicates that a sketch is fully constrained and robust?

---

A) All lines turn red

B) All lines turn green

C) All lines turn black

D) All lines turn blue

---

C) All lines turn black

///

In the demonstration, what diameter was set for the holes?

---

A) 15 mm

B) 20 mm

C) 10 mm

D) 12 mm

---

D) 12 mm

///

What happens to the sketch after a successful extrude operation?

---

A) It becomes editable

B) It disappears

C) It turns red

D) It remains visible

---

B) It disappears

///

When using the join operation, what happens to the number of bodies?

---

A) The body is deleted

B) It remains one unified body

C) The number of bodies increases

D) A new body is created

---

B) It remains one unified body

///

How do you re-show a sketch that has disappeared after an extrude operation?

---

A) Right-click and select "show"

B) Double-click the body

C) Click the eyeball icon

D) Press Ctrl+Z

---

C) Click the eyeball icon

///

What happens when you drag the extrude direction upward?

---

A) The operation is cancelled

B) Nothing changes

C) It switches to join operation

D) It switches to cut operation

---

C) It switches to join operation

///

What color indicates a cut operation is being performed?

---

A) Yellow

B) Red

C) Blue

D) Green

---

B) Red

///

What angle was set between the construction lines in the demonstration?

---

A) 90 degrees

B) 30 degrees

C) 60 degrees

D) 45 degrees

---

D) 45 degrees

///

What is the purpose of construction lines in CAD sketching?

---

A) To separate features

B) To create holes

C) For dimensioning and constraints

D) To add visual appeal

---

C) For dimensioning and constraints

///

When multiple bodies exist, what can you select in the extrude operation?

---

A) Only the first body

B) Which object to cut or not cut

C) All bodies automatically

D) Only the last body

---

B) Which object to cut or not cut

///

What does it mean when the instructor says "everything is now robust"?

---

A) The operation is complete

B) The material is thick

C) The design is strong

D) The sketch is fully constrained

---

D) The sketch is fully constrained

///

## Master Answer Key

1. C – Adding dimension to CAD parts creates 3D features and complexity, moving beyond flat designs to more sophisticated parts.

2. B – Join and cut are the two main operations in the extrude process, allowing you to either add or subtract material.

3. D – The join operation adds material to an existing body, creating features like pins or protrusions.

4. D – The cut operation subtracts material from an existing body, creating holes or removing sections.

5. C – Sketches for 3D features should be created on the actual object surface, not on origin planes, to properly interface with the existing geometry.

6. C – When all lines turn black, it indicates the sketch is fully constrained with proper dimensions and relationships.

7. D – The holes in the demonstration were set to 12 mm diameter for the washer design.

8. B – Sketches disappear after successful extrude operations, which is normal behavior in CAD software.

9. B – The join operation keeps everything as one unified body rather than creating separate components.

10. C – The eyeball icon is used to toggle sketch visibility, allowing you to re-show sketches that have disappeared.

11. C – Dragging the extrude direction upward switches the operation to join, while downward switches to cut.

12. B – Red color indicates a cut operation is being performed, providing visual feedback about the operation type.

13. D – The construction lines were set at 45 degrees to create the desired angular relationship in the design.

14. C – Construction lines serve as reference geometry for dimensioning and applying constraints to create robust sketches.

15. B – When multiple bodies exist, you can select which specific object you want to cut or not cut during the operation.

16. D – "Robust" refers to a sketch being fully constrained with all necessary dimensions and relationships properly defined.
