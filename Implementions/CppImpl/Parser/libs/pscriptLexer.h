
// Generated from ./pscriptLexer.g4 by ANTLR 4.13.0

#pragma once


#include "antlr4-runtime.h"




class  pscriptLexer : public pscriptLexerBase {
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

  explicit pscriptLexer(antlr4::CharStream *input);

  ~pscriptLexer() override;


  std::string getGrammarFileName() const override;

  const std::vector<std::string>& getRuleNames() const override;

  const std::vector<std::string>& getChannelNames() const override;

  const std::vector<std::string>& getModeNames() const override;

  const antlr4::dfa::Vocabulary& getVocabulary() const override;

  antlr4::atn::SerializedATNView getSerializedATN() const override;

  const antlr4::atn::ATN& getATN() const override;

  void action(antlr4::RuleContext *context, size_t ruleIndex, size_t actionIndex) override;

  // By default the static state used to implement the lexer is lazily initialized during the first
  // call to the constructor. You can call this function if you wish to initialize the static state
  // ahead of time.
  static void initialize();

private:

  // Individual action functions triggered by action() above.
  void OPEN_PARENAction(antlr4::RuleContext *context, size_t actionIndex);
  void CLOSE_PARENAction(antlr4::RuleContext *context, size_t actionIndex);
  void OPEN_BRACEAction(antlr4::RuleContext *context, size_t actionIndex);
  void CLOSE_BRACEAction(antlr4::RuleContext *context, size_t actionIndex);
  void OPEN_BRACKETAction(antlr4::RuleContext *context, size_t actionIndex);
  void CLOSE_BRACKETAction(antlr4::RuleContext *context, size_t actionIndex);
  void NEWLINEAction(antlr4::RuleContext *context, size_t actionIndex);
  void WSAction(antlr4::RuleContext *context, size_t actionIndex);

  // Individual semantic predicate functions triggered by sempred() above.

};

