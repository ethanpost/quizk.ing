## [Computer-Aided Design (CAD) Tools](https://www.youtube.com/watch?v=-VG06B7RBgc)

> Import this file into [Mochi](https://mochi.cards/) or give it to your favorite AI tool and have it proxy a quiz and check your answers. When importing make sure you select Markdown as the format, "Multiple cards per .md file", and a ```triple backslash``` as the string delimiter. You can use the link to the raw file in GitHub instead of downloading and importing if you prefer.

### Introduction to CAD Tools
- Class focus on software for Computer-Aided Design (CAD)
- Next week: hands-on lab sessions cutting materials
- Assignment: modeling a possible final project using multiple representation methods
- Following week: designing parametric pressfit construction kit

### Purpose of Different File Management Tools
- Dropbox, OneDrive, Google Drive vs Git
  - Commercial services host content centrally
  - Git offers content ownership with hosting flexibility
  - Git provides powerful branching and merging abilities
  - Git offers better collaborative management tools

### Types of 2D Design Tools
- Hand Drawing
  - Ink on paper, scanning for fabrication
  - Limited design tools but expressive
- Raster/Pixel-Based Tools
  - GIMP: Freely available open-source image manipulation
  - BiMP: Batch operations for resizing, compressing, cropping
  - Photoshop: Commercial alternative
  - ImageMagick: Command-line tool for image conversion and processing
  - MyPaint: Emulates paper, paint, ink with tablet support
- Vector Tools
  - Mods: Tool to trace boundaries and convert images to vectors
  - Inkscape: Free, cross-platform vector editing software
  - Adobe Illustrator: Commercial vector editing tool
  - Browser-based vector tools becoming more common
- Constrained Drawing
  - FreeCAD: Free, cross-platform constrained drawing with parametric capabilities
  - Uses constraints (parallel, perpendicular, tangent, aligned, etc.)
  - Critical for parametric design (propagating measurements throughout design)

### 3D Design Fundamentals
- Design History Management
  - Tracking design process history (like Git versioning)
  - Ability to change past steps and propagate changes
- Collaboration Management 
  - Multiple people working on different subsystems
  - Merging subsystems into complete design
- Representation Methods
  - Boundary representation: Mathematical surface representation (traditional CAD)
  - Function representation: Mathematical interior representation (more powerful)
  - Volume representation: 3D pixels for complex simulations

### 3D Design Tools
- Beginner Tools
  - SketchUp and TinkerCAD: Easy but limited in complexity
- Blender
  - Open-source tool with focus on rendering/animation
  - Great for sculpting and organic forms
  - Less optimized for precision engineering
  - Features Geometry Nodes for powerful construction graphs
- Professional CAD Tools
  - FreeCAD: Open-source, cross-platform CAD tool with workbenches
  - Fusion 360: Commercial tool with integrated workflow, available with educational licenses
  - SolidWorks: Industry standard, good for complex designs, Windows-only
  - xDesign: SolidWorks in the cloud
  - Onshape: Cloud-based collaborative CAD (like Google Docs for CAD)

### 3D Design Techniques
- Snapping and Alignment
  - Grid snapping, vertex snapping, edge alignment
- Coordinates and Properties
  - Numerical control over parameters
- Containers
  - Organizing multiple parts for manipulation
- 2D to 3D Operations
  - Extrusion: Stretching 2D shapes into 3D
  - Revolution: Spinning a 2D shape around an axis
  - Lofting: Connecting multiple 2D profiles
  - Sweeping: Pulling shapes along curves
- Constructive Solid Geometry (CSG)
  - Boolean operations (add, subtract, intersect) on 3D objects
- Symmetry
  - Mirroring parts for efficient design
- Padding and Pocketing
  - Adding material to or removing material from faces
- Filleting and Chamfering
  - Smoothing sharp edges to reduce stress concentration
- Offsetting
  - Inflating or deflating objects for clearance fits
- Hierarchical Design
  - Parts relate to each other, changes propagate
- Constraints in 3D
  - Tangency, concentricity, etc. in 3D space
- Assemblies
  - Creating relationships between separate parts
- Measurements
  - Taking measurements from completed designs
- Folding/Unfolding
  - Creating 3D designs that can be made from folded 2D materials

### Parametric Design
- Using variables and formulas instead of fixed dimensions
- Spreadsheets in CAD to manage variables
- Changes to parameters propagate through entire design
- Essential for designs that adapt to material properties

### Programming and Automation in CAD
- Macros: Running scripts to create complex geometries (gears, honeycombs)
- FreeCAD uses Python for automation
- OpenSCAD and JSCAD: Purely code-based CAD
- Matt Keeter's work with functional representation (f-rep)

### Technical Drawings and Documentation
- Converting 3D designs to standard engineering drawings
- Multiple views, cutouts, dimensions

### File Formats and Interchange
- Problems with interchange between CAD programs
- Recommended formats:
  - Avoid DXF when possible
  - STL: Common for 3D printing (triangulated surfaces)
  - STEP: Good for CAD interchange
  - SVG: Good for 2D interchange

### Rendering and Animation
- Blender: Powerful for rendering and animation
- FreeCAD: Basic rendering capabilities
- Game engines: Unity, Unreal, Godot
- VR/AR sculpting tools

### Simulation
- Blender physics engine: Good for basic simulations
- Chain, fabric, fluid simulations possible

### Video and Documentation
- Audio editing: Audacity (free, cross-platform)
- Video editors: KDEnlive, OpenShot (free), Premiere, Final Cut (commercial)
- Video compression: FFmpeg, HandBrake
- Web video formats: MP4 container with H.264 codec recommended
- Screen recording tools for documentation

### AI in Design
- 2D image generation: Midjourney, DALL-E, Stable Diffusion
- 3D CAD automation developing rapidly
- Current limitations: AI lacks understanding of physics and real geometry

### Terms
- Raster Graphics - Images made up of pixels (tiny squares) in a grid
- Vector Graphics - Images defined by mathematical paths and shapes
- Constraints - Rules applied to geometry to control relationships between elements
- Parametric Design - Design approach using variables and formulas instead of fixed dimensions
- Extrusion - Process of extending a 2D shape into 3D space
- Revolution - Creating a 3D object by rotating a 2D profile around an axis
- Lofting - Creating a 3D shape by connecting multiple 2D profiles
- Sweeping - Creating a 3D shape by moving a 2D profile along a path
- Boolean Operations - Logical operations (union, difference, intersection) applied to 3D shapes
- CSG (Constructive Solid Geometry) - Modeling technique using Boolean operations
- Fillet - Rounding of an interior corner
- Chamfer - Beveling of an edge
- Workbench - Task-specific environment in FreeCAD with specialized tools
- Assembly - Collection of parts with defined relationships
- Macro - Script that automates CAD operations
- STL (STereoLithography) - File format that represents 3D surfaces as triangular meshes
- STEP - Standard for exchange of product model data, good for CAD interchange
- SVG (Scalable Vector Graphics) - XML-based vector image format
- Codec - Technology for compressing and decompressing digital media

///

## According to the lecture, what is the main difference between Git and services like Dropbox or Google Drive?

---

A) Git allows ownership of content and hosting flexibility with powerful branching and merging

B) Git is more expensive than cloud storage services

C) Git automatically syncs files in real-time

D) Git only works with text files, not images or videos

---

Git allows ownership of content and hosting flexibility with powerful branching and merging

///

## Which of these is a pixel-based (raster) image tool mentioned in the lecture?

---

A) Inkscape

B) OpenSCAD

C) GIMP

D) FreeCAD

---

GIMP

///

## What is the key feature of "constrained drawing" that makes it different from regular vector drawing?

---

A) It uses pixels instead of vectors

B) It only works in 3D environments

C) It enforces relationships between elements (like parallel, perpendicular, tangent)

D) It requires an internet connection

---

It enforces relationships between elements (like parallel, perpendicular, tangent)

///

## According to the lecture, which method of 3D representation uses mathematical descriptions of the interior of objects?

---

A) Boundary representation

B) Vector representation

C) Volume representation

D) Function representation

---

Function representation

///

## What is a parametric design?

---

A) A design that uses different color parameters

B) A design where variables and formulas control dimensions rather than fixed values

C) A design created specifically for 3D printing

D) A design that requires special CAD software

---

A design where variables and formulas control dimensions rather than fixed values

///

## Which of these operations turns a 2D shape into a 3D object by rotating it around an axis?

---

A) Sweeping

B) Lofting

C) Revolution

D) Extrusion

---

Revolution

///

## What is Constructive Solid Geometry (CSG)?

---

A) A file format for exchanging 3D models

B) A method of using Boolean operations (add, subtract, intersect) on 3D objects

C) A technique for hand-drawing 3D objects

D) A type of 3D printer technology

---

A method of using Boolean operations (add, subtract, intersect) on 3D objects

///

## According to the lecture, what is a key benefit of using a spreadsheet in CAD software?

---

A) It helps with budgeting materials

B) It helps with project scheduling

C) It allows you to manage variables that can be used throughout your design

D) It generates bill of materials automatically

---

It allows you to manage variables that can be used throughout your design

///

## What file format is recommended for exchanging designs between different CAD programs?

---

A) GIF

B) DXF

C) STEP

D) MP4

---

STEP

///

## Which of these tools is specifically mentioned as being good for sculpting organic shapes?

---

A) AutoCAD

B) FreeCAD

C) Blender

D) SolidWorks

---

Blender

///

## Why is filleting (rounding edges) important in mechanical design?

---

A) It makes objects look more attractive

B) It reduces stress concentration where parts might fail

C) It speeds up the 3D printing process

D) It reduces file sizes

---

It reduces stress concentration where parts might fail

///

## What video format does the lecture recommend for web compatibility?

---

A) Raw uncompressed video

B) GIF for animations

C) H.264 in an MP4 container

D) H.265 in an MP4 container

---

H.264 in an MP4 container

///

## Which type of CAD representation is said to be most suitable for simulating complex phenomena like sand piles or breaking waves?

---

A) Function representation

B) Vector representation

C) Boundary representation

D) Volume representation

---

Volume representation

///

## What is the main limitation of AI in CAD design according to the lecture?

---

A) AI can only work with 2D designs

B) AI lacks understanding of physics and real geometry

C) AI is too slow for practical use

D) AI can't generate 3D models at all

---

AI lacks understanding of physics and real geometry

///

## What does the lecture recommend creating as part of next week's assignment?

---

A) A computer animation

B) A 3D printed vase

C) A parametric pressfit construction kit

D) A full mechanical robot

---

A parametric pressfit construction kit

///

## What is a workbench in FreeCAD?

---

A) A backup system for CAD files

B) A physical table where you place your computer

C) A task-specific environment with specialized tools

D) A type of 3D printing support structure

---

A task-specific environment with specialized tools

///

## When moving from 2D to 3D designs, what operation would you use to connect multiple 2D profiles into a smooth 3D shape?

---

A) Revolution

B) Boolean

C) Lofting

D) Extrusion

---

Lofting

///

## Which software did the instructor mention as being particularly good for batch image processing?

---

A) Photoshop

B) BiMP

C) Blender

D) GIMP

---

BiMP

///

## What is the main advantage of using macros in CAD software?

---

A) They enable collaboration between multiple users

B) They help reduce file sizes

C) They provide better rendering quality

D) They automate complex operations that would require a lot of clicking and dragging

---

They automate complex operations that would require a lot of clicking and dragging
