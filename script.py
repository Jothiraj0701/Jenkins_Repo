# script.py

def generate_fruit_love_message(fruit):
    """
    Generates a message expressing love for a fruit.
    
    Args:
        fruit (str): The name of the fruit.
    
    Returns:
        str: A message expressing love for the fruit.
    """
    return f"I have a profound affection for {fruit}s."

def main():
    fruits = ["apple", "banana", "orange", "grape", "pineapple","mango"]
    for fruit in fruits:
        print(generate_fruit_love_message(fruit))

if __name__ == "__main__":
    main()
