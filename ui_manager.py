"""
UI components and rendering logic
"""
import imgui
import OpenGL.GL as gl
from imgui.integrations.glfw import GlfwRenderer
from config import StyleConfig


class UIManager:
    """Manages ImGui UI components and rendering"""
    
    def __init__(self, window):
        self.window = window
        self.impl = None
        self.slider_value = 0.5
        
        # Initialize ImGui
        imgui.create_context()
        self.impl = GlfwRenderer(window)
        
        # Apply custom style
        StyleConfig.apply_style()
    
    def process_inputs(self):
        """Process input events"""
        self.impl.process_inputs()
    
    def render_ui(self):
        """Render the UI components"""
        imgui.new_frame()
        
        # Main window
        imgui.begin("Visgard Control")
        
        # Text label
        imgui.text("Hello there, from Dear ImGui")
        
        # Button
        if imgui.button("Click me"):
            print("Button clicked!")
        
        # Slider
        changed, self.slider_value = imgui.slider_float(
            "Slider", 
            self.slider_value, 
            0.0, 
            1.0
        )
        if changed:
            print(f"Slider value {self.slider_value:.2f}")
        
        imgui.end()
    
    def render(self):
        """Render ImGui and swap buffers"""
        # Clear background with transparency
        gl.glClearColor(0, 0, 0, 0)
        gl.glClear(gl.GL_COLOR_BUFFER_BIT)
        
        # Render ImGui
        imgui.render()
        self.impl.render(imgui.get_draw_data())
    
    def shutdown(self):
        """Cleanup ImGui resources"""
        self.impl.shutdown()