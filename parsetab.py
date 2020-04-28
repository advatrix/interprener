
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'nonassocIFXnonassocIFYnonassocELUNDleftPLUSMINUSnonassocGREATERLESSASSIGN BACKWARD BOOL BOX CARET CBRACKET CELL COMMA CSQBRACKET DECIMAL DO DONE DROP ELDEF ELUND EMPTY EQUAL EXIT FALSE FINISH FORWARD FUNCTION GREATER HEXADECIMAL IDENT IF INF INT LEFT LESS LOAD LOOK MINUS MINUS_INF NAN NL OBRACKET OSQBRACKET PLUS RETURN RIGHT SHARP SIZEOF TEST TRUE UNDEF VAR WALL WHILEprogram : stmt_listempty : stmt_list : stmt_list statement\n        | statementstatement : declaration_list NL\n        | assignment NL\n        | while NL\n        | if\n        | operator NL\n        | function NL\n        | function_call NL\n        | RETURN NL\n        | empty NL\n        declaration_list : type vars_listtype : INT\n        | CELL\n        | BOOL\n        | VAR\n        vars_list : IDENT COMMA vars_listvars_list : assignment COMMA vars_listvars_list : IDENTvars_list : assignmentassignment : variable ASSIGN expression\n        | variable ASSIGN arrayarray : OSQBRACKET expr_list CSQBRACKETexpr_list : expr_list COMMA expression\n        | expressionvariable : IDENT OBRACKET expression CBRACKET\n        | IDENTexpression : variable\n        | const\n        | al_expression\n        | function_call\n        | operatorconst : INF\n        | MINUS_INF\n        | NAN\n        | TRUE\n        | FALSE\n        | UNDEF\n        | EMPTY\n        | WALL\n        | BOX\n        | EXIT\n        | DECIMAL\n        | HEXADECIMALal_expression : expression PLUS expression\n        | expression MINUS expression\n        | MINUS expression\n        | SHARP expression\n        | expression CARET expression\n        | expression GREATER expression\n        | expression LESS expression\n        | expression EQUAL expressionfunction_call : IDENT OBRACKET variable CBRACKEToperator : FORWARD expression\n        | BACKWARD expression\n        | LEFT\n        | RIGHT\n        | LOAD expression\n        | DROP expression\n        | LOOK\n        | TEST\n        | SIZEOF variablewhile : WHILE expression DO stmt_list DONE\n        | WHILE expression DO stmt_list FINISH stmt_list DONEif : IF expression DO stmt_list DONE NL %prec IFXif : IF expression DO stmt_list DONE NL ELDEF DO stmt_list DONE NL %prec IFYif : IF expression DO stmt_list DONE NL ELUND DO stmt_list DONE NL %prec IFYif : IF expression DO stmt_list DONE NL ELDEF DO stmt_list DONE NL ELUND DO stmt_list DONEfunction : FUNCTION OBRACKET IDENT CBRACKET DO stmt_list DONEfunction : FUNCTION IDENT OBRACKET IDENT CBRACKET DO NL stmt_list DONE'
    
_lr_action_items = {'RETURN':([0,2,3,7,32,33,34,35,36,37,38,39,40,82,92,101,108,116,118,121,122,123,129,130,131,132,133,134,138,139,141,142,143,],[11,11,-4,-8,-3,-5,-6,-7,-9,-10,-11,-12,-13,11,11,11,11,11,11,11,-67,11,11,11,11,11,11,11,-68,-69,11,11,-70,]),'WHILE':([0,2,3,7,32,33,34,35,36,37,38,39,40,82,92,101,108,116,118,121,122,123,129,130,131,132,133,134,138,139,141,142,143,],[15,15,-4,-8,-3,-5,-6,-7,-9,-10,-11,-12,-13,15,15,15,15,15,15,15,-67,15,15,15,15,15,15,15,-68,-69,15,15,-70,]),'IF':([0,2,3,7,32,33,34,35,36,37,38,39,40,82,92,101,108,116,118,121,122,123,129,130,131,132,133,134,138,139,141,142,143,],[16,16,-4,-8,-3,-5,-6,-7,-9,-10,-11,-12,-13,16,16,16,16,16,16,16,-67,16,16,16,16,16,16,16,-68,-69,16,16,-70,]),'FORWARD':([0,2,3,7,15,16,17,18,21,22,32,33,34,35,36,37,38,39,40,44,64,65,75,77,81,82,83,84,85,86,87,88,89,92,101,108,114,116,118,121,122,123,129,130,131,132,133,134,138,139,141,142,143,],[17,17,-4,-8,17,17,17,17,17,17,-3,-5,-6,-7,-9,-10,-11,-12,-13,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,-67,17,17,17,17,17,17,17,-68,-69,17,17,-70,]),'BACKWARD':([0,2,3,7,15,16,17,18,21,22,32,33,34,35,36,37,38,39,40,44,64,65,75,77,81,82,83,84,85,86,87,88,89,92,101,108,114,116,118,121,122,123,129,130,131,132,133,134,138,139,141,142,143,],[18,18,-4,-8,18,18,18,18,18,18,-3,-5,-6,-7,-9,-10,-11,-12,-13,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,-67,18,18,18,18,18,18,18,-68,-69,18,18,-70,]),'LEFT':([0,2,3,7,15,16,17,18,21,22,32,33,34,35,36,37,38,39,40,44,64,65,75,77,81,82,83,84,85,86,87,88,89,92,101,108,114,116,118,121,122,123,129,130,131,132,133,134,138,139,141,142,143,],[19,19,-4,-8,19,19,19,19,19,19,-3,-5,-6,-7,-9,-10,-11,-12,-13,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,-67,19,19,19,19,19,19,19,-68,-69,19,19,-70,]),'RIGHT':([0,2,3,7,15,16,17,18,21,22,32,33,34,35,36,37,38,39,40,44,64,65,75,77,81,82,83,84,85,86,87,88,89,92,101,108,114,116,118,121,122,123,129,130,131,132,133,134,138,139,141,142,143,],[20,20,-4,-8,20,20,20,20,20,20,-3,-5,-6,-7,-9,-10,-11,-12,-13,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,-67,20,20,20,20,20,20,20,-68,-69,20,20,-70,]),'LOAD':([0,2,3,7,15,16,17,18,21,22,32,33,34,35,36,37,38,39,40,44,64,65,75,77,81,82,83,84,85,86,87,88,89,92,101,108,114,116,118,121,122,123,129,130,131,132,133,134,138,139,141,142,143,],[21,21,-4,-8,21,21,21,21,21,21,-3,-5,-6,-7,-9,-10,-11,-12,-13,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,-67,21,21,21,21,21,21,21,-68,-69,21,21,-70,]),'DROP':([0,2,3,7,15,16,17,18,21,22,32,33,34,35,36,37,38,39,40,44,64,65,75,77,81,82,83,84,85,86,87,88,89,92,101,108,114,116,118,121,122,123,129,130,131,132,133,134,138,139,141,142,143,],[22,22,-4,-8,22,22,22,22,22,22,-3,-5,-6,-7,-9,-10,-11,-12,-13,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,-67,22,22,22,22,22,22,22,-68,-69,22,22,-70,]),'LOOK':([0,2,3,7,15,16,17,18,21,22,32,33,34,35,36,37,38,39,40,44,64,65,75,77,81,82,83,84,85,86,87,88,89,92,101,108,114,116,118,121,122,123,129,130,131,132,133,134,138,139,141,142,143,],[23,23,-4,-8,23,23,23,23,23,23,-3,-5,-6,-7,-9,-10,-11,-12,-13,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,-67,23,23,23,23,23,23,23,-68,-69,23,23,-70,]),'TEST':([0,2,3,7,15,16,17,18,21,22,32,33,34,35,36,37,38,39,40,44,64,65,75,77,81,82,83,84,85,86,87,88,89,92,101,108,114,116,118,121,122,123,129,130,131,132,133,134,138,139,141,142,143,],[24,24,-4,-8,24,24,24,24,24,24,-3,-5,-6,-7,-9,-10,-11,-12,-13,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,-67,24,24,24,24,24,24,24,-68,-69,24,24,-70,]),'SIZEOF':([0,2,3,7,15,16,17,18,21,22,32,33,34,35,36,37,38,39,40,44,64,65,75,77,81,82,83,84,85,86,87,88,89,92,101,108,114,116,118,121,122,123,129,130,131,132,133,134,138,139,141,142,143,],[25,25,-4,-8,25,25,25,25,25,25,-3,-5,-6,-7,-9,-10,-11,-12,-13,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,-67,25,25,25,25,25,25,25,-68,-69,25,25,-70,]),'FUNCTION':([0,2,3,7,32,33,34,35,36,37,38,39,40,82,92,101,108,116,118,121,122,123,129,130,131,132,133,134,138,139,141,142,143,],[26,26,-4,-8,-3,-5,-6,-7,-9,-10,-11,-12,-13,26,26,26,26,26,26,26,-67,26,26,26,26,26,26,26,-68,-69,26,26,-70,]),'IDENT':([0,2,3,7,13,15,16,17,18,21,22,25,26,28,29,30,31,32,33,34,35,36,37,38,39,40,44,64,65,73,75,76,77,78,81,82,83,84,85,86,87,88,89,92,94,101,108,114,116,118,121,122,123,129,130,131,132,133,134,138,139,141,142,143,],[27,27,-4,-8,42,51,51,51,51,51,51,72,74,-15,-16,-17,-18,-3,-5,-6,-7,-9,-10,-11,-12,-13,51,51,51,93,51,42,51,42,51,27,51,51,51,51,51,51,51,27,110,27,27,51,27,27,27,-67,27,27,27,27,27,27,27,-68,-69,27,27,-70,]),'NL':([0,2,3,4,5,6,7,8,9,10,11,12,19,20,23,24,32,33,34,35,36,37,38,39,40,41,42,43,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,67,68,69,70,71,72,79,80,82,90,91,92,97,98,101,102,103,104,105,106,107,108,111,112,113,115,116,117,118,121,122,123,124,125,128,129,130,131,132,133,134,135,136,137,138,139,141,142,143,],[-2,-2,-4,33,34,35,-8,36,37,38,39,40,-58,-59,-62,-63,-3,-5,-6,-7,-9,-10,-11,-12,-13,-14,-21,-22,-30,-31,-32,-33,-34,-29,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-56,-57,-60,-61,-64,-29,-23,-24,-2,-49,-50,-2,-19,-20,-2,-47,-48,-51,-52,-53,-54,-2,-55,-28,-25,-65,-2,122,-2,-2,-67,-2,129,-66,-71,-2,-2,-2,-2,-2,-2,-72,138,139,-68,-69,-2,-2,-70,]),'INT':([0,2,3,7,32,33,34,35,36,37,38,39,40,82,92,101,108,116,118,121,122,123,129,130,131,132,133,134,138,139,141,142,143,],[28,28,-4,-8,-3,-5,-6,-7,-9,-10,-11,-12,-13,28,28,28,28,28,28,28,-67,28,28,28,28,28,28,28,-68,-69,28,28,-70,]),'CELL':([0,2,3,7,32,33,34,35,36,37,38,39,40,82,92,101,108,116,118,121,122,123,129,130,131,132,133,134,138,139,141,142,143,],[29,29,-4,-8,-3,-5,-6,-7,-9,-10,-11,-12,-13,29,29,29,29,29,29,29,-67,29,29,29,29,29,29,29,-68,-69,29,29,-70,]),'BOOL':([0,2,3,7,32,33,34,35,36,37,38,39,40,82,92,101,108,116,118,121,122,123,129,130,131,132,133,134,138,139,141,142,143,],[30,30,-4,-8,-3,-5,-6,-7,-9,-10,-11,-12,-13,30,30,30,30,30,30,30,-67,30,30,30,30,30,30,30,-68,-69,30,30,-70,]),'VAR':([0,2,3,7,32,33,34,35,36,37,38,39,40,82,92,101,108,116,118,121,122,123,129,130,131,132,133,134,138,139,141,142,143,],[31,31,-4,-8,-3,-5,-6,-7,-9,-10,-11,-12,-13,31,31,31,31,31,31,31,-67,31,31,31,31,31,31,31,-68,-69,31,31,-70,]),'$end':([1,2,3,7,32,33,34,35,36,37,38,39,40,122,138,139,143,],[0,-1,-4,-8,-3,-5,-6,-7,-9,-10,-11,-12,-13,-67,-68,-69,-70,]),'DONE':([3,7,32,33,34,35,36,37,38,39,40,101,108,121,122,123,132,133,134,138,139,142,143,],[-4,-8,-3,-5,-6,-7,-9,-10,-11,-12,-13,115,117,125,-67,128,135,136,137,-68,-69,143,-70,]),'FINISH':([3,7,32,33,34,35,36,37,38,39,40,101,122,138,139,143,],[-4,-8,-3,-5,-6,-7,-9,-10,-11,-12,-13,116,-67,-68,-69,-70,]),'ASSIGN':([14,27,42,112,],[44,-29,-29,-28,]),'INF':([15,16,17,18,21,22,44,64,65,75,77,81,83,84,85,86,87,88,89,114,],[52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,]),'MINUS_INF':([15,16,17,18,21,22,44,64,65,75,77,81,83,84,85,86,87,88,89,114,],[53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,]),'NAN':([15,16,17,18,21,22,44,64,65,75,77,81,83,84,85,86,87,88,89,114,],[54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,]),'TRUE':([15,16,17,18,21,22,44,64,65,75,77,81,83,84,85,86,87,88,89,114,],[55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,]),'FALSE':([15,16,17,18,21,22,44,64,65,75,77,81,83,84,85,86,87,88,89,114,],[56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,]),'UNDEF':([15,16,17,18,21,22,44,64,65,75,77,81,83,84,85,86,87,88,89,114,],[57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,]),'EMPTY':([15,16,17,18,21,22,44,64,65,75,77,81,83,84,85,86,87,88,89,114,],[58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,]),'WALL':([15,16,17,18,21,22,44,64,65,75,77,81,83,84,85,86,87,88,89,114,],[59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,]),'BOX':([15,16,17,18,21,22,44,64,65,75,77,81,83,84,85,86,87,88,89,114,],[60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,]),'EXIT':([15,16,17,18,21,22,44,64,65,75,77,81,83,84,85,86,87,88,89,114,],[61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,]),'DECIMAL':([15,16,17,18,21,22,44,64,65,75,77,81,83,84,85,86,87,88,89,114,],[62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,]),'HEXADECIMAL':([15,16,17,18,21,22,44,64,65,75,77,81,83,84,85,86,87,88,89,114,],[63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,]),'MINUS':([15,16,17,18,19,20,21,22,23,24,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,75,77,79,81,83,84,85,86,87,88,89,90,91,95,96,100,102,103,104,105,106,107,111,112,114,120,],[64,64,64,64,-58,-59,64,64,-62,-63,64,84,-30,-31,-32,-33,-34,-29,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,64,64,84,84,84,84,84,-64,-29,64,64,84,64,64,64,64,64,64,64,64,-49,84,-30,84,84,-47,-48,84,-52,-53,84,-55,-28,64,84,]),'SHARP':([15,16,17,18,21,22,44,64,65,75,77,81,83,84,85,86,87,88,89,114,],[65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,]),'DO':([19,20,23,24,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,66,67,68,69,70,71,72,90,91,102,103,104,105,106,107,109,111,112,119,126,127,140,],[-58,-59,-62,-63,82,-30,-31,-32,-33,-34,-29,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,92,-56,-57,-60,-61,-64,-29,-49,-50,-47,-48,-51,-52,-53,-54,118,-55,-28,124,130,131,141,]),'PLUS':([19,20,23,24,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,66,67,68,69,70,71,72,79,90,91,95,96,100,102,103,104,105,106,107,111,112,120,],[-58,-59,-62,-63,83,-30,-31,-32,-33,-34,-29,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,83,83,83,83,83,-64,-29,83,-49,83,-30,83,83,-47,-48,83,-52,-53,83,-55,-28,83,]),'CARET':([19,20,23,24,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,66,67,68,69,70,71,72,79,90,91,95,96,100,102,103,104,105,106,107,111,112,120,],[-58,-59,-62,-63,85,-30,-31,-32,-33,-34,-29,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,85,85,85,85,85,-64,-29,85,-49,85,-30,85,85,-47,-48,85,-52,-53,85,-55,-28,85,]),'GREATER':([19,20,23,24,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,66,67,68,69,70,71,72,79,90,91,95,96,100,102,103,104,105,106,107,111,112,120,],[-58,-59,-62,-63,86,-30,-31,-32,-33,-34,-29,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,86,86,86,86,86,-64,-29,86,86,86,-30,86,86,86,86,86,None,None,86,-55,-28,86,]),'LESS':([19,20,23,24,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,66,67,68,69,70,71,72,79,90,91,95,96,100,102,103,104,105,106,107,111,112,120,],[-58,-59,-62,-63,87,-30,-31,-32,-33,-34,-29,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,87,87,87,87,87,-64,-29,87,87,87,-30,87,87,87,87,87,None,None,87,-55,-28,87,]),'EQUAL':([19,20,23,24,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,66,67,68,69,70,71,72,79,90,91,95,96,100,102,103,104,105,106,107,111,112,120,],[-58,-59,-62,-63,88,-30,-31,-32,-33,-34,-29,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,88,88,88,88,88,-64,-29,88,-49,88,-30,88,88,-47,-48,88,-52,-53,88,-55,-28,88,]),'COMMA':([19,20,23,24,42,43,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,67,68,69,70,71,72,79,80,90,91,99,100,102,103,104,105,106,107,111,112,113,120,],[-58,-59,-62,-63,76,78,-30,-31,-32,-33,-34,-29,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-56,-57,-60,-61,-64,-29,-23,-24,-49,-50,114,-27,-47,-48,-51,-52,-53,-54,-55,-28,-25,-26,]),'CBRACKET':([19,20,23,24,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,67,68,69,70,71,72,90,91,93,95,96,102,103,104,105,106,107,110,111,112,],[-58,-59,-62,-63,-30,-31,-32,-33,-34,-29,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-56,-57,-60,-61,-64,-29,-49,-50,109,111,112,-47,-48,-51,-52,-53,-54,119,-55,-28,]),'CSQBRACKET':([19,20,23,24,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,67,68,69,70,71,72,90,91,99,100,102,103,104,105,106,107,111,112,120,],[-58,-59,-62,-63,-30,-31,-32,-33,-34,-29,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-56,-57,-60,-61,-64,-29,-49,-50,113,-27,-47,-48,-51,-52,-53,-54,-55,-28,-26,]),'OBRACKET':([26,27,42,51,72,74,],[73,75,77,89,77,94,]),'OSQBRACKET':([44,],[81,]),'ELDEF':([122,],[126,]),'ELUND':([122,138,],[127,140,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'stmt_list':([0,82,92,116,118,129,130,131,141,],[2,101,108,121,123,132,133,134,142,]),'statement':([0,2,82,92,101,108,116,118,121,123,129,130,131,132,133,134,141,142,],[3,32,3,3,32,32,3,3,32,32,3,3,3,32,32,32,3,32,]),'declaration_list':([0,2,82,92,101,108,116,118,121,123,129,130,131,132,133,134,141,142,],[4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,]),'assignment':([0,2,13,76,78,82,92,101,108,116,118,121,123,129,130,131,132,133,134,141,142,],[5,5,43,43,43,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,]),'while':([0,2,82,92,101,108,116,118,121,123,129,130,131,132,133,134,141,142,],[6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,]),'if':([0,2,82,92,101,108,116,118,121,123,129,130,131,132,133,134,141,142,],[7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,]),'operator':([0,2,15,16,17,18,21,22,44,64,65,75,77,81,82,83,84,85,86,87,88,89,92,101,108,114,116,118,121,123,129,130,131,132,133,134,141,142,],[8,8,50,50,50,50,50,50,50,50,50,50,50,50,8,50,50,50,50,50,50,50,8,8,8,50,8,8,8,8,8,8,8,8,8,8,8,8,]),'function':([0,2,82,92,101,108,116,118,121,123,129,130,131,132,133,134,141,142,],[9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,]),'function_call':([0,2,15,16,17,18,21,22,44,64,65,75,77,81,82,83,84,85,86,87,88,89,92,101,108,114,116,118,121,123,129,130,131,132,133,134,141,142,],[10,10,49,49,49,49,49,49,49,49,49,49,49,49,10,49,49,49,49,49,49,49,10,10,10,49,10,10,10,10,10,10,10,10,10,10,10,10,]),'empty':([0,2,82,92,101,108,116,118,121,123,129,130,131,132,133,134,141,142,],[12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,]),'type':([0,2,82,92,101,108,116,118,121,123,129,130,131,132,133,134,141,142,],[13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,]),'variable':([0,2,13,15,16,17,18,21,22,25,44,64,65,75,76,77,78,81,82,83,84,85,86,87,88,89,92,101,108,114,116,118,121,123,129,130,131,132,133,134,141,142,],[14,14,14,46,46,46,46,46,46,71,46,46,46,95,14,46,14,46,14,46,46,46,46,46,46,95,14,14,14,46,14,14,14,14,14,14,14,14,14,14,14,14,]),'vars_list':([13,76,78,],[41,97,98,]),'expression':([15,16,17,18,21,22,44,64,65,75,77,81,83,84,85,86,87,88,89,114,],[45,66,67,68,69,70,79,90,91,96,96,100,102,103,104,105,106,107,96,120,]),'const':([15,16,17,18,21,22,44,64,65,75,77,81,83,84,85,86,87,88,89,114,],[47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,]),'al_expression':([15,16,17,18,21,22,44,64,65,75,77,81,83,84,85,86,87,88,89,114,],[48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,]),'array':([44,],[80,]),'expr_list':([81,],[99,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> stmt_list','program',1,'p_program','parser.py',100),
  ('empty -> <empty>','empty',0,'p_empty','parser.py',104),
  ('stmt_list -> stmt_list statement','stmt_list',2,'p_stmt_list','parser.py',108),
  ('stmt_list -> statement','stmt_list',1,'p_stmt_list','parser.py',109),
  ('statement -> declaration_list NL','statement',2,'p_statement','parser.py',116),
  ('statement -> assignment NL','statement',2,'p_statement','parser.py',117),
  ('statement -> while NL','statement',2,'p_statement','parser.py',118),
  ('statement -> if','statement',1,'p_statement','parser.py',119),
  ('statement -> operator NL','statement',2,'p_statement','parser.py',120),
  ('statement -> function NL','statement',2,'p_statement','parser.py',121),
  ('statement -> function_call NL','statement',2,'p_statement','parser.py',122),
  ('statement -> RETURN NL','statement',2,'p_statement','parser.py',123),
  ('statement -> empty NL','statement',2,'p_statement','parser.py',124),
  ('declaration_list -> type vars_list','declaration_list',2,'p_declaration_list','parser.py',130),
  ('type -> INT','type',1,'p_type','parser.py',134),
  ('type -> CELL','type',1,'p_type','parser.py',135),
  ('type -> BOOL','type',1,'p_type','parser.py',136),
  ('type -> VAR','type',1,'p_type','parser.py',137),
  ('vars_list -> IDENT COMMA vars_list','vars_list',3,'p_vars_list_icv','parser.py',144),
  ('vars_list -> assignment COMMA vars_list','vars_list',3,'p_vars_list_acv','parser.py',149),
  ('vars_list -> IDENT','vars_list',1,'p_vars_list_ident','parser.py',153),
  ('vars_list -> assignment','vars_list',1,'p_vars_list','parser.py',157),
  ('assignment -> variable ASSIGN expression','assignment',3,'p_assignment','parser.py',161),
  ('assignment -> variable ASSIGN array','assignment',3,'p_assignment','parser.py',162),
  ('array -> OSQBRACKET expr_list CSQBRACKET','array',3,'p_array','parser.py',166),
  ('expr_list -> expr_list COMMA expression','expr_list',3,'p_expr_list','parser.py',170),
  ('expr_list -> expression','expr_list',1,'p_expr_list','parser.py',171),
  ('variable -> IDENT OBRACKET expression CBRACKET','variable',4,'p_variable','parser.py',178),
  ('variable -> IDENT','variable',1,'p_variable','parser.py',179),
  ('expression -> variable','expression',1,'p_expression','parser.py',186),
  ('expression -> const','expression',1,'p_expression','parser.py',187),
  ('expression -> al_expression','expression',1,'p_expression','parser.py',188),
  ('expression -> function_call','expression',1,'p_expression','parser.py',189),
  ('expression -> operator','expression',1,'p_expression','parser.py',190),
  ('const -> INF','const',1,'p_const','parser.py',194),
  ('const -> MINUS_INF','const',1,'p_const','parser.py',195),
  ('const -> NAN','const',1,'p_const','parser.py',196),
  ('const -> TRUE','const',1,'p_const','parser.py',197),
  ('const -> FALSE','const',1,'p_const','parser.py',198),
  ('const -> UNDEF','const',1,'p_const','parser.py',199),
  ('const -> EMPTY','const',1,'p_const','parser.py',200),
  ('const -> WALL','const',1,'p_const','parser.py',201),
  ('const -> BOX','const',1,'p_const','parser.py',202),
  ('const -> EXIT','const',1,'p_const','parser.py',203),
  ('const -> DECIMAL','const',1,'p_const','parser.py',204),
  ('const -> HEXADECIMAL','const',1,'p_const','parser.py',205),
  ('al_expression -> expression PLUS expression','al_expression',3,'p_al_expression','parser.py',209),
  ('al_expression -> expression MINUS expression','al_expression',3,'p_al_expression','parser.py',210),
  ('al_expression -> MINUS expression','al_expression',2,'p_al_expression','parser.py',211),
  ('al_expression -> SHARP expression','al_expression',2,'p_al_expression','parser.py',212),
  ('al_expression -> expression CARET expression','al_expression',3,'p_al_expression','parser.py',213),
  ('al_expression -> expression GREATER expression','al_expression',3,'p_al_expression','parser.py',214),
  ('al_expression -> expression LESS expression','al_expression',3,'p_al_expression','parser.py',215),
  ('al_expression -> expression EQUAL expression','al_expression',3,'p_al_expression','parser.py',216),
  ('function_call -> IDENT OBRACKET variable CBRACKET','function_call',4,'p_function_call','parser.py',223),
  ('operator -> FORWARD expression','operator',2,'p_operator','parser.py',227),
  ('operator -> BACKWARD expression','operator',2,'p_operator','parser.py',228),
  ('operator -> LEFT','operator',1,'p_operator','parser.py',229),
  ('operator -> RIGHT','operator',1,'p_operator','parser.py',230),
  ('operator -> LOAD expression','operator',2,'p_operator','parser.py',231),
  ('operator -> DROP expression','operator',2,'p_operator','parser.py',232),
  ('operator -> LOOK','operator',1,'p_operator','parser.py',233),
  ('operator -> TEST','operator',1,'p_operator','parser.py',234),
  ('operator -> SIZEOF variable','operator',2,'p_operator','parser.py',235),
  ('while -> WHILE expression DO stmt_list DONE','while',5,'p_while','parser.py',242),
  ('while -> WHILE expression DO stmt_list FINISH stmt_list DONE','while',7,'p_while','parser.py',243),
  ('if -> IF expression DO stmt_list DONE NL','if',6,'p_if_short','parser.py',252),
  ('if -> IF expression DO stmt_list DONE NL ELDEF DO stmt_list DONE NL','if',11,'p_if_eldef','parser.py',256),
  ('if -> IF expression DO stmt_list DONE NL ELUND DO stmt_list DONE NL','if',11,'p_if_elund','parser.py',260),
  ('if -> IF expression DO stmt_list DONE NL ELDEF DO stmt_list DONE NL ELUND DO stmt_list DONE','if',15,'p_if_long','parser.py',264),
  ('function -> FUNCTION OBRACKET IDENT CBRACKET DO stmt_list DONE','function',7,'p_unnamed_function','parser.py',268),
  ('function -> FUNCTION IDENT OBRACKET IDENT CBRACKET DO NL stmt_list DONE','function',9,'p_function','parser.py',279),
]
