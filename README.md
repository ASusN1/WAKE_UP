<a id="readme-top"></a>

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

<br />
<div align="center">
        <a href="https://github.com/ASusN1/WAKE_UP">
        <img src="https://raw.githubusercontent.com/ASusN1/WAKE_UP/main/visual_art/bg_panel_thingy.png" alt="Project Logo" width="350" height="150"/>
    </a>
    <h3 align="center">WAKE UP - Productivity & Task Management</h3>
    <p align="center">
        A powerful desktop application for managing tasks, brain dumps, and productivity with built-in timer functionality.
        <br />
        <br />
        <a href="https://github.com/ASusN1/WAKE_UP"><strong>View Project »</strong></a>
        <br />
        <br />
        <a href="https://github.com/ASusN1/WAKE_UP/releases/new">Download Release</a>
        ·
        <a href="https://github.com/ASusN1/WAKE_UP/issues">Report Bug</a>
        ·
        <a href="https://github.com/ASusN1/WAKE_UP/issues">Request Feature</a>
    </p>
</div>

<details>
    <summary>Table of Contents</summary>
    <ol>
        <li>
            <a href="#about-the-project">About The Project</a>
            <ul>
                <li><a href="#built-using">Built Using</a></li>
            </ul>
        </li>
        <li>
            <a href="#getting-started">Getting Started</a>
            <ul>
                <li><a href="#installation">Installation</a></li>
            </ul>
        </li>
        <li><a href="#usage">Usage</a></li>
        <li><a href="#features">Features</a></li>
        <li><a href="#file-structure">File Structure</a></li>
    </ol>
</details>

## About The Project
<br />

**WAKE UP** is a  productivity application designed to help you manage your daily tasks, capture quick thoughts (brain dumps), create sticky notes, and stay focused with built-in timer functionality. Whether you're working on personal projects, organizing your day, or just need a place to dump your ideas, WAKE UP has you covered.

**Key Features:**
* **Sticky Notes** - Create, edit, and manage daily task lists with priority highlighting
* **Brain Dump Notes** - Quickly capture and organize your thoughts and ideas
* **Editable Timer** - Set custom countdown timers for focused work sessions
* **Auto-Save & Load** - Automatically save notes with custom naming based on content
* **Task Prioritization** - Mark and highlight priority tasks at a glance
* **Standalone Executable** - Run as a .exe file without requiring Python installation
* **Clean GUI** - Simple interface built with Tkinter

<p align="right">(<a href="#readme-top">top</a>)</p>

### Built Using

* [Python 3.10+](https://www.python.org/)
* [Tkinter](https://docs.python.org/3/library/tkinter.html) - GUI framework
* [JSON](https://www.json.org/) - Data storage
* [PyInstaller](https://pyinstaller.org/) - Executable creation

<p align="right">(<a href="#readme-top">top</a>)</p>

## Getting Started

You can either download the ready-to-use [release executable](https://github.com/ASusN1/WAKE_UP/releases/tag/untagged-49fdae4980632b1b83b1) or set up the project locally to run from the source code.

### Installation

**Option 1: Use the Executable (Recommended)**
1. Download `WAKE_UP.exe` from the [releases page](https://github.com/ASusN1/WAKE_UP/releases/tag/untagged-49fdae4980632b1b83b1)
2. Run the executable directly - no installation needed!

**Option 2: Run from Source Code**

1. Clone the repository
   ```sh
   git clone https://github.com/ASusN1/WAKE_UP.git
   ```
2. Navigate into the directory
   ```sh
   cd WAKE_UP
   ```
3. Run the application
   ```sh
   python Main_menu.py
   ```

<p align="right">(<a href="#readme-top">top</a>)</p>

## Usage

### Launching the Application
From the executable:
```sh
D:\path\to\WAKE_UP\dist\WAKE_UP.exe
```

From source code:
```sh
python Main_menu.py
```

### Main Menu
The main interface provides quick access to all features:
- **Timer** - Set custom work session durations
- **Sticky Notes** - Create and manage task lists
- **Brain Dump** - Capture quick thoughts and ideas
- **Save/Load** - Persist your work across sessions

### Creating a Sticky Note
1. Click **"Sticky Notes"** button
2. Choose **"Create New"** or **"Load Saved"**
3. Click on the title to edit it
4. Add tasks by typing and pressing Enter
5. Use checkbox to mark completed tasks
6. Click **"Highlight Priority Task"** to mark important items
7. Click **"Finish"** to save

### Creating a Brain Dump Note
1. Click **"Brain Dump"** button
2. Choose **"Create New"** or **"Load Saved"**
3. Click the title to customize it
4. Type your thoughts and ideas
5. Click **"Finish"** to save

### Using the Timer
1. Click on the time display to edit hours, minutes, or seconds
2. Click **"Start Timer"** to begin countdown
3. Timer will count down and alert when time is up

<p align="right">(<a href="#readme-top">top</a>)</p>

## Features

### Smart File Naming
- Notes automatically save with meaningful names based on their title
- If using the default title, files are numbered (0, 1, 2, etc.)
- Future saves to the same note reuse the same file

### Data Organization
Files are organized by type:
- `sticky_note_data/` - Sticky note saves
- `brain_dump_data/` - Brain dump note saves
- `other_stuff_data/` - Reserved for future notes

### Load Previously Saved Notes
When creating a new note, you can browse and load previously saved files:
1. Select the note type
2. Click "Load Saved"
3. Choose from the list of available saves
4. Opens that note ready for editing

<p align="right">(<a href="#readme-top">top</a>)</p>

## File Structure

```
WAKE_UP/
├── Main_menu.py              # Main entry point
├── UI_sticky_notes.py        # Sticky notes interface
├── brain_dump_note.py        # Brain dump interface
├── store_note.py             # Data storage & retrieval
├── time_logic.py             # Timer functionality
├── main_menu_function_stuff.py # Menu utilities
├── function_sticky_note.py    # Sticky note logic
├── brain_dump_note_function.py # Brain dump logic
├── sticky_note_data/         # Saved sticky notes
├── brain_dump_data/          # Saved brain dumps
├── other_stuff_data/         # Reserved (for future update)
└── dist/
    └── WAKE_UP.exe           # Standalone executable
```

<p align="right">(<a href="#readme-top">top</a>)</p>

## Contributing

Contributions are welcome! Feel free to:
1. Fork the repository
2. Create a feature branch
3. Submit a pull request

<p align="right">(<a href="#readme-top">top</a>)</p>

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

<p align="right">(<a href="#readme-top">top</a>)</p>

---

[contributors-shield]: https://img.shields.io/github/contributors/ASusN1/WAKE_UP.svg?style=for-the-badge
[contributors-url]: https://github.com/ASusN1/WAKE_UP/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/ASusN1/WAKE_UP.svg?style=for-the-badge
[forks-url]: https://github.com/ASusN1/WAKE_UP/network/members
[stars-shield]: https://img.shields.io/github/stars/ASusN1/WAKE_UP.svg?style=for-the-badge
[stars-url]: https://github.com/ASusN1/WAKE_UP/stargazers
[issues-shield]: https://img.shields.io/github/issues/ASusN1/WAKE_UP.svg?style=for-the-badge
[issues-url]: https://github.com/ASusN1/WAKE_UP/issues
[product-screenshot]: https://via.placeholder.com/800x400?text=WAKE+UP+App+Screenshot
