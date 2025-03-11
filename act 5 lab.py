def classify_age(age):
    if age < 0:
        print("there is no such age that is less than 1 second after being born.")
    elif age <= 12:
        print("You are a Child.")
    elif age <= 19:
        print("You are a Teen.")
    elif age <= 64:
        print("You are an Adult.")
    else:
        print("You are a Senior.")

#Age Configuration
classify_age(12)
classify_age(15)
classify_age(30)
classify_age(70)
classify_age(-5)
classify_age(64)
classify_age(18)

#EPHRAIM JESTIE G. ROSARIO
#12-BSCPE-01