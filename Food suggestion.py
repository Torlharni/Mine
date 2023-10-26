#Name: SEKONI QUDUS
#Department: COMPUTER SCIENCE
#LEVEL: 300 LEVEL
#COURSE TITLE: ARTIFICIAL INTELLIGENCE
#Lecturer's Name: MR. IDRIS

#Assignment: Create a Program to Suggest food according to weather

food_suggestions = {
    'cold': {
        'freezing': ['Pap and Akara', 'Pepper soup', 'Hot Coffee and Bread'],
        'cool': ['rice and stew'],
    },
    'hot': {
        'sunny': ['Jollof rice', 'Eba and Egusi', 'White rice and Stew', 'Bread and Beans', 'Garri and Kuli Kuli'],
        'rainy': ['Hot Soup', 'Spaghetti'],
    }
}
#Get user input for weather conditions
weather = input("Enter the current weather condition (e.g., sunny, rainy, cold, hot): ").lower()

#check if the weather conditions is in the dictionary
if weather in food_suggestions:
    suggested_food = food_suggestions[weather]

    print("suggested_food: ", suggested_food)
else:
    print("weather condition not found in suggestions.")