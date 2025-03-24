
# Some strings to test the functions with.
test_string = "Hello World!"

test_string_two = "I am a string and I wish to be handled simply."

test_string_three = "This is a sentence I wish to test."

def alternate_character_casing(input_string):
   
  # Initialise the result string
  result_string = ""

   # Flatten the input string to lowercase characters
  input_string = input_string.lower()

   # Variable to get the length of the string
  string_tail = len(input_string)
   
   # Loop over string with for loop.
  for i in range(0, string_tail):
      
    # For every even index set the char to lower case.
    if i % 2 == 0:
          result_string += input_string[i].lower()

    # Else set the character to upper case.
    else:
          result_string += input_string[i].upper()
   
  return result_string


def alternate_word_casing(input_string):
  
  # Initialise the result string
  result_string = ""

  # Split the input_string into substrings and store in string_list
  string_list = input_string.split(' ')

  # Get the length of the string list
  word_length = len(string_list)

  # Loop over the list of strings
  for i in range(0, word_length):

    # If the index is divisible by 2 set all substring
    # characters to upper case.
    if i % 2 == 0:
      result_string += string_list[i].upper()

      # Reinsert  the whitespace character
      result_string += " "
    
    # Else set the substring characters to lower case.
    else:
      result_string += string_list[i].lower()
      # Reinsert  the whitespace character
      result_string += " "
  
  # Re-join the substrings with new whitespace characters.
  string_list = " ".join(string_list)
  
  # Return the resulting string
  return result_string


# Use functions with print()
print(alternate_character_casing(test_string))
print(alternate_character_casing(test_string_two))
print(alternate_character_casing(test_string_three))

print(alternate_word_casing(test_string))
print(alternate_word_casing(test_string_two))
print(alternate_word_casing(test_string_three))