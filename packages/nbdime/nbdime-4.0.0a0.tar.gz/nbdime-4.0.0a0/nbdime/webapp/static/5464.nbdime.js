"use strict";(self.webpackChunknbdime_webapp=self.webpackChunknbdime_webapp||[]).push([[5464],{65464:(e,t,n)=>{n.r(t),n.d(t,{factor:()=>r});const r=(0,n(14045).Q)({start:[{regex:/#?!.*/,token:"comment"},{regex:/"""/,token:"string",next:"string3"},{regex:/(STRING:)(\s)/,token:["keyword",null],next:"string2"},{regex:/\S*?"/,token:"string",next:"string"},{regex:/(?:0x[\d,a-f]+)|(?:0o[0-7]+)|(?:0b[0,1]+)|(?:\-?\d+.?\d*)(?=\s)/,token:"number"},{regex:/((?:GENERIC)|\:?\:)(\s+)(\S+)(\s+)(\()/,token:["keyword",null,"def",null,"bracket"],next:"stack"},{regex:/(M\:)(\s+)(\S+)(\s+)(\S+)/,token:["keyword",null,"def",null,"tag"]},{regex:/USING\:/,token:"keyword",next:"vocabulary"},{regex:/(USE\:|IN\:)(\s+)(\S+)(?=\s|$)/,token:["keyword",null,"tag"]},{regex:/(\S+\:)(\s+)(\S+)(?=\s|$)/,token:["keyword",null,"def"]},{regex:/(?:;|\\|t|f|if|loop|while|until|do|PRIVATE>|<PRIVATE|\.|\S*\[|\]|\S*\{|\})(?=\s|$)/,token:"keyword"},{regex:/\S+[\)>\.\*\?]+(?=\s|$)/,token:"builtin"},{regex:/[\)><]+\S+(?=\s|$)/,token:"builtin"},{regex:/(?:[\+\-\=\/\*<>])(?=\s|$)/,token:"keyword"},{regex:/\S+/,token:"variable"},{regex:/\s+|./,token:null}],vocabulary:[{regex:/;/,token:"keyword",next:"start"},{regex:/\S+/,token:"tag"},{regex:/\s+|./,token:null}],string:[{regex:/(?:[^\\]|\\.)*?"/,token:"string",next:"start"},{regex:/.*/,token:"string"}],string2:[{regex:/^;/,token:"keyword",next:"start"},{regex:/.*/,token:"string"}],string3:[{regex:/(?:[^\\]|\\.)*?"""/,token:"string",next:"start"},{regex:/.*/,token:"string"}],stack:[{regex:/\)/,token:"bracket",next:"start"},{regex:/--/,token:"bracket"},{regex:/\S+/,token:"meta"},{regex:/\s+|./,token:null}],languageData:{name:"factor",dontIndentStates:["start","vocabulary","string","string3","stack"],commentTokens:{line:"!"}}})},14045:(e,t,n)=>{function r(e){a(e,"start");var t={},n=e.languageData||{},r=!1;for(var g in e)if(g!=n&&e.hasOwnProperty(g))for(var d=t[g]=[],l=e[g],u=0;u<l.length;u++){var k=l[u];d.push(new o(k,e)),(k.indent||k.dedent)&&(r=!0)}return{name:n.name,startState:function(){return{state:"start",pending:null,indent:r?[]:null}},copyState:function(e){var t={state:e.state,pending:e.pending,indent:e.indent&&e.indent.slice(0)};return e.stack&&(t.stack=e.stack.slice(0)),t},token:s(t),indent:i(t,n),languageData:n}}function a(e,t){if(!e.hasOwnProperty(t))throw new Error("Undefined state "+t+" in simple mode")}function o(e,t){(e.next||e.push)&&a(t,e.next||e.push),this.regex=function(e,t){if(!e)return/(?:)/;var n="";return e instanceof RegExp?(e.ignoreCase&&(n="i"),e=e.source):e=String(e),new RegExp("^(?:"+e+")",n)}(e.regex),this.token=function(e){if(!e)return null;if(e.apply)return e;if("string"==typeof e)return e.replace(/\./g," ");for(var t=[],n=0;n<e.length;n++)t.push(e[n]&&e[n].replace(/\./g," "));return t}(e.token),this.data=e}function s(e){return function(t,n){if(n.pending){var r=n.pending.shift();return 0==n.pending.length&&(n.pending=null),t.pos+=r.text.length,r.token}for(var a=e[n.state],o=0;o<a.length;o++){var s=a[o],i=(!s.data.sol||t.sol())&&t.match(s.regex);if(i){s.data.next?n.state=s.data.next:s.data.push?((n.stack||(n.stack=[])).push(n.state),n.state=s.data.push):s.data.pop&&n.stack&&n.stack.length&&(n.state=n.stack.pop()),s.data.indent&&n.indent.push(t.indentation()+t.indentUnit),s.data.dedent&&n.indent.pop();var g=s.token;if(g&&g.apply&&(g=g(i)),i.length>2&&s.token&&"string"!=typeof s.token){n.pending=[];for(var d=2;d<i.length;d++)i[d]&&n.pending.push({text:i[d],token:s.token[d-1]});return t.backUp(i[0].length-(i[1]?i[1].length:0)),g[0]}return g&&g.join?g[0]:g}}return t.next(),null}}function i(e,t){return function(n,r){if(null==n.indent||t.dontIndentStates&&t.doneIndentState.indexOf(n.state)>-1)return null;var a=n.indent.length-1,o=e[n.state];e:for(;;){for(var s=0;s<o.length;s++){var i=o[s];if(i.data.dedent&&!1!==i.data.dedentIfLineStart){var g=i.regex.exec(r);if(g&&g[0]){a--,(i.next||i.push)&&(o=e[i.next||i.push]),r=r.slice(g[0].length);continue e}}}break}return a<0?0:n.indent[a]}}n.d(t,{Q:()=>r})}}]);
//# sourceMappingURL=5464.nbdime.js.map