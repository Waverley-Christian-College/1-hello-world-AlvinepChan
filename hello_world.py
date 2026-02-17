import random

warbonds = ["Steeled Veteran", "Cutting Edge", "Polar Patriots", "Democratic Detonation", "Viper Commandos", "Freedom's Flame", "Chemical Agents", "Truth Enforcers", "Urban Legends", "Force Of Law", "Servants Of Freedom", "Masters Of Ceromony", "Dust Devils", "Python Commandos", "Siege Breakers", "Borderline Justice", "Redacted Regiment"]

print("[Terminal Initializing...]")

print("[Terminal Connection Status: GALLANTRY BEYOND MEASURE]")

print("[Connection Location: DSS]")

print(" Welcome To The DSS Warbond Acquisition Recommendation Terminal")

helldiver_terminal_input = input("Please Enter Helldiver ID For Server To Provide Warbond Acquisition Recommendation: ")

helldiver_recommended_warbond = random.choice(warbonds)



print("[Requesting Data From DSS Server...]")

print("[Server Data Recieved]")

print(f"Warbond Recommended For {helldiver_terminal_input}: {helldiver_recommended_warbond}")

print("Long Live Liberty!")

