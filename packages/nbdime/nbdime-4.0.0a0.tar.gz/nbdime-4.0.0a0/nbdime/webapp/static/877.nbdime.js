"use strict";(self.webpackChunknbdime_webapp=self.webpackChunknbdime_webapp||[]).push([[877],{90877:(e,t,n)=>{n.r(t),n.d(t,{q:()=>p});var r,o=new RegExp("^("+["abs","acos","aj","aj0","all","and","any","asc","asin","asof","atan","attr","avg","avgs","bin","by","ceiling","cols","cor","cos","count","cov","cross","csv","cut","delete","deltas","desc","dev","differ","distinct","div","do","each","ej","enlist","eval","except","exec","exit","exp","fby","fills","first","fkeys","flip","floor","from","get","getenv","group","gtime","hclose","hcount","hdel","hopen","hsym","iasc","idesc","if","ij","in","insert","inter","inv","key","keys","last","like","list","lj","load","log","lower","lsq","ltime","ltrim","mavg","max","maxs","mcount","md5","mdev","med","meta","min","mins","mmax","mmin","mmu","mod","msum","neg","next","not","null","or","over","parse","peach","pj","plist","prd","prds","prev","prior","rand","rank","ratios","raze","read0","read1","reciprocal","reverse","rload","rotate","rsave","rtrim","save","scan","select","set","setenv","show","signum","sin","sqrt","ss","ssr","string","sublist","sum","sums","sv","system","tables","tan","til","trim","txf","type","uj","ungroup","union","update","upper","upsert","value","var","view","views","vs","wavg","where","where","while","within","wj","wj1","wsum","xasc","xbar","xcol","xcols","xdesc","xexp","xgroup","xkey","xlog","xprev","xrank"].join("|")+")$"),i=/[|/&^!+:\\\-*%$=~#;@><,?_\'\"\[\(\]\)\s{}]/;function s(e,t){var n=e.sol(),c=e.next();if(r=null,n){if("/"==c)return(t.tokenize=a)(e,t);if("\\"==c)return e.eol()||/\s/.test(e.peek())?(e.skipToEnd(),/^\\\s*$/.test(e.current())?(t.tokenize=l)(e):t.tokenize=s,"comment"):(t.tokenize=s,"builtin")}if(/\s/.test(c))return"/"==e.peek()?(e.skipToEnd(),"comment"):"null";if('"'==c)return(t.tokenize=u)(e,t);if("`"==c)return e.eatWhile(/[A-Za-z\d_:\/.]/),"macroName";if("."==c&&/\d/.test(e.peek())||/\d/.test(c)){var d=null;return e.backUp(1),e.match(/^\d{4}\.\d{2}(m|\.\d{2}([DT](\d{2}(:\d{2}(:\d{2}(\.\d{1,9})?)?)?)?)?)/)||e.match(/^\d+D(\d{2}(:\d{2}(:\d{2}(\.\d{1,9})?)?)?)/)||e.match(/^\d{2}:\d{2}(:\d{2}(\.\d{1,9})?)?/)||e.match(/^\d+[ptuv]{1}/)?d="temporal":(e.match(/^0[NwW]{1}/)||e.match(/^0x[\da-fA-F]*/)||e.match(/^[01]+[b]{1}/)||e.match(/^\d+[chijn]{1}/)||e.match(/-?\d*(\.\d*)?(e[+\-]?\d+)?(e|f)?/))&&(d="number"),!d||(c=e.peek())&&!i.test(c)?(e.next(),"error"):d}return/[A-Za-z]|\./.test(c)?(e.eatWhile(/[A-Za-z._\d]/),o.test(e.current())?"keyword":"variable"):/[|/&^!+:\\\-*%$=~#;@><\.,?_\']/.test(c)||/[{}\(\[\]\)]/.test(c)?null:"error"}function a(e,t){return e.skipToEnd(),/\/\s*$/.test(e.current())?(t.tokenize=c)(e,t):t.tokenize=s,"comment"}function c(e,t){var n=e.sol()&&"\\"==e.peek();return e.skipToEnd(),n&&/^\\\s*$/.test(e.current())&&(t.tokenize=s),"comment"}function l(e){return e.skipToEnd(),"comment"}function u(e,t){for(var n,r=!1,o=!1;n=e.next();){if('"'==n&&!r){o=!0;break}r=!r&&"\\"==n}return o&&(t.tokenize=s),"string"}function d(e,t,n){e.context={prev:e.context,indent:e.indent,col:n,type:t}}function m(e){e.indent=e.context.indent,e.context=e.context.prev}const p={name:"q",startState:function(){return{tokenize:s,context:null,indent:0,col:0}},token:function(e,t){e.sol()&&(t.context&&null==t.context.align&&(t.context.align=!1),t.indent=e.indentation());var n=t.tokenize(e,t);if("comment"!=n&&t.context&&null==t.context.align&&"pattern"!=t.context.type&&(t.context.align=!0),"("==r)d(t,")",e.column());else if("["==r)d(t,"]",e.column());else if("{"==r)d(t,"}",e.column());else if(/[\]\}\)]/.test(r)){for(;t.context&&"pattern"==t.context.type;)m(t);t.context&&r==t.context.type&&m(t)}else"."==r&&t.context&&"pattern"==t.context.type?m(t):/atom|string|variable/.test(n)&&t.context&&(/[\}\]]/.test(t.context.type)?d(t,"pattern",e.column()):"pattern"!=t.context.type||t.context.align||(t.context.align=!0,t.context.col=e.column()));return n},indent:function(e,t,n){var r=t&&t.charAt(0),o=e.context;if(/[\]\}]/.test(r))for(;o&&"pattern"==o.type;)o=o.prev;var i=o&&r==o.type;return o?"pattern"==o.type?o.col:o.align?o.col+(i?0:1):o.indent+(i?0:n.unit):0}}}}]);
//# sourceMappingURL=877.nbdime.js.map