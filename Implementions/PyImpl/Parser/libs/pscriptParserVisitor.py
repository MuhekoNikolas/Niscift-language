# Generated from ./pscriptParser.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .pscriptParser import pscriptParser
else:
    from pscriptParser import pscriptParser

# This class defines a complete generic visitor for a parse tree produced by pscriptParser.

class pscriptParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by pscriptParser#root.
    def visitRoot(self, ctx:pscriptParser.RootContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pscriptParser#single_input.
    def visitSingle_input(self, ctx:pscriptParser.Single_inputContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pscriptParser#file_input.
    def visitFile_input(self, ctx:pscriptParser.File_inputContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pscriptParser#eval_input.
    def visitEval_input(self, ctx:pscriptParser.Eval_inputContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pscriptParser#stmt.
    def visitStmt(self, ctx:pscriptParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pscriptParser#if_stmt.
    def visitIf_stmt(self, ctx:pscriptParser.If_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pscriptParser#while_stmt.
    def visitWhile_stmt(self, ctx:pscriptParser.While_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pscriptParser#for_stmt.
    def visitFor_stmt(self, ctx:pscriptParser.For_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pscriptParser#try_stmt.
    def visitTry_stmt(self, ctx:pscriptParser.Try_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pscriptParser#with_stmt.
    def visitWith_stmt(self, ctx:pscriptParser.With_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pscriptParser#class_def_stmt.
    def visitClass_def_stmt(self, ctx:pscriptParser.Class_def_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pscriptParser#func_def_stmt.
    def visitFunc_def_stmt(self, ctx:pscriptParser.Func_def_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pscriptParser#suite.
    def visitSuite(self, ctx:pscriptParser.SuiteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pscriptParser#decorator.
    def visitDecorator(self, ctx:pscriptParser.DecoratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pscriptParser#elif_clause.
    def visitElif_clause(self, ctx:pscriptParser.Elif_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pscriptParser#else_clause.
    def visitElse_clause(self, ctx:pscriptParser.Else_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pscriptParser#finally_clause.
    def visitFinally_clause(self, ctx:pscriptParser.Finally_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pscriptParser#with_item.
    def visitWith_item(self, ctx:pscriptParser.With_itemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pscriptParser#except_clause.
    def visitExcept_clause(self, ctx:pscriptParser.Except_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pscriptParser#classdef.
    def visitClassdef(self, ctx:pscriptParser.ClassdefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pscriptParser#funcdef.
    def visitFuncdef(self, ctx:pscriptParser.FuncdefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pscriptParser#typedargslist.
    def visitTypedargslist(self, ctx:pscriptParser.TypedargslistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pscriptParser#args.
    def visitArgs(self, ctx:pscriptParser.ArgsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pscriptParser#kwargs.
    def visitKwargs(self, ctx:pscriptParser.KwargsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pscriptParser#def_parameters.
    def visitDef_parameters(self, ctx:pscriptParser.Def_parametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pscriptParser#def_parameter.
    def visitDef_parameter(self, ctx:pscriptParser.Def_parameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pscriptParser#named_parameter.
    def visitNamed_parameter(self, ctx:pscriptParser.Named_parameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pscriptParser#simple_stmt.
    def visitSimple_stmt(self, ctx:pscriptParser.Simple_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pscriptParser#variable_def_stmt.
    def visitVariable_def_stmt(self, ctx:pscriptParser.Variable_def_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pscriptParser#func_call_stmt.
    def visitFunc_call_stmt(self, ctx:pscriptParser.Func_call_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pscriptParser#del_stmt.
    def visitDel_stmt(self, ctx:pscriptParser.Del_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pscriptParser#pass_stmt.
    def visitPass_stmt(self, ctx:pscriptParser.Pass_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pscriptParser#break_stmt.
    def visitBreak_stmt(self, ctx:pscriptParser.Break_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pscriptParser#continue_stmt.
    def visitContinue_stmt(self, ctx:pscriptParser.Continue_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pscriptParser#return_stmt.
    def visitReturn_stmt(self, ctx:pscriptParser.Return_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pscriptParser#raise_stmt.
    def visitRaise_stmt(self, ctx:pscriptParser.Raise_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pscriptParser#yield_stmt.
    def visitYield_stmt(self, ctx:pscriptParser.Yield_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pscriptParser#import_stmt.
    def visitImport_stmt(self, ctx:pscriptParser.Import_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pscriptParser#from_import_stmt.
    def visitFrom_import_stmt(self, ctx:pscriptParser.From_import_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pscriptParser#global_stmt.
    def visitGlobal_stmt(self, ctx:pscriptParser.Global_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pscriptParser#assert_stmt.
    def visitAssert_stmt(self, ctx:pscriptParser.Assert_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pscriptParser#nonlocal_stmt.
    def visitNonlocal_stmt(self, ctx:pscriptParser.Nonlocal_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pscriptParser#variable_def.
    def visitVariable_def(self, ctx:pscriptParser.Variable_defContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pscriptParser#variable_def_name.
    def visitVariable_def_name(self, ctx:pscriptParser.Variable_def_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pscriptParser#variable_def_comma_name.
    def visitVariable_def_comma_name(self, ctx:pscriptParser.Variable_def_comma_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pscriptParser#from_where.
    def visitFrom_where(self, ctx:pscriptParser.From_whereContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pscriptParser#comma_name.
    def visitComma_name(self, ctx:pscriptParser.Comma_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pscriptParser#comma_test.
    def visitComma_test(self, ctx:pscriptParser.Comma_testContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pscriptParser#variable_def_consts.
    def visitVariable_def_consts(self, ctx:pscriptParser.Variable_def_constsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pscriptParser#variable_def_consts_with_colon.
    def visitVariable_def_consts_with_colon(self, ctx:pscriptParser.Variable_def_consts_with_colonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pscriptParser#testlist_star_expr.
    def visitTestlist_star_expr(self, ctx:pscriptParser.Testlist_star_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pscriptParser#star_expr.
    def visitStar_expr(self, ctx:pscriptParser.Star_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pscriptParser#assign_part.
    def visitAssign_part(self, ctx:pscriptParser.Assign_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pscriptParser#exprlist.
    def visitExprlist(self, ctx:pscriptParser.ExprlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pscriptParser#import_as_names.
    def visitImport_as_names(self, ctx:pscriptParser.Import_as_namesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pscriptParser#import_as_name.
    def visitImport_as_name(self, ctx:pscriptParser.Import_as_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pscriptParser#name_as_names.
    def visitName_as_names(self, ctx:pscriptParser.Name_as_namesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pscriptParser#name_as_name.
    def visitName_as_name(self, ctx:pscriptParser.Name_as_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pscriptParser#test.
    def visitTest(self, ctx:pscriptParser.TestContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pscriptParser#varargslist.
    def visitVarargslist(self, ctx:pscriptParser.VarargslistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pscriptParser#vardef_parameters.
    def visitVardef_parameters(self, ctx:pscriptParser.Vardef_parametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pscriptParser#vardef_parameter.
    def visitVardef_parameter(self, ctx:pscriptParser.Vardef_parameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pscriptParser#varargs.
    def visitVarargs(self, ctx:pscriptParser.VarargsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pscriptParser#varkwargs.
    def visitVarkwargs(self, ctx:pscriptParser.VarkwargsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pscriptParser#logical_test.
    def visitLogical_test(self, ctx:pscriptParser.Logical_testContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pscriptParser#comparison.
    def visitComparison(self, ctx:pscriptParser.ComparisonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pscriptParser#expr.
    def visitExpr(self, ctx:pscriptParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pscriptParser#atom.
    def visitAtom(self, ctx:pscriptParser.AtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pscriptParser#dictmaker.
    def visitDictmaker(self, ctx:pscriptParser.DictmakerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pscriptParser#dictItem.
    def visitDictItem(self, ctx:pscriptParser.DictItemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pscriptParser#dictKey.
    def visitDictKey(self, ctx:pscriptParser.DictKeyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pscriptParser#setmaker.
    def visitSetmaker(self, ctx:pscriptParser.SetmakerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pscriptParser#testlist.
    def visitTestlist(self, ctx:pscriptParser.TestlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pscriptParser#dotted_name.
    def visitDotted_name(self, ctx:pscriptParser.Dotted_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pscriptParser#name.
    def visitName(self, ctx:pscriptParser.NameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pscriptParser#bool.
    def visitBool(self, ctx:pscriptParser.BoolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pscriptParser#number.
    def visitNumber(self, ctx:pscriptParser.NumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pscriptParser#integer.
    def visitInteger(self, ctx:pscriptParser.IntegerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pscriptParser#yield_expr.
    def visitYield_expr(self, ctx:pscriptParser.Yield_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pscriptParser#yield_arg.
    def visitYield_arg(self, ctx:pscriptParser.Yield_argContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pscriptParser#trailer.
    def visitTrailer(self, ctx:pscriptParser.TrailerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pscriptParser#arguments.
    def visitArguments(self, ctx:pscriptParser.ArgumentsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pscriptParser#arglist.
    def visitArglist(self, ctx:pscriptParser.ArglistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pscriptParser#argument.
    def visitArgument(self, ctx:pscriptParser.ArgumentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pscriptParser#subscriptlist.
    def visitSubscriptlist(self, ctx:pscriptParser.SubscriptlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pscriptParser#subscript.
    def visitSubscript(self, ctx:pscriptParser.SubscriptContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pscriptParser#sliceop.
    def visitSliceop(self, ctx:pscriptParser.SliceopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pscriptParser#comp_for.
    def visitComp_for(self, ctx:pscriptParser.Comp_forContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pscriptParser#comp_iter.
    def visitComp_iter(self, ctx:pscriptParser.Comp_iterContext):
        return self.visitChildren(ctx)



del pscriptParser