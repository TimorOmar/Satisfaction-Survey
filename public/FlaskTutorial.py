#Informed xp Challenge
#Gianna Flores Aguilar & Timor Omar

#which product is being reviewed
product = str(input("Will you be reviewing A) Smart TV or B) Wireless Speaker?: "))
if product == "A" or product == "a":
	#takes user data
	manual = int(input("How satisfied are you with how self explanatory the manual/setting up instructions were?: "))
	user_friendly = int(input("How satisfies are you with your ability to navigate your SmartTV?: "))
	confidence = int(input("How satisfied are you with your ability to use your device? "))
	remote = int(input("How satisfied are you with the userbility of the remote control?: "))
	usefulness_micro = int(input("You feel (insert satisfactory level) having the microphone button: "))

	score = (manual + user_friendly + confidence + remote + usefulness_micro)
	if 5 <= score <= 13:
		satisfaction = "Overall Unsatisfied"
	elif 14 <= score <= 22:
		satisfaction = "Overall Satisfied"
	elif 23 <= score <= 25:
		satisfaction = "Overall Very Satisfied"

	if manual == 3:
		resultq1 = "-No pressing feedback regarding the manual."
	if manual < 3:
		resultq1 = "-The customer had trouble using the manual provided for setting up."
	elif manual > 3:
		resultq1 = "-The customer was satisfied with the manual provided for setting up."

	if user_friendly == 3:
		resultq3 = "-No pressing feedback regarding navigation."
	if user_friendly < 3:
		resultq3 = "-The customer did not find our product user friendly."
	elif user_friendly > 3:
		resultq3 = "-The customer was satisfied with how user friendly our product was."

	if confidence == 3:
		resultq4 = "-No pressing feedback regarding confidence in ability to use product."
	if confidence < 3:
		resultq4 = "-The customer is not confident in their abilities to use their product."
	elif confidence > 3:
		resultq4 = "-The customer feels confident in their abilities to use their product to the full extent."

	if remote == 3:
		resultq5 = "-No pressing feedback regarding the remote control."
	if remote < 3:
		resultq5 = "-The customer does not find the remote provided user-friendly."
	elif remote > 3:
		resultq5 = "-The customer finds the remote provided user-friendly."

	if usefulness_micro == 3:
		resultq6 = "-No pressing feedback regarding the microphone feature of the remote control."
	if usefulness_micro < 3:
		resultq6 = "-The customer does not find the microphone button very useful."
	elif usefulness_micro == 4:
		resultq6 = "-The customer finds use in having the microphone button."
	elif usefulness_micro == 5:
		resultq6 = "-The customer finds significant use in having the microphone button."


elif product == "B" or product == "b":
	manual = int(input("How satsisfied are you with how self explanatory the manual/setting up instructions were?: "))
	privacy = int(input("How satsified are you with our privacy policies?: "))
	user_friendly = int(input("How satisfied are you with the bluetooth pairing feature?: "))
	confidence = int(input("How satisfied are you with your ability to use your device? "))
	usefulness_blue = int(input("You feel (insert satisfactory level) being able to pair multiple devices: "))

	score = (manual + privacy + user_friendly + confidence  + usefulness_blue)
	if 5 <= score <= 13:
		satisfaction = "Overall Unsatisfied"
	elif 14 <= score <= 22:
		satisfaction = "Overall Satisfied"
	elif 23 <= score <= 25:
		satisfaction = "Overall Very Satisfied"

	#analyzes data
	if manual == 3:
		resultq1 = "-No pressing feedback regarding manual/setting up instructions."
	if manual < 3:
		resultq1 = "-The customer had trouble using the manual provided for setting up."
	elif manual > 3:
		resultq1 = "-The customer was satisfied with the manual provided for setting up."

	if privacy == 3:
		resultq2 = "-No pressing feedback regarding privacy concerns."
	if privacy < 3:
		resultq2 = "-The customer has privacy concerns."
	elif privacy > 3:
		resultq2 = "-Privacy is not a concern to this customer."

	if user_friendly == 3:
		resultq3 = "-No pressing feedback the bluetooth pairing feature."
	if user_friendly < 3:
		resultq3 = "-The customer did not find our product user friendly."
	elif user_friendly > 3:
		resultq3 = "-The customer was satisfied with how user friendly our product was."

	if confidence == 3:
		resultq4 = "-No pressing feedback regarding confidence in ability to use the device."
	if confidence < 3:
		resultq4 = "-The customer is not confident in their abilities to use their product."
	elif confidence > 3:
		resultq4 = "-The customer feels confident in their abilities to use their product to the full extent."

	if usefulness_blue == 3:
		resultq7 = "-No pressing feedback regarding the ability to pair multiple devices."
	if usefulness_blue < 3:
		resultq7 = "-The customer finds that the ability to pair multiple devices is not useful."
	elif usefulness_blue == 4:
		resultq7 = "-The customer finds that the ability to pair multiple devices is useful."
	elif usefulness_blue == 5:
		resultq7 = "-The customer finds that the ability to pair multiple devices is significantly useful."

if product == "A" or product == "B":
	suggestions = str(input("Please leave any suggestions you may have: "))





#creates report
print ()
ask_forreport = str(input("Create satisfactory report?: "))
if ask_forreport == "Yes" or ask_forreport == "yes" or ask_forreport == "y" or ask_forreport == "Y":
	print ()
	print ("*******************************************************************")
	print ("Satisfactory Report:")
	print (resultq1)
	if product == "B":
		print (resultq2)
	print (resultq3)
	print (resultq4)
	if product == "A":
		print (resultq5)
		print (resultq6)
	if product == "B":
		print (resultq7)
	print ("Suggestions: " + suggestions)
	print ("*******************************************************************")
	print ("This concludes the survey. Thank you for participating!")



#creates satisfaction score
	print ()
	print ("Overall Satisfaction Score (out of 25 possible points): ")
	print (str(score) + "/25")
	print (satisfaction)

elif ask_forreport == "No" or ask_forreport == "no" or ask_forreport == "n" or ask_forreport == "N":
	print ("This concludes the survey. Thank you for participating!")
