# Python ImGui Overlay Template

A clean, modular template for creating transparent overlay applications on Windows using Dear ImGui, GLFW, and OpenGL.

## ✨ Features

- 🪟 **Transparent overlay** - Click-through capable window that stays on top
- 🎨 **ImGui interface** - Beautiful, immediate-mode GUI
- 📦 **Modular structure** - Well-organized, easy to extend
- ⚡ **Lightweight** - Minimal dependencies, fast performance
- 🔧 **Configurable** - Easy customization through config files

## 📁 Project Structure

```
.
├── main.py   # Main entry point
├── config.py            # Configuration settings
├── window_manager.py    # Window creation and GLFW management
├── ui_manager.py        # UI components and ImGui rendering
├── requirements.txt     # Python dependencies
└── README.md           # This file
```

## 🚀 Quick Start

### Prerequisites

- Python 3.7+
- Windows OS (for Win32 API transparency features)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/nick-tinnapat/imgui-glfw-overlay-template
cd imgui-glfw-overlay-template
```

2. Install dependencies:
```bash
pip install -r requirements.txt 
or 
pip install glfw PyOpenGL imgui[full] pywin32
```

3. Run the application:
```bash
python main.py
```

## 📚 Module Documentation

### `main.py`
Main application entry point containing the `OverlayApplication` class that orchestrates the entire application lifecycle:
- Initialization
- Main rendering loop
- Cleanup and shutdown

### `config.py`
Centralized configuration module with two main classes:
- **`WindowConfig`**: Window properties (title, dimensions, flags)
- **`StyleConfig`**: ImGui styling (colors, transparency, theme)

### `window_manager.py`
Handles all window-related operations:
- GLFW initialization
- Window creation with proper hints
- Win32 API transparency configuration
- Window lifecycle management

### `ui_manager.py`
Manages the user interface:
- ImGui context and renderer setup
- UI component rendering
- Input processing
- OpenGL rendering pipeline

## 🎨 Customization

### Change Window Background Color
Edit in `config.py`:
```python
WINDOW_BG_COLOR = (R, G, B, A)  # Values: 0.0-1.0
```

### Add New UI Components
Modify the `render_ui()` method in `ui_manager.py`:
```python
def render_ui(self):
    imgui.new_frame()
    imgui.begin("Your Window")
    
    # Add your components here
    imgui.text("Custom text")
    if imgui.button("Custom button"):
        print("Clicked!")
    
    imgui.end()
```

### Modify Window Size
Edit the `create_window()` method in `window_manager.py`

### Change Window Title
Edit in `config.py`:
```python
WINDOW_TITLE = "Your Custom Title"
```

## 📦 Dependencies

- **glfw** - Window management
- **imgui[glfw]** - Immediate mode GUI
- **PyOpenGL** - OpenGL bindings
- **pywin32** - Windows API access
- **numpy** - Required by PyOpenGL

## 🛠️ Use Cases

This template is perfect for creating:
- Game overlays
- Monitoring tools
- Screen annotations
- Desktop widgets
- Debug interfaces
- Real-time data displays

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest features
- Submit pull requests

## 📝 License

This project is open source and available under the MIT License.

## 🙏 Acknowledgments

- [Dear ImGui](https://github.com/ocornut/imgui) - Bloat-free Immediate Mode Graphical User interface
- [pyimgui](https://github.com/pyimgui/pyimgui) - Python bindings for ImGui
- [GLFW](https://www.glfw.org/) - Multi-platform library for OpenGL


**Happy coding! 🚀**