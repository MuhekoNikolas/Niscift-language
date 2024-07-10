
// Generated from ./pscriptParser.g4 by ANTLR 4.13.0

#pragma once


#include "antlr4-runtime.h"
#include "pscriptParser.h"


/**
 * This interface defines an abstract listener for a parse tree produced by pscriptParser.
 */
class  pscriptParserListener : public antlr4::tree::ParseTreeListener {
public:

  virtual void enterRoot(pscriptParser::RootContext *ctx) = 0;
  virtual void exitRoot(pscriptParser::RootContext *ctx) = 0;

  virtual void enterSingle_input(pscriptParser::Single_inputContext *ctx) = 0;
  virtual void exitSingle_input(pscriptParser::Single_inputContext *ctx) = 0;

  virtual void enterFile_input(pscriptParser::File_inputContext *ctx) = 0;
  virtual void exitFile_input(pscriptParser::File_inputContext *ctx) = 0;

  virtual void enterEval_input(pscriptParser::Eval_inputContext *ctx) = 0;
  virtual void exitEval_input(pscriptParser::Eval_inputContext *ctx) = 0;

  virtual void enterStmt(pscriptParser::StmtContext *ctx) = 0;
  virtual void exitStmt(pscriptParser::StmtContext *ctx) = 0;

  virtual void enterIf_stmt(pscriptParser::If_stmtContext *ctx) = 0;
  virtual void exitIf_stmt(pscriptParser::If_stmtContext *ctx) = 0;

  virtual void enterWhile_stmt(pscriptParser::While_stmtContext *ctx) = 0;
  virtual void exitWhile_stmt(pscriptParser::While_stmtContext *ctx) = 0;

  virtual void enterFor_stmt(pscriptParser::For_stmtContext *ctx) = 0;
  virtual void exitFor_stmt(pscriptParser::For_stmtContext *ctx) = 0;

  virtual void enterTry_stmt(pscriptParser::Try_stmtContext *ctx) = 0;
  virtual void exitTry_stmt(pscriptParser::Try_stmtContext *ctx) = 0;

  virtual void enterWith_stmt(pscriptParser::With_stmtContext *ctx) = 0;
  virtual void exitWith_stmt(pscriptParser::With_stmtContext *ctx) = 0;

  virtual void enterClass_def_stmt(pscriptParser::Class_def_stmtContext *ctx) = 0;
  virtual void exitClass_def_stmt(pscriptParser::Class_def_stmtContext *ctx) = 0;

  virtual void enterFunc_def_stmt(pscriptParser::Func_def_stmtContext *ctx) = 0;
  virtual void exitFunc_def_stmt(pscriptParser::Func_def_stmtContext *ctx) = 0;

  virtual void enterSuite(pscriptParser::SuiteContext *ctx) = 0;
  virtual void exitSuite(pscriptParser::SuiteContext *ctx) = 0;

  virtual void enterDecorator(pscriptParser::DecoratorContext *ctx) = 0;
  virtual void exitDecorator(pscriptParser::DecoratorContext *ctx) = 0;

  virtual void enterElif_clause(pscriptParser::Elif_clauseContext *ctx) = 0;
  virtual void exitElif_clause(pscriptParser::Elif_clauseContext *ctx) = 0;

  virtual void enterElse_clause(pscriptParser::Else_clauseContext *ctx) = 0;
  virtual void exitElse_clause(pscriptParser::Else_clauseContext *ctx) = 0;

  virtual void enterFinally_clause(pscriptParser::Finally_clauseContext *ctx) = 0;
  virtual void exitFinally_clause(pscriptParser::Finally_clauseContext *ctx) = 0;

  virtual void enterWith_item(pscriptParser::With_itemContext *ctx) = 0;
  virtual void exitWith_item(pscriptParser::With_itemContext *ctx) = 0;

  virtual void enterExcept_clause(pscriptParser::Except_clauseContext *ctx) = 0;
  virtual void exitExcept_clause(pscriptParser::Except_clauseContext *ctx) = 0;

  virtual void enterClassdef(pscriptParser::ClassdefContext *ctx) = 0;
  virtual void exitClassdef(pscriptParser::ClassdefContext *ctx) = 0;

  virtual void enterFuncdef(pscriptParser::FuncdefContext *ctx) = 0;
  virtual void exitFuncdef(pscriptParser::FuncdefContext *ctx) = 0;

  virtual void enterTypedargslist(pscriptParser::TypedargslistContext *ctx) = 0;
  virtual void exitTypedargslist(pscriptParser::TypedargslistContext *ctx) = 0;

  virtual void enterArgs(pscriptParser::ArgsContext *ctx) = 0;
  virtual void exitArgs(pscriptParser::ArgsContext *ctx) = 0;

  virtual void enterKwargs(pscriptParser::KwargsContext *ctx) = 0;
  virtual void exitKwargs(pscriptParser::KwargsContext *ctx) = 0;

  virtual void enterDef_parameters(pscriptParser::Def_parametersContext *ctx) = 0;
  virtual void exitDef_parameters(pscriptParser::Def_parametersContext *ctx) = 0;

  virtual void enterDef_parameter(pscriptParser::Def_parameterContext *ctx) = 0;
  virtual void exitDef_parameter(pscriptParser::Def_parameterContext *ctx) = 0;

  virtual void enterNamed_parameter(pscriptParser::Named_parameterContext *ctx) = 0;
  virtual void exitNamed_parameter(pscriptParser::Named_parameterContext *ctx) = 0;

  virtual void enterSimple_stmt(pscriptParser::Simple_stmtContext *ctx) = 0;
  virtual void exitSimple_stmt(pscriptParser::Simple_stmtContext *ctx) = 0;

  virtual void enterVariable_def_stmt(pscriptParser::Variable_def_stmtContext *ctx) = 0;
  virtual void exitVariable_def_stmt(pscriptParser::Variable_def_stmtContext *ctx) = 0;

  virtual void enterFunc_call_stmt(pscriptParser::Func_call_stmtContext *ctx) = 0;
  virtual void exitFunc_call_stmt(pscriptParser::Func_call_stmtContext *ctx) = 0;

  virtual void enterDel_stmt(pscriptParser::Del_stmtContext *ctx) = 0;
  virtual void exitDel_stmt(pscriptParser::Del_stmtContext *ctx) = 0;

  virtual void enterPass_stmt(pscriptParser::Pass_stmtContext *ctx) = 0;
  virtual void exitPass_stmt(pscriptParser::Pass_stmtContext *ctx) = 0;

  virtual void enterBreak_stmt(pscriptParser::Break_stmtContext *ctx) = 0;
  virtual void exitBreak_stmt(pscriptParser::Break_stmtContext *ctx) = 0;

  virtual void enterContinue_stmt(pscriptParser::Continue_stmtContext *ctx) = 0;
  virtual void exitContinue_stmt(pscriptParser::Continue_stmtContext *ctx) = 0;

  virtual void enterReturn_stmt(pscriptParser::Return_stmtContext *ctx) = 0;
  virtual void exitReturn_stmt(pscriptParser::Return_stmtContext *ctx) = 0;

  virtual void enterRaise_stmt(pscriptParser::Raise_stmtContext *ctx) = 0;
  virtual void exitRaise_stmt(pscriptParser::Raise_stmtContext *ctx) = 0;

  virtual void enterYield_stmt(pscriptParser::Yield_stmtContext *ctx) = 0;
  virtual void exitYield_stmt(pscriptParser::Yield_stmtContext *ctx) = 0;

  virtual void enterImport_stmt(pscriptParser::Import_stmtContext *ctx) = 0;
  virtual void exitImport_stmt(pscriptParser::Import_stmtContext *ctx) = 0;

  virtual void enterFrom_import_stmt(pscriptParser::From_import_stmtContext *ctx) = 0;
  virtual void exitFrom_import_stmt(pscriptParser::From_import_stmtContext *ctx) = 0;

  virtual void enterGlobal_stmt(pscriptParser::Global_stmtContext *ctx) = 0;
  virtual void exitGlobal_stmt(pscriptParser::Global_stmtContext *ctx) = 0;

  virtual void enterAssert_stmt(pscriptParser::Assert_stmtContext *ctx) = 0;
  virtual void exitAssert_stmt(pscriptParser::Assert_stmtContext *ctx) = 0;

  virtual void enterNonlocal_stmt(pscriptParser::Nonlocal_stmtContext *ctx) = 0;
  virtual void exitNonlocal_stmt(pscriptParser::Nonlocal_stmtContext *ctx) = 0;

  virtual void enterVariable_def(pscriptParser::Variable_defContext *ctx) = 0;
  virtual void exitVariable_def(pscriptParser::Variable_defContext *ctx) = 0;

  virtual void enterVariable_def_name(pscriptParser::Variable_def_nameContext *ctx) = 0;
  virtual void exitVariable_def_name(pscriptParser::Variable_def_nameContext *ctx) = 0;

  virtual void enterVariable_def_comma_name(pscriptParser::Variable_def_comma_nameContext *ctx) = 0;
  virtual void exitVariable_def_comma_name(pscriptParser::Variable_def_comma_nameContext *ctx) = 0;

  virtual void enterFrom_where(pscriptParser::From_whereContext *ctx) = 0;
  virtual void exitFrom_where(pscriptParser::From_whereContext *ctx) = 0;

  virtual void enterComma_name(pscriptParser::Comma_nameContext *ctx) = 0;
  virtual void exitComma_name(pscriptParser::Comma_nameContext *ctx) = 0;

  virtual void enterComma_test(pscriptParser::Comma_testContext *ctx) = 0;
  virtual void exitComma_test(pscriptParser::Comma_testContext *ctx) = 0;

  virtual void enterVariable_def_consts(pscriptParser::Variable_def_constsContext *ctx) = 0;
  virtual void exitVariable_def_consts(pscriptParser::Variable_def_constsContext *ctx) = 0;

  virtual void enterVariable_def_consts_with_colon(pscriptParser::Variable_def_consts_with_colonContext *ctx) = 0;
  virtual void exitVariable_def_consts_with_colon(pscriptParser::Variable_def_consts_with_colonContext *ctx) = 0;

  virtual void enterTestlist_star_expr(pscriptParser::Testlist_star_exprContext *ctx) = 0;
  virtual void exitTestlist_star_expr(pscriptParser::Testlist_star_exprContext *ctx) = 0;

  virtual void enterStar_expr(pscriptParser::Star_exprContext *ctx) = 0;
  virtual void exitStar_expr(pscriptParser::Star_exprContext *ctx) = 0;

  virtual void enterAssign_part(pscriptParser::Assign_partContext *ctx) = 0;
  virtual void exitAssign_part(pscriptParser::Assign_partContext *ctx) = 0;

  virtual void enterExprlist(pscriptParser::ExprlistContext *ctx) = 0;
  virtual void exitExprlist(pscriptParser::ExprlistContext *ctx) = 0;

  virtual void enterImport_as_names(pscriptParser::Import_as_namesContext *ctx) = 0;
  virtual void exitImport_as_names(pscriptParser::Import_as_namesContext *ctx) = 0;

  virtual void enterImport_as_name(pscriptParser::Import_as_nameContext *ctx) = 0;
  virtual void exitImport_as_name(pscriptParser::Import_as_nameContext *ctx) = 0;

  virtual void enterName_as_names(pscriptParser::Name_as_namesContext *ctx) = 0;
  virtual void exitName_as_names(pscriptParser::Name_as_namesContext *ctx) = 0;

  virtual void enterName_as_name(pscriptParser::Name_as_nameContext *ctx) = 0;
  virtual void exitName_as_name(pscriptParser::Name_as_nameContext *ctx) = 0;

  virtual void enterTest(pscriptParser::TestContext *ctx) = 0;
  virtual void exitTest(pscriptParser::TestContext *ctx) = 0;

  virtual void enterVarargslist(pscriptParser::VarargslistContext *ctx) = 0;
  virtual void exitVarargslist(pscriptParser::VarargslistContext *ctx) = 0;

  virtual void enterVardef_parameters(pscriptParser::Vardef_parametersContext *ctx) = 0;
  virtual void exitVardef_parameters(pscriptParser::Vardef_parametersContext *ctx) = 0;

  virtual void enterVardef_parameter(pscriptParser::Vardef_parameterContext *ctx) = 0;
  virtual void exitVardef_parameter(pscriptParser::Vardef_parameterContext *ctx) = 0;

  virtual void enterVarargs(pscriptParser::VarargsContext *ctx) = 0;
  virtual void exitVarargs(pscriptParser::VarargsContext *ctx) = 0;

  virtual void enterVarkwargs(pscriptParser::VarkwargsContext *ctx) = 0;
  virtual void exitVarkwargs(pscriptParser::VarkwargsContext *ctx) = 0;

  virtual void enterLogical_test(pscriptParser::Logical_testContext *ctx) = 0;
  virtual void exitLogical_test(pscriptParser::Logical_testContext *ctx) = 0;

  virtual void enterComparison(pscriptParser::ComparisonContext *ctx) = 0;
  virtual void exitComparison(pscriptParser::ComparisonContext *ctx) = 0;

  virtual void enterExpr(pscriptParser::ExprContext *ctx) = 0;
  virtual void exitExpr(pscriptParser::ExprContext *ctx) = 0;

  virtual void enterAtom(pscriptParser::AtomContext *ctx) = 0;
  virtual void exitAtom(pscriptParser::AtomContext *ctx) = 0;

  virtual void enterDictmaker(pscriptParser::DictmakerContext *ctx) = 0;
  virtual void exitDictmaker(pscriptParser::DictmakerContext *ctx) = 0;

  virtual void enterSetmaker(pscriptParser::SetmakerContext *ctx) = 0;
  virtual void exitSetmaker(pscriptParser::SetmakerContext *ctx) = 0;

  virtual void enterTestlist(pscriptParser::TestlistContext *ctx) = 0;
  virtual void exitTestlist(pscriptParser::TestlistContext *ctx) = 0;

  virtual void enterDotted_name(pscriptParser::Dotted_nameContext *ctx) = 0;
  virtual void exitDotted_name(pscriptParser::Dotted_nameContext *ctx) = 0;

  virtual void enterName(pscriptParser::NameContext *ctx) = 0;
  virtual void exitName(pscriptParser::NameContext *ctx) = 0;

  virtual void enterBool(pscriptParser::BoolContext *ctx) = 0;
  virtual void exitBool(pscriptParser::BoolContext *ctx) = 0;

  virtual void enterNumber(pscriptParser::NumberContext *ctx) = 0;
  virtual void exitNumber(pscriptParser::NumberContext *ctx) = 0;

  virtual void enterInteger(pscriptParser::IntegerContext *ctx) = 0;
  virtual void exitInteger(pscriptParser::IntegerContext *ctx) = 0;

  virtual void enterYield_expr(pscriptParser::Yield_exprContext *ctx) = 0;
  virtual void exitYield_expr(pscriptParser::Yield_exprContext *ctx) = 0;

  virtual void enterYield_arg(pscriptParser::Yield_argContext *ctx) = 0;
  virtual void exitYield_arg(pscriptParser::Yield_argContext *ctx) = 0;

  virtual void enterTrailer(pscriptParser::TrailerContext *ctx) = 0;
  virtual void exitTrailer(pscriptParser::TrailerContext *ctx) = 0;

  virtual void enterArguments(pscriptParser::ArgumentsContext *ctx) = 0;
  virtual void exitArguments(pscriptParser::ArgumentsContext *ctx) = 0;

  virtual void enterArglist(pscriptParser::ArglistContext *ctx) = 0;
  virtual void exitArglist(pscriptParser::ArglistContext *ctx) = 0;

  virtual void enterArgument(pscriptParser::ArgumentContext *ctx) = 0;
  virtual void exitArgument(pscriptParser::ArgumentContext *ctx) = 0;

  virtual void enterSubscriptlist(pscriptParser::SubscriptlistContext *ctx) = 0;
  virtual void exitSubscriptlist(pscriptParser::SubscriptlistContext *ctx) = 0;

  virtual void enterSubscript(pscriptParser::SubscriptContext *ctx) = 0;
  virtual void exitSubscript(pscriptParser::SubscriptContext *ctx) = 0;

  virtual void enterSliceop(pscriptParser::SliceopContext *ctx) = 0;
  virtual void exitSliceop(pscriptParser::SliceopContext *ctx) = 0;

  virtual void enterComp_for(pscriptParser::Comp_forContext *ctx) = 0;
  virtual void exitComp_for(pscriptParser::Comp_forContext *ctx) = 0;

  virtual void enterComp_iter(pscriptParser::Comp_iterContext *ctx) = 0;
  virtual void exitComp_iter(pscriptParser::Comp_iterContext *ctx) = 0;


};

