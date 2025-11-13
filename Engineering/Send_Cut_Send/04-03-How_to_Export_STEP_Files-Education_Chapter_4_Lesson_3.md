## [How to Export STEP Files- Education Chapter 4 Lesson 3](https://www.youtube.com/watch?v=-NS2MgHSY6M)

### Take the quiz [here](https://ethanpost.github.io/quizk.ing) by searching for the title.

## How to Export STEP Files Overview

### Introduction
- Lesson focuses on exporting 3D STEP files from CAD software
- Previous lesson covered exporting 2D vector files (DXF files)
- This lesson covers 3D file export process
- STEP files are the universal file type for 3D solid bodies

### Key Concepts
- STEP file equals 3D file (solid body)
- STEP is the universal file type for 3D solid bodies
- Mesh equals STL file
- STL files are used for 3D printing
- STEP files are used for CNC parts and 3D bodies
- Export option is found in the file menu
- Export allows selection of STEP file or native file types
- Native file types show up in export menu (SolidWorks, Fusion, etc.)

### Export Location and Requirements
- Export option is found underneath the file menu
- Export is the key word to look for
- STEP files only show up at the component level
- If you select a body, mesh (STL) will show up but not STEP file
- Must select component, not just body, to export STEP files

### Export Process in Fusion 360
- Two-body system example used in demonstration
- Bodies can be under one component
- Bodies can interact with each other
- Right-clicking on a body shows "save as mesh" option
- Right-clicking on a body does NOT show export option
- Right-clicking on component shows both "save as mesh" and "export" options
- Export option appears at component level, not body level

### Export Dialog Box
- Export opens a new dialogue box
- File type defaults to Fusion (F3D)
- Dropdown menu shows many different file type options
- STEP file is one of the options in the dropdown
- Can enter a generic name for the exported file
- Click export to complete the process

### Importing STEP Files into SendCutSend
- STEP files can be dragged and dropped into SendCutSend
- When multiple bodies are in one component, they export as one connected body
- Connected bodies are not desired for separate parts
- Bodies need to be separated for individual part export

### Separating Bodies for Export
- First step: deselect one of the bodies
- Hide the body you don't want to export
- Hidden bodies are not included in STEP file export
- Export the visible body as a separate STEP file
- Hide the other body and show the first one
- Export the second body as another separate STEP file
- This creates two different STEP files from one component

### Component Organization
- Having separate components for separate bodies is important
- Different components act like filing cabinets for parts
- Separates parts when doing exports
- Makes sharing with manufacturers easier
- Prevents bodies from being connected in export

### Alternative Export Method
- Export can also be accessed from main file location
- Export option appears in main file menu
- Can see all different file types from this location
- Can export DXFs, STEP files, and other formats
- DXF export will show error for 3D objects

### STEP File Characteristics
- STEP files have no history
- Native file types (F3D) preserve history and timeline
- Sharing native files allows others to see and edit history
- Others can edit extrusions and sketches in native files
- STEP files are solid objects with no history
- STEP files lose parametric design capabilities
- Cannot easily change chamfers or radii in STEP files
- Can sketch and extrude to manipulate STEP files, but not automatically
- Hands are tied on having changes happen automatically in background

### Working with STEP Files
- Can go into Fusion to make changes if you have access to original file
- Make changes in Fusion and reexport STEP file
- If manufacturer has issue with part, they cannot fix it on STEP file side
- Must go into Fusion, create changes, and reexport STEP file
- Exporting STEP file is the "handshake" to manufacturer
- Manufacturer cannot make changes because they don't have history
- STEP file says "this is an acceptable part, please manufacture it"
- STEP files are hard to manipulate once exported

### Next Steps
- Next lesson covers manipulating parts in SendCutSend
- Will cover adding features like bending
- Will cover hardware installation
- Will cover powder coating

### Terms
- STEP File - A 3D file format that represents a solid body, used as the universal file type for 3D solid bodies and CNC parts. STEP files have no history and lose parametric design capabilities.
- STL File - A 3D mesh file format used primarily for 3D printing. STL files are created when exporting at the body level rather than component level.
- Mesh - A 3D file type that represents surface geometry, equal to STL files, used for 3D printing rather than CNC manufacturing.
- Component - A level of organization in CAD software that contains one or more bodies. STEP files can only be exported at the component level, not at the body level.
- Body - A single 3D object within a component. Bodies can be hidden or shown individually, but STEP files cannot be exported directly from bodies.
- Export - The process of saving a CAD file in a different format. The export option is found in the file menu and allows selection of STEP files or native file types.
- Native File Type - A file format specific to a particular CAD software (e.g., F3D for Fusion 360). Native files preserve history and timeline, allowing full editing capabilities.
- F3D - The native file format for Fusion 360 that preserves all design history and parametric capabilities.
- Parametric Design - A design approach where features are defined by parameters that can be modified, allowing automatic updates throughout the model. STEP files lose this capability.
- History - The record of all design steps and modifications in a CAD file. Native files preserve history, while STEP files do not.
- Handshake - The act of exporting a STEP file to a manufacturer, indicating that the part is acceptable and ready for manufacturing. The manufacturer cannot easily modify STEP files.

///

## According to the video, what does STEP file equal?

---

A) 3D file

B) 2D file

C) Mesh file

D) Native file

---

3D file

///

## What is the universal file type for 3D solid bodies?

---

A) STL

B) STEP

C) OBJ

D) F3D

---

STEP

///

## According to the video, what does mesh equal?

---

A) STEP file

B) STL file

C) DXF file

D) Native file

---

STL file

///

## What are STL files used for according to the video?

---

A) CNC machining

B) 3D printing

C) Water jetting

D) Laser cutting

---

3D printing

///

## Where is the export option found?

---

A) Under the tools menu

B) Under the view menu

C) Underneath the export option

D) Under the file menu

---

Under the file menu

///

## At what level do STEP files show up for export?

---

A) Body level

B) Component level

C) Sketch level

D) Assembly level

---

Component level

///

## What happens if you select a body instead of a component for export?

---

A) STEP file option appears

B) Both STEP and mesh options appear

C) Mesh shows up but not STEP file

D) No export options appear

---

Mesh shows up but not STEP file

///

## When right-clicking on a body in Fusion 360, what option appears?

---

A) Export

B) Save as STEP

C) Save as mesh

D) Save as DXF

---

Save as mesh

///

## When right-clicking on a component in Fusion 360, what options appear?

---

A) Only save as mesh

B) Both save as mesh and export

C) Only export

D) Neither option appears

---

Both save as mesh and export

///

## What does the export dialogue box default to?

---

A) STEP file

B) DXF file

C) Fusion (F3D)

D) STL file

---

Fusion (F3D)

///

## According to the video, what happens when multiple bodies in one component are exported as a STEP file?

---

A) They export as separate files automatically

B) They export as one connected body

C) Only the first body exports

D) An error occurs

---

They export as one connected body

///

## How do you separate bodies when exporting STEP files?

---

A) Delete one of the bodies

B) Move bodies to different layers

C) Deselect and hide the body you don't want to export

D) Change the file format

---

Deselect and hide the body you don't want to export

///

## What happens to hidden bodies when exporting a STEP file?

---

A) They are included in the export

B) They are not included in the STEP file export

C) They cause an error

D) They export as separate files

---

They are not included in the STEP file export

///

## According to the video, why is it important to have separate components for separate bodies?

---

A) It makes files smaller

B) It separates parts when doing exports and sharing with manufacturers

C) It speeds up the export process

D) It prevents errors

---

It separates parts when doing exports and sharing with manufacturers

///

## What happens if you try to export a 3D object as a DXF file?

---

A) It works perfectly

B) It will have an error because it is a 3D object

C) It automatically converts to 2D

D) It creates a mesh file instead

---

It will have an error because it is a 3D object

///

## According to the video, do STEP files have history?

---

A) Yes, they preserve all history

B) No, STEP files have no history

C) They have partial history

D) It depends on the software

---

No, STEP files have no history

///

## What do native file types preserve that STEP files do not?

---

A) File size

B) Colors and textures

C) History and timeline

D) File format

---

History and timeline

///

## What happens when you share a native file (like F3D) with someone who has the same software?

---

A) They can only view it

B) They can see all history and timeline and edit extrusions and sketches

C) They cannot open it

D) It converts to STEP automatically

---

They can see all history and timeline and edit extrusions and sketches

///

## What do STEP files lose compared to native files?

---

A) File size

B) Colors

C) Parametric design capabilities

D) 3D geometry

---

Parametric design capabilities

///

## According to the video, if you want to change a chamfer or radius in a STEP file, what happens?

---

A) You can easily change it

B) You have lost that capability

C) It changes automatically

D) You must use a different software

---

You have lost that capability

///

## What can you do to manipulate a STEP file if needed?

---

A) Nothing, it cannot be changed

B) All changes happen automatically

C) Sketch and extrude to manipulate it, but changes won't happen automatically

D) Import it back as a native file

---

Sketch and extrude to manipulate it, but changes won't happen automatically

///

## If a manufacturer has an issue with a part sent as a STEP file, what must happen?

---

A) The manufacturer can fix it directly

B) Nothing can be done

C) You must go into Fusion, create changes, and reexport the STEP file

D) The file automatically updates

---

You must go into Fusion, create changes, and reexport the STEP file

///

## According to the video, what is exporting a STEP file to a manufacturer called?

---

A) The delivery

B) The transfer

C) The handshake

D) The submission

---

The handshake

///

## What does the "handshake" of exporting a STEP file indicate?

---

A) The part needs revision

B) The part is incomplete

C) This is an acceptable part and I need you to manufacture it

D) The manufacturer should modify it

---

This is an acceptable part and I need you to manufacture it

///

## Why can't manufacturers easily make changes to STEP files?

---

A) They don't have the software

B) They don't have the history

C) The files are too large

D) The files are corrupted

---

They don't have the history

///

## According to the video, what will the next lesson cover?

---

A) How to create 3D models

B) How to import files

C) How to manipulate parts in SendCutSend, including adding features like bending, hardware installation, and powder coating

D) How to use different CAD software

---

How to manipulate parts in SendCutSend, including adding features like bending, hardware installation, and powder coating

///

## What is a component in CAD software?

---

A) A single 3D object

B) A file format

C) A level of organization that contains one or more bodies

D) A type of export

---

A level of organization that contains one or more bodies

///

## What is a body in CAD software?

---

A) A component

B) A file format

C) A single 3D object within a component

D) An export option

---

A single 3D object within a component

///

## What is parametric design?

---

A) A design approach where features are defined by parameters that can be modified, allowing automatic updates

B) A file format

C) A type of 3D printing

D) A manufacturing process

---

A design approach where features are defined by parameters that can be modified, allowing automatic updates

///

## Master Answer Key

1. **A) 3D file** - STEP file equals 3D file, representing a solid body in CAD software.

2. **B) STEP** - STEP is the universal file type for 3D solid bodies, used across different CAD software and manufacturing services.

3. **B) STL file** - Mesh equals STL file, which is used for 3D printing rather than CNC manufacturing.

4. **B) 3D printing** - STL files are mesh files primarily used for additive manufacturing like 3D printing.

5. **D) Under the file menu** - The export option is found underneath the file menu in CAD software.

6. **B) Component level** - STEP files only show up at the component level, not at the body level for export.

7. **C) Mesh shows up but not STEP file** - When selecting a body instead of a component, mesh (STL) options appear but STEP file options do not.

8. **C) Save as mesh** - Right-clicking on a body shows "save as mesh" option, but not the export option for STEP files.

9. **B) Both save as mesh and export** - Right-clicking on a component shows both "save as mesh" and "export" options, allowing STEP file export.

10. **C) Fusion (F3D)** - The export dialogue box defaults to Fusion's native file format (F3D) before you select STEP file.

11. **B) They export as one connected body** - When multiple bodies are in one component, they export as a single connected body, which is usually not desired.

12. **C) Deselect and hide the body you don't want to export** - To separate bodies, you deselect and hide the body you don't want, then export the visible body as a separate STEP file.

13. **B) They are not included in the STEP file export** - Hidden bodies are excluded from STEP file exports, allowing you to export individual parts separately.

14. **B) It separates parts when doing exports and sharing with manufacturers** - Having separate components acts like filing cabinets, making it easier to export and share individual parts with manufacturers.

15. **B) It will have an error because it is a 3D object** - DXF files are for 2D objects, so exporting a 3D object as DXF will result in an error.

16. **B) No, STEP files have no history** - STEP files are solid objects with no design history, unlike native file types that preserve the timeline.

17. **C) History and timeline** - Native file types preserve the complete history and timeline of design changes, allowing full editing capabilities.

18. **B) They can see all history and timeline and edit extrusions and sketches** - Sharing native files with someone using the same software allows them to see and edit all design history, including extrusions and sketches.

19. **C) Parametric design capabilities** - STEP files lose parametric design capabilities, meaning you cannot easily modify parameters and have changes update automatically throughout the model.

20. **B) You have lost that capability** - Once exported as a STEP file, you lose the ability to easily change features like chamfers or radii because the parametric history is gone.

21. **C) Sketch and extrude to manipulate it, but changes won't happen automatically** - You can manually sketch and extrude to modify STEP files, but changes won't automatically propagate like they would in parametric design.

22. **C) You must go into Fusion, create changes, and reexport the STEP file** - Manufacturers cannot fix issues in STEP files directly, so you must modify the original file in Fusion and reexport.

23. **C) The handshake** - Exporting a STEP file to a manufacturer is called "the handshake," indicating the part is ready for manufacturing.

24. **C) This is an acceptable part and I need you to manufacture it** - The handshake communicates that the STEP file represents an acceptable, finalized part ready for manufacturing.

25. **B) They don't have the history** - Manufacturers cannot easily modify STEP files because they lack the design history and parametric information needed to make changes.

26. **C) How to manipulate parts in SendCutSend, including adding features like bending, hardware installation, and powder coating** - The next lesson covers post-import manipulation of parts in SendCutSend, including various manufacturing features.

27. **C) A level of organization that contains one or more bodies** - A component is an organizational structure in CAD software that can contain multiple bodies, and STEP files must be exported at this level.

28. **C) A single 3D object within a component** - A body is an individual 3D object that exists within a component, and multiple bodies can be grouped under one component.

29. **A) A design approach where features are defined by parameters that can be modified, allowing automatic updates** - Parametric design uses parameters to define features, enabling automatic updates when parameters change, but this capability is lost in STEP files.

