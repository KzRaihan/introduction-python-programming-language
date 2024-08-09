# WAP to fill in a letter template given below with and date
"""    letter = '''
                   Dear </Name!>,
                   Your are Selected!
                   </Date!>
                '''

"""
letter = '''
         Dear </Name!>,
         Your are Selected!
         </Date!>

         '''
print(letter.replace("</Name!>", "Kz").replace("</Date!>", "10 August 2024"))

# this replace() return new string
# first replace = </Name!> into Kz and return new string 
# then this new string second replace = </Date!> into 10 August 2024 