# ManageBackgroundLooks/background_choices.py

from OpenColabAI.settings import urls_paths


def background_choices():
    return [
        ('black', 'Dark Background'),
        ('white', 'Bright Background'),
        ('lightgray', 'Light Gray Background'),
        ('lightblue', 'Light Blue Background'),
        ('beige', 'Beige Background'),
        ('lightgreen', 'Light Green Background'),
        ('lightcoral', 'Light Coral Background')
    ]

# Example usage
# if __name__ == "__main__":
#     print(background_choices())

