# ⚔️ Cave Crawler: The Ultimate Text Adventure
**The most expansive text-based RPG I have ever developed!**

Welcome to a deep, atmospheric journey through a massive network of interconnected caves. This isn't just a simple script; it's a persistent world featuring complex equipment mechanics, stat-boosting loot, and a dedicated progression system.

## 🌟 Key Features
*   **Expansive Exploration:** Navigate a sprawling world of numerous unique caves, each filled with mystery and danger.
*   **Dynamic Equipment System:** Find and equip gear that provides **permanent positive boosts** to your character's capabilities.
*   **Persistent Progress:** Features a built-in save system that tracks your journey through the depths.

## 💾 Save Mechanics (How it Works)
To maintain the challenge and "rogue-lite" feel of the game, the save system uses a **Checkpoint Mechanic**:
*   **What is saved:** The game automatically records every new **Cave** you discover or enter.
*   **Reloading:** When you resume a game, you will begin at the **entrance** of the last cave you reached. Note that progress *inside* a specific cave (your exact room/coordinates) is not saved—only the cave location itself.

## 🛠️ Tech Stack
*   **Language:** Python 3.x
*   **Data Management:** Local file-based persistence for save states.
*   **Deployment:** Compiled to standalone Mac Executable using PyInstaller for a seamless user experience.

## 🎮 How to Play
1.  **Launch:** Run the Cave Crawler executable.
2.  **Navigate:** Use the text prompts to move between locations and interact with the environment.
3.  **Loot:** Keep an eye out for equipment! These items are essential for surviving deeper, more difficult caves.
4.  **Save:** Reaching a new cave entrance automatically logs your progress.
5.  **Restarting:** If you want to delete your save file and start over, simply choose the reset option in the main menu(this only becomes available after the first 2 caves, with some exceptions)

## 🚀 Installation & Setup
1.  Download the latest **Release** from the sidebar.
2.  Extract the ZIP file and follow the instructions in the "INSTRUCTIONS-IMPORTANT.txt" file.


## NOTE
The old variety ofsavefile is no longer supported foor the current version. For those who still wish to play with the legacy versions of this game a legacy folder has been added. All of the source code for past versions will be there, as well as a complete game. You can also find previous versions on the releases page, however V1.0.0 th game WILL NOT WORK. Instead use the ones provided in the legacy folder.
