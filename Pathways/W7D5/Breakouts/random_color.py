# write a randomized color guessing game where the user has to guess the color of a randomly generated RGB value and the color is validated by the user input

import random

def generate_random_rgb():
    """Generate a random RGB color tuple"""
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

def rgb_to_color_name(r, g, b):
    """Convert RGB values to approximate color name"""
    # Define color ranges for basic colors
    if r > 200 and g < 100 and b < 100:
        return "red"
    elif r < 100 and g > 200 and b < 100:
        return "green"
    elif r < 100 and g < 100 and b > 200:
        return "blue"
    elif r > 200 and g > 200 and b < 100:
        return "yellow"
    elif r > 200 and g < 100 and b > 200:
        return "magenta"
    elif r < 100 and g > 200 and b > 200:
        return "cyan"
    elif r > 200 and g > 200 and b > 200:
        return "white"
    elif r < 50 and g < 50 and b < 50:
        return "black"
    elif r > 150 and g > 100 and b < 100:
        return "orange"
    elif r > 100 and g < 100 and b < 100:
        return "brown"
    elif r > 150 and g > 150 and b > 150:
        return "gray"
    elif r < 150 and g < 150 and b < 150:
        return "dark gray"
    else:
        # For mixed colors, determine the dominant component
        max_val = max(r, g, b)
        if max_val == r:
            return "red"
        elif max_val == g:
            return "green"
        else:
            return "blue"

def get_valid_colors():
    """Return list of valid color names for user reference"""
    return ["red", "green", "blue", "yellow", "magenta", "cyan", 
            "white", "black", "orange", "brown", "gray", "dark gray"]

def display_rgb_values(r, g, b):
    """Display RGB values in a formatted way"""
    print(f"\nRGB Values: R={r}, G={g}, B={b}")
    print(f"Hex Value: #{r:02x}{g:02x}{b:02x}")
    
    # Create a simple visual representation
    print("\nVisual representation (intensity bars):")
    print(f"Red:   {'█' * (r // 10)}")
    print(f"Green: {'█' * (g // 10)}")
    print(f"Blue:  {'█' * (b // 10)}")

def play_round():
    """Play one round of the color guessing game"""
    # Generate random RGB values
    r, g, b = generate_random_rgb()
    correct_color = rgb_to_color_name(r, g, b)
    
    # Display RGB values to user
    display_rgb_values(r, g, b)
    
    # Get user's guess
    print(f"\nValid colors: {', '.join(get_valid_colors())}")
    user_guess = input("What color do you think this RGB value represents? ").strip().lower()
    
    # Validate the guess
    if user_guess == correct_color:
        print(f"🎉 Correct! The color is {correct_color}!")
        return True
    else:
        print(f"❌ Sorry, the correct color is {correct_color}.")
        return False

def main():
    """Main game function"""
    print("Welcome to the RGB Color Guessing Game!")
    print("=" * 40)
    print("I'll show you RGB values and you guess the color!")
    print("Try to identify the color based on the RGB values.\n")
    
    score = 0
    total_rounds = 0
    
    while True:
        print(f"\n{'='*20} Round {total_rounds + 1} {'='*20}")
        
        # Play one round
        if play_round():
            score += 1
        
        total_rounds += 1
        
        # Show current score
        percentage = (score / total_rounds) * 100 if total_rounds > 0 else 0
        print(f"\nCurrent Score: {score}/{total_rounds} ({percentage:.1f}%)")
        
        # Ask if user wants to continue
        play_again = input("\nDo you want to play another round? (y/n): ").strip().lower()
        if play_again not in ['y', 'yes']:
            break
    
    # Final score
    print(f"\n{'='*20} GAME OVER {'='*20}")
    print(f"Final Score: {score}/{total_rounds}")
    if total_rounds > 0:
        percentage = (score / total_rounds) * 100
        print(f"Accuracy: {percentage:.1f}%")
        
        if percentage >= 80:
            print("🏆 Excellent! You have great color recognition!")
        elif percentage >= 60:
            print("👍 Good job! You're getting the hang of it!")
        elif percentage >= 40:
            print("💪 Not bad! Keep practicing to improve!")
        else:
            print("🎯 Keep trying! Color recognition takes practice!")
    
    print("Thanks for playing!")

# Additional utility function for testing specific RGB values
def test_color(r, g, b):
    """Test a specific RGB color - useful for debugging"""
    print(f"Testing RGB({r}, {g}, {b})")
    display_rgb_values(r, g, b)
    color = rgb_to_color_name(r, g, b)
    print(f"Detected color: {color}")

if __name__ == "__main__":
    main()
