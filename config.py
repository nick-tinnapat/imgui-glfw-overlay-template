"""
Configuration settings for the overlay application
"""
import imgui


class WindowConfig:
    """Window-related configuration"""
    WINDOW_TITLE = "Visgard Control"
    FLOATING = True
    TRANSPARENT = True
    DECORATED = False
    
    @staticmethod
    def get_screen_dimensions(monitor, video_mode):
        """Get screen dimensions from video mode"""
        return video_mode.size.width, video_mode.size.height


class StyleConfig:
    """ImGui style configuration"""
    GLOBAL_ALPHA = 1.0
    WINDOW_BG_COLOR = (0.1, 0.1, 0.1, 1.0)
    
    @staticmethod
    def apply_style():
        """Apply custom style to ImGui"""
        style = imgui.get_style()
        style.alpha = StyleConfig.GLOBAL_ALPHA
        # style.colors[imgui.COLOR_WINDOW_BACKGROUND] = StyleConfig.WINDOW_BG_COLOR