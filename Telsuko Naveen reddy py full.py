//========================================================================================
/*                                                                                      *
 *                                 Telsuko Naveen reddy                                 *
 *                                                                                      */
//========================================================================================


    VID 9.Objects memory management in python

        # In this vedio we'll talk about memory management in python
        
        # if we create a variable like below
num = 5 # it'll be having a name "num" as well as the memory address 

        # To know the memory address we can use inbuild function --> id() » We can pass any Object into this function to get the memory address
id(num) 
>140716985840000  # So this is the memory address of the variable "num"

        # So, every variable we create will be having a memory address

a = 10  # lets say we've created a variable a with int 10 init 
b = a   # here we're trying to set 'b' variable to 10 which is the value in 'a', 
            #! Note that Object that needs a value should be on LHS otherwise it wont work => b = a will not work 

        # So, here we've 2 variables, lets see if these 2 variables whose values are same  have same or different memory address
id(a)
>140716985840160    
id(b)                   # We can see that both variables a & b whose value is same have same memory address
>140716985840160


        # So, In python when we create multiple variables with same data in them, all the variables will have same memory address 
        # So, for this reason people will say python is data efficient in memory management, because its not creating multiple data unnecessarily here 
        # So, now lets also pass the int Object 10 to the id() function to know its memory address As id() function will take any Object, 
            # and also note that every Object in python will have memory address

id(10)
>140716985840160  #! Here we can see that Object 10 has same memory address as variable a & b (see above)

        # So, the important point that we can make out from this is 
        # Assigning memory address to a variable is not based on variable name, its based on the value\Object stored inside that variable 
        # In otherwords, variables a & b are assigned with memory address which belongs to the value\Object that is inside these variables that is 10

        # so when we define a variable, and assign a value to it, the memory address of that value will be assigned to holding variable 

        # so, variable names are also called as TAGS, because we're tagging them to a value 
        # In otherwords 10 is a value and we're tagging variable names -> a,b to it (they are tagged to same Object int 10)
   
        # Thats the reason even if we change the value of the variable "a", the variable "b" will not be changed automatically 
        # because "b" is tagged to 10 and nothing to do with "a"

        #•Garbage collection
        # Now previously we said that a = 10 & a = b
        # lets say now a = 8 & b = 7. Now no variable is referring to 10
        # So, the 10 Object will still be there in the memory with no tags 
        # which will be removed during the Garbage collection (discussed later)
        # as long as the Object is referenced by something it'll  not Garbage collected 

        #•Constant Variables 
        # In programming we can make the value assigned to a variable Constant
        # In python we cannot do that
        
        #• knowing the datatype of a variable using type() function
        type() -> # it takes any kind of Object
        # we can create our own datatypes apart from inbuild datatypes like int float etc (check it)

    #VIDSUMMARY 
            # Every Object in python is assigned with a memory address, including variables 
            # we can know the memory address of an Object using the id() function, we can pass any kind of Object as an input to this function

            # The memory address of the value\Object stored inside the variable,will be assigned to the variable also 
                # for Eg if x = 10, the memory address of the value 10 will be assiged to the variable "x" also
                # for this reason python is memory efficient, because if x = 10 & x = y, both x & y variables will have same memory address, which is the memory address of 10

            # variable names are tags to the values stored inside those variables 
            # If a = 10 & a = b, a & b are tagged to 10, thats the reason even if we change the variable "a" value later -> variable "b" value will not be changed automatically 
            # if both variables "a & b" are changed to some other int, the value\Object 10 will still remain inside the memory, and will be garbage collected later as nothing is referencing it 
            # So, as long as the Object is referenced by something it'll  not be Garbage collected

            # In programming we can make a variable constant, but we cannot do that in python
            # TO know the "datatype of a variable" Or "to know which class the Object belongs to" we can use type() function, it accepts all kind of Objects 
    #!VIDSUMMARY 
#!VID 


    VID 10.DataTypes in python

        # Different Categories of datatypes in python are
            # None        → an empty variable in python contains None, in other programming languages its called as Null 
            # Numeric     → Int, Float, Complex, Bool are the major Numeric datatypes in python

                # Complex => a+bj » instead if "i" as the imaginary number, we'll have "j" in python, j = √-1
                #•Int() function => Using this function we can convert float datatype values/variables to int 
                    >a = 5.6
                    >b = int(a) => 5

                #•Float() function => we can convert int to float
                    >a = 5
                    >b = float(a) => 5.0

                #•Complex() function => using this function we can create complex numbers 
                    >complex(1) => 1+0j
                    >complex(1,2) => 1+2j

                # Bool Numeric datatype => True, False and 0,1 are bools in python. We can also convert True & false to ints as below 
                    int(True)  => 1
                    int(False) => 1
            
            # Below Datastructures belongs to “SEQUENCE”, Because we can generate a sequence of numbers using these datatypes
                # List   → [] => mutable   
                # Tuple  → () => imutable
                # Set    → {} => no duplicates
                
                # String → str() => we can use this function to convert int to String, reverse is not possible that is we cannot convert strings to ints 
                    # In other programming languages like Java,c++ we'll be having a "Char" datatype -> which is a  single character string => st = 'a'
                    # we dont have this datatype in python, the single character comes under string datatype in python
                
                # Range 
                    # Range datatype is only available in python 
                    # using Range() function we can generate a range Object => range(0,10)
                        >list(range(0,10)) => # we're convering the range Object to a list -> this will output a list from 0 - 9 (10-1) 
                    Syntax :- 
                    range(start,end,step) 
                        >list(range(0,11,2)) => # This will print even numbers » [0, 2, 4, 6, 8, 10]
                
                # Map or Dictionary 
                    # Each item of the list is tagged to a index 
                    # where as in a Dictionary, each value is tagged to a key and we'll not have any indexes in a Dictionary
                    # all the keys in a Dictionary should be unique 
                    Dictionary.keys()  # we can use keys() instance meathod to print all the keys inside a Dictionary
                    Dictionary.value() # we can use this instance meathod to print all the values of a Dictionary

    #VIDSUMMARY 
        # Different datatypes in python - along with their Categories
            # None - In other programming languages its called as null 
            # Numeric - int,float,complex,bool 
                Int() => # converts float to int 
                float() => # converts int to float
                complex() => a+bj
                    complex(1) => 1+0j
                    complex(1,2) => 1+2j
                Bool 
                    int(True)  => 1
                    int(False) => 1
                
            # SEQUENCE - list,tuple,set,string,range,dictionary 
                string - 
                    str() - # to convert int to string, viceversa is not possible 
                    char datatype - # is not available in python  as in java or c++, its a singe character 
                range - 
                    list(range(start,end,step)) - # we have to iterate over the rangeObj to convert it into ussable format 

                dictionary - 
                    # as each item in a list is tagged to index, each item in a dictionary is tagged to a key, hence there will be no numeric index concept in python
                        # hence we cannot access the items of the dictionary using an index
                    # Dictionary.keys() - to get all the keys 
                    # Dictionary.value() - to get all the values 
    #!VIDSUMMARY 
#!VID 


    #VID 11.Operators in Python

        #VIDSUMMARY 
            # Arithematic Operators
            # Assignment Operators  → x = 2 ; x+= 2 ; x*= 3 ; a,b,c = 1,2,3
            # Ralational Operators → < > >= <=  == !=
            # Logical Operators  → And  Or  Not  {x = True ; y = not x; "y" will be false } 
            # Unary Operators → (minus) "-"
                > N = 7
                > -N => -7
        #!VIDSUMMARY 
#!VID 


    VID 12.Number System Convertion in python

        # In programming we've below number systems 
            # Binary system (base 2)
            # Decimal system (base 10)
            # Octal system (base 8)
            # HexaDecimal system (base 16) -> Mac & Ipv6 address will be in this system

                # All the bases will be from 0 to n-1 => (0 - 1) (0 - 9) ETC
                # But for HexaDecimal system => 0 - 9 a - f  

        # Convertion from one system to another using python
        bin(25)  => # Using this function we can convert a number from -> Decimal to Binary
         '0b11001' → # "ob" are for representation that following number is in binary format
        
        0b11001 => # To convert a binary number to Decimal, we just have to put "ob" before the binary number
          25
        
        oct(25) => # From Decimal to Octal
          '0o31'   # 0o -> representation for octal 

        hex(21) => # From Decimal to HexaDecimal
          '0x15'   # 0x -> representation for HexaDecimal  
        
        # From any numbering system to Decimal
            # So to get to Decimal number from any numbering format, just type the respective numbering system code followed by the actual number in that format and hit enter 
            # for EG - 
                >0x25
                  37

        
        # Convertion from one system to another using math 
            # We can either use Factorial method or the Base numbering meathod

            # Lets say we want to convert 25 to Binary using Factorial
                2|25_
                2|12_ → 1
                2|6_ → 0
                2|3_ → 0 
                  1 → 1   # The Binary Convertion will be from here to top → 11001
            
            # In the similar way we've to divide the number with respective number system base to which we're converting 

            # Or we can use below base numbering meathod
                # converting 25 to binary 
                   16 8 4 2 1    →2^4 2^3 2^2 2^1 2^0
                   1  1 0 0 1 
                
                # convering 25 to Octal
                       16 8 1

        # So this topic is important for upcomming “ BitWise Operator ” topic 

    #VIDSUMMARY 
            # In programming we've below number systems 
            # Binary system (base 2) → bin function → 0b → 
            # Decimal system (base 10) 
            # Octal system (base 8) → Oct() → 0o
            # HexaDecimal system (base 16) -> Mac & Ipv6 address will be in this system → hex() → 0x
        
        # All the bases will be from 0 to n-1 => (0 - 1) (0 - 9) ETC
            # But for HexaDecimal system => 0 - 9 a - f  

        # To convert any number to Decimal format, we dont need any function
            # just type the respective numbering system code followed by the number and then hit enter, it'll return the value in decimal number
        
        # So this topic is important for upcomming “ BitWise Operator ” topic 
    #!VIDSUMMARY 
#!VID 


    VID 13.Swaping 2 variables
        # In different languages we've different way to solution 
        # •but using third variable is the common and basic meathod to solve this problem in most of the languages
    a = temp  # Note that LHS variable is taking the value & RHS variable is giving the value
    a = b
    b = temp 

        # •But how can be Swap the variables without using the 3rd variable
    a = a + b  # as we dont have to use extra variables, we're using existing variables (note that now variable a contains total sum)
    b = a - b  # total - b => a value » we store that in variable b (so now variable "b" contains variable a value)
    a = a - b  # total - ("a" value in variable b) => we'll be getting the variable "b" value and we store that in variable a 
        # Hence that values of variables are swapped 
    
        # !Using Xor Operator (^)
    a = a ^ b  # The advantage of using Xor is » it'll not waste any extra bits of information
    b = a ^ b  # as in the above example we're storing total value in variable a, which is more than the previous "a" value which is the extra information
    a = a ^ b
            # Xor -> 
                # returns  1 → if one of the bit is 1
                # returns  0 → If both bits are 0 or 1

                # remember in Raid 5 concept where we'll be using the Xor logic to generate a parity bit, which is used in data recovery 
                # That same concept will be used here 
                    a = a ^ b  # now a will have parity bit 
                    b = a ^ b  # parity xor B  => will return "a" value » stored in b  (think that a value is lost)
                    a = a ^ b  # parity Xor "a" value in b returns "b" value » will be stored in a  (think that b value is lost)

                # Xor or parity bit is generated using the A & B blocks of data
                # If any of the block data is lost, then using the parity bit and remaining block we can generate the lost blocks data
                # This is the Raid concept
    
        # !Using Tuple unpacking 
    tuple = 5,6  # we can skip the square brackets while defining a tuple  
    a,b  = 5,6   # this is tuple unpacking a technique => (5 → a) & (6 → b)

        # using the above 2 techniques we can swap the variables 
    a,b = b,a   
            # LHS contains the values & RHS contains the Assignments (python will always solve the RHS and assign the result to LHS)
            # So, LHS is a tuple (b,a) & RHS is the variables 
        
    a,b = (a,b) # in other words we're saying this, but we skipped the brackets on RHS 

    #DOUBTS     
        # According to Naveen reddy this is happening because of the below concept 
        Row_two()
        Swaps the two top - most stack items
            # he's saying that python is just rotating the values 
    #!DOUBTS


    #VIDSUMMARY 
        # We can swap the variables using third variable
        # If there is a restriction that - not to use third variable then we can either use 
            # addition or substraction calculations  Or we can use 
            # Xor Operator (^)

        # Finally in the python way - using tuple unpacking
    
    #!VIDSUMMARY 
#!VID 


    #VID 14.Python Bitwise Operator

    # This operator is very usefull when we're doing some scientific calculations 
    #•There are 6 types of bitwise operators 
        Complement ~
        And &
        Or  | 
        Xor ^
        Right Shift >>
        Left Shift  <<

    #T •Complement bitwise operator  → ~ 
        # Complement means a negation 
    > ~1  => 0  » # a Complement of one (on) bit gives us zero
    > ~0  => 1  » # Similarly a Complement of zero gives us one 

        # Bitwise complement operator(~) is a "8 Bit" "unary operator". It's also called as "Bitwise Not operator"
        # It'll convert the decimal to binary and then flip the bits which will be equal to the => -x -1
            # InOtherWords ~30 = -30 -1 => -31

        # Binary representation of negative numbers can be achieved by "2's complement"  (1's complement + 1)
            # First convert the given decimal number to its corresponding binary value
            # Then flip the bits, that is - all the One's in that binary code will be complemented to zero and vice versa (1st complement)
            # Then add one to the flipped bits, which will be the binary representation of the negative number (2's complement)
        
        # a quick glims of how we'll be calculating the binary of the negative number again
            # Conver the positive decimal to binary
            # Flip the bits
            # and then as per the 2's complement meathod, One is added to the fliped bits 
                # This addition is not AND operator
                # if we add 1+1 => result will be zero and one will be the carry for the next addition
 
    Eg :- 
    > ~ 12  # here we want Complement of a decimal number  12
        → 0000 1100  # Binary convertion of decimal 12
        → 1111 0011  # complementing to that binary (flipping the bits)  which gives us -13 ( this is also equal to 243 and also -13)
      

            # lets compare the above result with binary convert of -13
    >bin(13)
        0b1101  #Ob is code for binary in python
        1111 0010  # flipped all the bits and as complement bitwise is 8 bit we've also considered extra 4 bits on the left 
               +1  # adding one to calculate the 2's complement
        1111 00 11 # Finally this is the binary representation of -13


    # In a computer system, we dont store negative numbers, we always store positive numbers 
    # To store a negative decimal number, system will convert that to positive number using 2's complement, which will result in negation binary of that number as above
        # 2's complement = 1's complement(flipping of bits) + 1  

    # There is a simple formula to calculate the decimal output faster 
        ~x  =  -x - 1
        ~20 = -20 - 1 => -21  # here we want to calculte complement of decimal 20
    
    #!T 

    #T •Bitwise AND operator -> &
        # As we have "AND" operator in the logical operator, we also have this here, its similar to that 
    >12 & 13
        12
    
    >1100 & 1101  # one only if both the inputs are one 
        1100                          #!T 
    
    
    #T  •Bitwise Or operator → |
    >12 | 13     # if any input is one, then the output is one 
        13                             #!T 
    
    #T  •Bitwise Xor operator -> ^
                # if both the inputs are different then 1, if not 0 (its negation of Or operator)
    >12^13
        1                              #!T 

    #T •Left Shift  → <<
        # This bitwise operator will basically Shift the bits left 
        # In left shift we are gaining bits
        x << n  
            # X is the value on which we have to Shift the bits left 
            # n is the number of bits that we wnat to shift left 
    >20<<2
        80

    >10100.0000  
        1010000.00 => 50  # gained 2 bits

        # For both positive & negative numbers, we'll be adding zeros at the far right after the point as the +ve part gains bits     #!T 

     #T •Right Shift  → >>
        # This bitwise operator will basically Shift the bits Right 
        # In Right shift we are loosing bits
        x >> n
            X # actual number
            n # number of bits to shift Right, InOtherWords number of bit to loose
    
    >20>>2
        5  
    
    >10100.0000
        000101.0000 => 5  # on loosing 2 bits 

        # if we're dealing with positive value, we need to add zeros at the left, as we loose bits
        # if we're dealing with negative value, we need to add Ones at the left side after loosing bits       #!T 


    VIDSUMMARY 
        # Go through the summary first 
        # •Bitwise Operator is usfull during the scientific calculations
        # •There are 6 types of Bitwise Operators 
            Complement ~
            And &
            Or  | 
            Xor ^
            Right Shift >>
            Left Shift  <<

        # •Complement bitwise operator
            # Symbol - ~

            # 2's Complement meathod :-
                # First we need to understand how to convert negative numbers to binary
                # negative binary numbers are converted to binary using "2's Complement meathod" 
                # 2's Complement -> 1's Complement + 1 

                # Eg - lets convert -30 to binary
                    # Step1 -> convert 30 (+ve decimal) to binary => 00011110  » We've to consider 8 bits for this 
                    # Step2 -> 1's Complement => 11100001 » Flip all the bits 
                    # Step3 -> 2's Complement => 11100001 + 1 » 11100010 (this is binary representation of -30) ( 1 + 1 = 0 (carry will be 1))
                        # Off course its equal to 98
                        # But note that all the negative numbers are not stored as negatives in computer, they are stored as 2's Complement (like above -30 or 98)
            
            # Now lets get to the Complement bitwise operator - 
                # Complement means a negation and its a "8 Bit" "unary operator". It's also called as "Bitwise Not operator"
                # Complement bitwise formula => ~x = -x-1  (~20 = -20-1 => -21)
                # On applying the Complement bitwise operator on a decimal number, we'll be having a negative number
                    # we can check the result as below
                        # Convert decimal to binary and Flip the bits which will be the output of Complement bitwise operator
                        # we can compare the above result with the negative binary representation of that result (which can be achieved by 2's Complement)


        # •Bitwise AND operator  
            # Symbol &
            # This is similar to "AND" operator in logical Operators
            > 12 & 13

        # •Bitwise Or operator
            # Symbol | 
            # This is similar to "OR" operator in logical operators 
            >12 | 13
        
        # •Bitwise Xor operator
            # Symbol ^
            # If both the inputs are different then o/p - 1, else 0
            >12 ^ 13
        
        # •Left Shift  
            # Symbol <<
            # It'll Shift the bits left (before the decimal) in the binary (we'll be gaining bits)
            # Syntax - x << n   ("X" actual decimal number ; "n" no of bits to shift left)
            >20 << 2 
            10100.0000 => 1010000.0000
            # For both positive & negative numbers, we'll be adding zeros at the far right after the point as the +ve part gains bits

        # •Right Shift  
            # Symbol >>  
            # Will shift the bits right (we'll be loosing bits)
            > 20 >> 2 
            10100.0000 => 00101.0000

            # if we're dealing with positive value, we need to add zeros at the left, as we loose bits
            # if we're dealing with negative value, we need to add Ones at the left side after loosing bits 
    
    !VIDSUMMARY 
    !VID 


    VID 16.Math Module
        import math  

        sqrt()  #square root function
        floor() #previous int of the float (for 2.9 it'll be 2) remember that its not round off 
        ceil()  #after int of the float  (for 2.9 it'll be 3)  
        pow(3,2) # 3**2 (both these are same, later one is by using inbuild function) (3 to the power of 2)

        # Not only the mathematical functions, we also have constants in the math Module
        print(math.pi) => 3.141592653589793
        print(math.e)  => 2.718281828459045  # Epsilon constant value

        import math as m
        m.sqrt()    
        math.sqrt   # we can use both now 

        from math import sqrt,pow  # we've powerted 2 functions instead of whole math Module
        sqrt(4) # now we can run with the function name with out prefixing with Module name (math.sqrt())
    !VID 

    VID 17.User Input

        #T  Input() function :-
        # We can collect the input from the user using input function -> input()   ("read-host" cmd in powershell)
    
    x = input("enter the value:")
    y = input("enter the value:")
    z = x + y
        > 65  # here we got result of 65 instead of 6+5, because input() function will only return strings 
              # InOtherWords what ever the user has enterted it'll be converted to string and returned, thats what happened to 6 & 5 
              # Thats the reason there is a string concatination of 65, instead of adding 6+5
            
            #IMP input() function will always converts the inputs to string type  

            # Hence the corrected code will be below

    x = input("enter the value:")
    x = int(x)      # as input() function returns string, we're converting that back to int for addition
    y = input("enter the value:")
    y = int(y)
    z = x + y

    x = int(input("enter the value:"))  # some reduction in the above code 
    y = int(input("enter the value:"))
    z = x + y

        # What if we want to print only one character if the user inputs more than one character
        # we can use char format but its not available in python
    
    ch = input("enter a char") 
    print(ch)
        > prem  # if the user inputs a string, all the letters will be printed 

    ch = input("enter a char")  # User input is prem
    print(ch[0])   # even through the user inputs a string, only the first char which will be at index 0 will be printed 
        > p    

    ch = input("enter a char")[0]  # This is shortcut and modified code 
    print(ch)    
        > p                                                                                 #!T 


    #T eval() function
        #IMP This function evaluates the expressions 
     
    exp = eval(input("enter a exp"))  # user inputs expression -> 2+1-5
    print(exp)    
        > 2                                                                                 #!T 

    #T argv() function 
        #IMP This function is used to grab the inputs which are provided while running the python script
        # just like we give arguments to the parameters while running a  powershell command 
    > script.py  6  5   just like this 

        # we can do that using the argv() function
            # important things to remember while working with this function are  
                #IMP this function is from "sys" Module
                #IMP it'll grab the arguments provided while running the script and returns them in a string format, just like input() function
                    # Hence we have to convert the inputs to the required formats before execution  
                #IMP Note that argv() grabs the inputs based on position or index 
                # script.py  6  5  => index[0] → script.py,  index[1] → 6, index[2] → 5
                
                #IMP So, input() & argv() functions will converts the inputs to str() format

        
    import sys 
    x = int(sys.argv[1]) # because index 0 is the filename and we're converting it to int as argv() returns strings just like input
    y = int(sys.argv[2]) # here we're grabing index 2 and converting it to int() 
    z = x+y 
    print(z)

        > python script.py  6  5  # 6 goes to x & 5 goes to y
                                                                                             #!T 

    VIDSUMMARY 
        
        # Similar to "write-host" in powershell we can use below commands in python to collect the user input 
        # •Input() function 
                # It converts the user provided input to str() format 

            x = int(input("enter number:"))  # as the input() function returns string, we can convert it to required format in one line 
            x = input("enter char")[0]  # here even if the user inputs a string, we're only grabing the 1st character using the indexing meathod, in one line of code 

        # •eval() function
            exp = eval(input("enter an exp"))

                        # here the user will input a mathematical expression to the input() function
                        # but as the input function will convert that expression to a string format
                        # we're using eval() function to convert that back and execute the expression to get the output 

        # •argv() function
                # if you want to give arguments while running the python script itself, just like arguments to the parameters while running a powershell command, we've to use this function
                # InOtherWords "argv()" grabs the inputs based on position or index of the arguments that were provided to the script during execution 
                > python script.py 6 5    # script.py will be stored in index0 (argv[0]), in index 1 & 2 => 6 and 5 will be stored 
                # just like input() function, argv() also converts the input to string format
                # to use this function we need to import it from "sys" module 
            
            import sys
            x = int(sys.argv[1])
            y = int(sys.argv[2])
            z = x + y
            print(z)

            > script.py 6 5   # 6 = argv[1]  5 = argv[2]
    
    !VIDSUMMARY 
    !VID 

    VID 19.If: Elif: Else :

        # We all know that CPU has 3 parts 

            ├── CU  - Control unit
            ├── ALU - Arthematic & logical unit
            │     ├── Arthematic
            │     │         └── Math operators (% + -), Bitwise operator
            │     └── logical unit
            │               └── If condition, while for loop  ETC (decition making) 
            └── MU  - Memory unit
                  └── Variables, data containers etc

        #IMP Indentation in python can be of any spaces, but all the lines of a block should be in a same space Indentation, pep8 recomemds tab(4spaces)

        # If block
            # Only if the IF condition is True, then the block will be executed 
            # If IF condition results in false, it'll be skipped 
            #IMP we can use round brackets for if condition, its optional 
            if (x=y):
        
        # If you want to use multiple IF condition which belongs to same group
            # Then we can use "If Elif" statements 

            # if & elif conditions are checked one by One
                # if any one of it is true,that will be executed and remaining conditions will be igored 
                # if none of the "if elif" conditions are true, then atlast else block will be executed
                    # else will not have any condition, only condition for it is, it'll execute only if all the IF Elif conditions are false 

                #IMP If we use multiple IF conditions instead of if & elif, then every if condition is checked 
                    #IMP in If & elif, only if the first block is false then the next block is checked, and once any of the block is true, rest of them are ignored, if none of IF conditions are true, then Finally else block will be executed 
        if True:    
            pass
        elif True:
            pass
        else:
            pass

        # we can also have Nested If's 
    
    #!VID 


    #VID 20.While Loop

        # While (condition that tells till how many times this block has to be executed):

        i = 1   # i variable will be the counter
        while i<=5:  
            print('telsuko')
            i += 1   # it'll be incremented inside the loop each time, once the while code is executed 

            ___________________________________________________
            # Nested while loops 

        i = 1
        # j = 1 never initiate the counter variable of the inner loop outside the outer while loop
        while i<=5:  
            print('telsuko')
            j = 1       # we've to initiate it here at the top of inner while loop, 
            while j<=4: 
                print('rocks')
                j += 1
        i += 1 
         
            # because we need to reset "j" on every one execution of outer loop, other wise for the first execution of the outer loop, "j" will be incremented eventually to 5 and will not be resetted and 
            # hence inner while loop will not be executed from 2 executon of the outer while loop as the inner while condition will be satisfied => while j<=5:

            # for every execution of outer loop, inner loop will be executed 4 times, untill "j = 4"

            ________________________________________________________
            # To print telsuko and rocks on same line 

        print("prem","kumar")   # python will print prem kumar and goes to next line 
        print("prem", end = "") # python will print prem and stays on the same line, because we've used end parameter of the print statement
        print("kumar")   # This will print kumar beside the above prem
        print()     # this will make python to come to new line      
         
        i = 1
        while i<=5:  
            print('telsuko', end="")     # prints telsuko and stays on the same line 
            j = 1        
            while j<=4: 
                print('rocks', end="")   # prints rocks besides telsuko and stays on the same line
                j += 1
        i += 1 
        print()    # goes to the new line

        # hence this code will print telsuko rocks on same line 
        #IMP  for loop is more suitable when we know the range

        # IMP So in while loop we've to do 3 main steps 
            #IMP initializing counter variable → i = 0
            #IMP While condition → while i <= 0
            #IMP incremeting the counter variable in each iteration → i += 1

    #!VID 

    #VID 21.Range() function

        range(11,21,2)  → # generate a range Object with numbers from 11-20 with step 2
        range(20,10,-1) → # We can "step parameter" to -1, to print the numbers in reverse order, starts at 20 and prints till 11 (n+1)

            # In normal order prints till n-1
            # In reverse order prints till n+1

            # By default the "step parameter" is set to 1
    #!VID 

    
    #VID 22.Break,continue,Pass statement
        
        # Break & Pass & continue statements 

        #IMP  Break statement will break the loop (skip all the next iterations of the loop)
        #IMP  continue statement will skip all the next statements of that iteration(will skip that iteration from the continue statement) and will go to the next iteration of the loop
        #IMP  Pass statement means noting, pass on to next statement, it's mainly used to define empty blocks 
        #IMP Break,continue statements are used with loops and if blocks, where as pass statement is used with any block (function,class etc)

        #• Break - we can use this statement to Break the loop
            # Usually this statement is used with IF block inside a loop to break the loop based on the IF condition 

            # In the below example, 

    Available_Candies = 5
    x = input("No of candies")      # User will input how many candies he want

    i = 1
    while i<=x:                     # This while loop will print that many candies
        if i>Available_Candies:     # But during the execution of the loop, if number of candies the user requested is more than the stock(or we got out of stock)
            break                   # Then the loop will break 
        print('Candies',end= '')
        i +=1
    

        #• continue statement
                # Lets say you wnat to print 1 to 100 numbers and want to skip numbers which are divisible by 3 or 5 

    for x in range(1,101):      # range will print from 1-100 (n-1)
        if x%3 ==0 or x%5 ==0:  # if the remainders are zero when divided by 3 or 5
            continue            # skip the rest of the commands in the loop and go to next iteration   
        
        print (x)               # if not print the value of x
    print('bye')                


        #• Pass statement
                # If you have nothing to type inside a block, we can give pass 
                # It means that its an empty block 

    if x == 0:  # if this condition is satisfied
        pass    # then noting to do here, go to the next line
    else:
        print('x is not zero')

        #• IMP In nested loops 
            #IMP continue statement will only skip that particular iteration of the inner loop and continue the next interations of the inner loop and will not go to outer loop
            #IMP break statement will break the rest of interations of the inner loop and go to the outer loop
    
    #!VID 


    #VID 23.Printing patterns
            # # # #
            # # # #      #• Rows & columns are equal 
            # # # #
            # # # #

        for row in range(4)
            for column in range(4)
                print("#",end='')   # end='' will print # on same line
        print()                    # After inner loop completes to print 4 "#" on the same, inorder to go to the new line, we have this empty print statement here 

        
            #
            # #
            # # #       #• No.of columns = no.of rows 
            # # # #
        for row in range(4)    
            for column in range(row+1)  # Note that when its range(0), then the loop will be skipped, explained below, hence we've added row+1, so that when range(0) it'll be range(0)+1
                print("#",end='')
        print()

                        for i in range(0):
                            print('#')

                        >           # above code will print empty line


            # # # #
            # # #       #• No.of columns = no.of rows - 4
            # # 
            #
        for row in range(4):
            for column in range(4-row):     # when row = 0, column = 4 - 0 => 4 (prints 4 #), then 4 - 1 => 3 ETC
                print("#",end='')
        print()


    #!VID 


    #VID 24.For Else in python

            #IMP In other programming languages we usually use else with iF statements 
            #IMP But in python we can use else with FOR block 
                # Note that else comes under for loop, but they both have same Indentation just like IF & ELIF & ELSE statements
                # Else will be executed at the end of the for loop. but if there is a break statement in the for loop based on IF condition, else will not be executed if the loop is breaked in the middle 
                    #IMP InOtherWords Else will be executed after all iterations of for loop, if the for loop is breaked in the middle, then else will not be executed
            #IMP So important thing to note here in the "for else loop" is to have "Break statement" based on IF condition in the for loop, to grab the most of it 

        nums = [10,16,18,21,26]   # A list of ints,we want to print the first int that is divisible by 5, if noting found then we want to print 'nothing found'
        for num in nums:
            if num % 5 == 0:
                print(num)        # as soon as the first int that is divisible by 5 is found
                break             # Then break the loop, so else will not be executed
        else:
            print('noting found') # If the above for loop is not breaked (which means no int is found that is divisible by 5), then this else will be executed at the end of for loop

                    # If there is no break statement in the for loop in the above code 
                    # It'll print 10 and also 'nothing found', as else block will be executed at the end of the for loop
    
    #!VID 


    #VID 25.Finding Prime numbers logic 

        # Prime numbers - a number that is divisible only by itself and 1

            # If we divide  small number/Large number => Then we've to first add zero to the questient and then add zero to divident 
            # So in order to find the prime number 
            # check if the number is divisible by numbers from  '2' to 'that number-1'
                # as any number will be divisible by 1 and that number
                # numbers greater than that number will be never divisible (questient will always start with zero)

            num = 7
            
            for i in range(2,num):  # as range will take upto num-1
                if num%i == 0:      # as the num is 7, its checking the remainders when divisible by numbers from 2 to 6
                    print('prime')  # if zero, then the num is divisible, which means its not prime
                    break           # even if num is divisible by any one of the numbers in range(2,num), then its not prime number, hence we added break statement here to stop the loop
            else: 
                print('not prime')  # if above for loop is not breaked this else will be executed at the end of for loop


            # for FOR & ELSE block with break logic see above vid 

        #• But if the num is large number, then range() will generate more numbers
        #• hence below will be the better efficien logic

            • N= 239
            • Take its square root
                Sq root(239) will lie between 15 and 16. => 15.49  (take floor) (ceil will be 16)

            • all the prime numbers below 15 =>  2,3,7,11 and 13
            • Since 239 is not divisible by any of these.
            • Hence we can conclude that 239 is a prime number.

            # Using the above logic, we dont have to check the divisibility till 238 (239-1)

    #!VID 


    #VID 26.Arrays in python
         
         # Arrays Datastructure is not native to python, we've to import it from "Array" module
         # Arrays are similar to lists, but will only contain a values of single datatype 
            # a list can contain values of multiple datatypes 
        
        # Arrays in python will not have specific size, where as in other programming languages we need to predefine the size of the Array
            # which means that we can expand or shrink the size of the Array at any time 
        
        # Arrays will have similar meathods that we've seen in lists like 
            # append() - to add elements to the Array
            # index() - to find the index of an element
            # indexing also works with Arrays 
        
    from array import *   # from array module import every thing (just for practice, we just need to import array() function here)
    val = array('i',[1,2,3,4,5])   # so we can create arrays using the array() constructor meathod
 
        Syntax :- 
            array('Datatype',[list of elements])

                Datatype  - # For datatype we have to use the predefined "Type Codes", which can be found below 
                   
                    | Type code | C Type             | Python Type       | Minimum size in bytes |
                    |-----------|--------------------|-------------------|-----------------------|
                    | 'b'       | signed char        | int               | 1                     |
                    | 'B'       | unsigned char      | int               | 1                     |
                    | 'u'       | Py_UNICODE         | Unicode character | 2                     |
                    | 'h'       | signed short       | int               | 2                     |
                    | 'H'       | unsigned short     | int               | 2                     |
                    | 'i'       | signed int         | int               | 2                     |
                    | 'I'       | unsigned int       | int               | 2                     |
                    | 'l'       | signed long        | int               | 4                     |
                    | 'L'       | unsigned long      | int               | 4                     |
                    | 'q'       | signed long long   | int               | 8                     | 
                    | 'Q'       | unsigned long long | int               | 8                     |
                    | 'f'       | float              | float             | 4                     |
                    | 'd'       | double             | float             | 8                     |


                    # signed int takes less bytes than long int 
                    # Similarly float will take less memory than double

                    # signed int => goes from negaive to positive {-ve 0 +ve }
                    # unsigned int => will only have positive values, we can use this if we dont want to store -ve values  {0 +ve}

                [list of values] - # a list of values for that datatype which is the 1st parameter

        Meathods that are vailable with arrays :-
            array.buffer_info()  -> # Gives the size of the array 
                    # It'll output a tuple => ('MemAdd of array' , 'length of array[noof elements] ')

            array.typecode()  -> # Gives the datatype of the array

            array.append(), array.remove() -> # to add and remove the elements
            array.reverse()  -> # reverses the elements in the array  

            array[0] -> # We can access values using index 

        # Arrays are iterable

            for ele in array:       # when we use for loop, we can directly iterate over the iterable 
                print(ele)

            i = 0
            while i<= len(array):   # when we use while loop we've to use indexing to get the element
                print(array[i])
                i += 1
        
        # Creating a new array using the existing array

        array1 = array('i',[1,2,3,4,5])
        array2 = array(array1.typecode(),[a*a for a in array1])
                    # for parameter1 which is the datatype, we're getting the arguments from array1.typecode()
                    # for parameter2 which is list of elements, we're using list comprehention to iterate over the array1, get the values and do square of it 

        
    #VIDSUMMARY 
        
        # Array datastructure is not native to python, we've to import it from "Array" module 
        # A List can have elements of different datastructures
        # Where as an Array will only contain elements of same datastructure
        # The size of the Array in python is dynamic and we dont have to predefine the size of the Array while creating it 

        # Arrays are created in python using Array() constructor meathod 
        # Syntax :- 
            vals = array('datatype code',['list of elements'])

        # Arrays are iterable
        # Indexing works 
        # array.append(), array.remove() -> # to add and remove the elements
        # array.buffer_info()  -> # Gives the size of the array => # It'll output a tuple => ('MemAdd of array' , 'length of array[noof elements] ')
        # array.typecode()     -> # Gives the datatype of the array
        # array.reverse()      -> # reverses the elements in the array

        # Creating a new array using the existing array
        array1 = array('i',[1,2,3,4,5])
        array2 = array(array1.typecode(),[a*a for a in array1])

    #!VIDSUMMARY 
    #!VID 


    #VID 27.Array values from user 

        # Lets create an array where the user provides the elements for the array
            # For this we need to create a blank array
            # Then ask the user for the values 
            # at the end we'll ask the user to enter the element, to which we want to get the index number
                # we'll be achieving this in 2 ways 
                    # By manual meathod without using array Meathods → using conter variable => will be helpfull to get stronger in ALGORITHMS
                    # Next by using the array method → using array.index() meathod
        

    from array import array 

    arr = array('i',[])   # Creating an empty array
    length = int(input('enter the length of the array:'))  # As the input function outputs string, we're converting that back to int using the int() function

    for i in range(length):
        ele = int(input("enter the next element:"))
        arr.append(ele)
    
    print(ele)
     
    """ Manual way for getting the index of element
            Which is given by the user """
    
    ele = int(input("enter the element to find the index:"))
    x = 0                       # This is the iterator variable which resembles index value
    for e in arr:
        if e == ele:
            print('index',x)
            break               # if the if condition matches we want to break the loop
        x += 1                  # if not we want to increment the iterator variable

    """ Using the meathods of array to find 
            he index of the element """
    
    ele = int(input("enter the element to find the index:"))
    index = arr.index(ele)      # We're using the index meathod of the array to find the index of the element
    print('index',index)

    #!VID 


    #VID 28.NUMPY

        # We've different types of arrays 
            # Single dimentional array → Can be created using array() function => [1,2,3,4,5]  » we can also use numpy to create it 
            # Multi dimentional array → has to be created using numpy » mul rows & mul columns 
                 
                [1,2,3,4,5] -> # single dimentional array 
                [1,2,3,4,5 
                4,5,6,7,8] -> # 2 dimentional array, EG MATRIX
            
                CUBE       -> # multi dimentional array

        pip install numpy     # Installing 3rd party pakage numpy
        from numpy import *
        arr = array([1,2,3,4,5])      # we can create an array using an array() meathod from the numpy
        arr = array([1,2,3,4,5],int)  # We can specify the datatype of the array in the 2nd parameter 
                        
        from array import array
        arr = array('i',[1,2,3,4,5])  # as apposed to 1st parameter where we define typecode when we create array using the array() meathod from the array module

    #!VID 
    

    #VID 29.DIfferent Ways of Creating Arrays in Numpy
        
        #T Remember the difference between a list and array 
            # a list can contain elements of different datatypes 
            # an array will only contain elements of same datatype 
        !T
        
        #T There are 6 functions in numpy using which we can create arrays 
            array() 
            linespace()
            logspace()
            arrange()
            zeros()
            ones()
        !T 
        
        #T array() function :- 

            Syntax :- 
                array(['list of elements'], Datatype_optional) 

            # This array() function will implicitly guess the datatype of the elements that we enter 
                # thats the reason the 2nd parameter which is the datatype is optional

            array.dtype()  => # prints the datatype of the array

            # So, as the array function guess the datatype of the elements that we enter implicitly
                # so, even if we enter one flat while entering a list of ints, remaining all the int elements will be converted to float
                # because all the elements in the array should be of same datatype, so array() function will implicitly make this convertions 
            arr = array([1,2,3,4.5])
            arr.typecode  => float 
            print(arr) => [1. 2. 3. 4.5]  # we can see that all the ints are converted to floats implicitly to make all the elements in the array into a single datatype

                # If we dont want this implicit convertions, we can use the 2nd parameter (datatype) while defying the array
            
                # lets say we've entered all the ints as 1st parameter and entered float as the 2nd parameter
            arr = array([1,2,3,4], float)
            print(arr) => [1. 2. 3. 4.]  # then all the ints will be converted to float 

            TOPICSUMMARY 
                array(['list of elements'], Datatype_optional) 
                    # 2nd parameter 'datatype' is optional,because this function will automatically detect the datatype of of elements that we pass 
                    # if we enter all the int elements and one element as float, then all the ints will be converted to floats implicitly by the function, to make the array a single datatype 
                    # if we enter ints as 1st parameter and float datatype as the 2nd parameter, then all the ints will be converted to floats 
            !TOPICSUMMARY 
        !T 

        #T linespace() function :- 
            
            Syntax :-
                linespace(start,stop, step) 

                # This function takes 3 parameters
                    # in range() function, stop (2nd parameter) is excluded (prints upto stop-1)
                        # but in this function stop is included in the output 
                    # then the step parameter is not similar to the step parameter the we have in range() function 
                        # its the number of parts the range from start and stop has to be divided 
                        # Its optional parameter, if not specified by default it'll divide into 50 parts 
            Eg :-
            arr = linespace(0,3,4)  # range from 0 to 3 will be divided into 4 parts, (0 to 3 is 4 numbers hence we'll get equal parts)
            print(arr) => [0. 1. 2. 3.]

                # Note that we'll be always getting  an array of floats with the linespace function, because we're dividing range into parts which will most likely result into decimal numbers(floats) 
            
            arr = linespace(0,3,6) # now we're dividing the same range into 6 parts, which will result in decimals 
            
            arr = linespace(0,3)  # as the 3rd parameter step is not specified, it'll divide the range formed by start & stop into 50 parts

            TOPICSUMMARY 
                Syntax :- linespace(start,stop, step) 
                    # This function takes 3 parameters and some what similar to the range() function
                    # in range stop is not included (prints upto stop-1), in this function stop is included (prints upto stop)
                    # 3rd parameter step is not similar to the 3rd parameter step in the range() function
                        # its the number of parts the range from start and stop has to be divided 
                        # Its optional parameter, if not specified by default it'll divide into 50 parts 
                arr = linespace(0,3,6) => # divides range from 0 to 3 into 6 parts 
                arr = linespace(0,3) => # divides into 50 parts as 3rd parameter step is not specified
            !TOPICSUMMARY 
        !T 

        #T arrange() function :-
            
            # Its not a arrange function, its 'a'-'range' function 
                # which means it'll not arrange, it will create a range of elements in an array 
                #IMP This a-range function is similar to the range() function, unlike the above linespace function which has some differences with the range() function
            
            Syntax :-
                arrange(start,stop,step)  # all parameters are similar to the range() function parameters
            
            Eg :-
            arr = arrange(1,4,2) # will generate ints from 1 to 4  with step 2, similar to the output of "range(1,4,2)"
                [1,3]

        !T 

        #T logspace() function :-
            # logspace() & linespace() functions will break down the range into number of parts 
                # where as the a-range() function is similar to the range() function
            # But with the linespace() function, the gap or step between the start and stop is equal 
            # whereas with the logspace() function
                # if the step is 5 -> the parts between start & stop will be 5 
                # but the spacing between the start & stop will depend upon the log of it 
            #IMP It Returns numbers spaced evenly on a log scale
            
            Syntax :- 
                logspace(start,stop,step)

            Eg :-
                arr = logspace(1,40,5)
                    > [1.00000000e+01 5.62341325e+10 3.16227766e+20 1.77827941e+30  1.00000000e+40]
                    # This will create range from 10**1 to 10**40 (10 to the powerOfNumber = log of that number)
                    # Then this range will be divided into 5 parts 
                        # InOtherWords start & stop are differentiated using the log 

                print(arr[0]) => 10.0
                print(arr[0]) => 56234132519.034904
                print('%.2f'%arr[1]) => 56234132519.03  # '%.2f'% » is the regex to only grab 2 digits after the decimal with out 'e'

                >>> print(arr[4])
                    1e+40
                >>> print('%.2f'%arr[4])
                    10000000000000000303786028427003666890752.00
        !T 

        #T Zeros() & Ones() function :- 
            
            #IMP  These are helpfull to create an array of all zeros or ones respectively of any size 
            
            Syntax :- 
                zeros('size',datatype)   
                ones('size',datatype)    

                    #IMP  first parameter is size of the array in integer format 
                    #IMP  second parameter is datatype of the array, its optional
                        #IMP by default these function will output float values if this optional is not used 

            Eg :- 
                zeros(5) => array([0., 0., 0., 0., 0.])
                ones(5)  => array([1., 1., 1., 1., 1.])
            
            # We can see that we're getting float values on using these functions 
            
                ones(5,int)  => array([1, 1, 1, 1, 1])
                zeros(5,int) => array([0, 0, 0, 0, 0])
                    # as we've explicitly specified the datatype as int, we got integers instead of floats
 
        !T 
        #!VID 


    #VID 30.Different Operations on Numpy arrays 
    
        #TOPIC DIfferent Operations on Numpy arrays 

            #T Performing addition operation on each element of the array 
                    # We can do this manually using a loop 
                    # Or we can use the below simple operation 
                
                arr = array([1,2,3,4,5]) 
                IMP arr2 = arr + 5   
                print('arr2') => array([ 6,  7,  8,  9, 10])  # each element of arr is added to 5 

            #!T
            
            
            #T Adding two arrays 
                    #IMP each element of 2 arrays will be added with each other based on index position
                    #IMP we can do thatagain with "+" operator → arr3 = arr1 + arr2

                arr1 = array([1,2,3,4]) » [1 2 3 4]
                arr2 = arr1 + 2         » [3 4 5 6]   # defining 2nd array, which is "arr1 + 2"
                arr3 = arr1 + arr2      » [4 6 8 10]  # This will add each elements of 1st array with the respective 2nd array elements

            #!T 
        
        #DOUBTS Navin reddy missed Vectorized operations 
        #!DOUBTS 

        #TOPIC Other mathematical & trignometric Operations on Numpy arrays 
        
            #T Sin() of each element in the array 
                arr = array([1,2,3,4,5])
                #IMP arr2 = sin(arr)
                    > [ 0.84147098,  0.90929743,  0.14112001, -0.7568025 , -0.95892427]
            #!T 
            
            #T Cos() of each element in the array 
                #IMP arr2 = cos(arr)
                    > [ 0.54030231, -0.41614684, -0.9899925 , -0.65364362,  0.28366219]
            #!T 
            
            #T log() of each element in the array
                #IMP arr2 = log(arr)   
                    > [0.        , 0.69314718, 1.09861229, 1.38629436, 1.60943791] 
            #!T 
            
            #T sqrt() of each element in the array
                #IMP arr2 = sqrt(arr) 
                    > [1.        , 1.41421356, 1.73205081, 2.        , 2.23606798] 
            #!T
            
            #T SUM() if all elements in the array 
                #IMP arr2 = sum(arr)
                    > 15  # sum of all the elements in arr 
            #!T 
            
            #T Max() & Min() values in the array 
                #IMP arr2 = max(arr)
                #IMP arr2 = min(arr)
            #!T 
            
            #T unique() element in the array 
                #IMP arr2 = unique(arr)
            #!T 
            
            #T sort() the array 
            #IMP arr2 = sort(arr) 
            #!T
            
        #!TOPIC 
        

            #T Concatinating 2 arrays using concatinate() function
                #IMP arr3 = concatinate([arr1,arr2]) 
                    #IMP It'll combine the 2 arrays, it takes the arrays to be concatinated in a list  
        
        #!TOPIC 

        #TOPIC Copying arrays in numpy 
            # There are 3 types we can copy an array to another array in numpy 
                # nomral copying using the Assignment operator
                # Shallow copying
                # Deep copying 
            
            #T normal copying - Aliasing :- 
                #IMP arr2 = arr1  # here the arr1 array is copied to arr2 
                    
                    # we've seen this concept previously while discussing the memory address
                    # here in this case arr1 & arr2 will be pointing to same memory address, which means they both have same memory address
                        # InOtherWords arr1 & arr2 are the tags to the memory address of the data that is in the array 
                        # They both are pointing to the same array/memory address

                print(arr1)             
                print(arr2)      # Both these arrays will have same elements          
                print(id(arr1))  # also the memory address of these arrays will also be the same         
                print(id(arr1))         

                # This meathod of copying is called Aliasing
                    # because we're creating 2 difference Alias (arr1,arr2) for the same array or memory address

                # So now the import point here is :- 
                    # if we try to change any of the element in one of the array, then the other array will also be changed 
                        # this is not the case with variables, if both variables are pointing to same value, then that memory address of that value will be assigned to the tags or variable
                        # but if we change one of the variables value, then the other variable will not be affected, and this variable will be now pointing to another address or value 
                    
                #TOPICSUMMARY
                    # 1st type of copying is Aliasing
                    # arr1 = arr2
                    
                    # both these arrays are pointing to same data, they are the tags to that data
                    # so,the memory address of the data that is stored in these arrays will be assiged to them
                    # as we're creating a different Alias or tag to the existing array, this meathod is called Aliasing
                    # note that:- any changes applied to one array will implicitly also affect another array 
                        # InOtherWords both the arrays are still linked to each other 
                        # This is not the case with variables 
                        # if both the variables are pointing to same data, then that data's memory address will be assigned to both the variables, this condition is same for both variables and arrays
                        # but if we change one of the variables data, then the other variable data will not be change, and this variable will be not pointing to new value and will have different memory address
                #!TOPICSUMMARY
            #!T 

            #T Shallow Copying - .view() 
                #IMP Shallow copying is done using "array.view()" instance meathod
                #IMP In this type of copying the Original & copied arrays will have 
                    #IMP different memory address
                    #IMP but still they are linked to each other - if one array changes other also get effected

                # even through both the arrays will have different memory address, they are still linked to each other
                # thats the reason this type of copying is called Shallow copy 

                arr1 = array([1,2,3,4,5])
                arr2 = arr1.view()  

                    # So, view() is a function that will help us in creating new array at different locationb InOtherWords with new memory address
                    # So, both the arrays will have same values, but different memory address
                    # But arrays copied using view() function are still linked to each other 

                id(arr1) → 26813
                id(arr2) → 26813

                arr1[1] = 7  # any changes to one array, will still effect another array 

                #TOPICSUMMARY 
                    # Shallow Copy 
                        # done using "array.view()" instance meathod → arr2 = arr1.view()
                            # View() meathod will copy the arrays with different memory address, InOtherWords at different locations 
                            # But the arrays will be still linked to each other 
                                # any changes to one array, will still effect another array 
                #!TOPICSUMMARY 
            #!T 

            #T Deep Copying → .copy()
                #IMP Deep copying is done using "array.copy()" instance meathod
                #IMP  This copy function will create 2 different arrays 
                    #IMP which will have different memory address
                    #IMP and they are not linked to each other 

                IMP arr2 = arr1.copy() 

            #!T
        #!TOPIC 

            #VIDSUMMARY 
                
                arr2 = arr + 5   # performs addition operation on each element of the array 
                arr3 = arr1 + arr2 # each element of both the arrays are added with each other 
                arr3 = concatinate([arr1,arr2])  # concatinating 2 arrays
                "Vectorized operations"  # Navin reddy missed
                
                # Sin(),Cos(),log(),sqrt(),sum(),Max(),unique(),sort() of each element in the array 
                arr2 = sin(arr)  
                arr2 = cos(arr)  
                arr2 = log(arr)  
                arr2 = sqrt(arr)  
                arr2 = sum(arr)  
                arr2 = max(arr)  
                arr2 = min(arr)  
                arr2 = unique(arr)  
                arr2 = sort(arr)  
                
                # Different types of array copying 
                    # normal copying - Aliasing 
                    # Shallow Copying - .view()
                    # Deep Copying → .copy()

                    """
                        | Type of copying |        Code        | Memory address | linked  |
                        | :-------------: | :----------------: | :------------: | :------:|
                        |    Aliasing     |    arr2 = arr1     |      same      |  yes    |
                        |     shallow     | arr2 = arr1.view() |   different    |  yes    |
                        |      deep       | arr2 = arr1.copy() |   different    |  no     |    """

                    # Aliasing copying behaves differently from variable copying, see the topic-summary above 
            
            #!VIDSUMMARY 
    #!TOPIC 
    #!VID 

    #VID 31.Matrix in python
        #TOPIC multi dimentional arrays in numpy 

        #T Creation of multi dimentional arrays 
                # an array will multiple elements is a single dimentional array 
                # an array of arrays is a multidimentional array 

                # We've seen that arrays are created using array([]) function in numpy

            arr1 = array([ 1,2,3,4 ])     # single dimentional array 
            arr2 = array([ [1,2],[3,4] ]) # 2 dimentional array (Matrix), note that arrays inside the list are “comma seperated”
                > [[1 2]
                [3 4]]

        #!T 

        #T Meathods and attributes of numpy arrays 
                # Now lets see different operations that we can perform on numpy arrays 
                # attributes are also called as keywords
            
            # dtype attribute → contains the datatype of the array
            print(arr1.dtype) => int 

            # ndim attribute → contains the dimention of the array or Matrix which is also called as RANK
            print(arr1.ndim) => 2 » # its a 2 dimentional array ≈ Rank 

            # shape attribute → contains rows & columns of the Matrix or array
            print(arr1.shape) => (2,2) » # Gives us a tuple consisting of rows & columns 

            # size attribute → contains total elements of the Matrix or array
            print(arr1.size) => 4 » # 2 rows & 2 columns, total 4 elements 


            # flatten() instance meathod → converts multidimentional array into one dimentional
            # flatten() will flatten the array, converts multiple rows & columns into one row 
            arr2 = arr1.flatten()
            > [[1 2]    ≈  [1, 2, 3, 4]
               [3 4]]

            # reshape() instance meathod → to reshape arrays from one dimention to another dimention
            # we can see below that it takes 3 parameters 
                # first parameter is optional - by default it will take as 1 - 
                    # how many dimentions each inner array should contains 
                # second & third parameter is - if 1st parameter is one then it'll be --> no.of rows & cols of the outer array or whole array 
                    # if 1st parameter is other than one --> no.of rows & cols of each inner array  
 
            arr2 = arr1.reshape(no.of dimentional arrays to be created,rows,cols)
            
            arr1 = array([1,2,3,4,5,6,7,8])  # we've created a 1d array
            arr1.reshape(2,4)   # we want to reshape above 1d array into a 2d array
                        # 1st parameter is by default 1 => which means each inner arrays will be of 1d 
                        # 2nd & 3rd parameter => as 1st parameter is 1, then outer array will contain 2 rows & 4 cols 
                            # so, Finally it'll create an array of two 1d arrays, with 4 columns
            > [[1, 2, 3, 4],
               [5, 6, 7, 8]])

            arr1.reshape([2,2,2]) 
                        # 1st parameter -> each inner array will be a 2d array   
                        # as 1st parameter is not one, each inner 2d array will be of 2rows & 2 cols 
            > [ 
                [ [1 2]     #1st inner array
                 [3 4] ]

                [ [5 6]     #2nd inner array 
                  [7 8] ]  
                          ]

        #!T 

        #TOPICSUMMARY
            # multi dimentional arrays in numpy 
            # arrays are created using arrays() function in numpy 
                arr1 = array([ 1,2,3,4 ])     # single dimentional array 
                arr2 = array([ [1,2],[3,4] ]) # 2 dimentional array (Matrix), note that arrays inside the list are “comma seperated”
            
            # Meathods and attributes of numpy arrays
                # Attributes
                    print(arr1.dtype) => int   »  # datatype of the array
                    print(arr1.ndim)  => 2     »  # Rank ≈ its a 2 dimentional array   
                    print(arr1.shape) => (2,2) »  # Gives us a tuple consisting of rows & columns of the array 
                    print(arr1.size)  => 4     »  # 2 rows & 2 columns, total 4 elements (total elements of the Matrix or array)

                # Meathods
                    # flatten()
                    arr2 = arr1.flatten()     
                        # converts multidimentional array into one dimentional
                        # flatten() will flatten the array, converts multiple rows & columns into one row 

                    # reshape()
                        # to reshape arrays from one dimention to another dimention
                    arr2 = arr1.reshape(no.of dimentional arrays to be created,rows,cols)   #by default first parameter is 1
                    arr1.reshape(2,4)       # convert arr1 to an one dimentional array with 2 cols & 4 rows
                    arr1.reshape([2,2,2])   # convert arr2 to an array of 2 two dimentional arrays, each 2d array will have 2rows & 2 cols  
                        # please review the actual section for more clarity on this function
        #!TOPICSUMMARY
    #!TOPIC 

    #TOPIC Matrices 
            [1,2,3]  # row Matrix  => 1d array 
            [ 1,
              2,    # col Matrix  => 1d array
              3 ]
        
        #T converting arrays into Matrices using Matrix() function
            mat = matrix(arr1)  # it takes array as argument
                    # the output looks similar to the array, but it'll be converted from array to matrix, so that we can use matrix related attributes & meathods 

        #!T 

        #T creating Matrices using Matrix() function
            Matrix('1,2;3,4')  # this will create a 2d array with 2rows & 2cols
                # each row is sepeated by a semicoln 
                # entire argument is within quotes 
            >[ [1, 2],
               [3, 4] ]

            Matrix('1 2;3 4')  # instead of commas between the elements we can also give space 

        #!T 

        #T Meathods of Matrices
            # Diagonal() → returns the Diagonal elements of the matrix 
                arr = Matrix('1,2;3,4')  # a 2d matrix
                    [  [1, 2],
                    [3, 4] ]
                diagonal(arr) => [1, 4] 

            # min() & max() → returns the min & max elements from the matrix

            # "+" to add 2 Matrices
                arr1 = matrix('1,2;3,4')
                arr2 = matrix('5,6;7,8')

                arr3 = arr1 + arr2
                [[ 6,  8],
                [10, 12]]

            # "*" to multiply 2 Matrices
                arr3 = arr1 * arr2 
                ([[19, 22],
                  [43, 50]])
        #!T 

        #T How to do matrix multiplication 

            [19, 22 ]    [11, 12]
            [43, 50 ]    [43, 14]
              rank = 2x2        2x2 

            # 2 Matrices can be multiplied only when => no.of columns of first matrix == no.of columns of 2nd matrix
                # 2x(2) (2)x2

            # on multiplying 2 Matrices, the resultant matrix will be of rank => rows of 1st matrix x rows of 2nd matrix » (2)x2 (2)x2
            # each row of 1st matrix will be multiplied with each column of 2nd matrix (do google search)
            # write the program in python with out using any functions or meathods which will calculate multiplication of 2 matrics 
        #!T 

        #TOPICSUMMARY 
            # Matrices
            # we can create or convert arrays datatype into Matrices datatype using Matrix() function
                mat = matrix(arr1)  # arr1 array will be converted to matrix 
                Matrix('1,2;3,4')   # new matrix will be created, each row is sepeated by a semicoln and entire argument is within quotes
                Matrix('1 2;3 4')   # instead of commas between the elements we can also give space 

            # Meathods of Matrices
                diagonal(arr)       # returns the Diagonal elements of the matrix "arr"
                min(arr) & max(arr) # returns the min & max element from the matrix
                arr3 = arr1 + arr2  # Matrix addition
                arr3 = arr1 * arr2  # matrix multiplication
        #!TOPICSUMMARY 
    #!TOPIC 
#!VID 

    #VID 32.Functions
        # There are 2 types of functions
            # functions that returns values, these functions will contain "return" keyword
                # using this return keyword we can return as many values as we want 
            # functions that do specific task at the end - like print() statement at the end of the function
        
        # lets create a function that takes 2 inputs and returns 2 values 
        # list,tuple or variable unpacking will also work with functions which returns multiple values 
            # as usually no.of variables on RHS should be equal to the no.of values returned 

        def add_sub(x,y):
            add = x+y
            sub = x-y 
            return add,sub  # we're returning 2 values here
        
        var1,var2 = add_sub(3,2)   # function unpacking with function that returns multiple values 
    #!VID 

    #VID 33.Pass By Value\reference

        x = 10
        y = x  #RHS should have variable thats receiving value 

        # in the above case we discussed that 'x & y' will be having same memory address
        # we've also discussed that 
            # X&Y are just tags to value 10
            # the memory address of value 10, will be assiged to the tags also, in this case x&Y

        y = 9  # Here as the "y" value has changed, the memory address of value 9 will be assiged to "y"
            # and "x" will still have value 10 and its memory address 

        Pass By Reference & Pass By Value 
            # lets define a simple function here 

            def update(x):  # this function takes value from user and stores in "x"
                x = 8       # then it'll update the value of "x" to 8
                print(x)

            update(100)    # first x = 100, then will be updated to 8
            > 8            # hence we'll be getting 8 

            
            # now lets say we've a variable outside of the function
            a = 100        # lets say we've a variable "a" outside of the function
            update(a)      # we're passing that variable "a" as an input to update function => hence the value of "a" will be assiged to input variable of the function "x"
            > 8            # inside the function x = 8, hence we've 8

            print(a) => 100 # but the variable "a" value will be still the same off course


            # in other programming languages we'll be having a concept called → pass by Reference & pass by value 
            # call/pass by value means 
                # in the above function, we're passing variable a = 100 as an input to it 
                # in this case we're passing variable value 100 into the function
                # so pass by value => we're passing value and not the memory address

            # call/pass by Reference
                # but in pass by Reference we're passing the memory address itself 

            # so if its pass by value, what ever happens to the value that is passed to the function, variable "a" is not concered about it 
            # because as soon as value of "a" which is 100 is passed into the input variable "x" of the function, x will use different memory address though the value is same 
            # so even if we update "x" value it'll not effect "a" as the memory addresses are different

            # but in pass by Reference, we're passing the memory address of "a" to input variable of function "x"
            # which means both x & a are linked with each other, if one changes another also changes 

            # now which meathod python will follow 
            # in python we dont have any of the concepts 
            # in python, when we pass the "a" to the function, both input variable "x" & "a" refers to same memory address before the "x = 8" and onces the x becomes 8, it'll have different memory address
            # hence its not pass by value, but its also not pass by Reference, because here in this case "x" & "a" are not linked, they have to be linked if its pass by Reference
            # so in python its none of them 
            # we've discussed about the variable memory address in the previous vids  

            # take away point is 
                # python will neither have pass by value or pass by Reference
                # if a function is called by passing a value stored in a variable, both the input variable and the outside variable share the same memory address as the value is same 
                # but the moment the input variable value is changed the memory address will also be changed, which means input variable & outside variable are not linked to each other 

        reason why a variable memory address changes with value 

            # as integers and strings are immutable(cannot be changed) in python, as soon as the value of the variable is changed its memory address will also be changed (values memory address will be the variable/tags memory address)
            x = 100  # 100's memory address will be assiged to x 
            x = 8    # as ints 100 is immutable and cannot be changed to 8, each int will have its own memory address, hence in this case 8 memory address will be assiged to "x"

            # lets look at the behaviour of memory address for mutable objects like → lists 
            list1 = [10,20,30]
            id(list)  => 2811773112136

            list1[0] = 100  # we've changed one element of the list 
            id(list1) => 2811773112136  # the memory address remains same 

            # so in the below sinario, where we've created a list outside, and inside a function we've changed one element
            # will the outside list changes 
            # yes because, even if one element in the list changes the memory address will not be changed

            list1 = [10,20,30]
            def update_list(x):
                x[1] = 100
                print(x,id(x))
            
            update_list(list1) ==> [10, 100, 30] 2811773111496  # element at index1 is changed but memory address remains the same
            list1  ==>  [10, 100, 30]    # as the memory address remains the same, outside list also changes 
            id(list1) ==> 2811773111496  # also even though both inside and outside list has changed, but their memory address remains the same 

        #TOPICSUMMARY 
            # pass by reference & pass by value 
                # consider the below code 
                def fun(x):  # lets say we've this function, which takes x (input variable)
                    x = 8    # and then updates its value to 8
                    print(x)
                
                a = 100     # lets say this is the outside variable 
                fun(a)      # we're passing "a" to the function

                # now the question is weather the outside variable changes on updating its value inside 
                # in other programming languages, this depends upon pass by value\reference concept 
                # but python dosent have these things, so it depends on weather the values inside the variables are mutable or immutable 

                # first lets look at other programming languages - pass by value\reference
                # pass by value :- 
                    # only the value of variable "a"  is passed into the function
                    # outside variable and input variable of function will have different memory address 
                    # hence both these are not linked to each other, updating one variable will not effect another 

                # pass by reference
                    # in this case, the memory address of the outside variable is passed to the input parameter of the function
                    # hence the outside variable and input parameter variable of the function will have same memory address 
                    # hence both these are linked to each other, updating one variable will update another
                
                # now as python will not have neither of these concepts, it depends on wheather the value is mutable or immutable, note that x is the input variable of above function and x=8 is code line from the function
                    # if the variable contains immutable datatype values like - int,string => as these datatypes cannot be changed, every new value will have new memory address  and hence both the variables will not be linked as the memory address differ
                        a = 100   # a will have memory address of 100
                        x = a     # here both a & x will have same memory address, that is the address of 100 
                        x = 8     # here as the x value changed, now the x will have memory address of 8
                            # hence a & x are not linked to each other as their memory address is different
                    
                    # if the variables contains mutable datatype values like - lists => as these datatypes are editable or changable, a slight changes to the list will not get new memory address,hence both the variables are linked to each other as they share same memory address
                        # the reason is - as lists are mutable, even though one element of the list is changed, it'll not be assigned with new memory address, InotherWords its memory address will not be changed 
                        a = [10,20,30]  # outside variable "a" has a list 
                        x = a           # we've passed "a" as input parameter to the function "x" (x&a will have same memory address)
                        x[1] = 900      # inside the function, value of index1 in the list is changed (x&a will have same memory address)
                            # even though one element of the list is changed, it'll not be assigned with new memory address, InotherWords its memory address will not be changed 
                            # hence the inside and outside lists share the same memory address, they are linked to each other 
                            # changeds to inside list "x" will effect outside list "a"


                    # above sinarios for both mutable & immutable datatypes is same for function example as well as variable examples also 
        #!TOPICSUMMARY 


        #VIDSUMMARY 
            # pass by value --> pass only value and not the memory address, hence variables are not linked
            # pass by reference --> pass the memory address, hence variables are linked 

            # python will not have this pass by reference\value concept
            # it depends on weather the datatype of the variables is mutable or immutable
                # if immutable like strings,ints
                    # for different values in difference variables different memory address will be assigned to variables, hence not linked
                # if mutable like lists 
                    # for slight changes to a list in a variable, memory address will not be changed hence both the variables will have same memory address, hence linked 
            # if concept is same for both => "between 2 variables example" or "inside function & outside variable example"
        #!VIDSUMMARY 

    #!VID
    
    # VID 34.Types of arguments for functions
        #IMP parameters are also called as "formal arguments"
        #IMP Values given to them are called as "arguments or actual arguments" 
        #IMP parameters ≈ formal arguments ¦ arguments ≈ actual arguments 
        #IMP arguments can be passed in 4 different ways to the parameters of a function
            # positional arguments
            # keyword arguments
            # default arguments
            # Variable length arguments
        
        # consider the below function
            def add(a,b):
                print(a,b)    
        
        #T  positional arguments → same in powershell
            > add(5,6)          #!T

        #T keyword arguments → same in powershell
            > add(b=6,a=5)
            #IMP  parameter = argument
                                #!T  

        #T default arguments → same in powershell
            def add(a,b=6):
                print(a,b)    

            >add(a=5)  # "b" defaults to 6, we can override it by passing argument to "b"    #!T 

        #T Variable length arguments → [string[]]$string ← powershell equalent
            def add(a,*b):  # parameter "b" takes multiple arguments and store them as a tuple 
                print(a,b)

            >add(a=1,b=5,6,7)
                > a (5,6,7) # we can see that parameter "b" is a tuple
            
            #IMP variable length arguments => *param (one start param), stores as tuple 
                #IMP one star ≈ tuple ; two star ≈ dictionary   
                #IMP tupe (immutable), list can contains any thing, set(no duplicates),arrays-only single datatype elements
        
        #!T
    #!VID 
        

        #VID 35.keyword variable length arguments
            # In the previous vid we've discussed "variable length argument"
                # which is *parameter => which will be stored as tuple 
            # In case if we want to store the arguments to a parameter in a dictionary then we've to use double star 
                # **parameter => dictionary

            #IMP one star ≈ tuple(variable length argument) ; two star ≈ dictionary (keyword variable length argument) 

            #T example where we can use "keyword variable length arguments" - dictionary
                # lets define a function, that takes details from the user 
                # first we thought that name of the user is the mandatory detail and though of storing rest of the details in a tuple(variable length argument **param)
                    
                    def personal_details(name,*restOf_details):  # restOf_details will be a tuple 
                        print(name,restOf_details)

                    personal_details('prem',30,hyd,india) 
                        >prem (30,hyd,india)

                # Now in the above function, we dont know weather hyd is the working location or home town 
                # InotherWords parameter2 which is tupe details are not clear 
                # In that case we can use dictionary -> keyword variable length arguments 
                
                    def personal_details(name,**restOf_details):  # restOf_details will be a dictionary 
                        print(name,restOf_details)

                    personal_details('prem',age=30,work='hyd',native='india')    # we've to pass keyword and argument form 2nd parameter onwords
                        >prem {'age': 30, 'work': 'hyd', 'native': 'india'}  # all the keywords & arguments are stored as a dictionary in the 2nd parameter, and we can clearly know now hyd is his work location


                #IMP **param => dictionary ¦ function_Name('prem',age=30,work='hyd',native='india') → from keyword 'age' its dictionary(2nd param), prem goest to first param
                #IMP in the dictionay string keys dosent have quotes, but string values has to be in quotes => key='value' 
                    
                    dictionay = dict(age=30,work='hyd',native='india')      # creating the dictionay using dict() function
                    dictionay.items() => dict_items([('age', 30), ('work', 'hyd'), ('native', 'india')])  # items() instance meathod of the dictionay will return both keys and values
                    
                    for i,j in dictionay.items(): # using items() meathod we're doing dictionary unpacking here into variables "i & j"    
                        print(i,j) 

            #!T 
        #!VID 
        
    
    #VID 36.Globals keyword,globals() Function,Global Vs Local variable
        #T Scope
            #IMP variable inside the function is local to that function
            #IMP variable defined outside the function, on the code file is global variable
            #IMP If a variable or object is not found in the current Scope, then the intrepreter will look at the higher scope, vice versa is not possible 
            #IMP The preference is always given to the current scope object, if its dosent existing then it'll go to the higher scope
                # InOtherWords if an object is not found in the current scope, then the lower scope will not be cheked 
                # for Eg - if a variable is not found in the current scope, say inside the function (local scope), then intrepreter will look at higher global scope and get the value 
                # If its not found in the higher scope, then it'll result in an error 
                # If a variable on the file is not found(global scope), then intrepreter will not look into lower scopes like into the functions 
                    #IMP InOtherWords variables defined inside the function cannot be accessed outside the function
                    #IMP variables defined outside the function can be accessed inside the function, given - a variable with same name dosent exist inside the function or at current scope 
            
                a = 15      # This is global variable to the function

                def function(): 
                    a = 10  # This is local variable to the function
        #!T 
        
        #T Global Keyword → To import Global variable into a function, we can use "Global keyword" → global VarName

            a = 15  # global variable

            def function():
                global a    # we want to use global variable "a" inside this function, hence we've used global keyword
                a = 20 
         
            print(a) => 20 # Note that global variable value is changed to 20 inside the function using global keyword
                #! Note that we didnot define any local variables or local variable "a" inside the function
                #! IMP So, if you want to refer or import global variable inside a function we've to use keyword "Global" 

            --------------------   
            a = 15   
            def function():
                global a    
                a = 20 
                x = a   # x will be local variable here
            ----------------------

            #IMP When we say "Global a" inside the function, we've a global variable "a" inside the function, hence we are refering the global variable "a"
            #IMP Hence, we cannot have another local variable with same name that is "a" inside the function
            #IMP if we define it, the moment we define a = 9, it will treat "a" as global variable and its value will be changed 
            #IMP if you want to define a local variable "a" and also import the global variable "a" in same function, then we've to use Globals() function

        #!T 
        
        #T Globals() function → we can access the global variable address 
            
            #IMP globals() function will help us to change the global variable value from inside the function
            #IMP but we'll not import the global variable into the function, hence we can define a same name local variable inside the function
            #IMP where as with global keyword we'll import the global variable into the function, hence we cannot define another variable with same name inside the function
            #IMP if we define it, it'll again change the global variable value 
            
            #IMP globals() function will return all the global variables as a dictionary, hence we've to refer to one variable at a time using indexing → globals()['GlobalVarName'] 
            #IMP using this function, we can change the global variable value from inside the function, with out effecting another local variable value with same name which is also inside the function
            
            
            """ Global variables"""
            a = 15
            b = 6
            c = 10
            print(id(a))

            def function():
                
                globals()['a'] = 100 #! here we're changing the global variable "a"s value to 100, and we're not bringing the global variable "a" inside the function, as we did with global keyword above 
                a = 20               # This will be a local variable,hence we've used globals() function to change the global variable "a" value, with out effecting the local variable "a"

                x = globals()['a']   # as globals return all the global vars as dictionay, we're accessing particular global variable value using indexing
                print(id(x))         # as memory address of value inside the vars are assiged to vars itself, here 'x' & global var 'a' will have same value 100, hence will have same memory address, but x will be a local variable

                x = 6                # here the x value is changed, hence memory address of 6 will be assiged to x, and it will be a local variable here 

        #!T

        #VIDSUMMARY 
            # Objects defined inside a function is local to that function, and any Object on the script file will be global to the function
            # The preference is always given to the current scope object, if the object dosent exist in the current scope then intrepreter will go to the higher scope
                # InOtherWords → 
                    # variables defined inside the function are specific to that function and cannot be accessed outside the function, these variables are local to the function
                    # But variables defined on the script file which are global to the function, can be accessed inside the function by using either "global keyword" Or "globals() function"
            
            # global keyword => using this keyword we can import the global variable into the function » Syntax :- global VarName
                # as we'll be importing the global variable into the function, we cannot have another local variable with the same name inside the function
                # if we define a local variable with same name as the imported global variable, python will treat it as a global variable
                # inorder to have global & local variable with same name inside the function - we've to use globals() function

            # globals() function => using this globals() function we can grab the memory addressess of the global variables 
                # as we've learned that memory address of the values stored inside the variable will be assigned to the variable name\tag
                # we will be acessing the global variables values and tags using this globals() function  in a dictionary format 
                # and hence we can access the value of a particular  global variable using indexing meathod 
                # as we are just accessing the global variable using this function and we're not importing it, we can define another local variable with same name inside the function
            

            """Global variables"""
            a = 10
            b = 20

            def function():
                global a = 5         # we've imported the global variable "a" into the function and changed its value to 5
                a = 100              # here as we've imported global variable "a" above,  this "a" will be treated as global var and its value will be agian changed to 100

                x = globals()["b"]   # here we've used globals() function to access the global variable "b" value and its assigned to a local variable "x"
                globals()["b"] = 200 # here we're changing the global variable "b" value to 200
                b = 50               # as we've used globals() function to access the global variable "b" and as we didnot import it using the global keyword, we can define another local variable with same name, hence this "b" will be local
        #!VIDSUMMARY 
    #!VID 


    #VID 37.Passing List to a function
         # lets pass a list as an input to a function
            *param =>  #Tuple
            **param => #Dictionary

        # lets define a function that takes a list of numbers and return number of Odds & evens in that list 
            def even_odd(lis):         # We'll be passing a list to the input param "lis" of this function
                even = 01
                odd  = 0
                
                for ele in iist:
                    if 2 % ele == 0:
                        even += 1
                    else:
                        odd += 1
                
                return even,odd

            
            num = [1,2,3,4,6] 
            evenNum,OddNum = even_odd(num)  # as this function returns 2 values, we're unpacking them into 2 variables 

            print('even numbers: {} and Odd Numbers: {}'.format(evenNum,OddNum))
                #IMP format() is the instance meathod of the string object, its used to fill the place holders dynamically → 'prem {}'.format('kumar')
                # in the above print() function => "even numbers: {} and Odd Numbers: {}"" is the string and it has 2 place holders "{}"
                # we're using format() function to fill those place holders dynamically

        #VIDSUMMARY 
            # format() string instance meathod is important here 
            # also how to pass a list to the function is important
                *param =>  #Tuple
                **param => #Dictionary
                # to pass list its normal => def fun(var):
        #!VIDSUMMARY 
    #!VID 

    #VID 38.Fibonacci series in python
        # The Fibonacci Sequence is the series of numbers,
        # The next number is found by adding up the two numbers before it.
            # => 0, 1, 1, 2, 3, 5, 8, 13, 21, 34 
            #    0,1,0+1,1+1,2+3,5+4...
        
        # lets build a function to which the user can provide a limit, that says upto which we have to print the Fibonacci series
        # fib(5) => print first 5 Fibonacci series numbers 
        
        """ Naveen reddy's code """
        def feb(Input):

            Input = input('enter the number':)  # we're getting the input from the user and storing that in the input variable of the function
            Input = int(Input)  # as input() converts every thing to str format, we're again converting back to int
            a = 0
            b = 1

            if Input < 0:
                print('give +ve value')
            
            else:
                if Input == 1:  # if the users wants Fibonacci series only upto number 1
                    print(a)    # we'll just print "a"
                
                print(a)        # as the first 2 numbers of the Fibonacci series are => 0 & 1
                print(b)        # we'll be Printing them directly

                for i in range(2,input):  # range() function will only generates upto (input-1), so, we've to take either range(2,input) or range(3,input-1), we need to make sure that total numbers will be == input 
                    c = a + b
                    a = b       # second number will go to a
                    b = c       # sum of first 2 numbers will go to b
                    print(c)
        

        """ prems code """
        def fib(n):
            n = int(input("enter the number:"))

            if n < 0:
                print("U gave fcking -ve number")

            else:
                for i in range(0,n):
                    if i == 0:
                        a = i 
                    elif i == 1:
                        b = i   
                    
                    else:
                        c = a + b 
                        a = b
                        b = c
                        print(c)

        """ printing series till the number"""
        def fib2(n):
            n = int(input("enter the number:"))

            if n < 0:
                print("U gave fcking -ve number")

            else:
                c = 0
                for i in range(0,n):     # for loop inside a while loop will not work here,because we've break statements
                    while c <= n:
                        if i == 0:
                            a = i 
                            break        # this will break the while loop, continue statement here will go on running the while loop because c<n always because the code will never hit the outer for loop
                        elif i == 1:        # if we add break, the while will break and the code will go to for loop 
                            b = i           # inner loop will break and go to outer loop
                            break   
                        else:
                            c = a + b 
                            a = b
                            b = c
                            print(c) 

            --------------------------
            while c <= n:
                for i in range(0,n):    # for loop inside while will also work, only thing to notice here is, we've to use break instead of continue statements
                    break               #IMP continue statement will only skip that particular iteration of the inner loop and continue the next interations of the inner loop and will not go to outer loop
                                        #IMP break statement will break the rest of interations of the inner loop and go to the outer loop
#!VID 



#VID 39.Factorial of a number 
     # Below is how we can find Factorial of a given number
        5! = 5*4*3*2*1
        5! = 1*2*3*4*5
        # so we should start with one and end with the number, we can also do reverse 
    
    def Factorial(n):
        fact = 1
        for i in range(1,n+1): # we want numbers from 1 to n, and as 'range(1,n)' function will print only upto n-1, hence we've used n+1
            fact = fact * i
        return fact            # return keyword will not be the part of the loop, we just want to return the fact variable end the end of the loop, after calculating the Factorial of the given number 

    Factorial(8)

        # lets look at the range() function
        # range(5) => will generate rangeObj from  "0 <=> 4"
        # but above we want numbers from (1 => 5) » Hence we've used range(1,5+1)


    #! In the next vid we'll see how to calculate the Factorial using "recurssion concept"
#!VID 


#VID 40.RECURSION → function calling itself
    #IMP Calling a function from itself is called recurssion
    #IMP InOtherWords → Calling a function from the same function, which will result in an infinate loop 
    #IMP remember the recurssive option when we loop over the directories in powershell & bash

    # below function only prints hello, but lets say we want to print hello multiple times
    # we can go for a for loop(foreach in python) inside the function, or we can go for recurssion => which is noting but calling the same function from inside

    def greet():
        print('hello')   
        greet()         # we're calling the same function from the inside 

    greet() # this will execute the greet() function, the greet() inside the function, will go on execute when ever the function is called, hence it'll be an infinate loop

    #IMP Technically this recurssion should be continued infinate times
    #IMP but python has a limit for the recurssion, to prevent applications from crashing
        #IMP by default it'll be 1000 times but can be modified 

    #IMP we can see the default recurssion limit using the "getrecurssionlimit()" instanceMeathod of "sys" → sys.getrecursionlimit()
    import sys
    print(sys.getrecursionlimit()) |=> 1000  

    #IMP we can modify this recurssion limit using the  "setrecurssionlimit() instanceMeathod of sys"  → sys.setrecursionlimit(2000)
    import sys 
    sys.setrecursionlimit(2000)  # now the recurssion limit is set to 2000 


    # now as the recurssion limit is changed to 2000, lets count the recurssion and see if its modified
    i = 1
    def greet():
        print('hello',i)
        i += 1
    > UnboundLocalError: local variable 'i' referenced before assignment  # this will result in this error 
    # here "i" is the global variable, hence we have to either use global keyword or globals() to access or change the value of the global variable from inside the function 
        #IMP UnboundLocalError: local variable 'i' referenced before assignment → we'll get this error if we're using global variable inside the function without referencing it or importing it 

    i = 1
    def greet():
        global i    # we've imported the global variable "i" into the function (and we cannot define another local variable with same name "i" in this function)
        print('hello',i)
        i += 1
    > hello 1
        .
        .
      hello 1923

    # In the next vid we'll see the case example, where using a recurssion makes more sence that a for loop 
#!VID 


#VID 41.Factorial using recurssion
        # Factorial of a number => 5! = 5*4*3*2*1
        # it can also be calculated like => 5! = 5 * 4! ==> n * (n-1)!
    
    # so,lets see how we can find the Factorial of a number just using recurssion
    # recurssion is noting but → a function calling itself creating an infinate loop 

    # lets say we defined a fact() function which just does "n*(fact(n-1))"
        # we can see that we're calling the same function from itself => n * (fact() function will be called to findout fact(4))
        # in the 2nd recurssion to find the fact(4) => n * fact(4-1) » same function will be called to find fact(3)
        # in the third recurssion fact(3) => 3*fact(2)
        # in the forth recurssion fact(2) => 2*fact(1)
        # in the fifth recurssion fact(1) => as we know the Factorial of 1 is 1, so we'll put an IF condition to break the recurssion
    
    # so, Technically the code will go back to the initial point to find the Factorial of previous number and get returns back with Factorial of n 

    def fact(n):
        if n == 0:
            return 1    # the fact() function will return 1 when n == 0, and also if n == 0 fact() function is called again because in a function only one return statement will be executed, hence the recurssion ends here 
        return n * fact(n-1)  

    #IMP if a function has 2 returns on different lines, only the first return keyword will be executed and 2nd return will be skipped 
    def func():
        return 1
        return 2
    >>> 1  # only the first return keyword is executed 

    # This is what happened in the above fact() function,
        # if n ==0: only return 1 will be executed, last return will be skipped 

    # so we can do lot of thing with recurssion instead of using a for loop 

#VIDSUMMARY 
    # In the previous vid we've used a for loop and logic (5! = 5*4*3*2*1) to calculate the factorial 
    # In this vid we'll be using recussion instead of a for loop to calculate factorial and it usses the logic (5! = 5 * 4!)

    # •Things to know before proceeding :-
        # recurssion is noting but → a function calling itself creating an infinate loop 
        # if a function has 2 return statements on different lines, only the first return keyword will be executed and 2nd return will be skipped 
            def func():
                return 1
                return 2
            >>> 1  # only the first return keyword is executed 

    def fact(n):
        if n == 0:
            return 1     # the fact() function will return 1 when n == 0, and also if n == 0 fact() function is called again because in a function only one return statement will be executed, hence only this return will be executed and the recurssion ends here 
        return n * fact(n-1) # here we're calling the fact() itself to get the factorial of n-1 untill n == 0
#!VIDSUMMARY 
#!VID 


#VID 42.Lambda - Anonymous function
    # This Lambda functions or expressions concept is also discussed in MOSE series 
    # Main uses of Lambda functions :-
        #IMP as the way you pass values\Objects to the functions
        #IMP we can pass function to a function,as functions are also objects in python
        # say if the same situation arrived and IMP say the function to pass to another function is small, then instead of defining the function using def, we can use this one liner Lambda functions to define that function 
    
    # Syntax of Lambda functions :-
        IMP syntax → lambda parameter_list : Oneliner_expression  
            #IMP if we use (;) in the expression part of lambda, before (;) will be considered as lambda function, and after(;) will be considered as other code 

    # behaviour of Lambda functions :-
        #IMP a lambda function can contain N number of input parameters
        #IMP but the expression part of the Lambda function has to be a single expression on one line, semi colons(;) will not work 
        #IMP we can store the Lambda functions in a variable for later reference (because functions are also objects in python and objects can be stored in vars), otherwise we cannot reffer to this function later 
        len(lambda x,y : x+y)  # this lambda function takes x & y and adds them, and passes the expression result to the len() function
            # later we cannot reference this lambda function, because we didnot give any name to it 
        
        f = lambda x,y : x+y  # here we've stored the lambda function in a variable
        len(f(1,2))           # f(1,2) → we can reference the function using f() (that_variable())
#!VID 

#VID 43.Filter(),Map(),Reduce() fuctions 

        # remember Googles Map-Reduce concept in Hadoop 
            # we'll take chunk of data (big data)
            # we'll try to filter that data -> like filter() function here 
            # we'll then map it -> like map() function
            # and then we'll try to reduce it  -> like reduce() function

            # if you want to filter the iterable use -> filter()
            # if you want to perform certain operation on each element of the iterable use -> map()
            # if you want to get one summarized value out of iterable use -> reduce()

        filter(LamdaFun,iterable) |=>  # returns multiple elements which are of filterObj >-> Mainly used to operations that will filter the iterable » hence need to use "list(filter())"
        map(LamdaFun,iterable)    |=>  # returns multiple elements which are of mapObj >-> Mainly used to do operations on each element of the iterable » hence need to use "list(map())"

        from functools import reduce   # to use ‘reduce’ we need to import it from functools
        reduce(LamdaFun,iterable) |=>  # returns single element hence no need to pass it to list() >-> Mainly used to do operations on the iterable which returns a single value InOtherWords operations which will reduce the actual passed iterable  » like sum of the elements of the passed list 

        # The functions passed to filter() has to return True or false
        # For map() function, LamdaFun has to do operation on each element of the iterable
        # For reduce() function, the LamdaFun has to show how to do the operation on iterable

        # return,break,continue statements has to be used inside a function

        Eg :-
            nums = [1,12,13,55,66,98,77]  # lets say we've a list of values 

            Filter():- 
                # lets say we want to fetch all the even numbers from nums 
                    # as we are trying to filter the iterable we can go with Filter() function
                
                    def is_even(n):      # lets define a function which returns True when the element is even
                        return n%2 == 0  # this return statement will return true if n%2 == 0 

                    filter(is_even,nums) # now we'll pass the is_even() function & iterable to the filter function which will give filterObj which contains all the even numbers
                    list(filter(is_even,nums)) # to convert filterObj to list we're passing it to list() function

                        # Below is how filter() function executes 
                            # takes each element from iterable nums 
                            # pass it to the function, if its return true add it to output 
                            # else pass 

                    # now instead defyning the function externally we can use LamdaFun here
                    lam = lambda x: x % 2 ==0,nums
                    lam(2) >>>- True    # we can see that above LamdaFun also returns true & false
                    
                    list(filter(lambda x: x % 2 ==0,nums))

            map():-
                # lets say we want to double each element of the iterable
                # whenever you want to change every element of the iterable or map each element to another value - we can use map() 

                    list(map(lambda x: x*2,nums))

                        # This is how map() does it 
                            # each element of num is take into the input variable of the lambda function
                            # will execute the expression on that element 
                            # and store that in mapObj, which is later converted into list using list() function

            reduce():-
                # insted of returning multiple values, if you only want one value like sum of all elements we can use reduce() 
                # as reduce() is only used in sinarios when we get only one value, hence list() is not used
                    
                    from functools import reduce
                    reduce(lambda x,y: x+y,nums)    # LamdaFun of reduce() will always takes 2 values at a time

                    # This is how reduce does it 
                        # reduce() will take 2 values at time from iterable
                        # how it does sum depends on iternal code of reduce() 
                        # using the LamdaFun we are just saying that take 2 values from iterable each time and add them 
                            # and retrun a single aggrigate value

        #VIDSUMMARY 
            # Googles Map-Reduce concept in Hadoop is similar to Filter(),Map(),Reduce() fuctions 
                # we'll take chunk of data  → Iterables 
                # we'll try to filter that data -> like filter() function here 
                # we'll then map it -> like map() function
                # and then we'll try to reduce it  -> like reduce() function

                filter(LamdaFun,iterable) |=>  # returns multiple elements which are of filterObj >-> Mainly used to operations that will filter the iterable » hence need to use "list(filter())"
                map(LamdaFun,iterable)    |=>  # returns multiple elements which are of mapObj >-> Mainly used to do operations on each element of the iterable » hence need to use "list(map())"

                from functools import reduce   # to use ‘reduce’ we need to import it from functools
                reduce(LamdaFun,iterable) |=>  # returns single element hence no need to pass it to list() >-> Mainly used to do operations on the iterable which returns a single value InOtherWords operations which will reduce the actual passed iterable  » like sum of the elements of the passed list 

            filter():-
            list(filter(lambda x: x % 2 ==0,nums))
                # if you want to filter the iterable use -> filter()
                # The lambda functions passed to filter() has to return True or false
                    # Below is how filter() function executes 
                        # takes each element from iterable nums 
                        # pass it to the function, if its return true add it to output 
                        # else pass 

            map():-
            list(map(lambda x: x*2,nums))
                # if you want to perform certain operation on each element of the iterable use -> map()
                # so,whenever you want to change every element of the iterable or map each element to another value - we can use map()
                # For map() function, LamdaFun has to do operation on each element of the iterable
                    # This is how map() does it 
                        # each element of num is take into the input variable of the lambda function
                        # will execute the expression on that element 
                        # and store that in mapObj, which is later converted into list using list() function

            reduce():-
            from functools import reduce
            reduce(lambda x,y: x+y,nums)
                # to use ‘reduce’ we need to import it from functools
                # if you want to get one summarized value out of iterable use -> reduce()
                # For reduce() function, the LamdaFun has to show how to do the operation on iterable
                # insted of returning multiple values, if you only want one value like sum of all elements of the iterable, we can use reduce() 
                    # This is how reduce does it 
                        # reduce() will take 2 values at time from iterable
                        # how it does sum depends on iternal code of reduce() 
                        # using the LamdaFun we are just saying that take 2 values from iterable each time and add them 
                            # and retrun a single aggrigate value

            # return,break,continue statements has to be used inside a function
            def is_even(n):       
                return n%2 == 0     # this return statement will return true if n%2 == 0, hence can be used in filter()

            lam = lambda x: x % 2 ==0,nums
                lam(2) >>>- True    # we can also see that this LamdaFun also returns true & false, hence can be used in filter()

        #!VIDSUMMARY 
    #!VID 


#VID 44.Decorators 
    # Decorators feature is the only available in python
    #IMP Using Decorators we can extend the functionality of a function, without modifying the function itself

    # lets say we've a function that divides 2 numbers 
        def div(a,b):
            print(a/b)

        div(5,0)  # as we cannot divide by zero, this parameter set will result in an error 
    
    # one way to fix this is to add an IF condition to the actual function itself
    # Or we can use decorators 
    #IMP So,Using Decorators we can add extra features to the existing function, without modifying it

    #T creating decorator fuction
    # now lets see how we'll be creating a decorator to a function
    Eg1:-
        def check(func):      # lets define a func which takes another func as argument, so we'll pass our div func as argument later 
            def inside(a,b):  # In python we can create “nested functions”, this nested func will take 2 parameters which are those we'll be passing to our div() func
                if b == 0:    # this nested func will contain the logic
                    print('dividing by zero') # if we divide by zero, print this message
                    return    # and return out of the nested func
                func(a,b)     # else we'll execute the passed in func, with a&b parameters, hence this line will call whatever the func we passed as argument to the check() meathod 
            return inside     # !This line will execute the Inside() func, as the function has to be called after defyning otherwise it'll not executes, so this is where we are calling


        # so when we call check() func
            # it'll define the nested inside() func init, which will execute the func passed to the check() func based on the if condition
            # at the end after defyning the nested func, we'll call the nested func using the return statement

            # so, return inside => will execute the nested inside() function, which will inturn executes the func passed to check() based on condition

        #IMP So, read from back for better understanding
            #IMP actual func will be passed as input to decorator func
            #IMP decorator fuction will call inner func
            #IMP inner func will do the extra job or call the actual func with modified data 
    
    
    
    #!T 

    #T Executing actual function with decorator
        # now we've done with the defyning the decorator
        # now to add this extra functionality to div() function, we've 2 ways 
            # • T using variable
                div1 = check(div)   # we're passing the div as argument to the check() func and storing that in variable
                div1(1,0)           # here div1 is a code which contains check(div)
                >'dividing by zero' # hence this will print this as we are dividing by zero

                    IMP VarName = Decorator_fun(actial_fun) ¦ VarName(1,0) 
                    #IMP This is how it'll be executed 
                        #IMP div1(vairable) takes 1&0(parameters)
                        #IMP passes them to check()(decorator func)
                        #IMP check() will check the condition
                        #IMP and then passes them to div(actual_function) and executes div and returns div 
                #!T 

            # • T using decorator symbol '@'
            @check                  #IMP just before defining the function we just have to type -> @ NameOfDecoratorFun
            def div(a,b):           #IMP @decorator_fun means => decorator_fun(actial_fun) » we're passing div as argument to check() decorator function 
                print(a/b) 

            div1(1,0)               #IMP as we've decorator above the func while defyning, we can run the func as iz => div1(1,0)  
            >'dividing by zero'     # this will print this statement when divided by zero
                #!T 

    #!T 

        EG2:-
        # lets say we've a func that will divide 2 values and return the result
        # we wanted to swap the values passed to the func by using a decorator func and without modifying the original func

            def div(a,b):
                return a\b

            """ decorator function """
            def smart_div(func):       # decorator func takes actual func as input
                def inner(a,b):        # this nested func of decorator, will takes same inputs of actual func
                    a,b = b,a          # this will implement the logic with parameters of actual func  
                    return func(a,b)   # this will run the actual func with modified parameters
                return inner           # this will run the nested func
            
            """ executing meathod way1  - variable """
            div11 = smart_div(div)     
            div1(2,3)

            """ executing meathod way2  - using decorator """
            @smart_div                  # we've to use decorator above the func, which means below actual func is passed as input to decorator func for parameter logic validation and rerun 
            def div(a,b):
                return a\b
            
            div(1,2)

            # so we're creating a smart_div() function which will be the decorator for div() func
            # and this decorator func will have inner func which will be doing our job 

#VIDSUMMARY 
    # python supports nested functions 
    # Decorators feature is the only available in python
    # Using Decorators we can extend the functionality of a function, without modifying the function itself

    # •How to define a decorator function
        def funName(actual_function):  # * IMP decorator function takes the actual_function as input 
            def Nested_fun(a,b):      # * IMP this decorator function will have a nested loop, the parametes of the actual_function will be the input parametes of this nested function
                """
                    codition that will  #* IMP this nested func of the decorator func will execute the extra task
                    modify the 
                    actual_function function """
                
                return actual_function('with modified parametes')  #* IMP this return statement of nested loop will execute the actual_function with modified parameters 
                #Or simply return
            return Nested_fun         # * IMP this return statement of decorator function will execute the Nested function

        # So, read from back for better understanding
            # actual func will be passed as input to decorator func
            # decorator fuction will call inner func
            # inner func will do the extra job or call the actual func with modified data 

    # • IMP ways to execute functions with decorators 
        # · IMP way1 :- using variable 
            VarName = Decorator_fun(actual_function)
            VarName(1,0) 

                # This is how it'll be executed 
                    #div1 takes 1&0
                    #passes them to check()
                    #check() will check the condition
                    #and then passes them to div() and executes div and returns div 
        
        # · IMP way2 :- using decorators 

            @decorator_funName     # we'll give the decorator function name before defying the actual_function
            def funName(a,b):         # then will define the actual_function
                code 
            
            funName(a,b)           # while executing the function we'll execute it as it is 

                # !"@decorator_funName" before defying the function => we're passing the actual_function into the decorator_fun as an input 
#!VIDSUMMARY 
#!VID 


#VID 46.Special Variable __name__

    # What is __name__ variable
        # __name__ is the Special variable
        # it will store the value '__main__'
            # '__main__' is the “starting point of execution” → same with python,c,c++ & java 
        # the current file  __name__ variable  value will be always  '__main__'
            # if we print the __name__ variable value of other module or file in the current file, then __name__ variable value will be that modules name

        # on file1
            print(__name__)
        # on file2
            import file1
            print(_name__)
            >file1
            >__main__

            # on running the file2
                # we'll also run all the open statements of file1 as we're importing that file 
                # in the output we can see 2 things 
                file1 => # which is the __name__ variable value of file1 file 
                __main__ => # __name__ variable value of current file 

            # so, __name__ = __main__  in current file 
            # _name__ = moduleName if we print that module __name__ variable value in the current file
 
        # if the “starting point of execution” is the present module then '__main__' string will be stored in __name__ variable
            # We might have multiple modules in our project 
            # but there'll be one module that will be run first 
            # so, first module that runs will have __name__ = '__main__'
                # so this module will be the point of execution and this is where our code starts 
 
        # Lets look at the example :- 
            # lets say we've 2 modules → demo.py & calc.py 
            
            # in the demo.py module file, note that below print statements are open and they are not under any func
                print('hello')
                print('Welcome user')

            # in the calc.py file 
                import demo.py  # we're importing demo module
                print('its time to calculate')  # this is the print statement of current module
            
            # so the moment we run the cacl module
                # as we've imported demo module(which means we've executed the module once) in it and as there are open print statements in that module
            'hello'             # along with the print statement in calc module which we ran
            'Welcome user'      # we'll also get the open print statements from the imported module also 
            'its time to calculate'  


            # if you want to get rid of this behaviour
            # we should add an if condition in the demo module which we will import in another module
            # which says if __name__ == '__main__' then print these open print statements 

            # in demo file 
                if __name__ == '__main__':  # only if this module is the starting point of execution 
                    print('hello')          # only then execute these statements 
                    print('Welcome user')

            # which means when we import this module, __name__ will be the name of the module on execution file, hence these open print statements will not be printed 

    # VIDSUMMARY 
       # *in powershell, when we dottSource a module → that module will be executed once 
            # *which means all the functions in that module will be executed once (remember after defining a func we need to call it otherwise there will be no output, similarly on modules we define func, we'll not call them, hence no output on dottSourcing)
                # *which means these modules will be defined and loaded into the memory 
                # *if there are any open statements or function callings, these will be printed on the console when we dot source 
        
        # same in python, when we import a module, the module will be executed once 
            # hence all the functions in that module will be executed once which defines those func in the memory
            # if that module contains any open statements, those will be returned on importing that module
        
        # !so, point1 => on importing a module it'll be executed once 
        # !then, point2 => along with the module some the magic variables values like __name__ will also be modified

        # !the current file __name__ variable value will be always '__main__'
        # !on importing the same module, the module will be executed once and as the magic variables values will be changed,the __name__ variable value will also be changed to moduleName

        # we can chek that using below example 
            # file1 => contains open statement » print(__name__)
            # file 2 => 
                import file1
                print('this file __name',__name__ )
            
            # on execution of file2
                # as we're importing file1 
                    # it'll be executed once
                    # some the magic variables values of that module will be changed => __name__ value will be changed from '__main__' to file1(moduleName)
                    # all the open statement in the module will be printed while importing => print(__name__) this will be executed 
            
            # hence the output will be 
                file1 # print(__name__) output --> on executing import file1
                'this file __name' __main__   # print('this file __name',__name__ ) output, __name__ of current file will be always '__main__' (string)
            
 
        # •so if we have below code 
            If if __name__ == "__main__":
                print('this module')

            # on execution of current file =>  __name__ == "__main__", hence the IF condition will be True 
            # on importing the same module which has the current code => __name__ == "NameOfModule", hence the IF will be False, and the above code will not be executed
    
        # •so, below are the import points to remember
            #IMP __name__ magic variable value if we are on current file will be '__main__' string 
            #IMP on importing a module, below things happen 
                #IMP it'll be executed once, hence if any of the code that produces output is present in that module, we'll see that output
                    #IMP  InOtherWords all the open statements of that module will be executed once on importing that module
                #IMP some of the magic variables values of that module will be changed => __name__ value will be changed from '__main__' to moduleName

            #IMP VIDSUMMAR of this vid is important, go through it 
    #!VIDSUMMARY 
#!VID

#VID 47.__name__ variable part2 
    
    # Lets understand the __name__ variable again using another example
    # Lets say we've 2 python files → file1 & file2 (these files are modules)
        # below is the code on the file1 

            """ Files1 module has 2 functions """ 
            from file2 import add       # we're importing add function from file2 module
            
            def fun1():
                print("file1_function1")
            
            def fun2():
                print("file1_function2")

            def main():     # nomrally a module will not have any open statements, if we want to run certain tasks while user imports the module 
                fun1()      # then those tasks has to be under functions and all the functions that we want to call while importing has to be under another function
                fun2()      # like the main() function here, this is the standard programming procedure, main will be namming convention for these kind of functions, because 'main' is the starting point of execution 

            main()          # at the end we'll be calling main(), this function calling is the open statement and it'll run on importing this module, So using main() function we're calling all other functions


            """ Files2 module has 2 functions """
            def add():
                print(file2_add_fun)
            
            def sub():
                print(file2_sub_fun)

            def main():     # similar to above main() function, using main() function we're calling all other functions
                add()
                sub()

            main()          # this is the open statement and this main() function will be called on importing this module


            # Now lets say we want to import add() function from file2 to file1 
            # as we know that importing a module => running the whole code once 
                # which will execute open statements if any 
            # as we are calling main() at the end which is the open statement, and will be executed  
            # So, on importing module file2 into file will execute main() and main() will call all respective functions from file2 
            
            # inorder to overcome this situation, we just add a IFcondition to main 
            
            if __name__ == '__main__':
                main() 
            
            # as we discussed in the previous vid that on importing a module
                # all the module code will be executed once and loaded into memory
                    # In that process any open statements will be executed  
                # and also values of the magic variables will be changes 
                    # like __name__ variable value, which will be changed from '__main__' to module name if we're importing 

            # so if we run file2 module, then  => __name__ == '__main__', hence main() will be executed 
            # If we import the module, then => __name__ == 'file2', hence main() will not be executed, as IFcondition results in false
#!VID 

#VID 48.OOPS Introduction
    
    # In the above vids we've language fundementals of python
        # Variables
        # Functions
        # Modules 

    # Now lets move on to concepts of programming
    # The reason why python is so famous because
        #IMP Python supports all different programming paradymes   
            # It supports 
                #* Functional programming
                #* Object Oriented programming → OOPS
                #* Procedure Oriented programming 
        
            # Procedure Oriented programming :- 
                # project will be borken down into 
                    # breaking down project\software into modules & functions 
                    #Eg:- in the previous 2 vids while discussing __name__ variable, the code we've written comes under Functional programming 
                        # In that we've seen that every thing comes under functions & modules, we've also seen that even calling of other functions is also done using another function called main() 
            
            # Functional programming :- 
            # we will implement functions as mathematical functions where we'll not manipulate the data 
                # that is, without changing the data we'll still accomplish the task
                # One of the way is by passing function to a function as we've seen in with Lamda functions  
            
            # OOPS :- 
            # very famous in the industry
            # In this paradyme every thing is a object (lets take MAN as example)
                # Objects will have → Attributes & Meathods
                    # Attributes => its a data storage and it sotres properties of the object (height,colour,age,name) (we can use variables,and other datastructures like lists, arrays etc)
                    # Meathods  => functions in object Oriented programming are called meathods (these meathods define the behaviour of the object) (functionality of the object)
                
                # So, OOPS is all about breaking down a problem into objects & connecting them to solve the problem
            
            #! Below are the important concepts of object Oriented programming
                # Object → attributes & meathods
                # Class  → Blue print or design that contains how to define an object in this class, hence a class contains group of objects
                    # hence class => design, Blue print for objects
                    # Object => instance of that class 
                # Encapsulation
                # Abstraction
                # Polymorphism 

    #VIDSUMMARY 
        # Till now we've seen → Variables, functions & modules (proceedure oriented programming)
        # There are 3 programming paradymes (models)
            #* Functional programming
            #* Object Oriented programming → OOPS
            #* Procedure Oriented programming 
        # Python supports all of these 

        # Procedure Oriented programming :- (modules & functions)
            # breaking down project\software into modules & functions  (same like powershell)
        
        # Functional programming :- (prem didnot understand this)
            # we will implement functions as mathematical functions where we'll not manipulate the data 
                # that is, without changing the data we'll still accomplish the task
                # One of the way is by passing function to a function as we've seen in with Lamda functions  

        # OOPS :- classes & Objects
            # project\software is broken down into -> classes & Objects
            # everything is an Object 
            # we will have 
                # classes → blueprint\design for defying Objects under this class  
                    # Attributes → data storage (Variables) that store usefull information about the Object
                    # Meathods → functions in a class are called Meathods in OOPS, used to execute on Objects 
                #Object → an instance of that class 

            # Important concepts of OOPS :-
                # Class          => blueprint for objects
                    # Attributes => Variables
                    # Meathods   => functions under a class are called Meathods in OOPS
                # objects        => an instance of that class 
                # !Encapsulation => fill these
                # !Abstraction   => fill these
                # !Polymorphism  => fill the 
    #!VIDSUMMARY 
#!VID 

#VID 49.Class & Object 
    
    # In the last vid we've discussed about the theory part of OOPS, where we said 
        # Class => design\blueprint for creating objects in that class 
        # Object => actual instance 
    
    #• T How to Create Class & objects 
        # Lets say we want to define a computer class 
            # syntax for creating class => class ClassName(): --> instead of 'def', we'll use 'class' keyword to define a class
            # in the body section of the class we can have
                # Variables => Attributes
                # meathods  => behaviour or functionality
            
            class computer():
                def config(self):  #this is a meathod, note that it'll have a default input parameter "self", which we'll talk about later   
                    print('i5','1TB','16GB')  # So, defying a meathod is similar to function, but it'll have a default input parameter "self"

            # so now we've defined a class 'computer' & we've a meathod config() in that 
            # now lets see how to create objects of our computer class 
    
    #!T 
    
    #• T Creating Objects under a class 
        # every thing in python is an object
        # which also means that every thing will fall under a class
        
        # lets say we've defined a variable 'a', and in python as the datatype of the variables are intrepreted dynamically
            # we dont need to explicitly specify the datatype while defying the variables 
            a = 5 # hence the datatype of the below variable is intrepreted as int implicitly by python  
        
        # now as we said every in python is an object and belongs to a class, hence the variable 'a' will also be the object 
        # lets see to which class this variable a belongs to  
            type(a) --> <class 'int'> => # so this object 'a' belongs to class 'int' and the python intrepreted it dynamically as discussed above  

        # now lets see how to create an object under our class 'computer'
        # In Java & c# => we've a concept of constructor, which is used to create objects under that paraticular class 
        # In the same way we'll be using the constructor of our class → computer() to create an objects 
            com1 = computer()  # we've created an com1 object which falls under computer class as we've created the object using the constructor of that class  
        constructor => # just add brackets to the ClassName
            
            type(com1) 
            > <class '__main__.computer'>  # we can see that com1 object belongs to class computer()

            __main__.computer => # __main__ is from __name__ variable, as we're not importing this module, its still '__main__'
                # which also means that '__main__' is the moduleName so => moduleName.ClassName (__main__.computer)

            # for inbuild classes it'll be → <class 'int'>
            # for custum classes it'll be → <class '__main__.computer'>
    #!T 
    
    #T How to call\apply meathods of a class to an object
        # to call a meathod on an object we've 2 syntax :- 
            1.className.meathodName(object)
            2.object.meathodName() 
        
        1.className.meathodName(object) => 
            # if were calling a function, we've to go to the module path and then we can directly call the function with arguments 
            # now as the meathod config is under class computer(), so inorder to access that meathod
                # we've to mention → “className.meathodName”
                computer.config()
            
            # now as the config meathod has an default input parameter which is --> self 
            # we've to pass the object of that class as an argument  
                computer.config(com1) # we're passing the com1 object which we've created using the constructor above to this meathod
                >'i5','1TB','16GB'

            # we're saying that - human.walk() 
            # we've to also say to whom we're addressing - human.walk(mukesh)
            # human class, walk meathod, mukesh object

            # so the object we're passing into the meathod, will be loaded into the self input parameter of the meathod
            # there is an another syntax to call a method on a object 
            
        2.object.meathodName() => 
            com1.config()  
                # here as com1 is created using the constructor of computer class, python knows it and hence no need to specify it 
                # in this syntax, behind the scenes => #!object com1 will be passed as an argument to the config() meathod
                # this type of syntax is most preferred 
        
        # now hence we can do below 
            a = 5 # vairable 'a' object belongs to class int and hence we can all the meathods of int class on object 'a' using below 2 syntax
            a.bit_length()   
            int.bit_length(a)

            class int():
                def bit_length(self):
                    pass 

        # so this is how we create a class & object
    #!T 

    #VIDSUMMARY 
        #• Syntax for creating class :- 
            class className():
                """ In the body of the class
                    We define Attributes & Meathods """ 
                def meathodName(self):  # Meathods will have a default parameter - self 
                    pass                # Meathods will take objects as arguments to the self input parameter
            
            # so,instead of 'def', we'll use 'class' keyword to define a class
            # # So, defying a meathod is similar to function, but it'll have a default input parameter "self"

        #• Creating Objects for a class :-
            # as in java,c# we'll be creating objects using the constructor of the class 
                constructor => # just add brackets to the ClassName
                ObjName = className() 

            # on using type() function on an object --> it'll return the className the which the object belongs to 
            # for the objects belonging to inbuild classes, type() will return => <class 'inbuild className'>
            # if the object belongs to our custum class, type() will return => <class '__main__.className'>
                __main__.className => # __main__ is from __name__ variable, as we're not importing the module, its still '__main__'
                    # which also means that '__main__' is the moduleName so we can look at it as => moduleName.ClassName

            a = 5   # In python we dont have to define the datatype of the variable, based on the value, the datatype of the variable is automatically set  
            type(a) # as we said everything in python is an object and object comes under a class, so this variable 'a' will be also an object and it should belong to a class
            <class 'int'> # so this object 'a' belongs to int class  
            a.bit_length() # hence all the meathods\Attributes of int class can be applied on this object 'a'

        #• How to call\apply meathods of a class to an object
            # to call a meathod on an object we've 2 syntax :- 
                1.className.meathodName(object)
                2.object.meathodName() 

            1.className.meathodName(object) :- 
                # as the meathods will be under class, we need to give the FQDN of the meathod inoder to execute it => className.meathodName()
                # also as the meathods will have default input parameter 'self' which takes object of that class as an argument => className.meathodName(object)

            2.object.meathodName() :-
                # this syntax is frequently used 
                # in this syntax,behind the scenes object is passed as an argument to the meathod
                # as the object is created using the constructor of the class, hence python can understand to which class this object belogns to and there is no need to specify the className in this syntax

            a = 5 # vairable 'a' object belongs to class int and hence we can all the meathods of int class on object 'a' using below 2 syntax
            a.bit_length()     #syntax1
            int.bit_length(a)  #syntax2

            # this is how int() class and bit_length() meathod will be defined 
            class int():
                def bit_length(self):
                    pass 
    #!VIDSUMMARY 
#!VID 

#VID 50.__init__ special meathod
    
    # In the last section we've seen about → classes & objects, how to define then and also about → attributes & meathods 
        # so, attributes & meathods will be defined under a class which will be assigned\tagged to the object created under this class 
        # we've seen how to create meathods, and call them against the objects 
            className.meathodName(object) # we can call the meathod by using className (fqdn) and then passing the object itself to the meathod
            object.meathodName()   # Or we can call the meathod using the object itself
    
        # now lets see how to create attributes in a class which will be tagged to objects created under this class 
    
    #T creating attributes in a class 
        # we all know that attributes are variables
        # So, we'll be having 2 types
            # attributes values that are automatically assiged to the objects 
            # arguments to the attributes which are passed by us during the creation of the object are assiged to the object again 
        
        # in this vid we'll be seeing the 2nd type 
        # lets take the previous class computer for this example
            # every object in this class should have 2 attributes --> ram,cpu  
        
        #T __init__ special meathod
            # all the attributes for a class will be defined under a special meathod => __init__
                # __init__() meathod is used to initialize the variables 
                # in c,c++,Java this meathod is called constructor, we can also treat it as the same way in python
                # this __init__() meathod will be running automatically when we create an object using constructor, hence there is no need to call this meathod 
                
            # special variables & meathods will have underscores like __name__, just like system variables in powershell, hence these are predefined by python 
        #!T 
        
                # in the below class 
                    # to access the config() meathod, we should be calling that meathod() using either of the 2 syntaxes discussed above
                    # but the __init__() special meathod will be executed automatically, everytime we create objects using constructor 
                        com1 = computer() # the constructor will instantuate or call the __init__() which is constructor

                    # now we said that we'll be discussing the type2 attributes => Assigning arguments to the attributes while creating the objects using the constructor 
                        com1 = computer('16','i5')
                            # com1 will be passed to the self input parameter of the constructor (__init__() meathod) (this happens behind the scenes)
                            # '16' & i5' will be passed to ram & cpu parameter of the constructor
                        
                        computer.config(com1) 
                        com1.config()  # the way this com1 is passed as an argument to the config() meathod, in the similar way, com1 will also be passed to the self parameter of the constructor

                class computer():
                    def __init__(self,ram,cpu): # these 3 input parameters will be the input parameters of the constructor, because __init__() is the constructor => computer(self,ram,cpu)
                        self.ram = ram      # in the above statement we're collecting the arguments to the parameters, but here we're Assigning those values\arguments to the self(which is the object itself), we can assign it to the object attribute with same name or different (self.another = ram)
                        self.cpu = cpu      # so the constructor will instantuate objects and also create and assign values to the attributes of the object (constructor => computer() => __init__() meathod)
                    
                    def config(self):       # now the config meathod will take self(object) as argument, because in this meathod we want to access the cpu & ram attributes of the self(object)
                        print(self.cpu,self.ram) # we're printing the attributes of the object here. as ram & cpu are not local to this meathod, and they belongs to self object, we need to access them using the dot notation, otherwise it'll result in error 
                    

                # So we can see that -> meathods & attributes(data) of an object are working together 
                    # we've a name for this concept, which we'll discuss later  

                # now lets create objects and run config() meathod against them and see the results 
                    com1 = computer('16','i5')  # here computer() == __init__() => constructor. it takes self(com1),ram,cpu as arguments 
                    com2 = computer('8','i3')   

                            # here we're calling the config() meathods on the objects, hence config() is an 'instanceMeathod' and can be execute using below 2 syntax
                    com1.config()  => '16','i5'        # config() takes self(object - com1) and prints attributes of the object (self.ram, self.cpu) 
                    computer.config(com2) => '8','i3'

                # so remember
                    # __init__() meathod is the constructor
                    # it runs automatically when we instantuate using constructor
                    # all the attributes to the object will be defined under this constructor or __init__() meathod 
    #!T 

    #T No need to define __init__() meathod to use the constructor of the class :-
        # Lets say we dont have any attributes in a class, then we can skip defyning the constructor (__init__() meathod) in the class
        # even though the __init__() meathod is not defined we can create the objects using the constructor
            class temp():
                pass 

            tempObj = temp() # eventhough there is nothing under the class (no __init__() meathod), we can use the constructor to create the object
    #!T 

    #VIDSUMMARY 
        # we'll be having 2 types of attributes that we can define under constructor 
            # attributes values that are automatically assiged to the objects  → hence there will be no input parameters in the constructor or __init__() meathod 
            # arguments to the attributes are passed by us during the creation of the object are assiged to the object again → hence there will be input parameters in the constructor
        # in this vid we'll be seeing the 2nd type 

        # to define attributes in a class, we've to know about __init__() meathod
            # __init__() meathod is the constructor, same in c,c++,Java
            # __init__() meathod is special function as special variable __name__, all the special variables/functions will have uderscores, like system variable in powershell
            #__init__() meathod is used to initialize the variables in a class
            # all the attributes to the object will be defined under this constructor or __init__() meathod 
            # it runs automatically when we instantuate using constructor => com1 = computer()  (here computer() ==> __init__() » constructors)
                # and hence it'll assig the attributes values to the objects automatically

        
            class computer():
                def __init__(self,ram,cpu): # these 3 input parameters will be the input parameters of the constructor, because __init__() is the constructor => computer(self,ram,cpu)
                    self.ram = ram      # in the above statement we're collecting the arguments to the parameters, but here we're Assigning those values\arguments to the self(which is the object itself), we can assign it to the object attribute with same name or different (self.another = ram)
                    self.cpu = cpu      # !so the constructor will instantuate objects and also create and assign values to the attributes of the object (constructor => computer() => __init__() meathod)
                
                def config(self):       # now the config meathod will take self(object) as argument (hence its an instanceMeathod), because in this meathod we want to access the cpu & ram attributes of the self(object)
                    print(self.cpu,self.ram) # we're printing the attributes of the object here. as ram & cpu are not local to this meathod, and they belongs to self object, we need to access them using the dot notation, otherwise it'll result in error 
                
            # below we're creating object under computer class using constructor
            com1 = computer('16','i5')
                # computer() is the constructor
                # its same as __init__() meathod
                # it takes 3 parameters --> self,ram,cpu
                    # self = com1 object itself, it'll be passed to the constructor behind the scenes 
                    # 16 & i5 goes to ram & cpu positionally 
                    
                # as the __init__() meathod will  automatically runs on running the constructor
                    # which will create attributes cpu & ram and assign values to the attributes that we've passed (to the constructor) 

            com1.config() => '16','i5'
            computer.config(com1) => '16','i5'
                # as config is not __init__() meathod, which will executes automatically, we need to call this meathod using either of the above 2 ways  
                # as config(self) meathod  has self parameter, and it takes object as argument to this parameters, hence its an instanceMeathod
                # so config() takes self(object - com1) and prints attributes of the object (self.ram, self.cpu)  => '16','i5'

            # So we can see that -> meathods & attributes(data) of an object are working together 
                # we've a name for this concept, which we'll discuss later 

        #!eventhough '__init__()' meathod or constructor is not defined in a class, still we can use the constructor to create objects 
    
    #!VIDSUMMARY 
#!VID 

#VID 51.constructor,self,comparing objects special meathod

    # in the vid we'll talk about "constructor & self" 
        # We know that __init__() is called as constructor, we'll see why its called as constructor here 
    
    #T constructor
        # lets say we've a class computer → design
        # in that class we've created a com1 object

            class computer():
                pass 
                
            com1 = computer() 
                # here we can either say 
                    # com1 is an object Or 
                    # com1 is referring to an object under computer class  
            
        #T Heap Memory :- 
            # Heap Memory is the special memory inside our system
            # this memory will store all the objects that we'll be creating 
                # InotherWords a memory address\space from the this Heap memory will be assigned to the objects that we create 
                # So the objects that we create will take some space in the Heap memory and every memory space will have an address(memory address)
                # remember that everything in python is an object and will be assigned with a memory address
        #!T 

        # now lets create 2 objects under the computer class and check if they got same or different memory address\memory space from the Heap memory
            com1 = computer()
            com2 = computer()

            id(com1) |=> 15505552
            id(com2) |=> 3120752
                # we can see that different memory address or memory spaces are assigned to each object
                # so, every time we create an object under a class, it'll take new memory space or memory address

            # the size of the object depends upon its attributes (no.of variables it has)
            # but a constructor is responsible for 
                # calculating the total memory of the object 
               # and assigning memory space or memory address to that object

               computer() # is the constructor => whenever we run this it'll call the --> __init__() meathod
                    # hence we dont need to call the __init__() meathod explicitly
            
            # we've already discussed about this __init__() constructor in previous vids  
                # that its called implicitly
                # all the attributes for the objects under the class will be define under this __init__() meathod 
        #!T 

        #T How to change the value of an object's attribute
            # there are 2 ways 
                # we can define a special meathod that updates the attribute using dotnotation Or
                # we can change it by using the dotnotation on the console 
            
                class computer():
                    def __init__(self):       # as all the attributes will be defined under this __init__() constructor meathod, we can see below that we've defined 2 attributes 
                        self.Name = 'Naveen'  # Note that for all the objects under this class will have these attributes, as we didnot differentiate them    
                        self.age  = 28

                    def update(self):         # this is 1st meathod to change an attribute using a meathod
                        self.age = 30         # so, on calling this meathod against the object, the age attribute of that object will be updated to 30
                
                
                com1 = computer() 
                com2 = computer() 

                com2.Name = 'Reddy'           # here we've changed both the attributes of com2 object using dotnotation, 2nd meathod
                com2.age  = 30
        #!T 

        #T Use of self input parameter :- 
            # Now lets see why to we need this “self input parameter for every meathod under a class” 
            # lets say we've created 100 objects for a class
            # the self input parameter , will act as a pointer to the target object, on which update function should execute, based on which object we're calling 
                # InotherWords, we've seen 2 ways of executing a meathod on an object
                    # in both the meathods below com1 will be passed as an argument to the self input parameter of the update() meathod
                com1.update()   # notice that com1 will be passed to update() behind the scenes
                computer.update(com1)
        #!T 

        #T 'compare' meathod to compare 2 objects in a class 
            # lets say we want to be able to compare 2 objects in our class  
                # we'll be taking the same computer class & com1,com2 objects as above 
            # lets also say that both the objects have same values for the name & age attributes 
            # now lets say we want to compare the age attribute of both the objects 

                if com1 == com2:            # if we write it like this it dosent work because
                    print('they are same')  # !python dosent know how to compare 2 objects by default

            # so, to compare 2 objects in a class, we've to define a sperate meathod in the class as below 
                
                class computer():
                    def __init__():
                        pass
                
                    def compare(self,other):
                        if self.age == other.age:
                            return True 
                        else:
                            return false 

                # as every meathod we can call this compare() meathod also using 2 ways 
                com1.compare(com2)    # com1 will be passed to self input parameter of compare() meathod behind the scenes
                computer.compare(com1,com2)  # this is more clear way 

                # so to compare 2 objects in a class we've to define compare() meathod
                # compare() takes 2 parameters --> who is calling, whom to compare


                # as compare() function returns boolean values we can use it in IF condition
                    if com2.compare(com1):      # self = com2 & other = com1 (in the compare() meathod)
                        print('age is same')    
                    else:
                        print('age is diff')
            #!T 

 
        #VIDSUMMARY 
            #* greens are further short summary lines 
            
            com1 = computer()  # we can either say --> com1 is an object Or com1 is referring to an object under computer class

            #•Heap Memory :- 
                # Its a special Memory inside our system, which stores all the objects that we create 
                # every Memory space that an object occupies will have a Memory address, so that system can refer it back again 
                # hence to all the objects that we create will get Memory address or Memory space from this Heap Memory
                # also note that each object will take a different memory space or memory address from Heap memory
                    # remember that everything in python is an object and will be assigned with a memory address

                        #* special  memory which stores all the objects
                        #* memory space or memory address will be allocated to objects by the constructor() from this memory

            #•responsibilities of a constructor :- 
                # calculating the total memory of the object 
                # and assigning memory space or memory address to that object from Heap memory
            # the size of the object depends upon the no.of attributes it has 

            __init() meathod :- The constructor
                # className() will call the __init() meathod which is the constructor
                    # hence we dont need to call the __init__() meathod explicitly 
                # all the common attributes of the objects will be defined under this constructor meathod

            #•2 ways for changing attribute value of an object :-  # both meathods uses dotnotation to access the attributes value
                # •by defyning special meathod in the class 
                    class computer():
                        def __init__(self):
                            self.age = 20    # all the objects under this class have this age attribute
                        
                        def Att_update(self):
                            self.age = 30       
                            print('age attribute has changed')

                # •accessing the attribute of the object using dotnotation directly 
                    com1 = computer() 
                    com1.age = 30

            #•use of self input parameter :-
                # we should add self input parameter to every meathod in the class by default 
                # self input parameter will act as a pointer to the target object on which the meathod has to execute on 
                # InotherWords the object will be passed as an argument to the self input parameter of the meathod()
                # If we defined 100 objects in a class, this self will tell the meathod on which object it has to execute on 

                    # *object will be passed to self, hence it'll act as pointer to the object

                # bellow are the 2 ways for running meathods on an object
                com1.Att_update()   # com1 will be pass to the meathod behind the scenes 
                computer.Att_update(com1)
            
            #•'compare' meathod to compare 2 objects in a class :-
                # python dosent know how to compare 2 objects in a class by default
                # we've to define a sperate meathod in the class,to compare 2 objects in a class
                    class computer():
                        def __init__():
                            pass
                    
                        def compare(self,other):        #!note that compare() takes 2 parameters --> who is calling, whom to compare
                            if self.age == other.age:   #!this equalent operator logic is important 
                                return True 
                            else:
                                return false 

                # as every meathod we can call this compare() meathod also using 2 ways 
                    com1.compare(com2)    # com1 will be passed to self input parameter of compare() meathod behind the scenes, com2 will be passed to 'other' input parameter
                    computer.compare(com1,com2)  # this is more clear way 


                        # *python dosent know how to compare 2 objects in a class by default, we've to do that by creating a meathod with bellow logic 
                        def compare(self,other):        # *note that compare() takes 2 parameters --> who is calling, whom to compare
                            if self.age == other.age:   # *this equalent operator logic is important 

                        com1.compare(com2)  

        #!VIDSUMMARY 
    #!VID 


#VID  Types of variables\attributes 

    # In OOPS we've 2 different types of attributes 
        # Instance attribute\variable 
            # these are defined inside the constructor () __init__() meathod)
        # Class attribute\variable (static variable)
            # these are defined on the top of constructor
    
    #T Instance attributes :-
    #Eg :- 
        class car:                  # lets say we've a car class 
            def __init__(self):
                self.mileage = 5    # these 2 are called instance variables  
                self.company = 'Bentely'

            # these attributes are called as instance attributes because
                # even though all the objects in this class have these 2 attributes and their values as common  
                # but the memory address of these attributes is different for difference objects 
                # which means that changing the attributes of one object will not effect the other objects attribute 
            
        minicooper = car() 
        bmwi5  = car() 

        minicooper.mileage = 3  # on changing this bmwi5.mileage will be still 5 
    #!T 

    #T static\class attributes :- 
        # if we want to have same attribute for all the objects with same memory address\space --> then we've to go with these type 
        # Note that this attribute belogns to class and the object inherits from it 
            # hence we can access this attribute using either by class or object but 
            # to change its value, we only have to use class => className.classAttribute 
                # if we try to change this attribute value using object, then a new memory space\address will be assiged to this attribute for that object and the code will mess (explained in doubts section)

            class car:

                """ Variables defined inside __init__() => 
                        instance attributes (diff memory address)
                    Variables defined outside __init__() => 
                        class\static attributes (same memory address)  """
                
                wheels  = 4  # this will be the static\class attribute
                
                def __init__(self):
                    self.mileage = 5    # these 2 are called instance variables  
                    self.company = 'Bentely'


                minicooper = car()
                bmwi5  = car()
                            
                            #! Note that we can access this class\static attribute using either by object or class
                            # because this class\static attributes are same to all the objects in the class (same memory space\address) and thats is not the case with instance attributes  
                minicooper.wheels => 4 
                car.wheels => 4     

        #T NameSpace :- 
            # the place\area where attributes\objects are stored is called NameSpace
            # its of 2 types 
                # class NameSpace → all the class attributes are stored here 
                # Object\Instance NameSpace → all the instance attributes are stored 

            # so hence to modify an class\static attribute we've to use className
        #!T 
            
                car.wheels = 100  # this will change the wheels attribute of all the objects in this car class to 100
    #!T 

        #DOUBTS 
        # this is what prem found out 
            # usually its suggested to change the class\static attributes using className
            # if we try to change it using objectName then the class attribute of only that object is changed, and rest of the objects class attribute will remain the same  
                c1.wheels = 500 
                print(c1.wheels) |=> 500
                print(c2.wheels) |=> 100  # remains the same 

                print(id(c1.wheels)) |=> 324684132168   # we can see that the static attribute memory address for all the objects is same 
                print(id(c2.wheels)) |=> 324684132168

                car.wheels = 1000          # if we do that, then wheels attribute of c1 will have different memory address and will not be changed even though we change the wheels attribute using the car class, because memory address will be different
                print(c1.wheels) |=> 500   # wheels attribute of c1 remains as previous value  
                print(c2.wheels) |=> 1000  # it only effects other objects  

                print(id(c1.wheels)) |=> 4549684654968 # thats because the memory address of wheels attribute of c1 object will be changed, hence it'll not respond to static attribute changes which are made using className
                print(id(c2.wheels)) |=> 324684132168  # as this c2 objects static attribute memory address remains the same, hence it'll respond to the static attribute changes which are made using className

        #!DOUBTS 

    #VIDSUMMARY 
        # In OOPS we've 2 different types of attributes 
        # Instance attribute\variable 
            # these are defined inside the constructor () __init__() meathod)
            # each object Instance attribute will have their own memory address
                # InotherWords each objects Instance attribute will point to different memory address
            # hence if we change one objects Instance attribute, it'll not effect the other object Instance attribute
        
        # Class attribute\variable (static variable)
            # these are defined on the top of constructor
            # all the objects static attribute points to same memory address
            # we can access this static variables either by using objects or class  --> className\ObjName.staticAttName
            # but to change this static attribute, we've to only use class and on changing this attribute all the objects same static attribute will be changed as they point to same memory address  → className.staticAttName
            # if we change it using the object (ObjName.staticAttName),then this static attribute for that object points to different memory address
                # and hence the memory address of that static attribute for this object is different from all other objects static attribute,and hence any changes made to this static attribute using the className, will not effect this objects static attribute
            # see the doubts section 
        
        # Namespace :- 
            # the place\area where attributes\objects are stored is called NameSpace
            # its of 2 types 
                # class NameSpace → all the class attributes are stored here 
                # Object\Instance NameSpace → all the instance attributes are stored 

            # so hence to modify an class\static attribute we've to use className
    #!VIDSUMMARY 
#!VID 


#VID 53.Types of meathods 

    #• T Types of meathods → 3 types
        # In attributes we've 2 types 
            # Instance attributes       --> defined inside the constructor
            # Class\static attributes   --> defined outside the constructor
                # here note that :- class & static attributes are two different type of attributes
                # but there will be no difference between them when it comes to attributes.
                # and thats the reason we've combined both the static & class attributes and made the total type of attributes as 2
                # but this is not the case with meathods, in meathods they are different, and thats the reason we've 3 types of meathods
            
        # below are the 3 types of meathods 
            # Instance meathods 
            # class meathods 
            # static meathods 

    #• T Getters & setters 
        # but again, each meathod type can be broadly classified into 2 types 
            # Getters\Accessors => these meathods will 'get' the values of the attributes 
            # Setters\Mutators  => these meathods will 'change\set' the values of the attributes 
    #!T 
    #!T 

    #• T instanceMeathods :- 
    #EG :- 

        class student():            # lets create a student class 
            school = 'telsuko'      # this will be the class\static attribute, as its above the constructor
            
            def __init__(self,m1,m2,m3):  # this is the constructor, and here the agruments to m1,m2,m3 are passed during objects creation using the constructor
                self.m1 = m1        # and these are the instanceMeathods as these are defined below the constructor
                self.m2 = m2
                self.m3 = m3
            
            def avg(self):          # this is an instanceMeathod because we've 'self' input parameter Or this meathod takes object as input
                return (self.m1 + self.m2 + self.m3 / 3)    # this instanceMeathod calculates the average of marks 

            """ avg() is an instanceMeathod because 
                    It takes self as input parameter Or
                    It takes in Object as input
                    InotherWords we can also call this meathod using the object and not by class 
                        That is => object1.avg(), and not using class student.avg() """ 

        s1 = student(34,96,72)
        s2 = student(40,50,60)

        print(s1.avg())
            > 68.51646516
        print(s1.avg())
            > 56.35468465

        # Now we know that avg() meathod is the instanceMeathod because it works on the object
        # as said earlier, all the meathods can be broadly classified into 2 types → Getters\Accessors & Setters\Mutators
            
            # below is the Getters\Accessors meathod example :- These will get the values of an attribute
                # inorder to fetch the value of an attribute, we can directly access it using the dotnotation as below 
                    print(s1.m1) |=> 34
                # Or instead of using above dotnotation, we can use meathods 
                    class student():
                        def __init__(self):
                            pass 
                        def get_m1(self):   # so this meathod will be the Getters\Accessors meathod type
                            return self.m1  # because this meathod will get the value of the attribute

                        """ Its a convention to use 
                            'get' keyword for the Getter meathods """

            # Below is the Setters\Mutators meathod example :- These will set the values for an attribute
                # we can directly set the value to an attribute of an object using the dotnotation as below 
                    s1.m1 = 100
                # Or instead we can define a getter meathod for this 
                    class student():
                            def __init__(self):
                            pass 
                        def set_m1(self,New_m1):    # this is an Setters meathod, it takes object and New_m1 value as input parameters
                            return self.m1 = New_m1 # and then it'll set the New_m1 value to the m1 attribute of the object passed 

                        """ Its a convention to use 
                            'get' keyword for the Setters meathods """

            # SO,
                # Getters get the value
                    # and will not change the value hence they are called Accessors
                # Setters set the value
                    # and will change the value hence they are called Mutators
            
            # Note that 
                # instanceMeathods are used to set,get the values of instance attributes (defined in the constructor)
                # Inoder to work with class attributes (defined above the constructor), we need to use ClassMeathods
    #!T 

    #• T ClassMeathods :- 
        # so ClassMeathods works with class attributes & instance meathods work with instance attributes 
        # as the ClassMeathods works with class attributes 
            # it'll not take the object as input (as with instanceMeathods which will have 'self' as default input parameter)
            # !but it'll take class as input, and thats the reason we use “cls” default input parameter while defying the ClassMeathods
        # also note that 
            # !ClassMeathods will have “@ClassMeathod” decorators above 

        class student():

            class = 'Telsuko'   # this is class attribute

            def __init__(self,m1,m2,m3):    # instanceMeathod will have 'self' input parameter
                self.m1 = m1
                self.m2 = m2    # instance attributes 
                self.m3 = m3

            @classmeathod   
            def get_className(cls):         # ClassMeathods will have 'cls' input parameter
                return cls.class # this will return the value of class attribute 'class'

            """ We've learned about decorators previously --> vid 44
                @classmeathod is a function that takes below get_className classmeathod as input 
                InotherWords we can think of above code as ==> 
                    var = classmeathod(get_className)  --> so this variable represents this function combination
                    var(cls)    # this cls input will be passed to get_className classmeathod, and the result of that will be passed to decorator meathod """
            
        # so we know that we can run the instanceMeathods using 2 ways a below
            s1.avg()
            student.avg(s1)

        # but to run the classmeathod, we only have one way, that is by using className
            student.get_className()
                > 'telsuko'  # and this will print the class attribute value 
    #!T 

    #• T StaticMeathods :- 
        # If we want to define a meathod
            # that has noting to do with instance attributes & class attributes 
        # in that case we'll go with static meathods 
        # ! thats the reason these StaticMeathods will not take any input parameters (no 'self', no 'cls')
        # ! aso note that --> static meathods will have '@StaticMeathod' decorator at the top 

        # it'll be usefull in situations like 
            # if we perform operation, that has something to do with other class objects --> we can use StaticMeathods
        # or you want to find the factorial of a number in the middle of the class 
            # because these sinarios has noting to do with the class & instance attributes 

            class student():
                def __init__(self):
                    pass

                @StaticMeathod
                def info():
                    print('this is StaticMeathod')

            student.info()  
                # to run the StaticMeathods we've to use className
                # we dont have to pass anything --> neighter  'cls' or 'self(object)'

        # so, if you want to perform some extra operation on the class that has nothing to do with instance & class attributes of the class then go with StaticMeathod
    #!T

    #VIDSUMMARY 
        # •Basically we've 3 types of attributes & meathods for a class 
            # Instance 
            # Class 
            # static 
        # •when it comes to attributes :- 
            # class & static are same, hence we only have 2 types of attributes => Instance attributes & class\static attributes
        # •when it comes to meathods :- 
            # class & static are different, hence we've 3 types of meathods for a class 
                # InstanceMeathods
                # ClassMeathods
                # StaticMeathods 
        
        # •Note that each type of meathod can be again broadly classified into 2 types :- 
            # Getters\Accessors meathods => these will “get” the value of an attribute for an object in the class => convention is to have 'get'  keyword in the meathodName
            # Setters\Mutators meathods => these will “set” the value for an attribute of an object in a class  => convention is to have 'set'  keyword in the meathodName

        # •InstanceMeathods deal with Instance attributes (either setting Or getting)
        # ClassMeathods deal with class attributes (either setting Or getting)
        # StaticMeathods deal with neither class or Instance attributes 

        # •InstanceMeathods will have 'self' as default input parameter, as they deal with attributes of object (Instance attributes)
        # ClassMeathods will have 'cls' as default input parameter, as they deal with attributes of class (class attributes), class attributes applies to all the objects in that class under same memory space\address 
        # StaticMeathods will not have any input parameters, as they deal with nothing under the class 

        # •InstanceMeathods will not have any decorators 
        # ClassMeathods will have '@ClassMeathod' as decorator
        # StaticMeathods will have '@StaticMeathod' as decorator 
            
            # •decorators are explained in vid -44, they are functions that takes below meathods as input
                @decorator
                def meathod(cls):   # this is ClassMeathod as it has 'cls' input
                    Or 
                var = decorator(meathod) 
                var(cls)            # the 'cls' input is passed to var, which is passed to meathod & then the result will be passed to decorator
        
        # •below are the ways to run each type of meathod
        class.meathod(object) Or    # 2 ways to run InstanceMeathod
        object.meathod() 

        class.meathod()  # 1 way to run ClassMeathod

        class.meathod()  # 1 way to run StaticMeathod
        # so to run static or ClassMeathods we use className 

            # lets say if you want to perform certain operations on the objects of another class 
            # in that sinario we've to go with StaticMeathods, as the sinario has nothing to do with class attributes & Instance attributes of this class 


        | instance meathods                                         | Class Meathods                                         | Static Meathods                                |
        | +-------------------------------------------------------+ | +----------------------------------------------------+ | +--------------------------------------------+ |
        | deal with Instance attributes (either setting Or getting) | deal with class attributes (either setting Or getting) | deal with neither class or Instance attributes |
        | default input parameter → 'self'                          | default input parameter → 'cls'                        | there will be no default input parameter       |
        | no decorators                                             | '@ClassMeathod' as decorator                           | '@StaticMeathod' as decorator                  |
        | class.meathod(object) Or object.meathod()                 | class.meathod()                                        | class.meathod()                                |


    #!VIDSUMMARY 
#!VID 


#VID 54.Inner Class 
    
    # till now we've seen about different types of variables & meathods 
        # so, a class can contain different types of attributes & meathods 
    # can we have nested class --> like python supports nested meathods 

    #T defying Inner Class :- 
        # lets say we want to create a 'student' class, which gives details about the student like - name,roll number ETC.
        # we want to create a sepeate class for laptop details of the student

            class student():        
                def __init__(self,name,rollNo):    # arguments to these input parameters will be passed using the constructor while creating an object
                    self.name = name 
                    self.rollNo = rollNo

                def show(self):                     # we can directly print the attributes of an attribute --> ObjName.name Or ObjName.rollNo
                    print(self.name,self.rollno)    # Or we can use the instance get meathod like this 

                """ now if we also want to have the laptop details as well 
                    we can create them in the present class itself, by adding input parameters to the above constructor,
                    Or we can go with sepeate laptop class Or 
                    Or we can create a nested laptop class in this class, because laptop class will be only used by student class """
                
                class laptop():
                    def __init__(self):
                        self.brand = 'hp'
                        self.cpu = 'i7'
                        self.ram = 16
    #!T 

    #T How to define objects of inner class 
        # In the above example we've created a laptop class inside a outer student class 
        #IMP Tipically the objects of inner class are created inside the constructor (__init__) of outer class 

            class student():
                def __init__(self,name,rollno):
                    self.name = name,
                    self.rollno = rollno
                    self.varName = self.laptop() # here we've created the inner class object

                    """ as its a inner class and cannot be accessed directly, we've to use --> self.laptop()
                        the created inner class object is stored in attribute varName of self 
                        we can give any name instead of varName """

                class laptop():
                    def __init__(self):
                    self.brand = 'hp'
                    self.cpu = 'i7'
                    self.ram = 16
    #!T 

    #T How to get the values of an attribute for an inner class 
        # previously we've created(instantuated) a laptop (inner class) object inside the constructor of the outer class object
        # and stored it in the varName attribute of the outer class object
        # hence inoder to access the attributes of the inner class object, we've to say --> OuterClassObj.varName.InnerClassAtt
            # OuterClassObj.varName ==> represents InnerclassObj 
            # OuterClassObj.varName.cpu ==> represents the cpu attribute of InnerclassObj

        # Or we can use below meathod
            InnObj = OuterClassObj.varName  ==> # now InnObj respresents InnerclassObj
            InnObj.cpu  ==> # we're retriving cpu attribute of InnerclassObj

        s1 = student('prem',1)  
            # s1 OuterClassObj will be created. 
            # prem & 1 will be assigned to respective attributes of OuterClassObj  ==> self.name = name ; self.rollno = rollno
            # InnerclassObj will be created and stored in varName attribute of this OuterClassObj ==> self.varName = self.laptop()
        s1.varName.cpu => 'i5'
            # here, we're accessing the cpu attribute of InnerclassObj

        Or,
        InnObj = s1.varName  # This will create InnerClass laptopObj, as its stored in varName attribute of s1 which is OuterClassObj
        InnObj.cpu ==> 'i5'
 
        # SO,as the laptop InnerclassObj is inside the varName attribute of InnerclassObj, we've to say ==> s1.varName.cpu
        # if we are sure that laptop class is only used for student class, then instead of creating 2 different classes we can got with laptop class as inner class for outer student class  

    #!T 

    #T How to create InnerclassObj on console 
        # in the above, we've defined the InnerclassObj inside the constructor of the OuterClassObj and stored that in a attribute 'VarName'
        # lets say we dont want to do that, instead we want to create an object directly on the editor 

            lapObj = student.laptop()  # this will the constructor for the InnerClass
                # we cannot access the Innerclass constructor directly, because its inside the OuterClass student
                 
        # so point to remember is :- 
            # we can create objects of Innerclass using 2 ways :- 
                # inside the constructor of the OuterClass Or 
                # Outside, on the editor, by using OuterClass name to call the Innerclass constructor => student.laptop() 

    #!T 

    #T What if outer & inner class have a meathod with same name 
        # Lets say outer & inner class has a meathod with the same name --> show() 
            # show() meathod of OuterClass will print the attributes of OuterClass
            # show() meathod of InnerClass will print the attributes of Innerclass
            # note that these 2 meathods are different and python will point to the meathod based on the object we pass 

            class student():
                def __init__(self,name,rollno):
                    self.name = name
                    self.rollno = rollno
                    self.lapObj = self.laptop()     # here we've created the InnerclassObj in the constructor of the OuterClass

                    """ hence to create InnerclassObj
                            we've to use 'lapObj' attribute of OuterClassObj 'self'
                            ==> self.lapObj """

                def show(self):     # this is a OuterClass meathod
                    print(self.name,self.rollno)
                    self.lapObj.show()  # here we're trying to access the show() meathod of InnerClass using self.lapObj, as it contains the InnerclassObj

            class laptop(self):
                def __init__(self,cpu,ram,brand):
                    self.cpu = cpu 
                    self.ram = ram 
                    self.brand = brand 
                
                def show(self):     # this is a Innerclass meathod with same name as OuterClass meathod
                    print(self.cpu, self.ram, self.brand)

                
            s1 = student()
            s1.show()   # this will execute the OuterClass show() meathod
            s1.lapObj.show() # this will execute the InnerClass show() meathod

            # lets say we didnot create any InnerclassObj under the constructor of the OuterClass, then we can use the below meathod
            laptopObj = student.laptop() # creating InnerclassObj
            laptopObj.show()    # then accessing or executing the Innerclass show() meathod on the InnerclassObj that is created above 
    #!T 

#VIDSUMMARY 
    # in python we can have nested --> meathods & classes 
    # •if a class contain a inner class, we can create the innerClassObjs in 2 ways :-
        # in the constructor of the outerClass, created innerClassObj will be stored in the attribute of the outerClassObj ==> self.InnerClassObj = self.innerClassName()
        # Outside the class, on the editor, using the constructor of the innerClass. Note we've to access the constructor of the innerClass using the outerClass name ==> InnerClassObj = outerClassName.innerClassName()

        Meathod-1 :-
            class student():
            def __init__(self,name,rollno):
                self.name = name,
                self.rollno = rollno
                self.varName = self.laptop() # creating innerClassObj in the constructor of the outerClass
                    """ we cannot access the innerClass constructor directly as its a innerClass
                        we've to use self, which is the outerClassObj to access it 
                        the created innerClassObj is stored in varName attribute of outerClassObj """

            class laptop():
                def __init__(self):
                self.brand = 'hp'
                self.cpu = 'i7'
                self.ram = 16
        
        Meathod 2 :- 
            # lets say that innerClassObj is not created in the constructor of the outerClass
            laptopObj = student.laptop()  # here we're creating the innerClassObj using the constructor of the innerClass
                # but to access the constructor of the innerClass we need to use the outerClassName, as its a innerClass
        
            #! So, remember that inorder to access the innerClass constructor we've to either use innerClassObj or innerClassName
                # we cannot access it directly

    # •2 ways to get the values of an attribute of innerClass :-
        s1 = student('prem',1)  # creating outerClassObj
        s1.varName.cpu  # s1.varName constains innerClassObj, s1.varName.cpu --> accessing the cpu attribute of innerClassObj
            
            Or 
        
        laptopObj = student.laptop() # creating innerClassObj using the constructor of the innerClass, we've to access it using the outerClassName
        laptopObj.cpu   # then access the cpu attribute of innerClassObj

    
    # •if innerClass & outerClass has a meathod with same name :-
        # note that these 2 meathods will be different and python will point to the meathod based on the object we pass (innerClassObj or outerClassObj)
        # we know how to execute outerClass instance meathods, lets see how to access innerClass meathod

        class student():
            def __init__(self,name,rollno):
                self.lapObj = self.laptop()  # if innerClassObj is created in the constructor of outerClass

            def show(self):     # this is a OuterClass meathod
                print(self.name,self.rollno)
                self.lapObj.show()  #!way-1 here we're trying to access the show() meathod of InnerClass using self.lapObj, as it contains the InnerclassObj

            class laptop(self):
                def __init__(self,cpu,ram,brand):
                    self.cpu = cpu 
                    self.ram = ram 
                    self.brand = brand 
            
            def show(self):     # this is a Innerclass meathod with same name as OuterClass meathod
                print(self.cpu, self.ram, self.brand)

        
        s1 = student()
        s1.lapObj.show()  #!way-2 this will execute the InnerClass show() meathod
        
        # lets say we didnot create any InnerclassObj under the constructor of the OuterClass, #!then we can use the below meathod → way - 3
        laptopObj = student.laptop() # creating InnerclassObj
        laptopObj.show()    # then accessing or executing the Innerclass show() meathod on the InnerclassObj that is created above

        # it can be done in 3 ways :-
            # inside the meathod of outerClass, accessing the innerClass meathod using 'self.lapObj', for this innerClassObj has to be created inside the constructor of the outerClass
            # similar to above, create outerClassObj using the constructor of the outerClass and access the innerClass meathod using the lapObj attribute of the outerClassObj on the editor 
            # Or creating innerClassObj using the constructor of innerClass and then executing the innerClass meathod

#!VIDSUMMARY 
#!VID 

VID 55.Inheritance
        # as we discussed previously, all the OOPS programming languages will have certain concepts like --> Inheritance,Polymorphism,Encapsulation etc 
        # there are 3 types of Inheritance 
            # single level Inheritance → class B(A): ==> class B inherits all the attributes & methods from class A » class A will be the parent class 
            # multi-level Inheritance  → class C(B): ==> class C inherits from B, which inherits from A, hence class C inherits from A & B » Class A will be grand parent class
            # multiple Inheritance →  class D(A,X): ==> class D inherits from both classes A & X 
        
        # Inheritance is nothing but inheriting all the meathods & attributes of parent class 
        # so, with the use of Inheritance we dont have to redefine the meathods & attributes that exist in one of the class, we just have to inherit from that class  

        Syntax :- 
            class ClassName(inheriting ClassName):
                pass 

        # Parent\Super Class  <=> Child\Sub Class 

    | single level Inheritance | Multi level Inheritance | multiple Inheritance |
    | +----------------------+ | +---------------------+ | +------------------+ |
    | class B(A)               | class B(A) & class C(B) | class D(A,X)         |
    | A→B                      | A-B → C                 | A→D & X→D            |

#!VID 


#VID 56.Constructor Inheritance
    
    #TOPIC Constructor Inheritance
        #T Constructor Inheritance behaviour in single level Inheritance
            # Lets say  Class A is super class & Class B is Child class --> single level Inheritance
            # now lets see which constructor meathod will be called on creating ChildClassObj 
                #IMP If the constructor is not defined in both the classes, then constructor of parent class will be called to create ChildClassObj
                #IMP if ChildClass has a constructor, then its own constructor will be called on creating a ChildClassObj
        
        #EG1 :- 
            # In the below example we can see that both parent & Child class dosent have constructors defined 

            class A:
                def feature1(self):
                    print('A-feature1') 
                def feature2(self):
                    print('A-feature2') 
            
            class B(A):
                def feature1(self):
                    print('B-feature1') 
                def feature2(self):
                    print('B-feature2')

            AObj = A()  # even if we dont have __init__(self): constructor meathod define, it'll be called, here we're calling parent class constructor 
            BObj = B()  # as ChildClass dosent have a constructor, hence python will go a execute higher scope or higher class constructor ==> A() 

            # This is similar to the scopes that we discussed previously 
            # lets say → parentClass has constructor defined, but ChildClass dosent have it 
                # on on creation of ChildClassObj, as ChildClass dosent have a constructor, python will look at higher scope and execute the parentClass constructor
                # If the ChildClass has its own constructor, the python will not look at higher scope and will execute this ChildClass constructor
            
            # On creation of ChildClass --> checks for ChildClass constructor --> if its not there, then it'll go for parentClass constructor

            # Also note that :-
                # all the attributes & meathods of parentClass can be accessed by ChildClass
                # But this is not viceversa --> parentClass cannot access ChildClass attributes & meathods 

                # A SubClass can access all the features from SuperClass 
                # A SuperClass cannot access all the features from  SubClass
        #!T 
        
        #T Super() meathod → to access parentClass attributes & meathods in a ChildClass explicitly
            # Now lets say both the parentClass & ChildClass has their own constructors 
            # now Since the ChildClass has its own constructor, on creating a ChildClassObj, ChildClass constructor will be called 
            # now can we call the parentClass constructor explicitly in the ChildClass in this sinario 
                # we can do that with super() method → it represents a parentClassObj 
                # using super() meathod we can access all the attributes & meathods of parentClass
                    # super().attribute Or super().meathod() » Super() acts like parentClassObj   
            
            #EG1:- 
            class A:
                def __init__(self):
                    print('constructor of A')
                def feature1(self):
                    print('A-feature1') 
                def feature2(self):
                    print('A-feature2') 
            
            class B(A):
                def __init__(self):
                    print('constructor of B')
                    super().__init__()  #! here we're trying to call the __init__() meathod of parent class A 
                def feature1(self):
                    print('B-feature1') 
                def feature2(self):
                    print('B-feature2')
            
        #!T 
    
    
        #T Constructor Inheritance behaviour in multi level Inheritance
            # In MultiLevel Inheritance --> MRO kicks in  
                # IMP MRO --> Meathod Resolution Order  
                    # First the current class will be checked for attributes & meathods 
                    # then the first parentClass will be checked and then the 2nd parentClass       
                    # class c(x,y) → MRO starts from left to right (x → y )
                
            # now lets say we've class X & Y, and class z will inherit from both x&y 
            # lets also say that class X & Y has constructor defined 
                # Now on creating an ChildClassObj, the constructor of 1st parentClass X will be executed as ChildClass dosent have a constructor
                # As ChildClass Z has 2 SuperClass X & Y 
                    # As per MRO, the 1st parentClass (towards the left) will be checked first, for attributes and meathods, hence the constructor of X will be executed   
            
            #EG1 :- lets say in the ChildClass, we want to call a meathod of parentClass  
                # hence we've used super() meathod ==> super().feature1() 
                # now the twist is both the parentClass has the same meathod (with same name)
                # so as per MRO, the first parentClass meathod will be executed that is X class
                
                class X:
                    def __init__(self):
                        print('constructor of X')
                    def feature1(self):
                        print('X-feature1') 
                    def feature2(self):
                        print('X-feature2') 
                
                class Y:
                    def __init__(self):
                        print('constructor of Y')
                    def feature1(self):
                        print('Y-feature1') 
                    def feature2(self):
                        print('Y-feature2')
                
                class Z(X,Y):
                    def __init__(self):
                        print('constructor of X')
                        super().__init__()  # as per MRO constructor of class A will be executed
                        super().feature1    # both parentClass X & Y has this same meathod, but as per MRO class X meathod will be executed 
    
                Zobj = Z() 
                Zobj.feature1() 
                    # feature1 meathod is not in Z 
                    # Looks for parentClass, but we've 2, MRO kicks in  
                    # looks in 1st parentClass, if its not ther 
                    # looks in 2nd parentClass Finally
        #!T   
    #!TOPIC 
    
    #VIDSUMMARY 
        # As a constructor is a __init__() meathod in a class, its inheritance is similar to scope of any meathod in the class 

        # ChildClass can access all the attributes & meathods of ParentClass, this is not true in viceversa 

        # •constructor inheritance in single level inheritance
            # Class B inherits from ParentClass A 
            # On creating a ChildClassObj (Bobj), 
                # python will check for the constructor under the current scope, this is the constructor of the ChildClass, if its not available 
            # Then python will check for the constructor in the higher scope, this in the ParentClass 

            # we all know that we can skip the constructor meathod inside the class, but can still use the constructor while creating the objects 
            # lets say if both the ParentClass & ChildClass dosent have the constructor
            # then python will use the default constructor of the ParentClass on creating a ChildClassObj
        
        # •Super() meathod → to access parentClass attributes & meathods in a ChildClass » 'explicitly'
            # as per the scope python will look into the higher scope, if object is not available under current scope
            # now lets say we want to access the object of higher scope explicitly --> then we can use super() meathod
            # using super() meathod we can access all the attributes & meathods of parentClass
            # super().attribute Or super().meathod() » Super() acts like parentClassObj

        # •Constructor Inheritance in multi level Inheritance
            # In MultiLevel Inheritance --> MRO kicks in  
                # ·MRO --> Meathod Resolution Order  
                    # First the current class will be checked for attributes & meathods 
                    # then the first parentClass will be checked and then the 2nd parentClass       
                        # class c(x,y) → MRO starts from left to right (x → y )

            # so, even though we've same meathod in both the parentClass, the meathod of the 1st parentClass, which is on the left will be executed (that is x parentClass meathod)
    #!VIDSUMMARY 
#!VID 

#VID 57.Polymorphism

    # Along with inheritance, Polymorphism is a major concept in OOPS
    # it can broken down into 
        # !Poly + morphism
        # !Many + form  ==> which also means » one object can take multiple forms 
    
    # this concept is very important in software dovelopment 
    # •Polymorphism is used in 
        # loose coupling 
        # Dependency Injection 
        # Interfaces ETC 
    
    # •4 ways to implement Polymorphism
        # Duck Typing 
        # Operator Overloading 
        # Meathod Overloading
        # Meathod Overriding 

    # in Java,C++ & C#, we've to mention the datatype of the variable\object before creating it 
    # in python its different, we'll see that in next vid 
    # we'll also see how to implement Polymorphism
#!VID 


#VID 58.Duck Typing 

    # Please watch previous vid 
    # In this vid lets see one of the way to implement Polymorphism → Duck Typing

    # if a bird is 
        # quacking like a Duck
        # walking like a Duck 
        # swimming like a Duck 
            # Then its a Duck
    # InotherWords if the behaviour of the bird is matching with the behaviour of the Duck, then its a Duck
        # it dosent matter if its a real Duck or not 
    
    # now lets see how python implements this behaviour

    #T Dynamic Typing in python
        # in python we dont have to specify the datatype of the variable while creating, its datatype will be implicitly figured out by python based on the values we store under that variable
    #!T 

    #EG - 1 :- 
        # lets consider the below code   
            x = 5 
            x = 'Naveen'

            # Technically we say that the value of 'x' is changed to 'Naveen'
            # But logically -->
                # when 'x = 5', in the Heap memory a space will be allocated for type int, and the memory address of that space will be assiged to the variable 'x', and 'x' is just the tag for that memory space or memory address 
                # when 'x = 'Naveen', again a space for this string will be created and now tag x points to this memory space allocated for the string
                    # so, here 'x' is just a tag to the data init and
                    # 'x' tag will not have any specific datatype
                    # type(x) => will retrun the datatype of the value stored init
                
                # so, here 'x' is taking many forms, as its datatype is changing According to the value stored init → Eg of Polymorphism

    #Eg :- 2
        # lets take another example for understanding Duck Typing
        # lets say we've a class laptop, and it has a meathod 'code()'
            # this meathod accepts an IDEObj which is an object of another class 
        
            class laptop(): 
                def code(self,IDE): # here the 'code()' meathod accepts IDEObj 
                    IDE.execute()   # and then executes the execute() instanceMeathod of IDEObj

            class pycharm():    # hence we're creating an another class here
                def execute(self):  # which has execute() meathod
                    print('Now IDE is pycharm')


        # now lets say we want to run the code() meathod of laptop class, for this we need to create a laptopObj first
            # but the code() meathod of laptop class take, an object of another class which has execute() meathod
            # so, first we need to create an object of another class 

            pycharmObj = pycharm()      # creating an object of class which has execute() meathod
            lapObj = laptop()           # creating laptopObj
            lapObj.code(pycharmObj)  # executing the 'code()' meathod of laptopObj

        # here note that the code() meathod in the laptop class takes an object of another class as argument to 'IDE' input parameter
            # that class can be anything that has a execute() meathod init 
            # to prove that lets create an another class that has execute meathod init 

            class Vscode():
                def execute(self):
                    print('Ide is Vscode')

        # now we've one laptop class and 2 other classes that has execute() meathod
        # hence both the other classes has the execute() meathod, the code() meathod in laptop class dosent care which object is passed to IDE input parameter
            # as long as it has an execute() meathod for that object

        # InotherWords, the IDE input parameter of the code() meathod of the main laptop class, is not fixed to pycharmObj
            # because python supports DynamicTyping, and hence we can pass any class object that has execute() meathod

        # it dosent matter which class object we're passing, what matters is that object has to have execute() meathod

            VscodeObj = Vscode()
            lapObj = laptop()
            lapObj.code(VscodeObj)

        # a bird thats swimming like a Duck, walking like a Duck its a Duck
        # any object which has an execute meathod, can be passed to IDE input parameter of code() meathod of laptop class
        # this is Duck Typing --> a way to implement Polymorphism

        # In JAVA we've a concept of Interfaces 
            # we'll have an Interfaces
            # we'll also have classes like Vscode & pycharm that will implement that Interface 

        # different IDEs for JAVA :- Netbeans,eclipse,Inteli-j

    #VIDSUMMARY 
        # !Duck Typing is one of the way to implement polymorphism behaviour in python 
        # !if the behaviour of the bird is matching with the behaviour of the Duck, then its a Duck, dosent matter if its a real duck or not 

        # !python gets this polymorphism behaviour because of Dynamic Typing concept 
            # which is python automatically detects the datatype of the variable by looking at the values stored init and we dont have to explicity specify the datatype of the variable before creating it  

        #EGs of polymorphism/duck Typing in python :- 
            EG1 :-
                x = 5   # 'X' is a tag to int memory space\address in Heap memory
                x = 'N' # Now 'X' tags to string memory space\address 

                # here 'x' is a tag, and its of no datatype, type(x) will get the datatype of the values stored in x, its not the datatype of tag 'x' 
                # here 'x' is taking many forms, as its datatype is changing According to the value stored init → hence its a Eg of Polymorphism 

            Eg2 :-
                # lets say we've a class, which has a meathod init, and this meathod takes an object as input and executes duck() meathod of that passed in object
                # now this meathod dosent care from which class this object is comming from, as long as it has duck() meathod init 
                # here the input parameter of the meathod which takes in the object, is taking many forms by accepting any object that has duck() meathod
                # it dosent matter which class object we're passing, what matters is that object has to have execute() meathod
                # hence its an another example of polymorphism 

                # a bird thats swimming like a Duck, walking like a Duck its a Duck
                # any object which has an duck() meathod, can be passed to input parameter of the meathod of main class
                # this is Duck Typing --> a way to implement Polymorphism

        # !we can see that in both the examples, python get the polymorphism behaviour because of dynamic Typing
    #!VIDSUMMARY 
#!VID 

#VID 59.Operator Overloading

    #T Operator Overloading\Overriding of inbuild class 
        # In the previous vid we've seen one of the way to implement polymorphism → duck Typing
        # In this vid we'll see another way → Operator Overloading
            # its best to remember it as 'operator Overwriting'

        # "+,-,*,%,/" are some of the operators in python
            5 + 6   # 5,6 → Operands & '+' → operator

        # 5 + 6         # we can add 2 ints 
        # 5 + 6.2       # we can add int & float (python supports this)
        # 'p' + 'r'     # we can add two strings

        # 1 + 'p'       # but we cannot add an int & string

        # now lets understand, whats happening behind the scenes :-
            # we know that everything in python is an object
            # hence the blow variables a & b also objects, and they belong to 'int class' 
                a = 5
                b = 6
            
            # we know that a class contain multiple meathods, so that int class also contains meathod called → __add__(self,x)
            # int.__add__(self,x) ==> it talkes 2 parameters 
                # self → the object itself
                # x → another int object
            
                int.__add__(a,b)  == a+b     # !whenever we say a+b, python will call the int.__add__() meathod behind the scenes

            # if a & b are strings, and when we all these, then the __add__() meathod of the string class will be called 
                a = '5'
                b = '6'

                str.__add__(a,b)  == a + b   # !as a & b belogns to string class, str.__add__() meathod is called behind the scenes

            # if  'a' is int & 'b' is string, dynamic Typing of python will be in confution, because it cannot decide which class these variables fall under 
                # it'll try converting, but int cannot be converted to string & viceversa and hence it'll fail 

            
            # So, when we use '+' => __add__() magicMeathod of that class will be called 
                # '-' => __sub__() 
                # '*' => __mul__() 
            
        # InotherWords we can say that, respective operator is Overloaded or Overrided with respective magicMeathod
    #!T 

    #T Operator Overloading\Overriding in custum class 
        # now lets see how we can operatorOverload in our own class 

        #T '+' operatorOverload
            # lets say we've student class with m1 & m2 attributes 

                class student(self,m1,m2):
                    self.m1 = m1
                    self.m2 = m2

                s1 = student(68,52)
                s2 = student(92,85)
                
            # now we want to perform '+' operation on 2 student Objects 
            # but as discussed above s1 + s2 will call __add__() magicMeathod behind the scenes, hence we need to define that meathod
        
                class student(self,m1,m2):
                    self.m1 = m1
                    self.m2 = m2

                    def __add__(self,other):    # object on which this meathod executes is self, other object will be other, we can change the other variable name  
                        r1 = self.m1 + other.m1 # we're adding the respective m1 marks of each student
                        r2 = self.m2 + other.m2
                        return student(r1,r2)   # and then creating a new student object, with added up marks and returning that object

                s1 = student(68,52)
                s2 = student(92,85)

                s3 = s1 + s2  # now it works  ==> student.__add__(s1,s2)

            # so, if the objects of your class has to be able to perform operations using '+' operator, we need to Overload\override that operator using __add__() magicMeathod
            # we can do the same for → *,>=,>,<=,<
        #!T 
        
        #T greater(>) operatorOverload
            # without defining the __ge__() magicMeathod in our class and if we say s1 > s2 → TypeError: '>' not supported between the instance of s1 & s2 

                class student(self,m1,m2):
                    self.m1 = m1
                    self.m2 = m2

                    def __add__(self,other):     
                        r1 = self.m1 + other.m1  
                        r2 = self.m2 + other.m2
                        return student(r1,r2)  

                    def __ge__(self,other):
                        tms1 = self.m1 + self.m2    # we're adding up m1 & m2 marks of each student
                        tms2 = other.m1 + other.m2
                        if tms1 > tms2:
                            return True 
                        else:
                            False 


                s1 = student(68,52)
                s2 = student(92,85)

                if s1 > s2:
                    print('s1 wins')
                else:
                    print('s2 wins')

        #!T 
        #!T 

        #T __str__() magicMeathod (called for print())
                print(a)  # will print the value of 'a'
            # but behind the scenes __str__() meathod of the respective class will be called , and it converts value in 'a' to string format and prints it 
            # but if the respective class dosent have this magicMeathod, then as per scope python will look in build-in functions
                # we also have a build-in function => __str__() → it prints the memory address of the value in 'a'
                # in this format → <__main__.int object at 0x00ca00dd>


            # now as our class dosent have __str__() magicMeathod, so when we try to print, inbuild __str__() will be called and below will be printed
                print(s1) → <__main__.student object at 0x00ca00dd>

            # so, inoder to print the s1 value as string, we need to override\Overload the inbuild __str__() meathod
                # with our own __str__() meathod under our class, so that python will not look into inbuild classes as per scope 
            
                class student(self,m1,m2):
                    self.m1 = m1
                    self.m2 = m2

                def __str__(self):
                    return '{} {}'.format(self.m1,self.m2)   
                    """ retrun self.m1,self.m1  # will not work because, it returns a tuple 
                            1,1 will be a tupe → (1,1)
                        It should return a string """

                #! Note that __str__ has to only return string, otherwise Print() meathod will not work 
                # format() meathod is a string class meathod, which dynamically fills the place holders

            s1 = student(58,26)
            print(s1)  -> # calls → student.__str__(s1) => 58 26
        #!T 

        | Operator | respective magicMeathod called |
        | +------+ | +----------------------------+ |
        | +        | __add__(self,other)            |
        | -        | __sub__(self,other)            |
        | *        | __mul__(self,other)            |
        | /        | __div__(self,other)            |
        | >        | __gt__(self,other)             |
        | <        | __lt__(self,other)             |
        | >=       | __ge__(self,other)             |
        | <=       | __le__(self,other)             |

    #VIDSUMMARY     
        # this concept is also there in powershell
        # OperatorOverloading => OperatorOverwriting 
        # its another way to implementing polymorphism 

        # on execution of any operator ("+,-,*,%,/") --> their respective magicMeathods from the respective class will be called
            # 5 + 6      => int.__add__(5,6) magicMeathod will be called 
            # 'a' +' b'  => str.__add__(a,b) magicMeathod will be called 
            
            # 5 + 'a'    => both these objects belong to different classes, hence dynamic Typing of python fails and results in error 
                                # it first try to convert them, but int or str cannot be converted from one to another
        
        # So,we can say that, respective operator is Overloaded or Overrided with respective magicMeathod

        #• we can also do that inour own class
            # if our class objects has to be able to perform operations using operators --> we've to define respective magicMeathod under our class 

                class student(self,m1,m2):
                    self.m1 = m1
                    self.m2 = m2

                    def __add__(self,other):        # called when s1 + s2
                        r1 = self.m1 + other.m1  
                        r2 = self.m2 + other.m2
                        return student(r1,r2)  

                    def __ge__(self,other):         # called when s1 > s2
                        tms1 = self.m1 + self.m2    
                        tms2 = other.m1 + other.m2
                        if tms1 > tms2:
                            return True 
                        else:
                            False 
        
        #• __str__() magicMeathod (called for print())
                print(5)  # this will call the __str__() magicMeathod of int class, this magicMeathod will convert data to string format and prints it
            # If its not available, as per scope, python will execute the __str__() inbuilt magicMeathod 
                # it outputs will be like --> <__main__.int object at 0x00ca00dd>
            
            # similar thing goes to our class 
            # if __str__() magicMeathod is available in our class, then inbuilt magicMeathod will be called, which outputs <__main__.int object at 0x00ca00dd> instead of string value  
            # we need to override\Overload the inbuild __str__() meathod with our own meathod

                class student(self,m1,m2):
                    self.m1 = m1
                    self.m2 = m2

                def __str__(self):
                    return '{} {}'.format(self.m1,self.m2)    # format() meathod is a string class meathod, which dynamically fills the place holders
                
                #! Note that our __str__ has to only return string, otherwise Print() meathod will not work

                s1 = student(81,82)
                print(s1) ==> student.__str__(s1) » 81 82

        | Operator | respective magicMeathod called |
        | +------+ | +----------------------------+ |
        | +        | __add__(self,other)            |
        | -        | __sub__(self,other)            |
        | *        | __mul__(self,other)            |
        | /        | __div__(self,other)            |
        | >        | __gt__(self,other)             |
        | <        | __lt__(self,other)             |
        | >=       | __ge__(self,other)             |
        | <=       | __le__(self,other)             |

    #!VIDSUMMARY 
#!VID 


#VID 60.Method Overloading and Method Overriding 

    #T meathod Overloading   
        # IMP this concept is available in C,C++,Java. But its not available in python

        def :- 
            # IMP if a class has 2 Methods with same name & code, but with different parameters set,then respective meathods will be called based on the arguments we pass--> this concept is called meathod Overloading
            # IMP in python we dont have this concept --> because in python we cannot create meathod with same name in one class  
                EG :- 
                    # a class contains 2 meathods with 
                        # same name but different parameter set , one has two parameters, other has 3 parameters 
                        # while execution of the meathod, if we give two parameters, 1st meathod will be executed, if 3 are given 2nd meathod will be executed 
                    # as we can define meathods with same name in other programming languages, we can do above, but python dosent support meathod Overloading

                    # so how to implement meathod Overloading in python, without defying meathod with same name in a class
                        # we can solve this by defaulting the parameters to none (default arguments to parameters)
                        # so if no argument is provided to parameters, then they will default to their default value and not result in error 
                    # Or we can solve this using the variable length parameters 
                        # *param ==> a tuple                 

                # authour himself dosent have clarity on this ;)
    #!T 

    #T meathod Overriding
        # IMP We've discussed the same in --> vid 56.Constructor Inheritance → topic-Constructor Inheritance behaviour in single level Inheritance
        # this concept is famous in software industry, its used in Interfaces & abstract classes concepts also 
        def :- 
            # IMP lets say class B inherits class A  
            # IMP as per scope, if an object is not found in the current scope (class B), then python will check the higher scope (class A)
            # If both the classes have a meathod with same name & parameter set, as ChildClass inherits all the parentClass meathods, So the ChildClass will have 2 meathods with same name now (one from parent & other from Child) 
            # Now the parentClass meathod will be Overrided by the ChildClass meathod in the ChildClass--> this is called meathod Overriding
    #!T 
#!VID 

#VID Abstract Class and Abstract Method in Python
    
    # Def :-
        # AbstractClass   :- If a class contains one or more abstract meathods, then that class will be a abstract class
                                # an AbstractClass can have mul AbstractMeathods & normal meathods also   
        # AbstractMeathod :- It'll have '@AbstractMeathod' as a decorator, and it'll have a empty body (a pass statement)
            # InotherWords, these meathods will only have declaration and not have definition (no code inside)  
    
    # we cannot instantuate (create objects of) an AbstractClass
    # Python by default dosent support abstract class\method, other languages support this by default
    # inorder to support we need to import ABC module --> Abstract Base Class    
        # and then add the decorators to the AbstractMeathods  

    # eg - 1 :- 
        # As we said that python dosent support AbstractClass by default
        # even if we define a class with empty meathod init, we can still instantuate that class object 
        # but as the object will have an empty Meathod and on executing that meathod on the object will produce no result
        
            class class1:
                def meathod1(self):
                    pass            # meathod is empty (AbstractMeathod)

            obj1 = class1()
            obj1.meathod1()
                >Process finished with exit code 0  # we can see that meathod got executed with empty results

            # so we're able to instantuate and execute the meathods, because the above is not the AbstractClass yet as python dosent support AbstractClass by default
        
            from abc import ABC,AbstractMeathod     # so we need to import ABC & AbstractMeathod classes from 'abc' module
            class class1(ABC):  # AbstractClass has to be inherit from ABC class 
            @abstractmeathod    # below meathod will be passed to this decorator func, and this fun adds extra features to below fun,without modifying it 
            def meathod1(self):
                pass  

            obj1 = class()      # as above class is now AbstractClass
            > cant instantuate AbstractClass    # we cannot instantuate it 


    #Eg - 2 
        # AbstractClass concept also works with inheritance
        # lets say we've defined another class, that inherits from above AbstractClass class1 
        # So, this will be a multi-level inheritance (ABC→class1→thisclass)
        # so, any classes that inherits from a AbstractClass, will also be a AbstractClass, provided the body of meathods or that class should be empty

            def class2(class1):  # as its inheriting from a AbstractClass it'll be a AbstractClass, hence we cannot instantuate it  
                pass 

            obj1 = class2()     # gives error  

            # but if we define a body, then it'll not be a AbstractClass, even though it inherits from AbstractClass
            def class2(class1):
                def meathod1:
                    print('this is not AbstractMeathod')

            # AbstractClass will have atleast one AbstractMeathod

    # ussage :- 
        # AbstractClass & meathods only makes sence, when we're designing the application in a OOPS way  
        # ?we can create an AbstractClass so that other classes will have some restriction on which class to use 
        # eg:- lets say we've created an API, for someone who wants to use our API, they have to define their own meathods

    #VIDSUMMARY 
            # AbstractClass   :- If a class contains one or more abstract meathods, then that class will be a abstract class
                                    # an AbstractClass can have mul AbstractMeathods & also normal meathods, but one of them should be AbstractMeathod   
            # AbstractMeathod :- It'll have '@AbstractMeathod' as a decorator, and it'll have a empty body (a pass statement)
                # InotherWords, these meathods will only have declaration and not have definition (no code inside)  
        
        # we cannot instantuate (create objects of) an AbstractClass
        # Python by default dosent support abstract class\method, other languages support this by default
            # if we define a class that has empty meathod init, we can still instantuate that class 
            # because Python dosent support AbstractClass by default and will not treat above as AbstractClass as other languages do

        # inorder to support we need to import 'abc' module --> Abstract Base Class --> from abc import ABC,AbstractMeathod   
            # out class has to inherit from ABC class
            # and then add the decorator '@abstractmeathod' to the AbstractMeathods  

        # AbstractClass concept also works with inheritance 
        # so, any classes that inherits from an AbstractClass, will also be a AbstractClass, provided that the body of atleast one of the meathod or the entire class should be empty
            # because AbstractClass should have atleast one AbstractMeathod
        # InotherWords, eventhough a class inherits from an AbstractClass, but if it dosent have atleast one AbstractMeathod (empty meathod), then it'll not be considered as AbstractClass


        Ussage eg :- 
            # AbstractClass & meathods only makes sence, when we're designing the application in a OOPS way  
            # ?we can create an AbstractClass so that other classes will have some restriction on which class to use 
            # eg:- lets say we've created an API, for someone who wants to use our API, they have to define their own meathods

    #!VIDSUMMARY 
#!VID 



//========================================================================================
/*                                                                                      *
 *                             Telsuko --< Naveen Reddy >--  Part2                        *
 *                                                                                      */
//==========================================================================from 61==========

#VID 61.Iterator
    # Iterator objects are used for iterations, its similar to 'i++' concept in other programming languages
    # !even for a 'for loop', what makes it work is a 'Iterator', internally for loop calls the __next__() Meathod

    #T iter() function - creates iteratorObjs 
        # it takes in iterable and converts them into iteratorObjs 
        # using iteratorObjs.__next__() method we can get one value at a time from it 

            nums = [1,2,3,4]               # an iterable
            iteratorObjs = iter(nums)      # we've converted it into iteratorObjs using iter() function
            
            print(iteratorObjs)            # if we use print() function
                <list_iterator object at 0x354aef54>    # its printing the memory address of the iteratorObjs

            print(iteratorObjs.__next__()) # the __next__() method of the iteratorObj will get one value at a time from it 
            print(next(iteratorObjs))      #!note that next() function calls the __next__() magicMeathod of the iter-Class behind the scenes  
                # note that :- each time we run __next__() Or next()
                # these methods will get one next value and not the previous value from the iteratorObj
                    # !so, these method know the last value returned, and will return the next value on each execution of these methods
            print(iteratorObjs.__next__()) --> 1
            print(next(iteratorObjs))      --> 2
            print(iteratorObjs.__next__()) --> 3

        #TOPICSUMMARY 
            # even for a 'for loop', what makes it work is a 'Iterator', internally for loop calls the __next__() Meathod
            # iter() function -- takes in iterable and converts them into iteratorObjs
            # using __next__() magicMeathod of iteratorObj, we can get one value at a time from iteratorObj
            # next(iteratorObj) also does the same, it calls the __next__() magicMeathod behind the scenes
            # on each execution of these methods, they will get one next value and not the previous value from the iteratorObj
                # so, these methods know the last value returned, and will return the next value from the iteratorObj on each execution of these methods
        #!TOPICSUMMARY
     #!T
     
    #T Creating our own iteratorObjs :- 
        # the momement we say we need to create our own object, we need our own class 
        # lets create a class that prints top 10 numbers 
            
            class TopTen:
                def __init__(self):
                    self.CounterVar = 1     # we want to start the counting from 1, and this is our Counter Variable 
                
                """ as we want to create our own iterator class.
                    our class needs to have 2 important magicMeathods 
                        --> __iter__() & __next(__) (Or __iter()__)
                        
                    __iter()__ : will generate iteratorObj
                    __next()__ : will give the next value of the iteratorObj """ 
                
                def __iter__(self):
                    return self     # this method will simply return the iteratorObj
                
                def __next__(self): # usually this magicMeathod will return the next value of the iteratorObj
                    """ but here, as we want to print TopTen values, 
                        this method will increment the CounterVar attribute and prints that value, 
                        InOtherWords it'll print the next value from the iteratorObj """
                    while selt.CounterVar <= 10:
                        Val = self.CounterVar   # as this magicMeathod should print the first value (1), hence this line
                        self.CounterVar += 1    # after printing the value, CounterVar will be incremented 
                        return val              # hence this magicMeathod Meathod will return val and increment CounterVar

                        if selt.CounterVar > 10:
                            break
                    
                    """ even if we use while + if break, a for loop will not break and (as forloop calls __iter__() magicMeathod internally)
                        continously prints None after printing 1 to 10, hence there is no way to break the loop
                        So to break a forloop, we've to raise an exception 
                        for loop handles the exception internally and will not output the exception on the screen""" 
                    
                    if selt.CounterVar <= 10:
                        Val = self.CounterVar   
                        self.CounterVar += 1     
                        return val    
                    else :          
                        raise ValuesReached     # this will stop the below for loop 

                

            iteratorObj = TopTen()              # this is the object of our class  
            iteratorObj.__next__() → 1          # prints one value at a time             
            TopTen.__next__(iteratorObj) → 2    
            next(iteratorObj) → 3

                    # below we're using a forloop to iterate over the iteratorObj
                    # this forloop will call the __next__() magicMeathod of our class, as its iterating over our object behindTheScenes on each iteration (we've discussed this in the previous section)
                    # break statement in the __next__() Meathod will not stop this for loop, only way to stop this is to raise an exception
                    # forloop handles this exception internally and prints only 1 to 10 and stops 
            for i in iteratorObj:
                print(i)


        # So, this is how we create our own iterator class, 
        # our class should contain 2 magicMeathod --> 
            # __iter__()   --> gives the object of iterator 
            # __next__() --> gives the next object from the iteratorObj
            

        # in the below code 
            # next() function will fetch the 1st value from the iteratorObj --> 1
            # after that, as we know a forloop will call the __next__() Meathod, hence the for loop will print from 2 to 10 
                # because in each iteration it'll call __next__(), as we already retrived 1, it continues from 2

        teratorObj = TopTen()
        
        next(iteratorObj)  --> 1
        for i in iteratorObj:
            print(1)
        2
        .
        .
        10

        #TOPICSUMMARY 
            # if we're creating a iterator class,our class should contain 2 magicMeathods --> 
                # __iter__()   --> returns the object of iterator 
                # __next__()   --> returns the next object from the iteratorObj

            # Once the class has been defined and object is created 
            # we can use __next__() magicMeathod to get one next value at a time from that object
                # Or we can use next() function --> which behindTheScenes calls the __next__() magicMeathod
                # Or we can use a for loop --> which also internally calls __next__() magicMeathod through each iteration 

            # Things to note when iterating over our custum iteratorObj using a forloop 
                # forloop will call the __next__() magicMeathod of our class 
                # in the __next__() magicMeathod, even  if we use break keyword, or while loop with condition to break the loop 
                    # the forloop will not be broken and continues to print none , after execution of the __next__() magicMeathod 
                # to break this external for loop we've to raise an exception inside the __next__() magicMeathod
                # for loop can handle this exception internally and will stop when __next__() raises then exception, and will not print the exception(handles it) and will print only the output 
            
            obj = ourclassName()
            next(obj)  # this will call the __next__() magicMeathod and will retrive one value from obj
            
            for i in obj:  # as for loop will also call the __next__() magicMeathod
                print(i)      # it'll start with retriving the next value (2nd value) after the value above from our obj


            # so a for loop can iterate over any iterable --> list,tuple,set 
            # So, a forloop will call the __next__() magicMeathod of these datatypes
            # and hence these datatypes will have __iter__() & __next__() Meathods defined in the class to make them iterable


            # go through topic if any confution 

        #!TOPICSUMMARY 
    #!T 
#!VID 

#VID 62.Generators 
    
    # Generators & iterators fetch one value at a time 
    # the difference is --> Adds
        # if we want to use our own iteratorObj, then we've to define 2 magicMeathods --> __next__() & __iter__()
            # or else we've to use the inbuilt function called iter() to convert our object to a iteratorObj
        # also iterators uses 'return' keyword in the __iter__() magicMeathod, which means 
            # return keyword terminates the code 
            # it'll store the results untill then in the memory, and then return the results all at once and terminates the code  
        
        # generates uses Yeild keyword which gives a generatorObj which is also iterable
        # Yeild will not terminate the code, it'll return the value in each iteration 
        # hence only one value at a time is stored in memory, hence generators are used whenever we work with large datasets, for memory efficiency 
    # Dads :-
        # if we use iterators, as all the results are stored in memory we can get the total results, or calculate aggrigations on it 
        # but with generates as one value is stored in memory at a time, at the end of the code, we cannot fetch the previous results  
    

    # eg1 :- lets define a function, the uses generators to return top 1-10 values (we've also done same in above vid using iterators)
            # if a function contians Yeild keyword, it'll be a generator function, because Yeild gives generatorObj
            
            def TopTen():   # its a function, not Meathod, hence no 'self' input paremeter
                yield 5     # return will simply return the value 5, but Yeild will give a generatorObj

            print(TopTen()) → <generator object TopTen at 05x65465a>
            print(TopTen.__next__()) → 5   # similar to iterator, we've to use __next__() magicMeathod to get next one value 

            
            # since Yeild will not terminate the function, we can write multiple Yeild statements in the function
            def TopTen():
                yield 1     # it its return 1 ,code will return 1 and terminates here 
                yield 2
                yield 3
                yield 4
 
            TopTen().__next__() → 1
            TopTen().__next__() → 2 

            # so we dont have to use datatypes that has __iter__() & __next__() magicMeathod or define our own iterator class that has these 2 magicMeathods 
            # we can use Yeild keyword to get generatorObjs which are similar to iterators 

            # again, same as in iterators, a for loop will call the __next__() magicMeathod of generatorObjs 
            for i in TopTen():
                print(i)

    #eg2 :- Lets say we want to create a function that returns top 10 perfect squares 

            def perfSqr():
                 n = 1
                 while n<= 10:      # Naveen said he dosent want to use a forloop, because forloop usses iterators 
                    sq = n * n 
                    yield sq        # note that Yeild is part of while loop, because it'll not terminate the function
                                        # if we want to use return, it should be outside the while loop, because it will terminate the function
                    n += 1
                
            # as yeild is in while loop,everytime the while loop runs yeild, one value will be stored in memory and returned 
                # next time that value will be removed and other value will be stored 
            # if return is used, it has to be out of the while loop as it terminates the loop 
                # hence at the end of the loop, return keyword will store all the values in memory at once 

            # hence, thats the reason, generatorObjs are memory efficient 


        #VIDSUMMARY 

            # we'll use iter() function to convert objects to iteratorObjects
            # to create our own iteratorObjects, we need to create our own iterator class  
                # and that has has to have 2 MagicMeathods -> __iter__() & __next()__ 
            # in the __next__() MagicMeathod we've to use 'return' keyword 
            # return keyword will terminate the code and return the value at that point 
            # hence return keyword will be defined outside and at the end of the loop 

            # To work with GeneratorObjs, we dont have to convert other objects, or define our own Generator class with 2 MagicMeathods  
                # we just have to define 'yeild' keyword in our code
            # yeild keyword in a function, makes the function a generator function
            # because 'yeild' keyword returns a GeneratorObj
            # yeild keyword will not terminate the code, hence its defined used inside the loop 

            # on iterating through iterators or Generators using a forloop, it will call __next__() MagicMeathod of respective class, which returns one next value from the iterator or generator object
            # But as __next__() MagicMeathod of iterator uses return keyword, which is defined at the end of the loop, it'll store all the results in each iteration in the memory and return them all at once 
            # but yeild keyword will store one value generated in each iteration in the memory and return them 
                # in the next iteration previous value is removed from the memory and new value will be stored and returned 
            # hence GeneratorObjs are more memory efficient and suitable for large datasets 

            # but with iterators we can access the whole resultset 
            # with generators we cannot access them, as one value at a time is stored and returned 

        #!VIDSUMMARY 
    #!VID 

#VID 63. exception Handling 

    # There are 3 Types of errors 
        # CompileTime Errors → Syntax Errors 
                # CompileTime -> while writing\compiling
                # The red sqiglys on the editor, while writing the code due to Syntax errors 
                # these errors are easyest to find
        # Logical Errors → wrong output due to wrong Logic 
                # when 1+2 is done --> if the output is 2 and not 3, then its a Logical error
                # Logical Errors will return the output, but the wrong output
                    # the code gets compiled and return output but wrong output
                # these errors are found while testing the application, hence Logical errors comes under BUGS   
        # RunTime Errors → wrong user input
                # no CompileTime & Logical Errors in the code
                # but if there are errors because of 
                    # wrong user input
                    # file cannot be found Or cannot connect to database
                        # these are RunTime errors
                # RunTime Errors --> errors while running the code (RunTime)
                        

        # apart from all these errors -->  RunTime Errors are Terminating errors (CompileTime error are also Terminating error, but they are easy to findout) 
        # inorder to continue execution eventhough there is an RunTime Error, we've to use --> Try Except Finally blocks (Try Catch blocks)

    # we can divide our code into normal statements & critical statements 
        a = 5   # normal statement
        b = 6   # normal statement
        print(a/b)

    # Normal statements will not give us errors (there'll be no error in a = 5)
    # critical statements are the statements that will raise errors 

    #T Try-Except-Finally block :- 
        try:
            """ a critical statement """
        except Exception as E: 
            """ commands to execute if any exception in try block """
        finally:
            """ executes irrespective of above code """
        # any exceptions under the try block are handled under 'except' block
        # If there is no exception in the try block, except block will be skipped  
        # syntax of except statement :-
            # except <ExceptionName> as <variable to hold exception message,'Optional'>:
                # <ExceptionName> :- we've to give the name of the exception to handle 
                    # if keyword 'Exception' is given, all exceptions are handled 
                # as <ErrorVariable> is Optional, the exception message will be stored in this variable, and can be printed in the except block ==> print(e) (its like -ErrorVariable parameter in PowerShell)
        # Finally block :-
            # Finally block will be executed anyway at the end, irrespective of the exceptions in try block 
            # we can use this block to close the opened files Or database connections at the end, irrespective of the code in try & except blocks 
    #!T 

    #T Things to note when using Try-Catch Blocks 
        # If there is an exception at a line in the try block , rest of the code below that line, in the try block will be skipped and compiler will jump to Except block 
        # only the exceptionName that is given to the except block will be handled by it, in try block
            # if there is another exception in the try block, then it'll not be handled by except block and the exception will be raised
        # So, for each exception we can define one except block
            # InOtherWords, we can only have one 'try' & 'finally' block, but as many 'except' blocks as we want 
                # so for different exceptions we've to use different except blocks
                # Exception keyword to except block will handle all the exceptions  => except Exception:
        
        # Note that, below, 3rd except block with 'Exception keyword' will handle all the exceptions, except the exceptions that are defined in previous 2 except blocks 
            a = 5
            b = 0
            try:
                print('resource open')
                print(a/b)                          # will raise ZeroDivisionError
                k = int(input('enter any value:')) # will raise ValueError
            except ZeroDivisionError as x:         # executes when ZeroDivisionError in try block
                print(x)
            except ValueError as y:                 # executes when ValueError in try block
                print(y)
            except Exception as z:                  # if there is any other error, other than above, this will execute
                print(z)
            finally:                                # this will execute allways & anyways 
                print('resource closed')
        

        # this concept is same in all OPPS progamming languages
    
    #!T 
#!VID 

#VID 64.MultiThreading
    # One task is broken down into multiple processess
        # and those processess are broken down into threads, and threads are further broken down into handles
            # Tasks → processess → threads 
    # hence we can call the thread as a 'LightWeightProcess' 
    # A handle is a generic OS term that can be a ticket to an operating system object. Each handle is unique and identifies each object. A thread is an OS object and each one you create, you get back a handle for it.
    
    # In Operating Systems subject we learned that, an OS cannot do multiTasking, its made possible by CPU through TimeSharing 
        # TimeSharing --> every task will get some time, and multiple tasks cannot be run at the same time 
    # But this problem is solved using muti code cpus, which made multiple tasks run at same time 

    # vissum above and continue 



ken down into childThreads and after the childThreads completes the task, they join back to mainThread

    # In older python versions before 2.4, MultiThreading is available with 'thread' module
    # In newer python after 2.4, 'threading' module is available
        # it coveres all the features of before 'thread' module & adds some extra features 

        # Inorder to have MultiThreading feature in our code, we've to import 'threading' module
        # and our class & Meathods has to inherit from 'Thread class' (which is from threading module)
        # we've to override the constructor of 'Thread class', by defining our own constructor in our class, which is the childClass of Thread Class 
            # because, as per scope if the constructor is not in the childClass , interpreter will look into the parent class 
        # we've to also override the run() Meathod of the parent 'thread' class, by defining another run() method in our childClass
            # this Meathod should inculde the code\task that the thread has to implement when started 
        
        # Once our new Thread subclass is defined, we can instantuate it (create an instance\object of it)
            # using the ChildClassThreadObj.start() Meathod, which will call the run() Meathod of our class as per scope (behindTheScenes)
            # using the ChildClassThreadObj.join() Meathod, we'll tell the mainThread to wailt and not to execute other tasks untill the child threads completes their tasks and join the main thread
    
    #eg :- 
        from threading import *  # we've imported all classes from threading module

        class Hello(thread):    # our class must be a subclass of thread class 
            def run(self):      # our subclass has to override the thread class run Meathod
                for i in range(5):
                    print('hello')

        class Hi(thread):       # this is another subclass of thread
            def run(self):
                for i in range(5):
                    print('hi')

                # now we've defined 2 subclasses of thread class, now we've to instantuate them and then call the start() Meathod of parent class
                    # start() Meathod will be inherited by the subclasses and this Meathod will call the run() method behindTheScenes 

        th1 = hello()
        th2 - Hi()

        th1.start()
        th2.start()

                # now in the above code since we didnot introduce a delay, we cannot see the effect of MultiThreading
                # now lets introduce some delay, and during this delay in one class, python thinks of executing another class 
                    # normally things like connecting to a database takes time, so in those casses we dont have to do sleep
        from threading import *   
        import time

        class Hello(thread):     
            def run(self):       
                for i in range(5):
                    print('hello')
                    sleep(1)        # after completion of the task, sleep for 1 sec, during which other taks will be executed

        class Hi(thread):        
            def run(self):
                for i in range(5):
                    print('hi')
                    sleep(1)
        
        th1 = hello()
        th2 - Hi()

        th1.start()
        sleep(0.2)      # this delay is to avoid collitions, which is both tasks executing at same time 
        th2.start()

                # now at the end we've to join the individual threads to the mainThread
                # if that is skipped, mainThread many execute other tasks in between  
        
        th1.start()
        sleep(0.2) 
        th2.start()
        #th1.join()     # join() Meathod says to mainThread that, wait for th1 & th2 to join after the completion of their tasks
        #th2.join()     # and dont execute another task during the idle time
        print('Bye')    # so if join() Meathod is not used, python will print bye in the middle of th1 & th2

        # MultiThreading and multiProcessing is different
            # MultiThreading → executing multiple tasks simultaneously 
            # multiProcessing → allocating all the processing power to do one task  

        # The key difference between multiprocessing and multithreading is that 
            # multiprocessing allows a system to have more than two CPUs added to the system whereas 
            # multithreading lets a process generate multiple threads to increase the computing speed of a system

    #VIDSUMMARY 
        # MultiThreading ==> Tasks → processess → threads → handles
            # threads are also called as 'LightWeightProcess' 
            # A handle is a generic OS term that can be a ticket to an operating system object. Each handle is unique and identifies each object. A thread is an OS object and each one you create, you get back a handle for it.

        # MultiThreading  → One process is broken down into multiple threads
        # MultiProcessing → allocating extra cores to complete the task 

        # normally python executes the code sequentially 
        # in multiTasking, mainThread is broken down into childThreads (using start() method)
            # and after the childThreads completes the task, they join back to mainThread (using join() method)

        # before python 2.4 → 'thread module'
        # after python 2.4 → 'threading module' -> with some extra features 

        # Inorder to have MultiThreading feature in our code
            # from threading import *  --> we've imported all classes from threading module
            # class Hello(thread):  --> our class must be a subclass of thread class (which is from threading module)
            # we've to override the constructor & run() method of the thread class, by defining our own in our subclass
                # the code in the run() method will be executed by the thread, when its started 

            # ChildClassThreadObj = subClass()  ->  Once our new Thread subclass is defined, we can instantuate it 
            # start() => using the “ChildClassThreadObj.start()” Meathod, which will call the run() Meathod of our class as per scope (behindTheScenes)
            # join()  => using the “ChildClassThreadObj.join()” Meathod, we'll tell the mainThread to wailt and not to execute other tasks untill the child threads completes their tasks and join back the main thread

            # if there is any collition in the execution of 2 subclasses, then try introducing delay in the respective classes run Meathod 
                # So, during this delay, mainThread will think of executing other tasks 
    #!VIDSUMMARY 
#!VID 


#VID 65.FileHandling using Open()
    # we'll see how we can deal with files in python using - Open() inbuild function
    # for logging we can either use a relational database like → MySQL,Oracle (structured database)
        # Or we can either use a text file 
    
    # syntax :-
        open('fileName',Mode)
            Mode => r,w,a
    
    # Eg :-
        f = open(file,'r')  # so 'f' will be the reference to the openObj
        
        print(f)    # prints all the info about the openObj
            <_io.TextIOWrapper name='Mydata' mode='r' encoding='cp1252'>
        
        #T Meathods of open() to 'read' data :- 
            f.read()        # to get the content inside the file 
            f.readline()    # prints the first line from the file 
            f.readline()    # this time readline() will print the 2nd line, as this function will have a pointer that increamets and prints the next line each time
                                # this is similar to the next() meathod of generatorObj 
            f.readline(limit=5) # this will print 5 characters from the first line of the file  
        #!T
        
        #T Meathods of open() to 'write' data :-
            # inorder to write to the file - we've to open the file in 'write mode'
            # Note that, if the file dosent exists - it'll create a new file 
                # if the file exists - then it'll open that file 

            # also note that, In write mode,inputed data will be overwritten to the file 
            # inorder to append the data we provide we've to open the file in 'append' mode   

            f = open(file,'w')
            f.write('something')
            f.write('laptop')   # laptop will be overwritten to the file 
        #!T 

        #T Meathods of open() to 'append' data
            # inorder to append the data, we've to open the file in append mode and use the write() meathod to append the data 

            f = open(file,a)
            f.write('something')
            f.write('laptop')   # laptop will be appended to the file 
        #!T
 
        #T we can iterate over a openObj using a forloop
            # we can also use a forloop to read each line in each interation from a file 
            f = open('file','r')
            for data in f:
                print(data)     # in each interation, one line from the file will be stored in 'data' and then printed

            # using the same forloop,in each interation we can read & write the data from one file to another 
            f   = open('file','r')  # we'll read the data from this file, hence opened in a read mode  
            f2  = open('file2','w') # we'll write the data into this file, hence opened in write mode 

            for data in f:      # in each iteration one line will be stored inside 'data'
                f2.write(data)  # that stored line will be written into the f2 file 
        #!T 

        #T Working with IMG files using open() function
            # there are 2 versions for each mode in open() function
                # one is character version → used to read & write data from & to a text file » we've to use  'r','w','a'  for 2nd parameter 'mode'
                # another is binary version → used to read & write data from files like images » we've to use 'rb','wb' (read binary & write binary)

            IMG1 = open('ImgFile1','rb')    # mode 'rb' → read binary 
            for data in rb:     # hence this loop will print all the binary data from the image file 
                print(data) 

            # lets copy data from one image file into another image file, just like we did with files above 

            IMG1 = open('ImgFile1','rb')    # we've to use binary versions of modes
            IMG2 = open('Imgfile2','wb')    # if the file is not there,it'll be created

            for data in IMG1:
                IMG2.write(data)
        #!T

    #VIDSUMMARY 
        #•Open() is an inbuild function, used to deal with files 
        syntax :- 
            open('fileName',Mode)
                # Mode → we've 2 versions of modes » Character & Binary 
                # Character modes → 
                    # r = read ; w = write ; a = append » write mode will override the data, whereas append will append the data we provide 
                # Binary modes →
                    # rb = readBinary ; wb = writeBinary

        #•read meathods 
            f.read()            # to get the content inside the file 
            f.readline()        # prints the first line from the file 
            f.readline()        # this time readline() will print the 2nd line, as this function will have a pointer that increamets and prints the next line each time
                                # this is similar to the next() meathod of generatorObj 
            f.readline(limit=5) # this will print 5 characters from the first line of the file      
        
        #•write meathods
            # Open the file in write mode, if the file dosent exists it'll be created
            # write mode will override the data in the file, to append data open the file in append mode 
            f = open(file,'w')
            f.write('something')
            f.write('laptop')   # laptop will be overwritten to the file 
        
        #•append meathods 
            # open the file in append mode and then use the write meathod to append the data 
            # if the file is opened in write mode and the write meathod is used, write() will override the data  
            f = open(file,a)
            f.write('something')
            f.write('laptop')   # laptop will be appended to the file 

        #•read & write using forloop 
            # we can also use a forloop to read each line in each interation from a file and then write it to another file  
            f   = open('file','r')  # we'll read the data from this file, hence opened in a read mode  
            f2  = open('file2','w') # we'll write the data into this file, hence opened in write mode 

            for data in f:          # in each iteration one line from 'f' will be stored inside 'data'
                f2.write(data)      # that stored line will be written into the f2 file 

        #•Binary version modes are usefull to work with files like images 
            IMG1 = open('ImgFile1','rb')    # mode 'rb' → read binary 
            for data in rb:                 # hence this loop will print all the binary data from the image file 
                print(data) 

            # lets copy data from one image file into another image file, just like we did with files above 

            IMG1 = open('ImgFile1','rb')    # we've to use binary versions of modes
            IMG2 = open('Imgfile2','wb')    # if the file is not there,it'll be created

            for data in IMG1:
                IMG2.write(data)
    #!VIDSUMMARY 
#!VID 

#VID 67.Python is Compiled & intrepreted lang
    # python is both Compiled & intrepreted language 

    #T Compiled language
        # Eg C, C++
        # languages that uses compiler to convert its highLevelLanguage code into binary are called Compiled languages 
         
        
        # Compiler :-
            # compiler is a software that converts code from one language to another language
                # that can be from (high <-> high) Or (high <-> low )
    #!T 

    #T intrepreted language    
        # intrepreter is a software that reads\intreprets and executes our code lineByLine 
        # PVM → Python virtual macine (python intrepreter), can only run python code
        # JVM → Java virtual macine (Java intrepreter), can run other languages like » Scala,Groovy,scotlang

        # we use intrepreter to achive platform independence
        # As different cpus have different architechtures, a ByteCode for one cpu many not work for another cpu 
        # So the intrepreter virtual Machines like → PVM & JVM can read\covert & executes that ByteCode on different cpus 

        # these PVM & JVM are also used to tune the performance of software
    #!T 

    #T Python → Compiled + intrepreted
        | file.py |         Compiled         |            ByteCode            |        Intrepreted        | MachineLanguage |
        | +-----+ | +----------------------+ | +----------------------------+ | +-----------------------+ | +-------------+ |
        | py_file | Converted to Binary code | that binary code will be       | intrepreter will executes |                 |
        |         | By the compiler          | Intrepreted by the intrepreter | that binary code          |                 |

        # file.py → Compiled by compiler → converted to binary code (ByteCode) → intrepreted by intrepreter (PVM) → Converted according to the cpu architechture and executed lineByLine

        # Java is also a compiled & intrepreted language
        # hence to run the code in java, we've to do that in 2 steps (compile + intrepret)
            # in java first we've compile the code using → javac => JavaC javaFile.java (compile)
            # then we've to run the file using the java command  => java javaFile       (intrepret)

        # But python will take care of compilation behindTheScenes, hence we only have to run the code => python py_file.py  (only have to intrepret)
        # even the commands that we run on shell, will be compiled by python first and them run on PVM 
    #!T 

    #T Types of python
        # python is a language → set of rules & conventions
        # its implemented(internal code is written) in different other languages 
            Cpython    → # written in C,widely used (this vid covers this)
            PyPy 
            IRONPython → # written in .net (microsofts)
            Jython     → # written in Java
    #!T 

    #VIDSUMMARY 
        # •python is both Compiled & intrepreted language 
        # •Compiled language
            # uses compiler to convert code to binary
            # Eg C, C++
        
            # ·Compiler :-
                # compiler is a software that converts code from one language to another language → that can be from (high <-> high) Or (high <-> low )

        # •intrepreted language
            # intrepreter is a software that reads\intreprets and executes our code lineByLine
                # As different cpus have different architechtures, a ByteCode for one cpu many not work for another cpu, an intrepreter will take care of that 
            
            # PVM → Python virtual macine (python intrepreter), can only run python code
            # JVM → Java virtual macine (Java intrepreter), can run other languages like » Scala,Groovy,scotlang
            # these PVM & JVM are also used to tune the performance of software

        # •Python → Compiled + intrepreted
            # file.py → Compiled by compiler 
            # converted to binary code (ByteCode)
            # intrepreted by intrepreter (PVM)
                # Converted according to the cpu architechture and executed lineByLine
            
            #·Java is also a compiled & intrepreted language
            # hence to run the code in java, we've to do that in 2 steps (compile + intrepret)
                # in java first we've compile the code using → javac => JavaC javaFile.java (compile)
                # then we've to run the file using the java command  => java javaFile       (intrepret)

            # But python will take care of compilation behindTheScenes, hence we only have to run the code => python py_file.py  (only have to intrepret)

        # •Types of python
            # python is a language → set of rules & conventions
            # its implemented(internal code is written) in different other languages 
                Cpython    → # written in C,widely used (this vid covers this)
                PyPy 
                IRONPython → # written in .net (microsofts)
                Jython     → # written in Java
    #!VIDSUMMARY 
#!VID 


#VID 68.Linear Search
    # Lets Search an element from the list using Linear Search
        #IMP Linear Search Searchs linearly, one element after another

    #IMP note that these Searchs are implementations (algorithms), and will be implemented using normal code and without using functions 
        # we also have functions like listObj.index() to seach the list elements 

    #IMP we've to iterate over the list using any loop and compare the elements with our search element using indexing 

    #T implementing Linear Search using a WhileLoop :-
        # lets define a function that seachs the element from the list using linear seach

        list = [1,2,3,4,5,6,7,8,9]
        index = -1                          # to return the index value of the element if found, as index starts with zero, we're starting this variable at -1


        def Search(list,No_to_search): 
            i = 0                           # while loop incrementer 

            while i < len(list):            # len(list) = 9, thats the reason we've used lessthan and not the lessthan Or equalto
                if list[i] == No_to_search: # comparing each element with our seach number using index      
                    return True
                globals()[index] = i        # here we're tracking the index, as index is a global variable, we've used the globals function to change the value of the global variable, as globals() return all the global variables, we've to access the global variable using square brackets ==>[]
                i += 1                      
            
            return false                    # Once the which loop completes, which means we didnot find the number, then the function will return false



            # we cannot return false in the while loop itself, in the If_Else because we've to loop through the entire list and then return false if the number is not found
                # hence we return false outside the while loop 
            
            # we can either use @global decorator to import the global variable into the function, or we can use globals()['varName] to access or change the value of the globalVariable 
            # globalVariable concept is covered in previous vids  
            # 'i' value starts from zero, which is equalent to the index number, hence we're storing the value of 'i' in each interation to the index globalVariable, to track the index 
                # we can define index inside the function and outside the WhileLoop to skip the globalVariable concept
            

        # So, this is linear Search, we can also use binary Search, its faster than any other seach
        # linearSearch = Searchs each and every element from the start 
    #!T 

    #T implementing Linear Search using a forloop :-

        list = [1,2,3,4,5,6,7,8,9]

        def Search(list,No_to_search):
            index = 0

            for i in len(list):
                index = i
                if list[i] == No_to_search
                    return True,index   # as we know the return statements terminates the code, if the number is found, forloop returns True and terminates the code here     
            
            return False                # if the forloop is completed, which means the number is not found, hence the function returns false
    #!T 
#!VID 

#VID 69.Binary Search
    # So, a linearSearch will Search for every element, hence its not ideal to use when the dataset is huge 
    
    #T How binarySearch works:-
        # all the elements has to be sorted 
            # linearSearch donest require values to be sorted 
        # after the values are sorted, we'll have → lowerBound(index0),UpperBound(last element)
        # then the middle value is called midIndex → LB+UB/2  (we've to do integer division '//')
        # now check the result using below conditions 
            # if midIndex = our value  » we got the result 
            # if midIndex != our value 
                # midIndex > our value » our value will be in between LB & midIndex-1 (as the values are sorted) → hence midIndex will be changed to UB and search will be performed again as above
                # midIndex < our value » our value will be in between UB & midIndex+1 (as the values are sorted) → hence midIndex will be changed to LB and seach will be performed again as above

        # in this way, on each search operation, python has to only search one value in a small set of data which is between LB & UB

        Eg :-
            # we're searching for 8
        # values has to be sorted  [1,2,3,4,5,6,7,8,9]
        # 1 - LB, 9 - UB 
        # 1+9/2 = 5  (at index 5, 6 = midIndex)
            # as 8 > 6, 8 will be between midIndex & UB 
        # now new LB = 6 & UB = 9 
        # 6+9/2 = 7  (int division) (at index 7 values is 8, what we're searching for)
    #!T 

    #T implementing binarySearch using WhileLoop

        def Search(list,No_to_search):

            LB = 0                  # initial LB will be allways at index zero 
            UP = len(list)-1        # initial UB will be the last index value, len() gives the total elements, but as the index start at zero, we've to do len(list)-1

            """ at 2 sinarios we've to stop the loop
                If LB grater than or equalto UP (this will be the while loop condition) [if the number we need to search is last element, then only at UP=LB results can be found]
                If the value we're looking for is found (will be inside the loop) """
            
            while LB < UP:
                # In this loop, in each iteration
                    # New LB Or UB values has to be calculated depending on relation between our value and midIndex
                    # midIndex has to be calculated
                
                midIndex = (LB+UP)//2   #(// = integerDivision, / = normalDivision)
                if list[midIndex] == No_to_search:
                    return True         # we've to retminate the loop here, hence we can also use 'Break' statement here 
                elif list[midIndex] > No_to_search: # UB has to be changed
                    UB = midIndex -1
                elif list[midIndex] < No_to_search: # LB has to be changed
                    LB = midIndex +1

            return False                # if the loop is completed, which means that the value is not found, hence we'll return false
    
        
        # Notice that in the above whileLoop, we dont need to have any incrementer, because the condition dosent depend on 'i', it depends on LB < UP 
    
    #!T 
    
    #VIDSUMMARY 
        # linearSearch → every element will be searched linearly → not ideal for huge data sets 
        # data dosent need to be sorted 

        # Binary search 
            # sort values 
            # calculate starting LB(index0), UB(len(list)-1), MidValue (LB+UB//2)  ((// = integerDivision, / = normalDivision))
                #  LB ------ MidValue -------- UB
                # so the values has to be either in 
                    # LB ------ MidValue    (left half)
                    # MidValue -------- UB  (right half)
                    # or == MidValue        (middle)  
            
            # if value > MidValue » value will be in right half (MidValue -------- UB)
                # hence MidValue+1 == LB    (+1 to eleminate the MidValue)
                # UB remains the same and repeat the above process 
            # if value < MidValue » value will be in left half  (LB ------ MidValue)
                # hence MidValue-1 == UP    (-1 to eleminate the MidValue)
                # LB remains the same and repeat the above process
            
            # untill the value is found 

        # things to remember while implementing the BinarySearch using whileLoop
            # initial LB will be allways at index zero
            # initial UB will be the last index value, len() gives the total elements, but as the index start at zero, we've to do len(list)-1
            # at 2 sinarios we've to stop the loop
                # If LB grater than or equalto UP (this will be the while loop condition) [if the number we need to search is the last element, then only at UB=LB results can be found]
                # when the value we're looking for is found (will be inside the loop)
            # In this loop, in each iteration
                # New LB Or UB values has to be calculated depending on whether LB is >Or< MidValue
                # and the midIndex has to be calculated for every new LB & UB and has to compared with value we want to search

        # look at the "implementing binarySearch using WhileLoop" section in the vid 
    #!VIDSUMMARY 
#!VID 


#VID 70.Bubble Sort → compare & swap (multiple swappings)
    # we'll sort a list using Bubble sort, its the easyest sorting technique available
    # ‘swapping elements’ is the common technique in almost all the sorting algorithms 
        # swapping => 
            # remember the swapping of variables, which can be done using “3rd variable” Or by using a “tuple unpacking” 
                # using 3rd variable
                    t = a       # baking up var 'a' value in 3rd variable
                    a = b 
                    b = t 
                # using tuple unpacking
                    a,b = b,a   # LHS is a tuple, which is unpacked into variables a&b 

    #T How Bubble sort works :- 
        # This sorting algorithm is comparison-based algorithm 
        # each pair of adjacent elements are taken and compared and the elements are swapped if left side element is > right side element, to make sure that smallest element comes first
        # this continues untill all the elements are sorted 
        # so in each interation the highest element in that iteration will be moved to the extreeme right side of the list 
            # so in each iteration each highest element will be sorted from right to left

        #Eg :-
            # Take 2 adjacent index elements 
            # the smallest should come first ,or largest should come second, if so skip, else swap
            
            list = [5,3,8,6,7,2]
                # iteration1
                [5,3,8,6,7,2]  → # 5&3 are taken 5>3;   swap  » [3,5,8,6,7,2]
                [3,5,8,6,7,2]  → # 5&8 are taken 5<8; noswap  » [3,5,8,6,7,2]
                [3,5,8,6,7,2]  → # 8&6 are taken 8>6;   swap  » [3,5,6,8,7,2]
                [3,5,6,8,7,2]  → # 8&7 are taken 8>7;   swap  » [3,5,6,7,8,2]
                [3,5,6,7,8,2]  → # 8&2 are taken 8>2;   swap  » [3,5,6,7,2,8]
                    
                    [3,5,6,7,2,8] → # So this is the result of first iteration
                    # So, after the first iteration, the highest value in the list which is '8' is at the extreeme right of the list 
                    # but as the remaining elements are not sorted,we've to reiterate again and in each iteration each highest value will be moved to the extreeme right of the list 
                    # Hence the Bubble sort is all about comparing & sorting\swapping

                # iteration2
                [3,5,6,7,2,8]  → # 3&5 are taken 3<5; noswap » [3,5,6,7,2,8]
                [3,5,6,7,2,8]  → # 5&6 are taken 5<6; noswap » [3,5,6,7,2,8]
                [3,5,6,7,2,8]  → # 6&7 are taken 6<7; noswap » [3,5,6,7,2,8]
                [3,5,6,7,2,8]  → # 7&2 are taken 7>2;   swap » [3,5,6,2,7,8]
                [3,5,6,2,7,8]  → # 7&8 are taken 7<8; noswap » [3,5,6,2,7,8]    #! In the 2nd iteration we'll not check for this last steps, because the maximum value in the list is already moved to extreeme right in the first iteration

                    # Now after the 2nd iteration, 2nd element from the right is the 2nd largest value in the list 
                    # So, after the 1st & 2nd iteration, we've 2 largest values sorted in assending order at extreeme right 

                # so, after (number of elements in the list) - 1 iterations we'll have all the values sorted 
                    # after 7-1 = 6 iterations all the elements will be sorted 
                    # minus one because :- each iteration will run only for => (len(list) - (i-1))
                        # eg - 3rd iteration will only run for 4, because last 2 elements are already sorted in first 2 iterations
                        # similarly 5th iteration run for (5-(5-1) = 1) only one time, because last 4 elements will be sorted in previous iterations 
                        # and no need to do next iteration because if rest of the elements are sorted, then the first element is also sorted 
                
                # so, to achive Bubble sort we need 2 loops 
                    # InnerLoop to move the highest element to the extreeme right
                    # outerLoop to repeat the InnerLoop 
    #!T 
    
    #T Implementing Bubble sort
        list = [5,3,8,6,7,2]
            # we've inbuild sorting instanceMeathods for list DataStructur, but we'll implement the bubble sort here without predefined inbuild meathods

        def BubbleSort(List_to_sort):
            for i in range(len(List_to_sort)-1,0,-1):   # we need to do len(list)-1, because last element will be automatically sorted at the end 
                """also this is the outer loop & we're using range to print the reverse numbers, 
                    thats the reason we've used 3rd input parameter 'step' of range => -1 
                    range(start,stop,step) → so the above range will print from len(list)-1 to 1 """
            for j in range(i):  # this is inner loop, in each iteration largest value will be sorted in the extreem right of the list  
                """ each iteration has to go till 'i',that is 
                    In first iteration, first largest value will be sorted at the end, and inner loop has to go through all the elements of the list 
                    In the second iteration, second largest value will be sorted at the end, and the inner loop has to go through only through len(list)-1, because last element is already sorted in the first iteration
                    So, range() for this inner loop will be 'i' of outer loop """
                    if List_to_sort(j)>List_to_sort(j+1):   # comparing the elements 
                        temp = List_to_sort(j+1)            # swapping using 3rd variable
                        List_to_sort(j+1) = List_to_sort(j) # largest has to be on the left Or smallest should come first
                        List_to_sort(j) = temp
    #!T 
    
    #VIDSUMMARY

        #• Bubble sort is the  --> easyest sorting technique
        #• “swapping values” is the common logic behind most of the sorting techniques
            # we've learned how to swap variables, using 3rd variable Or by using tuple unpacking

        #• How Bubble sort works :-
            # it consists of 2 nested loops
                # Outerloop will track how many elements left to be sorted
                # InnerLoop will move the highest element in each iteration to the right by comparing adjecent elements and swapping the values

                # Outerloop will repeate the InnerLoop
                # InnerLoop will make sure that smallest element comes first Or highest element is on right in each comparition of adjecent elements, if not it'll swap the values
                    # this way each highest value will be moved to extreeme right of the list in each InnerLoop iteration

                # So, Bubble sort will sort from left-to-right or vieceversa depending on the logic, but by comparing & swapping values

            #• Things to remember while implementing the logic
                # In each iteration, highest value will be moved to righ, hence one element will be sorted in each InnerLoop iteration
                # hence each InnerLoop iteration has to go through only => (len(list) - (i-1)) » 'i' is the iteration number
                    # first iteration → 5-(1-1) = 5 (has to go through all the elements), 5th element will be sorted
                    # 2nd iteration   → 5-(2-1) = 4 (has to go through 5 elements), as 5th element is already sorted in first iteration

                # In this way, last element dosent have to be sorted because,rest of the elements will be already sorted in previous iterations
                # this will be tracked by Outerloop

        #• implementing Bubble sort :-
            list = [5,3,8,6,7,2]

            def BubbleSort(list):
                for i in range(len(list)-1,0,-1):    # len(list)-1 to skip the last element, step = -1 to count reverse
                    for j in range(i):               # InnerLoop has to skip last element, hence need to iterate only thorugh range(i)
                        if list(j)>list(j+1):        # highest value should be on right Or smallest value should come first, if not swap  
                            temp      = list(j)
                            list(j)   = list(j+1)
                            list(j+1) = temp 

        # DrawBacks :-
            # In each InnerLoop iterations we'll be doing multiple swappings untill the largest number will be moved to extreem righ of the list 
            # So, swapping consumes lot of cpu & memory 
            # In selection sort swapping is only done once, its discussed next 

    #!VIDSUMMARY
#!VID 


#VID Selection Sort → Compared and only swapped once 

    #T draw backs of using Bubble Sort :-
        # In each InnerLoop iterations we'll be doing multiple swappings untill the largest number will be moved to extreem righ of the list
        # So, swapping consumes lot of cpu & memory, its not ideal for large data sets
        # In selection sort swapping is only done once
    #!T

    #T How selection sort works :-
        # it'll also consists of 2 loops
        # Outerloop will repeat the inner loop and also keeps the track of how many elements that need to be sorted
        # InnerLoop will go through the unsorted elements and in each iteration it'll find min or max value based on the logic (here we'll cover min value)
            # so for each InnerLoop iteration
                # we'll find min or max value by comparing (explained in below example)
                # then swap the first element with min value, or last element with max value (if finding max is the logic)
                    # but note that we'll only swap once unlike Bubble sort

        # Eg :-
            [5,3,8,6,7,2]  → # lets say finding minvalue is the logic
                # iteration-1
                    # we'll assume that minvalue is at index 0 => 5
                    # we'll compare 5 with each element
                        # once the minvalue which is smaller than 5 is found, then the new minvalue is update to that value → 5>3 » now minvalue = 3
                    # we'll compare rest of the elements with new minvalue untill other new minvalue is found => 3>2, hence minvalue = 2
                    # as we reached end of the list, the minvalue of this InnerLoop iteration is 2
                    # hence index zero which is 5 will be swapped with 2

                    [2,3,8,6,7,5] => # so [2] will be the sorted array & [3,8,6,7,5] will be the unsorted array

                # iteration-2
                    # unsorted array will be taken → [3,8,6,7,5]
                    # minvalue = 3  » will compare it will rest of the elements
                    # if 3>x, our new minvalue = x, and rest of the values from x are compared with x and minvalue is updated
                    # once we reach to the end of the list, index 2 element 3 will be swaped with minvalue
                    # in this iteration 3 is minvalue than rest of the elements, hence no swapping in this iteration

                    [2,3,8,6,7,5] => # so [2,3] will be the sorted array & [8,6,7,5] will be the unsorted array

                # iteration-3
                    # first element from unsorted array = 8 » minvalue  = 8
                    # 8>6 » minvalue = 6
                    # 6<7 » minvalue = 6
                    # 6>5 » minvalue = 5
                    # first element of unsorted array Or 3rd element in full array will be swapped with 5

                    [2,3,5,6,7,8] => # so [2,3,5] will be the sorted array & [6,7,8] will be the unsorted array

            # as we can see in each InnerLoop iteration, one minvalue is update to extreem left by comparision, just like Bubble sort
            # but swapping is only done once

            # Things to note while implementing the logic :-
                # in each InnerLoop iteration one minvalue will be sorted, hence Outerloop has to make InnerLoop to skip sorted array elements from comparition
    #!T 

    #T Implementing selection sort :- 
        nums = [5,3,8,6,7,2]

        def selectionSort(list):
            for i in range(len(list)-1):        # -1 because last element will be automatically sorted, hence no need iterate for last one element
                    """ here we're trying to sort in assending order, if you want to sort in decending, 
                        then we've to use step parameter of range() becase we need to go from big to small values in reverse """
                MinPos = i  # lets have a variable that holds minvalue position(index), its equal to 'i' because by default on starting of each iteration, we'll take starting index value as minvalue
                for j in range(i,len(list)):    # Inner loop range() has to start from 'i'th element, to till last element of the list, note that elements before 'i' are sorted 
                    if list[j]<list(MinPos):    # we've comparing the every element with element at MinPos, because initially we'll take list(MinPos) as minimum value 
                        MinPos = j              # if the values lesser than list(MinPos) is found, then that index value will be updated to MinPos variable

                temp = list[MinPos]             # after comparing every element with MinPos, then the final value inside the MinPos will be the minvalue, hence we need to swap 
                list[MinPos] = list[i]          # latest MinPos position value is swapped with initial MinPos value ('i') which we thought as a minvalue initially 
                list[i] = temp                  # note that we should not use list[j], because this statement will be executed after completion of innerloop, then list[MinPos] = list[final value of 'j']
    #!T 

    #VIDSUMMARY
        #• drawbacks of bubble sort :- 
            # multiple swappings are done in the innerloop in each iteration, which consumes CPU & Memory
            # hence bubble sort is not ideal for large datasets 

        #• How selection sort works :-
            # first element is taken and stored in temp variable and is compared with rest of the elements, if an element lesser than that is found, it will be updated in a temp variable 
            # Once it reaches the end of the list, the value in the temp variable will be the smallest number in that iteration
            # hence it'll be swapped with the first element
                # in one iteration, we can see that swapping is only done once 
                # in each iteration, smallest or largest element will be moved to sorted part depending on logic by swapping 
                # only one swap per iteration unlike bubble sort

            # it will also consists of 2 loops 
            # OuterLoop :- 
                # repeat the innerloop
                # keep the track of how many elements are not sorted, which innerloop has to go through 
            # innerloop :-
                # iterate through unsorted elements 
                # take first val as minvalue and compare it with rest of unsorted elements and swap the real minvalue at the last in that iteration with the first value 
                # hence for each innerloop iteration, min or max value will be moved to extreeme left or right (sorted part)

            # bubble sort    :- # first element is taken → every time smallest element is found → swap → smallest element comes first 
            # selection sort :- # first element is taken and stored in variable → every time smallest element is found → update the variable → swap at the end of iteration → smallest value will be moved to extreeme left 
            
        #• Things to note while implementing the logic :-
            # in each InnerLoop iteration one minvalue will be sorted, hence Outerloop has to make InnerLoop to skip sorted part of elements from comparition


        #• Implementing selection sort :- 
            nums = [5,3,8,6,7,2]

            def selectionSort(list):
                for i in range(len(list)-1):    # last element need not to be sorted, hence len(list)-1 
                    MinPos = i                  # this holds the minvalue, initial minvalue will be 'i'
                    for j in range(i,len(list)) # range() => from i to end of the list 
                        if list[j]< list[MinPos]:  # if that current value in the iteration is less than MinPos value 
                            MinPos = j          # at the end of each innerloop iteration, minvalue for that iteration will be updated in this variable 

                    temp = list[MinPos]         # at the end of innerloop, we'll swap the minvalue with list[j]
                    list[MinPos] = list[i]      # we can use list[j] instead of list[MinPos] because (MinPos = j)
                    list[i] = temp              # but using list(MinPos) is ideal 
    #!VIDSUMMARY
#!VID


#VID 72.MYSql Workbench Setup
    # we’ll see how to connect to a database using python, 
    # we’ll take RDBMD (relational database management systems), →  postgress,Msql (we’ll take mysql for this vid)

    #T Msql Installation :-
        # Google search “MySql installer” which will install MySql Workbench, Connector etc 
        # On running the MySql installer, we can select “Developer Default” which will install enough features 
        # On the product configuration page, we’ll set the port no &  username/Pass for Root and as well as we’ll create users 
            # by default we’ll only get Root user, we need to add other users 
            # default port no of MySql is 3306, we can also change it 
        # Next we need to apply the configurations
            # this will not work if the port no assigned for the MySql is used by another software 
            # Make sure that the port is not busy 
        # Finally it’ll ask to connect to the server, we can check the connectivity of the Root & other users to the server on this page 
        
        #Now after installation, we can write the MySql code on the Shell Or MySql WorkBench (gui)
        # So, open the MySql workbench and connect to the local instances (as MySql is installed on the local machine)
    #!T 

    #T MySql Sample Commands :-
        Show Databases;             # Prints all the databases
        
        Create Database Telusko; 	# we’ve created a database 
            
            
        Use Telusko;                # Now lets create a table in Telusko database and insert some data 
        Create Table  Student(name varchar(20), Colleage varchar(20));
        Insert into Student Values (‘Naveen’, ‘Vsit’), (‘Priya’, ‘Bvit’);
    #!T 

    # In the next vid we’ll see how we can connect and insert, update data into the MySql databases using python 
#!VID



#VID 73 Connecting to MySql database

    # In the last vid, we've seen → how to install MySql, Workbench & shell, we've created a database,table
    # In this vid we'll see how we can connect to the MySql database using python 

    #T Things required for Connecting to a database → MySql connector
        # we need to have a MySql connector, inorder for any language to connect to MySql
            # so first lets intall the MySql connector using 'pip3'  → pip install MySql connector
    #!T 

    #T  Connecting to the database using python
        # MySql connector will provide a meathod called 'connect()' using which we can connect to a MySql database
            # Syntax of connect() meathod :-  
                connect(host='IpAdd Or LocalHost', UserName='', passwd='', databaseName= 'Optional')
                    # host will be the IpAdd or LocalHost if the MySql is installed on the local machine 
                    # databaseName is Optional, if we're running queries that are not specific to a database

        # Once we've connected to the database using the connect() meathod
        # next we need to have 'cursors' to run the MySql commands against the database
            # cursors are pointers to each row in a table, they are used to process the data on row by row, hence they are very bad in performance → (check part 63 of KudVetkat series prizim tech)
            # we can create cursors using the cursor() meathod, which is an instanceMeathod of connectObj  
            
        # So Once the cursorObj is created we can execute MySql queries on a table using the 'execute()' instanceMeathod of cursorObj
                MySql.connector.connect() → Connect to database
                cursor()  → create cursorObjs 
                execute() → execute MySql queries 

        #•Eg-1 :-
            import MySql.connector      # importing the connector which we've downloaded before 
     
            connectObj = MySql.connector.connect(host="LocalHost", UserName="Naveen", passwd="1234")        # with the use of this meathod, we can connect to the database
            cursorObj = connectObj.cursor()         # creating cursorObjs 
            cursorObj.execute(" show databases  ")  # executing  MySql queries, this query will fetch all tehe databaseNames

                # the results produced by the above MySql query will be stored in the cursorObj itself
                # so these cursorObjs are iterables, hence we can use forloop to feach the data from it 
            for i in cursorObj:
                print(i)        # in each iteration each databaseName will be in a tuple → ('telsuko',)

                # we can also use the fetchall() & fetchone() meathods of the cursorObj
                    # cursorObj.fetchall()   → returns all the records, so we need to again use a forloop to iterate over it 
                    # cursorObj.fetchone()   → returns the first record, so we can print it directly 
                    
            results = cursorObj.fetchall()
            for i in results:
                print(i)

            result = cursorObj.fetchone()
            print(result)

            

        # so in the above case, we're tried to execute a query on the schema and not on a specific database, hence we skipped the argument to the database parameter of the connect() meathod
        # but next time we'll run a query that will fetch all the records from a table, as we're refferring to a table in a database, we need to use the database parameter of the connect() meathod
            # if you're specifying the tableName in the query, then specify the databaseName in the connect() meathod


        #•Eg-2 :-
            import MySql.connector

            connectObj = MySql.connector.connect(host="LocalHost", UserName="Naveen", passwd="1234", database="telsuko")    # we've metioned the databaseName
            cursorObj = connectObj.cursor()
            cursorObj.execute(" select * from  student  ")      # as the student table belongs to telsuko database, we've to mention that above 

            results = cursorObj.fetchall()          # as all the outputs are stored in cursorObj, we're fetching them all and stroing them in a variable 

            for i in results:       # as results contain multiple values, we're using forloop to iterate overit 
                print(i)
                
    #!T

    #VIDSUMMARY

        #• first we need to install MySql Connector pakage using PiP3 → pip install MySql connector
            #Inorder for programming language to communicate with MySql, we need to have connector

        #• then we need to import that pakage 
            import MySql.connector


        #•  Connecting to database :- connect()
            # we can connect to the database using the → connect() meathod 
                # Syntax of connect() meathod :-
                    connect(host='IpAdd Or LocalHost', UserName='', passwd='', databaseName= 'Optional')
                            # host will be the IpAdd or LocalHost ( if the MySql is installed on the local machine )
                            # !databaseName is Optional (if we're running queries that are not specific to a database), if we're running the queries against a table, then we've to specify the databaseName here for sure

                connectObj = MySql.connector.connect(host="LocalHost", UserName="Naveen", passwd="1234")        → # for "show databases"
                connectObj = MySql.connector.connect(host="LocalHost", UserName="Naveen", passwd="1234",database="telsuko")  → # for "select * from student"
                
        #•  Create cursor :- cursor() 
            # once we've connected to the database, we need to create cursors using → cursor()  (an instanceMeathod of connectObj)
            # cursors are pointers to each row in a table, they are used to process the data on row by row, hence they are very bad in performance → (check part 63 of KudVetkat series prizim tech)

                cursorObj = connectObj.cursor()

        #• Executing the queries :- execute() 
            # So Once the cursorObj is created we can execute MySql queries on a table using the 'execute()' (an instanceMeathod of cursorObj)

                cursorObj.execute(" show databases")
                cursorObj.execute(" select * from students")
                
        #• Finally the results of the query will be stored in the cursorObj itself
            # hence we need to iterate over it using forloop Or
            # we can use 'fetchall()' which is an instanceMeathod of the cursorObj which is also iterable, hence we need to again use forloop 
            # we can use 'fetchone()' to fetch one record at a time 

                for i in cursorObj:
                    print(i)

                results = cursorObj.fetchall()
                for i in results:
                    print(i)

                results = cursorObj.fetchone()
                print(results)

    

        connectObj = MySql.connector.connect(host,userName,passwd,database)
        cursorObj  = connectObj.cursor()
        cursorObj.execute(" select * from table ")
            # after this refer the above code 

    
    #!VIDSUMMARY
#!VID


 # VID 74/.GitHub
	# With the help of GIT 
		# we can Merge the Code 
		# we can maintain Versions of the code 
	
	# there are other repositories available like GitHub repository 
		# Git Lab,Bit Bucket , CVS, Mercurial, Subversion
		
	# in this vid we’ll see how can pull & push the code from the GitHub
	# first, we need to create a GitHub repository on GitHub  ( we can think of the repository as a folder)
	# On creation of the repository it’ll show us some git commands that we can execute on our machine to communicate with git, for this we’ve to install git on our machine 
	
	# to pull our project from GitHub to the IDE we need to copy the url by clicking the “Clone Or Download” and we’ve to paste it on the Vscode 
		# on doing that Vscode will create a project , which contains all the files we’ve pulled from github 
	# to Version Control our code we need to Commit using the “Commit” command, on committing the file will be updated in the local repository 
	# to save it to the remote repository we need to Push the code using the “Push” command 

	# SO, Pull  → Edit the Code → Commit (saved to local repository) → push (will be saved to remote repository)
#!VID


#VID 75 Code Merger,Pull Request in GitHub

    # now lets say we've 2 dovelopers working on a same project 
    # both the dovelopers can create one GitHub account and make use of it, but its not ideal for large members 
    # in that case every dovelopers has to have seperate GitHub account
        # and in this vid lets see how these members with seperate GitHub accounts can Merge the code into one  

    # so below are the steps that other engineer has to take to contribute code to the main repository 
        # note that this engineer is having different GitHub account
        # so search for the main GitHub repository, click on the required repository
            # if we want to clone that repository to your GitHub repository to do some experiments, select -> "Clone Or download"
            # to contribute code for the main repository select -> Fork  (this copy same repository to your GitHub account)
            # now we can edit this copied repository and the changes will not be reflected to the main repository
                # so this user can pull the repository to the local machine, make some changes, commit & push the code back to his repository
                # but to upload the changes to the main repository we've to create a pullRequest --> on the users repository, click on the "New pullRequest" -> and then click on "create pull Request"
                    # as this repository is cloned from main repository, so we can see "1 pullRequest" message on the main repository, click on it and select "confirm Merge"
            # once the pull Request is completed, we can see "Merged" message on both the main & user repositories 

        # to get latest code onto your editor from the repository, you've to make a pull Request from the editor
        # for all this to happen we need to install git on the local machine
#!VID


#VID ZIP function
    # we can use this function to combine 2 lists/tuples like a zip (one element after the other from both the lists)

    #T Example :-
        # lets say we've 2 lists and we want to join then using ZIP function
            list1 = ['prem','kumar','kodi']
            list2 = ['rana','dhagubati','hero']

            zipped = zip(list1,list2)
            print(zipped)  # <zip object at 0x00000019DB10998>  --> we can see that we can getting the memory address of the zipObj

            zipped = list(zip(list1,list2))     # we can convert the zipObj into list
            print(zipped)  # [('prem', 'rana'), ('kumar', 'dhagubati'), ('kodi', 'hero')] --> we got a list of tuples, each value in each tuple is from each list 

            zipped = set(zip(list1,list2))      # you can use set() to remove duplicates
                # say if list1 has prem repeated & list 2 has rana repeated, on converting it to a set, all the duplicates from list1&2 will be removed 
                    # note that :- elements are not compared accross the lists, that is if both the lists have same name, then it'll not be considered as duplicates 

            zipped = dict(zip(list1,list2))     # we can also convert 2 lists into dictionary using zip() & dict(), "list1 will be keys & list2 will be values"

            for (a,b) in zipped:                # as zipped will output tuple in each iteration, we're unpacking them into a&b
                print(a,b)                      # list1-element  list1-element will be printed 
    #!T

    #VIDSUMMARY 
        # we can use zip() funtion to combine 2 lists/sets into one in a zip like pattern 
        # zip(list1,list2) -> this will output a zipObj, which is iterable and outputs a tuple on each iteration
        # list(zip())   -> we can directly convert the zipObj into a list using the list() function 
        # set(zip())   -> to remove duplicates from list1 or list2 we can use set() function, #! if an element is repeated in list1 & list2, it'll not be considered as a duplicate 
        # dict(zip()) -> zip will combine 2 lists & dict will convert zipObj into a dictionary, #! (list1 element will be Keys : list2 elements will be tuples)

        # we can iterate over the zipObj
            for a,b in zipObj:      # as zipped will output tuple in each iteration, we're unpacking them into a&b
                print(a,b)             # list1-element  list1-element will be printed 
    #!VIDSUMMARY
#!VID


# VID Socket Programming
    # Communications on the internet can be -> Client-Server Or Client-Client 
    # In this vid we'll talk about the client server applications
    # this Socket Programming is used to desing an client-server Or client-client applications like -> whats app for example 
    # Socket Programming is used in Network Programming

    #T PortNo & Type of connection(Tcp Or Udp) for our application:-
        # In client-server Socket Programming, we need to have 2 python files on client & server 
        # 2 things are important while designing the Socket Programming 
            # port No  :-  our application has to have a port no (we've to select a free portNo), every application on the machine will use a portNo .
                # we can use free port 9999, PortNo Range -> 0 to 65535
            # Tcp Or Udp :- we need to decide which type of connection our application has to use 
                # Tcp is Connection Oriented, our application has to first establish the connection and then tramsmit the data, 
                    # hence its secure & gives feed back weather the packet has reached the destination
                # Udp is Connection Less,our application will sent packets without establishing the connection, 
                    # based on the Network, peers & seeders our packets will reach the destination
    #!T    

    #T Socket Programming usefull meathods 
        # as said earlier we need to have code on client & server
        # we can have on server & multiple clients, but here lets have only one client

        # Things to note 
            # to achinve Socket Programming we need to import module called -> Socket
            # below are the important meathods in the Socket module
                # first we need to create a socket
                Socket(ipv4/ipv6, Tcp/Udp)    # constructor meathod to create socket (defaults will be ipv4 & Tcp)

                # bind() -> Server side & connect() client side 
                # next we need to bind that socket with a portNo, so that our application can listen or send requests from that port 
                bind((Ipaddres/localhosts ,portNo))      # Ipaddres of client or server, and the portNo what we want to use 
                    # note that we've to pass these 2 arguments as one argument, otherwise it'll result an error -> "Bind() takes only one argument"
                        # hence we need to include our 2 arguments in another square brackets, so that they will be as an object 
                    # now its the server job to bind to a portNo
                    # its the client job to connect to the server using that portNo
                        connect('ipadd_of_server' , 'PortNo the sever bound to' )

                # listen() server side & accept() client side        
                # next if its on server, we've to listed on this portNo
                listen('how many client you want to accept')    # if more clients are trying to connect, they will be rejected

                    # next, once a client sends the request we've to accept that request
                        # inorder to accept requests from multiple clients simulatenously we've to use a Loop 
                    accept()    # this meathod will return 2 things -> Client Socket & ipAdd of the client
                                # here note :-  that server binds to a portNo (say 9999) (and using bind() meathod)
                                # but the client will connnect to the server on portNo 9999, #! but through the auto selected portNo of the client
                                    # every time the client connects to the server, it usses random portNo of the client to connect to the server portNo 9999

                # send() server side & recv() client side, we can use these meathods on the sever side also 
                # next, we need to send some data back to the client, once the client is connected, or we can use this meathod to send data from client to server 
                send(bytes('statement to sent to client', 'utf-8'))  # we've to sent bytes and not the string, hence use bytes() meathod to convert string into byte, byte() also takes in the format in which you want to send as an argument 

                    recv('Buffer Size') # now client can recive the send() data by the server using this meathod, it takes max buffer Size as argument
                    recv().decode()    # decode() instanceMeathod will decode the sent data by the server and print it , if the server sends text it'll print text 

                
                # next we've to close the connection
                close()


            # we can create a chatbox with this socket Programming
                # we've to have a server and multiple clients connect to server to comminicate with each other 
            # this socket Programming also works in JAVA and also in other programming languages
    #!T 

    #T Socket programming code 
        # for this lets take Sever-Client, only one client 
        # you can run both the client & server code both on one machine, or use can use different machine 
            # if you are using the same machine, then we can use 'localhost' instead of IpAdd 

        Server Code :- 
            import socket 
            ServerSocket = socket.socket()  # socket() meathod defaults to Ipv4 & Tcp 
            print('Server Socket Hasbeen created')
            ServerSocket.bind( ('localhost' , 9999) )   # we're binding our application to portNo 9999 on server side (bind() take both these as one argument, otherwise it'll result in an error, explained above)
            ServerSocket.listen( 3 )        # server can listen & accept upto 3 connections 
            print('server is ready & waiting for connections')

            while true:         # we want the server to start from here for every client, because we dont want server to create seperate socket (which is the above code) for every client connection
                ClientSocket,IpAdd =  ServerSocket.accept()     # this accept meathod will give us client socket & ipAdd of the client machine 
                print( "Client Connected with" , "IpAdd" )
                ClientSocket.send( byte ( "you are connected to the server" , "utf-8") )     # Note that we're using the ClientSocket & send() meathod to send text to the client, as explained above we've to send in byte format 
                ClientSocket.close          # Once doen we've to close the client connection 

                """ code will be executed line by line untill the while loop, from the while loop 
                    server will listed, connect to client, send response to the client, and close the client connect and 
                    it'll not go back to the inital code of creating socket and stay at the while loop

                    So, because of while loop, server will move to listening state after doen with one client, and will not create new ServerSocket
                    Also, note that the socket used in while loop is ClientSocket, all the meathods are executed against that socket  """
                
        Client Code :- 
            import socket 

            ClientSocket = socket.socket()  
            ClientSocket.connect("localhost", 9999)     # client is trying to connect to the server(localhost/ipAdd) on port 9999
            print(ClientSocket.recv(1024).decode())     # we're printing the response sent to the client, as server sent data in bytes, we're decoding it here using decode() function

            """ binding to a portNo is the servers job & client will connect to the server through that port 
                On server we'll use ServerSocket & ClientSocket, but on client code we'll use only ClientSocket
                Note that, we've to convert the data to bytes "utf-8" before transferring data through the Network -> Byte()
                Once the data is recived on the other side, we've to decode it -> decode() """
            
    #!T 
    

    # VIDSUMMARY 
        # On server side 
            # import socket module  => import socket as Soc
            # create ServerSocket   => S =  Soc.socket( IpAdd,Tcp/Udp )     >> socket() defaults to localhost & Tcp by default 
            # bind portNo to the created socket     => S.bind(IpAdd,portNo)  >> IpAdd of the server & free portNo, this portNo will be used by the client to connect to the server to access this application
            # Listed through that port for clients  => S.listen(3)      >> it takes No.of clients that it can accpet simultaneously  

            # from this point, its time to make server listed and send reply to the client, it should not go back and create socket for each incomming client 
            # Hence we've to keep our code in a loop

            while True:   # this loop never ends, inOtherWords, code will never get to the first line, untill this execution is terminated 
                ClientSocket, IpAdd = S.accept()    # this meathod will listed & accept client connections, it'll return ClientSocket & client IpAdd, which are stored using variable unpacking 
                ClientSocket.send(byte("HttpStatus : 200", "uft-8"))    # using the ClientSocket, we're sending the status to client, it has to be in byte utf-8 format 
                ClientSocket.close()                # we're closing the connection at the end 

        # On Client Side :- 
            # import socket     => import socket as Soc 
            # create a ClientSocket => C = soc.socket()  >> defaults to localhost & ipv4 
            # connect to the server => C.connect("Server IpAdd", portNo)    # IpAdd & port no of the server can be found on above server code 
            # we can also send data to the server   => C.send(byte("this is lap1 connecting", "utf-8"))
            # we can also receive the data from the server => C.recv(1024).decode()     >> recv( takes in the buffer size), decode() will decode the byte formated data send by the server 


        # Flow Chart :- 
            Server Side                                                 Client Side :-
            import Socket as soc                                        import socket as soc
            S = soc.socket("ipv4", "Tcp")                               C = soc.socket("ipv4", "Tcp")         
            S.bind("ServerAdd", 9999)                                   C.connect("serverIpAdd",9999)
            S.listen(4)

            while True:
                ClientSocket,ClientIpAdd = S.accept()
                ClientHostName = Socket.recv(1024).decode()             C.send(bytes("HostName is prekod","utf-8"))
                ClientSocket.send(bytes("http status 200","uft-8"))     C.recv(1024).decode()     
                ClientSocket.close()
            
        # Server Side : -
            import socket  
            create soceket  -> socket()
            bind to a portNo -> bind()
            go to listening state  -> listen()

            accept any client connections ->accept()
            send responce back to the client  -> send()
            close the client connection and go back to the listening state -> close 
        
        # Things to remember :- 
            # Send() & recv() meathods can be used on both the server & client side 
            # data sent onto the Network has to be in bytes, so we've to use send(Bytes("data","utf-8"))
            # hence, the data on the reciving side has to be decoded -> recv(1024).decode()

            # ussage of while loop is important
    #!VIDSUMMARY
#!VID


# VID 76. Anaconda Setup
    # Anaconda is a python distrubution, that pre includes all the libraries that are required for - ME, Datascience, other Scitific research
    # we can install Anaconda from official website => www.Anaconda.com 
        # Anaconda -> Most Popular Python Datascience Platform 
        # its the fastest way to do python & R Datascience research
        # hence this python distrubution is Popular for Datascience

    # Software that Anaconda distrubution includes (below softwares and many more)
        # python
        # jupitor Notebooks -> Editor (just like Vscode)
        # spider -> IDE 
            # there are 2 versions 
                # Anaconda Python - free 
                # Anaconda Enterprise 

    # On installing Anaconda, we can open 
        # Anaconda promt -> IDE 
        # Anaconda Navigator -> Its a Gui from which we can launch different things like 
            # jupytor Notebook  -> will discuss about this in next vid, its like the normal editor with some extra features like - Conda which is the pakageManager ETC 
            # Spider -> editor (Scitific Python Deovelopment Environment)
#!VID     


#VID 77.  Jupyter Notebook Setup
	# lets see how to install & use Jupyter Notebook
	# Installation of jupytor Notebook:- 
		# either by installing full Anakonda Package -> you’ll have jupytor installed by default , which is accessible through "Anakonda Navigator"
		# Or we can install it manually separately either through website or pip (python -m pip install jupyter)
			# on jupytor website, we can also try the web version of jupytor 
		# jupytor Notebook is same as IPython 
	# Jupytor is an IDE just like Vscode for python 
#!VID
	
#VID Python is Famours for 
    # Python can be used in 
        # Web Dovelopment 
            # there are other options like 	→ Html,Css,JavaScript => these are for "frontend programming"
            # for backend programming we can use →Django, Flask (which are frameworks in python) (we can build web applications using these) 
        # AI → TensorFLow
        # Data Visuvalization, Data Extraction, Data Science 
            # Pandas 
            # MatpotLib  => plot the graphs 
            # SeaBorn   => data Visuvalization
        # Scripting
        # Software Dovelopment 
            #Gui Dovelopment → not famous but we can do that 
        # Mobile Dovelopment → we can build android app using python but its not recomended because android is build on JAVA, we've Hybrid app but python dosent have got support or that  
        # Enbeded Dovelopment →not recomended\famous but we can do that

    # So python is famours for → backend web Dovelopment, AI&ML 
#!VID

#IMP Next is Django
        





    

























	














            
     














            


        






 



















































































































































































































