# python notes 
  
  ## 1. check python version
  import sys
  print (sys.version)

  ## 2. don't name any code file the same as library
  this will cause an error

  ## 3. (ctrl + ظ )    هتحول الكود لكومنت و العكس صحيح
  <!-- print("programming") -->

  ## 4. """ bla bla bla """  Triple double quotes are strings, not comments

  *some data types*
  ## 5. int - integars numbers     =>        `print (type(10))`
  ## 6. float - floating point number   =>   `print (type(100.99))`
  ## 7. str - string          =>             `print (type("hello"))`
  ## 8. bool - boolean       =>              `print (type( 2 == 2 ))`, (2 == 4)   *yes or no*
  ## 9. list                 =>              `print (type([1, 2, 3, 4]))`          *use []*
  ## 10. tuple               =>              `print (type((1, 2, 3, 40)))`         *use ()*
  ## 11. dict - dictionary    =>    `print (type ({ "one" : 1, "two" : 2 }))` *key and value*
  <!-- لما بنكتب التايب وبعدين ندخل المتغيرات بيطلع نوع المتغير مش بيطبعه -->

  don't forget semicolon and You need indentation after the `if` statement, or Python will give an error.
  ## 12. `if 1<8:`                     
  ##        `print("one is less than eight")`

  *variables Name rules*
   - syntax  =>  [ myvariable = "value" ]
  ## 13. can start with (a-z A-Z) or underscore
  ## 14. cannot start with numbers or special character 
  ## 15. can include (0:9) or underscore
  ## 16. name is not as name Variable names are case-sensitive (age, Age and AGE are three different variables)
  ## Remember that variable names are case-sensitive
   name - normal   ,    myName - camelcase    ,    my_name - snake_case
  ##  don't use double quotation on "print (name)"
   `name = 10`
    `print (name)`

  ## 17. python is dynamic typing that means The last value assigned to the variable is what gets printed as the output.
  `x = 10`
  `x = "hi" `
  `print (x)`              then output = hi  

  ## 18.`help("keywords)` بتعرض الكلمات المحجوزه يعني مقدرش استعملها عشان هي تبع اللغه 

  ## 19. بالنسبه للارقام بنكتبها علي طول من غير ما نقول انها انتجر مثلا 
   `age = 20      NOT       age = int(20)`           دي بتكون منسقه اكتر
   كمان في الاوتبوب لما اجي اكبعها لازم اكتب سترينج الادج عشان يطبع الرقم يا اما مش هيطبعه

## 20. Notice the space character after "Python " and "is ", without them the result would be "Pythonisawesome", this only if i use "+" 
`x = "Python "`
`y = "is "`
`z = "awesome"`
`print(x + y + z)`

## 21. global variable any one can use cause it's public, it placed in/out the function
   go to variable1.py for code

## 22. global keyword,fisrt: if we have variable inside a func() then it's global but if we want convert it into public then we have to use global keyword, code on variable1.py
## 23. second: A global variable can be read inside any function, but its value can only be changed inside the function by using the global keyword, code in variable1.py