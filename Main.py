from Hand_Mouse_Controller import HandMouseController
from Game_Runner import GameRunner
from threading import Thread

def main(game_window_width=1300, game_window_height=1000):
    game_runner = GameRunner(exe_path=r"ChickenInvadersTNWdemo/CI2rmdemo.exe", window_title="Chicken Invaders", window_width=game_window_width, window_height=game_window_height)
    hand_mouse_controller = HandMouseController(screen_width=int(game_window_width/3), screen_height=int(game_window_height/3))

    # Tạo và bắt đầu luồng để chạy game
    game_thread = Thread(target=game_runner.run_game)
    game_thread.start()

    # Chạy HandMouseController
    hand_mouse_controller.run()

if __name__ == "__main__":
    main()
