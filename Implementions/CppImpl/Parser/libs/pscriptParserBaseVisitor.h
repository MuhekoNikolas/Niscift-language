
// Generated from ./pscriptParser.g4 by ANTLR 4.13.0

#pragma once


#include "antlr4-runtime.h"
#include "pscriptParserVisitor.h"


/**
 * This class provides an empty implementation of pscriptParserVisitor, which can be
 * extended to create a visitor which only needs to handle a subset of the available methods.
 */
class  pscriptParserBaseVisitor : public pscriptParserVisitor {
public:

  virtual std::any visitRoot(pscriptParser::RootContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitSingle_input(pscriptParser::Single_inputContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitFile_input(pscriptParser::File_inputContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitEval_input(pscriptParser::Eval_inputContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitStmt(pscriptParser::StmtContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitIf_stmt(pscriptParser::If_stmtContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitWhile_stmt(pscriptParser::While_stmtContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitFor_stmt(pscriptParser::For_stmtContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitTry_stmt(pscriptParser::Try_stmtContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitWith_stmt(pscriptParser::With_stmtContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitClass_def_stmt(pscriptParser::Class_def_stmtContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitFunc_def_stmt(pscriptParser::Func_def_stmtContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitSuite(pscriptParser::SuiteContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitDecorator(pscriptParser::DecoratorContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitElif_clause(pscriptParser::Elif_clauseContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitElse_clause(pscriptParser::Else_clauseContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitFinally_clause(pscriptParser::Finally_clauseContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitWith_item(pscriptParser::With_itemContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitExcept_clause(pscriptParser::Except_clauseContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitClassdef(pscriptParser::ClassdefContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitFuncdef(pscriptParser::FuncdefContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitTypedargslist(pscriptParser::TypedargslistContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitArgs(pscriptParser::ArgsContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitKwargs(pscriptParser::KwargsContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitDef_parameters(pscriptParser::Def_parametersContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitDef_parameter(pscriptParser::Def_parameterContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitNamed_parameter(pscriptParser::Named_parameterContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitSimple_stmt(pscriptParser::Simple_stmtContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitVariable_def_stmt(pscriptParser::Variable_def_stmtContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitFunc_call_stmt(pscriptParser::Func_call_stmtContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitDel_stmt(pscriptParser::Del_stmtContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitPass_stmt(pscriptParser::Pass_stmtContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitBreak_stmt(pscriptParser::Break_stmtContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitContinue_stmt(pscriptParser::Continue_stmtContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitReturn_stmt(pscriptParser::Return_stmtContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitRaise_stmt(pscriptParser::Raise_stmtContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitYield_stmt(pscriptParser::Yield_stmtContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitImport_stmt(pscriptParser::Import_stmtContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitFrom_import_stmt(pscriptParser::From_import_stmtContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitGlobal_stmt(pscriptParser::Global_stmtContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitAssert_stmt(pscriptParser::Assert_stmtContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitNonlocal_stmt(pscriptParser::Nonlocal_stmtContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitVariable_def(pscriptParser::Variable_defContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitVariable_def_name(pscriptParser::Variable_def_nameContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitVariable_def_comma_name(pscriptParser::Variable_def_comma_nameContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitFrom_where(pscriptParser::From_whereContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitComma_name(pscriptParser::Comma_nameContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitComma_test(pscriptParser::Comma_testContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitVariable_def_consts(pscriptParser::Variable_def_constsContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitVariable_def_consts_with_colon(pscriptParser::Variable_def_consts_with_colonContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitTestlist_star_expr(pscriptParser::Testlist_star_exprContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitStar_expr(pscriptParser::Star_exprContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitAssign_part(pscriptParser::Assign_partContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitExprlist(pscriptParser::ExprlistContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitImport_as_names(pscriptParser::Import_as_namesContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitImport_as_name(pscriptParser::Import_as_nameContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitName_as_names(pscriptParser::Name_as_namesContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitName_as_name(pscriptParser::Name_as_nameContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitTest(pscriptParser::TestContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitVarargslist(pscriptParser::VarargslistContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitVardef_parameters(pscriptParser::Vardef_parametersContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitVardef_parameter(pscriptParser::Vardef_parameterContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitVarargs(pscriptParser::VarargsContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitVarkwargs(pscriptParser::VarkwargsContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitLogical_test(pscriptParser::Logical_testContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitComparison(pscriptParser::ComparisonContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitExpr(pscriptParser::ExprContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitAtom(pscriptParser::AtomContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitDictmaker(pscriptParser::DictmakerContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitSetmaker(pscriptParser::SetmakerContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitTestlist(pscriptParser::TestlistContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitDotted_name(pscriptParser::Dotted_nameContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitName(pscriptParser::NameContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitBool(pscriptParser::BoolContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitNumber(pscriptParser::NumberContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitInteger(pscriptParser::IntegerContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitYield_expr(pscriptParser::Yield_exprContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitYield_arg(pscriptParser::Yield_argContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitTrailer(pscriptParser::TrailerContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitArguments(pscriptParser::ArgumentsContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitArglist(pscriptParser::ArglistContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitArgument(pscriptParser::ArgumentContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitSubscriptlist(pscriptParser::SubscriptlistContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitSubscript(pscriptParser::SubscriptContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitSliceop(pscriptParser::SliceopContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitComp_for(pscriptParser::Comp_forContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitComp_iter(pscriptParser::Comp_iterContext *ctx) override {
    return visitChildren(ctx);
  }


};

