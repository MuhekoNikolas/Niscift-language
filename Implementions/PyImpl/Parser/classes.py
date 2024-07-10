
import math, os, sys, json, importlib, types

import prodClasses

from prodClassesDir._PyPiSearch import PyPiSearch
#from pointers import _, to_var_ptr, NULL

class VariableScope:
    def __init__(self):
        _undefinedClassObj = prodClasses._Undefined
        _noneClassObj = prodClasses._None
        _trueClassObj = prodClasses._True

        self.preDefinedVariables = ["None", "null", "undefined", "False", "false", "True", "true"]
        self.reservedKeywords = ["if", "elif", "else", "for", "while"] + self.preDefinedVariables

        self.variables = {
            "undefined": _undefinedClassObj,
            "None": _noneClassObj,
            "null": _noneClassObj,
            "true": _trueClassObj,
            "True": _trueClassObj,

        }

    def checkNameStringIsReservedKeyword(self, namesString):
        
        thisTrimmedNameString = namesString[2:-2]

        if thisTrimmedNameString in self.reservedKeywords:
            return {
                "success": False,
                "errorType": "ReservedConstantError",
                "message": f"Variable '{thisTrimmedNameString}' is a reserved keyword.",
            }
        else:
            return {
                "success": True
            }
    

    def addVariable(self, namesString, value, isFirst=False, ____isConstant____=False, ctx=None):

        isReservedKeyword = self.checkNameStringIsReservedKeyword(namesString)
        if isReservedKeyword["success"] != True:
            return isReservedKeyword
        
        try:

            splittedNames = namesString.split("]")
            if splittedNames[-1] == "":
                splittedNames.pop()

            if isFirst == True:
                
                if (len(splittedNames) >= 2) == False:
                    if type(value) == dict:
                        thisValueKeys = value.keys()
                        
                        if len(thisValueKeys) == 2 and "____isConstant____" in thisValueKeys and "____value____" in thisValueKeys:
                            value = value["____value____"]

                        else:
                            value = {
                                "____isConstant____": ____isConstant____,
                                "____value____": value
                            }
                    else:
                        value = {
                            "____isConstant____": ____isConstant____,
                            "____value____": value
                        }


            _thisExecDump = {
                "variables": self.variables,
                "value": value,
                "splittedNames": splittedNames,
                "currentVal": self.variables
            }
            
            currentObj = self.variables
            addedCurrentString = ""
            for _nInd, _n in enumerate(splittedNames):
                if _nInd == len(splittedNames)-1:
                    continue

                thisIndexString = _n + "]"
                addedCurrentString+=thisIndexString

                temp = {
                    "variables": self.variables,
                    "currentObj": currentObj,
                    "prodClasses": prodClasses,
                    "os": os,
                    "_nInd": _nInd,
                    "addedCurrentString": addedCurrentString,
                    "ctx": ctx
                }

                exec(f"""

currentObj = variables{addedCurrentString}

if type(currentObj) == dict:
    if _nInd > 1:
        currentObj = prodClasses._Dict(ctx=ctx, contents=currentObj)
    else:
        currentObj = currentObj
    variables{addedCurrentString} = currentObj
elif type(currentObj)==type(os):
    currentObj = prodClasses._PyModule(ctx=ctx, module=currentObj)
    variables{addedCurrentString} = currentObj
else:   
    if hasattr(currentObj, "__getitem__"):
        currentObj = currentObj
    else:         
        currentObj = prodClasses._Object(ctx=ctx, obj=currentObj)
        variables{addedCurrentString} = currentObj
                """, 
                temp)


            exec(
                f"""

variables{namesString} = value
""", 
                _thisExecDump
            ) 

            self.variables = _thisExecDump["variables"]
            return {"success": True, "response":value}
        
        except Exception as err:
            exception_type, exception_object, exception_traceback = sys.exc_info()
            filename = exception_traceback.tb_frame.f_code.co_filename
            line_number = exception_traceback.tb_lineno

            print(err, line_number)
            return {"success": False, "errorType": exception_type.__name__, "message": "An error occured while setting the variable"}
        

    def _addVariable(self, name, value, ctx, root=False):
        try:
            if name in self.preDefinedVariables:
                return {
                    "success": False,
                    "errorType": "ReservedConstantError",
                    "message": f"Variable '{name}' is a reserved keyword.",
                    "ctx": ctx
                }
            else:
                thisAlreadyVariable = self.getVariable(name, root=True)

                if type(thisAlreadyVariable) != dict:
                    thisAlreadyVariable = {
                        "____isConstant____": False,
                        "____value____": thisAlreadyVariable
                    }

                if thisAlreadyVariable["____isConstant____"] == True:
                    return {
                        "success": False,
                        "errorType": "Constant_DefinitionError",
                        "message": f'Cannot redefine a constant value "{name}".',
                        "ctx": ctx
                    } 
                
                if root == True:
                    value = {
                        "____isConstant____": False,
                        "____value____": value
                    }


                self.variables[name] = value

                return {
                    "success": True
                }
        
        except Exception as err:
            return {
                "success": False,
                "errorType": "PythonicError",
                "message": err,
                "ctx": ctx
            }

        
    def getRawVariableWithStringName(self, namesString, ctx):
        try:
            _thisExecDump = {
                "variables": self.variables,
                "foundVariable": self.variables["undefined"](ctx=ctx),
            }
            exec(f"""foundVariable = variables{namesString}""", _thisExecDump)
            
            return {"success": True, "response":_thisExecDump["foundVariable"]}
        
        except Exception as e:
            return {"success": False, "errorType": "PythonicError", "message": "An error occured while getting the variable", "ctx": ctx}
        
    def getVariableWithStringName(self, namesString, ctx):
        splittedNameStringOld = namesString.split(']')
        if splittedNameStringOld[-1] == "":
            splittedNameStringOld.pop()

        splittedNameString = list(x+"]" for x in splittedNameStringOld if len(x) != 0)

        ____isConstant____ = False 

        if splittedNameString[-1] in ['["____value____"]', "['____value____']"]:

            splittedNameString.pop()

            thisLastCurrentNameString = "".join(x for x in splittedNameString)

            thisRawVariable = self.getRawVariableWithStringName(thisLastCurrentNameString, ctx=ctx)

            if thisRawVariable["success"] != True:
                return {
                    "success": False,
                    "message": thisRawVariable["message"]
                }
            
            thisRawVariable = thisRawVariable["response"]

            if thisRawVariable["____isConstant____"] == True:
                ____isConstant____ = True

        try:
            _thisExecDump = {
                "variables": self.variables,
                "foundVariable": self.variables["undefined"](ctx=ctx),
            }

            exec(f"""foundVariable = variables{namesString}""", _thisExecDump) 

            return {"success": True, "response":{"____isConstant____": ____isConstant____, "response": _thisExecDump["foundVariable"]}}
        
        except KeyError as e:
            print(e, type(e), "ff")
            return {"success": False, "errorType": "KeyError", "message": f"Invalid Key: {json.dumps(err.args[0])}."}
        
        except TypeError as e:
            return {"success": False, "errorType": "TypeError", "message": "Invalid indexing."}
        
        except Exception as e:
            print(e)
            return {"success": False, "errorType": "PythonicError", "message": "An error occured while getting the variable"}


    def getVariable(self, name, root=False):

        try:
            if name in self.preDefinedVariables or root==True:
                return self.variables[name]
            else:
                return self.variables[name]["____value____"]
        
        except KeyError:
            return prodClasses._Undefined(ctx=None)
        
        except Exception as err:
            print(err)
            return prodClasses._Undefined( ctx=None)
        

class PscriptObj:
    def __init__(self, ctx=None):
        self.ctx = ctx
        pass 

    def run(self, root, localScope=None):
        pass

class Root(PscriptObj):
    def __init__(self, statements=[], ctx=None):
        super().__init__()
        self.statements = statements
        self.ctx = ctx

        self.variableScope = VariableScope()
    
    def run(self, errorManager):
        localScope = self.variableScope

        for statement in self.statements:
            thisRanStatement = statement.run(root=self, localScope=localScope)

            if thisRanStatement["success"] != True:
                thisErrorType = thisRanStatement["errorType"]
                thisErrorMessage = thisRanStatement["message"]
                thisErrorCtx = thisRanStatement["ctx"]

                errorManager.invokeError(errorType=thisErrorType, errorMessage=thisErrorMessage, errorCtx=thisErrorCtx)

class Stmt(PscriptObj):
    def __init__(self, isSimpleStatement, _isCompoundStatement, ctx=None):
        super().__init__()
        self.isSimpleStatement = isSimpleStatement
        self.isCompountStatement = _isCompoundStatement
        self.statement = []

        self.ctx = ctx
    
    def run(self, root, localScope):

        if type(self.statement).__name__ == 'list':
            for statement in self.statement:

                thisRanResp = statement.run(root, localScope)

                if type(thisRanResp).__name__ != 'NoneType':
                    if thisRanResp["success"] != True:
                        return thisRanResp
                else:
                    print("thisRanResp is None")
                    exit()

        else:
            thisRanResp = self.statement.run(root, localScope)

        return {
            "success": True,
            "ctx": self.ctx
        }
            

class Testlist(PscriptObj):
    def __init__(self, contents=[], ctx=None):
        super().__init__()
        self.contents = contents
        self.ctx = ctx

        self.parsedValue = None

    def getParsedValue(self, root, localScope):
        _parsedContents = [] 

        if self.parsedValue != None:
            return {
                "success": True,
                "response": self.parsedValue
            }
        
        else:
            for val in self.contents:
                _thisParsedVal = val.getParsedValue(root, localScope)
                if _thisParsedVal["success"]!= True:
                    return {
                        "success": False,
                        "errorType": _thisParsedVal["errorType"],
                        "message": _thisParsedVal["message"],
                        "ctx": _thisParsedVal["ctx"]
                    }
                
                else: 
                    _thisParsedVal = _thisParsedVal["response"]
                    _parsedContents.append(_thisParsedVal)

            self.parsedValue  = _parsedContents
            
            return {
                "success": True,
                "response": _parsedContents
            }

class With(PscriptObj):
    def __init__(self, isAsync=False, with_expressions=[], suite=None, ctx=None):
        super().__init__()
        self.isAsync = isAsync
        self.with_expressions = with_expressions
        self.suite = suite
        self.ctx = ctx

class WithItem(PscriptObj):
    def __init__(self, test=None, _as=None, ctx=None):
        super().__init__()
        self.test = test
        self._as = _as
        self.ctx = ctx

class While(PscriptObj):
    def __init__(self, test=None, suite=None, ctx=None):
        super().__init__()
        self.test = test 
        self.suite = suite
        self.ctx = ctx

class For(PscriptObj):
    def __init__(self, isAsync=False, loopVariableNames=[], iterable=None, elseClause=None, suite=None, ctx=None):
        super().__init__()
        self.isAsync = isAsync
        self.loopVariableNames = loopVariableNames
        self.iterable = iterable
        self.suite = suite
        self.elseClause = elseClause
        self.ctx = ctx

class ElseClause(PscriptObj):
    def __init__(self, suite=None, ctx=None):
        super().__init__()
        self.suite = suite 
        self.ctx = ctx


class If(PscriptObj):
    def __init__(self, test, suite, elifs, elseClause, ctx=None):
        super().__init__()
        self.test = test
        self.suite = suite
        self.elifClauses = elifs
        self.elseClause = elseClause
        self.ctx = ctx
        

class ElifClause(PscriptObj):
    def __init__(self, suite=None, ctx=None):
        super().__init__()
        self.suite = suite 
        self.ctx = ctx

class Try_stmt(PscriptObj):
    def __init__(self, try_suite=None, except_clauses=[], else_clause=None, finally_clause=None, ctx=None):
        super().__init__()
        self.try_suite = try_suite
        self.except_clauses = except_clauses
        self.else_clause = else_clause
        self.finally_clause = finally_clause
        self.ctx = ctx
        
class Suite(PscriptObj):
    def __init__(self, statements=[], ctx=None):
        super().__init__()
        self.statements = statements
        self.ctx = ctx

        
class Number(PscriptObj):
    def __init__(self, value=None, isFloat=False, isNegative=False, ctx=None):
        super().__init__()
        self.value = value 
        self.isFloat = isFloat 
        self.isNegative = isNegative 
        self.ctx = ctx

        self.parsedValue = None

        
    def getParsedValue(self, root=None, localScope=None):
        if self.parsedValue!= None:
            return {"success": True, "response": self.parsedValue}
        else:
            if self.isFloat == False or math.floor(self.value) == self.value:
                self.parsedValue = prodClasses._Integer(value=math.floor(self.value), isNegative=self.isNegative, ctx=self.ctx)
            else:
                self.parsedValue = prodClasses._Float(value=self.value, isNegative=self.isNegative, ctx=self.ctx)
            
            return {
                "success": True,
                "response": self.parsedValue
            }


class Bool(PscriptObj):
    def __init__(self, isTrue, ctx=None):
        super().__init__()
        self.isTrue = isTrue
        self.ctx = ctx

class IDENTIFIER(PscriptObj):
    def __init__(self, name=None, ctx=None):
        super().__init__()
        self.name = name
        self.ctx = ctx
        self.value = None

        self.trailers = []

    def getParsedValue(self, root, localScope, thisValue=None, namesString=""):
        
        if type(self.name) == type(None):
            return {
                "success": False,
                "errorType": "TypeError",
                "message": "Identifier name returned a NoneType value.",
                "ctx": self.ctx
            }

        thisValue = thisValue or localScope.getVariable(name=self.name) or root.variableScope.getVariable(name=self.name)
        namesString = namesString + f'["{json.dumps(self.name)[1:-1]}"]'

        if type(thisValue) == prodClasses._Undefined:
            self.value = None

            return {
                "success": True,
                "response": thisValue,
                "namesString": namesString
            }
        
        if len(self.trailers) > 0:
            currentValue = thisValue 

            for tInd, t in enumerate(self.trailers):
                thisTrailerType = type(t).__name__

                match thisTrailerType:
                    case "Function_Call_Arguments":
                        if currentValue.isCallable != True:
                            return {
                                "success": False, 
                                "errorType": "TypeError",
                                "message": "Attempted to call a non-callable value.",
                                "ctx": t.ctx
                            }
                        else:
                            thisParsedArguments = t.getParsedArguments(root=root, localScope=localScope)

                            if thisParsedArguments["success"] != True:
                                return {
                                    "success": False, 
                                    "errorType": thisParsedArguments["errorType"],
                                    "message": thisParsedArguments["message"],
                                    "ctx": t.ctx
                                }
                            
                            currentValue = currentValue.____call____(arguments= thisParsedArguments["response"])
                            namesString = namesString + f'["{json.dumps(t.name)[1:-1]}"]'

                    case "IDENTIFIER":
                        #Check if current value has __dict__ key or can be indexed
                        
                        if hasattr(currentValue, "__dict__"):
                            currentValueDict = currentValue.__dict__
                        elif hasattr(currentValue, "__getitem__"):
                            currentValueDict = currentValue
                        elif hasattr(currentValue, "__vars__"):
                            currentValueDict = vars(currentValue)
                        else:
                            return {
                                "success": False,
                                "errorType": "IndexingError",
                                "message": "Invalid Indexing.",
                                "ctx": t.ctx
                            }

                        thisTrailerName = t.name
                        currentValueDictKeys = currentValueDict.keys()

                        if not thisTrailerName in currentValueDictKeys:
                            #Error here
                            currentValue = prodClasses._Undefined(ctx=t.ctx)
                            namesString = namesString + f'["{json.dumps(t.name)[1:-1]}"]'

                            #Check if there are more trailers
                            if len(t.trailers) > 0 or tInd < len(self.trailers)-1:
                                return {
                                    "success": False,
                                    "errorType": "IndexingError",
                                    "message": f"Invalid Indexing.",
                                    "ctx": t.ctx
                                }
                        
                        try:
                            currentValue = currentValueDict[thisTrailerName]
                        except KeyError as e:
                            return {
                                "success": False,
                                "errorType": "KeyError",
                                "message": f"Invalid Key: {json.dumps(err.args[0])}.",
                                "ctx": t.ctx
                            }
                        
                        namesString = namesString + f'["{json.dumps(t.name)[1:-1]}"]'
                        

                        for __trailerInd, __trailer in enumerate(t.trailers):
                            thisTrailerType = type(__trailer).__name__

                            match thisTrailerType:

                                case "IDENTIFIER":
                                    currentValue = __trailer.getParsedValue(root, localScope, thisValue)
                                    namesString = namesString + f'["{json.dumps(__trailer.name)[1:-1]}"]'

                                case "Indexing":
                                    thisAccumulatedCurrent = __trailer.get_accumulated_current_value(currentValue=currentValue, namesString=namesString, root=root, localScope=localScope)
                                    if thisAccumulatedCurrent["success"] != True:
                                        return thisAccumulatedCurrent
                                    thisAccumulatedCurrent = thisAccumulatedCurrent["response"]
                                    currentValue, namesString = thisAccumulatedCurrent

                                case default:
                                    print(default)
                                    exit()

                        
                    case "Indexing":
                        thisAccumulatedCurrent = t.get_accumulated_current_value(currentValue=currentValue, namesString=namesString, root=root, localScope=localScope)
                        if thisAccumulatedCurrent["success"] != True:
                            return thisAccumulatedCurrent
                        
                        thisAccumulatedCurrent = thisAccumulatedCurrent["response"]
                        currentValue, namesString = thisAccumulatedCurrent

                    case default:
                        currentValueDict = currentValue.__dict__
                        print(currentValueDict)
                        print(default)
                        exit()

            return {
                "success": True, 
                "response": currentValue,
                "namesString": namesString
            }
        
        else:
            self.value = thisValue
            return {
                "success": True, 
                "response": thisValue,
                "namesString": namesString
            }

    def get_as_dotted_name_string(self, current=None):
        current = current or ""

        current = current + f".{self.name}"

        for _tInd, _t in enumerate(self.trailers):
            _tType = type(_t).__name__

            match _tType:
                case "IDENTIFIER":
                    thisDottedNameResp = _t.get_as_dotted_name_string(current=current)
                    if thisDottedNameResp["success"] != True:
                        return thisDottedNameResp
                    
                    current = thisDottedNameResp["response"]
                    
                case default:
                    return {
                        "success": False,
                        "errorType": "SyntaxError",
                        "message": "Invalid property traversal.",
                        "ctx": _t.ctx
                    }

        return {
            "success": True,
            "response": current
        }

        

class Dotted_Name(PscriptObj):
    def __init__(self, names=[], ctx=None):
        super().__init__()
        self.names = names
        self.ctx = ctx

        self.namesString = None
        self.nameCurrent = None

    def get_as_dotted_name_string(self, current=None):
        current = current or ""

        for _nInd, _n in enumerate(self.names):
            _thisNType = type(_n).__name__
            match _thisNType:
                case "Dotted_Name":
                    thisDottedNameResp = _n.get_as_dotted_name_string(current=current)
                    if thisDottedNameResp["success"] != True:
                        return {
                            "success": False,
                            "errorType": thisDottedNameResp["errorType"],
                            "message": thisDottedNameResp["message"],
                            "ctx": _n.ctx
                        }
        
                    else:
                        current = thisDottedNameResp["response"]

                case "IDENTIFIER":
                    thisDottedNameResp = _n.get_as_dotted_name_string(current=current)
                    if thisDottedNameResp["success"] != True:
                        return  {
                            "success": False,
                            "errorType": thisDottedNameResp["errorType"],
                            "message": thisDottedNameResp["message"],
                            "ctx": _n.ctx
                        }
                    
                    else:
                        current = thisDottedNameResp["response"]

        return {
            "success": True, 
            "response": current
        }


    def as_name_string(self, current=None, isFirstName=False, isLastName=False, root=None, localScope=None):
        #Error not here

        # if self.namesString != None:
        #     return {
        #         "success": True, 
        #         "response": [self.namesString, self.nameCurrent]
        #     }
        
        namesString = ""
        for nameIndex, name in enumerate(self.names):
            namesLength = len(self.names)

            _thisIsFirstName = nameIndex == 0
            _thisIsLastName = nameIndex == namesLength - 1

            if type(name).__name__ == 'Dotted_Name':
                _thisDottedName = name.as_name_string(current=current, isFirstName=_thisIsFirstName, isLastName=_thisIsLastName, root=root, localScope=localScope)

                if _thisDottedName["success"] != True:
                    #CHeck if its the last name, if it is then just proceed, else throw the error
                    return {
                        "success": False, 
                        "errorType": _thisDottedName["errorType"],
                        "message": _thisDottedName["message"],
                        "ctx": _thisDottedName["ctx"]
                    }
                
                _thisDottedNameResp = _thisDottedName["response"]
                namesString = namesString + _thisDottedNameResp[0]
                current = _thisDottedNameResp[1]

            elif type(name).__name__ == 'IDENTIFIER':
                if type(current).__name__ == 'dict':
                    #Check if the dict has thisIdentifier name in keys 
                    thisIdentifierName = name.name
                    isInKeys = thisIdentifierName in current.keys()

                    if isInKeys == False:
                        #Return invalid property or indexing error.
                        #CHeck if its the last name, if it is then just proceed, else throw the error
                        if isLastName==True and _thisIsLastName == True:
                            thisCurrentKeys = current.keys()
                            if "____value____" in thisCurrentKeys and "____isConstant____" in thisCurrentKeys: 
                                current = current["____value____"]

                            current[thisIdentifierName] = prodClasses._Undefined(ctx=name.ctx)
                            current = current[thisIdentifierName]

                            namesString = namesString + f'["{json.dumps(thisIdentifierName)[1:-1]}"]'
                        
                        else:
                            return {
                                "success": False, 
                                "errorType": "KeyError",
                                "message": f'Invalid Key: {json.dumps(thisIdentifierName)}.',
                                "ctx": name.ctx
                            }
                    else:
                        
                        oldCurrent = current
                        current = current[thisIdentifierName]
                        
                        if _thisIsFirstName:
                            if type(current).__name__ == "dict":
                                thisCurrentKeys = current.keys()
                            else:
                                return {
                                    "success": False,
                                    "errorType": "InabnormalError",
                                    "message": f"Something went wrong.",
                                    "ctx": name.ctx
                                }
                            
                            if "____value____" in thisCurrentKeys and "____isConstant____" in thisCurrentKeys:
                                current = current["____value____"]

                                if type(current).__name__ == "_Dict":
                                    current = current.contents

                                namesString = namesString + f'["{json.dumps(thisIdentifierName)[1:-1]}"]' + '["____value____"]'
                                
                            else:
                                namesString = namesString + f'["{json.dumps(thisIdentifierName)[1:-1]}"]' 

                        else:
                            namesString = namesString + f'["{json.dumps(thisIdentifierName)[1:-1]}"]'
                
                else:
                    currentValue = name.getParsedValue(root=root, localScope=localScope, thisValue=current, namesString=namesString)

                    if currentValue["success"] != True:
                        return {
                            "success": False,
                            "errorType": currentValue["errorType"],
                            "message": currentValue["message"],
                            "ctx": name.ctx
                        }
                    

                    current = currentValue["response"]
                    namesString = currentValue["namesString"]
                    #exit()


        self.namesString = namesString

        return {"success": True, "response": [namesString, current]} 

class NameAsName(PscriptObj):
    def __init__(self, initial=None, _as=None, ctx=None):
        super().__init__()
        self.initial = initial 
        self._as = _as or initial
        self.ctx = ctx

class String(PscriptObj):
    def __init__(self, value="", prefixes=[], ctx=None):
        super().__init__()
        self.value = value
        self.ctx = ctx

        self.prefixes = prefixes
        self.toBeFormatted = True if "f" in self.prefixes else False

        self.parsedValue = None

    def getParsedValue(self, root=None, localScope=None):
        if self.parsedValue!= None:
            return {
                "success": True, 
                "response": self.parsedValue
            }
        
        else:
        
            #if self.toBeFormatted != True:
            if True:
                self.parsedValue = prodClasses._String(value=self.value, ctx=self.ctx)
                return {
                    "success": True, 
                    "response": self.parsedValue
                }

            else:
                #Format the string here.
                return {
                    "success": True, 
                    "response": self.parsedValue
                }
                _thisExecNamespace = {}

            return {
                "success": False, 
                "errorType": "TypeError",
                "message": f'Invalid String "{self.value}"',
                "ctx": self.ctx
            }


class Dict(PscriptObj):
    def __init__(self, ctx=None):
        super().__init__()
        self.contents = []
        self.ctx = ctx

        self.parsedValue = None

    def getParsedValue(self, root, localScope):
        if self.parsedValue!= None:
            return {
                "success": True, 
                "response": self.parsedValue
            }
        
        thisDict = {}

        for cont in self.contents:

            thisKey = cont["key"]
            thisParsedValue = cont["value"].getParsedValue(root=root, localScope=localScope)

            if thisParsedValue["success"] != True:
                return {
                    "success": False, 
                    "errorType": thisParsedValue["errorType"],
                    "message": thisParsedValue["message"],
                    "ctx": thisParsedValue["ctx"]
                }
            
            thisParsedValue = thisParsedValue["response"]   

            match type(thisKey).__name__:
                case "IDENTIFIER":
                    thisParsedKey = f"{thisKey.name}"
                case "Number":
                    _thisVal = thisKey.getParsedValue()

                    if _thisVal["success"] != True:
                        return {
                            "success": False, 
                            "errorType": _thisVal["errorType"],
                            "message": _thisVal["message"],
                            "ctx": _thisVal["ctx"]
                        }
                    
                    _thisVal = _thisVal["response"]
                    thisParsedKey = f"{_thisVal}"

                case "String":
                    _thisVal = thisKey.getParsedValue()
                    if _thisVal["success"] != True:
                        return {
                            "success": False, 
                            "errorType": _thisVal["errorType"],
                            "message": _thisVal["message"],
                            "ctx": _thisVal["ctx"]
                        }
                    
                    _thisVal = _thisVal["response"]
                    thisParsedKey = f"{_thisVal}"
                
            thisDict[thisParsedKey] = thisParsedValue

        self.parsedValue = prodClasses._Dict(contents=thisDict, ctx=self.ctx)

        return {
            "success": True, 
            "response": self.parsedValue
        }

class Set(PscriptObj):
    def __init__(self, ctx=None):
        super().__init__()
        self.contents = []
        self.ctx = ctx

class Tuple(PscriptObj):
    def __init__(self, contents=[], ctx=None):
        super().__init__()
        self.contents = contents
        self.ctx = ctx

        self.parsedValue = None


    def getParsedValue(self, root, localScope):
        _parsedContents = [] 

        if self.parsedValue != None:
            return {
                "success": True,
                "response": self.parsedValue
            }
        
        else:
            for val in self.contents:
                _thisParsedVal = val.getParsedValue(root, localScope)

                if _thisParsedVal["success"]!= True:
                    return {
                        "success": False,
                        "errorType": _thisParsedVal["errorType"],
                        "message": _thisParsedVal["message"],
                        "ctx": _thisParsedVal["ctx"]
                    }
                
                else: 
                    _thisParsedVal = _thisParsedVal["response"]
                    _parsedContents.append(_thisParsedVal)

            self.parsedValue = prodClasses._Tuple(contents=_parsedContents, ctx=self.ctx)
            
            return {
                "success": True,
                "response": self.parsedValue
            }
        


class Array(PscriptObj):
    def __init__(self, contents=[], ctx=None):
        super().__init__()
        self.contents = contents
        self.ctx = ctx

        self.parsedValue = None


    def getParsedValue(self, root, localScope):
        _parsedContents = [] 

        if self.parsedValue != None:
            return {
                "success": True,
                "response": self.parsedValue
            }
        
        else:
            for val in self.contents:
                _thisParsedVal = val.getParsedValue(root, localScope)

                if _thisParsedVal["success"]!= True:
                    return {
                        "success": False,
                        "errorType": _thisParsedVal["errorType"],
                        "message": _thisParsedVal["message"],
                        "ctx": _thisParsedVal["ctx"]
                    }
                
                else: 
                    _thisParsedVal = _thisParsedVal["response"]
                    _parsedContents.append(_thisParsedVal)

            self.parsedValue = prodClasses._Array(contents=_parsedContents, ctx=self.ctx)
            
            return {
                "success": True,
                "response": self.parsedValue
            }

class Function_Call_Arguments(PscriptObj):
    def __init__(self, arguments=[], ctx=None):
        super().__init__()
        self.arguments = arguments
        self.ctx = ctx

        self.parsedArguments = None

    def getParsedArguments(self, root, localScope):

        if self.parsedArguments != None:
            return {"success": True, "response": self.parsedArguments}
        else:
            thisParsedArguments = []

            for argument in self.arguments:
                thisParsedValue = argument.getParsedValue(root=root, localScope=localScope)

                if thisParsedValue["success"]!= True:
                    return {
                        "success": False, 
                        "errorType": thisParsedValue["errorType"],
                        "message": thisParsedValue["message"],
                        "ctx": thisParsedValue["ctx"]
                    }
                

                if type(argument.name).__name__ != "NoneType":
                    if len(argument.name.trailers) > 0:
                        return {
                            "success": False, 
                            "errorType": "SyntaxError.",
                            "message": "Invalid syntax.",
                            "ctx": argument.name.ctx
                        }
                    
                thisParsedArguments.append((argument.name, thisParsedValue["response"]))

            return {"success": True, "response": thisParsedArguments}

class Decorator(PscriptObj):
    def __init__(self, name, call_args=None, ctx=None):
        super().__init__()
        self.name = name
        self.call_args = call_args
        self.ctx = ctx

class Argument(PscriptObj):
    def __init__(self, name=None, value=None, ctx=None):
        super().__init__()
        self.name = name
        self.value = value 
        self.ctx = ctx

        self.parsedValue = None

    def getParsedValue(self, root, localScope):

        argumentValue = self.value 

        if self.parsedValue != None:
            return {"success": True, "response": self.parsedValue}
        else:
            parsedValue = None

            match type(argumentValue).__name__:
                case "IDENTIFIER":
                    _parsedValue = argumentValue.getParsedValue(root=root, localScope=localScope)

                    if _parsedValue["success"]!= True:
                        return {
                            "success": False, 
                            "errorType": _parsedValue["errorType"],
                            "message": _parsedValue["message"],
                            "ctx": _parsedValue["ctx"]
                        }
                    
                    parsedValue = _parsedValue["response"]
                
                case "Number": 
                    parsedValue = argumentValue.getParsedValue()

                case other:
                    print(other, "Error on line")
                    exit()
            


            return {"success": True, "response": parsedValue}



class Subscript(PscriptObj):
    def __init__(self, start=None, end=None, step=Number(1, False, False), ctx=None):
        super().__init__()
        self.start = start
        self.end = end
        self.step = step
        self.ctx = ctx

class Indexing(PscriptObj):
    def __init__(self, value, ctx=None):
        super().__init__()
        self.value = value
        self.ctx = ctx

    def getParsedValue(self, root, localScope):

        match type(self.value).__name__:
            case "String" | "Number":
                thisParsedValue = self.value.getParsedValue()

                if thisParsedValue["success"] != True:
                    return {
                        "success": False, 
                        "errorType": thisParsedValue["errorType"],
                        "message": thisParsedValue["message"],
                        "ctx": thisParsedValue["ctx"]
                    } 
                return {"success": True, "response": thisParsedValue["response"]}
            
            
            case "IDENTIFIER":
                thisIdentifier = self.value 
                thisIdentifierValue = thisIdentifier.getParsedValue(root, localScope)

                if thisIdentifierValue["success"] != True:
                    return {
                        "success": False, 
                        "errorType": thisIdentifierValue["errorType"],
                        "message": thisIdentifierValue["message"],
                        "ctx": thisIdentifierValue["ctx"]
                    }
                
                thisIdentifierValue = thisIdentifierValue["response"]

                return {"success": True, "response": thisIdentifierValue}

            case default:
                print(default)

        return {"success": False, "errorType": "SyntaxError", "message": "Invalid syntax.", "ctx": self.value.ctx}
    
    def get_accumulated_current_value(self, currentValue, namesString, root, localScope):
        if type(currentValue).__name__ in ["_Dict", "_PyModule"]:
            currentValueDict = currentValue.__dict__
            currentValueDictKeys = list(currentValueDict.keys())

            thisParsedValue = self.getParsedValue(root=root, localScope=localScope)

            if type(thisParsedValue["response"]).__name__ == "_Undefined":
                return {
                    "success": False,
                    "errorType": "IndexingError",
                    "message": "Invalid Indexing.",
                    "ctx": self.ctx
                }
            
            thisParsedValue = thisParsedValue["response"]
            thisIndexingValue = thisParsedValue

            if type(thisIndexingValue).__name__ in ["Number", "_Integer"]:
                namesString = namesString + f'[{thisIndexingValue.value}]'
                currentValue = currentValue[thisIndexingValue.value]

            elif type(thisIndexingValue).__name__ in ["String", "_String"]:
                _thisKeyValue = json.dumps(thisIndexingValue.value)[1:-1]
                namesString = namesString + f'["{_thisKeyValue}"]'
                try:
                    currentValue = currentValueDict[self.value.value]
                except KeyError as err:
                    print(err, currentValueDict, vars(self.value), type(self).__name__, vars(self), err.args)
                    return {
                        "success": False,
                        "errorType": "KeyError",
                        "message": f"Invalid Key: {json.dumps(err.args[0])}.",
                        "ctx": self.ctx
                    }

            else:
                print(type(thisParsedValue).__name__)
                exit()

            return {"success": True, "response": [currentValue, namesString]}
            
        else:
            print(currentValue, type(currentValue), vars(self), namesString, "llllllllllllllllllllllllllllllllll")
            exit()

class Operation(PscriptObj):
    def __init__(self, operation, left, right, ctx=None):
        super().__init__()
        self.operation = operation
        self.left = left
        self.right = right
        self.ctx = ctx


class ASSIGNMENT(PscriptObj):
    def __init__(self, type, value, ctx=None):
        super().__init__()
        self.type = type
        self.value = value 
        self.ctx = ctx

    def getParsedValue(self, names, root, localScope):

        _thisParsedValue = self.value.getParsedValue(root=root, localScope=localScope)

        if _thisParsedValue["success"]!= True:
            return {
                "success": False, 
                "errorType": _thisParsedValue["errorType"],
                "message": _thisParsedValue["message"],
                "ctx": _thisParsedValue["ctx"]
            }
        
        else:
            return {
                "success": True, 
                "response": _thisParsedValue["response"]
            }




class VariableDef(PscriptObj):
    def __init__(self, variable_const="var", variable_names=[], variable_assignment=None, ctx=None):
        super().__init__()
        self.variable_const = variable_const
        self.variable_names = variable_names 
        self.assignment = variable_assignment
        self.ctx = ctx

    def run(self, root, localScope):
        thisVariableScope = root.variableScope

        calcedNames = []

        for var_name in self.variable_names:

            if self.variable_const == "const" and ( len(var_name.names[0].names) > 1 or type(var_name.names[0].names[0]).__name__ != "IDENTIFIER" ):
                return {
                    "success": False, 
                    "errorType": "Constant_DefinitionError",
                    "message": "Invalid constant definition.",
                    "ctx": var_name.ctx
                }

            calculatedGlobalName = self.getVariableNameString(root, thisVariableScope, var_name)

            if calculatedGlobalName["success"] != True:
                return {
                    "success": False, 
                    "errorType": calculatedGlobalName["errorType"],
                    "message": calculatedGlobalName["message"],
                    "ctx": calculatedGlobalName["ctx"]
                }
            
            else:
                resp = calculatedGlobalName["response"]
                resp.append(var_name.ctx)
                calcedNames.append(resp)

        parsedAssignedValuesResp = self.assignment.getParsedValue(names=calcedNames, root=root, localScope=localScope)

        if parsedAssignedValuesResp["success"]!= True:
            return {
                "success": False, 
                "errorType": parsedAssignedValuesResp["errorType"],
                "message": parsedAssignedValuesResp["message"],
                "ctx": parsedAssignedValuesResp["ctx"]
            }

        parsedAssignedValues = parsedAssignedValuesResp["response"]

        parsedAssignedValuesLength = len(parsedAssignedValues)
        calcedNamesLength = len(calcedNames)

        if len(calcedNames) != parsedAssignedValuesLength:
            #multi variable assigns here
            #Check if the parsed assigned value is an array, or tuple. If it is, then assign the variables via indexes, elses perform x = y = value

            if parsedAssignedValuesLength > 1:
                #Assigned values length is bigger than 1
                if len(calcedNames) == 1:
                    _parsedAssigngedValues = prodClasses._Tuple(ctx= calcedNames[0][2])
                    _parsedAssigngedValues.contents = parsedAssignedValues

                    parsedAssignedValues = [_parsedAssigngedValues]

                else:
                    return {
                        "success": False, 
                        "errorType": "UnpackingError",
                        "message": f"Recieved {parsedAssignedValuesLength} values to unpack, expected 1.",
                        "ctx": calcedNames[0][2]
                    }
    
            if type(parsedAssignedValues[0]).__name__ in ["_Integer", "_String"]:
                thisValue = parsedAssignedValues[0]
                for name in calcedNames:
                    nameName = name[0]  

                    if self.variable_const in ["const", "var", "let"]:

                        isFirst = False
                        ____isConstant____ = False 

                        _thisNames = var_name.names[0].names

                        if len(_thisNames) == 1:
                            thisAlreadyName = localScope.getVariableWithStringName(nameName, ctx=name[2])

                            if thisAlreadyName["success"] != True:
                                return {
                                    "success": False, 
                                    "errorType": thisAlreadyName["errorType"],
                                    "message": thisAlreadyName["message"],
                                    "ctx": name[2]
                                } 
                            
                            thisAlreadyName = thisAlreadyName["response"]

                            isFirst = True

                            if type(thisAlreadyName).__name__ == "dict" and "____isConstant____" in thisAlreadyName.keys() and thisAlreadyName["____isConstant____"] == True:
                                return {
                                    "success": False, 
                                    "errorType": "Constant_DefinitionError",
                                    "message": f'Cannot redefine a constant value "{name[2].getText()}".',
                                    "ctx": name[2]
                                }
                            
                            thisAlreadyName = thisAlreadyName["response"]

                        if self.variable_const == "const":
                            ____isConstant____ = True 

                        thisAddedVariable = localScope.addVariable(nameName, thisValue, isFirst=isFirst, ____isConstant____=____isConstant____, ctx=name[2])

                        if thisAddedVariable["success"] != True:
                            return {
                                "success": False, 
                                "errorType": thisAddedVariable["errorType"],
                                "message": thisAddedVariable["message"],
                                "ctx": name[2]
                            } 

                    else:
                        print(self.variable_const)

            elif type(parsedAssignedValues[0]).__name__ in ["_Array", "_Tuple"]:

                if len(parsedAssignedValues[0]) < calcedNamesLength:
                    return {
                        "success": False, 
                        "errorType": "UnpackingError",
                        "message": f"Couldn't unpack {calcedNamesLength} values from a collection containing {len(parsedAssignedValues[0])}.",
                        "ctx": calcedNames[0][2]
                    }

                for calcedNamesInd, name in enumerate(calcedNames):
                    if calcedNamesInd != calcedNamesLength - 1:
                        thisValue = parsedAssignedValues[0][calcedNamesInd]
                    else:
                        _thisValue = parsedAssignedValues[0][calcedNamesInd::]
                        leftItemsToUnpack = _thisValue
                        leftItemsToUnpackLength = len(_thisValue)

                        if leftItemsToUnpackLength > 1:
                            thisTuple = prodClasses._Tuple()
                            thisTuple.contents = leftItemsToUnpack
                            thisTuple.ctx = name[2]
                            thisValue = thisTuple
                        else:
                            thisValue = _thisValue[0]
                     
                    nameName = name[0]  

                    if self.variable_const in ["const", "var", "let"]:

                        isFirst = False
                        ____isConstant____ = False 

                        _thisNames = var_name.names[0].names

                        if len(_thisNames) == 1:
                            thisAlreadyName = localScope.getVariableWithStringName(nameName, ctx=name[2])

                            if thisAlreadyName["success"] != True:
                                return {
                                    "success": False, 
                                    "errorType": thisAlreadyName["errorType"],
                                    "message": thisAlreadyName["message"],
                                    "ctx": name[2]
                                } 
                            
                            thisAlreadyName = thisAlreadyName["response"]

                            isFirst = True

                            if type(thisAlreadyName).__name__ == "dict" and "____isConstant____" in thisAlreadyName.keys() and thisAlreadyName["____isConstant____"] == True:
                                return {
                                    "success": False, 
                                    "errorType": "Constant_DefinitionError",
                                    "message": f'Cannot redefine a constant value "{name[2].getText()}".',
                                    "ctx": name[2]
                                }
                            
                            thisAlreadyName = thisAlreadyName["response"]

                        if self.variable_const == "const":
                            ____isConstant____ = True 

                        thisAddedVariable = localScope.addVariable(nameName, thisValue, isFirst=isFirst, ____isConstant____=____isConstant____, ctx=name[2])

                        if thisAddedVariable["success"] != True:
                            return {
                                "success": False, 
                                "errorType": thisAddedVariable["errorType"],
                                "message": thisAddedVariable["message"],
                                "ctx": name[2]
                            } 

                    else:
                        print(self.variable_const)
            else:
                return {
                    "success": False, 
                    "errorType": "UnpackingError",
                    "message": f"Invalid value to unpack {type(parsedAssignedValues[0]).__name__}",
                    "ctx": calcedNames[0][2]
                } 

        else:
            for nIndex, name in enumerate(calcedNames):
                thisValue = parsedAssignedValues[nIndex]
                nameName = name[0]  

                if self.variable_const in ["const", "var", "let"]:

                    isFirst = False
                    ____isConstant____ = False 

                    _thisNames = var_name.names[0].names

                    if len(_thisNames) == 1:
                        thisAlreadyName = localScope.getVariableWithStringName(nameName, ctx=name[2])

                        if thisAlreadyName["success"] != True:
                            return {
                                "success": False, 
                                "errorType": thisAlreadyName["errorType"],
                                "message": thisAlreadyName["message"],
                                "ctx": name[2]
                            } 
                        
                        thisAlreadyName = thisAlreadyName["response"]

                        isFirst = True

                        if type(thisAlreadyName).__name__ == "dict" and "____isConstant____" in thisAlreadyName.keys() and thisAlreadyName["____isConstant____"] == True:
                            return {
                                "success": False, 
                                "errorType": "Constant_DefinitionError",
                                "message": f'Cannot redefine a constant value "{name[2].getText()}".',
                                "ctx": name[2]
                            }
                        
                        thisAlreadyName = thisAlreadyName["response"]

                    if self.variable_const == "const":
                        ____isConstant____ = True 

                    thisAddedVariable = localScope.addVariable(nameName, thisValue, isFirst=isFirst, ____isConstant____=____isConstant____, ctx=name[2])

                    if thisAddedVariable["success"] != True:
                        return {
                            "success": False, 
                            "errorType": thisAddedVariable["errorType"],
                            "message": thisAddedVariable["message"],
                            "ctx": name[2]
                        } 

                else:
                    print(self.variable_const)


        return {
            "success": True,
            "response": calcedNames
        }


    def getVariableNameString(self, root, localScope, name):
        #Not here
        thisNames = name.names

        current = localScope.variables
        namesString = ""

        for nIndex, n in enumerate(thisNames):
            isLastName = nIndex == len(thisNames) - 1

            if type(n).__name__ == "Dotted_Name":
                _thisDottedName = n.as_name_string(current=current, isLastName=isLastName, root=root, localScope=localScope, )
                if _thisDottedName["success"]!= True:
                    return {
                        "success": False, 
                        "errorType": _thisDottedName["errorType"],
                        "message": _thisDottedName["message"],
                        "ctx": _thisDottedName["ctx"]
                    }
                
                _thisDottedNameResp = _thisDottedName["response"]

                namesString = namesString + _thisDottedNameResp[0]

                if len(thisNames) == 1:
                    _current = _thisDottedNameResp[1]

                    if (_current != None and type(_current).__name__ != "_None") == False:
                        current = prodClasses._Undefined( ctx=n.ctx)
                        
                else:
                    current = _thisDottedNameResp[1]

                oldCurrent = current
                

            elif type(n).__name__ == "Indexing":
                oldCurrent = current
                oldNamesString = namesString
                try:
                    nParsedValue = n.getParsedValue(root, localScope)

                    if nParsedValue["success"]!= True:
                        return {
                            "success": False, 
                            "errorType": nParsedValue["errorType"],
                            "message": nParsedValue["message"],
                            "ctx": nParsedValue["ctx"]
                        }
                    
                    nParsedValue = nParsedValue["response"]

                    #Check for function calls as arguments aswell.

                    if type(nParsedValue).__name__ in ["_Integer", "_Number", "_String"]:

                        __parsedValue = nParsedValue.value

                        #Check if current is a dict, and if the current key exists in the dict 
                        if type(current).__name__ == "dict":
                            thisCurrentKeys = current.keys()

                            if type(__parsedValue).__name__ != "str":
                                return {
                                    "success": False, 
                                    "errorType": "IndexingError",
                                    "message": "Invalid Indexing.",
                                    "ctx": n.ctx
                                }
                            
                            else:
                                if __parsedValue in thisCurrentKeys:
                                    current = current[__parsedValue]

                                    if type(__parsedValue).__name__ == "int":
                                        namesString = namesString + f'[{__parsedValue}]'
                                    else:
                                        namesString = namesString + f'["{json.dumps(__parsedValue)[1:-1]}"]'
 
                                else:
                                    #Check if its last name, if not, throw error.
                                    if isLastName:
                                        current = prodClasses._Undefined( ctx=n.ctx)
                                        if type(__parsedValue).__name__ == "int":
                                            namesString = namesString + f'[{__parsedValue}]'
                                        else:
                                            namesString = namesString + f'["{json.dumps(__parsedValue)[1:-1]}"]'
                        
                                    else:
                                        return {
                                            "success": False, 
                                            "errorType": "IndexingError",
                                            "message": f"Invalid Indexing.",
                                            "ctx": n.ctx
                                        }
                        
                        else:
                            #Might need to check if the current is also an array and stuff.
                            current = current[__parsedValue]

                            if type(__parsedValue).__name__ == "int":
                                namesString = namesString + f'[{__parsedValue}]'
                            else:
                                namesString = namesString + f'["{json.dumps(__parsedValue)[1:-1]}"]'
                        
                        
                    else:
                        return {
                            "success": False, 
                            "errorType": "IndexingError",
                            "message": "Invalid Indexing.",
                            "ctx": nParsedValue.ctx
                        }

                except KeyError as err:
                    current = oldCurrent
                    namesString = oldNamesString
                    return {
                            "success": False, 
                            "errorType": "KeyError",
                            "message": f'Invalid key: {json.dumps(err.args[0])}.',
                            "ctx": nParsedValue.ctx
                    }

                except Exception as e:
                    raise e
                    return {
                            "success": False, 
                            "errorType": "PythonicError",
                            "message": e,
                            "ctx": nParsedValue.ctx
                    }

        return {
            "success": True, 
            "response": [namesString, current]
        }

        

            

    

class FunctionDef(PscriptObj):
    def __init__(self, isAsync, name, arguments=[], suite=None, ctx=None):
        super().__init__()
        self.isAsync = isAsync
        self.name = name
        self.arguments = arguments
        self.suite = suite
        self.ctx = ctx

class ClassDef(PscriptObj):
    def __init__(self, name, arguments=[], suite=None, ctx=None):
        super().__init__()
        self.name = name
        self.arguments = arguments
        self.suite = suite
        self.ctx = ctx

class Variable_def_name(PscriptObj):
    def __init__(self, names=[], ctx=None):
        self.names = []
        self.ctx = ctx

class Function_Call(PscriptObj):
    def __init__(self, isAwaited, name, arguments=Tuple(), ctx=None):
        super().__init__()
        self.isAwaited = isAwaited
        self.name = name 
        self.arguments = arguments
        self.ctx = ctx

class Global(PscriptObj):
    def __init__(self, to_globalize=[], ctx=None):
        super().__init__()
        self.to_globalize = to_globalize
        self.ctx = ctx

class NonLocal(PscriptObj):
    def __init__(self, to_non_localize=[], ctx=None):
        super().__init__()
        self.to_non_localize = to_non_localize
        self.ctx = ctx

class Assert(PscriptObj):
    def __init__(self, tests=[], ctx=None):
        super().__init__()
        self.tests = tests
        self.ctx = ctx

class Return(PscriptObj):
    def __init__(self, to_return=[], ctx=None):
        super().__init__()
        self.to_return = to_return
        self.ctx = ctx

class Yield(PscriptObj):
    def __init__(self, to_yield=[], ctx=None):
        super().__init__()
        self.to_yield = to_yield
        self.ctx = ctx

class Await(PscriptObj):
    def __init__(self, to_await=[], ctx=None):
        super().__init__()
        self.to_await = to_await
        self.ctx = ctx

class Import:
    def __init__(self, to_import=[], importCmd="import", ctx=None):
        self.to_import = to_import
        self.importCmd = importCmd
        self.ctx = ctx

    def run(self, root, localScope):
        importCmd = self.importCmd.lower()

        if importCmd == "include":
            res = self.runPyImport(root, localScope)
        else:
            res = self.runImport(root, localScope)


        return res
    
    def runPyImport(self, root, localScope):

        for importName in self.to_import:

            try:

                importPackageName = importName.initial.name
                importedPackage = importlib.import_module(importPackageName)

                # importedPackage = types.ModuleType(importPackageName, f'A copy of the {importPackageName} module')

                # for attr_name in dir(_importedPackage):
                #     if not attr_name.startswith("__"):
                #         setattr(importedPackage, attr_name, getattr(_importedPackage, attr_name))



            except ModuleNotFoundError as err:
                PyPiSearchObj = PyPiSearch()

                thisPackageInfo = PyPiSearchObj.search(importPackageName)

                if thisPackageInfo["success"] != True:
                    return {
                        "success": False,
                        "errorType": "ModuleNotFoundError",
                        "message": err,
                        "ctx": importName.ctx
                    }
                
                else:
                    #Download and install the package
                    os.system(f"pip install {importPackageName}")
                    temp = {}
                    exec(f"import {importPackageName}",temp)
                    importedPackage = temp[importedPackageName] 

                del PyPiSearchObj

        thisAsName = importName._as
        currentThisAsName = localScope.getVariable(name=thisAsName.name, root=True) or root.variableScope.getVariable(name=thisAsName.name, root=True)

        if type(currentThisAsName) != dict:
            currentThisAsName = {
                "____isConstant____": False,
                "____value____": currentThisAsName
            }

        if currentThisAsName["____isConstant____"] == True:
            return {
                "success": False,
                "errorType": "Constant_DefinitionError",
                "message": f'Cannot redefine a constant value "{thisAsName.ctx.getText()}".',
                "ctx": thisAsName.ctx
            }
        

        thisAddedVariableResp = localScope._addVariable(name=thisAsName.name, value=importedPackage, ctx=thisAsName.ctx, root=True) or root.variableScope._addVariable(name=thisAsName.name, value=importedPackage, ctx=thisAsName.ctx, root=True)

        return {"success": True}
    
    def runImport(self, root, localScope):
        print(self.importCmd, self.to_import, 2)
        return {"success": True}
    


class Import_From(PscriptObj):
    def __init__(self, from_where=[], to_import=[], importCmd="import", ctx=None):
        super().__init__()
        self.from_where = from_where 
        self.to_import = to_import
        self.importCmd = importCmd
        self.ctx = ctx

    def run(self, root, localScope):
        importCmd = self.importCmd.lower()

        if importCmd == "include":
            res = self.runPyImport(root, localScope)
        else:
            res = self.runImport(root, localScope)

        return res
    
    def runPyImport(self, root, localScope):
        _thisFromWhere = self.from_where 
        _thisFromWhereDottedNames = _thisFromWhere["dotted_names"].get_as_dotted_name_string()
        if _thisFromWhereDottedNames["success"] != True:
            return _thisFromWhereDottedNames
        _thisFromWhereDottedNames = _thisFromWhereDottedNames["response"][1:]

        _thisToImport = self.to_import
        thisImportNamesToLookBackAt = []
        _thisToImportString = ""
        for _n in _thisToImport:
            thisInitial = _n.initial.name
            thisAs = _n._as.name
            thisImportNamesToLookBackAt.append([thisAs, _n.ctx])
            if len(_thisToImportString) > 0:
                _thisToImportString += f", {thisInitial} as {thisAs}"
            else:
                _thisToImportString += f"{thisInitial} as {thisAs}"

        thisImportsTemp = {}
        _thisImportFullExecStmt = f"from {_thisFromWhereDottedNames} import {_thisToImportString}"

        try:
            exec(_thisImportFullExecStmt, thisImportsTemp)

        except ImportError as err:
            return {
                "success": False,
                "errorType": "ImportError",
                "message": err,
                "ctx": self.ctx
            }

        for _na in thisImportNamesToLookBackAt:
            _thisImportValue = thisImportsTemp[_na[0]]
            _thisAddedVariable = localScope._addVariable(name=_na[0], value=_thisImportValue, ctx=_na[1], root=True)

            if _thisAddedVariable["success"] != True:
                return _thisAddedVariable

        return {
            "success": True
        }

class Del(PscriptObj):
    def __init__(self, to_delete=[], ctx=None):
        super().__init__()
        self.to_delete = to_delete
        self.ctx = ctx

class Raise(PscriptObj):
    def __init__(self, to_raise=[], ctx=None):
        super().__init__()
        self.to_raise = to_raise
        self.ctx = ctx


class All(PscriptObj):
    def __init__(self, ctx=None):
        super().__init__()
        self.ctx = ctx
        pass    

class Break(PscriptObj):
    def __init__(self, ctx=None):
        super().__init__()
        self.ctx = ctx
        pass 

class Pass(PscriptObj):
    def __init__(self, ctx=None):
        super().__init__()
        self.ctx = ctx
        pass 

class Continue(PscriptObj):
    def __init__(self, ctx=None):
        super().__init__()
        self.ctx = ctx
        pass 
