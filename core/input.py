def obtain_user_input(input_info):

  try:
    message = input_info[0]
  except:
    message = "Message not defined"
  try: 
    value = input_info[1]
  except:
    value = str
  try:
    allow_empty = input_info[2]
  except:
    allow_empty = True
  try:
    split = input_info[3]
  except:
    split = [False, '']
  

  user_input = None
  loop = True

  # While loop to catch invalid inputs
  if split[0] == True:
    while loop:
      user_input = input(message)
      if not user_input and allow_empty == True:
        break
      if split[1] in user_input:
        user_input = user_input.split(split[1])
        if not value is str:
          for i in range(0, len(user_input), 1):
            if user_input[i]:
              if user_input[i].isdigit():
                try: 
                  user_input[i] = value(user_input[i].strip())
                except Exception as e:
                  print(f"Conversion error: {e}")
                  break
              else:
                print("Invalid input: Value(s) not numeric")
                break
            else:
              print("Invalid input: Empty value(s)")
              break
          for item in user_input:
            if not type(item) is value:
              loop = True
              break
            loop = False
        else:
          user_input = [user_in.strip() for user_in in user_input]
          for item in user_input:
            if not item:
              print("Invalid input: Empty value(s)")
              loop = True
              break
            loop = False
      else:
        if user_input:
          if not value is str:
            if user_input.isdigit():
              try:
                user_input = value(user_input.strip())
              except Exception as e:
                print(f"Conversion error: {e}")
          loop = False
        else:
          print("Invalid input: Empty value(s)")
  else:
    while loop:
      user_input = input(message)
      if user_input:
        if not value is str:
          try:
            user_input = value(user_input.strip())
            loop = False
          except Exception as e: 
            print(f"Conversion error: {e}")
        else:
          user_input = user_input.strip()
          loop = False
      elif allow_empty == True:
        loop = False
      else:
        print(f"Invalid input: Empty value")
  
  return user_input