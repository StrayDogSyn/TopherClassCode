"""
Rock, Paper, Scissors, Spock, Lizard Game
A modern tkinter application with advanced features
"""

import tkinter as tk
from tkinter import ttk, messagebox
import random
import json
import os
from datetime import datetime
import threading
import time

class GradientFrame(tk.Canvas):
    """Custom frame with gradient background"""
    def __init__(self, parent, color1="#1a1a2e", color2="#16213e", **kwargs):
        super().__init__(parent, **kwargs)
        self.color1 = color1
        self.color2 = color2
        self.bind('<Configure>', self._draw_gradient)
        
    def _draw_gradient(self, event=None):
        self.delete("gradient")
        width = self.winfo_width()
        height = self.winfo_height()
        
        if width > 1 and height > 1:
            # Create vertical gradient
            for i in range(height):
                ratio = i / height
                r1, g1, b1 = self._hex_to_rgb(self.color1)
                r2, g2, b2 = self._hex_to_rgb(self.color2)
                
                r = int(r1 + (r2 - r1) * ratio)
                g = int(g1 + (g2 - g1) * ratio)
                b = int(b1 + (b2 - b1) * ratio)
                
                color = f"#{r:02x}{g:02x}{b:02x}"
                self.create_line(0, i, width, i, fill=color, tags="gradient")
    
    def _hex_to_rgb(self, hex_color):
        hex_color = hex_color.lstrip('#')
        return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

class RPSLSGame:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Rock Paper Scissors Spock Lizard - Modern Edition")
        self.root.geometry("1000x800")
        self.root.configure(bg="#0f0f23")
        
        # Game state
        self.player_score = 0
        self.computer_score = 0
        self.ties = 0
        self.total_games = 0
        self.current_round = 1
        self.max_rounds = 5
        self.time_left = 30
        self.timer_running = False
        self.sound_enabled = True
        self.difficulty = "Normal"
        
        # Game choices and rules
        self.choices = ["Rock", "Paper", "Scissors", "Spock", "Lizard"]
        self.choice_emojis = {
            "Rock": "🪨", "Paper": "📄", "Scissors": "✂️", 
            "Spock": "🖖", "Lizard": "🦎"
        }
        
        # Game rules (what beats what)
        self.rules = {
            "Rock": ["Scissors", "Lizard"],
            "Paper": ["Rock", "Spock"],
            "Scissors": ["Paper", "Lizard"],
            "Spock": ["Scissors", "Rock"],
            "Lizard": ["Spock", "Paper"]
        }
        
        # Color scheme - Modern dark theme with neon accents
        self.colors = {
            "bg_primary": "#0f0f23",
            "bg_secondary": "#1a1a2e", 
            "bg_tertiary": "#16213e",
            "accent": "#00d4aa",
            "accent_hover": "#00b894",
            "danger": "#ff3b30",
            "warning": "#ff9500",
            "text_primary": "#ffffff",
            "text_secondary": "#a0a0a0",
            "success": "#30d158"
        }
        
        # Load leaderboard
        self.load_leaderboard()
        
        # Setup UI
        self.setup_styles()
        self.create_menu()
        self.create_main_interface()
        self.create_status_bar()
        
        # Start with welcome message
        self.update_status("Welcome to Rock Paper Scissors Spock Lizard! 🎮")
        
    def setup_styles(self):
        """Configure modern styling"""
        self.style = ttk.Style()
        self.style.theme_use('clam')
        
        # Configure modern button style
        self.style.configure('Modern.TButton',
                           background=self.colors["accent"],
                           foreground=self.colors["text_primary"],
                           borderwidth=0,
                           focuscolor='none',
                           font=('Segoe UI', 11, 'bold'))
        
        self.style.map('Modern.TButton',
                      background=[('active', self.colors["accent_hover"]),
                                ('pressed', self.colors["bg_tertiary"])])
        
        # Configure danger button style
        self.style.configure('Danger.TButton',
                           background=self.colors["danger"],
                           foreground=self.colors["text_primary"],
                           borderwidth=0,
                           focuscolor='none',
                           font=('Segoe UI', 10, 'bold'))
        
        # Configure choice button style
        self.style.configure('Choice.TButton',
                           background=self.colors["bg_secondary"],
                           foreground=self.colors["text_primary"],
                           borderwidth=2,
                           relief='solid',
                           bordercolor=self.colors["accent"],
                           focuscolor='none',
                           font=('Segoe UI', 12, 'bold'))
        
    def create_menu(self):
        """Create modern menu bar"""
        menubar = tk.Menu(self.root, bg=self.colors["bg_secondary"], 
                         fg=self.colors["text_primary"], 
                         activebackground=self.colors["accent"],
                         activeforeground=self.colors["text_primary"])
        
        # Game menu
        game_menu = tk.Menu(menubar, tearoff=0, bg=self.colors["bg_secondary"],
                           fg=self.colors["text_primary"])
        game_menu.add_command(label="New Game", command=self.new_game, accelerator="Ctrl+N")
        game_menu.add_command(label="Reset Score", command=self.reset_score)
        game_menu.add_separator()
        game_menu.add_command(label="Exit", command=self.quit_game, accelerator="Ctrl+Q")
        menubar.add_cascade(label="Game", menu=game_menu)
        
        # View menu
        view_menu = tk.Menu(menubar, tearoff=0, bg=self.colors["bg_secondary"],
                           fg=self.colors["text_primary"])
        view_menu.add_command(label="Instructions", command=self.show_instructions)
        view_menu.add_command(label="Leaderboard", command=self.show_leaderboard)
        menubar.add_cascade(label="View", menu=view_menu)
        
        # Settings menu
        settings_menu = tk.Menu(menubar, tearoff=0, bg=self.colors["bg_secondary"],
                               fg=self.colors["text_primary"])
        settings_menu.add_command(label="Preferences", command=self.show_settings)
        menubar.add_cascade(label="Settings", menu=settings_menu)
        
        self.root.config(menu=menubar)
        
        # Keyboard shortcuts
        self.root.bind('<Control-n>', lambda e: self.new_game())
        self.root.bind('<Control-q>', lambda e: self.quit_game())
        
    def create_main_interface(self):
        """Create the main game interface with gradient background"""
        # Main container with gradient background
        self.main_frame = GradientFrame(self.root, color1="#0f0f23", color2="#1a1a2e")
        self.main_frame.pack(fill='both', expand=True, padx=10, pady=5)
        
        # Header
        self.create_header()
        
        # Game area
        self.create_game_area()
          # Footer
        self.create_footer()
        
    def create_header(self):
        """Create modern header with title and stats"""
        header_frame = tk.Frame(self.main_frame, bg=self.colors["bg_primary"])
        self.main_frame.create_window(500, 50, window=header_frame)
        
        # Title with modern font
        title_label = tk.Label(header_frame, 
                              text="🎮 ROCK PAPER SCISSORS SPOCK LIZARD",
                              font=('Segoe UI', 24, 'bold'),
                              fg=self.colors["accent"],
                              bg=self.colors["bg_primary"])
        title_label.pack(pady=(0, 10))
        
        # Stats frame
        stats_frame = tk.Frame(header_frame, bg=self.colors["bg_primary"])
        stats_frame.pack()
        
        # Score display with modern styling
        self.score_frame = tk.Frame(stats_frame, bg=self.colors["bg_secondary"], 
                                   relief='solid', bd=2)
        self.score_frame.pack(side='left', padx=10)
        
        tk.Label(self.score_frame, text="SCORE", 
                font=('Segoe UI', 10, 'bold'),
                fg=self.colors["text_secondary"],
                bg=self.colors["bg_secondary"]).pack(pady=5)
        
        self.score_label = tk.Label(self.score_frame,
                                   text=f"You: {self.player_score} | Computer: {self.computer_score} | Ties: {self.ties}",
                                   font=('Segoe UI', 12, 'bold'),
                                   fg=self.colors["text_primary"],
                                   bg=self.colors["bg_secondary"])
        self.score_label.pack(padx=20, pady=(0, 10))
        
        # Timer display
        self.timer_frame = tk.Frame(stats_frame, bg=self.colors["bg_secondary"],
                                   relief='solid', bd=2)
        self.timer_frame.pack(side='left', padx=10)
        
        tk.Label(self.timer_frame, text="TIME LEFT",
                font=('Segoe UI', 10, 'bold'),
                fg=self.colors["text_secondary"],
                bg=self.colors["bg_secondary"]).pack(pady=5)
        
        self.timer_label = tk.Label(self.timer_frame,
                                   text=f"{self.time_left}s",
                                   font=('Segoe UI', 16, 'bold'),
                                   fg=self.colors["accent"],
                                   bg=self.colors["bg_secondary"])        self.timer_label.pack(padx=20, pady=(0, 10))
        
    def create_game_area(self):
        """Create the main game area"""
        game_frame = tk.Frame(self.main_frame, bg=self.colors["bg_primary"])
        self.main_frame.create_window(500, 400, window=game_frame)
        
        # Choice buttons frame
        choices_frame = tk.Frame(game_frame, bg=self.colors["bg_primary"])
        choices_frame.pack(pady=20)
        
        tk.Label(choices_frame, text="Choose Your Weapon:",
                font=('Segoe UI', 16, 'bold'),
                fg=self.colors["text_primary"],
                bg=self.colors["bg_primary"]).pack(pady=10)
        
        # Create choice buttons in a grid
        buttons_frame = tk.Frame(choices_frame, bg=self.colors["bg_primary"])
        buttons_frame.pack()
        
        self.choice_buttons = {}
        for i, choice in enumerate(self.choices):
            row = i // 3
            col = i % 3
            
            btn = tk.Button(buttons_frame,
                           text=f"{self.choice_emojis[choice]}\n{choice}",
                           font=('Segoe UI', 14, 'bold'),
                           bg=self.colors["bg_secondary"],
                           fg=self.colors["text_primary"],
                           activebackground=self.colors["accent"],
                           activeforeground=self.colors["text_primary"],
                           relief='solid',
                           bd=2,
                           width=12,
                           height=3,
                           command=lambda c=choice: self.player_choice(c))
            
            btn.grid(row=row, column=col, padx=5, pady=5)
            self.choice_buttons[choice] = btn
        
        # Result display area
        self.result_frame = tk.Frame(game_frame, bg=self.colors["bg_secondary"],
                                    relief='solid', bd=2)
        self.result_frame.pack(pady=20, padx=20, fill='x')
        
        tk.Label(self.result_frame, text="BATTLE RESULT",
                font=('Segoe UI', 12, 'bold'),
                fg=self.colors["text_secondary"],
                bg=self.colors["bg_secondary"]).pack(pady=5)
        
        self.result_label = tk.Label(self.result_frame,
                                    text="Make your choice to start the battle!",
                                    font=('Segoe UI', 14),
                                    fg=self.colors["text_primary"],
                                    bg=self.colors["bg_secondary"],
                                    wraplength=600)
        self.result_label.pack(pady=10)
        
        # Control buttons
        control_frame = tk.Frame(game_frame, bg='transparent')
        control_frame.pack(pady=10)
        
        ttk.Button(control_frame, text="🔄 New Game", 
                  style='Modern.TButton',
                  command=self.new_game).pack(side='left', padx=5)
        
        ttk.Button(control_frame, text="❓ Help",
                  style='Modern.TButton', 
                  command=self.show_instructions).pack(side='left', padx=5)
        
        ttk.Button(control_frame, text="🏆 Leaderboard",
                  style='Modern.TButton',
                  command=self.show_leaderboard).pack(side='left', padx=5)
        
        ttk.Button(control_frame, text="⚙️ Settings",
                  style='Modern.TButton',
                  command=self.show_settings).pack(side='left', padx=5)
        
        ttk.Button(control_frame, text="❌ Quit",
                  style='Danger.TButton',
                  command=self.quit_game).pack(side='left', padx=5)
        
    def create_footer(self):
        """Create footer with additional info"""
        footer_frame = tk.Frame(self.main_frame, bg='transparent')
        self.main_frame.create_window(500, 750, window=footer_frame)
        
        round_info = tk.Label(footer_frame,
                             text=f"Round {self.current_round} of {self.max_rounds}",
                             font=('Segoe UI', 10),
                             fg=self.colors["text_secondary"],
                             bg='transparent')
        round_info.pack()
        
    def create_status_bar(self):
        """Create status bar at bottom"""
        self.status_bar = tk.Label(self.root,
                                  text="Ready to play!",
                                  font=('Segoe UI', 9),
                                  fg=self.colors["text_primary"],
                                  bg=self.colors["bg_tertiary"],
                                  anchor='w',
                                  relief='sunken',
                                  bd=1)
        self.status_bar.pack(side='bottom', fill='x')
        
    def player_choice(self, choice):
        """Handle player choice"""
        if self.timer_running:
            return
            
        self.start_timer()
        computer_choice = self.get_computer_choice()
        result = self.determine_winner(choice, computer_choice)
        
        self.display_result(choice, computer_choice, result)
        self.update_score(result)
        self.check_game_end()
        
        if self.sound_enabled:
            self.play_sound_effect(choice)
            
    def get_computer_choice(self):
        """Get computer choice based on difficulty"""
        if self.difficulty == "Easy":
            # Computer makes more random choices
            return random.choice(self.choices)
        elif self.difficulty == "Hard":
            # Computer tries to counter player's most used choice
            # For now, just random (could implement AI logic)
            return random.choice(self.choices)
        else:  # Normal
            return random.choice(self.choices)
            
    def determine_winner(self, player_choice, computer_choice):
        """Determine the winner of the round"""
        if player_choice == computer_choice:
            return "tie"
        elif computer_choice in self.rules[player_choice]:
            return "player"
        else:
            return "computer"
            
    def display_result(self, player_choice, computer_choice, result):
        """Display the result of the round"""
        player_emoji = self.choice_emojis[player_choice]
        computer_emoji = self.choice_emojis[computer_choice]
        
        if result == "tie":
            result_text = f"🤝 TIE!\n{player_emoji} {player_choice} vs {computer_choice} {computer_emoji}"
            color = self.colors["warning"]
        elif result == "player":
            beaten = [choice for choice in self.rules[player_choice] if choice == computer_choice][0]
            result_text = f"🎉 YOU WIN!\n{player_emoji} {player_choice} beats {computer_choice} {computer_emoji}"
            color = self.colors["success"]
        else:
            result_text = f"💥 COMPUTER WINS!\n{computer_emoji} {computer_choice} beats {player_choice} {player_emoji}"
            color = self.colors["danger"]
            
        self.result_label.config(text=result_text, fg=color)
        
    def update_score(self, result):
        """Update the game score"""
        if result == "player":
            self.player_score += 1
            self.update_status("You scored a point! 🎯")
        elif result == "computer":
            self.computer_score += 1
            self.update_status("Computer scored a point! 🤖")
        else:
            self.ties += 1
            self.update_status("It's a tie! 🤝")
            
        self.total_games += 1
        self.current_round += 1
        
        self.score_label.config(text=f"You: {self.player_score} | Computer: {self.computer_score} | Ties: {self.ties}")
        
    def check_game_end(self):
        """Check if the game has ended"""
        if self.current_round > self.max_rounds:
            self.end_game()
            
    def end_game(self):
        """End the current game"""
        self.stop_timer()
        
        if self.player_score > self.computer_score:
            winner_text = "🏆 CONGRATULATIONS! YOU WON THE GAME!"
            self.update_status("Victory! You are the champion! 👑")
        elif self.computer_score > self.player_score:
            winner_text = "🤖 COMPUTER WINS THE GAME!"
            self.update_status("Better luck next time! 🎮")
        else:
            winner_text = "🤝 IT'S A TIE GAME!"
            self.update_status("What an epic battle! 💥")
            
        # Save to leaderboard
        self.save_game_result()
        
        # Show end game dialog
        play_again = messagebox.askyesno("Game Over", 
                                        f"{winner_text}\n\nFinal Score:\nYou: {self.player_score}\nComputer: {self.computer_score}\nTies: {self.ties}\n\nWould you like to play again?")
        
        if play_again:
            self.new_game()
        else:
            self.quit_game()
            
    def new_game(self):
        """Start a new game"""
        self.player_score = 0
        self.computer_score = 0
        self.ties = 0
        self.total_games = 0
        self.current_round = 1
        self.time_left = 30
        
        self.score_label.config(text=f"You: {self.player_score} | Computer: {self.computer_score} | Ties: {self.ties}")
        self.result_label.config(text="Make your choice to start the battle!", 
                                fg=self.colors["text_primary"])
        self.timer_label.config(text=f"{self.time_left}s", fg=self.colors["accent"])
        
        self.update_status("New game started! Let the battle begin! ⚔️")
        
    def reset_score(self):
        """Reset just the score without starting new game"""
        self.player_score = 0
        self.computer_score = 0
        self.ties = 0
        self.score_label.config(text=f"You: {self.player_score} | Computer: {self.computer_score} | Ties: {self.ties}")
        self.update_status("Score reset! 🔄")
        
    def start_timer(self):
        """Start the round timer"""
        if self.timer_running:
            return
            
        self.timer_running = True
        self.time_left = 30
        self.timer_thread = threading.Thread(target=self._timer_countdown)
        self.timer_thread.daemon = True
        self.timer_thread.start()
        
    def _timer_countdown(self):
        """Timer countdown in separate thread"""
        while self.time_left > 0 and self.timer_running:
            time.sleep(1)
            self.time_left -= 1
            
            # Update timer display
            if self.time_left <= 5:
                color = self.colors["danger"]
            elif self.time_left <= 10:
                color = self.colors["warning"]
            else:
                color = self.colors["accent"]
                
            self.root.after(0, lambda: self.timer_label.config(text=f"{self.time_left}s", fg=color))
            
        if self.time_left <= 0 and self.timer_running:
            self.root.after(0, self._timer_expired)
            
    def _timer_expired(self):
        """Handle timer expiration"""
        self.timer_running = False
        self.update_status("Time's up! Computer gets the point! ⏰")
        self.computer_score += 1
        self.total_games += 1
        self.current_round += 1
        self.score_label.config(text=f"You: {self.player_score} | Computer: {self.computer_score} | Ties: {self.ties}")
        self.result_label.config(text="⏰ TIME'S UP! Computer wins by default!", 
                                fg=self.colors["danger"])
        self.check_game_end()
        
    def stop_timer(self):
        """Stop the timer"""
        self.timer_running = False
        
    def play_sound_effect(self, choice):
        """Play sound effect (placeholder - would need actual sound files)"""
        # This would play actual sound files in a real implementation
        # For now, just update status
        sound_effects = {
            "Rock": "🎵 *THUD*",
            "Paper": "🎵 *RUSTLE*", 
            "Scissors": "🎵 *SNIP*",
            "Spock": "🎵 *ZAP*",
            "Lizard": "🎵 *HISS*"
        }
        if self.sound_enabled:
            self.update_status(f"Sound: {sound_effects.get(choice, '🎵')}")
            
    def show_instructions(self):
        """Show game instructions"""
        instructions = """
🎮 ROCK PAPER SCISSORS SPOCK LIZARD

RULES:
• Rock crushes Scissors and Lizard
• Paper covers Rock and disproves Spock  
• Scissors cuts Paper and decapitates Lizard
• Spock vaporizes Rock and smashes Scissors
• Lizard eats Paper and poisons Spock

HOW TO PLAY:
• Click on your choice
• You have 30 seconds per round
• Play 5 rounds to complete a game
• Beat the computer to win!

FEATURES:
• Timer countdown for each round
• Score tracking and leaderboard
• Sound effects and modern UI
• Difficulty settings
• Keyboard shortcuts (Ctrl+N for new game, Ctrl+Q to quit)

Good luck and have fun! 🚀
        """
        
        messagebox.showinfo("Game Instructions", instructions)
        
    def show_leaderboard(self):
        """Show leaderboard"""
        leaderboard_window = tk.Toplevel(self.root)
        leaderboard_window.title("🏆 Leaderboard")
        leaderboard_window.geometry("400x500")
        leaderboard_window.configure(bg=self.colors["bg_primary"])
        
        # Title
        tk.Label(leaderboard_window, text="🏆 TOP PLAYERS",
                font=('Segoe UI', 18, 'bold'),
                fg=self.colors["accent"],
                bg=self.colors["bg_primary"]).pack(pady=20)
        
        # Leaderboard list
        lb_frame = tk.Frame(leaderboard_window, bg=self.colors["bg_secondary"])
        lb_frame.pack(fill='both', expand=True, padx=20, pady=10)
        
        if not hasattr(self, 'leaderboard') or not self.leaderboard:
            tk.Label(lb_frame, text="No games played yet!\nPlay some games to see the leaderboard.",
                    font=('Segoe UI', 12),
                    fg=self.colors["text_secondary"],
                    bg=self.colors["bg_secondary"]).pack(expand=True)
        else:
            # Sort leaderboard by score
            sorted_scores = sorted(self.leaderboard, 
                                 key=lambda x: (x['wins'], x['total_games']), 
                                 reverse=True)[:5]
            
            for i, entry in enumerate(sorted_scores):
                rank_text = f"#{i+1} - Wins: {entry['wins']}/{entry['total_games']} - {entry['date']}"
                tk.Label(lb_frame, text=rank_text,
                        font=('Segoe UI', 10),
                        fg=self.colors["text_primary"],
                        bg=self.colors["bg_secondary"]).pack(pady=5)
                
    def show_settings(self):
        """Show settings dialog"""
        settings_window = tk.Toplevel(self.root)
        settings_window.title("⚙️ Settings")
        settings_window.geometry("300x250")
        settings_window.configure(bg=self.colors["bg_primary"])
        
        # Title
        tk.Label(settings_window, text="⚙️ GAME SETTINGS",
                font=('Segoe UI', 16, 'bold'),
                fg=self.colors["accent"],
                bg=self.colors["bg_primary"]).pack(pady=20)
        
        # Sound setting
        sound_frame = tk.Frame(settings_window, bg=self.colors["bg_primary"])
        sound_frame.pack(pady=10)
        
        self.sound_var = tk.BooleanVar(value=self.sound_enabled)
        tk.Checkbutton(sound_frame, text="🔊 Sound Effects",
                      variable=self.sound_var,
                      font=('Segoe UI', 12),
                      fg=self.colors["text_primary"],
                      bg=self.colors["bg_primary"],
                      selectcolor=self.colors["bg_secondary"],
                      activebackground=self.colors["bg_primary"],
                      command=lambda: setattr(self, 'sound_enabled', self.sound_var.get())).pack()
        
        # Difficulty setting
        diff_frame = tk.Frame(settings_window, bg=self.colors["bg_primary"])
        diff_frame.pack(pady=10)
        
        tk.Label(diff_frame, text="🎯 Difficulty:",
                font=('Segoe UI', 12, 'bold'),
                fg=self.colors["text_primary"],
                bg=self.colors["bg_primary"]).pack()
        
        self.diff_var = tk.StringVar(value=self.difficulty)
        for difficulty in ["Easy", "Normal", "Hard"]:
            tk.Radiobutton(diff_frame, text=difficulty,
                          variable=self.diff_var,
                          value=difficulty,
                          font=('Segoe UI', 10),
                          fg=self.colors["text_primary"],
                          bg=self.colors["bg_primary"],
                          selectcolor=self.colors["bg_secondary"],
                          activebackground=self.colors["bg_primary"],
                          command=lambda: setattr(self, 'difficulty', self.diff_var.get())).pack()
        
        # Close button
        ttk.Button(settings_window, text="✅ Apply",
                  style='Modern.TButton',
                  command=settings_window.destroy).pack(pady=20)
        
    def save_game_result(self):
        """Save game result to leaderboard"""
        if not hasattr(self, 'leaderboard'):
            self.leaderboard = []
            
        game_result = {
            'wins': self.player_score,
            'losses': self.computer_score,
            'ties': self.ties,
            'total_games': self.total_games,
            'date': datetime.now().strftime("%Y-%m-%d %H:%M")
        }
        
        self.leaderboard.append(game_result)
        
        # Save to file
        try:
            with open('leaderboard.json', 'w') as f:
                json.dump(self.leaderboard, f)
        except:
            pass  # Ignore file errors
            
    def load_leaderboard(self):
        """Load leaderboard from file"""
        try:
            if os.path.exists('leaderboard.json'):
                with open('leaderboard.json', 'r') as f:
                    self.leaderboard = json.load(f)
            else:
                self.leaderboard = []
        except:
            self.leaderboard = []
            
    def update_status(self, message):
        """Update status bar message"""
        self.status_bar.config(text=message)
        
    def quit_game(self):
        """Quit the application"""
        if messagebox.askyesno("Quit Game", "Are you sure you want to quit?"):
            self.stop_timer()
            self.root.quit()
            
    def run(self):
        """Start the game"""
        self.root.mainloop()

if __name__ == "__main__":
    game = RPSLSGame()
    game.run()