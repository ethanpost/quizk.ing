## [3D Scanning and Printing Overview](https://www.youtube.com/watch?v=IMVRRhiDfjk)

> Import this file into [Mochi](https://mochi.cards/) or give it to your favorite AI tool and have it proxy a quiz and check your answers. When importing make sure you select Markdown as the format, "Multiple cards per .md file", and a ```triple backslash``` as the string delimiter. You can use the link to the raw file in GitHub instead of downloading and importing if you prefer.

### Introduction and Faculty
- Week focuses on 3D scanning and printing
- Goal: Learn strengths and weaknesses of 3D printing
- Faculty includes Yogen, Ohad, and Adrien Bowyer
- Adrien Bowyer democratized 3D printing and led RepRap project
- RepRap project aimed to create self-replicating 3D printers

### 3D Scanning

#### Historical Methods
- Coordinate Measuring Machine (CMM) - oldest digital scanning method
- Uses Cartesian robot with air bearings and touch probe
- Touch probe uses three rods on six balls with electrical contacts
- Principle: breaking contact is more accurate than making contact
- Touch probe can be 3D printed

#### Scanning Process Overview
- Scanning produces point clouds (XYZ coordinates)
- Point clouds must be converted to usable formats
- Process involves triangulation (turning points into triangles)
- Triangles preferred over quadrilaterals because they're always flat
- Probe offset requires Minkowski sum/difference correction

#### Stereo Vision and Point Correspondence
- Most scanning methods use binocular stereo vision
- Human vision uses angle between eyes for triangulation
- Scanning can use single camera with turntable instead of two cameras
- Point correspondence problem: matching same point in different images
- Four stages: gathering images (easy), point correspondence (hard), creating point cloud (easy), triangulation (hard)

#### Structured Light Scanning
- Simplifies point correspondence by structuring light
- Laser produces bright dot that computer can easily detect
- Knowing laser and camera positions allows 3D coordinate calculation
- Can use sharp beam (laser) or sheet of light (barcode scanner style)

#### Triangulation Challenges
- Ambiguity in reconstruction from point clouds
- Insufficient points can lead to incorrect surface reconstruction
- More points reduce but don't eliminate ambiguity
- Poisson surface reconstruction requires points and normal vectors
- Normal vectors calculated using principal component analysis

#### Practical Scanners
- FabScan Pi: Raspberry Pi-based scanner with turntable
- Creality Ferret Pro 3D scanner: uses structured infrared light
- Two cameras detect pattern and object color
- Cost around $300
- Produces triangulated 3D representation for CAD systems

#### Emerging Technologies
- Time-of-flight measurement for augmented reality
- Measures picosecond timing (light travels foot in nanosecond)
- Cameras with pixels measuring picosecond timing becoming accessible
- Can project 8x8 pattern of timed beams
- Typical range: 200mm to 4 meters
- Latest iPhones include picosecond timing imagers

### 3D Printing

#### History of Making Things
- Four fundamental ways humans shape solid objects since prehistory
- Cutting/subtractive: remove material from block
- Deforming: shape deformable material (molten glass)
- Adding: add material to build shape (clay coils)
- Modern: computer-controlled versions of these methods

#### History of 3D Printing
- William Herschel's 3D printer (1930s): cylindrical buildings with cement
- David Jones (1974): first modern 3D printer concept (scientific joke)
- Win Kelly Swainson: simultaneous patent for photoresist polymerization
- Two-photon 3D printing based on this early concept
- Charles Hull: invented stereolithography (SLA), first commercial system
- Scott Crump: invented FDM (Fused Deposition Modeling) using glue gun concept
- RepRap project: self-replicating 3D printers

#### Why 3D Print?

##### Advantages
- Small forces (5N) vs large forces (500N) in milling
- Less rigid machinery required
- Two-dimensional problem vs five-dimensional problem for complex shapes
- Five-axis CNC mills needed for complex subtractive shapes
- 3D printing works in layers (2D slices)
- Free space above print plane allows unrestricted movement
- Can make shapes impossible with milling (e.g., whistle with internal rattle)
- Complexity is almost free (time similar for simple and complex shapes)
- Near-net-shape process with less waste than milling
- Can make functional objects in single shot (mechanisms)

##### Disadvantages
- Slow process
- Can fail: birds nesting (material doesn't stick)
- Objects can stick too well and detach from bed
- SLA printing can distort without proper support

#### FFF (Fused Filament Fabrication) 3D Printing

##### Technology Overview
- Also called FDM (trademarked term)
- Extrudes molten plastic through heated nozzle
- Builds object layer by layer
- Filament spool feeds through heated nozzle
- Build platform descends or head ascends
- Essentially computer-controlled hot glue gun
- Slow process (quality decreases with speed)

##### Emissions and Safety
- Ultrafine particle emissions vary by material
- PLA (polylactic acid): low emissions, benign, smells like caramel when hot
- Other materials require enclosed machines with activated carbon filters
- Volatile organic compounds (VOCs) can be harmful
- Certification schemes exist for emission compliance

##### Materials
- Many materials available with different mechanical properties
- Flexible plastics can be printed
- PLA: hygroscopic (absorbs water), plant-based, low glass transition temperature
- PLA should be stored in sealed container with silica gel
- PETG: higher temperature resistance, better UV resistance
- PLA often contains titanium dioxide for UV resistance

##### Design Rules - Overhangs and Supports
- Overhangs require support material
- Support material printed to be easily removable
- Support material can be friable (crumbles easily)
- Brachiating tree-like structures use less support material
- Overhangs up to about 40° can print without support
- Bridging: can print across gaps with supports at ends
- Molten polymer is non-Newtonian viscous fluid
- Bridge length limited by sagging

##### Belt Printers
- Conveyor belt-based printers
- Print head moves at angle (e.g., 40° to horizontal)
- Advantages: continuous printing, mass production capability
- Can print without support material using 45° overhang rule
- Can extend belt for prints of any length (e.g., 6m beams)

##### Clearances and Mechanisms
- Different clearances between parts allow movement
- Can make mechanisms in single print
- Example: scissor screw jack printed in one shot
- Parts can be free to rotate or constrained

##### Material Properties
- Anisotropy: different strength in different directions
- Horizontal layers stronger than vertical bonds between layers
- Dimensional accuracy: holes often undersized
- Exterior dimensions usually accurate
- Surface finish: visible layer steps on curved surfaces

##### Infill
- Objects rarely printed completely solid
- Honeycomb infill almost as strong, faster, uses less material
- Infill percentages: 100% (rare), 50%, 15%, 0%
- Zero infill relies on bridging for top surface
- Various infill patterns available
- Free flow infill: air fully connected throughout
- Can fill with resin after printing for strength (hot/cold riser technique)

##### Bed Leveling
- Beds are never perfectly level
- Machines detect when nozzle touches bed
- Create map of bed surface (typically 0.2mm variation)
- Machine adjusts head height during printing
- Ensures first layer adhesion

##### 3D Printer as Coordinate Measuring Machine
- Can use printer to digitize objects
- Hold ball bearing under nozzle, extrude plastic
- Use touch detection to map object surface
- Adequate for some purposes

##### Additional Material Types
- Skirt: rim around object to clear nozzle throat
- Brim: increases contact area with build plate
- Raft: material layer under print for leveling and adhesion

##### Embedded Objects
- Can pause print and insert objects
- Example: magnets embedded in cavities
- Print continues over embedded objects

##### Advanced Infill Techniques
- Random fine cylinders subtracted from object
- Creates fiberglass-like reinforcement
- Can use finite element analysis to optimize reinforcement placement
- Internal structure invisible but affects mechanical properties

##### Multi-Material Printing
- Multiple materials allow colors
- Can combine hard and flexible plastics
- Electrically conducting filament available (much higher resistivity than copper)
- Soluble support material (PVA - polyvinyl alcohol, water soluble)
- Other soluble materials dissolve in sodium hydroxide

##### Slicing and G-Code
- STL file represents object
- Slicing: cutting object into layers
- Generates G-code file to control printer
- G-code: standard for numerically controlled machines
- G1: move command with X, Y, Z coordinates
- Feed rate in millimeters per minute
- Extrusion treated as another dimension
- Can edit G-code manually (risky)

##### Fitting Parts Together - Minkowski Sum
- Parts often need to fit together
- Simple subtraction doesn't work (holes undersized)
- Minkowski sum: expands shape slightly
- Mathematical definition: union of all positions of one shape visiting all points of another
- FreeCAD can compute Minkowski sums
- Keep added shape simple (cylinder better than sphere)

##### Post-Processing
- Can paint prints
- Solvent vapor smoothing: dissolves surface slightly, surface tension smooths it
- Dangerous: toxic fumes, heating flammable materials
- Electroplating: cover with conducting paint, then electroplate
- Fixings: screws (can self-tap), rivets, threaded inserts (heated insertion)
- Embedded nuts: leave cavities, drop nuts in during printing

#### Vat Polymerization (SLA/MSLA/DLP)

##### Technology Overview
- Uses photopolymers (liquid monomers that polymerize with UV light)
- Thermoset polymers: require chemical reaction to harden
- Different from thermoplastics (can be reheated and reused)

##### Types of Vat Polymerization
- SLA (Stereolithography): laser-based, vector printing, most precise but slower
- DLP (Digital Light Processing): projector-based, entire layer at once, faster
- MSLA (Masked Stereolithography): LCD screen at bottom, pixel-based, most common

##### Safety and Post-Processing
- Resin is toxic before hardening
- Need gloves, mask, UV glasses
- Parts deformable before full cure
- Remove supports, wash in IPA (isopropyl alcohol)
- Ultrasonic wash preferred
- Some materials need water wash after IPA
- UV cure chamber: very toxic, needs ventilation
- Parts angled 30-45° to allow drainage and prevent sticking

##### Advantages and Disadvantages
- Finer details and higher accuracy than FFF
- Monomaterial (no multimaterial like FFF)
- Post-processing takes significant time
- Non-recyclable parts

#### Multi-Jet Printing
- Multiple heads print like inkjet
- Drops material, roller flattens to create voxels
- UV lamps cure material as it falls
- Can use multimaterial and multicolor
- Can create objects with varying material properties (50% rigid, 50% flexible)
- Used for impact absorption
- Medical applications: mimic organ behavior for surgical practice
- Example: heart defect surgery reduced from 60+ hours to 15 hours

#### File Formats
- STL: traditional format
- 3MF: most recommended format
- 3MF: compressed, supports texture and multimaterial
- Can embed G-code within 3MF file

#### Assignment Requirements
- Group assignment: test printer capabilities
- Know your printer's limitations (wall thickness, behavior)
- Main assignment: Design 3D printed object that cannot be made subtractively
- Consider advantages: enclosed parts, moving parts, complex geometries
- Scan anything (extra credit: print scanned object)
- Photogrammetry apps available for cell phones
- Global open time for challenges

### Terms
- Additive Manufacturing - Manufacturing process that builds objects by adding material layer by layer, also called 3D printing.
- Anisotropy - Property where material has different mechanical properties in different directions, common in 3D prints due to layer-by-layer construction.
- Bed Leveling - Process where 3D printer maps the build platform surface to compensate for slight variations in flatness.
- Brim - Additional material printed around base of object to increase contact area with build plate and prevent detachment.
- Bridging - Technique of printing across gaps without support material underneath by quickly dragging molten plastic between supports.
- Coordinate Measuring Machine (CMM) - Early digital scanning device using Cartesian robot with touch probe to measure object dimensions.
- DLP (Digital Light Processing) - Vat polymerization 3D printing using projector to expose entire layer at once, faster than SLA.
- FDM (Fused Deposition Modeling) - Trademarked term for material extrusion 3D printing, also called FFF.
- FFF (Fused Filament Fabrication) - Open-source term for material extrusion 3D printing using heated nozzle to extrude plastic filament.
- Free Flow Infill - Infill pattern where air inside object is fully connected, allowing liquid to flow throughout.
- G-Code - Standard programming language for controlling numerically controlled machines including 3D printers, CNC mills, and lathes.
- Infill - Internal structure pattern inside 3D printed object, typically honeycomb, used to save material and time while maintaining strength.
- Minkowski Sum - Mathematical operation to expand shape by adding another shape to it, used to create proper clearances for fitting 3D printed parts together.
- MSLA (Masked Stereolithography) - Vat polymerization using LCD screen at bottom of vat to mask UV light, most common resin printing method.
- Normal Vector - Line pointing perpendicular to surface, required for some surface reconstruction algorithms.
- Overhang - Part of 3D print that extends beyond previously printed material, typically requires support if angle too shallow.
- Photogrammetry - Technique of creating 3D models from multiple photographs, increasingly available on cell phones.
- Photopolymer - Liquid monomer material that polymerizes (hardens) when exposed to UV light, used in vat polymerization printing.
- Point Cloud - Collection of XYZ coordinates representing points on surface of scanned object, must be processed into usable format.
- Point Correspondence - Problem of matching same point in different images when reconstructing 3D object from multiple views.
- Poisson Surface Reconstruction - Method of converting point cloud into triangulated surface mesh using points and normal vectors.
- Principal Component Analysis - Statistical method used to calculate normal vectors from groups of nearby points in point cloud.
- Raft - Layer of material printed underneath object before main print starts, helps with adhesion and leveling.
- RepRap - Project to create self-replicating 3D printers, led by Adrien Bowyer.
- Skirt - Rim of material printed around object before main print to clear nozzle and ensure proper filament flow.
- SLA (Stereolithography) - Vat polymerization 3D printing using laser to trace each layer, most precise but slower method.
- Slicing - Process of converting 3D model (STL file) into layers and generating G-code instructions for 3D printer.
- STL File - File format representing 3D object as triangulated surface mesh, traditional format for 3D printing.
- Structured Light - Scanning technique using projected light pattern (laser dot, sheet, or grid) to simplify point correspondence problem.
- Support Material - Extra material printed to support overhanging parts during printing, designed to be easily removable.
- Thermoplastic - Plastic material that softens when heated and can be reshaped, used in FFF printing, recyclable.
- Thermoset - Polymer material that requires chemical reaction to harden, cannot be reheated and reshaped, used in vat polymerization.
- Time-of-Flight - Scanning method measuring time for light to travel to object and back, enables picosecond timing measurements.
- Triangulation - Process of converting point cloud into mesh of triangles representing object surface, or geometric method using angles to determine distance.
- Vat Polymerization - Category of 3D printing where liquid photopolymer is selectively hardened by UV light in vat of resin.
- Voxel - Three-dimensional pixel, unit of volume in 3D printing, particularly relevant for pixel-based methods like DLP and MSLA.

///

## According to the video, what was the primary goal of the RepRap project?

---

A) To create self-replicating 3D printers

B) To develop new printing materials

C) To create the fastest 3D printer

D) To make 3D printing accessible to everyone

---

A) To create self-replicating 3D printers

///

## What is the main reason triangles are preferred over quadrilaterals when converting point clouds to surfaces?

---

A) Triangles use less memory

B) Triangles print faster

C) Triangles are always guaranteed to be flat

D) Triangles are easier to calculate

---

C) Triangles are always guaranteed to be flat

///

## According to the lecture, what is the typical force range for 3D printing compared to CNC milling?

---

A) 3D printing uses similar forces

B) 3D printing uses larger forces

C) 3D printing uses 100 times smaller forces (5N vs 500N)

D) Forces are not relevant to the comparison

---

C) 3D printing uses 100 times smaller forces (5N vs 500N)

///

## What problem does structured light solve in 3D scanning?

---

A) The accuracy of measurements

B) The speed of scanning

C) The point correspondence problem

D) The cost of scanning equipment

---

C) The point correspondence problem

///

## Why can a CNC mill not make a whistle with an internal rattle, but a 3D printer can?

---

A) 3D printers can access internal cavities during layer-by-layer construction

B) 3D printers are faster

C) 3D printers are more accurate

D) 3D printers use different materials

---

A) 3D printers can access internal cavities during layer-by-layer construction

///

## What is the approximate maximum overhang angle that can be printed without support material in FFF printing?

---

A) 40 degrees

B) 20 degrees

C) 90 degrees

D) 60 degrees

---

A) 40 degrees

///

## According to the lecture, what is PLA short for?

---

A) Polymeric layered additive

B) Polynactic acid

C) Printed layered assembly

D) Polylactic acid

---

D) Polylactic acid

///

## What is the main advantage of belt-based 3D printers mentioned in the lecture?

---

A) They use less material

B) They are more accurate

C) They can print continuously for mass production

D) They are cheaper

---

C) They can print continuously for mass production

///

## What is the purpose of bed leveling in 3D printing?

---

A) To adjust print speed

B) To clean the bed surface

C) To map bed surface variations so printer can compensate during printing

D) To make the bed perfectly flat

---

C) To map bed surface variations so printer can compensate during printing

///

## According to the lecture, why is the Minkowski sum used when fitting 3D printed parts together?

---

A) To expand shapes slightly to account for undersized holes in prints

B) To make parts fit more tightly

C) To speed up printing

D) To reduce material usage

---

A) To expand shapes slightly to account for undersized holes in prints

///

## What is the difference between SLA, DLP, and MSLA printing technologies?

---

A) SLA uses laser (vector), DLP uses projector (layer at once), MSLA uses LCD screen (pixel-based)

B) They use different materials

C) They differ only in speed

D) They are different names for the same technology

---

A) SLA uses laser (vector), DLP uses projector (layer at once), MSLA uses LCD screen (pixel-based)

///

## What is the main safety concern mentioned for vat polymerization (resin) printing?

---

A) Toxic fumes and uncured resin requiring gloves, mask, and ventilation

B) Electrical hazards

C) High temperatures

D) Moving parts

---

A) Toxic fumes and uncured resin requiring gloves, mask, and ventilation

///

## According to the lecture, what is G-code?

---

A) A file format for 3D models

B) Standard programming language for controlling numerically controlled machines

C) A scanning technique

D) A type of 3D printer

---

B) Standard programming language for controlling numerically controlled machines

///

## What is the primary reason infill is used instead of printing objects completely solid?

---

A) Infill is almost as strong, faster to print, and uses less material

B) Infill looks better

C) Solid prints are weaker

D) Solid prints cannot be made

---

A) Infill is almost as strong, faster to print, and uses less material

///

## According to the lecture, what happens during the slicing process?

---

A) Object is scanned

B) 3D model (STL file) is converted into layers and G-code instructions

C) Print is post-processed

D) Support material is added

---

B) 3D model (STL file) is converted into layers and G-code instructions

///

## What is the main advantage mentioned for multi-jet printing?

---

A) It is the fastest method

B) It can create objects with varying material properties (multimaterial and multicolor)

C) It requires no post-processing

D) It is the cheapest method

---

B) It can create objects with varying material properties (multimaterial and multicolor)

///

## According to the lecture, what is the recommended file format for 3D printing?

---

A) OBJ

B) PLY

C) 3MF

D) STL

---

C) 3MF

///

## What is anisotropy in 3D printing?

---

A) Different colors in different directions

B) Different mechanical properties in different directions due to layer construction

C) Different print speeds

D) Different material types

---

B) Different mechanical properties in different directions due to layer construction

///

## According to the lecture, what is the four-stage process of 3D scanning?

---

A) Gather images (easy), point correspondence (hard), create point cloud (easy), triangulation (hard)

B) Design, slice, print, post-process

C) Scan, process, print, finish

D) Measure, calculate, model, verify

---

A) Gather images (easy), point correspondence (hard), create point cloud (easy), triangulation (hard)

///

## What is bridging in 3D printing?

---

A) Technique of printing across gaps without support by quickly dragging molten plastic between supports

B) Post-processing technique

C) Connecting multiple printers

D) Adding support material

---

A) Technique of printing across gaps without support by quickly dragging molten plastic between supports

///

## According to the lecture, what is the main reason 3D printing is considered a two-dimensional problem while CNC milling for complex shapes is five-dimensional?

---

A) 3D printing builds in flat layers (2D slices) while complex milling requires five-axis movement

B) 3D printing is slower

C) 3D printers are simpler machines

D) 3D printing uses less material

---

A) 3D printing builds in flat layers (2D slices) while complex milling requires five-axis movement

///

## What is the difference between a skirt, brim, and raft?

---

A) Skirt clears nozzle, brim increases bed contact area, raft provides leveling layer under print

B) They are different printer types

C) They are different materials

D) They are different infill patterns

---

A) Skirt clears nozzle, brim increases bed contact area, raft provides leveling layer under print

///

## According to the lecture, what is the main assignment requirement for this week?

---

A) Compare different printing technologies

B) Print a test object

C) Design a 3D printed object that cannot be made subtractively

D) Scan an object

---

C) Design a 3D printed object that cannot be made subtractively

///

## What is a point cloud?

---

A) Collection of XYZ coordinates representing points on surface of scanned object

B) A file format

C) A type of 3D printer

D) A scanning technique

---

A) Collection of XYZ coordinates representing points on surface of scanned object

///

## According to the lecture, what is the main reason PLA should be stored in a sealed container with silica gel?

---

A) It is fragile

B) It degrades in light

C) It is expensive

D) It is hygroscopic and absorbs water from atmosphere

---

D) It is hygroscopic and absorbs water from atmosphere

///

## What is the difference between thermoplastic and thermoset polymers in 3D printing?

---

A) Thermoplastics can be reheated and reshaped, thermosets require chemical reaction to harden and cannot be reheated

B) Thermosets are only used in FFF printing

C) They are the same thing

D) Thermoplastics are only used in SLA printing

---

A) Thermoplastics can be reheated and reshaped, thermosets require chemical reaction to harden and cannot be reheated

///

## According to the lecture, what is Poisson surface reconstruction?

---

A) A scanning method

B) A printing technique

C) Method of converting point cloud into triangulated surface using points and normal vectors

D) A file format

---

C) Method of converting point cloud into triangulated surface using points and normal vectors

///

## What is the main advantage of time-of-flight scanning mentioned in the lecture?

---

A) It is cheaper

B) It requires no equipment

C) It measures picosecond timing to determine distance, becoming accessible in devices like iPhones

D) It is faster

---

C) It measures picosecond timing to determine distance, becoming accessible in devices like iPhones

///

## According to the lecture, what is the typical cost range mentioned for a Creality Ferret Pro 3D scanner?

---

A) Around $5000

B) Around $1000

C) Around $300

D) Around $100

---

C) Around $300

///

## What is the main reason complexity is "almost free" in 3D printing compared to milling?

---

A) Complex shapes take similar time to print as simple shapes

B) 3D printers are faster

C) 3D printers are cheaper

D) 3D printing uses less material

---

A) Complex shapes take similar time to print as simple shapes

///

## According to the lecture, what is the purpose of free flow infill?

---

A) To speed up printing

B) To allow liquid to flow throughout connected air spaces, enabling resin filling

C) To improve surface finish

D) To make prints lighter

---

B) To allow liquid to flow throughout connected air spaces, enabling resin filling

///

## What is the main difference between FDM and FFF?

---

A) FDM is trademarked term, FFF is open-source alternative name for same technology

B) FDM is faster

C) FFF is more accurate

D) They use different materials

---

A) FDM is trademarked term, FFF is open-source alternative name for same technology

///

## According to the lecture, what is the main reason holes in 3D printed objects often come out undersized?

---

A) Design software errors

B) Printer calibration issues

C) Material shrinkage

D) Layer adhesion problems

---

C) Material shrinkage

///

## What is the main advantage of using soluble support material in multi-material printing?

---

A) It prints faster

B) Support material dissolves away cleanly in water or other solvents

C) It is stronger

D) It is cheaper

---

B) Support material dissolves away cleanly in water or other solvents

///

## According to the lecture, what historical figure created what is considered the first 3D printer in the 1930s?

---

A) Adrien Bowyer

B) William Herschel

C) Charles Hull

D) Scott Crump

---

B) William Herschel

///

## What is the main reason a touch probe breaks contact rather than makes contact for detection?

---

A) It is easier to build

B) It is faster

C) Breaking contact produces more accurate and repeatable results

D) It uses less power

---

C) Breaking contact produces more accurate and repeatable results

///

## According to the lecture, what is the typical bed level variation that bed leveling compensates for?

---

A) About 0.2 millimeters

B) About 2 millimeters

C) About 20 millimeters

D) About 0.02 millimeters

---

A) About 0.2 millimeters

///

## What is the main medical application example given for multi-jet printing?

---

A) Mimicking organ behavior for surgical practice, reducing surgery time significantly

B) Printing medications

C) Creating medical instruments

D) Creating prosthetics

---

A) Mimicking organ behavior for surgical practice, reducing surgery time significantly

///

## According to the lecture, what is the main reason 3D printing creates less waste than CNC milling?

---

A) 3D printing is a near-net-shape process with minimal waste compared to cutting material away

B) 3D printers are more efficient

C) 3D printing uses less material

D) 3D printing recycles material

---

A) 3D printing is a near-net-shape process with minimal waste compared to cutting material away

///

## What is the main reason parts are angled 30-45 degrees in vat polymerization printing?

---

A) To allow liquid resin to drain and prevent parts from sticking to tray

B) To improve print quality

C) To speed up printing

D) To reduce material usage

---

A) To allow liquid resin to drain and prevent parts from sticking to tray

///

## According to the lecture, what is photogrammetry?

---

A) A type of 3D printer

B) A file format

C) Technique of creating 3D models from multiple photographs, available on cell phones

D) A scanning hardware device

---

C) Technique of creating 3D models from multiple photographs, available on cell phones

///

## What is the main reason a sphere is more computationally difficult than a cylinder for Minkowski sum operations?

---

A) Spheres are harder to print

B) Spheres use more material

C) Spheres require many more triangles to represent than cylinders

D) Spheres are larger

---

C) Spheres require many more triangles to represent than cylinders

///

## According to the lecture, what is the main characteristic of PLA that makes it relatively safe for printing?

---

A) Low particulate emissions, smells like caramel when hot, plant-based polymer

B) It is very strong

C) It is flexible

D) It is transparent

---

A) Low particulate emissions, smells like caramel when hot, plant-based polymer

///

## What is the main reason bridging works in 3D printing?

---

A) Molten polymer is non-Newtonian viscous fluid that stays up when dragged quickly between supports

B) Material is very strong

C) Gravity doesn't affect plastic

D) Support material is always used

---

A) Molten polymer is non-Newtonian viscous fluid that stays up when dragged quickly between supports

///

## According to the lecture, what is the main advantage of DLP over SLA printing?

---

A) DLP is more accurate

B) DLP projects entire layer at once, making it faster than vector-based SLA

C) DLP uses less material

D) DLP is cheaper

---

B) DLP projects entire layer at once, making it faster than vector-based SLA

///

## What is the main reason normal vectors are needed for Poisson surface reconstruction?

---

A) Algorithm requires both point locations and surface orientation information

B) To calculate print time

C) To determine print orientation

D) To determine material usage

---

A) Algorithm requires both point locations and surface orientation information

///

## According to the lecture, what is the main reason 3D printing can make functional mechanisms in a single shot?

---

A) Can print parts with proper clearances that move relative to each other without assembly

B) 3D printers are faster

C) 3D printers are more accurate

D) 3D printing uses special materials

---

A) Can print parts with proper clearances that move relative to each other without assembly

///

## What is the main reason principal component analysis is used in scanning?

---

A) To calculate normal vectors from groups of nearby points in point cloud

B) To speed up scanning

C) To reduce file size

D) To improve print quality

---

A) To calculate normal vectors from groups of nearby points in point cloud

///

## According to the lecture, what is the main difference between stereo vision scanning and structured light scanning?

---

A) Structured light uses two cameras

B) Structured light is slower

C) They are the same thing

D) Structured light projects pattern to simplify point correspondence problem

---

D) Structured light projects pattern to simplify point correspondence problem

///

## What is the main reason a 3D printer can be used as a coordinate measuring machine?

---

A) Printer can detect when nozzle touches something, allowing it to digitize objects

B) It can scan while printing

C) It has built-in sensors

D) It can print measurement tools

---

A) Printer can detect when nozzle touches something, allowing it to digitize objects

///

## According to the lecture, what is the main reason objects can be printed with embedded magnets or nuts?

---

A) Printers have special features

B) Magnets stick to plastic

C) Can pause print, insert objects, then resume printing over them

D) Special materials are used

---

C) Can pause print, insert objects, then resume printing over them

///

## What is the main reason solvent vapor smoothing is dangerous?

---

A) Involves toxic fumes and heating flammable materials

B) It is slow

C) It is expensive

D) It damages prints

---

A) Involves toxic fumes and heating flammable materials

///

## According to the lecture, what is the main reason screws can self-tap into 3D printed parts?

---

A) Make hole slightly undersized and steel/brass screw thread cuts its own thread

B) Plastic is soft

C) Special materials are used

D) Holes are pre-threaded

---

A) Make hole slightly undersized and steel/brass screw thread cuts its own thread

///

## What is the main reason the Creality Ferret Pro scanner can capture color information?

---

A) Cameras can capture color when infrared light is turned off

B) It uses color cameras

C) Color is added in post-processing

D) It uses special sensors

---

A) Cameras can capture color when infrared light is turned off

///

## According to the lecture, what is the main reason 3D printing is considered simpler computationally than five-axis CNC milling?

---

A) Software difficulty increases dramatically with number of dimensions, and 3D printing works in 2D layers

B) 3D printers are slower

C) 3D printers are cheaper

D) 3D printing uses less memory

---

A) Software difficulty increases dramatically with number of dimensions, and 3D printing works in 2D layers

///

## What is the main reason the mathematical definition of Minkowski sum involves allowing a point to visit all points in another shape?

---

A) To simplify calculations

B) To make it easier to understand

C) To describe the union of all possible positions creating expanded shape

D) To reduce computation time

---

C) To describe the union of all possible positions creating expanded shape

///

## According to the lecture, what is the main reason titanium dioxide is often added to PLA?

---

A) To change its color

B) To make it flexible

C) To make it stronger

D) To provide UV resistance (same material used in sunscreen)

---

D) To provide UV resistance (same material used in sunscreen)

///

## What is the main reason the lecture mentions that "your brain has had three and a half billion years of evolution" regarding point correspondence?

---

A) To compare human and computer vision

B) To describe brain evolution

C) To emphasize how difficult the problem is for computers

D) To explain why humans are better at scanning

---

C) To emphasize how difficult the problem is for computers

///

## According to the lecture, what is the main reason belt printers can print objects of any length?

---

A) Conveyor belt can be extended to accommodate longer prints

B) They use less material

C) They are faster

D) They are more accurate

---

A) Conveyor belt can be extended to accommodate longer prints

///

## What is the main reason the lecture describes 3D printing as "essentially a computer-controlled hot glue gun"?

---

A) To compare it to other technologies

B) To describe how FFF printing works by extruding molten plastic

C) To explain its history

D) To emphasize its simplicity

---

B) To describe how FFF printing works by extruding molten plastic

///

## According to the lecture, what is the main reason the first RepRap machine is now in a museum?

---

A) It was donated

B) It represents historical significance as first self-replicating 3D printer

C) It was broken

D) It was very expensive

---

B) It represents historical significance as first self-replicating 3D printer

///

## What is the main reason the lecture mentions that complexity is "almost free" in 3D printing?

---

A) Printing time is similar for simple and complex shapes

B) 3D printers are very cheap

C) 3D printers are very fast

D) Complex shapes use less material

---

A) Printing time is similar for simple and complex shapes

///

## According to the lecture, what is the main reason a turntable can replace a second camera in stereo vision scanning?

---

A) Rotating object creates multiple views equivalent to having two eyes

B) Turntables are more accurate

C) Turntables are faster

D) Turntables are cheaper

---

A) Rotating object creates multiple views equivalent to having two eyes

///

## What is the main reason the lecture describes scanning as having "two easy stages and two hard stages"?

---

A) Gathering images and creating point cloud are easy, point correspondence and triangulation are hard

B) To compare with printing

C) To explain the process

D) To emphasize the difficulty

---

A) Gathering images and creating point cloud are easy, point correspondence and triangulation are hard

///

## According to the lecture, what is the main reason the Stanford bunny example shows points with "hairs" (normal vectors)?

---

A) To demonstrate scanning accuracy

B) Poisson surface reconstruction requires both points and normal vectors

C) To show file format

D) To show fur texture

---

B) Poisson surface reconstruction requires both points and normal vectors

///

## What is the main reason the lecture mentions that "it's no use knowing how far away the tiger is 5 seconds after it's eaten you"?

---

A) To explain evolution

B) To compare scanning speeds

C) To emphasize that vision systems need to work very quickly for survival

D) To describe animal behavior

---

C) To emphasize that vision systems need to work very quickly for survival

///

## According to the lecture, what is the main reason the 3MF format is recommended over STL?

---

A) It is older

B) It is compressed, supports texture and multimaterial, and can embed G-code

C) It is simpler

D) It is faster to process

---

B) It is compressed, supports texture and multimaterial, and can embed G-code

///

## What is the main reason the lecture mentions that scanning is "increasingly important for augmented reality"?

---

A) Commercial effort going into cell phone scanning capabilities

B) It is more accurate

C) It is cheaper

D) It is faster

---

A) Commercial effort going into cell phone scanning capabilities

///

## According to the lecture, what is the main reason the example of the scissor screw jack is notable?

---

A) It was made in one shot as complete functional mechanism without assembly

B) It uses special materials

C) It is very large

D) It is very fast

---

A) It was made in one shot as complete functional mechanism without assembly

///

## What is the main reason the lecture describes the touch probe as "rather interesting"?

---

A) It is expensive

B) It is very accurate

C) It is very old

D) It illustrates technical principles and can be 3D printed

---

D) It illustrates technical principles and can be 3D printed

///

## According to the lecture, what is the main reason the lecture mentions that "your own creations are now museum pieces"?

---

A) To note historical significance of RepRap project

B) To describe museums

C) To compare with other projects

D) To emphasize age

---

A) To note historical significance of RepRap project

///

## What is the main reason the lecture mentions that "the ambiguity is always going to remain in some circumstances" regarding scanning?

---

A) Scanning is imperfect

B) Software is insufficient

C) Equipment is inadequate

D) Inherent limitation that can be minimized but not eliminated

---

D) Inherent limitation that can be minimized but not eliminated

///

## According to the lecture, what is the main reason the lecture describes 3D printing as working "in flat layers"?

---

A) This is why it's a two-dimensional problem rather than five-dimensional

B) To compare with milling

C) To describe materials

D) To explain the process

---

A) This is why it's a two-dimensional problem rather than five-dimensional

///

## What is the main reason the lecture mentions that "everywhere above the plane in which we're printing is going to be free of any obstructions"?

---

A) Printer can move freely in that space, unlike milling where tool must avoid collisions

B) To explain print orientation

C) To explain support material

D) To describe bed leveling

---

A) Printer can move freely in that space, unlike milling where tool must avoid collisions

///

## According to the lecture, what is the main reason the lecture describes FFF printing as "comparatively slow"?

---

A) Quality decreases when attempting to print very fast

B) It uses less material

C) It is more accurate

D) It requires more setup

---

A) Quality decreases when attempting to print very fast

///

## What is the main reason the lecture mentions that "the little P is still attached to the base of the print" in the whistle example?

---

A) It needs to be manually detached after printing to allow movement

B) It is part of the design

C) It cannot be printed separately

D) It is a printing error

---

A) It needs to be manually detached after printing to allow movement

///

## According to the lecture, what is the main reason the lecture mentions that "milling creates waste" while 3D printing is "near-net-shape"?

---

A) Milling cuts material away creating swarf, while 3D printing adds material with minimal waste

B) 3D printing uses different materials

C) 3D printing is more accurate

D) 3D printing is faster

---

A) Milling cuts material away creating swarf, while 3D printing adds material with minimal waste

///

## What is the main reason the lecture describes "birds nesting" as a failure mode?

---

A) Material doesn't stick down properly creating wild mess

B) It is a design feature

C) It is a printer feature

D) It is a material property

---

A) Material doesn't stick down properly creating wild mess

///

## According to the lecture, what is the main reason the lecture mentions that "the particulate emissions from PLA are not that great"?

---

A) PLA is relatively benign and safe for open-air printing

B) PLA is transparent

C) PLA is very strong

D) PLA is flexible

---

A) PLA is relatively benign and safe for open-air printing

///

## What is the main reason the lecture mentions that "as we move to the left" on the emission diagram, emissions increase?

---

A) Different printer types

B) Different materials have higher emissions requiring enclosed machines and filters

C) Different print sizes

D) Different print speeds

---

B) Different materials have higher emissions requiring enclosed machines and filters

///

## According to the lecture, what is the main reason the lecture describes the scissor screw jack as making a "crack" sound when first used?

---

A) Parts initially constrained by support material are releasing to allow movement

B) It is a design feature

C) It is a material property

D) It is breaking

---

A) Parts initially constrained by support material are releasing to allow movement

///

## What is the main reason the lecture mentions that "the welding between the layers is not as strong as the plastic solidifying inner layer"?

---

A) To explain anisotropy - different strength in different directions

B) To explain print orientation

C) To describe material properties

D) To explain print speed

---

A) To explain anisotropy - different strength in different directions

///

## According to the lecture, what is the main reason the lecture mentions that "we occasionally have to have extra material which we're going to throw away"?

---

A) Support material is needed but discarded after printing

B) It is a design flaw

C) It is unavoidable waste

D) It is a material property

---

A) Support material is needed but discarded after printing

///

## What is the main reason the lecture describes the free flow infill technique with hot and cold risers?

---

A) To improve print speed

B) To allow resin to be poured into print and fill all connected spaces for strength

C) To reduce material usage

D) To explain casting principles

---

B) To allow resin to be poured into print and fill all connected spaces for strength

///

## According to the lecture, what is the main reason the lecture mentions that "almost all modern FFF 3D printers can do" bed leveling?

---

A) It is essential for ensuring first layer adhesion

B) It is a new feature

C) It is optional

D) It is expensive

---

A) It is essential for ensuring first layer adhesion

///

## What is the main reason the lecture describes the random fine cylinders technique as creating "fiberglass-like" reinforcement?

---

A) Printer creates continuous surface reinforcement similar to fiberglass structure

B) It uses similar materials

C) It has similar appearance

D) It uses glass fibers

---

A) Printer creates continuous surface reinforcement similar to fiberglass structure

///

## According to the lecture, what is the main reason the lecture mentions that conducting filament resistivity is "about 10 million times worse" than copper?

---

A) To explain why it can illuminate LED but isn't like working with metal

B) To emphasize it is not suitable for high-current applications

C) To describe material properties

D) To compare costs

---

A) To explain why it can illuminate LED but isn't like working with metal

///

## What is the main reason the lecture mentions that PVA (polyvinyl alcohol) is water soluble?

---

A) It is a material property

B) It is a disadvantage

C) It is a printing requirement

D) It makes it useful as soluble support material

---

D) It makes it useful as soluble support material

///

## According to the lecture, what is the main reason the lecture describes G-code as treating "extrusion as another dimension like x, y, and z"?

---

A) To describe file format

B) To explain print speed

C) Extrusion amount can be controlled independently just like spatial movement

D) To explain the coordinate system

---

C) Extrusion amount can be controlled independently just like spatial movement

///

## What is the main reason the lecture mentions that "you can edit G-code by hand if you're feeling brave"?

---

A) It is text-based format but risky as wrong commands could cause collisions

B) It is recommended

C) It is required

D) It is easy to do

---

A) It is text-based format but risky as wrong commands could cause collisions

///

## According to the lecture, what is the main reason the lecture describes the Minkowski sum as "computationally intensive"?

---

A) It requires complex calculations

B) Should keep added shape simple to reduce computation

C) It is slow

D) It requires special hardware

---

B) Should keep added shape simple to reduce computation

///

## What is the main reason the lecture mentions that solvent vapor smoothing uses "surface tension" to smooth surfaces?

---

A) It is a material property

B) Slight surface dissolution allows surface tension to smooth the surface

C) It is a chemical reaction

D) It is a physical property

---

B) Slight surface dissolution allows surface tension to smooth the surface

///

## According to the lecture, what is the main reason the lecture mentions that threaded inserts are inserted "with a heated soldering iron"?

---

A) Heat softens plastic allowing insert to be pushed into undersized hole

B) To clean the hole

C) To melt the plastic

D) To harden the insert

---

A) Heat softens plastic allowing insert to be pushed into undersized hole

///

## What is the main reason the lecture describes electroplating as requiring "electrically conducting paint" first?

---

A) To improve adhesion

B) 3D printed plastic is not conductive, so must be coated before electroplating

C) To change color

D) To protect the print

---

B) 3D printed plastic is not conductive, so must be coated before electroplating

///

## According to the lecture, what is the main reason the lecture mentions that "some materials ask us to wash it after with water" after IPA wash?

---

A) To improve finish

B) Different resin materials have different post-processing requirements

C) To speed up curing

D) To remove IPA

---

B) Different resin materials have different post-processing requirements

///

## What is the main reason the lecture mentions that UV cure chamber process is "very toxic"?

---

A) It uses dangerous materials

B) Requires buffer or good ventilation due to toxic fumes

C) It is expensive

D) It is slow

---

B) Requires buffer or good ventilation due to toxic fumes

///

## According to the lecture, what is the main reason the lecture describes multi-jet printing as using "voxels"?

---

A) Material drops are flattened by roller creating three-dimensional pixels

B) To explain the process

C) To describe file format

D) To compare with other methods

---

A) Material drops are flattened by roller creating three-dimensional pixels

///

## What is the main reason the lecture mentions that multi-jet printing can create objects with "50% rigid material and 50% flexible material"?

---

A) Shows how material distribution affects behavior, not just appearance

B) To explain cost

C) To describe speed

D) To demonstrate multimaterial capability

---

A) Shows how material distribution affects behavior, not just appearance

///

## According to the lecture, what is the main reason the lecture mentions that the heart defect surgery example reduced time "from 60+ hours to 15 hours"?

---

A) Simpler procedure

B) Doctor could practice on 3D printed hearts mimicking actual organ behavior

C) Better equipment

D) Better materials

---

B) Doctor could practice on 3D printed hearts mimicking actual organ behavior

///

## What is the main reason the lecture mentions that "the web page is the design tool" for one student project?

---

A) Student wrote code to generate STL file rather than using CAD software

B) To describe file formats

C) To explain the process

D) To explain web design

---

A) Student wrote code to generate STL file rather than using CAD software

///

## According to the lecture, what is the main reason the lecture mentions that "orientation is important" for support removal?

---

A) Post-processing can destroy parts if not designed with support removal in mind

B) To reduce material usage

C) To speed up printing

D) To improve print quality

---

A) Post-processing can destroy parts if not designed with support removal in mind

///

## What is the main reason the lecture mentions that AI-designed projects "count as design as long as you document the workflow"?

---

A) Design includes documenting how something was created, not just manual CAD work

B) Documentation is optional

C) AI is required

D) Process is what matters

---

A) Design includes documenting how something was created, not just manual CAD work

///

## According to the lecture, what is the main reason the lecture mentions "photogrammetry apps that work on cell phones"?

---

A) Scanning technology is rapidly maturing and becoming accessible

B) They are free

C) They are fast

D) They are accurate

---

A) Scanning technology is rapidly maturing and becoming accessible

///

## What is the main reason the lecture describes the assignment as requiring testing "your printer's capabilities" first?

---

A) To learn the printer

B) To compare printers

C) To calibrate it

D) Need to understand printer limitations like wall thickness and behavior before designing

---

D) Need to understand printer limitations like wall thickness and behavior before designing

///

## According to the lecture, what is the main reason the lecture mentions that "3MF is now the most recommended file format"?

---

A) It is compressed, supports texture and multimaterial, and can embed G-code

B) It is oldest

C) It is simplest

D) It is fastest

---

A) It is compressed, supports texture and multimaterial, and can embed G-code

///

## What is the main reason the lecture mentions that the student project involved "heating the model and then inflate it and deflate it"?

---

A) To check if model is watertight after printing

B) To test strength

C) To improve appearance

D) To test material properties

---

A) To check if model is watertight after printing

///

## According to the lecture, what is the main reason the lecture describes Chinese balls (ball within ball within ball) as notable?

---

A) They demonstrate capabilities that cannot be made subtractively

B) They are very large

C) They are very complex

D) They use special materials

---

A) They demonstrate capabilities that cannot be made subtractively

///

## What is the main reason the lecture mentions that "the heart is the design task" for the assignment?

---

A) Main requirement is designing something that cannot be made subtractively

B) It is optional

C) It is the easiest part

D) It is the most important part

---

A) Main requirement is designing something that cannot be made subtractively

///

## According to the lecture, what is the main reason the lecture mentions "global open time for any challenge of any kind"?

---

A) Flexible assignment structure allows various approaches

B) To encourage creativity

C) To reduce workload

D) To extend deadline

---

A) Flexible assignment structure allows various approaches

///

## What is the main reason the lecture describes this week as "one of the more creative weeks"?

---

A) Assignment requires designing novel objects leveraging 3D printing advantages

B) It uses more materials

C) It is shorter

D) It is easier

---

A) Assignment requires designing novel objects leveraging 3D printing advantages

///