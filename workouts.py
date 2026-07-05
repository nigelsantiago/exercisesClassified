import csv

def loadExercises():
    exerciseBook = {}
    with open("exercise_classifications.csv") as file:
        exerciseReader = csv.reader(file, delimiter=',')
        for exercise, classification in exerciseReader:
            exerciseBook[exercise] = classification
    return exerciseBook

def display_workout_plan(exerciseBook, userChoice):
    day = userChoice.lower()
    if (day == 'push' or day == 'pull'):
        for exercise in exerciseBook:
            if exerciseBook.get(exercise) == day:
                print(exercise)
    else:
        print("I see we're hitting legs today. Bye!")
    return

def main():
    exerciseBook = loadExercises()
    userChoice = input("What are you hitting today, 'push' or 'pull'? ")
    display_workout_plan(exerciseBook, userChoice)

if __name__ == "__main__":
    main()