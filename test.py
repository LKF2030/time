import time

# 定义专注时间和休息时间（秒）
FOCUS_TIME = 25 * 60  # 25分钟
BREAK_TIME = 5 * 60   # 5分钟

def countdown(seconds):
    while seconds:
        mins, secs = divmod(seconds, 60)
        timer = f'{mins:02}:{secs:02}'
        print(timer, end="\r")  # 使用 \r 刷新同一行
        time.sleep(1)
        seconds -= 1

def start_pomodoro():
    while True:
        print("开始专注时间！请专注工作 25 分钟。")
        countdown(FOCUS_TIME)
        print("时间到！请休息 5 分钟。")
        countdown(BREAK_TIME)
        print("休息结束！开始新的专注时间。")

if __name__ == "__main__":
    start_pomodoro()
