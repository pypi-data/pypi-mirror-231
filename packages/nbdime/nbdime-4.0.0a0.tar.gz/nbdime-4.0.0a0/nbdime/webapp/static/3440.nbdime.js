"use strict";(self.webpackChunknbdime_webapp=self.webpackChunknbdime_webapp||[]).push([[3440],{33440:(e,n,t)=>{function i(e,n){for(var t=0;t<e.length;t++)n(e[t],t)}function r(e,n){for(var t=0;t<e.length;t++)if(n(e[t],t))return!0;return!1}t.r(n),t.d(n,{dylan:()=>k});var a={unnamedDefinition:["interface"],namedDefinition:["module","library","macro","C-struct","C-union","C-function","C-callable-wrapper"],typeParameterizedDefinition:["class","C-subtype","C-mapped-subtype"],otherParameterizedDefinition:["method","function","C-variable","C-address"],constantSimpleDefinition:["constant"],variableSimpleDefinition:["variable"],otherSimpleDefinition:["generic","domain","C-pointer-type","table"],statement:["if","block","begin","method","case","for","select","when","unless","until","while","iterate","profiling","dynamic-bind"],separator:["finally","exception","cleanup","else","elseif","afterwards"],other:["above","below","by","from","handler","in","instance","let","local","otherwise","slot","subclass","then","to","keyed-by","virtual"],signalingCalls:["signal","error","cerror","break","check-type","abort"]};a.otherDefinition=a.unnamedDefinition.concat(a.namedDefinition).concat(a.otherParameterizedDefinition),a.definition=a.typeParameterizedDefinition.concat(a.otherDefinition),a.parameterizedDefinition=a.typeParameterizedDefinition.concat(a.otherParameterizedDefinition),a.simpleDefinition=a.constantSimpleDefinition.concat(a.variableSimpleDefinition).concat(a.otherSimpleDefinition),a.keyword=a.statement.concat(a.separator).concat(a.other);var o="[-_a-zA-Z?!*@<>$%]+",l=new RegExp("^"+o),f={symbolKeyword:o+":",symbolClass:"<"+o+">",symbolGlobal:"\\*"+o+"\\*",symbolConstant:"\\$"+o},c={symbolKeyword:"atom",symbolClass:"tag",symbolGlobal:"variableName.standard",symbolConstant:"variableName.constant"};for(var s in f)f.hasOwnProperty(s)&&(f[s]=new RegExp("^"+f[s]));f.keyword=[/^with(?:out)?-[-_a-zA-Z?!*@<>$%]+/];var u={keyword:"keyword",definition:"def",simpleDefinition:"def",signalingCalls:"builtin"},m={},d={};function p(e,n,t){return n.tokenize=t,t(e,n)}function b(e,n){var t=e.peek();if("'"==t||'"'==t)return e.next(),p(e,n,y(t,"string"));if("/"==t){if(e.next(),e.eat("*"))return p(e,n,h);if(e.eat("/"))return e.skipToEnd(),"comment";e.backUp(1)}else if(/[+\-\d\.]/.test(t)){if(e.match(/^[+-]?[0-9]*\.[0-9]*([esdx][+-]?[0-9]+)?/i)||e.match(/^[+-]?[0-9]+([esdx][+-]?[0-9]+)/i)||e.match(/^[+-]?\d+/))return"number"}else{if("#"==t)return e.next(),'"'==(t=e.peek())?(e.next(),p(e,n,y('"',"string"))):"b"==t?(e.next(),e.eatWhile(/[01]/),"number"):"x"==t?(e.next(),e.eatWhile(/[\da-f]/i),"number"):"o"==t?(e.next(),e.eatWhile(/[0-7]/),"number"):"#"==t?(e.next(),"punctuation"):"["==t||"("==t?(e.next(),"bracket"):e.match(/f|t|all-keys|include|key|next|rest/i)?"atom":(e.eatWhile(/[-a-zA-Z]/),"error");if("~"==t)return e.next(),"="==(t=e.peek())?(e.next(),"="==(t=e.peek())?(e.next(),"operator"):"operator"):"operator";if(":"==t){if(e.next(),"="==(t=e.peek()))return e.next(),"operator";if(":"==t)return e.next(),"punctuation"}else{if(-1!="[](){}".indexOf(t))return e.next(),"bracket";if(-1!=".,".indexOf(t))return e.next(),"punctuation";if(e.match("end"))return"keyword"}}for(var i in f)if(f.hasOwnProperty(i)){var a=f[i];if(a instanceof Array&&r(a,(function(n){return e.match(n)}))||e.match(a))return c[i]}return/[+\-*\/^=<>&|]/.test(t)?(e.next(),"operator"):e.match("define")?"def":(e.eatWhile(/[\w\-]/),m.hasOwnProperty(e.current())?d[e.current()]:e.current().match(l)?"variable":(e.next(),"variableName.standard"))}function h(e,n){for(var t,i=!1,r=!1,a=0;t=e.next();){if("/"==t&&i){if(!(a>0)){n.tokenize=b;break}a--}else"*"==t&&r&&a++;i="*"==t,r="/"==t}return"comment"}function y(e,n){return function(t,i){for(var r,a=!1,o=!1;null!=(r=t.next());){if(r==e&&!a){o=!0;break}a=!a&&"\\"==r}return!o&&a||(i.tokenize=b),n}}i(["keyword","definition","simpleDefinition","signalingCalls"],(function(e){i(a[e],(function(n){m[n]=e,d[n]=u[e]}))}));const k={name:"dylan",startState:function(){return{tokenize:b,currentIndent:0}},token:function(e,n){return e.eatSpace()?null:n.tokenize(e,n)},languageData:{commentTokens:{block:{open:"/*",close:"*/"}}}}}}]);
//# sourceMappingURL=3440.nbdime.js.map