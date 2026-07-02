import sys
import threading
import time

# Communication flags between main game and animation thread
qte_completed = False
player_input = ""


'''def spinning_clock_game(target_hand, clock_hands):
    """Continuously spins the clock hand inside a box until input is received."""
    global qte_completed, player_input

    frame_index = 0
    print("--- PRECISION TIMING EVENT ---")
    print(f"Goal: Stop the clock when the hand points UP '{target_hand}'!")
    # Print blank lines so the ANSI escape codes do not corrupt previous text
    print("\n\n")

    while not qte_completed:
        # Loop through the clock frames continuously
        current_hand = clock_hands[frame_index % len(clock_hands)]

        # Render the UI
        animation_output = (
            f"\r┌─0─┐  Target: [ {target_hand} ]\n"
            f"│ {current_hand} │  PRESS ENTER TO STOP!\n"
            f"└───┘"
        )

        # Move cursor up 2 lines to cleanly overwrite the box
        sys.stdout.write("\033[F\033[F")
        sys.stdout.write(animation_output)
        sys.stdout.flush()

        frame_index += 1
        time.sleep(0.12)  # Adjust this decimal to make the game faster or slower

    # Return the exact hand the user landed on
    final_hand = clock_hands[(frame_index - 1) % len(clock_hands)]
    return final_hand '''


'''def run_precision_qte():
    global qte_completed

    # Setup game assets
    clock_frames = ["↑", "↗︎", "→", "↘︎","↓","↙︎","←","↖︎"]
    target = "↑"  # The straight up position

    # Start the visual loop in a background thread
    animation_thread = threading.Thread(
        target=spinning_clock_game,
        args=(
            target,
            clock_frames,
        ),
    )
    animation_thread.daemon = True
    animation_thread.start()

    # The main thread blocks here until the user presses Enter
    input()
    qte_completed = True

    # Allow a microsecond for the background thread to finish its last loop
    time.sleep(0.05)

    # Fetch the final position the clock stopped on
    stopped_on = clock_frames[(animation_thread.ident is not None)]

    # Check if the player won
    # Note: Because threads run concurrently, we fetch the result safely
    # by checking the last evaluated frame state before qte_completed flipped.
    print("\n" * 2)  # Move past the drawn box layout

    # For safety in terminal timing, we manually double-check what frame was live
    # Since input interrupts instantly, we grab the final displayed frame.
    if spinning_clock_game.__code__:
        # In a real run, we evaluate if the stopped position matches target
        pass

    # Clean calculation for the evaluation:
    # (To keep code simple, the thread updates a shared state or we evaluate here) '''


def run_fixed_precision_qte():
    """Clean, robust execution of the target-landing loop."""
    global qte_completed
    qte_completed = False

    clock_frames = ["↑", "↗︎", "→", "↘︎","↓","↙︎","←","↖︎"]
    target = "↑"
    close_to_target_right = '/'
    close_to_target_left = '\\'

    # Shared container to safely pass data out of the thread
    result_container = {"final_frame": ""}

    def game_loop():
        frame_idx = 0
        print("--- PRECISION TIMING EVENT ---")
        print(f"Goal: Stop the clock when the hand points UP '{target}'!")
        print("\n\n")

        while not qte_completed:
            curr_frame = clock_frames[frame_idx % len(clock_frames)]
            result_container["final_frame"] = curr_frame

            output = (
                f"\r┌─0─┐  Target: [ {target} ]\n"
                f"│ {curr_frame} │  PRESS ENTER TO STOP!\n"
                f"└───┘"
            )
            sys.stdout.write("\033[F\033[F")
            sys.stdout.write(output)
            sys.stdout.flush()

            frame_idx += 1
            time.sleep(0.10)  # Lowering this number increases difficulty

    # Run animation
    t = threading.Thread(target=game_loop)
    t.daemon = True
    t.start()

    # Wait for player hit
    input()
    qte_completed = True
    time.sleep(0.02)  # Sync buffer

    # Results
    final_position = result_container["final_frame"]
    print(f"\nYou stopped the clock on: '{final_position}'")

    if final_position == target:
        print("Perfect Hit! You picked the lock successfully!")
    elif final_position == close_to_target_right or close_to_target_left:
        print("you were close")
    else:
        print("Off-balance! The mechanism jammed.")


# Run the updated game mechanics
run_fixed_precision_qte()
