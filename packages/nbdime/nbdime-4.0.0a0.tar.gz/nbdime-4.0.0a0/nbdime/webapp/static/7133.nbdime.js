"use strict";(self.webpackChunknbdime_webapp=self.webpackChunknbdime_webapp||[]).push([[7133],{97133:(e,t,n)=>{function r(e){var t="error";function n(e){return new RegExp("^(("+e.join(")|(")+"))\\b","i")}var r=new RegExp("^[\\+\\-\\*/&\\\\\\^<>=]"),a=new RegExp("^((<>)|(<=)|(>=))"),i=new RegExp("^[\\.,]"),o=new RegExp("^[\\(\\)]"),c=new RegExp("^[A-Za-z][_A-Za-z0-9]*"),b=n(["and","or","not","xor","is","mod","eqv","imp"]),l=["WScript","err","debug","RegExp"],s=["clear","execute","raise","replace","test","write","writeline","close","open","state","eof","update","addnew","end","createobject","quit"].concat(["description","firstindex","global","helpcontext","helpfile","ignorecase","length","number","pattern","source","value","count"]);l=l.concat(["vbBlack","vbRed","vbGreen","vbYellow","vbBlue","vbMagenta","vbCyan","vbWhite","vbBinaryCompare","vbTextCompare","vbSunday","vbMonday","vbTuesday","vbWednesday","vbThursday","vbFriday","vbSaturday","vbUseSystemDayOfWeek","vbFirstJan1","vbFirstFourDays","vbFirstFullWeek","vbGeneralDate","vbLongDate","vbShortDate","vbLongTime","vbShortTime","vbObjectError","vbOKOnly","vbOKCancel","vbAbortRetryIgnore","vbYesNoCancel","vbYesNo","vbRetryCancel","vbCritical","vbQuestion","vbExclamation","vbInformation","vbDefaultButton1","vbDefaultButton2","vbDefaultButton3","vbDefaultButton4","vbApplicationModal","vbSystemModal","vbOK","vbCancel","vbAbort","vbRetry","vbIgnore","vbYes","vbNo","vbCr","VbCrLf","vbFormFeed","vbLf","vbNewLine","vbNullChar","vbNullString","vbTab","vbVerticalTab","vbUseDefault","vbTrue","vbFalse","vbEmpty","vbNull","vbInteger","vbLong","vbSingle","vbDouble","vbCurrency","vbDate","vbString","vbObject","vbError","vbBoolean","vbVariant","vbDataObject","vbDecimal","vbByte","vbArray"]),e.isASP&&(l=l.concat(["server","response","request","session","application"]),s=s.concat(["addheader","appendtolog","binarywrite","end","flush","redirect","binaryread","remove","removeall","lock","unlock","abandon","getlasterror","htmlencode","mappath","transfer","urlencode"],["buffer","cachecontrol","charset","contenttype","expires","expiresabsolute","isclientconnected","pics","status","clientcertificate","cookies","form","querystring","servervariables","totalbytes","contents","staticobjects","codepage","lcid","sessionid","timeout","scripttimeout"]));var u=n(["dim","redim","then","until","randomize","byval","byref","new","property","exit","in","const","private","public","get","set","let","stop","on error resume next","on error goto 0","option explicit","call","me"]),v=n(["true","false","nothing","empty","null"]),d=n(["abs","array","asc","atn","cbool","cbyte","ccur","cdate","cdbl","chr","cint","clng","cos","csng","cstr","date","dateadd","datediff","datepart","dateserial","datevalue","day","escape","eval","execute","exp","filter","formatcurrency","formatdatetime","formatnumber","formatpercent","getlocale","getobject","getref","hex","hour","inputbox","instr","instrrev","int","fix","isarray","isdate","isempty","isnull","isnumeric","isobject","join","lbound","lcase","left","len","loadpicture","log","ltrim","rtrim","trim","maths","mid","minute","month","monthname","msgbox","now","oct","replace","rgb","right","rnd","round","scriptengine","scriptenginebuildversion","scriptenginemajorversion","scriptengineminorversion","second","setlocale","sgn","sin","space","split","sqr","strcomp","string","strreverse","tan","time","timer","timeserial","timevalue","typename","ubound","ucase","unescape","vartype","weekday","weekdayname","year"]),m=n(l),p=n(s),h=n(["class","sub","select","while","if","function","property","with","for"]),f=n(["else","elseif","case"]),y=n(["next","loop","wend"]),g=n(["end"]),k=n(["do"]),w=n(["on error resume next","exit"]),x=n(["rem"]);function C(e,t){t.currentIndent++}function I(e,t){t.currentIndent--}function L(e,n){if(e.eatSpace())return null;var l,s,S;if("'"===e.peek())return e.skipToEnd(),"comment";if(e.match(x))return e.skipToEnd(),"comment";if(e.match(/^((&H)|(&O))?[0-9\.]/i,!1)&&!e.match(/^((&H)|(&O))?[0-9\.]+[a-z_]/i,!1)){var D=!1;if((e.match(/^\d*\.\d+/i)||e.match(/^\d+\.\d*/)||e.match(/^\.\d+/))&&(D=!0),D)return e.eat(/J/i),"number";var E=!1;if(e.match(/^&H[0-9a-f]+/i)||e.match(/^&O[0-7]+/i)?E=!0:e.match(/^[1-9]\d*F?/)?(e.eat(/J/i),E=!0):e.match(/^0(?![\dx])/i)&&(E=!0),E)return e.eat(/L/i),"number"}return e.match('"')?(n.tokenize=(l=e.current(),s=1==l.length,S="string",function(e,t){for(;!e.eol();){if(e.eatWhile(/[^'"]/),e.match(l))return t.tokenize=L,S;e.eat(/['"]/)}return s&&(t.tokenize=L),S}),n.tokenize(e,n)):e.match(a)||e.match(r)||e.match(b)?"operator":e.match(i)?null:e.match(o)?"bracket":e.match(w)?(n.doInCurrentLine=!0,"keyword"):e.match(k)?(C(0,n),n.doInCurrentLine=!0,"keyword"):e.match(h)?(n.doInCurrentLine?n.doInCurrentLine=!1:C(0,n),"keyword"):e.match(f)?"keyword":e.match(g)?(I(0,n),I(0,n),"keyword"):e.match(y)?(n.doInCurrentLine?n.doInCurrentLine=!1:I(0,n),"keyword"):e.match(u)?"keyword":e.match(v)?"atom":e.match(p)?"variableName.special":e.match(d)||e.match(m)?"builtin":e.match(c)?"variable":(e.next(),t)}return{name:"vbscript",startState:function(){return{tokenize:L,lastToken:null,currentIndent:0,nextLineIndent:0,doInCurrentLine:!1,ignoreKeyword:!1}},token:function(e,n){e.sol()&&(n.currentIndent+=n.nextLineIndent,n.nextLineIndent=0,n.doInCurrentLine=0);var r=function(e,n){var r=n.tokenize(e,n),a=e.current();return"."===a?(r=n.tokenize(e,n),a=e.current(),!r||"variable"!==r.substr(0,8)&&"builtin"!==r&&"keyword"!==r?t:("builtin"!==r&&"keyword"!==r||(r="variable"),s.indexOf(a.substr(1))>-1&&(r="keyword"),r)):r}(e,n);return n.lastToken={style:r,content:e.current()},null===r&&(r=null),r},indent:function(e,t,n){var r=t.replace(/^\s+|\s+$/g,"");return r.match(y)||r.match(g)||r.match(f)?n.unit*(e.currentIndent-1):e.currentIndent<0?0:e.currentIndent*n.unit}}}n.r(t),n.d(t,{vbScript:()=>a,vbScriptASP:()=>i});const a=r({}),i=r({isASP:!0})}}]);
//# sourceMappingURL=7133.nbdime.js.map