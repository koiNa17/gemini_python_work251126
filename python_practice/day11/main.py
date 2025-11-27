import sys
import platform

print("=" * 30)
print("Hello from inside Docker!")
print("=" * 30)

# Pythonのバージョンを表示
print(f"Python Version: {sys.version}")

# OS（Linux）の情報を表示
print(f"System: {platform.system()} {platform.release()}")