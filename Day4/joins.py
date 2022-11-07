web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
result = ' #'.join(web_tech)
print(result) # 'HTML CSS JavaScript React'

web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
result = ', '.join(web_tech)
print(result) # 'HTML CSS JavaScript React'

web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
result = ' , '.join(web_tech)
print(web_tech)

web_tech = ['HTML', 'CSS', 'JavaScript','React']
result = ' #'.join(web_tech)
print(web_tech)

challenge = 'thirty days of python'
print(challenge.strip('noth')) # 'irty days of py'

challenge = 'thirty days of python'
print(challenge.replace('python', 'coding')) # 'thirty days of coding'

challenge = 'thirty days of python'
print(challenge.title()) # Thirty Days Of Python

challenge = 'thirty days of python'
print(challenge.swapcase())   # THIRTY DAYS OF PYTHON
challenge = 'Thirty Days Of Python'
print(challenge.swapcase())  # tHIRTY dAYS oF pYTHON

challenge = 'thirty days of python'
print(challenge.startswith('thirty')) # True

challenge = '30 days of python'
print(challenge.startswith('thirty')) # False
