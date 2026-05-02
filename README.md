# ⚔️ Cave Crawler: The Ultimate Text Adventure
**The most expansive text-based RPG I have ever developed!**

Welcome to a deep, atmospheric journey through a massive network of interconnected caves. This isn't just a simple script; it's a persistent world featuring complex equipment mechanics, stat-boosting loot, and a dedicated progression system.

## 🌟 Key Features
*   **Expansive Exploration:** Navigate a sprawling world of numerous unique caves, each filled with mystery and danger.
*   **Dynamic Equipment System:** Find and equip gear that provides **permanent positive boosts** to your character's capabilities.
*   **Persistent Progress:** Features a built-in save system that tracks your journey through the depths.
*   **One-Click Reset:** Includes a dedicated `reset.py` utility for players who wish to wipe their data and start a fresh adventure.

## 💾 Save Mechanics (How it Works)
To maintain the challenge and "rogue-lite" feel of the game, the save system uses a **Checkpoint Mechanic**:
*   **What is saved:** The game automatically records every new **Cave** you discover or enter.
*   **Reloading:** When you resume a game, you will begin at the **entrance** of the last cave you reached. Note that progress *inside* a specific cave (your exact room/coordinates) is not saved—only the cave location itself.

## 🛠️ Tech Stack
*   **Language:** Python 3.x
*   **Data Management:** Local file-based persistence for save states.
*   **Deployment:** Compiled to standalone `.exe` using PyInstaller for a seamless user experience.

## 🎮 How to Play
1.  **Launch:** Run the `Runner.exe`.
2.  **Navigate:** Use the text prompts to move between locations and interact with the environment.
3.  **Loot:** Keep an eye out for equipment! These items are essential for surviving deeper, more difficult caves.
4.  **Save:** Reaching a new cave entrance automatically logs your progress.
5.  **Restarting:** If you want to delete your save file and start over, simply run `reset.exe`.

## 🚀 Installation & Setup
1.  Download the latest **Release** from the sidebar.
2.  Extract the ZIP file to a folder of your choice.
3.  Double-click the `.exe` file to begin your
