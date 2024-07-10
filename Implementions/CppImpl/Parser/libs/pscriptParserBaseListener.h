
// Generated from ./pscriptParser.g4 by ANTLR 4.13.0

#pragma once


#include "antlr4-runtime.h"
#include "pscriptParserListener.h"


/**
 * This class provides an empty implementation of pscriptParserListener,
 * which can be extended to create a listener which only needs to handle a subset
 * of the available methods.
 */
class  pscriptParserBaseListener : public pscriptParserListener {
public:

  virtual void enterRoot(pscriptParser::RootContext * /*ctx*/) override { }
  virtual void exitRoot(pscriptParser::RootContext * /*ctx*/) override { }

  virtual void enterSingle_input(pscriptParser::Single_inputContext * /*ctx*/) override { }
  virtual void exitSingle_input(pscriptParser::Single_inputContext * /*ctx*/) override { }

  virtual void enterFile_input(pscriptParser::File_inputContext * /*ctx*/) override { }
  virtual void exitFile_input(pscriptParser::File_inputContext * /*ctx*/) override { }

  virtual void enterEval_input(pscriptParser::Eval_inputContext * /*ctx*/) override { }
  virtual void exitEval_input(pscriptParser::Eval_inputContext * /*ctx*/) override { }

  virtual void enterStmt(pscriptParser::StmtContext * /*ctx*/) override { }
  virtual void exitStmt(pscriptParser::StmtContext * /*ctx*/) override { }

  virtual void enterIf_stmt(pscriptParser::If_stmtContext * /*ctx*/) override { }
  virtual void exitIf_stmt(pscriptParser::If_stmtContext * /*ctx*/) override { }

  virtual void enterWhile_stmt(pscriptParser::While_stmtContext * /*ctx*/) override { }
  virtual void exitWhile_stmt(pscriptParser::While_stmtContext * /*ctx*/) override { }

  virtual void enterFor_stmt(pscriptParser::For_stmtContext * /*ctx*/) override { }
  virtual void exitFor_stmt(pscriptParser::For_stmtContext * /*ctx*/) override { }

  virtual void enterTry_stmt(pscriptParser::Try_stmtContext * /*ctx*/) override { }
  virtual void exitTry_stmt(pscriptParser::Try_stmtContext * /*ctx*/) override { }

  virtual void enterWith_stmt(pscriptParser::With_stmtContext * /*ctx*/) override { }
  virtual void exitWith_stmt(pscriptParser::With_stmtContext * /*ctx*/) override { }

  virtual void enterClass_def_stmt(pscriptParser::Class_def_stmtContext * /*ctx*/) override { }
  virtual void exitClass_def_stmt(pscriptParser::Class_def_stmtContext * /*ctx*/) override { }

  virtual void enterFunc_def_stmt(pscriptParser::Func_def_stmtContext * /*ctx*/) override { }
  virtual void exitFunc_def_stmt(pscriptParser::Func_def_stmtContext * /*ctx*/) override { }

  virtual void enterSuite(pscriptParser::SuiteContext * /*ctx*/) override { }
  virtual void exitSuite(pscriptParser::SuiteContext * /*ctx*/) override { }

  virtual void enterDecorator(pscriptParser::DecoratorContext * /*ctx*/) override { }
  virtual void exitDecorator(pscriptParser::DecoratorContext * /*ctx*/) override { }

  virtual void enterElif_clause(pscriptParser::Elif_clauseContext * /*ctx*/) override { }
  virtual void exitElif_clause(pscriptParser::Elif_clauseContext * /*ctx*/) override { }

  virtual void enterElse_clause(pscriptParser::Else_clauseContext * /*ctx*/) override { }
  virtual void exitElse_clause(pscriptParser::Else_clauseContext * /*ctx*/) override { }

  virtual void enterFinally_clause(pscriptParser::Finally_clauseContext * /*ctx*/) override { }
  virtual void exitFinally_clause(pscriptParser::Finally_clauseContext * /*ctx*/) override { }

  virtual void enterWith_item(pscriptParser::With_itemContext * /*ctx*/) override { }
  virtual void exitWith_item(pscriptParser::With_itemContext * /*ctx*/) override { }

  virtual void enterExcept_clause(pscriptParser::Except_clauseContext * /*ctx*/) override { }
  virtual void exitExcept_clause(pscriptParser::Except_clauseContext * /*ctx*/) override { }

  virtual void enterClassdef(pscriptParser::ClassdefContext * /*ctx*/) override { }
  virtual void exitClassdef(pscriptParser::ClassdefContext * /*ctx*/) override { }

  virtual void enterFuncdef(pscriptParser::FuncdefContext * /*ctx*/) override { }
  virtual void exitFuncdef(pscriptParser::FuncdefContext * /*ctx*/) override { }

  virtual void enterTypedargslist(pscriptParser::TypedargslistContext * /*ctx*/) override { }
  virtual void exitTypedargslist(pscriptParser::TypedargslistContext * /*ctx*/) override { }

  virtual void enterArgs(pscriptParser::ArgsContext * /*ctx*/) override { }
  virtual void exitArgs(pscriptParser::ArgsContext * /*ctx*/) override { }

  virtual void enterKwargs(pscriptParser::KwargsContext * /*ctx*/) override { }
  virtual void exitKwargs(pscriptParser::KwargsContext * /*ctx*/) override { }

  virtual void enterDef_parameters(pscriptParser::Def_parametersContext * /*ctx*/) override { }
  virtual void exitDef_parameters(pscriptParser::Def_parametersContext * /*ctx*/) override { }

  virtual void enterDef_parameter(pscriptParser::Def_parameterContext * /*ctx*/) override { }
  virtual void exitDef_parameter(pscriptParser::Def_parameterContext * /*ctx*/) override { }

  virtual void enterNamed_parameter(pscriptParser::Named_parameterContext * /*ctx*/) override { }
  virtual void exitNamed_parameter(pscriptParser::Named_parameterContext * /*ctx*/) override { }

  virtual void enterSimple_stmt(pscriptParser::Simple_stmtContext * /*ctx*/) override { }
  virtual void exitSimple_stmt(pscriptParser::Simple_stmtContext * /*ctx*/) override { }

  virtual void enterVariable_def_stmt(pscriptParser::Variable_def_stmtContext * /*ctx*/) override { }
  virtual void exitVariable_def_stmt(pscriptParser::Variable_def_stmtContext * /*ctx*/) override { }

  virtual void enterFunc_call_stmt(pscriptParser::Func_call_stmtContext * /*ctx*/) override { }
  virtual void exitFunc_call_stmt(pscriptParser::Func_call_stmtContext * /*ctx*/) override { }

  virtual void enterDel_stmt(pscriptParser::Del_stmtContext * /*ctx*/) override { }
  virtual void exitDel_stmt(pscriptParser::Del_stmtContext * /*ctx*/) override { }

  virtual void enterPass_stmt(pscriptParser::Pass_stmtContext * /*ctx*/) override { }
  virtual void exitPass_stmt(pscriptParser::Pass_stmtContext * /*ctx*/) override { }

  virtual void enterBreak_stmt(pscriptParser::Break_stmtContext * /*ctx*/) override { }
  virtual void exitBreak_stmt(pscriptParser::Break_stmtContext * /*ctx*/) override { }

  virtual void enterContinue_stmt(pscriptParser::Continue_stmtContext * /*ctx*/) override { }
  virtual void exitContinue_stmt(pscriptParser::Continue_stmtContext * /*ctx*/) override { }

  virtual void enterReturn_stmt(pscriptParser::Return_stmtContext * /*ctx*/) override { }
  virtual void exitReturn_stmt(pscriptParser::Return_stmtContext * /*ctx*/) override { }

  virtual void enterRaise_stmt(pscriptParser::Raise_stmtContext * /*ctx*/) override { }
  virtual void exitRaise_stmt(pscriptParser::Raise_stmtContext * /*ctx*/) override { }

  virtual void enterYield_stmt(pscriptParser::Yield_stmtContext * /*ctx*/) override { }
  virtual void exitYield_stmt(pscriptParser::Yield_stmtContext * /*ctx*/) override { }

  virtual void enterImport_stmt(pscriptParser::Import_stmtContext * /*ctx*/) override { }
  virtual void exitImport_stmt(pscriptParser::Import_stmtContext * /*ctx*/) override { }

  virtual void enterFrom_import_stmt(pscriptParser::From_import_stmtContext * /*ctx*/) override { }
  virtual void exitFrom_import_stmt(pscriptParser::From_import_stmtContext * /*ctx*/) override { }

  virtual void enterGlobal_stmt(pscriptParser::Global_stmtContext * /*ctx*/) override { }
  virtual void exitGlobal_stmt(pscriptParser::Global_stmtContext * /*ctx*/) override { }

  virtual void enterAssert_stmt(pscriptParser::Assert_stmtContext * /*ctx*/) override { }
  virtual void exitAssert_stmt(pscriptParser::Assert_stmtContext * /*ctx*/) override { }

  virtual void enterNonlocal_stmt(pscriptParser::Nonlocal_stmtContext * /*ctx*/) override { }
  virtual void exitNonlocal_stmt(pscriptParser::Nonlocal_stmtContext * /*ctx*/) override { }

  virtual void enterVariable_def(pscriptParser::Variable_defContext * /*ctx*/) override { }
  virtual void exitVariable_def(pscriptParser::Variable_defContext * /*ctx*/) override { }

  virtual void enterVariable_def_name(pscriptParser::Variable_def_nameContext * /*ctx*/) override { }
  virtual void exitVariable_def_name(pscriptParser::Variable_def_nameContext * /*ctx*/) override { }

  virtual void enterVariable_def_comma_name(pscriptParser::Variable_def_comma_nameContext * /*ctx*/) override { }
  virtual void exitVariable_def_comma_name(pscriptParser::Variable_def_comma_nameContext * /*ctx*/) override { }

  virtual void enterFrom_where(pscriptParser::From_whereContext * /*ctx*/) override { }
  virtual void exitFrom_where(pscriptParser::From_whereContext * /*ctx*/) override { }

  virtual void enterComma_name(pscriptParser::Comma_nameContext * /*ctx*/) override { }
  virtual void exitComma_name(pscriptParser::Comma_nameContext * /*ctx*/) override { }

  virtual void enterComma_test(pscriptParser::Comma_testContext * /*ctx*/) override { }
  virtual void exitComma_test(pscriptParser::Comma_testContext * /*ctx*/) override { }

  virtual void enterVariable_def_consts(pscriptParser::Variable_def_constsContext * /*ctx*/) override { }
  virtual void exitVariable_def_consts(pscriptParser::Variable_def_constsContext * /*ctx*/) override { }

  virtual void enterVariable_def_consts_with_colon(pscriptParser::Variable_def_consts_with_colonContext * /*ctx*/) override { }
  virtual void exitVariable_def_consts_with_colon(pscriptParser::Variable_def_consts_with_colonContext * /*ctx*/) override { }

  virtual void enterTestlist_star_expr(pscriptParser::Testlist_star_exprContext * /*ctx*/) override { }
  virtual void exitTestlist_star_expr(pscriptParser::Testlist_star_exprContext * /*ctx*/) override { }

  virtual void enterStar_expr(pscriptParser::Star_exprContext * /*ctx*/) override { }
  virtual void exitStar_expr(pscriptParser::Star_exprContext * /*ctx*/) override { }

  virtual void enterAssign_part(pscriptParser::Assign_partContext * /*ctx*/) override { }
  virtual void exitAssign_part(pscriptParser::Assign_partContext * /*ctx*/) override { }

  virtual void enterExprlist(pscriptParser::ExprlistContext * /*ctx*/) override { }
  virtual void exitExprlist(pscriptParser::ExprlistContext * /*ctx*/) override { }

  virtual void enterImport_as_names(pscriptParser::Import_as_namesContext * /*ctx*/) override { }
  virtual void exitImport_as_names(pscriptParser::Import_as_namesContext * /*ctx*/) override { }

  virtual void enterImport_as_name(pscriptParser::Import_as_nameContext * /*ctx*/) override { }
  virtual void exitImport_as_name(pscriptParser::Import_as_nameContext * /*ctx*/) override { }

  virtual void enterName_as_names(pscriptParser::Name_as_namesContext * /*ctx*/) override { }
  virtual void exitName_as_names(pscriptParser::Name_as_namesContext * /*ctx*/) override { }

  virtual void enterName_as_name(pscriptParser::Name_as_nameContext * /*ctx*/) override { }
  virtual void exitName_as_name(pscriptParser::Name_as_nameContext * /*ctx*/) override { }

  virtual void enterTest(pscriptParser::TestContext * /*ctx*/) override { }
  virtual void exitTest(pscriptParser::TestContext * /*ctx*/) override { }

  virtual void enterVarargslist(pscriptParser::VarargslistContext * /*ctx*/) override { }
  virtual void exitVarargslist(pscriptParser::VarargslistContext * /*ctx*/) override { }

  virtual void enterVardef_parameters(pscriptParser::Vardef_parametersContext * /*ctx*/) override { }
  virtual void exitVardef_parameters(pscriptParser::Vardef_parametersContext * /*ctx*/) override { }

  virtual void enterVardef_parameter(pscriptParser::Vardef_parameterContext * /*ctx*/) override { }
  virtual void exitVardef_parameter(pscriptParser::Vardef_parameterContext * /*ctx*/) override { }

  virtual void enterVarargs(pscriptParser::VarargsContext * /*ctx*/) override { }
  virtual void exitVarargs(pscriptParser::VarargsContext * /*ctx*/) override { }

  virtual void enterVarkwargs(pscriptParser::VarkwargsContext * /*ctx*/) override { }
  virtual void exitVarkwargs(pscriptParser::VarkwargsContext * /*ctx*/) override { }

  virtual void enterLogical_test(pscriptParser::Logical_testContext * /*ctx*/) override { }
  virtual void exitLogical_test(pscriptParser::Logical_testContext * /*ctx*/) override { }

  virtual void enterComparison(pscriptParser::ComparisonContext * /*ctx*/) override { }
  virtual void exitComparison(pscriptParser::ComparisonContext * /*ctx*/) override { }

  virtual void enterExpr(pscriptParser::ExprContext * /*ctx*/) override { }
  virtual void exitExpr(pscriptParser::ExprContext * /*ctx*/) override { }

  virtual void enterAtom(pscriptParser::AtomContext * /*ctx*/) override { }
  virtual void exitAtom(pscriptParser::AtomContext * /*ctx*/) override { }

  virtual void enterDictmaker(pscriptParser::DictmakerContext * /*ctx*/) override { }
  virtual void exitDictmaker(pscriptParser::DictmakerContext * /*ctx*/) override { }

  virtual void enterSetmaker(pscriptParser::SetmakerContext * /*ctx*/) override { }
  virtual void exitSetmaker(pscriptParser::SetmakerContext * /*ctx*/) override { }

  virtual void enterTestlist(pscriptParser::TestlistContext * /*ctx*/) override { }
  virtual void exitTestlist(pscriptParser::TestlistContext * /*ctx*/) override { }

  virtual void enterDotted_name(pscriptParser::Dotted_nameContext * /*ctx*/) override { }
  virtual void exitDotted_name(pscriptParser::Dotted_nameContext * /*ctx*/) override { }

  virtual void enterName(pscriptParser::NameContext * /*ctx*/) override { }
  virtual void exitName(pscriptParser::NameContext * /*ctx*/) override { }

  virtual void enterBool(pscriptParser::BoolContext * /*ctx*/) override { }
  virtual void exitBool(pscriptParser::BoolContext * /*ctx*/) override { }

  virtual void enterNumber(pscriptParser::NumberContext * /*ctx*/) override { }
  virtual void exitNumber(pscriptParser::NumberContext * /*ctx*/) override { }

  virtual void enterInteger(pscriptParser::IntegerContext * /*ctx*/) override { }
  virtual void exitInteger(pscriptParser::IntegerContext * /*ctx*/) override { }

  virtual void enterYield_expr(pscriptParser::Yield_exprContext * /*ctx*/) override { }
  virtual void exitYield_expr(pscriptParser::Yield_exprContext * /*ctx*/) override { }

  virtual void enterYield_arg(pscriptParser::Yield_argContext * /*ctx*/) override { }
  virtual void exitYield_arg(pscriptParser::Yield_argContext * /*ctx*/) override { }

  virtual void enterTrailer(pscriptParser::TrailerContext * /*ctx*/) override { }
  virtual void exitTrailer(pscriptParser::TrailerContext * /*ctx*/) override { }

  virtual void enterArguments(pscriptParser::ArgumentsContext * /*ctx*/) override { }
  virtual void exitArguments(pscriptParser::ArgumentsContext * /*ctx*/) override { }

  virtual void enterArglist(pscriptParser::ArglistContext * /*ctx*/) override { }
  virtual void exitArglist(pscriptParser::ArglistContext * /*ctx*/) override { }

  virtual void enterArgument(pscriptParser::ArgumentContext * /*ctx*/) override { }
  virtual void exitArgument(pscriptParser::ArgumentContext * /*ctx*/) override { }

  virtual void enterSubscriptlist(pscriptParser::SubscriptlistContext * /*ctx*/) override { }
  virtual void exitSubscriptlist(pscriptParser::SubscriptlistContext * /*ctx*/) override { }

  virtual void enterSubscript(pscriptParser::SubscriptContext * /*ctx*/) override { }
  virtual void exitSubscript(pscriptParser::SubscriptContext * /*ctx*/) override { }

  virtual void enterSliceop(pscriptParser::SliceopContext * /*ctx*/) override { }
  virtual void exitSliceop(pscriptParser::SliceopContext * /*ctx*/) override { }

  virtual void enterComp_for(pscriptParser::Comp_forContext * /*ctx*/) override { }
  virtual void exitComp_for(pscriptParser::Comp_forContext * /*ctx*/) override { }

  virtual void enterComp_iter(pscriptParser::Comp_iterContext * /*ctx*/) override { }
  virtual void exitComp_iter(pscriptParser::Comp_iterContext * /*ctx*/) override { }


  virtual void enterEveryRule(antlr4::ParserRuleContext * /*ctx*/) override { }
  virtual void exitEveryRule(antlr4::ParserRuleContext * /*ctx*/) override { }
  virtual void visitTerminal(antlr4::tree::TerminalNode * /*node*/) override { }
  virtual void visitErrorNode(antlr4::tree::ErrorNode * /*node*/) override { }

};

