print("Learn more about STEM! Answers: Science, Mathematics, Engineering! Pick a subject.")
enter1 = input()
enter1 = enter1.lower() #this makes everything lowercase so it won't be case sensitive
if enter1 == "science":
  enter2 = input("What specific subject would you like to know about? Answers: Physics, Biology, Chemistry, Computer Science. ")
  enter2 = enter2.lower()
  if enter2 == "physics": 
    enter3 = input("Cool! Which type of physics? Answer: Classical Mechanics, Modern Physics ")
    enter3 = enter3.lower()
    if enter3 == "classical physics":
         print("Awesome! Here are some research project ideas.")
    if enter3 == "modern physics":
         print("Awesome! Here are some research project ideas.")
  elif enter2 == "biology": 
    enter3 = input("Cool! Which field of biology? Answer: Botany, Zoology, Microbiology, Anatomy, Evolutionary, Molecular? ")
    enter3 = enter3.lower()
    if enter3 == "botany":
         print("Awesome! Here are some research project ideas.")
    elif enter3 == "zoology":
         print("Awesome! Here are some research project ideas.")
    elif enter3 == "microbiology":
         print("Awesome! Here are some research project ideas.")
    elif enter3 == "anatomy":
         print("Awesome! Here are some research project ideas.")
    elif enter3 == "evolutionary":
         print("Awesome! Here are some research project ideas.")
    elif enter3 == "molecular":
         print("Awesome! Here are some research project ideas.")
  
  elif enter2 == "chemistry": 
    enter3 = input("Cool! Which field of Chemistry? Answer: Organic, Inorganic, Physical, Analytical, Biochemistry?")
    enter3 = enter6.lower
    if enter3 == "organic":
         print("Awesome! Here are some research project ideas.")
    elif enter3 == "inorganic":
         print("Awesome! Here are some research project ideas.")
    elif enter3 == "physical":
         print("Awesome! Here are some research project ideas.")
    elif enter3 == "analytical":
         print("Awesome! Here are some research project ideas.")
    elif enter3 == "biochemistry":
         print("Awesome! Here are some research project ideas.")
  
  elif enter3 == "computer science": 
    print("Alright, what field? Answers: Theoretical, Computer Engineering, Applications") #way too many branches need to narrow down and add
    enter3 = input()
    enter3 = enter7.lower()
    if enter3 == "theoretical":
      print("Awesome! Here are some project ideas!")
    if enter3 == "computer engineering":
      print("Awesome! Here are some things you can do!")
    if enter3 == "applications": 
      print("Awesome! Which application field?")
      enter4 = input("ML, AR/VR, NLP, Image Processing, CV")
  
if enter1 == "engineering":
  enter2 = input("Cool! Which field of engineering? Answer: Chemical, Civil, Mechanical, Electrical, Biomedical, Environmental, Biotech, Nanotech?")
  enter2 = enter2.lower()
if enter1 == "mathematics": 
  enter2 = input("What specific subject would you like to know about? Answers: Geometry, Trigonometry, Calculus, Algebra, Statistics. ")
  enter2 = enter2.lower()
else: 
  print("Please try to run the program again, and adjust to the necessary choices.")