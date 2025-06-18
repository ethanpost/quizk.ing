## [Interface and Application Programming](https://www.youtube.com/watch?v=2baDZPkYvc0)

> Import this file into [Mochi](https://mochi.cards/) or give it to your favorite AI tool and have it proxy a quiz and check your answers. When importing make sure you select Markdown as the format, "Multiple cards per .md file", and a ```triple backslash``` as the string delimiter. You can use the link to the raw file in GitHub instead of downloading and importing if you prefer.

### Programming Languages
- C and C++ - Low to high level languages
  - C is venerable with security and safety issues
  - C++ extends C with objects and methods
  - Used in Arduino IDE programming
- Modern Languages
  - Go and Rust - Address C's security issues
  - Rust gaining traction for embedded applications
  - High performance with cleaner, more reliable code
- Functional Languages
  - Describe functions instead of steps
  - Evaluate functions to write programs
- Scripting Languages
  - Designed for simple scripts
  - Terminal command interpreters
  - Bash scripts for automation
- Python
  - Beautiful, well-documented, cross-platform language
  - Performance issues but can be accelerated
  - Package proliferation managed by virtual environments
  - Dominates machine learning applications
- Processing
  - Like Arduino for desktop
  - Handles graphics, sound, and multimedia
  - Standalone and JavaScript (p5.js) versions available
- Java
  - Platform-independent through bytecode interpretation
  - Historical technical and commercial issues
  - Still used in corporate computing
- JavaScript
  - Web programming language (unrelated to Java)
  - Just-in-time compilation for performance
  - Runs in web browsers and Node.js
  - Web Serial API for device communication

### Low-Code and No-Code Environments
- Data Flow Programming
  - Visual programming with blocks and diagrams
  - LabVIEW for lab automation
  - Simulink for MATLAB
  - Max for music
  - Scratch for kids' programming
  - App Inventor for mobile apps
  - Node-RED for IoT and event programming
  - Mods as general-purpose data flow framework

### Device Communication
- Serial Communication
  - RS232 and USB serial
  - Python with pyserial
  - Node.js serial port libraries
  - Web Serial API in Chrome browsers
- I2C and USB Protocols
  - Direct USB communication
  - Higher-level protocol implementation
- Network Communication
  - Sockets for web programming
  - MQTT (Message Queuing Telemetry Transport)
    - Most common for IoT device ecosystems
    - Publish/subscribe model
    - Broker-based architecture
    - Manages multiple devices efficiently

### Data Organization
- Text Formats
  - JSON for object description
  - TOML for markup language
  - Spreadsheets (limited scalability)
- Databases
  - Open-source database options
  - Used when data exceeds computer memory
  - File-based storage for smaller datasets

### User Interface Frameworks
- Text Interfaces
  - Terminal with ncurses programming interface
  - Command-line arguments
- Desktop GUI Frameworks
  - Tkinter - Cross-platform, consistent appearance
  - wxWidgets - Native-looking interfaces
  - Qt, GTK, Clutter, Kivy - Various widget sets
- Web Interfaces
  - HTML Forms - Basic web interface elements
  - jQuery - Advanced JavaScript widgets
  - Modern frameworks for cross-platform development
  - Mobile and desktop responsive design

### Graphics and Visualization
- Web Graphics
  - Canvas - Pixel-level drawing
  - SVG - Resolution-independent vector graphics
  - WebGL - 3D accelerated graphics
  - Three.js - High-level 3D scene description
- Python Graphics
  - PyGFX for 3D environments
  - Taichi for graphics and acceleration
- Game Engines
  - Blender with Python scripting
  - 3D environment programming

### Audio and Video
- Multimedia Frameworks
  - SDL for multimedia
  - Pygame wrapper around SDL
  - OpenFrameworks for video projection mapping
- Web Audio/Video
  - HTML5 audio and video extensions
  - Audio context for sound generation
  - Camera access and video streaming
- Virtual and Augmented Reality
  - VR, AR, MR, XR environments
  - Three.js VR integration
  - Web-based AR standards

### Mathematics and Data Analysis
- Mathematical Libraries
  - NumPy - Extends Python for mathematical operations
  - Matplotlib - Graphing and plotting framework
  - SymPy - Symbolic mathematics
- Interactive Computing
  - Jupyter notebooks
  - Google Colab cloud service
  - Live code execution and documentation
- Advanced Visualization
  - Plotly for Python and JavaScript
  - D3.js for complex data visualizations
  - Specialized graph types and layouts

### Performance Optimization
- Language Performance
  - Python interpretation vs. compilation
  - Numba for Python acceleration
  - JAX for Python acceleration and derivatives
- Parallel Computing
  - JavaScript workers for multi-core processing
  - Rust threading and Rayon parallelization
  - MPI for distributed computing
- Hardware Acceleration
  - CUDA for GPU computing
  - Web standards for graphics acceleration
  - Taichi framework integration

### Machine Learning
- Frameworks
  - TensorFlow and TensorFlow.js
  - PyTorch (most common currently)
  - Hugging Face for model sharing
- Implementation
  - Neural network architectures
  - Training loops and backpropagation
  - Loss functions and optimization
  - Data preprocessing and model evaluation
- Cloud Services
  - Commercial and free ML model interfaces
  - Production deployment options

### Deployment and Security
- Cloud Deployment
  - Amazon AWS and other cloud providers
  - Serverless applications
  - GitLab for production code management
- Security Considerations
  - Dependency vulnerabilities
  - Package management and updates
  - Historical security breaches (Heartbleed)
  - Best practices for secure development

### Terms
- **Hello World** - The traditional first program written in a new programming language, originating from the C programming book.
- **Esoteric Languages** - Programming languages created for amusement rather than practical use, often with unusual syntax.
- **Buffer Overflow** - A security vulnerability where a program writes data beyond the allocated memory buffer.
- **Race Condition** - A timing-dependent bug where program behavior depends on unpredictable timing between operations.
- **Memory Leak** - When a program uses memory that doesn't get properly returned to the system.
- **Virtual Environment** - An isolated Python environment with specific packages and dependencies.
- **Just-in-Time Compilation** - A technique where code is compiled to machine code at runtime for better performance.
- **WebSocket** - A communication protocol providing full-duplex communication channels over a single TCP connection.
- **MQTT Broker** - A server that handles message routing between publishers and subscribers in the MQTT protocol.
- **Publish/Subscribe** - A messaging pattern where senders (publishers) don't directly send messages to receivers (subscribers).
- **Widget** - A graphical user interface element like buttons, sliders, or text boxes.
- **Canvas** - An HTML element for drawing graphics and animations using JavaScript.
- **SVG** - Scalable Vector Graphics, an XML-based format for vector images.
- **WebGL** - A JavaScript API for rendering 3D graphics in web browsers.
- **Jupyter Notebook** - An interactive computing environment that combines code, output, and documentation.
- **NumPy** - A Python library for numerical computing with support for large arrays and matrices.
- **Matplotlib** - A Python plotting library for creating static, animated, and interactive visualizations.
- **Neural Network** - A machine learning model inspired by biological neural networks.
- **Backpropagation** - An algorithm for training neural networks by calculating gradients of the loss function.
- **Loss Function** - A function that measures how well a machine learning model performs on training data.

///

## What is the traditional first program written in a new programming language?

---

A) Hello World

B) Goodbye World

C) Welcome World

D) Start World

---

Hello World

///

## Which programming language is described as "beautiful, well-documented, cross-platform" and dominates machine learning applications?

---

A) Java

B) Python

C) JavaScript

D) C++

---

Python

///

## What type of programming environment allows you to describe what you want interactively without learning to write code?

---

A) Assembly programming

B) High-level programming

C) Low-code and no-code environments

D) Functional programming

---

Low-code and no-code environments

///

## Which protocol is described as the most common way to manage an ecosystem of multiple IoT devices?

---

A) HTTP

B) FTP

C) SMTP

D) MQTT

---

MQTT

///

## What is the main security issue mentioned with the C programming language that allows accessing memory you shouldn't be able to see?

---

A) Stack overflow

B) Race condition

C) Buffer overflow

D) Memory leak

---

Buffer overflow

///

## Which web graphics technology is described as "resolution-independent" and uses graphic elements with identities?

---

A) WebGL

B) Three.js

C) SVG

D) Canvas

---

SVG

///

## What is the name of the Python library that extends Python to make it more like APL for mathematical operations?

---

A) Pandas

B) SymPy

C) Matplotlib

D) NumPy

---

NumPy

///

## Which machine learning framework is currently described as the most common for AI applications?

---

A) Scikit-learn

B) PyTorch

C) Keras

D) TensorFlow

---

PyTorch

///

## What is the term for a timing-dependent bug where program behavior depends on unpredictable timing between operations?

---

A) Buffer overflow

B) Deadlock

C) Race condition

D) Memory leak

---

Race condition

///

## Which JavaScript feature allows you to run code on separate cores for parallel programming?

---

A) Callbacks

B) Async/await

C) Workers

D) Promises

---

Workers

///

## What is the name of the interactive computing environment that combines code, output, and documentation?

---

A) Terminal

B) Python REPL

C) Jupyter Notebook

D) Google Colab

---

Jupyter Notebook

///

## Which programming language is described as having "nothing to do with Java" despite its name?

---

A) LiveScript

B) TypeScript

C) CoffeeScript

D) JavaScript

---

JavaScript

///

## What is the term for an isolated Python environment with specific packages and dependencies?

---

A) Container

B) Virtual environment

C) Sandbox

D) Virtual machine

---

Virtual environment

///

## Which web technology provides full-duplex communication channels over a single TCP connection?

---

A) WebRTC

B) HTTP

C) WebSocket

D) WebGL

---

WebSocket

///

## What is the name of the algorithm used to train neural networks by calculating gradients of the loss function?

---

A) Gradient descent

B) Forward propagation

C) Backpropagation

D) Stochastic optimization

---

Backpropagation

///

## Which GUI framework is described as looking the same on any computer but not native-looking?

---

A) Qt

B) GTK

C) wxWidgets

D) Tkinter

---

Tkinter

///

## What is the term for a messaging pattern where senders don't directly send messages to receivers?

---

A) Point-to-point

B) Request-response

C) Broadcast

D) Publish-subscribe

---

Publish-subscribe

///

## Which Python library is described as a "wrapper around SDL" for multimedia programming?

---

A) OpenFrameworks

B) Taichi

C) Pygame

D) PyGFX

---

Pygame

///

## What is the name of the function that measures how well a machine learning model performs on training data?

---

A) Performance function

B) Error function

C) Loss function

D) Cost function

---

Loss function

///

## Which security vulnerability is described as making "much of the whole internet vulnerable" due to a low-level package issue?

---

A) Shellshock

B) Meltdown

C) Heartbleed

D) Spectre

---

Heartbleed

///

## What is the term for a machine learning model inspired by biological neural networks?

---

A) Support vector machine

B) Decision tree

C) Random forest

D) Neural network

---

Neural network

///

## Which programming technique compiles code to machine code at runtime for better performance?

---

A) Interpreted execution

B) Just-in-time compilation

C) Bytecode interpretation

D) Ahead-of-time compilation

---

Just-in-time compilation

///

## What is the name of the HTML element used for drawing graphics and animations using JavaScript?

---

A) Three.js

B) WebGL

C) Canvas

D) SVG

---

Canvas

///

## Which Python library is described as a "plotting library for creating static, animated, and interactive visualizations"?

---

A) Seaborn

B) Plotly

C) Matplotlib

D) NumPy

---

Matplotlib

///

## What is the term for when a program uses memory that doesn't get properly returned to the system?

---

A) Stack overflow

B) Buffer overflow

C) Memory leak

D) Race condition

---

Memory leak

///

## Which web graphics technology is described as a "JavaScript API for rendering 3D graphics in web browsers"?

---

A) Three.js

B) Canvas

C) SVG

D) WebGL

---

WebGL

///

## What is the name of the server that handles message routing between publishers and subscribers in the MQTT protocol?

---

A) MQTT Gateway

B) MQTT Router

C) MQTT Broker

D) MQTT Server

---

MQTT Broker

///

## Which programming languages are described as addressing C's security issues with "high performance but cleaner, modern language"?

---

A) Python and JavaScript

B) C++ and Objective-C

C) Go and Rust

D) Java and C#

---

Go and Rust

///

## What is the term for a graphical user interface element like buttons, sliders, or text boxes?

---

A) Control

B) Component

C) Element

D) Widget

---

Widget

///

## Which machine learning framework is described as having a "version that runs in a browser"?

---

A) Scikit-learn

B) Keras

C) PyTorch

D) TensorFlow

---

TensorFlow

///

## What is the name of the library for Rust that automatically knows how to parallelize code across all cores?

---

A) Futures

B) Rayon

C) Async-std

D) Tokio

---

Rayon
