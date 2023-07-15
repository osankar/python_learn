# Prints the user input back to screen after replacing :) with 😐 and :( with 🙁
x = input("Eter a sentence with faces: ")
print(x.replace(":)", "😐").replace(":(", "🙁"))