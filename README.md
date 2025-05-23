# Assignment 3: NBA Finals 2023-2024 Insights – Mavericks vs Celtics

This notebook presents a comprehensive analysis and visualisation of player and team performance during the NBA Finals 2023-2024 between the Dallas Mavericks and the Boston Celtics.

---

### **Notebook Structure:**
-  GUI.ipynb: The notebook contains the structure of the Interactive Graphical User Interface GUI
-  Assignment3_PythonProgramming_Project.ipynb. The notebook includes the following sections:
##### **1. API** : 
- Retrieved data using a free API provided by RapidAPI - API-Basketball website https://rapidapi.com/api-sports/api/api-basketball
- API key used: c3d8aa9a21msh7581db5aa693f61p1ab7fcjsnf0cdd2ef7be3
- Extracted relevant data specific to the championship finals between the Dallas Mavericks and Boston Celtics.
- Data stored in CSV format as NBA_Finals_2023_2024_API.csv

##### **2. Web Scraping:** 
- Collected detailed box score data for the final 5 games from ESPN:

  - Game 1: https://www.espn.com.au/nba/boxscore/_/gameId/401656359

  - Game 2: https://www.espn.com.au/nba/game/_/gameId/401656360/mavericks-celtics

  - Game 3: https://www.espn.com.au/nba/game/_/gameId/401656361/celtics-mavericks

  - Game 4: https://www.espn.com.au/nba/game/_/gameId/401656362/celtics-mavericks

  - Game 5: https://www.espn.com.au/nba/game/_/gameId/401656363/mavericks-celtics

- Implemented all 3 web scraping techniques demonstrated in the week 6 tutorial:

  - Game 1: HTML parsing

  - Game 2: GET requests

  - Game 3: Table extraction

  - Game 4: GET requests

  - Game 5: GET requests

##### **3. Data Cleaning:** 

- Cleaned each game's dataset to retain relevant information, including: Player, MIN, FG, 3PT, FT, OREB, DREB, REB, AST, STL, BLK, TO, PF, +/-, PTS, Team, Role, Game

##### **4. Data Integration:** 
- Combined individual game datasets to create comprehensive data sets:

  - Game 1: Maverick_dataset_1, Celtics_dataset_1, Combine_dataset_1

  - Game 2: Maverick_dataset_2, Celtics_dataset_2, Combine_dataset_2

  - Game 3: Maverick_dataset_3, Celtics_dataset_3, Combine_dataset_3

  - Game 4: Maverick_dataset_4, Celtics_dataset_4, Combine_dataset_4

  - Game 5: Maverick_dataset_5, Celtics_dataset_5, Combine_dataset_5

- Created full-series datasets:

  - Maverick_full_dataset: Combined data from all Mavericks games.

  - Celtics_full_dataset: Combined data from all Celtics games.

  - Full_series_dataset: Comprehensive combined dataset from all games with the API dataset.

##### **5. Data Processing:** 
- Performed further processing to prepare data for visualisation and analysis, such as aggregation, sorting, and filtering.

##### **6. Data Visualisation:** 
- Generated interactive and insightful visualisations highlighting key statistics and performance metrics for teams and players.

##### **7. OOP Principles:**

- Implemented Object-Oriented Programming (OOP) principles to create structured and reusable code.

##### **8. Unit Testing:**
- Developed unit tests to ensure data processing and cleaning functions work correctly, enhancing reliability and maintainability.

##### **9. Graphical User Interface (GUI):** 
- A Python-based GUI developed using Tkinter to visualise key insights interactively. The GUI is structured into clearly navigable tabs:
  - Overview: Championship summary.
  - Player Stats: Interactive statistics of individual players.
  - Team Comparison: Quarter-by-quarter performance charts for each final game (Games 1-5).
  - Game Box Scores: Detailed box scores for each final game (Games 1–5).
    
---

### **Necessary API Keys:**
- The project uses data retrieved from the website https://rapidapi.com/api-sports/api/api-basketball
- The API key is c3d8aa9a21msh7581db5aa693f61p1ab7fcjsnf0cdd2ef7be3

---
### **Dependencies:**
- Python version 3.7 or higher
- The GUI requires the following Python libraries:
 pandas
  - pandas  
  - matplotlib  
  - seaborn  
  - requests  
  - beautifulsoup4  
  - tkinter  
  - Pillowmatplotlib
  
---

### **Run the GUI**
- Download the file
- Unzip the file .rar or .zip 
- Navigate to the extracted folder, and you will see a file named GUI.py
- Install Dependencies: install required packages using:
```bash
pip install -r requirements.txt
```

- Run the GUI
  - On terminal/command prompt using:
```bash
python GUI.py
``` 
  - On Jupyter Notebook using
```bash
jupyter notebook GUI.ipynb
```
---
### **Notes**
- The GUI.ipynb file can only run on Anaconda Terminal or Jupyter Notebook. It cannot run directly on Google Colab due to limitations.

- The file named Assignment3_PythonProgramming_Project.ipynb can run on Google Colab and Jupyter Notebook.

- Because Game 1's data was collected via HTML web scraping, you must add the game1.html file:

  - Download the webpage from ESPN Game 1 Boxscore and save it as game1.html.

  - Place the game1.html file in the same folder as Assignment3_PythonProgramming_GroupProject.ipynb.


---
### **Contributors:**
- **Nhu Thanh Nguyen** – 25505569  
- **Andrew Fenelon** – 26100786  

---

###  **Course Details:**
- **Subject:** 36122 - Python Programming - Autumn 2025  
- **Program:** Master of Data Science and Innovation  
- **Institution:** University of Technology Sydney (UTS)

