#!/usr/bin/env python
# coding: utf-8

# In[47]:


get_ipython().system('pip install pillow')
import tkinter as tk
from PIL import Image, ImageTk


# In[48]:


import os
for file in os.listdir('.'):
    if file.lower().endswith('.png'):
        print(file)


# In[49]:


import pandas as pd

df1 = pd.read_csv('df_combined_game1.csv')
df2 = pd.read_csv('df_combined_game2.csv')
df3 = pd.read_csv('df_combined_game3.csv')
df4 = pd.read_csv('df_combined_game4.csv')
df5 = pd.read_csv('df_combined_game5.csv')


# In[50]:


import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd


# In[51]:


df4.replace("DNP-COACH'S DECISION", 0, inplace=True)
print(df4.head(30))


# In[52]:


df_combined_all = pd.read_csv('NBA_Finals_Combined_Final.csv')


# In[55]:


print(df_combined_all['Player'].unique())


# In[57]:


df_combined_all = df_combined_all[
    ~df_combined_all['Player'].isin([
        'Team celtics Total', 
        'Team Celtics Total', 
        'Team Maverick Total'
    ])
]

print(df_combined_all['Player'].unique())


# In[58]:


df_team_comparison = pd.read_csv('NBA_Team_Performance_by_Quarter.csv')
df_team_comparison.head()


# In[59]:


print(df_team_comparison.columns.tolist())


# In[60]:


import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd

game_files = [df1, df2, df3, df4, df5]

df_combined_all = pd.concat(game_files, ignore_index=True)


# Main GUI Class
class mainGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("NBA Finals Insight: Mavericks vs Celtics 2023-2024")

        self.create_tabs()

    def create_tabs(self):
        self.tab_control = ttk.Notebook(self.root)

        self.overview_tab = ttk.Frame(self.tab_control)
        self.player_tab = ttk.Frame(self.tab_control)
        self.team_tab = ttk.Frame(self.tab_control)
        self.game_tab = ttk.Frame(self.tab_control)

        self.tab_control.add(self.overview_tab, text='Overview')
        self.tab_control.add(self.player_tab, text='Player Stats')
        self.tab_control.add(self.team_tab, text='Team Comparison')
        self.tab_control.add(self.game_tab, text='Game Box Scores')

        self.tab_control.pack(expand=1, fill="both")

        self.create_overview_tab()
        self.create_player_tab()
        self.create_team_tab()
        self.create_game_tab()

    def create_overview_tab(self):
        # Overview Title
        title_label = ttk.Label(
            self.overview_tab, 
            text="NBA Finals Insight 2023-2024", 
            font=('Arial', 18, 'bold')
        )
        title_label.pack(pady=(10, 5))

        # Subtitle 2 teams
        teams_label = ttk.Label(
            self.overview_tab, 
            text="Dallas Mavericks vs Boston Celtics", 
            font=('Arial', 16)
        )
        teams_label.pack(pady=(0, 15))

        # Logo Team
        logo_frame = ttk.Frame(self.overview_tab)
        logo_frame.pack(pady=10)

        mav_logo = Image.open('Dallas_Mavericks_logo.png').resize((120,120))
        celt_logo = Image.open('celtics_logo.png').resize((120,120))

        self.mav_photo = ImageTk.PhotoImage(mav_logo)
        self.celt_photo = ImageTk.PhotoImage(celt_logo)

        mav_label = tk.Label(logo_frame, image=self.mav_photo)
        mav_label.pack(side='left', padx=20)

        celt_label = tk.Label(logo_frame, image=self.celt_photo)
        celt_label.pack(side='right', padx=20)
        
        #Show text score
        result_label = ttk.Label(
        self.overview_tab,
          text="Boston Celtics Win 4-1 against Dallas Mavericks \n"
         "🏆 Boston Celtics is the 2023-2024 NBA Champion 🏆",
        font=('Arial', 16, 'bold'),
        foreground='black',
        justify='center'
        )
        result_label.pack(pady=15)
        

    def create_player_tab(self):
        player_label = ttk.Label(self.player_tab, text="Select Player:", font=('Arial', 12))
        player_label.pack(pady=5)

        self.player_combobox = ttk.Combobox(self.player_tab, values=df_combined_all["Player"].unique().tolist())
        self.player_combobox.pack(pady=5)
        self.player_combobox.bind('<<ComboboxSelected>>', self.plot_player_stats)

        self.canvas_frame = ttk.Frame(self.player_tab)
        self.canvas_frame.pack()

    def plot_player_stats(self, event):
        player = self.player_combobox.get()
        player_data = df_combined_all[df_combined_all['Player'] == player]

        fig, ax = plt.subplots(figsize=(6, 4))
        stats = ['PTS', 'REB', 'AST']
        values = [player_data['PTS'].mean(), player_data['REB'].mean(), player_data['AST'].mean()]

        colors = ['#1f77b4', '#ff7f0e', '#2ca02c']  
        bars = ax.bar(stats, values, color=colors, edgecolor='black')

        # Title
        ax.set_title(f"{player} - Average Game Stats", fontsize=14, fontweight='bold')

        # Show the Value column
        for bar in bars:
            height = bar.get_height()
            ax.annotate(f'{height:.1f}',
                        xy=(bar.get_x() + bar.get_width() / 2, height),
                        xytext=(0, 5), 
                        textcoords="offset points",
                        ha='center', va='bottom', fontsize=12, fontweight='bold', color='black')

        ax.set_ylim(0, max(values)*1.3)  
        ax.set_ylabel('Stats', fontsize=12, fontweight='bold')

        for widget in self.canvas_frame.winfo_children():
            widget.destroy()

        canvas = FigureCanvasTkAgg(fig, master=self.canvas_frame)
        canvas.draw()
        canvas.get_tk_widget().pack()
        
    def create_team_tab(self):
        ttk.Label(self.team_tab, text="Team Performance by Quarter", font=('Arial', 16)).pack(pady=10)

        # Combobox select game
        ttk.Label(self.team_tab, text="Select Game:", font=('Arial', 12)).pack(pady=5)
        self.team_game_combobox = ttk.Combobox(
            self.team_tab,
            values=df_team_comparison['Game'].tolist()
        )
        self.team_game_combobox.pack(pady=5)
        self.team_game_combobox.bind('<<ComboboxSelected>>', self.plot_team_quarters)

        # Frame show quarter
        self.team_canvas_frame = ttk.Frame(self.team_tab)
        self.team_canvas_frame.pack(pady=10)

        # Frame show shotchart
        self.shotchart_frame = ttk.Frame(self.team_tab)
        self.shotchart_frame.pack(pady=10)

    def plot_team_quarters(self, event):
        game_selected = self.team_game_combobox.get()

        # Clear previous canvas
        for widget in self.team_canvas_frame.winfo_children():
            widget.destroy()
        for widget in self.shotchart_frame.winfo_children():
            widget.destroy()

        # Set data in each game
        game_data = df_team_comparison[df_team_comparison['Game'] == game_selected].iloc[0]

        quarters = ['Q1', 'Q2', 'Q3', 'Q4']

        if game_data['Home Team'] == 'Boston Celtics':
            celtics_scores = [game_data['Home Q1'], game_data['Home Q2'], game_data['Home Q3'], game_data['Home Q4']]
            mavericks_scores = [game_data['Away Q1'], game_data['Away Q2'], game_data['Away Q3'], game_data['Away Q4']]
        else:
            celtics_scores = [game_data['Away Q1'], game_data['Away Q2'], game_data['Away Q3'], game_data['Away Q4']]
            mavericks_scores = [game_data['Home Q1'], game_data['Home Q2'], game_data['Home Q3'], game_data['Home Q4']]

        fig, ax = plt.subplots(figsize=(8, 4))

        ax.plot(quarters, celtics_scores, marker='o', label='Boston Celtics', color='green', linewidth=2)
        ax.plot(quarters, mavericks_scores, marker='o', label='Dallas Mavericks', color='blue', linewidth=2)

        ax.set_title(f'Team Comparison by Quarter - {game_selected}', fontsize=14, fontweight='bold')
        ax.set_xlabel('Quarter', fontsize=12)
        ax.set_ylabel('Points', fontsize=12)
        ax.grid(True, linestyle='--', alpha=0.7)
        ax.legend()

        canvas = FigureCanvasTkAgg(fig, master=self.team_canvas_frame)
        canvas.draw()
        canvas.get_tk_widget().pack()

        # Set pics
        game_images = {
            "Game 1": "game1.PNG",
            "Game 2": "game2.PNG",
            "Game 3": "game3.PNG",
            "Game 4": "game4.PNG",
            "Game 5": "game 5.PNG"
        }

        # Set label
        annotations = {
            "Game 1": "Game 1: Black - Dallas Mavericks | Green - Boston Celtics",
            "Game 2": "Game 2: Black - Dallas Mavericks | Green - Boston Celtics",
            "Game 3": "Game 3: Black - Boston Celtics | Blue - Dallas Mavericks",
            "Game 4": "Game 4: Black - Boston Celtics | Blue - Dallas Mavericks",
            "Game 5": "Game 5: Black - Dallas Mavericks | Green - Boston Celtics"
        }

        # Show pic
        shotchart_img = Image.open(game_images[game_selected]).resize((700, 350))
        self.shotchart_photo = ImageTk.PhotoImage(shotchart_img)

        img_label = ttk.Label(self.shotchart_frame, image=self.shotchart_photo)
        img_label.pack(pady=10)

        # Show Label
        annotation_label = ttk.Label(
            self.shotchart_frame,
            text=annotations[game_selected],
            font=('Arial', 12, 'bold'),
            foreground='black'
        )
        annotation_label.pack(pady=5)



    def create_game_tab(self):
        ttk.Label(self.game_tab, text="Select Game:", font=('Arial', 12)).pack(pady=5)

        self.game_combobox = ttk.Combobox(self.game_tab, values=[f"Game {i+1}" for i in range(5)])
        self.game_combobox.pack(pady=5)
        self.game_combobox.bind('<<ComboboxSelected>>', self.show_box_score)

        self.table_frame = ttk.Frame(self.game_tab)
        self.table_frame.pack(pady=10, fill='both', expand=True)

    def show_box_score(self, event):
        selected_game = self.game_combobox.get()
        game_index = int(selected_game.split(' ')[1]) - 1

        df_game = game_files[game_index]

        # Clear table frame 
        for widget in self.table_frame.winfo_children():
            widget.destroy()

        # Build box score
        for team in df_game['Team'].unique():
            team_label = ttk.Label(self.table_frame, text=f"{team} Box Score", font=('Arial', 14))
            team_label.pack(pady=5)

            team_data = df_game[df_game['Team'] == team]

            columns = list(team_data.columns)
            tree = ttk.Treeview(self.table_frame, columns=columns, show='headings', height=10)

            for col in columns:
                tree.heading(col, text=col)
                tree.column(col, anchor='center')

            for _, row in team_data.iterrows():
                tree.insert('', tk.END, values=list(row))

            tree.pack(pady=5, fill='both', expand=True)



# Run the GUI
if __name__ == "__main__":
    root = tk.Tk()
    app = mainGUI(root)
    root.mainloop()


# In[ ]:





# In[ ]:




