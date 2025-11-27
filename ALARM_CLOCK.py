import time
from datetime import datetime
import os
import platform
import sys

def clear_console():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def beep():
    if platform.system() == "Windows":
        import winsound
        winsound.Beep(1000, 500)
    else:
        sys.stdout.write("\a")
        sys.stdout.flush()

def main():
    clear_console()
    print("=== Ceas simplu cu alarmă ===")
    print("Format oră: HH:MM (ex: 07:30)\n")

    while True:
        alarm_time = input("Setează ora alarmei: ").strip()
        try:
            datetime.strptime(alarm_time, "%H:%M")
            break
        except ValueError:
            print("Format invalid. Folosește HH:MM (ex: 07:30).")

    alarm_msg = input("Mesaj pentru alarmă: ").strip() or "Trezirea!"

    print("\nAlarmă setată pentru:", alarm_time)
    print("Mesaj:", alarm_msg)
    print("\nApasă Ctrl+C pentru a opri programul.\n")

    try:
        while True:
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            current_hm = now.strftime("%H:%M")

            clear_console()
            print(f"Timp curent: {current_time}")
            print(f"Alarmă: {alarm_time}")
            print("--------------------------")
            print("Aștept alarma...")

            if current_hm == alarm_time:
                clear_console()
                print("=== ALARMĂ! ===")
                print(f"{alarm_time} - {alarm_msg}")
                print("================")
                for _ in range(5):
                    beep()
                    time.sleep(0.5)
                break

            time.sleep(1)

    except KeyboardInterrupt:
        print("\nProgram oprit manual.")

if __name__ == "__main__":
    main()
