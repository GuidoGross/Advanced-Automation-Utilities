# **Advanced Automation Utilities**

Personal use automation utilities library. A powerful, native Python library for Windows automation, featuring Context Manager-based async chaining and zero dependence on heavy GUI automation libraries. It leverages native `ctypes` hooks for maximum speed, security, and lower overhead.

---

## **Purpose**

**This library is designed for scripts and applications that need:**

- Reliable, human-like mouse movements natively in Windows.
- Low-level keyboard hooks and precise inputs.
- Fast and accurate screen vision (OCR and image matching).
- Asynchronous execution and method chaining.
- Reliable timing, sound, and system-level operations.

---

## **Requirements**

### **Dependencies**

**Standard library modules are used where possible; only external dependencies are listed:**

- `mss` (6.1.0 or higher)
- `numpy` (1.21.0 or higher)
- `opencv-python` (4.5.5 or higher)
- `psutil` (5.8.0 or higher)
- `PyGetWindow` (0.0.9 or higher)
- `pyperclip` (1.8.2 or higher)
- `tui_utilities` (1.9.17 or higher)
- `winrt-Windows.Foundation` (3.0 or higher)
- `winrt-Windows.Foundation.Collections` (3.0 or higher)
- `winrt-Windows.Graphics.Imaging` (3.0 or higher)
- `winrt-Windows.Media.Ocr` (3.0 or higher)
- `winrt-Windows.Storage.Streams` (3.0 or higher)

### **Python version**

Python (3.10 or higher)

### **Operating System**

- Windows 10 or higher.

---

## **Features**

### **Asynchronous Execution**

All hardware-bound actions (Mouse, Keyboard, Screen, Sound, System) can be queued and executed in the background using the `asynchronous` context manager. This allows you to perform operations concurrently without blocking the main thread. By returning `Self`, actions can be seamlessly chained.

```python
from advanced_automation_utilities import Mouse, Keyboard

# Queue multiple actions to run in the background
with Mouse().asynchronous() as mouse_task: Mouse().move(500, 500).click().scroll(1000)
with Keyboard().asynchronous() as keyboard_task: Keyboard().write("Hello World!")
# Wait for both tasks to complete synchronously
mouse_task.wait()
keyboard_task.wait()
mouse_task.cancel() # Cancel a running task
```

### **Physics (Human Simulation)**

Both **Mouse** and **Keyboard** actions are governed by highly configurable dataclasses (`MousePhysics` and `KeyboardPhysics`) designed to mimic human behavior perfectly. 

You can pass a custom physics object to their respective facades to alter their simulation parameters:
```python
from advanced_automation_utilities.mouse import MousePhysics, Mouse
from advanced_automation_utilities.keyboard import KeyboardPhysics, Keyboard

# Configure human-like Bézier curve mouse movements
mouse_physics = MousePhysics(
    speed = 1500,
    minimum_speed = 0,
    maximum_speed = 0,
    speed_variation = 0.1,
    duration = 0,
    duration_variation = 0,
    base_duration = 0.1,
    base_duration_variation = 0.1,
    inconsistency = 0.25,
    target_radius = 25,
    readjustment_duration_ratio = 0.25,
    click_delay = 0.05,
    click_delay_variation = 0.1,
    click_duration = 0.05,
    click_duration_variation = 0.1,
    scroll_speed = 1000,
    scroll_speed_variation = 0.1,
    scroll_duration = 0,
    scroll_duration_variation = 0,
    scroll_step = 120,
    scroll_pause_variation = 0.1
)
mouse = Mouse(mouse_physics)
# Configure advanced typing simulation with errors and delayed realizations
keyboard_physics = KeyboardPhysics(
    press_delay = 0.15,
    press_delay_variation = 0.5,
    press_duration = 0.05,
    press_duration_variation = 0.1,
    hotkey_delay = 0.01,
    hotkey_delay_variation = 0.5,
    typing_error_chance = 0.025,
    typing_error_correction_delay = 0.25,
    typing_error_correction_delay_variation = 0.5,
    typing_error_delayed_realization_chance = 0.5,
    auto_repeat = True
)
keyboard = Keyboard(keyboard_physics)
```

### **Mouse Utilities (mouse)**

**Native pointer manipulation with Bézier-curve physics for human-like behavior:**

- **MouseInfo().coordinates:** Gets the current (X, Y) coordinates of the pointer.
  ```python
  x, y = MouseInfo().coordinates
  ```
- **MouseInfo().x:** Gets the current X coordinate of the pointer.
  ```python
  x = MouseInfo().x
  ```
- **MouseInfo().y:** Gets the current Y coordinate of the pointer.
  ```python
  y = MouseInfo().y
  ```
- **MouseInfo().pixel_color():** Gets the RGB color of the pixel currently under the pointer.
  ```python
  r, g, b = MouseInfo().pixel_color()
  ```
- **MouseInfo().on_screen:** Checks if the pointer is currently within the bounds of any screen.
  ```python
  is_visible = MouseInfo().on_screen
  ```
- **Mouse().move():** Moves the pointer to the specified coordinates smoothly based on the configured physics.
  ```python
  Mouse().move(x = 250, y = 500)
  ```
- **Mouse().click():** Clicks the mouse at its current position or at specified coordinates.
  ```python
  Mouse().click()
  Mouse().click(x = 100, y = 200) # Moves before clicking
  ```
- **Mouse().double_click():** Performs a double click.
  ```python
  Mouse().double_click()
  ```
- **Mouse().right_click():** Performs a right click.
  ```python
  Mouse().right_click()
  ```
- **Mouse().middle_click():** Performs a middle click.
  ```python
  Mouse().middle_click()
  ```
- **Mouse().hold_click():** Holds down a mouse button.
  ```python
  Mouse().hold_click()
  ```
- **Mouse().release_click():** Releases a previously held mouse button.
  ```python
  Mouse().release_click()
  ```
- **Mouse().drag_and_drop():** Drags an item from start to end coordinates smoothly.
  ```python
  Mouse().drag_and_drop(start_x = 100, start_y = 100, end_x = 500, end_y = 500)
  ```
- **Mouse().scroll():** Scrolls the mouse wheel by the specified amount in the specified direction.
  ```python
  Mouse().scroll(amount = 1000, direction = "down")
  ```
- **Mouse().scroll_until():** Scrolls the mouse wheel continuously in the background until a given condition function evaluates to True, or an amount limit / timeout is reached.
  ```python
  # Scrolls down infinitely until the image is found
  Mouse().scroll_until(
    condition_function = lambda: KeyboardInfo().is_pressed("shift"),
    direction = "down"
  )
  ```
- **Mouse().wander():** Simulates idle mouse wandering by moving the pointer around randomly.
  ```python
  Mouse().wander(duration = 10)
  ```
- **Mouse().wander_until():** Simulates idle mouse wandering continuously in the background until a given condition function evaluates to True, or a maximum steps / timeout is reached.
  ```python
  # Wanders around infinitely until the image is found
  Mouse().wander_until(condition_function = lambda: KeyboardInfo().is_pressed("shift"))
  ```

### **Keyboard Utilities (keyboard)**

**Low-level keyboard interaction and information retrieval:**

- **KeyboardInfo().is_pressed():** Returns True if the specified key is currently physically pressed down.
  ```python
  is_shift_down = KeyboardInfo().is_pressed("shift")
  ```
- **Keyboard().press_key():** Presses and immediately releases a single key.
  ```python
  Keyboard().press_key("a")
  ```
- **Keyboard().hold_key():** Presses a key and holds it down.
  ```python
  Keyboard().hold_key("shift")
  ```
- **Keyboard().release_key():** Releases a previously held key.
  ```python
  Keyboard().release_key("shift")
  ```
- **Keyboard().hotkey():** Holds down a combination of keys and releases them in reverse order.
  ```python
  Keyboard().hotkey("ctrl", "c")
  ```
- **Keyboard().block_key():** Blocks all physical input from a specific key.
  ```python
  Keyboard().block_key("esc")
  ```
- **Keyboard().unblock_key():** Unblocks a previously blocked key.
  ```python
  Keyboard().unblock_key("esc")
  ```
- **Keyboard().write():** Types a string character by character with advanced, human-like typing error simulations, delays, and physics.
  ```python
  Keyboard().write("Hello, world!")
  ```

### **Screen Utilities (screen)**

**Advanced computer vision leveraging OpenCV and Windows OCR:**

- **ScreenInfo().resolution:** Gets the (width, height) resolution of the primary screen.
  ```python
  width, height = ScreenInfo().resolution
  ```
- **ScreenInfo().width:** Gets the width of the primary screen.
  ```python
  width = ScreenInfo().width
  ```
- **ScreenInfo().height:** Gets the height of the primary screen.
  ```python
  height = ScreenInfo().height
  ```
- **ScreenInfo().pixel_color():** Gets the RGB color of a specific pixel coordinate.
  ```python
  r, g, b = ScreenInfo().pixel_color(250, 500)
  ```
- **Screen().locate_image():** Searches for a template image on the screen and returns its central coordinates. Supports multi-monitor setups.
  ```python
  x, y = Screen().locate_image("button.png", monitor_index = 0)
  ```
- **Screen().locate_text():** Uses OCR to find specific text on the screen and returns its central coordinates. Supports multi-monitor setups.
  ```python
  x, y = Screen().locate_text("Submit", monitor_index = 0)
  ```
- **Screen().read_text():** Uses OCR to extract all readable text from the screen or a specific region. Supports multi-monitor setups.
  ```python
  text = Screen().read_text(monitor_index = 0)
  ```

### **Timing Utilities (timing)**

**Delays, chronometers, and condition-based execution flow:**

- **TimingInfo().time:** Gets the current time in seconds.
  ```python
  current_time = TimingInfo().time
  ```
- **Timing().wait():** Pauses execution for an exact amount of seconds.
  ```python
  Timing().wait(2.5)
  ```
- **Timing().wait_random():** Pauses execution for a random duration between two limits.
  ```python
  Timing().wait_random(minimum_duration = 1, maximum_duration = 3)
  ```
- **Timing().wait_until():** Halts execution until a given function or lambda condition evaluates to True.
  ```python
  # Waits until the shift key is pressed
  Timing().wait_until(lambda: KeyboardInfo().is_pressed("shift"))
  ```
- **Timing().measure_time():** A decorator to automatically measure and print the execution time of any function.
  ```python
  @measure_time
  def heavy_task(): pass
  ```

### **Sound Utilities (sound)**

**Audio playback and text-to-speech features:**

- **Sound().play_beep_sound():** Plays a motherboard beep with a specific frequency and duration.
  ```python
  Sound().play_beep_sound(frequency = 1000, duration = 0.5)
  ```
- **Sound().play_audio():** Plays an audio file from the file system.
  ```python
  Sound().play_audio("alert.wav")
  ```
- **Sound().play_system_sound():** Plays a default Windows system sound.
  ```python
  Sound().play_system_sound("warning")
  ```
- **Sound().speak():** Synthesizes text to speech using the default Windows voice.
  ```python
  Sound().speak("Hello, world!")
  ```

### **System Utilities (system)**

**High-level operating system actions and process management:**

- **SystemInfo().clipboard_text:** Gets the current text content of the Windows clipboard.
  ```python
  text = SystemInfo().clipboard_text
  ```
- **SystemInfo().active_window_title:** Gets the title of the currently focused/active window.
  ```python
  title = SystemInfo().active_window_title
  ```
- **SystemInfo().is_process_running():** Checks if a specific process is currently running.
  ```python
  is_running = SystemInfo().is_process_running("notepad.exe")
  ```
- **System().set_clipboard_text():** Sets the text content of the Windows clipboard.
  ```python
  System().set_clipboard_text("Text to paste later")
  ```
- **System().open_process():** Opens a process or file with optional arguments.
  ```python
  System().open_process("notepad.exe")
  ```
- **System().kill_process():** Terminates an active process by its name.
  ```python
  System().kill_process("notepad.exe", force = True)
  ```
- **System().focus_window():** Brings a specific window to the foreground by its title.
  ```python
  System().focus_window("Untitled - Notepad")
  ```
- **System().resize_window():** Resizes a specific window to the specified dimensions by its title.
  ```python
  System().resize_window("Untitled - Notepad", width = 800, height = 600)
  ```
- **System().move_window():** Moves a specific window to the specified coordinates by its title.
  ```python
  System().move_window("Untitled - Notepad", x = 100, y = 100)
  ```
- **System().close_window():** Gently closes a specific window by its title.
  ```python
  System().close_window("Untitled - Notepad")
  ```
- **System().enable_kill_switch():** Enables a global kill switch (Ctrl + Shift + Alt + K by default) to abort execution instantly.
  ```python
  System().enable_kill_switch()
  ```
- **System().disable_kill_switch():** Disables the global kill switch.
  ```python
  System().disable_kill_switch()
  ```
- **System().lock_screen():** Locks the Windows session (Win+L).
  ```python
  System().lock_screen()
  ```
- **System().sign_out():** Signs out the current Windows user.
  ```python
  System().sign_out()
  ```
- **System().sleep():** Puts the computer into sleep mode.
  ```python
  System().sleep()
  ```
- **System().hibernate():** Puts the computer into hibernation mode.
  ```python
  System().hibernate()
  ```
- **System().shutdown():** Turns off the computer.
  ```python
  System().shutdown()
  ```
- **System().restart():** Restarts the computer.
  ```python
  System().restart()
  ```

---

## **Installation**

```bash
pip install advanced_automation_utilities
```

---

## **Update**

```bash
pip install -U advanced_automation_utilities
```

---

## **Uninstall**

```bash
pip uninstall -y advanced_automation_utilities
```