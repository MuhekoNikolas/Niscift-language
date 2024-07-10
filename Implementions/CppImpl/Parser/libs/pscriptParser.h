
// Generated from ./pscriptParser.g4 by ANTLR 4.13.0

#pragma once


#include "antlr4-runtime.h"




class  pscriptParser : public pscriptParserBase {
public:
  enum {
    INDENT = 1, DEDENT = 2, LINE_BREAK = 3, DEF = 4, RETURN = 5, RAISE = 6, 
    FROM = 7, IMPORT = 8, NONLOCAL = 9, AS = 10, GLOBAL = 11, ASSERT = 12, 
    IF = 13, ELIF = 14, ELSE = 15, WHILE = 16, FOR = 17, IN = 18, TRY = 19, 
    NONE = 20, FINALLY = 21, WITH = 22, EXCEPT = 23, LAMBDA = 24, OR = 25, 
    AND = 26, NOT = 27, IS = 28, CLASS = 29, YIELD = 30, DEL = 31, PASS = 32, 
    CONTINUE = 33, BREAK = 34, ASYNC = 35, AWAIT = 36, EXEC = 37, TRUE = 38, 
    FALSE = 39, VAR = 40, CONST = 41, LET = 42, DOT = 43, REVERSE_QUOTE = 44, 
    STAR = 45, COMMA = 46, COLON = 47, SEMI_COLON = 48, POWER = 49, ASSIGN = 50, 
    OR_OP = 51, XOR = 52, AND_OP = 53, LEFT_SHIFT = 54, RIGHT_SHIFT = 55, 
    ADD = 56, MINUS = 57, DIV = 58, MOD = 59, IDIV = 60, NOT_OP = 61, LESS_THAN = 62, 
    GREATER_THAN = 63, EQUALS = 64, GT_EQ = 65, LT_EQ = 66, NOT_EQ_1 = 67, 
    NOT_EQ_2 = 68, AT = 69, ARROW = 70, ADD_ASSIGN = 71, SUB_ASSIGN = 72, 
    MULT_ASSIGN = 73, DIV_ASSIGN = 74, MOD_ASSIGN = 75, XOR_ASSIGN = 76, 
    POWER_ASSIGN = 77, IDIV_ASSIGN = 78, STRING = 79, DECIMAL_INTEGER = 80, 
    OCT_INTEGER = 81, HEX_INTEGER = 82, BIN_INTEGER = 83, IMAG_NUMBER = 84, 
    FLOAT_NUMBER = 85, OPEN_PAREN = 86, CLOSE_PAREN = 87, OPEN_BRACE = 88, 
    CLOSE_BRACE = 89, OPEN_BRACKET = 90, CLOSE_BRACKET = 91, NAME = 92, 
    LINE_JOIN = 93, NEWLINE = 94, WS = 95, COMMENT = 96
  };

  enum {
    RuleRoot = 0, RuleSingle_input = 1, RuleFile_input = 2, RuleEval_input = 3, 
    RuleStmt = 4, RuleCompound_stmt = 5, RuleSuite = 6, RuleDecorator = 7, 
    RuleElif_clause = 8, RuleElse_clause = 9, RuleFinally_clause = 10, RuleWith_item = 11, 
    RuleExcept_clause = 12, RuleClassdef = 13, RuleFuncdef = 14, RuleTypedargslist = 15, 
    RuleArgs = 16, RuleKwargs = 17, RuleDef_parameters = 18, RuleDef_parameter = 19, 
    RuleNamed_parameter = 20, RuleSimple_stmt = 21, RuleSmall_stmt = 22, 
    RuleVariable_def = 23, RuleVariable_def_name = 24, RuleVariable_def_comma_name = 25, 
    RuleFrom_where = 26, RuleComma_name = 27, RuleComma_test = 28, RuleVariable_def_consts = 29, 
    RuleVariable_def_consts_with_colon = 30, RuleTestlist_star_expr = 31, 
    RuleStar_expr = 32, RuleAssign_part = 33, RuleExprlist = 34, RuleImport_as_names = 35, 
    RuleImport_as_name = 36, RuleName_as_names = 37, RuleName_as_name = 38, 
    RuleTest = 39, RuleVarargslist = 40, RuleVardef_parameters = 41, RuleVardef_parameter = 42, 
    RuleVarargs = 43, RuleVarkwargs = 44, RuleLogical_test = 45, RuleComparison = 46, 
    RuleExpr = 47, RuleAtom = 48, RuleDictmaker = 49, RuleSetmaker = 50, 
    RuleTestlist = 51, RuleDotted_name = 52, RuleName = 53, RuleBool = 54, 
    RuleNumber = 55, RuleInteger = 56, RuleYield_expr = 57, RuleYield_arg = 58, 
    RuleTrailer = 59, RuleArguments = 60, RuleArglist = 61, RuleArgument = 62, 
    RuleSubscriptlist = 63, RuleSubscript = 64, RuleSliceop = 65, RuleComp_for = 66, 
    RuleComp_iter = 67
  };

  explicit pscriptParser(antlr4::TokenStream *input);

  pscriptParser(antlr4::TokenStream *input, const antlr4::atn::ParserATNSimulatorOptions &options);

  ~pscriptParser() override;

  std::string getGrammarFileName() const override;

  const antlr4::atn::ATN& getATN() const override;

  const std::vector<std::string>& getRuleNames() const override;

  const antlr4::dfa::Vocabulary& getVocabulary() const override;

  antlr4::atn::SerializedATNView getSerializedATN() const override;


  class RootContext;
  class Single_inputContext;
  class File_inputContext;
  class Eval_inputContext;
  class StmtContext;
  class Compound_stmtContext;
  class SuiteContext;
  class DecoratorContext;
  class Elif_clauseContext;
  class Else_clauseContext;
  class Finally_clauseContext;
  class With_itemContext;
  class Except_clauseContext;
  class ClassdefContext;
  class FuncdefContext;
  class TypedargslistContext;
  class ArgsContext;
  class KwargsContext;
  class Def_parametersContext;
  class Def_parameterContext;
  class Named_parameterContext;
  class Simple_stmtContext;
  class Small_stmtContext;
  class Variable_defContext;
  class Variable_def_nameContext;
  class Variable_def_comma_nameContext;
  class From_whereContext;
  class Comma_nameContext;
  class Comma_testContext;
  class Variable_def_constsContext;
  class Variable_def_consts_with_colonContext;
  class Testlist_star_exprContext;
  class Star_exprContext;
  class Assign_partContext;
  class ExprlistContext;
  class Import_as_namesContext;
  class Import_as_nameContext;
  class Name_as_namesContext;
  class Name_as_nameContext;
  class TestContext;
  class VarargslistContext;
  class Vardef_parametersContext;
  class Vardef_parameterContext;
  class VarargsContext;
  class VarkwargsContext;
  class Logical_testContext;
  class ComparisonContext;
  class ExprContext;
  class AtomContext;
  class DictmakerContext;
  class SetmakerContext;
  class TestlistContext;
  class Dotted_nameContext;
  class NameContext;
  class BoolContext;
  class NumberContext;
  class IntegerContext;
  class Yield_exprContext;
  class Yield_argContext;
  class TrailerContext;
  class ArgumentsContext;
  class ArglistContext;
  class ArgumentContext;
  class SubscriptlistContext;
  class SubscriptContext;
  class SliceopContext;
  class Comp_forContext;
  class Comp_iterContext; 

  class  RootContext : public antlr4::ParserRuleContext {
  public:
    RootContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *EOF();
    Single_inputContext *single_input();
    File_inputContext *file_input();
    Eval_inputContext *eval_input();

    virtual void enterRule(antlr4::tree::ParseTreeListener *listener) override;
    virtual void exitRule(antlr4::tree::ParseTreeListener *listener) override;

    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  RootContext* root();

  class  Single_inputContext : public antlr4::ParserRuleContext {
  public:
    Single_inputContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *LINE_BREAK();
    Simple_stmtContext *simple_stmt();
    Compound_stmtContext *compound_stmt();

    virtual void enterRule(antlr4::tree::ParseTreeListener *listener) override;
    virtual void exitRule(antlr4::tree::ParseTreeListener *listener) override;

    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Single_inputContext* single_input();

  class  File_inputContext : public antlr4::ParserRuleContext {
  public:
    File_inputContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<antlr4::tree::TerminalNode *> LINE_BREAK();
    antlr4::tree::TerminalNode* LINE_BREAK(size_t i);
    std::vector<StmtContext *> stmt();
    StmtContext* stmt(size_t i);

    virtual void enterRule(antlr4::tree::ParseTreeListener *listener) override;
    virtual void exitRule(antlr4::tree::ParseTreeListener *listener) override;

    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  File_inputContext* file_input();

  class  Eval_inputContext : public antlr4::ParserRuleContext {
  public:
    Eval_inputContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    TestlistContext *testlist();
    std::vector<antlr4::tree::TerminalNode *> LINE_BREAK();
    antlr4::tree::TerminalNode* LINE_BREAK(size_t i);

    virtual void enterRule(antlr4::tree::ParseTreeListener *listener) override;
    virtual void exitRule(antlr4::tree::ParseTreeListener *listener) override;

    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Eval_inputContext* eval_input();

  class  StmtContext : public antlr4::ParserRuleContext {
  public:
    StmtContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    Simple_stmtContext *simple_stmt();
    Compound_stmtContext *compound_stmt();

    virtual void enterRule(antlr4::tree::ParseTreeListener *listener) override;
    virtual void exitRule(antlr4::tree::ParseTreeListener *listener) override;

    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  StmtContext* stmt();

  class  Compound_stmtContext : public antlr4::ParserRuleContext {
  public:
    Compound_stmtContext(antlr4::ParserRuleContext *parent, size_t invokingState);
   
    Compound_stmtContext() = default;
    void copyFrom(Compound_stmtContext *context);
    using antlr4::ParserRuleContext::copyFrom;

    virtual size_t getRuleIndex() const override;

   
  };

  class  While_stmtContext : public Compound_stmtContext {
  public:
    While_stmtContext(Compound_stmtContext *ctx);

    antlr4::tree::TerminalNode *WHILE();
    TestContext *test();
    antlr4::tree::TerminalNode *COLON();
    SuiteContext *suite();
    Else_clauseContext *else_clause();
    virtual void enterRule(antlr4::tree::ParseTreeListener *listener) override;
    virtual void exitRule(antlr4::tree::ParseTreeListener *listener) override;

    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
  };

  class  Func_def_stmtContext : public Compound_stmtContext {
  public:
    Func_def_stmtContext(Compound_stmtContext *ctx);

    FuncdefContext *funcdef();
    std::vector<DecoratorContext *> decorator();
    DecoratorContext* decorator(size_t i);
    virtual void enterRule(antlr4::tree::ParseTreeListener *listener) override;
    virtual void exitRule(antlr4::tree::ParseTreeListener *listener) override;

    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
  };

  class  Try_stmtContext : public Compound_stmtContext {
  public:
    Try_stmtContext(Compound_stmtContext *ctx);

    antlr4::tree::TerminalNode *TRY();
    antlr4::tree::TerminalNode *COLON();
    SuiteContext *suite();
    Finally_clauseContext *finally_clause();
    std::vector<Except_clauseContext *> except_clause();
    Except_clauseContext* except_clause(size_t i);
    Else_clauseContext *else_clause();
    virtual void enterRule(antlr4::tree::ParseTreeListener *listener) override;
    virtual void exitRule(antlr4::tree::ParseTreeListener *listener) override;

    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
  };

  class  If_stmtContext : public Compound_stmtContext {
  public:
    If_stmtContext(Compound_stmtContext *ctx);

    pscriptParser::TestContext *cond = nullptr;
    antlr4::tree::TerminalNode *IF();
    antlr4::tree::TerminalNode *COLON();
    SuiteContext *suite();
    TestContext *test();
    std::vector<Elif_clauseContext *> elif_clause();
    Elif_clauseContext* elif_clause(size_t i);
    Else_clauseContext *else_clause();
    virtual void enterRule(antlr4::tree::ParseTreeListener *listener) override;
    virtual void exitRule(antlr4::tree::ParseTreeListener *listener) override;

    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
  };

  class  With_stmtContext : public Compound_stmtContext {
  public:
    With_stmtContext(Compound_stmtContext *ctx);

    antlr4::tree::TerminalNode *WITH();
    std::vector<With_itemContext *> with_item();
    With_itemContext* with_item(size_t i);
    antlr4::tree::TerminalNode *COLON();
    SuiteContext *suite();
    antlr4::tree::TerminalNode *ASYNC();
    std::vector<antlr4::tree::TerminalNode *> COMMA();
    antlr4::tree::TerminalNode* COMMA(size_t i);
    virtual void enterRule(antlr4::tree::ParseTreeListener *listener) override;
    virtual void exitRule(antlr4::tree::ParseTreeListener *listener) override;

    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
  };

  class  For_stmtContext : public Compound_stmtContext {
  public:
    For_stmtContext(Compound_stmtContext *ctx);

    antlr4::tree::TerminalNode *FOR();
    ExprlistContext *exprlist();
    antlr4::tree::TerminalNode *IN();
    TestlistContext *testlist();
    antlr4::tree::TerminalNode *COLON();
    SuiteContext *suite();
    antlr4::tree::TerminalNode *ASYNC();
    Else_clauseContext *else_clause();
    virtual void enterRule(antlr4::tree::ParseTreeListener *listener) override;
    virtual void exitRule(antlr4::tree::ParseTreeListener *listener) override;

    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
  };

  class  Class_def_stmtContext : public Compound_stmtContext {
  public:
    Class_def_stmtContext(Compound_stmtContext *ctx);

    ClassdefContext *classdef();
    std::vector<DecoratorContext *> decorator();
    DecoratorContext* decorator(size_t i);
    virtual void enterRule(antlr4::tree::ParseTreeListener *listener) override;
    virtual void exitRule(antlr4::tree::ParseTreeListener *listener) override;

    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
  };

  Compound_stmtContext* compound_stmt();

  class  SuiteContext : public antlr4::ParserRuleContext {
  public:
    SuiteContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    Simple_stmtContext *simple_stmt();
    antlr4::tree::TerminalNode *LINE_BREAK();
    antlr4::tree::TerminalNode *INDENT();
    antlr4::tree::TerminalNode *DEDENT();
    std::vector<StmtContext *> stmt();
    StmtContext* stmt(size_t i);

    virtual void enterRule(antlr4::tree::ParseTreeListener *listener) override;
    virtual void exitRule(antlr4::tree::ParseTreeListener *listener) override;

    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  SuiteContext* suite();

  class  DecoratorContext : public antlr4::ParserRuleContext {
  public:
    DecoratorContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *AT();
    Dotted_nameContext *dotted_name();
    antlr4::tree::TerminalNode *LINE_BREAK();
    antlr4::tree::TerminalNode *OPEN_PAREN();
    antlr4::tree::TerminalNode *CLOSE_PAREN();
    ArglistContext *arglist();

    virtual void enterRule(antlr4::tree::ParseTreeListener *listener) override;
    virtual void exitRule(antlr4::tree::ParseTreeListener *listener) override;

    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  DecoratorContext* decorator();

  class  Elif_clauseContext : public antlr4::ParserRuleContext {
  public:
    Elif_clauseContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *ELIF();
    TestContext *test();
    antlr4::tree::TerminalNode *COLON();
    SuiteContext *suite();

    virtual void enterRule(antlr4::tree::ParseTreeListener *listener) override;
    virtual void exitRule(antlr4::tree::ParseTreeListener *listener) override;

    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Elif_clauseContext* elif_clause();

  class  Else_clauseContext : public antlr4::ParserRuleContext {
  public:
    Else_clauseContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *ELSE();
    antlr4::tree::TerminalNode *COLON();
    SuiteContext *suite();

    virtual void enterRule(antlr4::tree::ParseTreeListener *listener) override;
    virtual void exitRule(antlr4::tree::ParseTreeListener *listener) override;

    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Else_clauseContext* else_clause();

  class  Finally_clauseContext : public antlr4::ParserRuleContext {
  public:
    Finally_clauseContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *FINALLY();
    antlr4::tree::TerminalNode *COLON();
    SuiteContext *suite();

    virtual void enterRule(antlr4::tree::ParseTreeListener *listener) override;
    virtual void exitRule(antlr4::tree::ParseTreeListener *listener) override;

    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Finally_clauseContext* finally_clause();

  class  With_itemContext : public antlr4::ParserRuleContext {
  public:
    With_itemContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    TestContext *test();
    antlr4::tree::TerminalNode *AS();
    ExprContext *expr();

    virtual void enterRule(antlr4::tree::ParseTreeListener *listener) override;
    virtual void exitRule(antlr4::tree::ParseTreeListener *listener) override;

    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  With_itemContext* with_item();

  class  Except_clauseContext : public antlr4::ParserRuleContext {
  public:
    Except_clauseContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *EXCEPT();
    antlr4::tree::TerminalNode *COLON();
    SuiteContext *suite();
    TestContext *test();
    antlr4::tree::TerminalNode *AS();
    NameContext *name();

    virtual void enterRule(antlr4::tree::ParseTreeListener *listener) override;
    virtual void exitRule(antlr4::tree::ParseTreeListener *listener) override;

    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Except_clauseContext* except_clause();

  class  ClassdefContext : public antlr4::ParserRuleContext {
  public:
    ClassdefContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *CLASS();
    NameContext *name();
    antlr4::tree::TerminalNode *COLON();
    SuiteContext *suite();
    antlr4::tree::TerminalNode *OPEN_PAREN();
    antlr4::tree::TerminalNode *CLOSE_PAREN();
    ArglistContext *arglist();

    virtual void enterRule(antlr4::tree::ParseTreeListener *listener) override;
    virtual void exitRule(antlr4::tree::ParseTreeListener *listener) override;

    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  ClassdefContext* classdef();

  class  FuncdefContext : public antlr4::ParserRuleContext {
  public:
    FuncdefContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *DEF();
    NameContext *name();
    antlr4::tree::TerminalNode *OPEN_PAREN();
    antlr4::tree::TerminalNode *CLOSE_PAREN();
    antlr4::tree::TerminalNode *COLON();
    SuiteContext *suite();
    antlr4::tree::TerminalNode *ASYNC();
    TypedargslistContext *typedargslist();

    virtual void enterRule(antlr4::tree::ParseTreeListener *listener) override;
    virtual void exitRule(antlr4::tree::ParseTreeListener *listener) override;

    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  FuncdefContext* funcdef();

  class  TypedargslistContext : public antlr4::ParserRuleContext {
  public:
    TypedargslistContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    ArgsContext *args();
    KwargsContext *kwargs();
    std::vector<Def_parametersContext *> def_parameters();
    Def_parametersContext* def_parameters(size_t i);
    std::vector<antlr4::tree::TerminalNode *> COMMA();
    antlr4::tree::TerminalNode* COMMA(size_t i);

    virtual void enterRule(antlr4::tree::ParseTreeListener *listener) override;
    virtual void exitRule(antlr4::tree::ParseTreeListener *listener) override;

    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  TypedargslistContext* typedargslist();

  class  ArgsContext : public antlr4::ParserRuleContext {
  public:
    ArgsContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *STAR();
    Named_parameterContext *named_parameter();

    virtual void enterRule(antlr4::tree::ParseTreeListener *listener) override;
    virtual void exitRule(antlr4::tree::ParseTreeListener *listener) override;

    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  ArgsContext* args();

  class  KwargsContext : public antlr4::ParserRuleContext {
  public:
    KwargsContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *POWER();
    Named_parameterContext *named_parameter();

    virtual void enterRule(antlr4::tree::ParseTreeListener *listener) override;
    virtual void exitRule(antlr4::tree::ParseTreeListener *listener) override;

    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  KwargsContext* kwargs();

  class  Def_parametersContext : public antlr4::ParserRuleContext {
  public:
    Def_parametersContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<Def_parameterContext *> def_parameter();
    Def_parameterContext* def_parameter(size_t i);
    std::vector<antlr4::tree::TerminalNode *> COMMA();
    antlr4::tree::TerminalNode* COMMA(size_t i);

    virtual void enterRule(antlr4::tree::ParseTreeListener *listener) override;
    virtual void exitRule(antlr4::tree::ParseTreeListener *listener) override;

    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Def_parametersContext* def_parameters();

  class  Def_parameterContext : public antlr4::ParserRuleContext {
  public:
    Def_parameterContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    Named_parameterContext *named_parameter();
    antlr4::tree::TerminalNode *ASSIGN();
    TestContext *test();
    antlr4::tree::TerminalNode *STAR();

    virtual void enterRule(antlr4::tree::ParseTreeListener *listener) override;
    virtual void exitRule(antlr4::tree::ParseTreeListener *listener) override;

    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Def_parameterContext* def_parameter();

  class  Named_parameterContext : public antlr4::ParserRuleContext {
  public:
    Named_parameterContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    NameContext *name();
    antlr4::tree::TerminalNode *COLON();
    TestContext *test();

    virtual void enterRule(antlr4::tree::ParseTreeListener *listener) override;
    virtual void exitRule(antlr4::tree::ParseTreeListener *listener) override;

    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Named_parameterContext* named_parameter();

  class  Simple_stmtContext : public antlr4::ParserRuleContext {
  public:
    Simple_stmtContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<Small_stmtContext *> small_stmt();
    Small_stmtContext* small_stmt(size_t i);
    antlr4::tree::TerminalNode *LINE_BREAK();
    antlr4::tree::TerminalNode *EOF();
    std::vector<antlr4::tree::TerminalNode *> SEMI_COLON();
    antlr4::tree::TerminalNode* SEMI_COLON(size_t i);

    virtual void enterRule(antlr4::tree::ParseTreeListener *listener) override;
    virtual void exitRule(antlr4::tree::ParseTreeListener *listener) override;

    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Simple_stmtContext* simple_stmt();

  class  Small_stmtContext : public antlr4::ParserRuleContext {
  public:
    Small_stmtContext(antlr4::ParserRuleContext *parent, size_t invokingState);
   
    Small_stmtContext() = default;
    void copyFrom(Small_stmtContext *context);
    using antlr4::ParserRuleContext::copyFrom;

    virtual size_t getRuleIndex() const override;

   
  };

  class  Assert_stmtContext : public Small_stmtContext {
  public:
    Assert_stmtContext(Small_stmtContext *ctx);

    antlr4::tree::TerminalNode *ASSERT();
    std::vector<TestContext *> test();
    TestContext* test(size_t i);
    antlr4::tree::TerminalNode *COMMA();
    virtual void enterRule(antlr4::tree::ParseTreeListener *listener) override;
    virtual void exitRule(antlr4::tree::ParseTreeListener *listener) override;

    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
  };

  class  Func_call_stmtContext : public Small_stmtContext {
  public:
    Func_call_stmtContext(Small_stmtContext *ctx);

    AtomContext *atom();
    antlr4::tree::TerminalNode *OPEN_PAREN();
    antlr4::tree::TerminalNode *CLOSE_PAREN();
    antlr4::tree::TerminalNode *AWAIT();
    ArglistContext *arglist();
    virtual void enterRule(antlr4::tree::ParseTreeListener *listener) override;
    virtual void exitRule(antlr4::tree::ParseTreeListener *listener) override;

    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
  };

  class  Nonlocal_stmtContext : public Small_stmtContext {
  public:
    Nonlocal_stmtContext(Small_stmtContext *ctx);

    antlr4::tree::TerminalNode *NONLOCAL();
    Comma_nameContext *comma_name();
    virtual void enterRule(antlr4::tree::ParseTreeListener *listener) override;
    virtual void exitRule(antlr4::tree::ParseTreeListener *listener) override;

    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
  };

  class  Pass_stmtContext : public Small_stmtContext {
  public:
    Pass_stmtContext(Small_stmtContext *ctx);

    antlr4::tree::TerminalNode *PASS();
    virtual void enterRule(antlr4::tree::ParseTreeListener *listener) override;
    virtual void exitRule(antlr4::tree::ParseTreeListener *listener) override;

    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
  };

  class  Variable_def_stmtContext : public Small_stmtContext {
  public:
    Variable_def_stmtContext(Small_stmtContext *ctx);

    Variable_defContext *variable_def();
    virtual void enterRule(antlr4::tree::ParseTreeListener *listener) override;
    virtual void exitRule(antlr4::tree::ParseTreeListener *listener) override;

    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
  };

  class  Import_stmtContext : public Small_stmtContext {
  public:
    Import_stmtContext(Small_stmtContext *ctx);

    antlr4::tree::TerminalNode *IMPORT();
    Name_as_namesContext *name_as_names();
    virtual void enterRule(antlr4::tree::ParseTreeListener *listener) override;
    virtual void exitRule(antlr4::tree::ParseTreeListener *listener) override;

    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
  };

  class  From_import_stmtContext : public Small_stmtContext {
  public:
    From_import_stmtContext(Small_stmtContext *ctx);

    antlr4::tree::TerminalNode *FROM();
    From_whereContext *from_where();
    antlr4::tree::TerminalNode *IMPORT();
    antlr4::tree::TerminalNode *STAR();
    antlr4::tree::TerminalNode *OPEN_PAREN();
    Import_as_namesContext *import_as_names();
    antlr4::tree::TerminalNode *CLOSE_PAREN();
    virtual void enterRule(antlr4::tree::ParseTreeListener *listener) override;
    virtual void exitRule(antlr4::tree::ParseTreeListener *listener) override;

    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
  };

  class  Raise_stmtContext : public Small_stmtContext {
  public:
    Raise_stmtContext(Small_stmtContext *ctx);

    antlr4::tree::TerminalNode *RAISE();
    Comma_testContext *comma_test();
    virtual void enterRule(antlr4::tree::ParseTreeListener *listener) override;
    virtual void exitRule(antlr4::tree::ParseTreeListener *listener) override;

    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
  };

  class  Yield_stmtContext : public Small_stmtContext {
  public:
    Yield_stmtContext(Small_stmtContext *ctx);

    Yield_exprContext *yield_expr();
    virtual void enterRule(antlr4::tree::ParseTreeListener *listener) override;
    virtual void exitRule(antlr4::tree::ParseTreeListener *listener) override;

    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
  };

  class  Global_stmtContext : public Small_stmtContext {
  public:
    Global_stmtContext(Small_stmtContext *ctx);

    antlr4::tree::TerminalNode *GLOBAL();
    Comma_nameContext *comma_name();
    virtual void enterRule(antlr4::tree::ParseTreeListener *listener) override;
    virtual void exitRule(antlr4::tree::ParseTreeListener *listener) override;

    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
  };

  class  Continue_stmtContext : public Small_stmtContext {
  public:
    Continue_stmtContext(Small_stmtContext *ctx);

    antlr4::tree::TerminalNode *CONTINUE();
    virtual void enterRule(antlr4::tree::ParseTreeListener *listener) override;
    virtual void exitRule(antlr4::tree::ParseTreeListener *listener) override;

    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
  };

  class  Break_stmtContext : public Small_stmtContext {
  public:
    Break_stmtContext(Small_stmtContext *ctx);

    antlr4::tree::TerminalNode *BREAK();
    virtual void enterRule(antlr4::tree::ParseTreeListener *listener) override;
    virtual void exitRule(antlr4::tree::ParseTreeListener *listener) override;

    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
  };

  class  Del_stmtContext : public Small_stmtContext {
  public:
    Del_stmtContext(Small_stmtContext *ctx);

    antlr4::tree::TerminalNode *DEL();
    ExprlistContext *exprlist();
    virtual void enterRule(antlr4::tree::ParseTreeListener *listener) override;
    virtual void exitRule(antlr4::tree::ParseTreeListener *listener) override;

    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
  };

  class  Return_stmtContext : public Small_stmtContext {
  public:
    Return_stmtContext(Small_stmtContext *ctx);

    antlr4::tree::TerminalNode *RETURN();
    TestlistContext *testlist();
    virtual void enterRule(antlr4::tree::ParseTreeListener *listener) override;
    virtual void exitRule(antlr4::tree::ParseTreeListener *listener) override;

    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
  };

  Small_stmtContext* small_stmt();

  class  Variable_defContext : public antlr4::ParserRuleContext {
  public:
    Variable_defContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    Variable_def_consts_with_colonContext *variable_def_consts_with_colon();
    Variable_def_nameContext *variable_def_name();
    antlr4::tree::TerminalNode *SEMI_COLON();
    Variable_def_constsContext *variable_def_consts();
    Assign_partContext *assign_part();
    Variable_def_comma_nameContext *variable_def_comma_name();

    virtual void enterRule(antlr4::tree::ParseTreeListener *listener) override;
    virtual void exitRule(antlr4::tree::ParseTreeListener *listener) override;

    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Variable_defContext* variable_def();

  class  Variable_def_nameContext : public antlr4::ParserRuleContext {
  public:
    Variable_def_nameContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    Dotted_nameContext *dotted_name();
    std::vector<antlr4::tree::TerminalNode *> OPEN_BRACKET();
    antlr4::tree::TerminalNode* OPEN_BRACKET(size_t i);
    std::vector<ExprContext *> expr();
    ExprContext* expr(size_t i);
    std::vector<antlr4::tree::TerminalNode *> CLOSE_BRACKET();
    antlr4::tree::TerminalNode* CLOSE_BRACKET(size_t i);
    antlr4::tree::TerminalNode *DOT();
    Variable_def_nameContext *variable_def_name();

    virtual void enterRule(antlr4::tree::ParseTreeListener *listener) override;
    virtual void exitRule(antlr4::tree::ParseTreeListener *listener) override;

    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Variable_def_nameContext* variable_def_name();

  class  Variable_def_comma_nameContext : public antlr4::ParserRuleContext {
  public:
    Variable_def_comma_nameContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<Variable_def_nameContext *> variable_def_name();
    Variable_def_nameContext* variable_def_name(size_t i);
    std::vector<antlr4::tree::TerminalNode *> COMMA();
    antlr4::tree::TerminalNode* COMMA(size_t i);

    virtual void enterRule(antlr4::tree::ParseTreeListener *listener) override;
    virtual void exitRule(antlr4::tree::ParseTreeListener *listener) override;

    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Variable_def_comma_nameContext* variable_def_comma_name();

  class  From_whereContext : public antlr4::ParserRuleContext {
  public:
    From_whereContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    Dotted_nameContext *dotted_name();
    std::vector<antlr4::tree::TerminalNode *> DOT();
    antlr4::tree::TerminalNode* DOT(size_t i);

    virtual void enterRule(antlr4::tree::ParseTreeListener *listener) override;
    virtual void exitRule(antlr4::tree::ParseTreeListener *listener) override;

    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  From_whereContext* from_where();

  class  Comma_nameContext : public antlr4::ParserRuleContext {
  public:
    Comma_nameContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<Dotted_nameContext *> dotted_name();
    Dotted_nameContext* dotted_name(size_t i);
    std::vector<antlr4::tree::TerminalNode *> COMMA();
    antlr4::tree::TerminalNode* COMMA(size_t i);

    virtual void enterRule(antlr4::tree::ParseTreeListener *listener) override;
    virtual void exitRule(antlr4::tree::ParseTreeListener *listener) override;

    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Comma_nameContext* comma_name();

  class  Comma_testContext : public antlr4::ParserRuleContext {
  public:
    Comma_testContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<TestContext *> test();
    TestContext* test(size_t i);
    std::vector<antlr4::tree::TerminalNode *> COMMA();
    antlr4::tree::TerminalNode* COMMA(size_t i);

    virtual void enterRule(antlr4::tree::ParseTreeListener *listener) override;
    virtual void exitRule(antlr4::tree::ParseTreeListener *listener) override;

    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Comma_testContext* comma_test();

  class  Variable_def_constsContext : public antlr4::ParserRuleContext {
  public:
    antlr4::Token *variable_const = nullptr;
    Variable_def_constsContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *VAR();
    antlr4::tree::TerminalNode *CONST();
    antlr4::tree::TerminalNode *LET();

    virtual void enterRule(antlr4::tree::ParseTreeListener *listener) override;
    virtual void exitRule(antlr4::tree::ParseTreeListener *listener) override;

    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Variable_def_constsContext* variable_def_consts();

  class  Variable_def_consts_with_colonContext : public antlr4::ParserRuleContext {
  public:
    antlr4::Token *variable_const = nullptr;
    Variable_def_consts_with_colonContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *VAR();
    antlr4::tree::TerminalNode *LET();

    virtual void enterRule(antlr4::tree::ParseTreeListener *listener) override;
    virtual void exitRule(antlr4::tree::ParseTreeListener *listener) override;

    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Variable_def_consts_with_colonContext* variable_def_consts_with_colon();

  class  Testlist_star_exprContext : public antlr4::ParserRuleContext {
  public:
    Testlist_star_exprContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<TestContext *> test();
    TestContext* test(size_t i);
    std::vector<antlr4::tree::TerminalNode *> COMMA();
    antlr4::tree::TerminalNode* COMMA(size_t i);
    TestlistContext *testlist();

    virtual void enterRule(antlr4::tree::ParseTreeListener *listener) override;
    virtual void exitRule(antlr4::tree::ParseTreeListener *listener) override;

    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Testlist_star_exprContext* testlist_star_expr();

  class  Star_exprContext : public antlr4::ParserRuleContext {
  public:
    Star_exprContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *STAR();
    ExprContext *expr();

    virtual void enterRule(antlr4::tree::ParseTreeListener *listener) override;
    virtual void exitRule(antlr4::tree::ParseTreeListener *listener) override;

    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Star_exprContext* star_expr();

  class  Assign_partContext : public antlr4::ParserRuleContext {
  public:
    antlr4::Token *op = nullptr;
    Assign_partContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *ASSIGN();
    antlr4::tree::TerminalNode *ADD_ASSIGN();
    antlr4::tree::TerminalNode *SUB_ASSIGN();
    antlr4::tree::TerminalNode *MULT_ASSIGN();
    antlr4::tree::TerminalNode *DIV_ASSIGN();
    antlr4::tree::TerminalNode *MOD_ASSIGN();
    antlr4::tree::TerminalNode *XOR_ASSIGN();
    antlr4::tree::TerminalNode *POWER_ASSIGN();
    antlr4::tree::TerminalNode *IDIV_ASSIGN();
    Yield_exprContext *yield_expr();
    TestlistContext *testlist();

    virtual void enterRule(antlr4::tree::ParseTreeListener *listener) override;
    virtual void exitRule(antlr4::tree::ParseTreeListener *listener) override;

    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Assign_partContext* assign_part();

  class  ExprlistContext : public antlr4::ParserRuleContext {
  public:
    ExprlistContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<ExprContext *> expr();
    ExprContext* expr(size_t i);
    std::vector<antlr4::tree::TerminalNode *> COMMA();
    antlr4::tree::TerminalNode* COMMA(size_t i);

    virtual void enterRule(antlr4::tree::ParseTreeListener *listener) override;
    virtual void exitRule(antlr4::tree::ParseTreeListener *listener) override;

    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  ExprlistContext* exprlist();

  class  Import_as_namesContext : public antlr4::ParserRuleContext {
  public:
    Import_as_namesContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<Import_as_nameContext *> import_as_name();
    Import_as_nameContext* import_as_name(size_t i);
    std::vector<antlr4::tree::TerminalNode *> COMMA();
    antlr4::tree::TerminalNode* COMMA(size_t i);

    virtual void enterRule(antlr4::tree::ParseTreeListener *listener) override;
    virtual void exitRule(antlr4::tree::ParseTreeListener *listener) override;

    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Import_as_namesContext* import_as_names();

  class  Import_as_nameContext : public antlr4::ParserRuleContext {
  public:
    Import_as_nameContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<NameContext *> name();
    NameContext* name(size_t i);
    antlr4::tree::TerminalNode *AS();

    virtual void enterRule(antlr4::tree::ParseTreeListener *listener) override;
    virtual void exitRule(antlr4::tree::ParseTreeListener *listener) override;

    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Import_as_nameContext* import_as_name();

  class  Name_as_namesContext : public antlr4::ParserRuleContext {
  public:
    Name_as_namesContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<Name_as_nameContext *> name_as_name();
    Name_as_nameContext* name_as_name(size_t i);
    std::vector<antlr4::tree::TerminalNode *> COMMA();
    antlr4::tree::TerminalNode* COMMA(size_t i);

    virtual void enterRule(antlr4::tree::ParseTreeListener *listener) override;
    virtual void exitRule(antlr4::tree::ParseTreeListener *listener) override;

    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Name_as_namesContext* name_as_names();

  class  Name_as_nameContext : public antlr4::ParserRuleContext {
  public:
    Name_as_nameContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<NameContext *> name();
    NameContext* name(size_t i);
    antlr4::tree::TerminalNode *AS();

    virtual void enterRule(antlr4::tree::ParseTreeListener *listener) override;
    virtual void exitRule(antlr4::tree::ParseTreeListener *listener) override;

    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Name_as_nameContext* name_as_name();

  class  TestContext : public antlr4::ParserRuleContext {
  public:
    TestContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<Logical_testContext *> logical_test();
    Logical_testContext* logical_test(size_t i);
    antlr4::tree::TerminalNode *IF();
    antlr4::tree::TerminalNode *ELSE();
    TestContext *test();
    antlr4::tree::TerminalNode *LAMBDA();
    antlr4::tree::TerminalNode *COLON();
    VarargslistContext *varargslist();

    virtual void enterRule(antlr4::tree::ParseTreeListener *listener) override;
    virtual void exitRule(antlr4::tree::ParseTreeListener *listener) override;

    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  TestContext* test();

  class  VarargslistContext : public antlr4::ParserRuleContext {
  public:
    VarargslistContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    VarargsContext *varargs();
    VarkwargsContext *varkwargs();
    std::vector<Vardef_parametersContext *> vardef_parameters();
    Vardef_parametersContext* vardef_parameters(size_t i);
    std::vector<antlr4::tree::TerminalNode *> COMMA();
    antlr4::tree::TerminalNode* COMMA(size_t i);

    virtual void enterRule(antlr4::tree::ParseTreeListener *listener) override;
    virtual void exitRule(antlr4::tree::ParseTreeListener *listener) override;

    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  VarargslistContext* varargslist();

  class  Vardef_parametersContext : public antlr4::ParserRuleContext {
  public:
    Vardef_parametersContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<Vardef_parameterContext *> vardef_parameter();
    Vardef_parameterContext* vardef_parameter(size_t i);
    std::vector<antlr4::tree::TerminalNode *> COMMA();
    antlr4::tree::TerminalNode* COMMA(size_t i);

    virtual void enterRule(antlr4::tree::ParseTreeListener *listener) override;
    virtual void exitRule(antlr4::tree::ParseTreeListener *listener) override;

    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Vardef_parametersContext* vardef_parameters();

  class  Vardef_parameterContext : public antlr4::ParserRuleContext {
  public:
    Vardef_parameterContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    NameContext *name();
    antlr4::tree::TerminalNode *ASSIGN();
    TestContext *test();
    antlr4::tree::TerminalNode *STAR();

    virtual void enterRule(antlr4::tree::ParseTreeListener *listener) override;
    virtual void exitRule(antlr4::tree::ParseTreeListener *listener) override;

    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Vardef_parameterContext* vardef_parameter();

  class  VarargsContext : public antlr4::ParserRuleContext {
  public:
    VarargsContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *STAR();
    NameContext *name();

    virtual void enterRule(antlr4::tree::ParseTreeListener *listener) override;
    virtual void exitRule(antlr4::tree::ParseTreeListener *listener) override;

    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  VarargsContext* varargs();

  class  VarkwargsContext : public antlr4::ParserRuleContext {
  public:
    VarkwargsContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *POWER();
    NameContext *name();

    virtual void enterRule(antlr4::tree::ParseTreeListener *listener) override;
    virtual void exitRule(antlr4::tree::ParseTreeListener *listener) override;

    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  VarkwargsContext* varkwargs();

  class  Logical_testContext : public antlr4::ParserRuleContext {
  public:
    antlr4::Token *op = nullptr;
    Logical_testContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    ComparisonContext *comparison();
    antlr4::tree::TerminalNode *NOT();
    std::vector<Logical_testContext *> logical_test();
    Logical_testContext* logical_test(size_t i);
    antlr4::tree::TerminalNode *AND();
    antlr4::tree::TerminalNode *OR();

    virtual void enterRule(antlr4::tree::ParseTreeListener *listener) override;
    virtual void exitRule(antlr4::tree::ParseTreeListener *listener) override;

    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Logical_testContext* logical_test();
  Logical_testContext* logical_test(int precedence);
  class  ComparisonContext : public antlr4::ParserRuleContext {
  public:
    antlr4::Token *optional = nullptr;
    ComparisonContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    ExprContext *expr();
    std::vector<ComparisonContext *> comparison();
    ComparisonContext* comparison(size_t i);
    antlr4::tree::TerminalNode *LESS_THAN();
    antlr4::tree::TerminalNode *GREATER_THAN();
    antlr4::tree::TerminalNode *EQUALS();
    antlr4::tree::TerminalNode *GT_EQ();
    antlr4::tree::TerminalNode *LT_EQ();
    antlr4::tree::TerminalNode *NOT_EQ_1();
    antlr4::tree::TerminalNode *NOT_EQ_2();
    antlr4::tree::TerminalNode *IN();
    antlr4::tree::TerminalNode *IS();
    antlr4::tree::TerminalNode *NOT();

    virtual void enterRule(antlr4::tree::ParseTreeListener *listener) override;
    virtual void exitRule(antlr4::tree::ParseTreeListener *listener) override;

    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  ComparisonContext* comparison();
  ComparisonContext* comparison(int precedence);
  class  ExprContext : public antlr4::ParserRuleContext {
  public:
    antlr4::Token *op = nullptr;
    ExprContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    AtomContext *atom();
    antlr4::tree::TerminalNode *AWAIT();
    std::vector<TrailerContext *> trailer();
    TrailerContext* trailer(size_t i);
    std::vector<ExprContext *> expr();
    ExprContext* expr(size_t i);
    antlr4::tree::TerminalNode *ADD();
    antlr4::tree::TerminalNode *MINUS();
    antlr4::tree::TerminalNode *NOT_OP();
    antlr4::tree::TerminalNode *STAR();
    antlr4::tree::TerminalNode *DIV();
    antlr4::tree::TerminalNode *MOD();
    antlr4::tree::TerminalNode *IDIV();
    antlr4::tree::TerminalNode *POWER();

    virtual void enterRule(antlr4::tree::ParseTreeListener *listener) override;
    virtual void exitRule(antlr4::tree::ParseTreeListener *listener) override;

    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  ExprContext* expr();
  ExprContext* expr(int precedence);
  class  AtomContext : public antlr4::ParserRuleContext {
  public:
    AtomContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *OPEN_PAREN();
    antlr4::tree::TerminalNode *CLOSE_PAREN();
    Yield_exprContext *yield_expr();
    TestlistContext *testlist();
    antlr4::tree::TerminalNode *OPEN_BRACKET();
    antlr4::tree::TerminalNode *CLOSE_BRACKET();
    antlr4::tree::TerminalNode *OPEN_BRACE();
    antlr4::tree::TerminalNode *CLOSE_BRACE();
    DictmakerContext *dictmaker();
    SetmakerContext *setmaker();
    std::vector<antlr4::tree::TerminalNode *> REVERSE_QUOTE();
    antlr4::tree::TerminalNode* REVERSE_QUOTE(size_t i);
    antlr4::tree::TerminalNode *COMMA();
    NameContext *name();
    NumberContext *number();
    antlr4::tree::TerminalNode *MINUS();
    antlr4::tree::TerminalNode *NONE();
    std::vector<antlr4::tree::TerminalNode *> STRING();
    antlr4::tree::TerminalNode* STRING(size_t i);

    virtual void enterRule(antlr4::tree::ParseTreeListener *listener) override;
    virtual void exitRule(antlr4::tree::ParseTreeListener *listener) override;

    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  AtomContext* atom();

  class  DictmakerContext : public antlr4::ParserRuleContext {
  public:
    DictmakerContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<TestContext *> test();
    TestContext* test(size_t i);
    std::vector<antlr4::tree::TerminalNode *> COLON();
    antlr4::tree::TerminalNode* COLON(size_t i);
    std::vector<antlr4::tree::TerminalNode *> POWER();
    antlr4::tree::TerminalNode* POWER(size_t i);
    std::vector<ExprContext *> expr();
    ExprContext* expr(size_t i);
    std::vector<antlr4::tree::TerminalNode *> COMMA();
    antlr4::tree::TerminalNode* COMMA(size_t i);

    virtual void enterRule(antlr4::tree::ParseTreeListener *listener) override;
    virtual void exitRule(antlr4::tree::ParseTreeListener *listener) override;

    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  DictmakerContext* dictmaker();

  class  SetmakerContext : public antlr4::ParserRuleContext {
  public:
    SetmakerContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    TestlistContext *testlist();

    virtual void enterRule(antlr4::tree::ParseTreeListener *listener) override;
    virtual void exitRule(antlr4::tree::ParseTreeListener *listener) override;

    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  SetmakerContext* setmaker();

  class  TestlistContext : public antlr4::ParserRuleContext {
  public:
    TestlistContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<TestContext *> test();
    TestContext* test(size_t i);
    std::vector<antlr4::tree::TerminalNode *> COMMA();
    antlr4::tree::TerminalNode* COMMA(size_t i);

    virtual void enterRule(antlr4::tree::ParseTreeListener *listener) override;
    virtual void exitRule(antlr4::tree::ParseTreeListener *listener) override;

    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  TestlistContext* testlist();

  class  Dotted_nameContext : public antlr4::ParserRuleContext {
  public:
    Dotted_nameContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    NameContext *name();
    Dotted_nameContext *dotted_name();
    antlr4::tree::TerminalNode *DOT();

    virtual void enterRule(antlr4::tree::ParseTreeListener *listener) override;
    virtual void exitRule(antlr4::tree::ParseTreeListener *listener) override;

    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Dotted_nameContext* dotted_name();
  Dotted_nameContext* dotted_name(int precedence);
  class  NameContext : public antlr4::ParserRuleContext {
  public:
    NameContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *NAME();
    BoolContext *bool_();

    virtual void enterRule(antlr4::tree::ParseTreeListener *listener) override;
    virtual void exitRule(antlr4::tree::ParseTreeListener *listener) override;

    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  NameContext* name();

  class  BoolContext : public antlr4::ParserRuleContext {
  public:
    BoolContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *TRUE();
    antlr4::tree::TerminalNode *FALSE();

    virtual void enterRule(antlr4::tree::ParseTreeListener *listener) override;
    virtual void exitRule(antlr4::tree::ParseTreeListener *listener) override;

    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  BoolContext* bool_();

  class  NumberContext : public antlr4::ParserRuleContext {
  public:
    NumberContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    IntegerContext *integer();
    antlr4::tree::TerminalNode *IMAG_NUMBER();
    antlr4::tree::TerminalNode *FLOAT_NUMBER();

    virtual void enterRule(antlr4::tree::ParseTreeListener *listener) override;
    virtual void exitRule(antlr4::tree::ParseTreeListener *listener) override;

    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  NumberContext* number();

  class  IntegerContext : public antlr4::ParserRuleContext {
  public:
    IntegerContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *DECIMAL_INTEGER();
    antlr4::tree::TerminalNode *OCT_INTEGER();
    antlr4::tree::TerminalNode *HEX_INTEGER();
    antlr4::tree::TerminalNode *BIN_INTEGER();

    virtual void enterRule(antlr4::tree::ParseTreeListener *listener) override;
    virtual void exitRule(antlr4::tree::ParseTreeListener *listener) override;

    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  IntegerContext* integer();

  class  Yield_exprContext : public antlr4::ParserRuleContext {
  public:
    Yield_exprContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *YIELD();
    Yield_argContext *yield_arg();

    virtual void enterRule(antlr4::tree::ParseTreeListener *listener) override;
    virtual void exitRule(antlr4::tree::ParseTreeListener *listener) override;

    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Yield_exprContext* yield_expr();

  class  Yield_argContext : public antlr4::ParserRuleContext {
  public:
    Yield_argContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    TestlistContext *testlist();

    virtual void enterRule(antlr4::tree::ParseTreeListener *listener) override;
    virtual void exitRule(antlr4::tree::ParseTreeListener *listener) override;

    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Yield_argContext* yield_arg();

  class  TrailerContext : public antlr4::ParserRuleContext {
  public:
    TrailerContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *DOT();
    NameContext *name();
    ArgumentsContext *arguments();

    virtual void enterRule(antlr4::tree::ParseTreeListener *listener) override;
    virtual void exitRule(antlr4::tree::ParseTreeListener *listener) override;

    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  TrailerContext* trailer();

  class  ArgumentsContext : public antlr4::ParserRuleContext {
  public:
    ArgumentsContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *OPEN_PAREN();
    antlr4::tree::TerminalNode *CLOSE_PAREN();
    ArglistContext *arglist();
    antlr4::tree::TerminalNode *OPEN_BRACKET();
    SubscriptlistContext *subscriptlist();
    antlr4::tree::TerminalNode *CLOSE_BRACKET();

    virtual void enterRule(antlr4::tree::ParseTreeListener *listener) override;
    virtual void exitRule(antlr4::tree::ParseTreeListener *listener) override;

    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  ArgumentsContext* arguments();

  class  ArglistContext : public antlr4::ParserRuleContext {
  public:
    ArglistContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<ArgumentContext *> argument();
    ArgumentContext* argument(size_t i);
    std::vector<antlr4::tree::TerminalNode *> COMMA();
    antlr4::tree::TerminalNode* COMMA(size_t i);

    virtual void enterRule(antlr4::tree::ParseTreeListener *listener) override;
    virtual void exitRule(antlr4::tree::ParseTreeListener *listener) override;

    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  ArglistContext* arglist();

  class  ArgumentContext : public antlr4::ParserRuleContext {
  public:
    ArgumentContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<TestContext *> test();
    TestContext* test(size_t i);
    antlr4::tree::TerminalNode *ASSIGN();
    antlr4::tree::TerminalNode *POWER();
    antlr4::tree::TerminalNode *STAR();

    virtual void enterRule(antlr4::tree::ParseTreeListener *listener) override;
    virtual void exitRule(antlr4::tree::ParseTreeListener *listener) override;

    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  ArgumentContext* argument();

  class  SubscriptlistContext : public antlr4::ParserRuleContext {
  public:
    SubscriptlistContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<SubscriptContext *> subscript();
    SubscriptContext* subscript(size_t i);
    std::vector<antlr4::tree::TerminalNode *> COMMA();
    antlr4::tree::TerminalNode* COMMA(size_t i);

    virtual void enterRule(antlr4::tree::ParseTreeListener *listener) override;
    virtual void exitRule(antlr4::tree::ParseTreeListener *listener) override;

    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  SubscriptlistContext* subscriptlist();

  class  SubscriptContext : public antlr4::ParserRuleContext {
  public:
    SubscriptContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<TestContext *> test();
    TestContext* test(size_t i);
    antlr4::tree::TerminalNode *COLON();
    SliceopContext *sliceop();

    virtual void enterRule(antlr4::tree::ParseTreeListener *listener) override;
    virtual void exitRule(antlr4::tree::ParseTreeListener *listener) override;

    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  SubscriptContext* subscript();

  class  SliceopContext : public antlr4::ParserRuleContext {
  public:
    SliceopContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *COLON();
    TestContext *test();

    virtual void enterRule(antlr4::tree::ParseTreeListener *listener) override;
    virtual void exitRule(antlr4::tree::ParseTreeListener *listener) override;

    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  SliceopContext* sliceop();

  class  Comp_forContext : public antlr4::ParserRuleContext {
  public:
    Comp_forContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *FOR();
    ExprlistContext *exprlist();
    antlr4::tree::TerminalNode *IN();
    Logical_testContext *logical_test();
    Comp_iterContext *comp_iter();

    virtual void enterRule(antlr4::tree::ParseTreeListener *listener) override;
    virtual void exitRule(antlr4::tree::ParseTreeListener *listener) override;

    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Comp_forContext* comp_for();

  class  Comp_iterContext : public antlr4::ParserRuleContext {
  public:
    Comp_iterContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    Comp_forContext *comp_for();
    antlr4::tree::TerminalNode *IF();
    TestContext *test();
    Comp_iterContext *comp_iter();

    virtual void enterRule(antlr4::tree::ParseTreeListener *listener) override;
    virtual void exitRule(antlr4::tree::ParseTreeListener *listener) override;

    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Comp_iterContext* comp_iter();


  bool sempred(antlr4::RuleContext *_localctx, size_t ruleIndex, size_t predicateIndex) override;

  bool logical_testSempred(Logical_testContext *_localctx, size_t predicateIndex);
  bool comparisonSempred(ComparisonContext *_localctx, size_t predicateIndex);
  bool exprSempred(ExprContext *_localctx, size_t predicateIndex);
  bool dotted_nameSempred(Dotted_nameContext *_localctx, size_t predicateIndex);

  // By default the static state used to implement the parser is lazily initialized during the first
  // call to the constructor. You can call this function if you wish to initialize the static state
  // ahead of time.
  static void initialize();

private:
};

