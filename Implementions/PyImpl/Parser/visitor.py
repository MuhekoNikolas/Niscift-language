

import classes
import asyncio, math
from libs.pscriptParser import pscriptParser
from libs.pscriptLexer import pscriptLexer
from libs.pscriptParserVisitor import pscriptParserVisitor
from typing import *

Lexer = pscriptLexer()


unary_operands = {
    '+': lambda x: x,
    '-': lambda x: {'Multiply': {'left': x, 'right': -1}},
    '_': lambda x: {'Floor': x},
    '^': lambda x: {'Ceil': x},
    '!': lambda x: {'Not': x}
}

operations = {
    '**': lambda x, y: {'Power': {'left': x, 'right': y}},
    '*': lambda x, y: {'Multiply': {'left': x, 'right': y}},
    '/': lambda x, y: {'Divide': {'left': x, 'right': y}},
    '//': lambda x, y: {'Round_Divide': {'left': x, 'right': y}},
    '%': lambda x, y: {'Modulo': {'left': x, 'right': y}},
    '+': lambda x, y: {'Add': {'left': x, 'right': y}},
    '-': lambda x, y: {'Subtract': {'left': x, 'right': y}},
    '==': lambda x, y: {'Equals': {'left': x, 'right': y}},
    '!=': lambda x, y: {'NotEquals': {'left': x, 'right': y}},
    '>': lambda x, y: {'Greater': {'left': x, 'right': y}},
    '>=': lambda x, y: {'GreaterEquals': {'left': x, 'right': y}},
    '<': lambda x, y: {'Less': {'left': x, 'right': y}},
    '<=': lambda x, y: {'LessEquals': {'left': x, 'right': y}},
    '<>': lambda x, y: {'NotEquals': {'left': x, 'right': y}},
    'is': lambda x, y: {'Is': {'left': x, 'right': y}},
    'in': lambda x, y: {'In': {'subject': x,'container': y}}
}

assignments = {
    '=': lambda x: {'ASSIGN': x},
    '+=': lambda x: {'ADD_ASSIGN': x},
    '-=': lambda x: {'SUB_ASSIGN': x},
    '*=': lambda x: {'MULT_ASSIGN': x},
    '/=': lambda x: {'DIV_ASSIGN': x},
    '%=': lambda x: {'MOD_ASSIGN': x},
    '&=': lambda x: {'AND_ASSIGN': x},
    '|=': lambda x: {'OR_ASSIGN': x},
    '^=': lambda x: {'XOR_ASSIGN': x},
    '**=': lambda x: {'POWER_ASSIGN': x},
    '//=': lambda x: {'ROUND_DIV_ASSIGN': x},
}

isLastChild = lambda index, totalSize : index == totalSize

class MyVisitor(pscriptParserVisitor):
    def __init__(self):
        super().__init__()
        self.previous_contexts = []

    def getPreviousCtx(self, ctx):
        if len(self.previous_contexts) > 2:
            return self.previous_contexts[-2]
        else:
            return None

    def visit(self, ctx):
        #self.previous_contexts.append(ctx)
        result = super().visit(ctx)

        if type(ctx).__name__ == "ErrorNodeImpl":
            print(f"An error occured", 2, "fkfpofopf")
            exit()

        #self.previous_contexts.pop()

        return result

    async def visitRoot(self, ctx):
        _thisChildren = ctx.children

        objToReturn = {}
        classifiedObjToReturn = None  #classes.Root(ctx=ctx)

        for child in _thisChildren:
            if type(child).__name__ == "File_inputContext":
                _thisVisited = await self.visitFile_input(child)
                objToReturn =  _thisVisited[0]
                classifiedObjToReturn = _thisVisited[1]
                break

        return objToReturn, classifiedObjToReturn

    
    async def visitFile_input(self, ctx):
        thisStatements = []
        classifiedStatements = []

        for child in ctx.children:
            if type(child).__name__ == "StmtContext":
                visitedChild = await self.visitStmt(child)
                classifiedStatements.append(visitedChild[1])
                thisStatements.append(visitedChild[0])

        classifiedObjToReturn = classes.Root(ctx=ctx)
        classifiedObjToReturn.statements = classifiedStatements
        return {
           "Root": {
                "statements" : thisStatements
            }
        }, classifiedObjToReturn
    

    # Visit a parse tree produced by pscriptParser#assign_part.
    async def visitStmt(self, ctx:pscriptParser.StmtContext):

        _thisChildren = ctx.children
        _thisChildrenCount = ctx.getChildCount()

        _isCompoundStatement = ctx.compound_stmt() != None
        _isSimpleStatement =  ctx.simple_stmt() != None

        objToReturn = {}

        classifiedObjToReturn = classes.Stmt(_isSimpleStatement, _isCompoundStatement, ctx=ctx)


        for child in _thisChildren:
            _thisChildType = type(child).__name__
            if _thisChildType == "Simple_stmtContext":
                visitedSimpleStmt = self.visitSimple_stmt(child)
                objToReturn["Simple_stmt"] = {
                    "isSimpleStatement": _isSimpleStatement,
                    "isCompoundStatement": _isCompoundStatement,
                    "statement": visitedSimpleStmt[0]
                }
                classifiedObjToReturn.statement = visitedSimpleStmt[1]
            
            elif _thisChildType == "Func_def_stmtContext":
                visitedSimpleStmt = await self.visitFunc_def_stmt(child)
                objToReturn["Func_def"] = {
                    "isSimpleStatement": _isSimpleStatement,
                    "isCompoundStatement": _isCompoundStatement,
                    "statement": visitedSimpleStmt[0]
                }
                classifiedObjToReturn.statement = visitedSimpleStmt[1]

            elif _thisChildType == "Class_def_stmtContext":
                visitedSimpleStmt = await self.visitClass_def_stmt(child)
                objToReturn["Class_def"] = {
                    "isSimpleStatement": _isSimpleStatement,
                    "isCompoundStatement": _isCompoundStatement,
                    "statement": visitedSimpleStmt[0]
                }
                classifiedObjToReturn.statement = visitedSimpleStmt[1]

            elif _thisChildType == "While_stmtContext":
                visitedWhileLoop = await self.visitWhile_stmt(child)
                objToReturn["While_Loop"] = {
                    "isSimpleStatement": _isSimpleStatement,
                    "isCompoundStatement": _isCompoundStatement,
                    "statement": visitedWhileLoop[0]
                }
                classifiedObjToReturn.statement = visitedWhileLoop[1]

            elif _thisChildType == "With_stmtContext":
                visitedWithLoop = await self.visitWith_stmt(child)
                objToReturn["With_Loop"] = {
                    "isSimpleStatement": _isSimpleStatement,
                    "isCompoundStatement": _isCompoundStatement,
                    "statement": visitedWithLoop[0]
                }
                classifiedObjToReturn.statement = visitedWithLoop[1]
            
            elif _thisChildType == "For_stmtContext":
                visitedForLoop = await self.visitFor_stmt(child)
                objToReturn["For_loop"] = {
                    "isSimpleStatement": _isSimpleStatement,
                    "isCompoundStatement": _isCompoundStatement,
                    "statement": visitedForLoop[0]
                }
                classifiedObjToReturn.statement = visitedForLoop[1]

            elif _thisChildType == "If_stmtContext":
                visitedIf_stmt = await self.visitIf_stmt(child)
                objToReturn["If_stmt"] = {
                    "isSimpleStatement": _isSimpleStatement,
                    "isCompoundStatement": _isCompoundStatement,
                    "statement": visitedIf_stmt[0]
                }
                classifiedObjToReturn.statement = visitedIf_stmt[1]

            elif _thisChildType == "Try_stmtContext":
                visitedTry_stmt = await self.visitTry_stmt(child)
                objToReturn["Try_stmt"] = {
                    "isSimpleStatement": _isSimpleStatement,
                    "isCompoundStatement": _isCompoundStatement,
                    "statement": visitedTry_stmt[0]
                }
                classifiedObjToReturn.statement = visitedTry_stmt[1]


        return objToReturn, classifiedObjToReturn
    

    def visitSimple_stmt(self, ctx:pscriptParser.Simple_stmtContext):
        _thisChildren = ctx.children

        _thisStatements = ctx.small_stmt()


        objToReturn = []

        classifiedObjToReturn = []

        for stmt in _thisStatements:
            thisVisitedStmt = self.visit(stmt)
            objToReturn.append(thisVisitedStmt[0])
            classifiedObjToReturn.append(thisVisitedStmt[1])
        
        return objToReturn, classifiedObjToReturn
    

    async def visitSuite(self, ctx:pscriptParser.SuiteContext):
        _thisChildren = ctx.children 

        objToReturn = {
            "statements": []
        }

        classifiedObjToReturn = classes.Suite([], ctx=ctx)

        for child in _thisChildren:
            if type(child).__name__ != "TerminalNodeImpl":
                loop = asyncio.get_event_loop()

                print(self.visit(child), type(child), vars(child))
                if type(child).__name__ in ["Simple_stmtContext"]:
                    visitedChild = self.visit(child)
                else:
                    visitedChild = await self.visit(child)


                objToReturn["statements"].append(visitedChild[0])
                classifiedObjToReturn.statements.append(visitedChild[1])

        return objToReturn, classifiedObjToReturn
    

    def visitVariable_def_stmt(self, ctx:pscriptParser.Variable_def_stmtContext):
        _thisChildren = ctx.children

        _thisVariableDef = self.visit(_thisChildren[0])

        return _thisVariableDef
    
    def visitVariable_def(self, ctx:pscriptParser.Variable_defContext):
        _thisChildren = ctx.children 

        _thisConst = ctx.variable_def_consts() or ctx.variable_def_consts_with_colon()
        _thisName = ctx.variable_def_name()
        _thisCommaNames = ctx.variable_def_comma_name()
        _thisAssignPart = ctx.assign_part()


        visitedVariableConst = self.visit(_thisConst)["Variable_Def_Const"] if _thisConst!= None else "var"
        visitedVariableName = self.visit(_thisName) if _thisName != None else None
        visitedCommaNames = self.visit(_thisCommaNames) if _thisCommaNames != None else None
        visitedAssignPart = self.visitAssign_part(_thisAssignPart) if _thisAssignPart != None else ({"assignment": {"ASSIGN": {"IDENTIFIER": {"name": "undefined"}}}}, {"assignment": classes.ASSIGNMENT(type="ASSIGN", value=classes.IDENTIFIER(name="undefined", ctx=ctx), ctx=ctx)})

        objToReturn = {
            "variable_const": visitedVariableConst,
            "variable_names": [visitedVariableName[0]] if visitedVariableName!= None else visitedCommaNames[0]["Comma_Names"]["content"],
            "assignment": visitedAssignPart[0]
        }

        classifiedObjToReturn = classes.VariableDef(visitedVariableConst, [visitedVariableName[1]] if visitedVariableName!= None else visitedCommaNames[1]["content"], visitedAssignPart[1], ctx=ctx)

        return objToReturn, classifiedObjToReturn
    
    def visitVariable_def_consts(self, ctx:pscriptParser.Variable_def_constsContext):
        _thisConstText = ctx.getText()

        if _thisConstText == "var":
            objToReturn = {"Variable_Def_Const": "var"}
        elif _thisConstText == "const":
            objToReturn = {"Variable_Def_Const": "const"}
        elif _thisConstText == "let":
            objToReturn = {"Variable_Def_Const": "let"}
        
        return objToReturn
    
    def visitVariable_def_consts_with_colon(self, ctx:pscriptParser.Variable_def_consts_with_colonContext):
        _thisConstText = ctx.getText()

        if _thisConstText == "var":
            objToReturn = {"Variable_Def_Const": "var"}
        elif _thisConstText == "let":
            objToReturn = {"Variable_Def_Const": "let"}
        
        return objToReturn
    
    def visitVariable_def_name(self, ctx:pscriptParser.Variable_def_nameContext):
        thisChildren = ctx.children 

        objToReturn = {
            "names": []
        }
        classifiedObjToReturn = classes.Variable_def_name(ctx=ctx)

        for child in thisChildren:
            if type(child).__name__ == "TerminalNodeImpl":
                continue 

            visitedChild = self.visit(child)

            if type(child).__name__ == "ExprContext":
                objToReturn["names"].append({
                    "Indexing": visitedChild[0]
                })
                classifiedObjToReturn.names.append(classes.Indexing(visitedChild[1], ctx=child))
                continue
            
            elif type(child).__name__ == "Variable_def_nameContext":
                objToReturn["names"] += visitedChild[0]["names"]
                classifiedObjToReturn.names += visitedChild[1].names
                continue

            else:
                objToReturn["names"].append(visitedChild[0])
                classifiedObjToReturn.names.append(visitedChild[1])
                continue
        
        return objToReturn, classifiedObjToReturn

    def visitVariable_def_comma_name(self, ctx:pscriptParser.Variable_def_comma_nameContext):
        objToReturn = {
            "Comma_Names": {
                "content": []
            }
        }
        classifiedObjToReturn = {
            "content": []
        }
        _thisNames = ctx.variable_def_name()

        for name in _thisNames:
            thisVisited = self.visit(name)
            objToReturn["Comma_Names"]["content"].append(thisVisited[0])
            classifiedObjToReturn["content"].append(thisVisited[1])
        
        return objToReturn, classifiedObjToReturn
    

    def visitComma_name(self, ctx:pscriptParser.Comma_nameContext):
        _thisChildren = ctx.children

        objToReturn = {
            "Comma_Names": {
                "content": []
            }
        }
        classifiedObjToReturn = {
            "content": []
        }
        _thisNames = ctx.dotted_name()

        for name in _thisNames:
            thisVisited = self.visit(name)
            objToReturn["Comma_Names"]["content"].append(thisVisited[0])
            classifiedObjToReturn["content"].append(thisVisited[1])
        
        return objToReturn, classifiedObjToReturn
    
    def visitAssign_part(self, ctx:pscriptParser.Assign_partContext):
        _thisChildren = ctx.children

        _thisVisitedFirstChild = self.visit(_thisChildren[1])
        objToReturn = assignments[ctx.op.text](_thisVisitedFirstChild[0])
        classifiedObjToReturn = classes.ASSIGNMENT(ctx.op.text, _thisVisitedFirstChild[1], ctx=ctx)

        return objToReturn, classifiedObjToReturn

    
    def visitDel_stmt(self, ctx:pscriptParser.Del_stmtContext):
        _thisChildren = ctx.children

        objToReturn = {
            "Del": {
                "to_delete": []
            }
        }

        classifiedObjToReturn = classes.Del(ctx=ctx)

        _thisExpressions = ctx.children[1].expr()

        for _expr in _thisExpressions:
            visitedExpr = self.visit(_expr)
            objToReturn["Del"]["to_delete"].append(visitedExpr[0])
            classifiedObjToReturn.to_delete.append(visitedExpr[1])
    
        return objToReturn, classifiedObjToReturn
    
    def visitPass_stmt(self, ctx:pscriptParser.Pass_stmtContext):
        return {"Pass": {}}, classes.Pass(ctx=ctx)
    
    def visitBreak_stmt(self, ctx:pscriptParser.Break_stmtContext):
        return {"Break": {}}, classes.Break(ctx=ctx)

    def visitContinue_stmt(self, ctx:pscriptParser.Continue_stmtContext):
        return {"Continue": {}}, classes.Continue(ctx=ctx)

    def visitReturn_stmt(self, ctx:pscriptParser.Return_stmtContext):
        thisChildren = ctx.children
        if ctx.getChildCount() == 1:
            objToReturn = {
                "Return": {
                    "to_return": []
                }
            }
            classifiedObjToReturn = classes.Return(ctx=ctx)

        else:
            objToReturn = {
                "Return": {
                    "to_return": []
                }
            }
            classifiedObjToReturn = classes.Return(ctx=ctx)

            for test in thisChildren[1].test():
                thisVisitedTest = self.visit(test)
                objToReturn["Return"]["to_return"].append(thisVisitedTest[0])
                classifiedObjToReturn.to_return.append(thisVisitedTest[1])

        return objToReturn, classifiedObjToReturn
    

    def visitRaise_stmt(self, ctx:pscriptParser.Raise_stmtContext):
        thisChildren = ctx.children 
        thisCommaTest = ctx.comma_test()

        classifiedObjToReturn = classes.Raise(ctx=ctx)

        if thisCommaTest == None:
            objToReturn = {
                "Raise": {
                    "to_raise": []
                }
            }

        else:
            objToReturn = {
                "Raise": {
                    "to_raise": []
                }
            }

            for test in thisCommaTest.test():
                thisVisitedTest = self.visit(test)
                objToReturn["Raise"]["to_raise"].append(thisVisitedTest[0])
                classifiedObjToReturn.to_raise.append(thisVisitedTest[1])

        return objToReturn, classifiedObjToReturn

    def visitYield_stmt(self, ctx:pscriptParser.Yield_stmtContext):
        thisChildren = ctx.children 
        thisYieldExpr = thisChildren[0]
        thisVisitedExpr = self.visit(thisYieldExpr)

        return thisVisitedExpr
    
    
    def visitYield_expr(self, ctx:pscriptParser.Yield_exprContext):
        thisChildren = ctx.children 

        objToReturn = {
            "Yield": {
                "to_yield": []
            }
        }
        classifiedObjToReturn = classes.Yield(ctx=ctx)

        if ctx.getChildCount() != 1:

            thisToYieldArray = thisChildren[1].testlist().children

            for toYield in thisToYieldArray:
                if type(toYield).__name__ != "TerminalNodeImpl":
                    thisVisitedToYield = self.visit(toYield)
                    objToReturn["Yield"]["to_yield"].append(thisVisitedToYield[0])
                    classifiedObjToReturn.to_yield.append(thisVisitedToYield[1])
        
        return objToReturn, classifiedObjToReturn

    def visitFunc_call_stmt(self, ctx: pscriptParser.Func_call_stmtContext):
        thisChildren = ctx.children

        thisAwait = ctx.AWAIT()
        thisName = ctx.atom()
        thisArguments = ctx.arglist()

        visitedName = self.visit(thisName)

        if thisArguments != None:
            visitedArguments = self.visit(thisArguments) 
        else:
            visitedArguments = ({'Function_Call_Arguments': []}, classes.Function_Call_Arguments(ctx=ctx))

        objToReturn = {
            "Function_Call": {
                "isAwaited": True if thisAwait != None else False,
                "name": visitedName[0],
                "arguments": visitedArguments[0]
            }
        }
        classifiedObjToReturn = classes.Function_Call(True if thisAwait != None else False, visitedName[1], visitedArguments[1], ctx)

        return objToReturn, classifiedObjToReturn

    def visitImport_stmt(self, ctx:pscriptParser.Import_stmtContext):
        thisChildren = ctx.children 

        importCmd = ctx.IMPORT().getText()

        objToReturn = {
            "Import": {
                "to_import": [],
                "importCmd": importCmd
            }
        }

        classifiedObjToReturn = classes.Import(ctx=ctx, importCmd=importCmd)

        thisVisitedImports = self.visit(thisChildren[1])

        objToReturn["Import"]["to_import"] = thisVisitedImports[0]["content"]
        classifiedObjToReturn.to_import = thisVisitedImports[1]["content"]

        return objToReturn, classifiedObjToReturn
    
    def visitFrom_import_stmt(self, ctx: pscriptParser.From_import_stmtContext):
        thisChildren = ctx.children 

        importCmd = ctx.IMPORT().getText()

        objToReturn = {
            "Import_From": {
                "from_where": None, 
                "to_import": None,
                "importCmd": importCmd
            }
        }

        classifiedObjToReturn = classes.Import_From(ctx=ctx, importCmd=importCmd)

        thisWhere = ctx.from_where()
        thisToImport = thisChildren[3]

        thisVisitedFromWhere = self.visit(thisWhere)

        objToReturn["Import_From"]["from_where"] = thisVisitedFromWhere[0]
        classifiedObjToReturn.from_where = thisVisitedFromWhere[1]


        if thisToImport.getText() == "*":
            thisVisitedToImport = ([{"All": {}}], [classes.All(ctx=ctx)])
        else:
            thisVisitedToImport = self.visitImport_as_names(thisToImport)

        objToReturn["Import_From"]["to_import"] = thisVisitedToImport[0]
        classifiedObjToReturn.to_import = thisVisitedToImport[1]

        return objToReturn, classifiedObjToReturn
    
    def visitFrom_where(self, ctx: pscriptParser.From_whereContext):
        thisChildren = ctx.children 
        thisStartingDots = 0 

        currentCharInd = 0
        nextChar = thisChildren[currentCharInd]
        while nextChar.getText() == "." and currentCharInd < len(thisChildren)-1:
            nextChar = thisChildren[currentCharInd]
            currentCharInd += 1

        thisStartingDotsCount = currentCharInd
        thisDottedName = ctx.dotted_name()
        visitedDottedName = self.visit(thisDottedName) if thisDottedName != None else ([], [])

        objToReturn = {
            "folder_traversals": thisStartingDotsCount-1 if thisStartingDotsCount > 0 else 0,
            "dotted_names": visitedDottedName[0]
        }

        classifiedObjToReturn = {
            "folder_traversals": thisStartingDotsCount-1 if thisStartingDotsCount > 0 else 0,
            "dotted_names": visitedDottedName[1]
        }

        return objToReturn, classifiedObjToReturn

    def visitDotted_name(self, ctx: pscriptParser.Dotted_nameContext):
        thisChildren = ctx.children 
        thisChildCount = ctx.getChildCount()

        objToReturn = {
            "Dotted_Name": {
                "names": []
            }
        }

        classifiedObjToReturn = classes.Dotted_Name(ctx=ctx)

        objToReturnNames = []
        classifiedObjToReturnNames = []

        if thisChildCount == 1:
            visitedFirstChild = self.visit(thisChildren[0])
            objToReturnNames.append(visitedFirstChild[0])
            classifiedObjToReturnNames.append(visitedFirstChild[1])
        
        elif thisChildCount == 2:
            print(10)
            pass

        elif thisChildCount == 3:
            thisFirstChild = thisChildren[0]
            thisSecondChild = thisChildren[1]
            thisThirdChild = thisChildren[2]

            if thisSecondChild.getText() == ".":

                visitedFirstChild = self.visit(thisFirstChild)
                visitedThirdChild = self.visit(thisThirdChild)

                objToReturnNames = visitedFirstChild[0]["Dotted_Name"]["names"] + [visitedThirdChild[0]]
                classifiedObjToReturnNames = visitedFirstChild[1].names + [visitedThirdChild[1]]

        objToReturn["Dotted_Name"]["names"] = objToReturnNames
        classifiedObjToReturn.names = classifiedObjToReturnNames

        return objToReturn, classifiedObjToReturn
    
    def visitImport_as_names(self, ctx: pscriptParser.Import_as_namesContext):
        thisChildren = ctx.children 
        thisNames = ctx.import_as_name()

        objToReturn = []
        classifiedObjToReturn = []

        for name in thisNames:
            visitedName = self.visit(name)
            objToReturn.append(visitedName[0])
            classifiedObjToReturn.append(visitedName[1])

        return objToReturn, classifiedObjToReturn

    def visitImport_as_name(self, ctx: pscriptParser.Import_as_nameContext):
        thisChildren = ctx.children 

        thisChildCount = ctx.getChildCount()

        if thisChildCount == 3:
            firstChild = thisChildren[0]
            secondChild = thisChildren[1]
            thirdChild = thisChildren[2]

            if secondChild.getText() == "as":
                visitedFirst = self.visit(firstChild)
                visitedThird = self.visit(thirdChild)
                objToReturn = {
                    "initial": visitedFirst[0],
                    "as": visitedThird[0]
                }

                classifiedObjToReturn = classes.NameAsName(visitedFirst[1], visitedThird[1], ctx=ctx)
        
        elif thisChildCount == 1:
            firstChild = thisChildren[0]
            visitedFirstChild = self.visit(firstChild)

            objToReturn = {
                "initial": visitedFirstChild[0],
                "as": visitedFirstChild[0]
            }
            classifiedObjToReturn = classes.NameAsName(visitedFirstChild[1], visitedFirstChild[1], ctx=ctx)

        return objToReturn, classifiedObjToReturn

    
    def visitName_as_names(self, ctx: pscriptParser.Name_as_namesContext):
        objToReturn = {
            "content": []
        }
        classifiedObjToReturn = {
            "content": []
        }

        thisNames = ctx.name_as_name()
        thisChildren = ctx.children 

        for name in thisNames:
            visitedName = self.visit(name)
            objToReturn["content"].append(visitedName[0])
            classifiedObjToReturn["content"].append(visitedName[1])

        return objToReturn, classifiedObjToReturn
    
    def visitName_as_name(self, ctx: pscriptParser.Name_as_nameContext):
        thisChildren = ctx.children 

        thisChildCount = ctx.getChildCount()

        if thisChildCount == 3:
            firstChild = thisChildren[0]
            secondChild = thisChildren[1]
            thirdChild = thisChildren[2]

            if secondChild.getText() == "as":
                visitedFirst = self.visit(firstChild)
                visitedThird = self.visit(thirdChild)
                objToReturn = {
                    "initial": visitedFirst[0],
                    "as": visitedThird[0]
                }

                classifiedObjToReturn = classes.NameAsName(visitedFirst[1], visitedThird[1], ctx=ctx)
        
        elif thisChildCount == 1:
            firstChild = thisChildren[0]
            visitedFirstChild = self.visit(firstChild)

            objToReturn = {
                "initial": visitedFirstChild[0],
                "as": visitedFirstChild[0]
            }
            classifiedObjToReturn = classes.NameAsName(visitedFirstChild[1], visitedFirstChild[1], ctx=ctx)

        
        return objToReturn, classifiedObjToReturn
    
    def visitGlobal_stmt(self, ctx:pscriptParser.Global_stmtContext):
        thisChildren = ctx.children 
        thisCommaNames = ctx.comma_name().name()
        
        objToReturn = {
            "Global": {
                "to_globalize": []
            }
        }
        classifiedObjToReturn = classes.Global(ctx=ctx)

        for name in thisCommaNames:
            visitedName = self.visit(name)
            objToReturn["Global"]["to_globalize"].append(visitedName[0])
            classifiedObjToReturn.to_globalize.append(visitedName[1])

        return objToReturn, classifiedObjToReturn


    def visitNonlocal_stmt(self, ctx:pscriptParser.Nonlocal_stmtContext):
        thisChildren = ctx.children 
        thisCommaNames = ctx.comma_name().name()
        
        objToReturn = {
            "NonLocal": {
                "to_non_localize": []
            }
        }
        classifiedObjToReturn = classes.NonLocal(ctx=ctx)

        for name in thisCommaNames:
            visitedName = self.visit(name)
            objToReturn["NonLocal"]["to_non_localize"].append(visitedName[0])
            classifiedObjToReturn.to_non_localize.append(visitedName[1])

        return objToReturn, classifiedObjToReturn

    def visitAssert_stmt(self, ctx:pscriptParser.Assert_stmtContext):
        thisChildren = ctx.children 
        thisTests = ctx.test()
        
        objToReturn = {
            "Assert": {
                "tests": []
            }
        }
        classifiedObjToReturn = classes.Assert(ctx=ctx)

        for test in thisTests:
            visitedTest = self.visit(test)
            objToReturn["Assert"]["tests"].append(visitedTest[0])
            classifiedObjToReturn.tests.append(visitedTest[1])

        return objToReturn, classifiedObjToReturn
    
    
    async def visitIf_stmt(self, ctx:pscriptParser.If_stmtContext):
        _thisChildren = ctx.children

        _thisTest = ctx.test()
        _thisElifs = ctx.elif_clause()
        _thisElse = ctx.else_clause()
        _thisSuite = ctx.suite()

        thisElif = []
        classifiedElif = []

        for clause in _thisElifs:
            thisVisitedElif = await self.visitElif_clause(clause)
            thisElif.append(thisVisitedElif[0])
            classifiedElif.append(thisVisitedElif[1])

        thisVisitedTest = self.visitTest(_thisTest)
        thisVisitedSuite = await self.visitSuite(_thisSuite)
        thisVisitedElse = await self.visit(_thisElse) if _thisElse!= None else (None, None)

        objToReturn = {
            "test": thisVisitedTest[0],
            "suite": thisVisitedSuite[0],
            'Elif': thisElif,
            "Else": thisVisitedElse[0]
        }

        classifiedObjToReturn = classes.If(thisVisitedTest[1], thisVisitedSuite[1], classifiedElif, thisVisitedElse[1], ctx=ctx)

        return objToReturn, classifiedObjToReturn
    

    async def visitClass_def_stmt(self, ctx: pscriptParser.Class_def_stmtContext):
        thisChildren = ctx.children 

        objToReturnAll = await self.visit(ctx.classdef())

        thisDecorators = ctx.decorator()

        decorators = []
        classifiedDecorators = []

        for decorator in thisDecorators:
            visitedDecorator = self.visit(decorator)
            decorators.append(visitedDecorator[0])
            classifiedDecorators.append(visitedDecorator[1])

        objToReturnAll[0]["decorators"] =  decorators
        objToReturnAll[1].decorators =  classifiedDecorators

        return objToReturnAll
    

    async def visitClassdef(self, ctx:pscriptParser.ClassdefContext):
        thisChildren = ctx.children 

        _thisName = ctx.name()
        _thisParams = ctx.arglist()
        _thisSuite = ctx.suite()

        objToReturn = {
                "name": None,
                "params": [],
                "suite": None
            
        }

        visitedName = self.visit(_thisName)
        visitedParams = self.visit(_thisParams) if _thisParams!= None else ([], [])
        visitedSuite = await self.visitSuite(_thisSuite)

        classifiedObjToReturn = classes.ClassDef(visitedName[1], visitedParams[1], visitedSuite[1], ctx=ctx)

        objToReturn["name"] = visitedName[0]
        objToReturn["params"] = visitedParams[0]
        objToReturn["suite"] = visitedSuite[0]

        return objToReturn, classifiedObjToReturn
    
    async def visitFunc_def_stmt(self, ctx: pscriptParser.Func_def_stmtContext):
        thisChildren = ctx.children 

        objToReturnAll = await self.visit(ctx.funcdef())

        thisDecorators = ctx.decorator()

        decorators = []
        classifiedDecorators = []

        for decorator in thisDecorators:
            visitedDecorator = self.visit(decorator)
            decorators.append(visitedDecorator[0])
            classifiedDecorators.append(visitedDecorator[1])

        objToReturnAll[0]["decorators"] =  decorators
        objToReturnAll[1].decorators =  classifiedDecorators

        return objToReturnAll
    
    async def visitFuncdef(self, ctx:pscriptParser.FuncdefContext):
        thisChildren = ctx.children 

        _thisIsAsync = False if ctx.ASYNC() == None else True
        _thisName = ctx.name()
        _thisParams = ctx.typedargslist()
        _thisSuite = ctx.suite()

        objToReturn = {
                "isAsync": _thisIsAsync,
                "name": None,
                "params": [],
                "suite": None
            
        }

        visitedName = self.visit(_thisName)
        visitedParams = self.visit(_thisParams) if _thisParams!= None else ([], [])
        visitedSuite = await self.visitSuite(_thisSuite)

        classifiedObjToReturn = classes.FunctionDef(_thisIsAsync, visitedName[1], visitedParams[1], visitedSuite[1], ctx=ctx)

        objToReturn["name"] = visitedName[0]
        objToReturn["params"] = visitedParams[0]
        objToReturn["suite"] = visitedSuite[0]
        
        return objToReturn, classifiedObjToReturn
    
    def visitDecorator(self, ctx:pscriptParser.DecoratorContext):
        _thisChildren = ctx.children 
        thisName = ctx.dotted_name()
        thisArgs = ctx.arglist()
        thisOpeningBrace = ctx.OPEN_PAREN()

        visitedName = self.visit(thisName)

        visitedArgs = (None, None) 

        if thisOpeningBrace!= None:
            thisNamesLength = len(visitedName[0]["Dotted_Name"]["names"])
            visitedArgs = self.visit(thisArgs) if thisArgs != None else (None, None)

        objectToReturn = {
            "Decorator": {
                "name": visitedName[0],
                "call_args": visitedArgs[0]
            }
        }
        classifiedObjToReturn = classes.Decorator(visitedName[1], visitedArgs[1], ctx=ctx)

        return objectToReturn, classifiedObjToReturn

    async def visitWith_stmt(self, ctx:pscriptParser.With_stmtContext):
        _thisChildren = ctx.children

        _thisIsAsync = False if ctx.ASYNC() == None else True
        _thisWithItems = ctx.with_item()
        _thisSuite = ctx.suite()

        objToReturn = {
            "isAsync": _thisIsAsync,
            "with_expressions": [],
            "suite": None
        }
    
        classifiedObjToReturn = classes.With(_thisIsAsync, ctx=ctx)

        thisVisitedSuite = await self.visitSuite(_thisSuite)
        objToReturn["suite"] = thisVisitedSuite[0]
        classifiedObjToReturn.suite = thisVisitedSuite[1]

        for withItem in _thisWithItems:
            thisVisitedWithItem = self.visitWith_item(withItem)
            objToReturn["with_expressions"].append(thisVisitedWithItem[0])
            classifiedObjToReturn.with_expressions.append(thisVisitedWithItem[1])

        return objToReturn, classifiedObjToReturn
    
    def visitWith_item(self, ctx:pscriptParser.With_itemContext):
        thisTest = ctx.test()
        thisAs = ctx.expr()

        thisVisitedTest = self.visitTest(thisTest) 
        thisVisitedAs = self.visit(thisAs) if thisAs != None else (None, None)

        objToReturn = {
            "test": thisVisitedTest[0],
            "_as": thisVisitedAs[0]
        }

        classifiedObjToReturn = classes.WithItem(thisVisitedTest[1], thisVisitedAs[1], ctx=ctx)
        return objToReturn, classifiedObjToReturn
        
    async def visitFor_stmt(self, ctx:pscriptParser.For_stmtContext):
        _thisChildren = ctx.children

        _thisIsAsync = False if ctx.ASYNC() == None else True
        _thisInVariable = ctx.exprlist()
        _thisIterable = ctx.testlist()
        _thisSuite = ctx.suite()
        _thisElse = ctx.else_clause()

        if type(_thisInVariable).__name__ == "ExprContext":
            parsedVariableName = self.visit(_thisInVariable)
            _thisParsedVariableName = [parsedVariableName[0]]
            classifiedVariableName = [parsedVariableName[1]]
            if list(_thisParsedVariableName.keys())[0] != "IDENTIFIER":
                print("An error occured")
                exit()
        else:
            parsedVariableName = self.visit(_thisInVariable)
            _thisParsedVariableName = [parsedVariableName[0]["content"]]
            classifiedVariableName = [parsedVariableName[1]["content"]]

        thisVisitedIterable = self.visit(_thisIterable)
        thisVisitedSuite = await self.visitSuite(_thisSuite)
        thisVisitedElseClause = await self.visitElse_clause(_thisElse) if _thisElse != None else (None, None)

        objToReturn = {
            "isAsync": _thisIsAsync,
            "loopVariableNames": _thisParsedVariableName,
            "iterable": thisVisitedIterable[0],
            "suite": thisVisitedSuite[0],
            "else": thisVisitedElseClause[0]
        }

        classifiedObjToReturn = classes.For(_thisIsAsync, classifiedVariableName, thisVisitedIterable[1], thisVisitedSuite[1], thisVisitedElseClause[1], ctx=ctx)

        return objToReturn, classifiedObjToReturn

    async def visitWhile_stmt(self, ctx:pscriptParser.While_stmtContext):
        _thisChildren = ctx.children

        _thisObjToReturn = {
            "test": None, 
            "suite": None
        }

        classifiedObjToReturn = classes.While(None, None, ctx=ctx)

        _thisTest = ctx.test()
        _thisSuite = ctx.suite()
        _thisElse = ctx.else_clause()

        _thisObjToReturn["Else"] = None if _thisElse==None else await self.visitElse_clause(_thisElse) 

        for child in _thisChildren:
            if type(child).__name__ == "TestContext":
                visitedTest = self.visitTest(_thisTest)
                _thisObjToReturn["test"] = visitedTest[0]
                classifiedObjToReturn.test = visitedTest[1]

            elif type(child).__name__ == "SuiteContext":
                visitedSuite = await self.visitSuite(_thisSuite)
                _thisObjToReturn["suite"] = visitedSuite[0]
                classifiedObjToReturn.test = visitedSuite[1]

        return _thisObjToReturn, classifiedObjToReturn
    
    async def visitElif_clause(self, ctx:pscriptParser.Elif_clauseContext):
        _thisSuite = ctx.suite()

        thisVisitedSuite = await self.visitSuite(_thisSuite)

        objToReturn = {
            "suite": thisVisitedSuite[0]
        }

        classifiedObjToReturn = classes.ElifClause(suite=thisVisitedSuite[1], ctx=ctx)

        return objToReturn, classifiedObjToReturn
    
    async def visitElse_clause(self, ctx:pscriptParser.Else_clauseContext):
        _thisSuite = ctx.suite()

        thisVisitedSuite = await self.visitSuite(_thisSuite)
        objToReturn = {
            "suite": thisVisitedSuite[0]
        }

        classifiedObjToReturn = classes.ElseClause(suite=thisVisitedSuite[1], ctx=ctx)

        return objToReturn, classifiedObjToReturn

    
    async def visitTry_stmt(self, ctx:pscriptParser.Try_stmtContext):
        thisChildren = ctx.children 

        objToReturn = {
            "Try_stmt": {
                "try_suite": None,
                "except_clauses": [],
                "else_clause": None,
                "finally_clause": None
            }
        }
        classifiedObjToReturn = classes.Try_stmt(ctx=ctx)

        thisSuite = ctx.suite()
        thisExceptClauses = ctx.except_clause()
        thisElseClause = ctx.else_clause()
        thisFinallyClause = ctx.finally_clause()

        thisVisitedSuite = await self.visitSuite(thisSuite)
        thisVisitedElseClause = await self.visitElse_clause(thisElseClause) if thisElseClause!= None else (None, None)
        thisVisitedFinallyClause = await self.visitFinally_clause(thisFinallyClause) if thisFinallyClause!=None else (None, None)

        for exceptClause in thisExceptClauses:
            visitedExceptClause = await self.visit(exceptClause)
            objToReturn["Try_stmt"]["except_clauses"].append(visitedExceptClause[0])
            classifiedObjToReturn.except_clauses.append(visitedExceptClause[1])

        objToReturn["Try_stmt"]["try_suite"] = thisVisitedSuite[0]
        objToReturn["Try_stmt"]["else_clause"] = thisVisitedElseClause[0]
        objToReturn["Try_stmt"]["finally_clause"] = thisVisitedFinallyClause[0]

        classifiedObjToReturn.try_suite = thisVisitedSuite[1]
        classifiedObjToReturn.else_clause = thisVisitedElseClause[1]
        classifiedObjToReturn.finally_clause = thisVisitedFinallyClause[1]

        return objToReturn, classifiedObjToReturn


    def visitTest(self, ctx:pscriptParser.TestContext):
        _thisChildren = ctx.children
        _thisLogic = _thisChildren[0]

        objToReturn = self.visitLogical_test(_thisLogic)
        return objToReturn
    
    def visitSliceopContext(self, ctx: pscriptParser.SliceopContext):
        pass
    
    def visitLogical_test(self, ctx:pscriptParser.Logical_testContext):
        _thisChildren = ctx.children 

        #self.visit(_thisChildren[0]))

        if ctx.getChildCount() == 3:
            _thisConditionJoiner = _thisChildren[1]
            _thisParsedLeft = self.visit(_thisChildren[0])
            _thisParsedRight = self.visit(_thisChildren[2])
            
            if _thisConditionJoiner.getText() in ["or"]:
                objToReturn = {
                    "OR": {
                        "left": _thisParsedLeft[0],
                        "right": _thisParsedRight[0]
                    }
                }
                classifiedObjToReturn = {
                    "OR": {
                        "left": _thisParsedLeft[1],
                        "right": _thisParsedRight[1]
                    }
                }

            elif _thisConditionJoiner.getText() in ["and"]:
                objToReturn = {
                    "AND": {
                        "left": _thisParsedLeft[0],
                        "right": _thisParsedRight[0]
                    }
                }
                classifiedObjToReturn = {
                    "AND": {
                        "left": _thisParsedLeft[1],
                        "right": _thisParsedRight[1]
                    }
                }


        elif ctx.getChildCount() == 2:
            _thisFirstChild = _thisChildren[0]
            _thisExpr = _thisChildren[1]

            if _thisFirstChild.getText() in ["not"]:
                visitedExpr = self.visit(_thisExpr)
                objToReturn = {
                    "NOT":  visitedExpr[0]
                }
                classifiedObjToReturn = {
                    "NOT": visitedExpr[1]
                }


        elif ctx.getChildCount() == 1:
            _thisTest = _thisChildren[0]
            if type(_thisTest).__name__ == "ComparisonContext":
                objToReturnAll = self.visitComparison(_thisTest)
                objToReturn = objToReturnAll[0]
                classifiedObjToReturn = objToReturnAll[1]

            if type(_thisTest).__name__ == "AtomContext":
                objToReturnAll = self.visitAtom(_thisTest)
                objToReturn = objToReturnAll[0]
                classifiedObjToReturn = objToReturnAll[1]


        return objToReturn, classifiedObjToReturn
    
    def visitComparison(self, ctx: pscriptParser.ComparisonContext):
        _thisChildren = ctx.children 

        if ctx.getChildCount() == 4:
            _thisFirstChild = _thisChildren[0]
            _thisSecondChild = _thisChildren[1]
            _thisThirdChild = _thisChildren[2]
            _thisFourthChild = _thisChildren[3]

            if _thisSecondChild.getText() in ["is"] and _thisThirdChild.getText() in ["not"]:
                visitedLeft = self.visit(_thisFirstChild)
                visitedRight = self.visit(_thisFourthChild)
                objToReturn = {
                    "IS_NOT": {
                        "left": visitedLeft[0],
                        "right": visitedRight[0]
                    }
                }
                classifiedObjToReturn = {
                    "IS_NOT": {
                        "left": visitedLeft[1],
                        "right": visitedRight[1]
                    }
                }
                
        elif ctx.getChildCount() == 3:
            _thisOp = _thisChildren[1]
            _thisLeft = _thisChildren[0]
            _thisRight = _thisChildren[2]

            
            visitedLeft = self.visit(_thisLeft)
            visitedRight = self.visit(_thisRight)

            objToReturn = operations[_thisOp.getText().lower()](visitedLeft[0], visitedRight[0]) 
            classifiedObjToReturn = classes.Operation(_thisOp.getText(), visitedLeft[1], visitedRight[1], ctx=ctx)
        elif ctx.getChildCount() == 2:
            print(10)
            pass
        elif ctx.getChildCount() == 1:
            _thisFirstChild = _thisChildren[0]
            objToReturnAll = self.visitExpr(_thisFirstChild)
            objToReturn = objToReturnAll[0]
            classifiedObjToReturn = objToReturnAll[1]
        else:
            print("fijfoijfoi", ctx.getText(), ctx.getChildCount(), list([x.getText(), type(x).__name__] for x in _thisChildren)) 

        return objToReturn, classifiedObjToReturn
    
    
    def visitExprlist(self, ctx: pscriptParser.ExprlistContext):
        objToReturn = { "content": []}
        classifiedObjToReturn = { "content": []}

        for child in ctx.children:
            if type(child).__name__ == "ExprContext":
                _thisParsed = self.visitExpr(child)

                if list(_thisParsed[0].keys())[0] != "IDENTIFIER":
                    print("An error occured")
                    exit()

                objToReturn["content"].append(_thisParsed[0])
                classifiedObjToReturn["content"].append(_thisParsed[1])

        return objToReturn, classifiedObjToReturn
    
    def visitExpr(self, ctx:pscriptParser.ExprContext):
        _thisChildren = ctx.children 

        objToReturn = {
        }


        if ctx.getChildCount() == 3:
            _thisOp = _thisChildren[1]
            _thisLeft = _thisChildren[0]
            _thisRight = _thisChildren[2]

            visitedLeft = self.visit(_thisLeft)
            visitedRight = self.visit(_thisRight)

            if type(_thisOp).__name__ == 'TerminalNodeImpl' and _thisOp.getText() in operations.keys():
                objToReturn = operations[_thisOp.getText()](visitedLeft[0], visitedRight[0])
                classifiedObjToReturn = classes.Operation(_thisOp.getText(), visitedLeft[1], visitedRight[1], ctx=ctx)
                
            elif type(_thisLeft).__name__ == 'TerminalNodeImpl' and _thisLeft.getText() == "await":
                objToReturn = {
                    "Await": {
                        "to_await": None
                    }
                }
                classifiedObjToReturn = classes.Await(ctx=ctx)

                thisVisitedIdentifier = self.visit(_thisOp)
                thisVisitedIdentifier[0]["trailers"] = [visitedRight[0]]
                thisVisitedIdentifier[1].trailers = [visitedRight[1]]

                objToReturn["Await"]["to_await"] = thisVisitedIdentifier[0]
                classifiedObjToReturn.to_await = thisVisitedIdentifier[1]
                
            else:
                thisVisitedOp = self.visit(_thisOp)
                objToReturnAll = self.visit(_thisLeft)
                objToReturn = objToReturnAll[0]
                objToReturn["trailers"] = [] 
                objToReturn["trailers"].append(thisVisitedOp[0])
                objToReturn["trailers"].append(visitedRight[0])

                classifiedObjToReturn = objToReturnAll[1]
                classifiedObjToReturn.trailers = []
                classifiedObjToReturn.trailers.append(thisVisitedOp[1])
                classifiedObjToReturn.trailers.append(visitedRight[1])


        elif ctx.getChildCount() == 2:
            _thisFirstChild = _thisChildren[0]
            _thisSecondChild = _thisChildren[1]

            if type(_thisFirstChild).__name__ == "TerminalNodeImpl":

                _thisOp = _thisFirstChild.getText()
                _thisLeft = {
                    "Number": {
                        "value": 0,
                        "isNegative": False,
                        "isFloat": False
                    }
                }
                _thisRight = _thisSecondChild
                thisVisitedRight = self.visit(_thisRight)
  
                objToReturn = operations[_thisOp](_thisLeft, thisVisitedRight[0])
                classifiedObjToReturn = classes.Operation(_thisOp, classes.Number(0, False, False, ctx=ctx), thisVisitedRight[1], ctx=ctx)
                
            elif type(_thisFirstChild).__name__ == "AtomContext":
                _thisVisitedTrailer = self.visitTrailer(_thisSecondChild)
                objToReturnAll = self.visitAtom(_thisFirstChild)
                objToReturn = objToReturnAll[0]
                objToReturn[list(objToReturn.keys())[0]]["trailers"] = [_thisVisitedTrailer[0]]
                classifiedObjToReturn = objToReturnAll[1]
                classifiedObjToReturn.trailers = [_thisVisitedTrailer[1]]


        elif ctx.getChildCount() == 1:
            _thisFirstChild = _thisChildren[0]
            objToReturnAll = self.visit(_thisFirstChild)
            objToReturn = objToReturnAll[0]
            classifiedObjToReturn = objToReturnAll[1]

        else:
            _thisFirstChild = _thisChildren[0]
            objToReturnAll = self.visit(_thisFirstChild)
            objToReturn = objToReturnAll[0]
            classifiedObjToReturn = objToReturnAll[1]

            _thisChildTrailers = _thisChildren[1::]
            objToReturn[list(objToReturn.keys())[0]]["trailers"] = []
            classifiedObjToReturn.trailers = []

            for trailerInd, trailer in enumerate(_thisChildTrailers):
                thisVisitedTrailer = self.visitTrailer(trailer)
                objToReturn[list(objToReturn.keys())[0]]["trailers"].append(thisVisitedTrailer[0])
                classifiedObjToReturn.trailers.append(thisVisitedTrailer[1])

        
        return objToReturn, classifiedObjToReturn
    
    def visitTrailer(self, ctx: pscriptParser.TrailerContext):

        objToReturn = {

        }

        _thisChildren = ctx.children 
        _thisChildrenCount = ctx.getChildCount()

        if _thisChildrenCount == 3:
            _thisFirstChild = _thisChildren[0]
            _thisSecondChild = _thisChildren[1]
            _thisThirdChild = _thisChildren[2]

            if _thisFirstChild.getText() == ".":
                objToReturnAll = self.visit(_thisSecondChild)
                objToReturn = objToReturnAll[0]
                classifiedObjToReturn = objToReturnAll[1]
                thisVisitedTrailer = self.visit(_thisThirdChild)
                objToReturn[list(objToReturn.keys())[0]]["trailers"] = [thisVisitedTrailer[0]]

                classifiedObjToReturn.trailers = [thisVisitedTrailer[1]]
                
            else:
                print("An error occured.")
                exit()

        elif _thisChildrenCount == 2:
            _thisFirstChild = _thisChildren[0]
            _thisSecondChild = _thisChildren[1]

            if type(_thisFirstChild).__name__ == "TerminalNodeImpl":
                if type(_thisSecondChild).__name__ == "TerminalNodeImpl":
                    print("An error occured.")
                    exit()

                objToReturnAll = self.visit(_thisSecondChild)
                objToReturn = objToReturnAll[0]
                classifiedObjToReturn = objToReturnAll[1]


        elif _thisChildrenCount == 1:
            _thisChild = _thisChildren[0]
            objToReturnAll = self.visit(_thisChild)
            objToReturn = objToReturnAll[0]
            classifiedObjToReturn = objToReturnAll[1]


        return objToReturn, classifiedObjToReturn
    
    def visitArguments(self, ctx: pscriptParser.ArgumentsContext):
        _thisChildren = ctx.children

        if ctx.getChildCount() == 3:
            if _thisChildren[0].getText() == "(":
                objToReturnAll = self.visit(_thisChildren[1])
                objToReturn = objToReturnAll[0]
            elif _thisChildren[0].getText() == "[":
                objToReturnAll = self.visit(_thisChildren[1])
                objToReturn = objToReturnAll[0]

            classifiedObjToReturn = objToReturnAll[1]

        elif ctx.getChildCount() == 2:
            if _thisChildren[0].getText() == "(":
                objToReturn = {
                    "Function_Call_Arguments": []
                }

                classifiedObjToReturn = classes.Function_Call_Arguments(ctx=ctx)

            elif _thisChildren[0].getText() == "[":
                print("Invalid indexing.")
                exit()

        return objToReturn, classifiedObjToReturn
    
    def visitSubscriptlist(self, ctx: pscriptParser.SubscriptlistContext):
        _thisChildren = ctx.children

        objToReturnAll = self.visit(_thisChildren[0])

        objToReturn = {
            "Subscript": objToReturnAll[0]
        }

        if list(objToReturn.keys())[0] == "Subscript":
            classifiedObjToReturn = objToReturnAll[1]
        elif list(objToReturn.keys())[0] == "Indexing":
            classifiedObjToReturn = objToReturnAll[1]

        return objToReturn, classifiedObjToReturn
    
    def visitSubscript(self, ctx: pscriptParser.SubscriptContext):
        _thisChildren = ctx.children

        if len(_thisChildren) > 5 or len(_thisChildren) == 0:
            print("An error occurred")
            exit()

        objToReturn = {
            "Subscript": {
                "start": None,
                "end": None, 
                "step": {
                    "Number": {
                        "value": 1,
                        "isNegative": False,
                        "isFloat": False
                    }
                }
            }
        }

        classifiedObjToReturn = classes.Subscript(ctx=ctx)

        if len(_thisChildren) == 1:
            _thisChild = _thisChildren[0] 
            if _thisChild.getText() == ":":
                objToReturn["Subscript"]["start"] = {
                    "Number": {
                        "value": 0,
                        "isNegative": False,
                        "isFloat": False
                    }
                }

                objToReturn["Subscript"]["end"] = {
                    "Number": {
                        "value": -1,
                        "isNegative": True,
                        "isFloat": False
                    }
                }

                classifiedObjToReturn.start = classes.Number(value=0, isNegative=False, ctx=ctx)
                classifiedObjToReturn.end = classes.Number(value=-1, isNegative=True, ctx=ctx)

            else:
                thisValue = self.visit(_thisChild)
                objToReturn = {
                    "Indexing": thisValue[0]
                }

                classifiedObjToReturn = classes.Indexing(value=thisValue[1], ctx=ctx)
        else:
            objToReturn = {
                "Subscript": {
                    "start": {
                        "Number": {
                            "value": 0,
                            "isNegative": False,
                            "isFloat": False
                        }
                    },
                    "end": {
                        "Number": {
                            "value": -1,
                            "isNegative": True,
                            "isFloat": False
                        }
                    }, 
                    "step": {
                        "Number": {
                            "value": 1,
                            "isNegative": False,
                            "isFloat": False
                        }
                    }
                }
            }

            thisTests = ctx.test()
            thisSliceops = ctx.sliceop()

            thisSliceOpsTexts = []
            if thisSliceops != None:
                visitedSliceOp = self.visit(thisSliceops.children[1])
                objToReturn["Subscript"]["step"] = visitedSliceOp[0]
                classifiedObjToReturn.step = visitedSliceOp[1]
                thisSliceOpsTexts.append(thisSliceops.getText()) 

            if len(thisTests) == 1:
                visitedTest = self.visit(thisTests[0])
                objToReturn["Subscript"]["start"] = visitedTest[0]
                classifiedObjToReturn.start = visitedTest[1]
            elif len(thisTests) == 2:
                visitedFirstTest = self.visit(thisTests[0])
                visitedSecondTest = self.visit(thisTests[1])
                objToReturn["Subscript"]["start"] = visitedFirstTest[0]
                objToReturn["Subscript"]["end"] = visitedSecondTest[0]

                classifiedObjToReturn.start = visitedFirstTest[1]
                classifiedObjToReturn.end = visitedSecondTest[1]

            

        return objToReturn, classifiedObjToReturn
    
    def visitArglist(self, ctx: pscriptParser.ArglistContext):
        
        objToReturn = {
            "Function_Call_Arguments": []
        }

        classifiedObjToReturn = classes.Function_Call_Arguments(ctx=ctx)


        thisArguments = ctx.argument() 
        classifiedVisitedArguments = []

        for _child in thisArguments: 
            if type(_child).__name__ != "TerminalNodeImpl":
                _thisValue = self.visit(_child)
                objToReturn["Function_Call_Arguments"].append(_thisValue[0])
                classifiedVisitedArguments.append(_thisValue[1])

        classifiedObjToReturn.arguments = classifiedVisitedArguments
        
        return objToReturn, classifiedObjToReturn
    
    def visitArgument(self, ctx: pscriptParser.ArgumentContext):
        objToReturn = { 
            "Argument": {
                "name": None,
                "value": None
            }
        }

        classifiedObjToReturn = classes.Argument(None, None, ctx=ctx)

        _thisChildren = ctx.children

        if ctx.getChildCount() == 3:
            if _thisChildren[1].getText() == "=":
                thisVisitedName = self.visit(_thisChildren[0])
                thisVisitedValue = self.visit(_thisChildren[2])

                objToReturn["Argument"]["name"] = thisVisitedName[0]
                objToReturn["Argument"]["value"] = thisVisitedValue[0]
                classifiedObjToReturn.name = thisVisitedName[1]
                classifiedObjToReturn.value = thisVisitedValue[1]
            else:
                print("An error occured.")
                exit()
        elif ctx.getChildCount() == 1:
            thisVisitedValue = self.visit(_thisChildren[0])
            objToReturn["Argument"]["value"] = thisVisitedValue[0]
            classifiedObjToReturn.value = thisVisitedValue[1]

        return objToReturn, classifiedObjToReturn
    
    
    def visitAtom(self, ctx:pscriptParser.AtomContext):
        _thisChildren = ctx.children

        objToReturn = {

        }

        if ctx.getChildCount() == 3:
            _thisFirstChild = _thisChildren[0]
            _thisSecondChild = _thisChildren[1]
            _thisThirdChild = _thisChildren[2]

            if _thisFirstChild.getText() == "(":
                if type(_thisSecondChild).__name__ == "TestlistContext":
                    _thisContents = self.visit(_thisSecondChild)

                    objToReturn = {
                        "Tuple": {
                            "contents": _thisContents[0]["contents"]
                        }
                    }
                    objToReturnClassified = classes.Tuple(_thisContents[1].contents, ctx=ctx)

            elif _thisFirstChild.getText() == "{":
                if type(_thisSecondChild).__name__ == "DictmakerContext":
                    objToReturnAll = self.visit(_thisSecondChild)
                    objToReturn = objToReturnAll[0]
                    objToReturnClassified = objToReturnAll[1]

                elif type(_thisSecondChild).__name__ == "SetmakerContext":
                    objToReturnAll = self.visit(_thisSecondChild)
                    objToReturn = objToReturnAll[0]
                    objToReturnClassified = objToReturnAll[1]

                else:
                    print("Herre")
                    exit()

            elif _thisFirstChild.getText() == "[":
                _thisContents = self.visit(_thisSecondChild)
                objToReturn = {
                    "Array": {
                        "contents": _thisContents[0]["contents"]
                    }
                }

                objToReturnClassified = classes.Array(_thisContents[1].contents, ctx=ctx)
            
            else:
                print("Herre")
                exit()

        elif ctx.getChildCount() == 2:
            thisFirstChild = _thisChildren[0]
            if thisFirstChild.getText() in ["-"]:
                left = {
                    "Number": {
                        "value": -1,
                        "isNegative": True,
                        "isFloat": False
                    }
                }
                right = self.visit(_thisChildren[1])
                objToReturn = operations["*"](left, right[0])

                objToReturnClassified = classes.Operation("*", classes.Number(-1, True, False, ctx=ctx), right[1], ctx=ctx)
            
            elif thisFirstChild.getText() in ["{"]:
                #Fix here, make it return a dict manually

                objToReturn = {
                    "Dict":{
                        "contents": [

                        ]
                    }
                }

                objToReturnClassified = classes.Dict(ctx=thisFirstChild)
            
            elif thisFirstChild.getText() in ["["]:
                objToReturn = {
                    "Array": [

                    ]
                }
                objToReturnClassified = classes.Array(ctx=thisFirstChild)

                
            else:
                print("Herre")
                exit()

        elif ctx.getChildCount() == 1:
            _thisChildType = type(_thisChildren[0]).__name__

            thisString = ctx.STRING()
            thisNone = ctx.NONE()
            
            if _thisChildType == "TerminalNodeImpl":
               
                if thisString != None:
                    if _thisChildren[0].getText()[0] in ['\'', '\"', '`']:
                        _thisPrefixes = []
                        _thisValue = _thisChildren[0].getText()

                    else:
                        _origValue = _thisChildren[0].getText()

                        _thisPrefixes = []

                        currentCharInd = 0
                        currentChar = _origValue[currentCharInd]

                        
                        while (currentChar in ['\'', '\"', '`']) == False:
                            _thisPrefixes.append(currentChar.lower())
                            currentCharInd += 1 
                            currentChar = _origValue[currentCharInd]

                        _thisValue = _origValue[currentCharInd::]

                    thisOpeningQoute = _thisValue[0]
                    currentCharInd = 0
                    currentChar = thisOpeningQoute 

                    openingQouteCount = 0
                    while currentChar == thisOpeningQoute and currentCharInd <= len(_thisValue)-2:
                        openingQouteCount += 1

                        currentCharInd += 1 
                        currentChar = _thisValue[currentCharInd]


                    _thisValue = _thisValue[openingQouteCount:(openingQouteCount*-1)]
                    

                    objToReturn = {
                        "String": {
                            "value": _thisValue,
                            "prefixes": _thisPrefixes
                        }
                    }

                    objToReturnClassified = classes.String(_thisValue, prefixes=_thisPrefixes, ctx=ctx)

                elif thisNone != None:

                    objToReturn = { "IDENTIFIER": { "name": "undefined" } }
                    objToReturnClassified = classes.IDENTIFIER(name="undefined", ctx=ctx)
                        
                else:
                    _thisValue = _thisChildren[0].getText()

                    objToReturn = {
                        "String": {
                            "value": _thisValue
                        }
                    }
                    objToReturnClassified = classes.String(_thisValue, ctx=ctx)

            elif _thisChildType == "NumberContext":
                objToReturnAll = self.visitNumber(_thisChildren[0])
                objToReturn = objToReturnAll[0]
                objToReturnClassified = objToReturnAll[1]

            elif _thisChildType == "NameContext":
                objToReturnAll = self.visitName(_thisChildren[0])
                objToReturn = objToReturnAll[0]
                objToReturnClassified = objToReturnAll[1]

            elif _thisChildType == "BoolContext":
                objToReturnAll = self.visitBool(_thisChildren[0])
                objToReturn = objToReturnAll[0]
                objToReturnClassified = objToReturnAll[1]

            else:
                print(_thisChildType)
                exit()
        else:
            print(_thisChildren, ctx.getChildCount())
            exit()


        return objToReturn, objToReturnClassified
    
    def visitSetmaker(self, ctx: pscriptParser.SetmakerContext):
        objToReturn = {
            "Set": {
                "contents": [

                ]
            }
        }
        objToReturnClassified = classes.Set(ctx=ctx)

        _thisChildren = ctx.children 

        for _child in _thisChildren: 
            if type(_child).__name__ != "TerminalNodeImpl":
                _thisValue = self.visit(_child)
                objToReturn["Set"]["contents"] = _thisValue[0]["contents"]
                objToReturnClassified.contents = _thisValue[1].contents
            else:
                continue

        return objToReturn, objToReturnClassified
    
    
    def visitDictmaker(self, ctx: pscriptParser.DictmakerContext):
        objToReturn = {
            "Dict":{
                "contents": [

                ]
            }
        }

        objToReturnClassified = classes.Dict(ctx=ctx)

        thisDictItems = ctx.dictItem()

        for thisItem in thisDictItems:
            thisItemKey = thisItem.dictKey()
            thisItemValue = thisItem.test()

            thisVisitedKey = self.visit(thisItemKey)
            thisVisitedValue = self.visit(thisItemValue)

            _thisValue = {
                "key": thisVisitedKey[0],
                "value": thisVisitedValue[0]
            }

            objToReturn["Dict"]["contents"].append(_thisValue)
            objToReturnClassified.contents.append({
                "key": thisVisitedKey[1],
                "value": thisVisitedValue[1]
            })

        return objToReturn, objToReturnClassified
    
    def visitDictKey(self, ctx:pscriptParser.DictKeyContext):
        thisString = ctx.STRING()
        _thisChildren = ctx.children

        _thisChild = _thisChildren[0]
        _thisChildType = type(thisString).__name__


        if _thisChildType == "TerminalNodeImpl":
               
            if thisString != None:
                if _thisChild.getText()[0] in ['\'', '\"', '`']:
                    _thisPrefixes = []
                    _thisValue = _thisChild.getText()

                else:
                    _origValue = _thisChild.getText()

                    _thisPrefixes = []

                    currentCharInd = 0
                    currentChar = _origValue[currentCharInd]

                    
                    while (currentChar in ['\'', '\"', '`']) == False:
                        _thisPrefixes.append(currentChar.lower())
                        currentCharInd += 1 
                        currentChar = _origValue[currentCharInd]

                    _thisValue = _origValue[currentCharInd::]

                thisOpeningQoute = _thisValue[0]
                currentCharInd = 0
                currentChar = thisOpeningQoute 

                openingQouteCount = 0
                while currentChar == thisOpeningQoute and currentCharInd <= len(_thisValue)-2:
                    openingQouteCount += 1

                    currentCharInd += 1 
                    currentChar = _thisValue[currentCharInd]


                _thisValue = _thisValue[openingQouteCount:(openingQouteCount*-1)]
                
                objToReturn = {
                    "String": {
                        "value": _thisValue,
                        "prefixes": _thisPrefixes
                    }
                }

                objToReturnClassified = classes.String(_thisValue, prefixes=_thisPrefixes, ctx=ctx)

            else:
                print("This dict string key is none")
                exit()
        else:
            _thisValue = _thisChild.getText()

            objToReturn = {
                "String": {
                    "value": _thisValue,
                    "prefixes": []
                }
            }

            objToReturnClassified = classes.String(_thisValue, prefixes=[], ctx=ctx)

        return objToReturn, objToReturnClassified
    
    def visitTestlist(self, ctx:pscriptParser.TestlistContext):
        objToReturn = {"contents": []}
        classifiedObjToReturn = classes.Testlist(ctx=ctx)
        classifiedTestlistContents = []

        for test in ctx.test(): 
            thisVisitedChild = self.visit(test)

            objToReturn["contents"].append(thisVisitedChild[0])
            classifiedTestlistContents.append(thisVisitedChild[1])

        classifiedObjToReturn.contents = classifiedTestlistContents


        return objToReturn, classifiedObjToReturn
    

    
    def visitName(self, ctx: pscriptParser.NameContext):
        _thisChildren = ctx.children

        objToReturnClassified = classes.IDENTIFIER(ctx=ctx)

        objectToReturn = {
            "IDENTIFIER": {
                "name": None,
            }
        }
        
        thisNameText = ctx.getText()

        if ctx.getChildCount() == 2:
            print(1)
        elif ctx.getChildCount() == 1:
            if type(_thisChildren[0]).__name__ == "BoolContext":
                objectToReturn = self.visitBool(_thisChildren[0])

            elif type(_thisChildren[0]).__name__ == "TerminalNodeImpl":
                objectToReturn = {
                    "IDENTIFIER": {
                        "name": thisNameText,
                    }
                }
                
            objToReturnClassified.name = thisNameText
        else:
            print("Gigoigj")

        return objectToReturn, objToReturnClassified
    
    def visitBool(self, ctx: pscriptParser.BoolContext):
        _thisBoolText = ctx.getText().lower()

        isTrue = False if _thisBoolText == "false" else True
        objToReturn = {
            "Bool": {
                "isTrue": isTrue
            }
        }

        objToReturnClassified = classes.Bool(isTrue, ctx=ctx)

        return objToReturn

    def visitNumber(self, ctx: pscriptParser.NumberContext):
        _thisChildren = ctx.children

        _thisNumberType = type(_thisChildren[0]).__name__

        classifiedObjToReturn = classes.Number(ctx=ctx)

        if _thisNumberType == "TerminalNodeImpl":
            numberValue = float(_thisChildren[0].getText())
            objToReturn = {
                "Number": {
                    "value": numberValue,
                    "isNegative": False,
                    "isFloat": True
                }
            }

            classifiedObjToReturn.value = numberValue  
            classifiedObjToReturn.isNegative = False 
            classifiedObjToReturn.isFloat = True

        elif _thisNumberType == "IntegerContext":

            objToReturnAll = self.visitInteger(_thisChildren[0])
            objToReturn = objToReturnAll[0]
            classifiedObjToReturn = objToReturnAll[1]

        return objToReturn, classifiedObjToReturn

    def visitInteger(self, ctx: pscriptParser.IntegerContext):
        _thisNumberText = ctx.children[0].getText()


        if len(_thisNumberText) > 2:
            if _thisNumberText.startswith('0x'):
                _thisNumber = float.fromhex(_thisNumberText)
            elif _thisNumberText.startswith('0o'):
                _thisNumber = float(int(_thisNumberText, 8))
            elif _thisNumberText.startswith('0b'):
                _thisNumber =  float(int(_thisNumberText, 2))
            else:
                _thisNumber = float(_thisNumberText)
        else:
            try:
                _thisNumber = round(float(_thisNumberText))
            except Exception as e:
                print(f"An error occured. {e}")
                exit()


        objToReturn = { 
            "Number": {
                "value": _thisNumber,
                "isNegative": False,
                "isFloat": False
            } 
        }

        classifiedObjToReturn = classes.Number(value=_thisNumber, isNegative=False, isFloat=False, ctx=ctx)
                
        return objToReturn, classifiedObjToReturn
        