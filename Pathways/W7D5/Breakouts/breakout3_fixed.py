'''
Rock, Paper, Scissors, Spock, Lizard Game
A modern tkinter application with responsive layout and interactive gameplay.
Features: Timer, Leaderboard, Menu bar, Status bar, and comprehensive game logic.
'''

import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import random
import json
import os
from datetime import datetime

class RockPaperScissorsGame:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Rock, Paper, Scissors, Spock, Lizard")
        self.root.geometry("900x750")
        self.root.minsize(700, 600)
        
        # Game state
        self.player_score = 0
        self.computer_score = 0
        self.ties = 0
        self.game_active = False
        self.timer_running = False
        self.time_left = 30
        self.player_name = "Player"
        
        # Game choices and rules
        self.choices = ["Rock", "Paper", "Scissors", "Spock", "Lizard"]
        self.choice_emojis = {
            "Rock": "🪨",
            "Paper": "📄", 
            "Scissors": "✂️",
            "Spock": "🖖",
            "Lizard": "🦎"
        }
        
        # Game rules: what beats what
        self.rules = {
            "Rock": ["Lizard", "Scissors"],
            "Paper": ["Rock", "Spock"],
            "Scissors": ["Paper", "Lizard"],
            "Spock": ["Scissors", "Rock"],
            "Lizard": ["Spock", "Paper"]
        }
        
        # Leaderboard file
        self.leaderboard_file = "leaderboard.json"
        
        # Configure styles
        self.setup_styles()
        
        # Create UI
        self.create_menu()
        self.create_widgets()
        self.update_status("Welcome to Rock, Paper, Scissors, Spock, Lizard!")
        
        # Load leaderboard
        self.load_leaderboard()
        
        # Configure grid weights for responsiveness
        self.configure_grid_weights()
        
    def setup_styles(self):
        """Configure modern styling for the application"""
        style = ttk.Style()
        
        # Set modern theme
        try:
            style.theme_use('clam')
        except:
            style.theme_use('default')
        
        # Modern color scheme
        bg_color = "#f8f9fa"
        primary_color = "#3498db"
        secondary_color = "#2c3e50"
        success_color = "#27ae60"
        warning_color = "#f39c12"
        danger_color = "#e74c3c"
        accent_color = "#9b59b6"
        
        # Configure root background
        self.root.configure(bg=bg_color)
        
        # Main frame styling
        style.configure("Main.TFrame",
                       background=bg_color,
                       relief="flat")
        
        # Card-style frames
        style.configure("Card.TLabelframe",
                       background=bg_color,
                       borderwidth=2,
                       relief="ridge",
                       labelanchor="n")
        
        style.configure("Card.TLabelframe.Label",
                       background=bg_color,
                       foreground=secondary_color,
                       font=("Segoe UI", 11, "bold"))
        
        # Choice buttons with modern hover effects
        style.configure("Choice.TButton",
                       padding=(15, 15),
                       font=("Segoe UI", 10, "bold"),
                       focuscolor="none",
                       borderwidth=2,
                       relief="solid")
        
        style.map("Choice.TButton",
                 background=[('active', primary_color), ('pressed', '#2980b9'), ('!active', '#ecf0f1')],
                 foreground=[('active', 'white'), ('pressed', 'white'), ('!active', secondary_color)],
                 bordercolor=[('active', primary_color), ('pressed', '#2980b9'), ('!active', '#bdc3c7')])
        
        # Action buttons
        style.configure("Action.TButton",
                       padding=(10, 6),
                       font=("Segoe UI", 9, "bold"),
                       focuscolor="none",
                       borderwidth=1,
                       relief="solid")
        
        style.map("Action.TButton",
                 background=[('active', accent_color), ('pressed', '#8e44ad'), ('!active', '#ecf0f1')],
                 foreground=[('active', 'white'), ('pressed', 'white'), ('!active', secondary_color)])
        
        # Label styles with modern typography
        style.configure("Title.TLabel",
                       font=("Segoe UI", 20, "bold"),
                       foreground=secondary_color,
                       background=bg_color,
                       anchor="center")
        
        style.configure("Score.TLabel",
                       font=("Segoe UI", 12, "bold"),
                       foreground=success_color,
                       background=bg_color)
        
        style.configure("Result.TLabel",
                       font=("Segoe UI", 16, "bold"),
                       foreground=danger_color,
                       background=bg_color,
                       anchor="center")
        
        style.configure("Timer.TLabel",
                       font=("Segoe UI", 11, "bold"),
                       foreground=warning_color,
                       background=bg_color)
        
        style.configure("Choice.TLabel",
                       font=("Segoe UI", 12),
                       foreground=secondary_color,
                       background=bg_color,
                       anchor="center",
                       justify="center")
        
        style.configure("VS.TLabel",
                       font=("Segoe UI", 16, "bold"),
                       foreground=primary_color,
                       background=bg_color,
                       anchor="center")
        
        # Status bar
        style.configure("Status.TLabel",
                       font=("Segoe UI", 9),
                       foreground=secondary_color,
                       background="#ecf0f1",
                       relief="sunken",
                       borderwidth=1)
        
    def create_menu(self):
        """Create the menu bar"""
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)
        
        # Game menu
        game_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Game", menu=game_menu)
        game_menu.add_command(label="New Game", command=self.new_game)
        game_menu.add_command(label="Set Player Name", command=self.set_player_name)
        game_menu.add_separator()
        game_menu.add_command(label="Exit", command=self.quit_game)
        
        # Help menu
        help_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Help", menu=help_menu)
        help_menu.add_command(label="Instructions", command=self.show_instructions)
        help_menu.add_command(label="Leaderboard", command=self.show_leaderboard)
        help_menu.add_command(label="About", command=self.show_about)
        
    def create_widgets(self):
        """Create all the UI widgets"""
        # Main container with modern styling
        main_frame = ttk.Frame(self.root, style="Main.TFrame")
        main_frame.grid(row=0, column=0, sticky="nsew", padx=20, pady=15)
        
        # Header
        self.create_header(main_frame)
        
        # Game area
        self.create_game_area(main_frame)
        
        # Score area
        self.create_score_area(main_frame)
        
        # Control buttons
        self.create_control_buttons(main_frame)
        
        # Status bar
        self.create_status_bar()
        
    def create_header(self, parent):
        """Create the header section"""
        header_frame = ttk.Frame(parent, style="Main.TFrame")
        header_frame.grid(row=0, column=0, columnspan=2, sticky="ew", pady=(0, 25))
        
        # Title
        title_label = ttk.Label(header_frame, text="🎮 Rock, Paper, Scissors, Spock, Lizard 🎮", 
                               style="Title.TLabel")
        title_label.grid(row=0, column=0, columnspan=3, pady=(0, 15))
        
        # Info row
        info_frame = ttk.Frame(header_frame, style="Main.TFrame")
        info_frame.grid(row=1, column=0, columnspan=3, sticky="ew", pady=(0, 10))
        
        # Timer
        self.timer_label = ttk.Label(info_frame, text="⏰ Ready", style="Timer.TLabel")
        self.timer_label.grid(row=0, column=0, sticky="w")
        
        # Player name
        self.player_label = ttk.Label(info_frame, text=f"👤 {self.player_name}", 
                                     style="Score.TLabel")
        self.player_label.grid(row=0, column=1, sticky="ew", padx=30)
        
        # Game status
        self.game_status_label = ttk.Label(info_frame, text="🎯 Ready to Play!", 
                                          style="Score.TLabel")
        self.game_status_label.grid(row=0, column=2, sticky="e")
        
        header_frame.columnconfigure(0, weight=1)
        info_frame.columnconfigure(1, weight=1)
        
    def create_game_area(self, parent):
        """Create the main game playing area"""
        game_frame = ttk.LabelFrame(parent, text="🎲 Make Your Choice", 
                                   padding=25, style="Card.TLabelframe")
        game_frame.grid(row=1, column=0, columnspan=2, sticky="ew", pady=(0, 20))
        
        # Choice buttons with improved responsive layout
        choice_frame = ttk.Frame(game_frame, style="Main.TFrame")
        choice_frame.grid(row=0, column=0, columnspan=3, pady=(0, 30), sticky="ew")
        
        self.choice_buttons = {}
        for i, choice in enumerate(self.choices):
            btn = ttk.Button(choice_frame, 
                           text=f"{self.choice_emojis[choice]}\n{choice}",
                           style="Choice.TButton",
                           command=lambda c=choice: self.make_choice(c))
            btn.grid(row=0, column=i, padx=8, pady=10, sticky="ew")
            self.choice_buttons[choice] = btn
            choice_frame.columnconfigure(i, weight=1)
        
        # Battle results display
        battle_frame = ttk.Frame(game_frame, style="Main.TFrame")
        battle_frame.grid(row=1, column=0, columnspan=3, sticky="ew", pady=20)
        
        # Player choice
        self.player_choice_label = ttk.Label(battle_frame, text="Your Choice:\n❓", 
                                           style="Choice.TLabel")
        self.player_choice_label.grid(row=0, column=0, padx=20, sticky="ew")
        
        # VS indicator
        vs_label = ttk.Label(battle_frame, text="⚔️\nVS", style="VS.TLabel")
        vs_label.grid(row=0, column=1, padx=15)
        
        # Computer choice
        self.computer_choice_label = ttk.Label(battle_frame, text="Computer Choice:\n❓", 
                                             style="Choice.TLabel")
        self.computer_choice_label.grid(row=0, column=2, padx=20, sticky="ew")
        
        battle_frame.columnconfigure(0, weight=1)
        battle_frame.columnconfigure(2, weight=1)
        
        # Result announcement
        self.result_label = ttk.Label(game_frame, text="", style="Result.TLabel")
        self.result_label.grid(row=2, column=0, columnspan=3, pady=20)
        
    def create_score_area(self, parent):
        """Create the score display area"""
        score_frame = ttk.LabelFrame(parent, text="📊 Score Board", 
                                    padding=20, style="Card.TLabelframe")
        score_frame.grid(row=2, column=0, columnspan=2, sticky="ew", pady=(0, 20))
        
        # Score display with better spacing
        scores_container = ttk.Frame(score_frame, style="Main.TFrame")
        scores_container.grid(row=0, column=0, sticky="ew")
        
        self.player_score_label = ttk.Label(scores_container, text=f"👤 {self.player_name}: 0", 
                                          style="Score.TLabel")
        self.player_score_label.grid(row=0, column=0, sticky="w")
        
        self.computer_score_label = ttk.Label(scores_container, text="🤖 Computer: 0", 
                                            style="Score.TLabel")
        self.computer_score_label.grid(row=0, column=1, sticky="ew", padx=40)
        
        self.ties_label = ttk.Label(scores_container, text="🤝 Ties: 0", style="Score.TLabel")
        self.ties_label.grid(row=0, column=2, sticky="e")
        
        score_frame.columnconfigure(0, weight=1)
        scores_container.columnconfigure(1, weight=1)
        
    def create_control_buttons(self, parent):
        """Create control buttons"""
        control_frame = ttk.Frame(parent, style="Main.TFrame")
        control_frame.grid(row=3, column=0, columnspan=2, sticky="ew", pady=(0, 15))
        
        # Left side buttons
        left_frame = ttk.Frame(control_frame, style="Main.TFrame")
        left_frame.grid(row=0, column=0, sticky="w")
        
        self.new_game_btn = ttk.Button(left_frame, text="🎮 New Game", 
                                      style="Action.TButton", command=self.new_game)
        self.new_game_btn.grid(row=0, column=0, padx=(0, 8))
        
        self.help_btn = ttk.Button(left_frame, text="❓ Help", 
                                  style="Action.TButton", command=self.show_instructions)
        self.help_btn.grid(row=0, column=1, padx=8)
        
        # Right side buttons
        right_frame = ttk.Frame(control_frame, style="Main.TFrame")
        right_frame.grid(row=0, column=2, sticky="e")
        
        self.leaderboard_btn = ttk.Button(right_frame, text="🏆 Leaderboard", 
                                         style="Action.TButton", command=self.show_leaderboard)
        self.leaderboard_btn.grid(row=0, column=0, padx=8)
        
        self.quit_btn = ttk.Button(right_frame, text="🚪 Quit", 
                                  style="Action.TButton", command=self.quit_game)
        self.quit_btn.grid(row=0, column=1, padx=(8, 0))
        
        control_frame.columnconfigure(1, weight=1)
        
    def create_status_bar(self):
        """Create the status bar at the bottom"""
        self.status_bar = ttk.Label(self.root, text="🎯 Ready to play!", 
                                   style="Status.TLabel", anchor=tk.W, padding=(10, 5))
        self.status_bar.grid(row=1, column=0, sticky="ew")
        
    def configure_grid_weights(self):
        """Configure grid weights for responsive layout"""
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        
    def make_choice(self, player_choice):
        """Handle player's choice and play a round"""
        if self.timer_running:
            return
            
        # Start timer for this round
        self.start_timer()
        
        # Disable choice buttons during round
        for btn in self.choice_buttons.values():
            btn.config(state="disabled")
        
        # Computer makes random choice
        computer_choice = random.choice(self.choices)
        
        # Update display with animation-like effect
        self.player_choice_label.config(text=f"Your Choice:\n{self.choice_emojis[player_choice]} {player_choice}")
        self.computer_choice_label.config(text=f"Computer Choice:\n{self.choice_emojis[computer_choice]} {computer_choice}")
        
        # Determine winner
        result = self.determine_winner(player_choice, computer_choice)
        
        # Update scores and display with color-coded results
        if result == "win":
            self.player_score += 1
            self.result_label.config(text="🎉 Victory! You Win! 🎉")
            self.update_status(f"🎉 You won! {player_choice} beats {computer_choice}")
        elif result == "lose":
            self.computer_score += 1
            self.result_label.config(text="😞 Defeat! Computer Wins! 😞")
            self.update_status(f"😞 You lost! {computer_choice} beats {player_choice}")
        else:
            self.ties += 1
            self.result_label.config(text="🤝 It's a Draw! 🤝")
            self.update_status(f"🤝 It's a tie! Both chose {player_choice}")
        
        self.update_score_display()
        
        # Re-enable buttons after delay
        self.root.after(3000, self.enable_choice_buttons)
        
    def determine_winner(self, player_choice, computer_choice):
        """Determine the winner of a round"""
        if player_choice == computer_choice:
            return "tie"
        elif computer_choice in self.rules[player_choice]:
            return "win"
        else:
            return "lose"
    
    def start_timer(self):
        """Start the 30-second timer for a round"""
        self.timer_running = True
        self.time_left = 30
        self.update_timer()
        
    def update_timer(self):
        """Update the timer display"""
        if self.timer_running and self.time_left > 0:
            self.timer_label.config(text=f"⏰ Time: {self.time_left}s")
            self.time_left -= 1
            self.root.after(1000, self.update_timer)
        else:
            self.timer_running = False
            self.timer_label.config(text="⏰ Ready")
            self.enable_choice_buttons()
    
    def enable_choice_buttons(self):
        """Re-enable choice buttons"""
        for btn in self.choice_buttons.values():
            btn.config(state="normal")
        self.timer_running = False
        
    def update_score_display(self):
        """Update the score display"""
        self.player_score_label.config(text=f"👤 {self.player_name}: {self.player_score}")
        self.computer_score_label.config(text=f"🤖 Computer: {self.computer_score}")
        self.ties_label.config(text=f"🤝 Ties: {self.ties}")
        
    def new_game(self):
        """Start a new game"""
        # Save current game to leaderboard if there were any plays
        if self.player_score > 0 or self.computer_score > 0 or self.ties > 0:
            self.save_to_leaderboard()
        
        # Reset scores
        self.player_score = 0
        self.computer_score = 0
        self.ties = 0
        
        # Reset display
        self.player_choice_label.config(text="Your Choice:\n❓")
        self.computer_choice_label.config(text="Computer Choice:\n❓")
        self.result_label.config(text="")
        self.timer_label.config(text="⏰ Ready")
        
        # Update displays
        self.update_score_display()
        self.update_status("🎮 New game started! Make your choice!")
        
        # Enable buttons
        self.enable_choice_buttons()
        
    def set_player_name(self):
        """Allow player to set their name"""
        name = simpledialog.askstring("Player Name", "Enter your name:", 
                                     initialvalue=self.player_name)
        if name and name.strip():
            self.player_name = name.strip()
            self.player_label.config(text=f"👤 {self.player_name}")
            self.update_score_display()
            
    def show_instructions(self):
        """Show game instructions"""
        instructions = """
🎮 Rock, Paper, Scissors, Spock, Lizard Rules:

🪨 Rock crushes Lizard and crushes Scissors
📄 Paper covers Rock and disproves Spock  
✂️ Scissors cuts Paper and decapitates Lizard
🖖 Spock smashes Scissors and vaporizes Rock
🦎 Lizard poisons Spock and eats Paper

🎯 How to Play:
1. Click on one of the five choice buttons
2. The computer will make its choice
3. The winner is determined by the rules above
4. You have 30 seconds for each round
5. Scores are tracked and saved to leaderboard

🏆 Scoring:
• Win: +1 point for you
• Lose: +1 point for computer  
• Tie: +1 tie for both

Good luck and have fun! 🎉
        """
        messagebox.showinfo("Game Instructions", instructions)
        
    def show_leaderboard(self):
        """Show the leaderboard"""
        leaderboard = self.load_leaderboard()
        
        if not leaderboard:
            messagebox.showinfo("Leaderboard", "🏆 No games played yet!\n\nStart playing to see your scores here! 🎮")
            return
            
        # Sort by wins, then by win percentage
        sorted_board = sorted(leaderboard, key=lambda x: (x['wins'], x['win_percentage']), reverse=True)
        
        leaderboard_text = "🏆 TOP 5 PLAYERS 🏆\n\n"
        leaderboard_text += f"{'Rank':<5} {'Name':<15} {'Wins':<6} {'Losses':<8} {'Ties':<6} {'Win %':<8}\n"
        leaderboard_text += "─" * 65 + "\n"
        
        for i, entry in enumerate(sorted_board[:5]):
            rank = f"#{i + 1}"
            name = entry['name'][:14]  # Truncate long names
            wins = entry['wins']
            losses = entry['losses'] 
            ties = entry['ties']
            win_pct = f"{entry['win_percentage']:.1f}%"
            
            leaderboard_text += f"{rank:<5} {name:<15} {wins:<6} {losses:<8} {ties:<6} {win_pct:<8}\n"
            
        messagebox.showinfo("🏆 Leaderboard", leaderboard_text)
        
    def load_leaderboard(self):
        """Load leaderboard from file"""
        try:
            if os.path.exists(self.leaderboard_file):
                with open(self.leaderboard_file, 'r') as f:
                    return json.load(f)
        except Exception as e:
            print(f"Error loading leaderboard: {e}")
        return []
        
    def save_to_leaderboard(self):
        """Save current game to leaderboard"""
        if self.player_score == 0 and self.computer_score == 0 and self.ties == 0:
            return
            
        leaderboard = self.load_leaderboard()
        
        total_games = self.player_score + self.computer_score + self.ties
        win_percentage = (self.player_score / total_games * 100) if total_games > 0 else 0
        
        entry = {
            'name': self.player_name,
            'wins': self.player_score,
            'losses': self.computer_score,
            'ties': self.ties,
            'win_percentage': win_percentage,
            'date': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        
        leaderboard.append(entry)
        
        try:
            with open(self.leaderboard_file, 'w') as f:
                json.dump(leaderboard, f, indent=2)
        except Exception as e:
            print(f"Error saving leaderboard: {e}")
            
    def show_about(self):
        """Show about dialog"""
        about_text = """
🎮 Rock, Paper, Scissors, Spock, Lizard

Version: 2.0
Created: 2025

A modern implementation of the classic game
with Spock and Lizard additions, featuring:

✨ Responsive GUI layout
⏰ Timer functionality  
🏆 Leaderboard system
🎨 Modern styling with hover effects
📋 Menu system
📊 Real-time status updates
🎯 Interactive gameplay

Based on the Big Bang Theory variant
of the classic Rock, Paper, Scissors game.

Enjoy playing! 🎉
        """
        messagebox.showinfo("About", about_text)
        
    def update_status(self, message):
        """Update the status bar"""
        self.status_bar.config(text=message)
        
    def quit_game(self):
        """Quit the application"""
        # Save current game if any plays were made
        if self.player_score > 0 or self.computer_score > 0 or self.ties > 0:
            if messagebox.askyesno("Save Game", "Do you want to save your current game to the leaderboard?"):
                self.save_to_leaderboard()
        
        self.root.quit()
        self.root.destroy()
        
    def run(self):
        """Start the application"""
        self.root.mainloop()

if __name__ == "__main__":
    game = RockPaperScissorsGame()
    game.run()
