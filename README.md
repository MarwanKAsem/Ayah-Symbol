# Ayah-Symbol
📖 Ayah Symbol Generator (Arabic End of Verse Marker)
This Python script allows you to easily append Arabic End of Ayah symbols (۝) to verses with proper Arabic-Indic numeral formatting. Ideal for displaying Quranic text with accurate visual notation.

✨ Features
🕌 Automatically converts Ayah numbers to Arabic-Indic numerals.

🧾 Uses Unicode End of Ayah symbol U+06DD.

📜 Cleanly appends Ayah markers to verses for display or output.

🧠 How It Works
The script defines two main functions:

create_ayah_symbol(number)
Converts a given Ayah number into Arabic-Indic digits and appends the ۝ symbol.

print_text_with_ayah_symbols(text, ayah_numbers)
Prints each Ayah (verse) from a list and adds its corresponding End of Ayah symbol with the number.

🧪 Example
```
sample_text = [  "بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ", "الْحَمْدُ لِلَّهِ رَبِّ الْعَالَمِينَ", "الرَّحْمَٰنِ الرَّحِيمِ"]
ayah_numbers = [5, 6, 7]

print_text_with_ayah_symbols(sample_text, ayah_numbers)
```
Output:

بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ ۝٥
الْحَمْدُ لِلَّهِ رَبِّ الْعَالَمِينَ ۝٦
الرَّحْمَٰنِ الرَّحِيمِ ۝٧

🧰 Prerequisites
Python 3.6+

No external dependencies required


📂 Project Structure

├── ayah_symbol.py        
├── README.md             


📜 License
This project is licensed under the MIT License.


🙌 Contribution
Feel free to fork the repo, suggest features, or submit pull requests!
Perfect for use in Quranic apps, educational tools, or visual display formatting.

