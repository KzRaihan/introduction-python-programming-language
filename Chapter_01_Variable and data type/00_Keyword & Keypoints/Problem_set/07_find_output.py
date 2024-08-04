"""   
 -> Find the output the provide code

      str1 = "Raihan"
      num = 3
      result = str1 + "Kz" * num
"""

str1 = "Raihan"
num = 3
result = str1 + "Kz" * num
print(result)  # o/p: RaihanKzKzKz

# result = str1 + "Kz" * num
#        = "Raihan" + "Kz" * 3                        # -> First  : *
#        = "Raihan" +  "KzKzKz"                       # -> Second : +
#        = "RaihanKzKzKz"                             # -> Third  : =