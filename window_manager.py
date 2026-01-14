"""
Window manager for creating and configuring the overlay window
"""
import glfw
import win32gui
import win32con
from config import WindowConfig


class WindowManager:
    """Manages window creation and configuration"""
    
    def __init__(self):
        self.window = None
        self.screen_width = 0
        self.screen_height = 0
    
    def initialize_glfw(self):
        """Initialize GLFW library"""
        if not glfw.init():
            raise Exception("Could not initialize GLFW")
    
    def create_window(self):
        """Create the overlay window with proper settings"""
        # Set window hints
        glfw.window_hint(glfw.FLOATING, WindowConfig.FLOATING)
        glfw.window_hint(glfw.TRANSPARENT_FRAMEBUFFER, WindowConfig.TRANSPARENT)
        glfw.window_hint(glfw.DECORATED, WindowConfig.DECORATED)
        
        # Get screen dimensions
        monitor = glfw.get_primary_monitor()
        video_mode = glfw.get_video_mode(monitor)
        self.screen_width, self.screen_height = WindowConfig.get_screen_dimensions(
            monitor, video_mode
        )
        
        # Create window
        self.window = glfw.create_window(
            self.screen_width,
            self.screen_height - 1,
            WindowConfig.WINDOW_TITLE,
            None,
            None
        )
        
        # Position window
        glfw.set_window_pos(self.window, 0, 0)
        glfw.make_context_current(self.window)
        
        return self.window
    
    def configure_transparency(self):
        """Configure window transparency using Win32 API"""
        hwnd = glfw.get_win32_window(self.window)
        ex_style = win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE)
        
        # Set window to be layered and always on top
        win32gui.SetWindowLong(
            hwnd,
            win32con.GWL_EXSTYLE,
            ex_style | win32con.WS_EX_LAYERED | win32con.WS_EX_TOPMOST,
        )
        
        # Set color key for transparency (black = transparent)
        win32gui.SetLayeredWindowAttributes(
            hwnd, 
            0x000000,  # Color key (black)
            255,        # Alpha
            win32con.LWA_COLORKEY
        )
    
    def should_close(self):
        """Check if window should close"""
        return glfw.window_should_close(self.window)
    
    def terminate(self):
        """Terminate GLFW"""
        glfw.terminate()