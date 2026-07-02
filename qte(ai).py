import sys
import threading
import time
# Flags to manage thread communication
qte_completed = False


def clock_box_animation(time_limit):
    """Draws a box with a rotating clock hand and handles the timer."""
    global qte_completed
    start_time = time.time()
    end_time = start_time + time_limit

    # The sequence of characters representing a rotating clock hand
    clock_hands = ["|", "/", "-", "\\"]
    frame_index = 0

    while time.time() < end_time:
        if qte_completed:
            return  # Stop drawing instantly when player inputs

        remaining = max(0.0, end_time - time.time())
        current_hand = clock_hands[frame_index % len(clock_hands)]

        # Construct the box with the rotating hand inside
        # \r brings the cursor to the start of the line to overwrite it
        animation_output = (
            f"\r┌───┐  Time Left: {remaining:.1f}s\n"
            f"│ {current_hand} │  PRESS 'E' NOW!\n"
            f"└───┘  Input: "
        )

        # Move the cursor up 2 lines before writing to stay in place
        sys.stdout.write("\033[F\033[F")
        sys.stdout.write(animation_output)
        sys.stdout.flush()

        frame_index += 1
        time.sleep(0.15)  # Controls the rotation speed of the clock hand

    # If the loop finishes, the player ran out of time
    if not qte_completed:
        sys.stdout.write("\n\n\n Too slow! You failed the event.\n")
        sys.exit()


def run_clock_qte():
    global qte_completed

    time_limit = 4.0
    correct_key = "E"

    print("--- QUICK TIME EVENT ---")
    # Print dummy blank lines so the cursor up codes (\033[F) do not erase old text
    print("\n\n")

    # Start the animation thread
    timer_thread = threading.Thread(
        target=clock_box_animation, args=(time_limit,)
    )
    timer_thread.daemon = True
    timer_thread.start()

    # Capture the player's input
    user_input = input().strip().upper()
    qte_completed = True

    # Evaluate the result
    if user_input == correct_key:
        print("\nSuccess! You timed it perfectly!")
    else:
        print("\nWrong key! The trap triggered.")


# Run the event
run_clock_qte()
