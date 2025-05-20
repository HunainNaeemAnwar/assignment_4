import time
def countdown(seconds):
    try:
        while seconds:
            mins, secs = divmod(seconds, 60)
            timer = f'{mins:02d}:{secs:02d}'
            print(f'\r Time Remaining: {timer}', end='')
            time.sleep(1)
            seconds -= 1
        print('\r Time\'s up!')
    except KeyboardInterrupt:
        print("\n Timer cancelled.")

if __name__ == "__main__":
    duration = int(input("Enter countdown duration (in seconds): "))
    countdown(duration)
