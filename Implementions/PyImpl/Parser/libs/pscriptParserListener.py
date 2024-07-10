# Generated from ./pscriptParser.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .pscriptParser import pscriptParser
else:
    from pscriptParser import pscriptParser

# This class defines a complete listener for a parse tree produced by pscriptParser.
class pscriptParserListener(ParseTreeListener):

    # Enter a parse tree produced by pscriptParser#root.
    def enterRoot(self, ctx:pscriptParser.RootContext):
        pass

    # Exit a parse tree produced by pscriptParser#root.
    def exitRoot(self, ctx:pscriptParser.RootContext):
        pass


    # Enter a parse tree produced by pscriptParser#single_input.
    def enterSingle_input(self, ctx:pscriptParser.Single_inputContext):
        pass

    # Exit a parse tree produced by pscriptParser#single_input.
    def exitSingle_input(self, ctx:pscriptParser.Single_inputContext):
        pass


    # Enter a parse tree produced by pscriptParser#file_input.
    def enterFile_input(self, ctx:pscriptParser.File_inputContext):
        pass

    # Exit a parse tree produced by pscriptParser#file_input.
    def exitFile_input(self, ctx:pscriptParser.File_inputContext):
        pass


    # Enter a parse tree produced by pscriptParser#eval_input.
    def enterEval_input(self, ctx:pscriptParser.Eval_inputContext):
        pass

    # Exit a parse tree produced by pscriptParser#eval_input.
    def exitEval_input(self, ctx:pscriptParser.Eval_inputContext):
        pass


    # Enter a parse tree produced by pscriptParser#stmt.
    def enterStmt(self, ctx:pscriptParser.StmtContext):
        pass

    # Exit a parse tree produced by pscriptParser#stmt.
    def exitStmt(self, ctx:pscriptParser.StmtContext):
        pass


    # Enter a parse tree produced by pscriptParser#if_stmt.
    def enterIf_stmt(self, ctx:pscriptParser.If_stmtContext):
        pass

    # Exit a parse tree produced by pscriptParser#if_stmt.
    def exitIf_stmt(self, ctx:pscriptParser.If_stmtContext):
        pass


    # Enter a parse tree produced by pscriptParser#while_stmt.
    def enterWhile_stmt(self, ctx:pscriptParser.While_stmtContext):
        pass

    # Exit a parse tree produced by pscriptParser#while_stmt.
    def exitWhile_stmt(self, ctx:pscriptParser.While_stmtContext):
        pass


    # Enter a parse tree produced by pscriptParser#for_stmt.
    def enterFor_stmt(self, ctx:pscriptParser.For_stmtContext):
        pass

    # Exit a parse tree produced by pscriptParser#for_stmt.
    def exitFor_stmt(self, ctx:pscriptParser.For_stmtContext):
        pass


    # Enter a parse tree produced by pscriptParser#try_stmt.
    def enterTry_stmt(self, ctx:pscriptParser.Try_stmtContext):
        pass

    # Exit a parse tree produced by pscriptParser#try_stmt.
    def exitTry_stmt(self, ctx:pscriptParser.Try_stmtContext):
        pass


    # Enter a parse tree produced by pscriptParser#with_stmt.
    def enterWith_stmt(self, ctx:pscriptParser.With_stmtContext):
        pass

    # Exit a parse tree produced by pscriptParser#with_stmt.
    def exitWith_stmt(self, ctx:pscriptParser.With_stmtContext):
        pass


    # Enter a parse tree produced by pscriptParser#class_def_stmt.
    def enterClass_def_stmt(self, ctx:pscriptParser.Class_def_stmtContext):
        pass

    # Exit a parse tree produced by pscriptParser#class_def_stmt.
    def exitClass_def_stmt(self, ctx:pscriptParser.Class_def_stmtContext):
        pass


    # Enter a parse tree produced by pscriptParser#func_def_stmt.
    def enterFunc_def_stmt(self, ctx:pscriptParser.Func_def_stmtContext):
        pass

    # Exit a parse tree produced by pscriptParser#func_def_stmt.
    def exitFunc_def_stmt(self, ctx:pscriptParser.Func_def_stmtContext):
        pass


    # Enter a parse tree produced by pscriptParser#suite.
    def enterSuite(self, ctx:pscriptParser.SuiteContext):
        pass

    # Exit a parse tree produced by pscriptParser#suite.
    def exitSuite(self, ctx:pscriptParser.SuiteContext):
        pass


    # Enter a parse tree produced by pscriptParser#decorator.
    def enterDecorator(self, ctx:pscriptParser.DecoratorContext):
        pass

    # Exit a parse tree produced by pscriptParser#decorator.
    def exitDecorator(self, ctx:pscriptParser.DecoratorContext):
        pass


    # Enter a parse tree produced by pscriptParser#elif_clause.
    def enterElif_clause(self, ctx:pscriptParser.Elif_clauseContext):
        pass

    # Exit a parse tree produced by pscriptParser#elif_clause.
    def exitElif_clause(self, ctx:pscriptParser.Elif_clauseContext):
        pass


    # Enter a parse tree produced by pscriptParser#else_clause.
    def enterElse_clause(self, ctx:pscriptParser.Else_clauseContext):
        pass

    # Exit a parse tree produced by pscriptParser#else_clause.
    def exitElse_clause(self, ctx:pscriptParser.Else_clauseContext):
        pass


    # Enter a parse tree produced by pscriptParser#finally_clause.
    def enterFinally_clause(self, ctx:pscriptParser.Finally_clauseContext):
        pass

    # Exit a parse tree produced by pscriptParser#finally_clause.
    def exitFinally_clause(self, ctx:pscriptParser.Finally_clauseContext):
        pass


    # Enter a parse tree produced by pscriptParser#with_item.
    def enterWith_item(self, ctx:pscriptParser.With_itemContext):
        pass

    # Exit a parse tree produced by pscriptParser#with_item.
    def exitWith_item(self, ctx:pscriptParser.With_itemContext):
        pass


    # Enter a parse tree produced by pscriptParser#except_clause.
    def enterExcept_clause(self, ctx:pscriptParser.Except_clauseContext):
        pass

    # Exit a parse tree produced by pscriptParser#except_clause.
    def exitExcept_clause(self, ctx:pscriptParser.Except_clauseContext):
        pass


    # Enter a parse tree produced by pscriptParser#classdef.
    def enterClassdef(self, ctx:pscriptParser.ClassdefContext):
        pass

    # Exit a parse tree produced by pscriptParser#classdef.
    def exitClassdef(self, ctx:pscriptParser.ClassdefContext):
        pass


    # Enter a parse tree produced by pscriptParser#funcdef.
    def enterFuncdef(self, ctx:pscriptParser.FuncdefContext):
        pass

    # Exit a parse tree produced by pscriptParser#funcdef.
    def exitFuncdef(self, ctx:pscriptParser.FuncdefContext):
        pass


    # Enter a parse tree produced by pscriptParser#typedargslist.
    def enterTypedargslist(self, ctx:pscriptParser.TypedargslistContext):
        pass

    # Exit a parse tree produced by pscriptParser#typedargslist.
    def exitTypedargslist(self, ctx:pscriptParser.TypedargslistContext):
        pass


    # Enter a parse tree produced by pscriptParser#args.
    def enterArgs(self, ctx:pscriptParser.ArgsContext):
        pass

    # Exit a parse tree produced by pscriptParser#args.
    def exitArgs(self, ctx:pscriptParser.ArgsContext):
        pass


    # Enter a parse tree produced by pscriptParser#kwargs.
    def enterKwargs(self, ctx:pscriptParser.KwargsContext):
        pass

    # Exit a parse tree produced by pscriptParser#kwargs.
    def exitKwargs(self, ctx:pscriptParser.KwargsContext):
        pass


    # Enter a parse tree produced by pscriptParser#def_parameters.
    def enterDef_parameters(self, ctx:pscriptParser.Def_parametersContext):
        pass

    # Exit a parse tree produced by pscriptParser#def_parameters.
    def exitDef_parameters(self, ctx:pscriptParser.Def_parametersContext):
        pass


    # Enter a parse tree produced by pscriptParser#def_parameter.
    def enterDef_parameter(self, ctx:pscriptParser.Def_parameterContext):
        pass

    # Exit a parse tree produced by pscriptParser#def_parameter.
    def exitDef_parameter(self, ctx:pscriptParser.Def_parameterContext):
        pass


    # Enter a parse tree produced by pscriptParser#named_parameter.
    def enterNamed_parameter(self, ctx:pscriptParser.Named_parameterContext):
        pass

    # Exit a parse tree produced by pscriptParser#named_parameter.
    def exitNamed_parameter(self, ctx:pscriptParser.Named_parameterContext):
        pass


    # Enter a parse tree produced by pscriptParser#simple_stmt.
    def enterSimple_stmt(self, ctx:pscriptParser.Simple_stmtContext):
        pass

    # Exit a parse tree produced by pscriptParser#simple_stmt.
    def exitSimple_stmt(self, ctx:pscriptParser.Simple_stmtContext):
        pass


    # Enter a parse tree produced by pscriptParser#variable_def_stmt.
    def enterVariable_def_stmt(self, ctx:pscriptParser.Variable_def_stmtContext):
        pass

    # Exit a parse tree produced by pscriptParser#variable_def_stmt.
    def exitVariable_def_stmt(self, ctx:pscriptParser.Variable_def_stmtContext):
        pass


    # Enter a parse tree produced by pscriptParser#func_call_stmt.
    def enterFunc_call_stmt(self, ctx:pscriptParser.Func_call_stmtContext):
        pass

    # Exit a parse tree produced by pscriptParser#func_call_stmt.
    def exitFunc_call_stmt(self, ctx:pscriptParser.Func_call_stmtContext):
        pass


    # Enter a parse tree produced by pscriptParser#del_stmt.
    def enterDel_stmt(self, ctx:pscriptParser.Del_stmtContext):
        pass

    # Exit a parse tree produced by pscriptParser#del_stmt.
    def exitDel_stmt(self, ctx:pscriptParser.Del_stmtContext):
        pass


    # Enter a parse tree produced by pscriptParser#pass_stmt.
    def enterPass_stmt(self, ctx:pscriptParser.Pass_stmtContext):
        pass

    # Exit a parse tree produced by pscriptParser#pass_stmt.
    def exitPass_stmt(self, ctx:pscriptParser.Pass_stmtContext):
        pass


    # Enter a parse tree produced by pscriptParser#break_stmt.
    def enterBreak_stmt(self, ctx:pscriptParser.Break_stmtContext):
        pass

    # Exit a parse tree produced by pscriptParser#break_stmt.
    def exitBreak_stmt(self, ctx:pscriptParser.Break_stmtContext):
        pass


    # Enter a parse tree produced by pscriptParser#continue_stmt.
    def enterContinue_stmt(self, ctx:pscriptParser.Continue_stmtContext):
        pass

    # Exit a parse tree produced by pscriptParser#continue_stmt.
    def exitContinue_stmt(self, ctx:pscriptParser.Continue_stmtContext):
        pass


    # Enter a parse tree produced by pscriptParser#return_stmt.
    def enterReturn_stmt(self, ctx:pscriptParser.Return_stmtContext):
        pass

    # Exit a parse tree produced by pscriptParser#return_stmt.
    def exitReturn_stmt(self, ctx:pscriptParser.Return_stmtContext):
        pass


    # Enter a parse tree produced by pscriptParser#raise_stmt.
    def enterRaise_stmt(self, ctx:pscriptParser.Raise_stmtContext):
        pass

    # Exit a parse tree produced by pscriptParser#raise_stmt.
    def exitRaise_stmt(self, ctx:pscriptParser.Raise_stmtContext):
        pass


    # Enter a parse tree produced by pscriptParser#yield_stmt.
    def enterYield_stmt(self, ctx:pscriptParser.Yield_stmtContext):
        pass

    # Exit a parse tree produced by pscriptParser#yield_stmt.
    def exitYield_stmt(self, ctx:pscriptParser.Yield_stmtContext):
        pass


    # Enter a parse tree produced by pscriptParser#import_stmt.
    def enterImport_stmt(self, ctx:pscriptParser.Import_stmtContext):
        pass

    # Exit a parse tree produced by pscriptParser#import_stmt.
    def exitImport_stmt(self, ctx:pscriptParser.Import_stmtContext):
        pass


    # Enter a parse tree produced by pscriptParser#from_import_stmt.
    def enterFrom_import_stmt(self, ctx:pscriptParser.From_import_stmtContext):
        pass

    # Exit a parse tree produced by pscriptParser#from_import_stmt.
    def exitFrom_import_stmt(self, ctx:pscriptParser.From_import_stmtContext):
        pass


    # Enter a parse tree produced by pscriptParser#global_stmt.
    def enterGlobal_stmt(self, ctx:pscriptParser.Global_stmtContext):
        pass

    # Exit a parse tree produced by pscriptParser#global_stmt.
    def exitGlobal_stmt(self, ctx:pscriptParser.Global_stmtContext):
        pass


    # Enter a parse tree produced by pscriptParser#assert_stmt.
    def enterAssert_stmt(self, ctx:pscriptParser.Assert_stmtContext):
        pass

    # Exit a parse tree produced by pscriptParser#assert_stmt.
    def exitAssert_stmt(self, ctx:pscriptParser.Assert_stmtContext):
        pass


    # Enter a parse tree produced by pscriptParser#nonlocal_stmt.
    def enterNonlocal_stmt(self, ctx:pscriptParser.Nonlocal_stmtContext):
        pass

    # Exit a parse tree produced by pscriptParser#nonlocal_stmt.
    def exitNonlocal_stmt(self, ctx:pscriptParser.Nonlocal_stmtContext):
        pass


    # Enter a parse tree produced by pscriptParser#variable_def.
    def enterVariable_def(self, ctx:pscriptParser.Variable_defContext):
        pass

    # Exit a parse tree produced by pscriptParser#variable_def.
    def exitVariable_def(self, ctx:pscriptParser.Variable_defContext):
        pass


    # Enter a parse tree produced by pscriptParser#variable_def_name.
    def enterVariable_def_name(self, ctx:pscriptParser.Variable_def_nameContext):
        pass

    # Exit a parse tree produced by pscriptParser#variable_def_name.
    def exitVariable_def_name(self, ctx:pscriptParser.Variable_def_nameContext):
        pass


    # Enter a parse tree produced by pscriptParser#variable_def_comma_name.
    def enterVariable_def_comma_name(self, ctx:pscriptParser.Variable_def_comma_nameContext):
        pass

    # Exit a parse tree produced by pscriptParser#variable_def_comma_name.
    def exitVariable_def_comma_name(self, ctx:pscriptParser.Variable_def_comma_nameContext):
        pass


    # Enter a parse tree produced by pscriptParser#from_where.
    def enterFrom_where(self, ctx:pscriptParser.From_whereContext):
        pass

    # Exit a parse tree produced by pscriptParser#from_where.
    def exitFrom_where(self, ctx:pscriptParser.From_whereContext):
        pass


    # Enter a parse tree produced by pscriptParser#comma_name.
    def enterComma_name(self, ctx:pscriptParser.Comma_nameContext):
        pass

    # Exit a parse tree produced by pscriptParser#comma_name.
    def exitComma_name(self, ctx:pscriptParser.Comma_nameContext):
        pass


    # Enter a parse tree produced by pscriptParser#comma_test.
    def enterComma_test(self, ctx:pscriptParser.Comma_testContext):
        pass

    # Exit a parse tree produced by pscriptParser#comma_test.
    def exitComma_test(self, ctx:pscriptParser.Comma_testContext):
        pass


    # Enter a parse tree produced by pscriptParser#variable_def_consts.
    def enterVariable_def_consts(self, ctx:pscriptParser.Variable_def_constsContext):
        pass

    # Exit a parse tree produced by pscriptParser#variable_def_consts.
    def exitVariable_def_consts(self, ctx:pscriptParser.Variable_def_constsContext):
        pass


    # Enter a parse tree produced by pscriptParser#variable_def_consts_with_colon.
    def enterVariable_def_consts_with_colon(self, ctx:pscriptParser.Variable_def_consts_with_colonContext):
        pass

    # Exit a parse tree produced by pscriptParser#variable_def_consts_with_colon.
    def exitVariable_def_consts_with_colon(self, ctx:pscriptParser.Variable_def_consts_with_colonContext):
        pass


    # Enter a parse tree produced by pscriptParser#testlist_star_expr.
    def enterTestlist_star_expr(self, ctx:pscriptParser.Testlist_star_exprContext):
        pass

    # Exit a parse tree produced by pscriptParser#testlist_star_expr.
    def exitTestlist_star_expr(self, ctx:pscriptParser.Testlist_star_exprContext):
        pass


    # Enter a parse tree produced by pscriptParser#star_expr.
    def enterStar_expr(self, ctx:pscriptParser.Star_exprContext):
        pass

    # Exit a parse tree produced by pscriptParser#star_expr.
    def exitStar_expr(self, ctx:pscriptParser.Star_exprContext):
        pass


    # Enter a parse tree produced by pscriptParser#assign_part.
    def enterAssign_part(self, ctx:pscriptParser.Assign_partContext):
        pass

    # Exit a parse tree produced by pscriptParser#assign_part.
    def exitAssign_part(self, ctx:pscriptParser.Assign_partContext):
        pass


    # Enter a parse tree produced by pscriptParser#exprlist.
    def enterExprlist(self, ctx:pscriptParser.ExprlistContext):
        pass

    # Exit a parse tree produced by pscriptParser#exprlist.
    def exitExprlist(self, ctx:pscriptParser.ExprlistContext):
        pass


    # Enter a parse tree produced by pscriptParser#import_as_names.
    def enterImport_as_names(self, ctx:pscriptParser.Import_as_namesContext):
        pass

    # Exit a parse tree produced by pscriptParser#import_as_names.
    def exitImport_as_names(self, ctx:pscriptParser.Import_as_namesContext):
        pass


    # Enter a parse tree produced by pscriptParser#import_as_name.
    def enterImport_as_name(self, ctx:pscriptParser.Import_as_nameContext):
        pass

    # Exit a parse tree produced by pscriptParser#import_as_name.
    def exitImport_as_name(self, ctx:pscriptParser.Import_as_nameContext):
        pass


    # Enter a parse tree produced by pscriptParser#name_as_names.
    def enterName_as_names(self, ctx:pscriptParser.Name_as_namesContext):
        pass

    # Exit a parse tree produced by pscriptParser#name_as_names.
    def exitName_as_names(self, ctx:pscriptParser.Name_as_namesContext):
        pass


    # Enter a parse tree produced by pscriptParser#name_as_name.
    def enterName_as_name(self, ctx:pscriptParser.Name_as_nameContext):
        pass

    # Exit a parse tree produced by pscriptParser#name_as_name.
    def exitName_as_name(self, ctx:pscriptParser.Name_as_nameContext):
        pass


    # Enter a parse tree produced by pscriptParser#test.
    def enterTest(self, ctx:pscriptParser.TestContext):
        pass

    # Exit a parse tree produced by pscriptParser#test.
    def exitTest(self, ctx:pscriptParser.TestContext):
        pass


    # Enter a parse tree produced by pscriptParser#varargslist.
    def enterVarargslist(self, ctx:pscriptParser.VarargslistContext):
        pass

    # Exit a parse tree produced by pscriptParser#varargslist.
    def exitVarargslist(self, ctx:pscriptParser.VarargslistContext):
        pass


    # Enter a parse tree produced by pscriptParser#vardef_parameters.
    def enterVardef_parameters(self, ctx:pscriptParser.Vardef_parametersContext):
        pass

    # Exit a parse tree produced by pscriptParser#vardef_parameters.
    def exitVardef_parameters(self, ctx:pscriptParser.Vardef_parametersContext):
        pass


    # Enter a parse tree produced by pscriptParser#vardef_parameter.
    def enterVardef_parameter(self, ctx:pscriptParser.Vardef_parameterContext):
        pass

    # Exit a parse tree produced by pscriptParser#vardef_parameter.
    def exitVardef_parameter(self, ctx:pscriptParser.Vardef_parameterContext):
        pass


    # Enter a parse tree produced by pscriptParser#varargs.
    def enterVarargs(self, ctx:pscriptParser.VarargsContext):
        pass

    # Exit a parse tree produced by pscriptParser#varargs.
    def exitVarargs(self, ctx:pscriptParser.VarargsContext):
        pass


    # Enter a parse tree produced by pscriptParser#varkwargs.
    def enterVarkwargs(self, ctx:pscriptParser.VarkwargsContext):
        pass

    # Exit a parse tree produced by pscriptParser#varkwargs.
    def exitVarkwargs(self, ctx:pscriptParser.VarkwargsContext):
        pass


    # Enter a parse tree produced by pscriptParser#logical_test.
    def enterLogical_test(self, ctx:pscriptParser.Logical_testContext):
        pass

    # Exit a parse tree produced by pscriptParser#logical_test.
    def exitLogical_test(self, ctx:pscriptParser.Logical_testContext):
        pass


    # Enter a parse tree produced by pscriptParser#comparison.
    def enterComparison(self, ctx:pscriptParser.ComparisonContext):
        pass

    # Exit a parse tree produced by pscriptParser#comparison.
    def exitComparison(self, ctx:pscriptParser.ComparisonContext):
        pass


    # Enter a parse tree produced by pscriptParser#expr.
    def enterExpr(self, ctx:pscriptParser.ExprContext):
        pass

    # Exit a parse tree produced by pscriptParser#expr.
    def exitExpr(self, ctx:pscriptParser.ExprContext):
        pass


    # Enter a parse tree produced by pscriptParser#atom.
    def enterAtom(self, ctx:pscriptParser.AtomContext):
        pass

    # Exit a parse tree produced by pscriptParser#atom.
    def exitAtom(self, ctx:pscriptParser.AtomContext):
        pass


    # Enter a parse tree produced by pscriptParser#dictmaker.
    def enterDictmaker(self, ctx:pscriptParser.DictmakerContext):
        pass

    # Exit a parse tree produced by pscriptParser#dictmaker.
    def exitDictmaker(self, ctx:pscriptParser.DictmakerContext):
        pass


    # Enter a parse tree produced by pscriptParser#dictItem.
    def enterDictItem(self, ctx:pscriptParser.DictItemContext):
        pass

    # Exit a parse tree produced by pscriptParser#dictItem.
    def exitDictItem(self, ctx:pscriptParser.DictItemContext):
        pass


    # Enter a parse tree produced by pscriptParser#dictKey.
    def enterDictKey(self, ctx:pscriptParser.DictKeyContext):
        pass

    # Exit a parse tree produced by pscriptParser#dictKey.
    def exitDictKey(self, ctx:pscriptParser.DictKeyContext):
        pass


    # Enter a parse tree produced by pscriptParser#setmaker.
    def enterSetmaker(self, ctx:pscriptParser.SetmakerContext):
        pass

    # Exit a parse tree produced by pscriptParser#setmaker.
    def exitSetmaker(self, ctx:pscriptParser.SetmakerContext):
        pass


    # Enter a parse tree produced by pscriptParser#testlist.
    def enterTestlist(self, ctx:pscriptParser.TestlistContext):
        pass

    # Exit a parse tree produced by pscriptParser#testlist.
    def exitTestlist(self, ctx:pscriptParser.TestlistContext):
        pass


    # Enter a parse tree produced by pscriptParser#dotted_name.
    def enterDotted_name(self, ctx:pscriptParser.Dotted_nameContext):
        pass

    # Exit a parse tree produced by pscriptParser#dotted_name.
    def exitDotted_name(self, ctx:pscriptParser.Dotted_nameContext):
        pass


    # Enter a parse tree produced by pscriptParser#name.
    def enterName(self, ctx:pscriptParser.NameContext):
        pass

    # Exit a parse tree produced by pscriptParser#name.
    def exitName(self, ctx:pscriptParser.NameContext):
        pass


    # Enter a parse tree produced by pscriptParser#bool.
    def enterBool(self, ctx:pscriptParser.BoolContext):
        pass

    # Exit a parse tree produced by pscriptParser#bool.
    def exitBool(self, ctx:pscriptParser.BoolContext):
        pass


    # Enter a parse tree produced by pscriptParser#number.
    def enterNumber(self, ctx:pscriptParser.NumberContext):
        pass

    # Exit a parse tree produced by pscriptParser#number.
    def exitNumber(self, ctx:pscriptParser.NumberContext):
        pass


    # Enter a parse tree produced by pscriptParser#integer.
    def enterInteger(self, ctx:pscriptParser.IntegerContext):
        pass

    # Exit a parse tree produced by pscriptParser#integer.
    def exitInteger(self, ctx:pscriptParser.IntegerContext):
        pass


    # Enter a parse tree produced by pscriptParser#yield_expr.
    def enterYield_expr(self, ctx:pscriptParser.Yield_exprContext):
        pass

    # Exit a parse tree produced by pscriptParser#yield_expr.
    def exitYield_expr(self, ctx:pscriptParser.Yield_exprContext):
        pass


    # Enter a parse tree produced by pscriptParser#yield_arg.
    def enterYield_arg(self, ctx:pscriptParser.Yield_argContext):
        pass

    # Exit a parse tree produced by pscriptParser#yield_arg.
    def exitYield_arg(self, ctx:pscriptParser.Yield_argContext):
        pass


    # Enter a parse tree produced by pscriptParser#trailer.
    def enterTrailer(self, ctx:pscriptParser.TrailerContext):
        pass

    # Exit a parse tree produced by pscriptParser#trailer.
    def exitTrailer(self, ctx:pscriptParser.TrailerContext):
        pass


    # Enter a parse tree produced by pscriptParser#arguments.
    def enterArguments(self, ctx:pscriptParser.ArgumentsContext):
        pass

    # Exit a parse tree produced by pscriptParser#arguments.
    def exitArguments(self, ctx:pscriptParser.ArgumentsContext):
        pass


    # Enter a parse tree produced by pscriptParser#arglist.
    def enterArglist(self, ctx:pscriptParser.ArglistContext):
        pass

    # Exit a parse tree produced by pscriptParser#arglist.
    def exitArglist(self, ctx:pscriptParser.ArglistContext):
        pass


    # Enter a parse tree produced by pscriptParser#argument.
    def enterArgument(self, ctx:pscriptParser.ArgumentContext):
        pass

    # Exit a parse tree produced by pscriptParser#argument.
    def exitArgument(self, ctx:pscriptParser.ArgumentContext):
        pass


    # Enter a parse tree produced by pscriptParser#subscriptlist.
    def enterSubscriptlist(self, ctx:pscriptParser.SubscriptlistContext):
        pass

    # Exit a parse tree produced by pscriptParser#subscriptlist.
    def exitSubscriptlist(self, ctx:pscriptParser.SubscriptlistContext):
        pass


    # Enter a parse tree produced by pscriptParser#subscript.
    def enterSubscript(self, ctx:pscriptParser.SubscriptContext):
        pass

    # Exit a parse tree produced by pscriptParser#subscript.
    def exitSubscript(self, ctx:pscriptParser.SubscriptContext):
        pass


    # Enter a parse tree produced by pscriptParser#sliceop.
    def enterSliceop(self, ctx:pscriptParser.SliceopContext):
        pass

    # Exit a parse tree produced by pscriptParser#sliceop.
    def exitSliceop(self, ctx:pscriptParser.SliceopContext):
        pass


    # Enter a parse tree produced by pscriptParser#comp_for.
    def enterComp_for(self, ctx:pscriptParser.Comp_forContext):
        pass

    # Exit a parse tree produced by pscriptParser#comp_for.
    def exitComp_for(self, ctx:pscriptParser.Comp_forContext):
        pass


    # Enter a parse tree produced by pscriptParser#comp_iter.
    def enterComp_iter(self, ctx:pscriptParser.Comp_iterContext):
        pass

    # Exit a parse tree produced by pscriptParser#comp_iter.
    def exitComp_iter(self, ctx:pscriptParser.Comp_iterContext):
        pass



del pscriptParser