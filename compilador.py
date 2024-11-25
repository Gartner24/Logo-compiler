from lark import Tree, Token

def translate_program(ast, out, identacion = 0):
    # print("Tree node", ast)
    if ast.data == "start":
        out.write("import turtle\n")
        out.write("t = turtle.Turtle()\n")
        # Call the method recursively to visit the children
        for c in ast.children:
            translate_program(c, out)
        out.write("turtle.mainloop() \n")
        
    elif ast.data == "basic_instruction":
        # This will be run when the node is a basic_instruction
        [left, right] = ast.children
        #out.write(left.data + " " + right.data)
        if left.value == "FD":
            out.write("t.forward(")
            out.write(right.value)
            out.write(")\n")
    else:
        # No implementation fro the node was found
        print("There is nothing to do for ast node ", ast)