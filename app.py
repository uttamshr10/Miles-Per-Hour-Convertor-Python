print("Welcome to the Miles Per Hour to Meters Per Second Conversion App")

# Gather user input.
mph = float(input("What is your speed in miles per hour: "))

# Convert to meters per second 1 mps = mph*0.4474
mps = mph*0.4474
convertor = round(mps, 2)
# Converting float into string because we cannot concatenate float.
print("Your speed in meters per second is " + str(convertor) + ".")
