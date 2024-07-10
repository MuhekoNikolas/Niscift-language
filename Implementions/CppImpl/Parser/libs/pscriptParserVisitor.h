
// Generated from ./pscriptParser.g4 by ANTLR 4.13.0

#pragma once


#include "antlr4-runtime.h"
#include "pscriptParser.h"



/**
 * This class defines an abstract visitor for a parse tree
 * produced by pscriptParser.
 */
class  pscriptParserVisitor : public antlr4::tree::AbstractParseTreeVisitor {
public:

  /**
   * Visit parse trees produced by pscriptParser.
   */
    virtual std::any visitRoot(pscriptParser::RootContext *context) = 0;

    virtual std::any visitSingle_input(pscriptParser::Single_inputContext *context) = 0;

    virtual std::any visitFile_input(pscriptParser::File_inputContext *context) = 0;

    virtual std::any visitEval_input(pscriptParser::Eval_inputContext *context) = 0;

    virtual std::any visitStmt(pscriptParser::StmtContext *context) = 0;

    virtual std::any visitIf_stmt(pscriptParser::If_stmtContext *context) = 0;

    virtual std::any visitWhile_stmt(pscriptParser::While_stmtContext *context) = 0;

    virtual std::any visitFor_stmt(pscriptParser::For_stmtContext *context) = 0;

    virtual std::any visitTry_stmt(pscriptParser::Try_stmtContext *context) = 0;

    virtual std::any visitWith_stmt(pscriptParser::With_stmtContext *context) = 0;

    virtual std::any visitClass_def_stmt(pscriptParser::Class_def_stmtContext *context) = 0;

    virtual std::any visitFunc_def_stmt(pscriptParser::Func_def_stmtContext *context) = 0;

    virtual std::any visitSuite(pscriptParser::SuiteContext *context) = 0;

    virtual std::any visitDecorator(pscriptParser::DecoratorContext *context) = 0;

    virtual std::any visitElif_clause(pscriptParser::Elif_clauseContext *context) = 0;

    virtual std::any visitElse_clause(pscriptParser::Else_clauseContext *context) = 0;

    virtual std::any visitFinally_clause(pscriptParser::Finally_clauseContext *context) = 0;

    virtual std::any visitWith_item(pscriptParser::With_itemContext *context) = 0;

    virtual std::any visitExcept_clause(pscriptParser::Except_clauseContext *context) = 0;

    virtual std::any visitClassdef(pscriptParser::ClassdefContext *context) = 0;

    virtual std::any visitFuncdef(pscriptParser::FuncdefContext *context) = 0;

    virtual std::any visitTypedargslist(pscriptParser::TypedargslistContext *context) = 0;

    virtual std::any visitArgs(pscriptParser::ArgsContext *context) = 0;

    virtual std::any visitKwargs(pscriptParser::KwargsContext *context) = 0;

    virtual std::any visitDef_parameters(pscriptParser::Def_parametersContext *context) = 0;

    virtual std::any visitDef_parameter(pscriptParser::Def_parameterContext *context) = 0;

    virtual std::any visitNamed_parameter(pscriptParser::Named_parameterContext *context) = 0;

    virtual std::any visitSimple_stmt(pscriptParser::Simple_stmtContext *context) = 0;

    virtual std::any visitVariable_def_stmt(pscriptParser::Variable_def_stmtContext *context) = 0;

    virtual std::any visitFunc_call_stmt(pscriptParser::Func_call_stmtContext *context) = 0;

    virtual std::any visitDel_stmt(pscriptParser::Del_stmtContext *context) = 0;

    virtual std::any visitPass_stmt(pscriptParser::Pass_stmtContext *context) = 0;

    virtual std::any visitBreak_stmt(pscriptParser::Break_stmtContext *context) = 0;

    virtual std::any visitContinue_stmt(pscriptParser::Continue_stmtContext *context) = 0;

    virtual std::any visitReturn_stmt(pscriptParser::Return_stmtContext *context) = 0;

    virtual std::any visitRaise_stmt(pscriptParser::Raise_stmtContext *context) = 0;

    virtual std::any visitYield_stmt(pscriptParser::Yield_stmtContext *context) = 0;

    virtual std::any visitImport_stmt(pscriptParser::Import_stmtContext *context) = 0;

    virtual std::any visitFrom_import_stmt(pscriptParser::From_import_stmtContext *context) = 0;

    virtual std::any visitGlobal_stmt(pscriptParser::Global_stmtContext *context) = 0;

    virtual std::any visitAssert_stmt(pscriptParser::Assert_stmtContext *context) = 0;

    virtual std::any visitNonlocal_stmt(pscriptParser::Nonlocal_stmtContext *context) = 0;

    virtual std::any visitVariable_def(pscriptParser::Variable_defContext *context) = 0;

    virtual std::any visitVariable_def_name(pscriptParser::Variable_def_nameContext *context) = 0;

    virtual std::any visitVariable_def_comma_name(pscriptParser::Variable_def_comma_nameContext *context) = 0;

    virtual std::any visitFrom_where(pscriptParser::From_whereContext *context) = 0;

    virtual std::any visitComma_name(pscriptParser::Comma_nameContext *context) = 0;

    virtual std::any visitComma_test(pscriptParser::Comma_testContext *context) = 0;

    virtual std::any visitVariable_def_consts(pscriptParser::Variable_def_constsContext *context) = 0;

    virtual std::any visitVariable_def_consts_with_colon(pscriptParser::Variable_def_consts_with_colonContext *context) = 0;

    virtual std::any visitTestlist_star_expr(pscriptParser::Testlist_star_exprContext *context) = 0;

    virtual std::any visitStar_expr(pscriptParser::Star_exprContext *context) = 0;

    virtual std::any visitAssign_part(pscriptParser::Assign_partContext *context) = 0;

    virtual std::any visitExprlist(pscriptParser::ExprlistContext *context) = 0;

    virtual std::any visitImport_as_names(pscriptParser::Import_as_namesContext *context) = 0;

    virtual std::any visitImport_as_name(pscriptParser::Import_as_nameContext *context) = 0;

    virtual std::any visitName_as_names(pscriptParser::Name_as_namesContext *context) = 0;

    virtual std::any visitName_as_name(pscriptParser::Name_as_nameContext *context) = 0;

    virtual std::any visitTest(pscriptParser::TestContext *context) = 0;

    virtual std::any visitVarargslist(pscriptParser::VarargslistContext *context) = 0;

    virtual std::any visitVardef_parameters(pscriptParser::Vardef_parametersContext *context) = 0;

    virtual std::any visitVardef_parameter(pscriptParser::Vardef_parameterContext *context) = 0;

    virtual std::any visitVarargs(pscriptParser::VarargsContext *context) = 0;

    virtual std::any visitVarkwargs(pscriptParser::VarkwargsContext *context) = 0;

    virtual std::any visitLogical_test(pscriptParser::Logical_testContext *context) = 0;

    virtual std::any visitComparison(pscriptParser::ComparisonContext *context) = 0;

    virtual std::any visitExpr(pscriptParser::ExprContext *context) = 0;

    virtual std::any visitAtom(pscriptParser::AtomContext *context) = 0;

    virtual std::any visitDictmaker(pscriptParser::DictmakerContext *context) = 0;

    virtual std::any visitSetmaker(pscriptParser::SetmakerContext *context) = 0;

    virtual std::any visitTestlist(pscriptParser::TestlistContext *context) = 0;

    virtual std::any visitDotted_name(pscriptParser::Dotted_nameContext *context) = 0;

    virtual std::any visitName(pscriptParser::NameContext *context) = 0;

    virtual std::any visitBool(pscriptParser::BoolContext *context) = 0;

    virtual std::any visitNumber(pscriptParser::NumberContext *context) = 0;

    virtual std::any visitInteger(pscriptParser::IntegerContext *context) = 0;

    virtual std::any visitYield_expr(pscriptParser::Yield_exprContext *context) = 0;

    virtual std::any visitYield_arg(pscriptParser::Yield_argContext *context) = 0;

    virtual std::any visitTrailer(pscriptParser::TrailerContext *context) = 0;

    virtual std::any visitArguments(pscriptParser::ArgumentsContext *context) = 0;

    virtual std::any visitArglist(pscriptParser::ArglistContext *context) = 0;

    virtual std::any visitArgument(pscriptParser::ArgumentContext *context) = 0;

    virtual std::any visitSubscriptlist(pscriptParser::SubscriptlistContext *context) = 0;

    virtual std::any visitSubscript(pscriptParser::SubscriptContext *context) = 0;

    virtual std::any visitSliceop(pscriptParser::SliceopContext *context) = 0;

    virtual std::any visitComp_for(pscriptParser::Comp_forContext *context) = 0;

    virtual std::any visitComp_iter(pscriptParser::Comp_iterContext *context) = 0;


};

