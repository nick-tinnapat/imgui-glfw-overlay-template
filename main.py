"""
Main application class that orchestrates the overlay application
"""
import glfw
from window_manager import WindowManager
from ui_manager import UIManager


class OverlayApplication:
    """Main overlay application"""
    
    def __init__(self):
        self.window_manager = WindowManager()
        self.ui_manager = None
    
    def initialize(self):
        """Initialize the application"""
        # Initialize GLFW
        self.window_manager.initialize_glfw()
        
        # Create window
        window = self.window_manager.create_window()
        
        # Configure transparency
        self.window_manager.configure_transparency()
        
        # Initialize UI
        self.ui_manager = UIManager(window)
    
    def run(self):
        """Main application loop"""
        while not self.window_manager.should_close():
            # Poll events
            glfw.poll_events()
            
            # Process inputs
            self.ui_manager.process_inputs()
            
            # Render UI
            self.ui_manager.render_ui()
            self.ui_manager.render()
            
            # Swap buffers
            glfw.swap_buffers(self.window_manager.window)
    
    def cleanup(self):
        """Cleanup resources"""
        if self.ui_manager is not None:
            self.ui_manager.shutdown()
        self.window_manager.terminate()


def main():
    """Entry point of the application"""
    app = OverlayApplication()
    
    try:
        app.initialize()
        app.run()
    finally:
        app.cleanup()


if __name__ == "__main__":
    main()