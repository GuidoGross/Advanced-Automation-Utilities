<div align = "center">

# **Advanced Automation Utilities**

[![Version](https://img.shields.io/pypi/v/advanced-automation-utilities?color=blue&labelColor=grey&label=Version&logo=data:image/svg%2bxml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA0NDggNTEyIj48cGF0aCBmaWxsPSJ3aGl0ZSIgZD0iTTAgODBWMjI5LjVjMCAxNyA2LjcgMzMuMyAxOC43IDQ1LjNsMTc2IDE3NmMyNSAyNSA2NS41IDI1IDkwLjUgMEw0MTguNyAzMTcuM2MyNS0yNSAyNS02NS41IDAtOTAuNWwtMTc2LTE3NmMtMTItMTItMjguMy0xOC43LTQ1LjMtMTguN0g0OEMyMS41IDMyIDAgNTMuNSAwIDgwem0xMTIgMzJhMzIgMzIgMCAxIDEgMCA2NCAzMiAzMiAwIDEgMSAwLTY0eiIvPjwvc3ZnPg==&logoColor=white&style=flat-square)](https://pypi.org/project/advanced-automation-utilities/)
[![Python Version](https://img.shields.io/badge/Python_version-%E2%89%A5_v3.10-blue?labelColor=grey&logo=python&logoColor=white&style=flat-square)](https://www.python.org/downloads/)
[![Windows Version](https://img.shields.io/badge/Windows_version-%E2%89%A5_10-blue?labelColor=grey&logo=data:image/svg%2bxml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA4OCA4OCI+PHBhdGggZmlsbD0id2hpdGUiIGQ9Ik0wIDEyLjQgTDM1LjcgNy42IFY0MS42IEgwIFogTTM5LjYgNyBMODggMCBWNDEuNiBIMzkuNiBaIE0wIDQ2LjQgSDM1LjcgVjgwLjQgTDAgNzUuNiBaIE0zOS42IDQ2LjQgSDg4IFY4OCBMMzkuNiA4MSBaIi8+PC9zdmc+&logoColor=white&style=flat-square)](https://www.microsoft.com/software-download/windows10)
[![Total Downloads](https://img.shields.io/pepy/dt/advanced-automation-utilities?color=blue&labelColor=grey&label=Total%20downloads&logo=data:image/svg%2bxml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA1MTIgNTEyIj48cGF0aCBmaWxsPSJ3aGl0ZSIgZD0iTTI4OCAzMmMwLTE3LjctMTQuMy0zMi0zMi0zMnMtMzIgMTQuMy0zMiAzMmwwIDI0Mi43LTczLjQtNzMuNGMtMTIuNS0xMi41LTMyLjgtMTIuNS00NS4zIDBzLTEyLjUgMzIuOCAwIDQ1LjNsMTI4IDEyOGMxMi41IDEyLjUgMzIuOCAxMi41IDQ1LjMgMGwxMjgtMTI4YzEyLjUtMTIuNSAxMi41LTMyLjggMC00NS4zcy0zMi44LTEyLjUtNDUuMyAwTDI4OCAyNzQuNyAyODggMzJ6TTY0IDM1MmMtMzUuMyAwLTY0IDI4LjctNjQgNjRsMCAzMmMwIDM1LjMgMjguNyA2NCA2NCA2NGwzODQgMGMzNS4zIDAgNjQtMjguNyA2NC02NGwwLTMyYzAtMzUuMy0yOC43LTY0LTY0LTY0bC0xMDEuNSAwLTQ1LjMgNDUuM2MtMjUgMjUtNjUuNSAyNS05MC41IDBMMTY1LjUgMzUyIDY0IDM1MnptMzY4IDU2YTI0IDI0IDAgMSAxIDAgNDggMjQgMjQgMCAxIDEgMC00OHoiLz48L3N2Zz4=&logoColor=white&style=flat-square)](https://pepy.tech/project/advanced-automation-utilities)

**A powerful, native Python library for Windows automation, featuring Context Manager-based asynchronous chaining, advanced human-like physics, and zero dependence on heavy automation libraries. It leverages native `ctypes` hooks for maximum speed, security, and lower overhead.**
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

### **Asynchronous execution**

The library features a powerful Context Manager-based asynchronous execution system. All hardware-bound actions, such as Mouse, Keyboard, Screen, Sound, or System operations, can be seamlessly queued and executed in the background. This architecture allows you to perform heavy operations concurrently without blocking your main script's logic.

> [!TIP]
> All actions return `Self`, meaning they can be fluidly chained together. For instance, `Mouse().move(x, y).click()` queues both actions sequentially within the same background task. 

> [!NOTE]
> To fetch the return value of an action (such as a boolean from `scroll_until`), use `.last_result` at the end of a synchronous chain, or `.results` on the task object for asynchronous queues.

```python
mouse = Mouse()
with mouse.asynchronous() as mouse_task:
    mouse.move(x = 500, y = 500).scroll_until(
        condition_function = lambda: KeyboardInfo().is_pressed(key = "shift"),
        amount = 1000,
        direction = "down",
        timeout = 5,
        poll_interval = 0.1
    )
keyboard = Keyboard()
with keyboard.asynchronous() as keyboard_task: keyboard.write(text = "Hello World!")
mouse_task.wait()
keyboard_task.wait()
print(mouse_task.results)
result = Mouse().scroll_until(
    condition_function = lambda: KeyboardInfo().is_pressed(key = "shift"),
    amount = 1000,
    direction = "down",
    timeout = 5,
    poll_interval = 0.1
).last_result
print(result)
```

### **Physics (human simulation)**

To evade bot-detection mechanisms and simulate real user interactions, both **Mouse** and **Keyboard** modules are governed by highly configurable, immutable dataclasses (`MousePhysics` and `KeyboardPhysics`). 

Mouse movements follow randomized Bézier curves with dynamic speeds and overshoots, while keyboard typing simulates human delays, keystroke variations, and even random typos with delayed corrections.

> [!TIP]
> Physics parameters are highly granular. You can pass a custom physics object to their respective facades to alter their simulation parameters dynamically.

```python
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

- **Mouse().move():** Moves the pointer to the specified coordinates smoothly based on the configured physics.
  
  **Description:**
  
  Generates a realistic Bézier curve from the current pointer location to the target. The trajectory, speed, and overshoots are governed by `MousePhysics`.
  
  **Arguments:**

  - **`x` (`int`)**
  - **`y` (`int`)**

  **Returns:**

  **`Self`**

  **Example:**
  
  ```python
  Mouse().move(x = 250, y = 500)
  ```

> [!NOTE]
> Because it uses Bézier curves, the mouse will naturally curve and accelerate/decelerate just like a real human hand.

- **Mouse().click():** Clicks the mouse at specified coordinates.
  
  **Description:**
  
  Simulates a physical click (DOWN and UP events) with a customizable, randomized delay in between.
  
  **Arguments:**

  - **`x` (`Optional[int]`):** Must be >= 0 and <= screen width.
  - **`y` (`Optional[int]`):** Must be >= 0 and <= screen height.
  - **`button` (`str`):** Valid options: "left", "right", "middle".

  **Returns:**

  **`Self`**

  **Example:**
  
  ```python
  Mouse().click(x = 250, y = 500, button = "left", clicks = 1)
  ```

> [!TIP]
> Passing `x` and `y` automatically moves the pointer to that location before clicking. It is exactly equivalent to `Mouse().move(x, y).click()`.

- **Mouse().double_click():** Performs a double click at specified coordinates.
  
  **Description:**
  
  A convenient wrapper around `click()` that forces `clicks = 2`.
  
  **Arguments:**

  - **`x` (`Optional[int]`):** Must be >= 0 and <= screen width.
  - **`y` (`Optional[int]`):** Must be >= 0 and <= screen height.
  - **`button` (`str`):** Valid options: "left", "right", "middle".

  **Returns:**

  **`Self`**

  **Example:**
  
  ```python
  Mouse().double_click(x = 250, y = 500, button = "left")
  ```

- **Mouse().right_click():** Performs a right click at specified coordinates.
  
  **Description:**
  
  A convenient wrapper around `click()` that forces `button = "right"`.
  
  **Arguments:**

  - **`x` (`Optional[int]`):** Must be >= 0 and <= screen width.
  - **`y` (`Optional[int]`):** Must be >= 0 and <= screen height.

  **Returns:**

  **`Self`**

  **Example:**
  
  ```python
  Mouse().right_click(x = 250, y = 500, clicks = 1)
  ```

- **Mouse().middle_click():** Performs a middle click at specified coordinates.
  
  **Description:**
  
  A convenient wrapper around `click()` that forces `button = "middle"`.
  
  **Arguments:**

  - **`x` (`Optional[int]`):** Must be >= 0 and <= screen width.
  - **`y` (`Optional[int]`):** Must be >= 0 and <= screen height.

  **Returns:**

  **`Self`**

  **Example:**
  
  ```python
  Mouse().middle_click(x = 100, y = 200, clicks = 1)
  ```

- **Mouse().hold_click():** Holds down a mouse button at specified coordinates.
  
  **Description:**
  
  Sends the physical DOWN signal for the mouse button without releasing it.
  
  **Arguments:**

  - **`x` (`Optional[int]`):** Must be >= 0 and <= screen width.
  - **`y` (`Optional[int]`):** Must be >= 0 and <= screen height.
  - **`button` (`str`):** Valid options: "left", "right", "middle".

  **Returns:**

  **`Self`**

  **Example:**
  
  ```python
  Mouse().hold_click(x = 250, y = 500, button = "left")
  ```

> [!WARNING]
> Always ensure you eventually call `release_click()` to avoid leaving the system in a locked state.

- **Mouse().release_click():** Releases a previously held mouse button at specified coordinates.
  
  **Description:**
  
  Sends the physical UP signal for the mouse button.
  
  **Arguments:**

  - **`x` (`Optional[int]`):** Must be >= 0 and <= screen width.
  - **`y` (`Optional[int]`):** Must be >= 0 and <= screen height.
  - **`button` (`str`):** Valid options: "left", "right", "middle".

  **Returns:**

  **`Self`**

  **Example:**
  
  ```python
  Mouse().release_click(x = 250, y = 500, button = "left")
  ```

- **Mouse().drag_and_drop():** Drags an item from start to end coordinates smoothly, based on the configured physics.
  
  **Description:**
  
  Moves to the start coordinates, holds the specified button, waits, smoothly moves to the end coordinates, waits again, and releases the button.
  
  **Arguments:**

  - **`start_x` (`int`)**
  - **`start_y` (`int`)**
  - **`end_x` (`int`)**
  - **`end_y` (`int`)**
  - **`button` (`str`):** Valid options: "left", "right", "middle".

  **Returns:**

  **`Self`**

  **Example:**
  
  ```python
  Mouse().drag_and_drop(start_x = 250, start_y = 500, end_x = 750, end_y = 250, button = "left")
  ```

> [!NOTE]
> Short pauses are automatically inserted before moving and before releasing to simulate a human confirming the grab and drop actions.

- **Mouse().scroll():** Scrolls the mouse wheel by the specified amount in the specified direction.
  
  **Description:**
  
  Sends discrete mouse wheel signals to scroll the active window.
  
  **Arguments:**

  - **`amount` (`int`):** Must be >= 0.
  - **`direction` (`str`):** Valid options: "up", "down", "left", "right".

  **Returns:**

  **`Self`**

  **Example:**
  
  ```python
  Mouse().scroll(amount = 1000, direction = "down")
  ```

- **Mouse().scroll_until():** Scrolls the mouse wheel continuously until a condition is met.
  
  **Description:**
  
  Executes in a loop, scrolling step by step while periodically until either the `condition_function` is met or the `amount`/`timeout` is reached.
  
  **Arguments:**

  - **`condition_function` (`Callable[[], bool]`)**
  - **`amount` (`int`)**
  - **`direction` (`str`):** Valid options: "up", "down", "left", "right".
  - **`timeout` (`float`)**
  - **`poll_interval` (`float`)**

  **Returns:**

  **`Self`**

  **Example:**
  
  ```python
  Mouse().scroll_until(
      condition_function = lambda: KeyboardInfo().is_pressed("shift"),
      amount = 1000,
      direction = "down",
      timeout = 5,
      poll_interval = 0.1
  )
  ```

- **Mouse().wander():** Simulates idle mouse wandering by moving the pointer around randomly.
  
  **Description:**
  
  Generates erratic but smooth Bézier movements around a specific region, to keep the computer awake or simulate idle human activity.
  
  **Arguments:**

  - **`duration` (`float`):** Seconds. Must be >= 0.
  - **`region` (`Optional[tuple[int, int, int, int]]`):** Format: (left, top, right, bottom).
  - **`maximum_steps` (`Optional[int]`):** Must be >= 0.

  **Returns:**

  **`Self`**

  **Example:**
  
  ```python
  Mouse().wander(duration = 10, region = (250, 250, 500, 500), maximum_steps = 3)
  ```

> [!NOTE]
> Although random, the movements generally tend toward the center of the region.

- **Mouse().wander_until():** Simulates idle mouse wandering continuously until a condition is met.
  
  **Description:**
  
  Executes the wander logic until the `condition_function` is met or the `maximum_steps`/`timeout` is reached.
  
  **Arguments:**

  - **`condition_function` (`Callable[[], bool]`)**
  - **`region` (`Optional[tuple[int, int, int, int]]`):** Format: (left, top, right, bottom).
  - **`maximum_steps` (`Optional[int]`):** Must be >= 0.
  - **`timeout` (`float`)**
  - **`poll_interval` (`float`)**

  **Returns:**

  **`Self`**

  **Example:**
  
  ```python
  Mouse().wander_until(
      condition_function = lambda: KeyboardInfo().is_pressed("shift"),
      region = (250, 250, 500, 500),
      maximum_steps = 3,
      timeout = 5,
      poll_interval = 0.1
  )
  ```

- **MouseInfo().coordinates:** Gets the current (X, Y) coordinates of the pointer.
  
  **Description:**
  
  Reads the system's pointer position and returns it as a tuple. This is an instantaneous, non-blocking hardware read.
  
  **Returns:**

  **`tuple[int, int]`:** Format: (x, y).

  **Example:**
  
  ```python
  x, y = MouseInfo().coordinates
  ```

- **MouseInfo().x:** Gets the current X coordinate of the pointer.
  
  **Description:**
  
  Reads the system's pointer position and extracts only the horizontal axis value.
  
  **Returns:**

  **`int`**

  **Example:**
  
  ```python
  x = MouseInfo().x
  ```

- **MouseInfo().y:** Gets the current Y coordinate of the pointer.
  
  **Description:**
  
  Reads the system's pointer position and extracts only the vertical axis value.
  
  **Returns:**

  **`int`**

  **Example:**
  
  ```python
  y = MouseInfo().y
  ```

- **MouseInfo().pixel_color():** Gets the RGB or hexadecimal color of the pixel currently under the pointer.
  
  **Description:**
  
  Takes a micro-screenshot of the exact pixel the mouse is hovering over and extracts its color.
  
  **Arguments:**

  - **`format` (`str`):** Valid options: "rgb", "hexadecimal".

  **Returns:**

  **`tuple[int, int, int]` | `str`**

  **Example:**
  
  ```python
  color = MouseInfo().pixel_color(format = "rgb")
  ```

- **MouseInfo().on_screen:** Checks if the pointer is currently within the bounds of any screen.
  
  **Description:**
  
  Verifies if the current mouse coordinates fall inside the desktop's virtual screen boundaries. Useful for multi-monitor setups.
  
  **Returns:**

  **`bool`**

  **Example:**
  
  ```python
  is_pointer_on_screen = MouseInfo().on_screen
  ```

### **Keyboard Utilities (keyboard)**

**Low-level keyboard interaction and information retrieval:**

- **Keyboard().press_key():** Presses and releases a single key.
  
  **Description:**
  
  Sends a physical DOWN signal followed instantly by an UP signal for the specified key.
  
  **Arguments:**

  - **`key` (`str`)**

  **Returns:**

  **`Self`**

  **Example:**
  
  ```python
  Keyboard().press_key(key = "a")
  ```

- **Keyboard().hold_key():** Holds a key down.
  
  **Description:**
  
  Sends a physical DOWN signal for the key without releasing it.
  
  **Arguments:**

  - **`key` (`str`)**

  **Returns:**

  **`Self`**

  **Example:**
  
  ```python
  Keyboard().hold_key(key = "shift")
  ```

> [!WARNING]
> Make sure to call `release_key()` to prevent the key from getting physically stuck.

- **Keyboard().release_key():** Releases a previously held key.
  
  **Description:**
  
  Sends the physical UP signal for the key.
  
  **Arguments:**

  - **`key` (`str`)**

  **Returns:**

  **`Self`**

  **Example:**
  
  ```python
  Keyboard().release_key(key = "shift")
  ```

- **Keyboard().hotkey():** Holds down a combination of keys and releases them in reverse order.
  
  **Description:**
  
  Sequentially holds all provided keys with a tiny human delay between each, waits for a moment, and then releases them in reverse to ensure the OS registers the shortcut properly.
  
  **Arguments:**

  - **`*keys` (`str`)**

  **Returns:**

  **`Self`**

  **Example:**
  
  ```python
  Keyboard().hotkey("ctrl", "shift", "esc")
  ```

- **Keyboard().block_key():** Blocks all physical input from a specific key.
  
  **Description:**
  
  Uses a low-level C hook to intercept and discard any hardware events from this key. Useful for preventing user interference during automation.
  
  **Arguments:**

  - **`key` (`str`)**

  **Returns:**

  **`Self`**

  **Example:**
  
  ```python
  Keyboard().block_key(key = "esc")
  ```

> [!TIP]
> This blocks PHYSICAL input. The script can still simulate presses for this key perfectly fine.

- **Keyboard().unblock_key():** Unblocks a previously blocked key.
  
  **Description:**
  
  Restores physical input functionality for the key.
  
  **Arguments:**

  - **`key` (`str`)**

  **Returns:**

  **`Self`**

  **Example:**
  
  ```python
  Keyboard().unblock_key(key = "esc")
  ```

- **Keyboard().write():** Types a string character by character with advanced, human-like typing error simulations and delays, based on the configured physics.
  
  **Description:**
  
  Rather than instantly pasting text, this method allows the user to simulate a human typing on a keyboard. It can even make random typos, realize the mistake a few characters later, hit backspace to fix it, and resume typing.
  
  **Arguments:**

  - **`text` (`str`)**

  **Returns:**

  **`Self`**

  **Example:**
  
  ```python
  Keyboard().write(text = "Hello, world!")
  ```

- **KeyboardInfo().is_pressed():** Returns True if the specified key is currently physically held down.
  
  **Description:**
  
  Reads the hardware state asynchronously, capturing even keys pressed outside the script.
  
  **Arguments:**

  - **`key` (`str`)**

  **Returns:**

  **`bool`**

  **Example:**
  
  ```python
  is_shift_down = KeyboardInfo().is_pressed(key = "shift")
  ```

### **Screen Utilities (screen)**

**Advanced computer vision leveraging OpenCV and Windows OCR:**

- **Screen().locate_image():** Searches for a template image on the screen and returns its central coordinates.
  
  **Description:**
  
  Takes a fast screenshot and uses OpenCV Template Matching (`TM_CCOEFF_NORMED`) to find the image in the specified region.
  
  **Arguments:**

  - **`image_path` (`str`):** Must be a valid file path.
  - **`confidence` (`float`):** Must be >= 0 and <= 1.
  - **`region` (`Optional[tuple[int, int, int, int]]`):** Format: (left, top, right, bottom). Values must be >= 0 and <= screen width/height.
  - **`monitor_index` (`int`)**

  **Returns:**

  **`tuple[Optional[int], Optional[int]]`:** Format: (x, y).

  **Example:**
  
  ```python
  x, y = Screen().locate_image(
      image_path = "button.png",
      confidence = 0.9,
      region = (250, 250, 500, 500),
      monitor_index = 0
  )
  ```

- **Screen().locate_text():** Uses OCR to find specific text on the screen and returns its central coordinates.
  
  **Description:**
  
  Leverages the blazing-fast native Windows OCR API to find the location of specific text within the specified region.
  
  **Arguments:**

  - **`text` (`str`)**
  - **`region` (`Optional[tuple[int, int, int, int]]`):** Format: (left, top, right, bottom). Values must be >= 0 and <= screen width/height.
  - **`exact_match` (`bool`)**
  - **`monitor_index` (`int`)**

  **Returns:**

  **`tuple[Optional[int], Optional[int]]`**

  **Example:**
  
  ```python
  x, y = Screen().locate_text(
      text = "Submit",
      region = (250, 250, 500, 500),
      exact_match = True,
      monitor_index = 0
  )
  ```

- **Screen().read_text():** Uses OCR to extract all readable text from the screen or a specific region.
  
  **Description:**

  Leverages the blazing-fast native Windows OCR API to extract all readable text from the screen or a specific region.

  **Arguments:**

  - **`region` (`Optional[tuple[int, int, int, int]]`):** Format: (left, top, right, bottom). Values must be >= 0 and <= screen width/height.
  - **`monitor_index` (`int`)**

  **Returns:**

  **`str`**

  **Example:**
  
  ```python
  text = Screen().read_text(region = (250, 250, 500, 500), monitor_index = 0)
  ```

- **ScreenInfo().resolution:** Gets the resolution of the primary screen.

  **Description:**

  Returns the resolution of the primary screen as a tuple.

  **Returns:**

  **`tuple[int, int]`:** Format: (width, height).

  **Example:**
  
  ```python
  width, height = ScreenInfo().resolution
  ```

- **ScreenInfo().width:** Gets the width of the primary screen.

  **Description:**

  Returns only the width of the primary screen as an integer.

  **Returns:**

  **`int`**

  **Example:**
  
  ```python
  width = ScreenInfo().width
  ```

- **ScreenInfo().height:** Gets the height of the primary screen.

  **Description:**

  Returns only the height of the primary screen as an integer.

  **Returns:**

  **`int`**

  **Example:**
  
  ```python
  height = ScreenInfo().height
  ```

- **ScreenInfo().pixel_color():** Gets the RGB or hexadecimal color of a specific pixel coordinate.
  
  **Description:**

  Returns the color of the pixel at the specified coordinates on RGB or hexadecimal format.

  **Arguments:**

  - **`x` (`int`)**
  - **`y` (`int`)**
  - **`format` (`str`):** Valid options: "rgb", "hexadecimal".

  **Returns:**

  **`Union[tuple[int, int, int], str]`:** Format: (R, G, B) for "rgb" or "#RRGGBB" for "hexadecimal".

  **Example:**
  
  ```python
  color = ScreenInfo().pixel_color(x = 250, y = 500, format = "hexadecimal")
  ```

### **Timing Utilities (timing)**

**Delays, chronometers, and condition-based execution flow:**

- **Timing().wait():** Pauses execution for an exact amount of seconds.

  **Description:**

  Pauses execution for an exact amount of seconds. It acts as a safe, responsive wrapper around standard sleep mechanisms, ensuring that long pauses can still be instantly interrupted if the global kill switch is triggered.

  **Arguments:**

  - **`duration` (`float`):** Seconds. Must be >= 0.

  **Returns:**

  **`None`**

  **Example:**
  
  ```python
  Timing().wait(duration = 2.5)
  ```

> [!NOTE]
> This internally uses the global `KILL_SWITCH_EVENT`, meaning if the Kill Switch is triggered during a wait, the wait is aborted instantly.

- **Timing().wait_random():** Pauses execution for a random duration between two limits.

  **Description:**

  Pauses execution for a random duration between two limits. This is particularly useful for simulating human unpredictability and preventing strict pattern recognition in automated tasks.

  **Arguments:**

  - **`minimum_duration` (`float`):** Seconds. Must be >= 0.
  - **`maximum_duration` (`float`):** Seconds. Must be >= 0.

  **Returns:**

  **`None`**

  **Example:**
  
  ```python
  Timing().wait_random(minimum_duration = 1, maximum_duration = 3)
  ```

- **Timing().wait_until():** Pauses execution until a given condition function is met.
  
  **Description:**
  
  Continuously polls the condition function at a specified interval until is met or the timeout is reached.
  
  **Arguments:**

  - **`condition_function` (`Callable[[], bool]`)**
  - **`timeout` (`float`):** Seconds. Must be >= 0.
  - **`poll_interval` (`float`):** Seconds. Must be > 0.

  **Returns:**

  **`bool`**

  **Example:**
  
  ```python
  Timing().wait_until(
      condition_function = lambda: KeyboardInfo().is_pressed("shift"),
      timeout = 10,
      poll_interval = 0.1
  )
  ```

- **TimingInfo().time:** Gets the current time in seconds.
  
  **Description:**
  
  Utilizes the high-resolution performance counter (`time.perf_counter`) to get the current time in seconds.
  
  **Returns:**

  **`float`**

  **Example:**
  
  ```python
  current_time = TimingInfo().time
  ```

- **@measure_time:** A decorator to automatically measure and print the execution time of any function.
  
  **Description:**
  
  Place this above your function definitions to measure their execution time.
  
  **Example:**
  
  ```python
  @measure_time
  def heavy_task(): pass
  ```

### **Sound Utilities (sound)**

**Audio playback and text-to-speech features:**

- **Sound().play_beep_sound():** Plays a motherboard beep with a specific frequency and duration.

  **Description:**

  Plays a beep sound using the Windows API. Useful for audible notifications.
  
  **Arguments:**

  - **`frequency` (`int`):** Must be between 37 and 32767.
  - **`duration` (`float`):** Seconds. Must be > 0.

  **Returns:**

  **`Self`**

  **Example:**
  
  ```python
  Sound().play_beep_sound(frequency = 1000, duration = 0.5)
  ```

- **Sound().play_audio():** Plays an audio file from the file system.
  
  **Description:**
  
  Uses the native Windows MCI API for lightweight audio playback.
  
  **Arguments:**

  - **`file_path` (`str`)**

  **Returns:**

  **`Self`**

  **Example:**
  
  ```python
  Sound().play_audio(file_path = "alert.wav")
  ```

- **Sound().play_system_sound():** Plays a default Windows system sound.

  **Description:**

  Plays a default Windows system sound between the given options.
  
  **Arguments:**

  - **`sound_type` (`str`):** Valid options: "info", "warning", "error", "question", "ok".

  **Returns:**

  **`Self`**

  **Example:**
  
  ```python
  Sound().play_system_sound(sound_type = "warning")
  ```

- **Sound().speak():** Synthesizes text to speech using the default Windows voice.
  
  **Description:**
  
  Uses native PowerShell SAPI integration for zero-dependency TTS to synthesize text to speech.
  
  **Arguments:**

  - **`text` (`str`)**

  **Returns:**

  **`Self`**

  **Example:**
  
  ```python
  Sound().speak(text = "Automation task completed successfully.")
  ```

### **System Utilities (system)**

**High-level operating system actions and process management:**

- **System().set_clipboard_text():** Sets the text content of the Windows clipboard.

  **Description:**

  Sets the text content of the Windows clipboard. This is extremely useful for automating copy-paste workflows or seamlessly transferring data from your script to other applications.
  
  **Arguments:**

  - **`text` (`str`)**

  **Returns:**

  **`Self`**

  **Example:**
  
  ```python
  System().set_clipboard_text(text = "Text to paste later.")
  ```

- **System().open_process():** Opens a process or file.
  
  **Description:**
  
  Uses `os.startfile` internally to launch applications or open files with their default program.
  
  **Arguments:**

  - **`executable_path` (`str`)**

  **Returns:**

  **`Self`**

  **Example:**
  
  ```python
  System().open_process(process_path = "notepad.exe")
  ```

- **System().kill_process():** Terminates an active process by its name.

  **Description:**

  Terminates an active process by its name. This provides a robust way to clean up applications after an automation task finishes, or to forcefully close unresponsive programs.
  
  **Arguments:**

  - **`process` (`str`)**
  - **`force` (`bool`)**

  **Returns:**

  **`Self`**

  **Example:**
  
  ```python
  System().kill_process(process = "notepad.exe", force = True)
  ```

- **System().focus_window():** Brings a specific window to the foreground by its title.

  **Description:**

  Brings a specific window to the foreground by its title. This is essential for ensuring that subsequent mouse clicks and keyboard strokes are sent to the correct application, avoiding accidental interactions with background apps.
  
  **Arguments:**

  - **`window_title` (`str`)**

  **Returns:**

  **`Self`**

  **Example:**
  
  ```python
  System().focus_window(window_title = "Untitled - Notepad")
  ```

- **System().resize_window():** Resizes a specific window to the specified dimensions by its title.

  **Description:**

  Resizes a specific window to the specified dimensions by its title. This is extremely useful for automating GUI applications or ensuring that a window occupies the exact screen space required for subsequent automation steps.
  
  **Arguments:**

  - **`window_title` (`str`)**
  - **`width` (`int`):** Must be > 0.
  - **`height` (`int`):** Must be > 0.

  **Returns:**

  **`Self`**

  **Example:**
  
  ```python
  System().resize_window(window_title = "Untitled - Notepad", width = 800, height = 600)
  ```

- **System().move_window():** Moves a specific window to the specified coordinates by its title.

  **Description:**

  Moves a specific window to the specified coordinates by its title. Similar to `resize_window()`, this helps guarantee that your automation target is perfectly positioned before executing coordinate-based mouse interactions.
  
  **Arguments:**

  - **`window_title` (`str`)**
  - **`x` (`int`)**
  - **`y` (`int`)**

  **Returns:**

  **`Self`**

  **Example:**
  
  ```python
  System().move_window(window_title = "Untitled - Notepad", x = 250, y = 500)
  ```

- **System().close_window():** Gently closes a specific window by its title.
  
  **Description:**
  
  Sends a graceful WM_CLOSE signal to a specific window by its title.
  
  **Arguments:**

  - **`window_title` (`str`)**

  **Returns:**

  **`Self`**

  **Example:**
  
  ```python
  System().close_window(window_title = "Untitled - Notepad")
  ```

- **System().lock_screen():** Locks the Windows session (Win+L).

  **Description:**

  Locks the Windows session (equivalent to pressing Win+L). This is ideal for scripts that handle sensitive information and need to secure the computer immediately after the automated task finishes.
  
  **Returns:**

  **`Self`**

  **Example:**
  
  ```python
  System().lock_screen()
  ```

- **System().sign_out():** Signs out the current Windows user.

  **Description:**

  Signs out the current Windows user. This gently closes all running applications and returns to the Windows login screen, making it useful for gracefully ending a day's worth of automated tasks.
  
  **Returns:**

  **`Self`**

  **Example:**
  
  ```python
  System().sign_out()
  ```

- **System().sleep():** Puts the computer into sleep mode.

  **Description:**

  Puts the computer into sleep mode (suspend to RAM). This is a great way to save energy when an automation task finishes running overnight without completely turning off the machine.

  **Returns:**

  **`Self`**

  **Example:**
  
  ```python
  System().sleep()
  ```

- **System().hibernate():** Puts the computer into hibernation mode.

  **Description:**

  Puts the computer into hibernation mode (suspend to disk). This completely powers off the machine while saving the exact state of all open applications, allowing you to seamlessly resume your work later.
  
  **Returns:**

  **`Self`**

  **Example:**
  
  ```python
  System().hibernate()
  ```

- **System().shutdown():** Turns off the computer.
  
  **Description:**

  Turns off the computer, optionally waiting for a specified delay before powering down. This is perfect for cleanly shutting down a remote or unattended machine after a long-running automation process finishes.
  
  **Arguments:**

  - **`delay` (`int`):** Seconds. Must be >= 0.

  **Returns:**

  **`Self`**

  **Example:**
  
  ```python
  System().shutdown(delay = 60)
  ```

- **System().restart():** Restarts the computer.

  **Description:**

  Restarts the computer, optionally waiting for a specified delay before rebooting. This is useful for applying system updates or resetting the environment before starting a fresh automation cycle.
  
  **Arguments:**

  - **`delay` (`int`):** Seconds. Must be >= 0.

  **Returns:**

  **`Self`**

  **Example:**
  
  ```python
  System().restart(delay = 60)
  ```

- **System().enable_kill_switch():** Enables a global kill switch to abort execution instantly.
  
  **Description:**
  
  Injects a high-priority hardware hook to listen for the abort shortcut.
  
  **Arguments:**

  - **`*keys` (`str`)**

  **Returns:**

  **`Self`**

  **Example:**
  
  ```python
  System().enable_kill_switch("ctrl", "shift", "alt", "k")
  ```

> [!IMPORTANT]
> When triggered, an asynchronous `KillSwitchTriggered` exception is raised in all automation threads, completely aborting execution safely.

- **System().disable_kill_switch():** Disables the global kill switch.
  
  **Description:**
  
  Safely unregisters the hook to disable the kill switch.
  
  **Returns:**

  **`Self`**

  **Example:**
  
  ```python
  System().disable_kill_switch()
  ```

- **SystemInfo().clipboard_text:** Gets the current text content of the Windows clipboard.

  **Description:**

  Gets the current text content of the Windows clipboard. This allows your scripts to seamlessly read and process text that the user or other applications have recently copied.
  
  **Returns:**

  **`str`**

  **Example:**
  
  ```python
  text = SystemInfo().clipboard_text
  ```

- **SystemInfo().active_window_title:** Gets the title of the currently focused/active window.

  **Description:**

  Gets the title of the currently focused/active window. This allows your scripts to interact with the active window or to determine which application the user is currently using.
  
  **Returns:**

  **`str`**

  **Example:**
  
  ```python
  title = SystemInfo().active_window_title
  ```

- **SystemInfo().is_process_running():** Checks if a specific process is currently running.

  **Description:**

  Checks if a specific process is currently running. This allows your scripts to determine if an application is active or not.
  
  **Arguments:**

  - **`process` (`str`)**

  **Returns:**

  **`bool`**

  **Example:**
  
  ```python
  is_running = SystemInfo().is_process_running(process = "notepad.exe")
  ```