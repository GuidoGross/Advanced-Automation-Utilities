**[Home](Home)** ➔ **[Keyboard](Keyboard)**

<div align = "center">

# **Keyboard**

**Low-level keyboard interaction and hardware state retrieval. Simulates human typing with configurable physics, handles complex hotkey combinations, and can selectively block physical hardware inputs to prevent interference during critical automation tasks.**

</div>

---

### **`Keyboard().press_key()`**

Presses and releases a single key.

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

---

### **`Keyboard().hold_key()`**

Holds a key down.

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

---

### **`Keyboard().release_key()`**

Releases a previously held key.

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

---

### **`Keyboard().hotkey()`**

Holds down a combination of keys and releases them in reverse order.

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

---

### **`Keyboard().block_key()`**

Blocks all physical input from a specific key.

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

---

### **`Keyboard().unblock_key()`**

Unblocks a previously blocked key.

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

---

### **`Keyboard().write()`**

Types a string character by character with advanced, human-like typing error simulations and delays, based on the configured physics.

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

---

### **`KeyboardInfo().is_pressed()`**

Returns True if the specified key is currently physically held down.

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