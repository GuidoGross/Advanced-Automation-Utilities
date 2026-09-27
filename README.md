<div align = "center">

# **Advanced Automation Utilities**

[![Version](https://img.shields.io/pypi/v/advanced-automation-utilities?color=blue&labelColor=grey&label=Version&logo=data:image/svg%2bxml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA0NDggNTEyIj48cGF0aCBmaWxsPSJ3aGl0ZSIgZD0iTTAgODBWMjI5LjVjMCAxNyA2LjcgMzMuMyAxOC43IDQ1LjNsMTc2IDE3NmMyNSAyNSA2NS41IDI1IDkwLjUgMEw0MTguNyAzMTcuM2MyNS0yNSAyNS02NS41IDAtOTAuNWwtMTc2LTE3NmMtMTItMTItMjguMy0xOC43LTQ1LjMtMTguN0g0OEMyMS41IDMyIDAgNTMuNSAwIDgwem0xMTIgMzJhMzIgMzIgMCAxIDEgMCA2NCAzMiAzMiAwIDEgMSAwLTY0eiIvPjwvc3ZnPg==&logoColor=white&style=flat-square)](https://pypi.org/project/advanced-automation-utilities/)
[![Python Version](https://img.shields.io/badge/Python_version-%E2%89%A5_v3.10-blue?labelColor=grey&logo=python&logoColor=white&style=flat-square)](https://pypi.org/project/advanced-automation-utilities/)
[![Windows Version](https://img.shields.io/badge/Windows_version-%E2%89%A5_10-blue?labelColor=grey&logo=data:image/svg%2bxml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA4OCA4OCI+PHBhdGggZmlsbD0id2hpdGUiIGQ9Ik0wIDEyLjQgTDM1LjcgNy42IFY0MS42IEgwIFogTTM5LjYgNyBMODggMCBWNDEuNiBIMzkuNiBaIE0wIDQ2LjQgSDM1LjcgVjgwLjQgTDAgNzUuNiBaIE0zOS42IDQ2LjQgSDg4IFY4OCBMMzkuNiA4MSBaIi8+PC9zdmc+&logoColor=white&style=flat-square)](https://pypi.org/project/advanced-automation-utilities/)
[![Total Downloads](https://img.shields.io/pepy/dt/advanced-automation-utilities?color=blue&labelColor=grey&label=Total%20downloads&logo=data:image/svg%2bxml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA1MTIgNTEyIj48cGF0aCBmaWxsPSJ3aGl0ZSIgZD0iTTI4OCAzMmMwLTE3LjctMTQuMy0zMi0zMi0zMnMtMzIgMTQuMy0zMiAzMmwwIDI0Mi43LTczLjQtNzMuNGMtMTIuNS0xMi41LTMyLjgtMTIuNS00NS4zIDBzLTEyLjUgMzIuOCAwIDQ1LjNsMTI4IDEyOGMxMi41IDEyLjUgMzIuOCAxMi41IDQ1LjMgMGwxMjgtMTI4YzEyLjUtMTIuNSAxMi41LTMyLjggMC00NS4zcy0zMi44LTEyLjUtNDUuMyAwTDI4OCAyNzQuNyAyODggMzJ6TTY0IDM1MmMtMzUuMyAwLTY0IDI4LjctNjQgNjRsMCAzMmMwIDM1LjMgMjguNyA2NCA2NCA2NGwzODQgMGMzNS4zIDAgNjQtMjguNyA2NC02NGwwLTMyYzAtMzUuMy0yOC43LTY0LTY0LTY0bC0xMDEuNSAwLTQ1LjMgNDUuM2MtMjUgMjUtNjUuNSAyNS05MC41IDBMMTY1LjUgMzUyIDY0IDM1MnptMzY4IDU2YTI0IDI0IDAgMSAxIDAgNDggMjQgMjQgMCAxIDEgMC00OHoiLz48L3N2Zz4=&logoColor=white&style=flat-square)](https://pepy.tech/project/advanced-automation-utilities)

**A powerful, native Python library for Windows automation, featuring Context Manager-based asynchronous chaining, advanced human-like physics, and zero dependence on heavy GUI automation libraries. It leverages native `ctypes` hooks for maximum speed, security, and lower overhead.**

</div>

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

> [!NOTE]
> Standard library modules are used where possible; only external dependencies are listed.

- `mss` (v6.1.0 or higher)
- `numpy` (v1.21.0 or higher)
- `opencv-python` (v4.5.5 or higher)
- `psutil` (v5.8.0 or higher)
- `PyGetWindow` (v0.0.9 or higher)
- `pyperclip` (v1.8.2 or higher)
- `tui_utilities` (v1.9.17 or higher)
- `winrt-Windows.Foundation` (v3.0 or higher)
- `winrt-Windows.Foundation.Collections` (v3.0 or higher)
- `winrt-Windows.Graphics.Imaging` (v3.0 or higher)
- `winrt-Windows.Media.Ocr` (v3.0 or higher)
- `winrt-Windows.Storage.Streams` (v3.0 or higher)

### **Python version**

Python (v3.10 or higher)

### **Operating System**

Windows 10 or higher.

---

## **Installation**

- **Install:**
  ```bash
  pip install advanced_automation_utilities
  ```
- **Update:**
  ```bash
  pip install -U advanced_automation_utilities
  ```
- **Uninstall:**
  ```bash
  pip uninstall -y advanced_automation_utilities
  ```

---

## **Features**

### **Asynchronous Execution**

The library features a powerful Context Manager-based asynchronous execution system. All hardware-bound actions, such as Mouse, Keyboard, Screen, Sound, or System operations, can be seamlessly queued and executed in the background. This architecture allows you to perform heavy operations concurrently without blocking your main script's logic.

> [!TIP]
> All actions return `Self`, meaning they can be fluidly chained together. For instance, `Mouse().move(x, y).click()` queues both actions sequentially within the same background task. 

> [!NOTE]
> To fetch the return value of an action (such as a boolean from `scroll_until`), use `.last_result` at the end of a synchronous chain, or `.results` on the task object for asynchronous queues.

```python
from advanced_automation_utilities import Mouse, Keyboard

# Queue multiple actions to run in the background
mouse = Mouse()
keyboard = Keyboard()
with mouse.asynchronous() as mouse_task:
    mouse.move(500, 500).scroll_until(lambda: KeyboardInfo().is_pressed("shift"))
with keyboard.asynchronous() as keyboard_task: keyboard.write("Hello World!")
# Wait for both tasks to complete synchronously
mouse_task.wait()
keyboard_task.wait()
# Retrieve the return values of the queued actions in order
print(mouse_task.results) # E.g., [None, True]
# Or fetch it instantly in synchronous mode
result = Mouse().scroll_until(...).last_result 
```

### **Physics (Human Simulation)**

To evade bot-detection mechanisms and simulate real user interactions, both **Mouse** and **Keyboard** modules are governed by highly configurable, immutable dataclasses (`MousePhysics` and `KeyboardPhysics`). 

Mouse movements follow randomized Bézier curves with dynamic speeds and overshoots, while keyboard typing simulates human delays, keystroke variations, and even random typos with delayed corrections.

> [!TIP]
> Physics parameters are highly granular. You can pass a custom physics object to their respective facades to alter their simulation parameters dynamically.
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

<details open>
<summary><h3><b>Mouse Utilities (mouse)</b></h3></summary>

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

</details>

<details open>
<summary><h3><b>Keyboard Utilities (keyboard)</b></h3></summary>

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

</details>

<details open>
<summary><h3><b>Screen Utilities (screen)</b></h3></summary>

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

</details>

<details open>
<summary><h3><b>Timing Utilities (timing)</b></h3></summary>

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
- **@measure_time:** A decorator to automatically measure and print the execution time of any function.
  ```python
  @measure_time
  def heavy_task(): pass
  ```

</details>

<details open>
<summary><h3><b>Sound Utilities (sound)</b></h3></summary>

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

</details>

<details open>
<summary><h3><b>System Utilities (system)</b></h3></summary>

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
- **System().open_process():** Opens a process or file.
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

</details>