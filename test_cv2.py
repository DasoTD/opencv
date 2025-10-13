import cv2
import sys
print(f"cv2.__file__: {cv2.__file__}")
print(f"cv2.config: {getattr(sys.modules.get('cv2.config', {}), '__file__', 'Not found')}")
print(f"cv2.config_3: {getattr(sys.modules.get('cv2.config_3', {}), '__file__', 'Not found')}")
def test_import():
    assert cv2.__version__
