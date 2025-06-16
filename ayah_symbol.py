def create_ayah_symbol(number):
    """
    Creates an Arabic End of Ayah symbol with the number appearing inside.
    Uses Unicode's special number formatting for the End of Ayah symbol.
    
    Args:
        number (int): The Ayah number to display (1-999)
    
    Returns:
        str: The Ayah symbol with the number inside
    """
    # Convert to Arabic-Indic numerals using Unicode range
    # The Unicode range for Arabic-Indic digits starts at 0x0660
    arabic_number = ''.join(chr(0x0660 + int(d)) for d in str(number))
    
    # Use Unicode's special End of Ayah marker with the number
    # U+06DD is the Arabic End of Ayah symbol
    return chr(0x06DD) + arabic_number

def print_text_with_ayah_symbols(text, ayah_numbers):
    """
    Prints text with Ayah end symbols.
    
    Args:
        text (list): List of strings, each representing an Ayah
        ayah_numbers (list): List of corresponding Ayah numbers
    """
    for verse, number in zip(text, ayah_numbers):
        print(f"{verse} {create_ayah_symbol(number)}")

# Example usage
if __name__ == "__main__":
    # Example text with Ayah numbers
    sample_text = [
        "بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ",
        "الْحَمْدُ لِلَّهِ رَبِّ الْعَالَمِينَ",
        "الرَّحْمَٰنِ الرَّحِيمِ"
    ]
    ayah_numbers = [5, 6, 7]
    
    # Print sample text with Ayah symbols
    print("\nFull verses with Ayah symbols:")
    print_text_with_ayah_symbols(sample_text, ayah_numbers)
