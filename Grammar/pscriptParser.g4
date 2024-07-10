/*
Python grammar.
The MIT License (MIT).
Copyright (c) 2014, Bart Kiers, bart@big-o.nl
Copyright (c) 2019, Dmitriy Litovchenko, Dmitry.Litovchenko1@yandex.ru, Positive Technologies
Copyright (c) 2019, Nikita Subbotin, sub.nik.and@gmail.com, Positive Technologies
Copyright (c) 2019, Ivan Kochurkin, kvanttt@gmail.com, Positive Technologies

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
*/

parser grammar pscriptParser;

// Insert here @header for C++ parser.

options { tokenVocab=pscriptLexer; superClass=pscriptParserBase; }

root
    : (file_input
    | eval_input)? EOF
    ;

// A single interactive statement;
single_input
    : LINE_BREAK
    | simple_stmt
    | compound_stmt LINE_BREAK
    ;

// A module or sequence of commands read from an input file
file_input
    : (LINE_BREAK | stmt)+
    | single_input
    ;

// An input for the eval() and input() functions
eval_input
    : testlist LINE_BREAK*
    ;

stmt
    : simple_stmt
    | compound_stmt
    ;

compound_stmt
    : IF cond=test COLON suite elif_clause* else_clause?                                                                                         #if_stmt
    // | ( (WHILE test COLON suite else_clause?) | ( WHILE test OPEN_BRACE suite CLOSE_BRACE else_clause?) )                                        #while_stmt
    | WHILE test COLON suite else_clause? #while_stmt
    | ASYNC? FOR exprlist IN testlist COLON suite else_clause?                                                                                   #for_stmt
    | TRY COLON suite (except_clause+ else_clause? finally_clause? | finally_clause)                                                             #try_stmt
    | ASYNC? WITH with_item (COMMA with_item)* COLON suite                                                                                       #with_stmt
    | decorator* classdef                                                                                                            #class_def_stmt
    | decorator* funcdef #func_def_stmt
    ;

suite
    : simple_stmt
    | LINE_BREAK INDENT stmt+ DEDENT
    ;

decorator
    : AT dotted_name (OPEN_PAREN arglist? CLOSE_PAREN)? LINE_BREAK
    ;

elif_clause
    : ELIF test COLON suite
    ;

else_clause
    : ELSE COLON suite
    ;

finally_clause
    : FINALLY COLON suite
    ;

with_item
    // NB compile.c makes sure that the default except clause is last
    : test (AS expr)?
    ;

// Python 2 : EXCEPT test COMMA name
// Python 3 : EXCEPT test AS name
except_clause
    : EXCEPT (test (AS name)?)? COLON suite
    ;

classdef
    : CLASS name (OPEN_PAREN arglist? CLOSE_PAREN)? COLON suite
    ;

funcdef
    : ASYNC? DEF name OPEN_PAREN typedargslist? CLOSE_PAREN COLON suite
    ;

// python 3 paramters
// parameters list may have a trailing comma
typedargslist
    : (def_parameters COMMA)? (args (COMMA def_parameters)? (COMMA kwargs)? | kwargs) COMMA?
    | def_parameters COMMA?
    ;

args
    : STAR named_parameter
    ;

kwargs
    : POWER named_parameter
    ;

def_parameters
    : def_parameter (COMMA def_parameter)*
    ;

// TODO: bare STAR parameter must follow named ones
def_parameter
    : named_parameter (ASSIGN test)?
    | STAR
    ;

named_parameter
    : name (COLON test)?
    ;

simple_stmt
    : small_stmt (SEMI_COLON small_stmt)* SEMI_COLON? (LINE_BREAK | EOF)
    ;

// TODO 1: left part augmented assignment should be `test` only, no stars or lists
// TODO 2: semantically annotated declaration is not an assignment
small_stmt
    : variable_def                                                        #variable_def_stmt
    | AWAIT? atom OPEN_PAREN arglist? CLOSE_PAREN                                              #func_call_stmt
    | DEL exprlist                                                                    #del_stmt
    | PASS                                                                            #pass_stmt
    | BREAK                                                                           #break_stmt
    | CONTINUE                                                                        #continue_stmt
    | RETURN testlist?                                                                #return_stmt
    | RAISE comma_test?                         #raise_stmt
    | yield_expr                                                                      #yield_stmt
    | IMPORT name_as_names                                             #import_stmt
    | FROM from_where
      IMPORT (STAR | OPEN_PAREN import_as_names CLOSE_PAREN | import_as_names)        #from_import_stmt
    | GLOBAL comma_name                                                      #global_stmt
    | ASSERT test (COMMA test)?                                                       #assert_stmt
    | NONLOCAL comma_name                 #nonlocal_stmt 
    ;


variable_def
    : variable_def_consts_with_colon variable_def_name SEMI_COLON 
    | variable_def_consts variable_def_name assign_part
    | variable_def_consts variable_def_comma_name assign_part
    | variable_def_name assign_part
    | variable_def_comma_name assign_part
    ;

variable_def_name
    : dotted_name (OPEN_BRACKET expr CLOSE_BRACKET)* (DOT variable_def_name)?
    ;

variable_def_comma_name
    : variable_def_name (COMMA variable_def_name)* 
    ;


from_where
    : (DOT)* dotted_name | (DOT)+
    ;

comma_name
    : dotted_name (COMMA dotted_name)*
    ;

comma_test
    : test (COMMA test (COMMA test)?)?
    ;

variable_def_consts
    : variable_const=(VAR | CONST | LET)
    ;

variable_def_consts_with_colon
    : variable_const=(VAR | LET) 
    ;

testlist_star_expr
    : (test COMMA)+ (test)?
    | testlist
    ;


star_expr
    : STAR expr
    ;

assign_part
    // if left expression in assign is bool literal, it's mean that is Python 2 here
    : op=( ASSIGN
         | ADD_ASSIGN
         | SUB_ASSIGN
         | MULT_ASSIGN
         | DIV_ASSIGN
         | MOD_ASSIGN
         | XOR_ASSIGN
         | POWER_ASSIGN
         | IDIV_ASSIGN
         )
      (yield_expr | testlist)
    ;

exprlist
    : expr (COMMA expr)* COMMA?
    ;

import_as_names
    : import_as_name (COMMA import_as_name)* COMMA?
    ;

// TODO: that means we can use keyword True as the name here: `from foo import bar as True` -- no
import_as_name
    : name (AS name)?
    ;

name_as_names
    : name_as_name (COMMA name_as_name)*
    ;

name_as_name
    : name (AS name)?
    ;

/*
 * Warning!
 * According to https://docs.python.org/3/reference/expressions.html#lambda LAMBDA should be followed by
 * `parameter_list` (in our case it is `typedargslist`)
 * But that's not true! `typedargslist` may have parameters with type hinting, but that's not permitted in lambda
 * definition
 */
// https://docs.python.org/3/reference/expressions.html#operator-precedence
test
    : logical_test (IF logical_test ELSE test)?
    | LAMBDA varargslist? COLON test
    ;

// the same as `typedargslist`, but with no types
varargslist
    : (vardef_parameters COMMA)? (varargs (COMMA vardef_parameters)? (COMMA varkwargs)? | varkwargs) COMMA?
    | vardef_parameters COMMA?
    ;

vardef_parameters
    : vardef_parameter (COMMA vardef_parameter)*
    ;

// TODO: bare STAR parameter must follow named ones
vardef_parameter
    : name (ASSIGN test)?
    | STAR
    ;

varargs
    : STAR name
    ;

varkwargs
    : POWER name
    ;

logical_test
    : comparison
    | NOT logical_test
    | logical_test op=AND logical_test
    | logical_test op=OR logical_test
    ;

comparison
    : comparison (LESS_THAN | GREATER_THAN | EQUALS | GT_EQ | LT_EQ | NOT_EQ_1 | NOT_EQ_2 | optional=NOT? IN | IS optional=NOT?) comparison
    | expr
    ;

expr
    : AWAIT? atom trailer*
    | op=(ADD | MINUS | NOT_OP) expr
    | expr op=(ADD | MINUS | STAR | DIV | MOD | IDIV | POWER) expr
    ;

atom
    : OPEN_PAREN (yield_expr | testlist)? CLOSE_PAREN
    | OPEN_BRACKET testlist? CLOSE_BRACKET
    | OPEN_BRACE dictmaker? CLOSE_BRACE
    | OPEN_BRACE setmaker CLOSE_BRACE
    | REVERSE_QUOTE testlist COMMA? REVERSE_QUOTE
    | name
    | MINUS? number
    | NONE
    | STRING
    ;

dictmaker
    : dictItem (COMMA dictItem)* //(test COLON test | POWER expr) (COMMA (test COLON test | POWER expr))* COMMA? // key_datum_list                                                
    ;

dictItem 
    : dictKey COLON test
    ;

dictKey 
    : number | name | STRING
    ;

setmaker
    : testlist
    ;

testlist
    : test (COMMA test)*
    ;

dotted_name
    : dotted_name DOT name
    | name
    ;

name
    : NAME
    | bool
    ;

bool
    : TRUE
    | FALSE
    ;

number
    : integer
    | IMAG_NUMBER
    | FLOAT_NUMBER
    ;

integer
    : DECIMAL_INTEGER
    | OCT_INTEGER
    | HEX_INTEGER
    | BIN_INTEGER
    ;

yield_expr
    : YIELD yield_arg?
    ;

yield_arg
    : testlist
    ;

// TODO: this way we can pass: `f(x for x in i, a)`, but it's invalid.
// See: https://docs.python.org/3/reference/expressions.html#calls
trailer
    : DOT name arguments?
    | arguments
    ;

arguments
    : OPEN_PAREN arglist? CLOSE_PAREN
    | OPEN_BRACKET subscriptlist CLOSE_BRACKET
    ;

arglist
    // The reason that keywords are test nodes instead of name is that using name
    // results in an ambiguity. ast.c makes sure it's a name.
    : argument (COMMA argument)* COMMA?
    ;

argument
    : test (ASSIGN test)?
    | (POWER | STAR) test
    ;

// TODO: maybe inline?
subscriptlist
    : subscript (COMMA subscript)* COMMA?
    ;

subscript
    : test (COLON test? sliceop?)?
    | COLON test? sliceop?
    ;

// TODO: maybe inline?
sliceop
    : COLON test?
    ;

comp_for
    : FOR exprlist IN logical_test comp_iter?
    ;

comp_iter
    : comp_for
    | IF test comp_iter?
    ;