import subprocess
import time
import pygetwindow as gw
import pyautogui

class GameRunner:
    """
        Lớp khởi tạo và chạy game

        tham số cần thiết:
        - exe_path VD: exe_path="game/rungame.exe" (string)
        - window_title VD: window_title="GameRunner" (string)
        - window_width VD: window_width=1920 (int)
        - window_height VD: window_height=1080 (int)
    """
    def __init__(self, exe_path, window_title, window_width, window_height):
        self.exe_path = exe_path
        self.window_title = window_title
        self.window_width = window_width
        self.window_height = window_height

    def run_game(self):
        # Chạy và Điều chỉnh vị trí cửa sổ game
        subprocess.Popen([self.exe_path], creationflags=subprocess.CREATE_NEW_CONSOLE)
        time.sleep(5) 

        windows = gw.getWindowsWithTitle(self.window_title)
        if windows:
            game_window = windows[0]
            game_window.restore()
            game_window.resizeTo(self.window_width, self.window_height)
            game_window.moveTo(0, 0)

            game_window.activate()
            pyautogui.click(game_window.left + 100, game_window.top + 100) 
        else:
            print(f"Không tìm thấy cửa sổ với tiêu đề: {self.window_title}")

        # Điều chỉnh vị trí camera
        camera_window_title = "Hand Tracking"
        camera_windows = gw.getWindowsWithTitle(camera_window_title)
        if camera_windows:
            camera_window = camera_windows[0]
            camera_window.resizeTo(640, 480)
            camera_window.moveTo(1920 - 640, 0) 
        else:
            print(f"Không tìm thấy cửa sổ với tiêu đề: {camera_window_title}")
