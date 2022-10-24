def arithmetic_arranger(self):

#---Checks if the length of the list is larger than 5. 
    if len(self)>5:
        return 'Error: Too many problems'        
    row_one = [ ]
    new_line= ['\n']
    row_two = [ ]
    row_three = [ ]
    row_four = [ ]
    rows_combined =[]
    
 #--Beginning of the For Loop   
    for each_index in self:
        each_index = each_index.replace(' ','')
 #------If/else block, the operator will have different values depending on which operator is present in the string.       
        if '+' in each_index:
            operator = '+'
        elif '-' in each_index:
            operator = '-'
        else: 
            return 'Error: Operator must either be + or -'
#-------Assigning the variables to compose the operands and result.        
        n = each_index.index(operator)
        operand_one = each_index[0:n]
        operand_two = each_index[n+1:]
        combinedoperands = operand_one+operand_two
        num1 = int(operand_one)
        num2 = int(operand_two)
#-------Checks if the operands have only digits.
        if combinedoperands.isdigit() == False:
            return ' Numbers must only contain digits'
            break
#-------Checks operands lengths
        if len(operand_one) >4:
            return 'Numbers cannot be more than four digits'
            break
        elif len(operand_two)>4:
            return 'Numbers cannot be more than four digits'
            break
#------Based on the value of the operator, the operation will change.        
        if operator =='+':
            addition = num1+num2
            result = str(addition)
            
        elif operator =='-':
            if num1>num2:
                minus = num1-num2
            else:
                minus = num2-num1
            result=str(minus)
#-------Assigning variables that will compose the display of the problem.            

        left_margin = ' '            
        slashn = '\n'
        whitespace =''
        left_space =''
        margin = ' '
#------If/else block to adjust the formating of the output depending on the length of the smaller operand.
        if len(operand_one) > len(operand_two):
            difference = len(operand_one)-len(operand_two)
            whitespace = ' '*difference

        elif len(operand_one) < len(operand_two):
            difference = len(operand_two)-len(operand_one)
            left_space = ' '*difference
        elif len(result) > len(operand_one):
            margin = ''
 #------Assigning variables to compose the output (display of the problem)       
        separator='    '
        line_one = left_margin+left_space+operand_one+separator
        line_two = operator+whitespace+operand_two
        dashes = '_'*len(line_two)
        line_three = dashes+separator
        line_four= margin+result+separator
        
        
#------Here is where I come up with the second issue, regarding the return/print function            
        # output = '{0}{1}{2}{3}'.format(line_one,line_two,line_three,line_four)
        output =line_one+line_two+line_three+line_four
       
        row_one.append(line_one)
        
        row_two.append(line_two)
        row_two.append(separator)
        
        row_three.append(line_three)
        

        row_four.append(line_four)
        rows_combined = row_one+new_line+row_two+new_line+row_three+new_line+row_four
        
        display = ''.join(rows_combined)


        # print(line_one,type(line_one))
       
    return display
    
        
        

    #If I don't leave this command here, the output will show the value None 
    
    # return 'output'
    

print(arithmetic_arranger(['6666+6000', '3000+7', '8000-4000']))