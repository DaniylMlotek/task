import math
operation = input('''
*
/
+
-
sin
cos
select your operation:
''')

x = int(input('enter your first number:'))
y = int(input('enter your second number:'))


if operation == '*':
    print('your result',x*y)
elif operation == '/':
    print('your result',x/y)
elif operation == '+':
    print('your result',x+y)
elif operation == '-':
        print('your result',x-y)
elif operation == 'cos':
    print('result from the first digit',math.cos(x))
elif operation == 'sin':
    print('result from the first digit',math.sin(x))
else:
    print('incorrect operation,have a nice day')

