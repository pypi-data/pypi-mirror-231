"use strict";(self.webpackChunknbdime_webapp=self.webpackChunknbdime_webapp||[]).push([[8245],{58245:function(t,e,r){var i,o=this&&this.__extends||(i=function(t,e){return i=Object.setPrototypeOf||{__proto__:[]}instanceof Array&&function(t,e){t.__proto__=e}||function(t,e){for(var r in e)Object.prototype.hasOwnProperty.call(e,r)&&(t[r]=e[r])},i(t,e)},function(t,e){if("function"!=typeof e&&null!==e)throw new TypeError("Class extends value "+String(e)+" is not a constructor or null");function r(){this.constructor=t}i(t,e),t.prototype=null===e?Object.create(e):(r.prototype=e.prototype,new r)}),n=this&&this.__assign||function(){return n=Object.assign||function(t){for(var e,r=1,i=arguments.length;r<i;r++)for(var o in e=arguments[r])Object.prototype.hasOwnProperty.call(e,o)&&(t[o]=e[o]);return t},n.apply(this,arguments)},s=this&&this.__read||function(t,e){var r="function"==typeof Symbol&&t[Symbol.iterator];if(!r)return t;var i,o,n=r.call(t),s=[];try{for(;(void 0===e||e-- >0)&&!(i=n.next()).done;)s.push(i.value)}catch(t){o={error:t}}finally{try{i&&!i.done&&(r=n.return)&&r.call(n)}finally{if(o)throw o.error}}return s},a=this&&this.__spreadArray||function(t,e,r){if(r||2===arguments.length)for(var i,o=0,n=e.length;o<n;o++)!i&&o in e||(i||(i=Array.prototype.slice.call(e,0,o)),i[o]=e[o]);return t.concat(i||Array.prototype.slice.call(e))},l=this&&this.__values||function(t){var e="function"==typeof Symbol&&Symbol.iterator,r=e&&t[e],i=0;if(r)return r.call(t);if(t&&"number"==typeof t.length)return{next:function(){return t&&i>=t.length&&(t=void 0),{value:t&&t[i++],done:!t}}};throw new TypeError(e?"Object is not iterable.":"Symbol.iterator is not defined.")};Object.defineProperty(e,"__esModule",{value:!0}),e.AssistiveMmlHandler=e.AssistiveMmlMathDocumentMixin=e.AssistiveMmlMathItemMixin=e.LimitedMmlVisitor=void 0;var u=r(31614),c=r(10280),p=r(76556),h=function(t){function e(){return null!==t&&t.apply(this,arguments)||this}return o(e,t),e.prototype.getAttributes=function(e){return t.prototype.getAttributes.call(this,e).replace(/ ?id=".*?"/,"")},e}(c.SerializedMmlVisitor);function f(t){return function(t){function e(){return null!==t&&t.apply(this,arguments)||this}return o(e,t),e.prototype.assistiveMml=function(t,e){if(void 0===e&&(e=!1),!(this.state()>=u.STATE.ASSISTIVEMML)){if(!this.isEscaped&&(t.options.enableAssistiveMml||e)){var r=t.adaptor,i=t.toMML(this.root).replace(/\n */g,"").replace(/<!--.*?-->/g,""),o=r.firstChild(r.body(r.parse(i,"text/html"))),n=r.node("mjx-assistive-mml",{unselectable:"on",display:this.display?"block":"inline"},[o]);r.setAttribute(r.firstChild(this.typesetRoot),"aria-hidden","true"),r.setStyle(this.typesetRoot,"position","relative"),r.append(this.typesetRoot,n)}this.state(u.STATE.ASSISTIVEMML)}},e}(t)}function y(t){var e;return e=function(t){function e(){for(var e=[],r=0;r<arguments.length;r++)e[r]=arguments[r];var i=t.apply(this,a([],s(e),!1))||this,o=i.constructor,n=o.ProcessBits;return n.has("assistive-mml")||n.allocate("assistive-mml"),i.visitor=new h(i.mmlFactory),i.options.MathItem=f(i.options.MathItem),"addStyles"in i&&i.addStyles(o.assistiveStyles),i}return o(e,t),e.prototype.toMML=function(t){return this.visitor.visitTree(t)},e.prototype.assistiveMml=function(){var t,e;if(!this.processed.isSet("assistive-mml")){try{for(var r=l(this.math),i=r.next();!i.done;i=r.next())i.value.assistiveMml(this)}catch(e){t={error:e}}finally{try{i&&!i.done&&(e=r.return)&&e.call(r)}finally{if(t)throw t.error}}this.processed.set("assistive-mml")}return this},e.prototype.state=function(e,r){return void 0===r&&(r=!1),t.prototype.state.call(this,e,r),e<u.STATE.ASSISTIVEMML&&this.processed.clear("assistive-mml"),this},e}(t),e.OPTIONS=n(n({},t.OPTIONS),{enableAssistiveMml:!0,renderActions:(0,p.expandable)(n(n({},t.OPTIONS.renderActions),{assistiveMml:[u.STATE.ASSISTIVEMML]}))}),e.assistiveStyles={"mjx-assistive-mml":{position:"absolute !important",top:"0px",left:"0px",clip:"rect(1px, 1px, 1px, 1px)",padding:"1px 0px 0px 0px !important",border:"0px !important",display:"block !important",width:"auto !important",overflow:"hidden !important","-webkit-touch-callout":"none","-webkit-user-select":"none","-khtml-user-select":"none","-moz-user-select":"none","-ms-user-select":"none","user-select":"none"},'mjx-assistive-mml[display="block"]':{width:"100% !important"}},e}e.LimitedMmlVisitor=h,(0,u.newState)("ASSISTIVEMML",153),e.AssistiveMmlMathItemMixin=f,e.AssistiveMmlMathDocumentMixin=y,e.AssistiveMmlHandler=function(t){return t.documentClass=y(t.documentClass),t}},1474:function(t,e,r){var i,o=this&&this.__extends||(i=function(t,e){return i=Object.setPrototypeOf||{__proto__:[]}instanceof Array&&function(t,e){t.__proto__=e}||function(t,e){for(var r in e)Object.prototype.hasOwnProperty.call(e,r)&&(t[r]=e[r])},i(t,e)},function(t,e){if("function"!=typeof e&&null!==e)throw new TypeError("Class extends value "+String(e)+" is not a constructor or null");function r(){this.constructor=t}i(t,e),t.prototype=null===e?Object.create(e):(r.prototype=e.prototype,new r)});Object.defineProperty(e,"__esModule",{value:!0}),e.MmlVisitor=void 0;var n=r(2383),s=function(t){function e(e){return void 0===e&&(e=null),e||(e=new n.MmlFactory),t.call(this,e)||this}return o(e,t),e.prototype.visitTextNode=function(t){for(var e=[],r=1;r<arguments.length;r++)e[r-1]=arguments[r]},e.prototype.visitXMLNode=function(t){for(var e=[],r=1;r<arguments.length;r++)e[r-1]=arguments[r]},e}(r(50562).AbstractVisitor);e.MmlVisitor=s},10280:function(t,e,r){var i,o=this&&this.__extends||(i=function(t,e){return i=Object.setPrototypeOf||{__proto__:[]}instanceof Array&&function(t,e){t.__proto__=e}||function(t,e){for(var r in e)Object.prototype.hasOwnProperty.call(e,r)&&(t[r]=e[r])},i(t,e)},function(t,e){if("function"!=typeof e&&null!==e)throw new TypeError("Class extends value "+String(e)+" is not a constructor or null");function r(){this.constructor=t}i(t,e),t.prototype=null===e?Object.create(e):(r.prototype=e.prototype,new r)}),n=this&&this.__values||function(t){var e="function"==typeof Symbol&&Symbol.iterator,r=e&&t[e],i=0;if(r)return r.call(t);if(t&&"number"==typeof t.length)return{next:function(){return t&&i>=t.length&&(t=void 0),{value:t&&t[i++],done:!t}}};throw new TypeError(e?"Object is not iterable.":"Symbol.iterator is not defined.")},s=this&&this.__read||function(t,e){var r="function"==typeof Symbol&&t[Symbol.iterator];if(!r)return t;var i,o,n=r.call(t),s=[];try{for(;(void 0===e||e-- >0)&&!(i=n.next()).done;)s.push(i.value)}catch(t){o={error:t}}finally{try{i&&!i.done&&(r=n.return)&&r.call(n)}finally{if(o)throw o.error}}return s};Object.defineProperty(e,"__esModule",{value:!0}),e.SerializedMmlVisitor=e.toEntity=e.DATAMJX=void 0;var a=r(1474),l=r(84644),u=r(91864);e.DATAMJX="data-mjx-",e.toEntity=function(t){return"&#x"+t.codePointAt(0).toString(16).toUpperCase()+";"};var c=function(t){function r(){return null!==t&&t.apply(this,arguments)||this}return o(r,t),r.prototype.visitTree=function(t){return this.visitNode(t,"")},r.prototype.visitTextNode=function(t,e){return this.quoteHTML(t.getText())},r.prototype.visitXMLNode=function(t,e){return e+t.getSerializedXML()},r.prototype.visitInferredMrowNode=function(t,e){var r,i,o=[];try{for(var s=n(t.childNodes),a=s.next();!a.done;a=s.next()){var l=a.value;o.push(this.visitNode(l,e))}}catch(t){r={error:t}}finally{try{a&&!a.done&&(i=s.return)&&i.call(s)}finally{if(r)throw r.error}}return o.join("\n")},r.prototype.visitTeXAtomNode=function(t,e){var r=this.childNodeMml(t,e+"  ","\n");return e+"<mrow"+this.getAttributes(t)+">"+(r.match(/\S/)?"\n"+r+e:"")+"</mrow>"},r.prototype.visitAnnotationNode=function(t,e){return e+"<annotation"+this.getAttributes(t)+">"+this.childNodeMml(t,"","")+"</annotation>"},r.prototype.visitDefault=function(t,e){var r=t.kind,i=s(t.isToken||0===t.childNodes.length?["",""]:["\n",e],2),o=i[0],n=i[1],a=this.childNodeMml(t,e+"  ",o);return e+"<"+r+this.getAttributes(t)+">"+(a.match(/\S/)?o+a+n:"")+"</"+r+">"},r.prototype.childNodeMml=function(t,e,r){var i,o,s="";try{for(var a=n(t.childNodes),l=a.next();!l.done;l=a.next()){var u=l.value;s+=this.visitNode(u,e)+r}}catch(t){i={error:t}}finally{try{l&&!l.done&&(o=a.return)&&o.call(a)}finally{if(i)throw i.error}}return s},r.prototype.getAttributes=function(t){var e,r,i=[],o=this.constructor.defaultAttributes[t.kind]||{},s=Object.assign({},o,this.getDataAttributes(t),t.attributes.getAllAttributes()),a=this.constructor.variants;s.hasOwnProperty("mathvariant")&&a.hasOwnProperty(s.mathvariant)&&(s.mathvariant=a[s.mathvariant]);try{for(var l=n(Object.keys(s)),u=l.next();!u.done;u=l.next()){var c=u.value,p=String(s[c]);void 0!==p&&i.push(c+'="'+this.quoteHTML(p)+'"')}}catch(t){e={error:t}}finally{try{u&&!u.done&&(r=l.return)&&r.call(l)}finally{if(e)throw e.error}}return i.length?" "+i.join(" "):""},r.prototype.getDataAttributes=function(t){var e={},r=t.attributes.getExplicit("mathvariant"),i=this.constructor.variants;r&&i.hasOwnProperty(r)&&this.setDataAttribute(e,"variant",r),t.getProperty("variantForm")&&this.setDataAttribute(e,"alternate","1"),t.getProperty("pseudoscript")&&this.setDataAttribute(e,"pseudoscript","true"),!1===t.getProperty("autoOP")&&this.setDataAttribute(e,"auto-op","false");var o=t.getProperty("scriptalign");o&&this.setDataAttribute(e,"script-align",o);var n=t.getProperty("texClass");if(void 0!==n){var s=!0;if(n===l.TEXCLASS.OP&&t.isKind("mi")){var a=t.getText();s=!(a.length>1&&a.match(u.MmlMi.operatorName))}s&&this.setDataAttribute(e,"texclass",n<0?"NONE":l.TEXCLASSNAMES[n])}return t.getProperty("scriptlevel")&&!1===t.getProperty("useHeight")&&this.setDataAttribute(e,"smallmatrix","true"),e},r.prototype.setDataAttribute=function(t,r,i){t[e.DATAMJX+r]=i},r.prototype.quoteHTML=function(t){return t.replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;").replace(/\"/g,"&quot;").replace(/[\uD800-\uDBFF]./g,e.toEntity).replace(/[\u0080-\uD7FF\uE000-\uFFFF]/g,e.toEntity)},r.variants={"-tex-calligraphic":"script","-tex-bold-calligraphic":"bold-script","-tex-oldstyle":"normal","-tex-bold-oldstyle":"bold","-tex-mathit":"italic"},r.defaultAttributes={math:{xmlns:"http://www.w3.org/1998/Math/MathML"}},r}(a.MmlVisitor);e.SerializedMmlVisitor=c},50562:function(t,e,r){var i=this&&this.__values||function(t){var e="function"==typeof Symbol&&Symbol.iterator,r=e&&t[e],i=0;if(r)return r.call(t);if(t&&"number"==typeof t.length)return{next:function(){return t&&i>=t.length&&(t=void 0),{value:t&&t[i++],done:!t}}};throw new TypeError(e?"Object is not iterable.":"Symbol.iterator is not defined.")},o=this&&this.__read||function(t,e){var r="function"==typeof Symbol&&t[Symbol.iterator];if(!r)return t;var i,o,n=r.call(t),s=[];try{for(;(void 0===e||e-- >0)&&!(i=n.next()).done;)s.push(i.value)}catch(t){o={error:t}}finally{try{i&&!i.done&&(r=n.return)&&r.call(n)}finally{if(o)throw o.error}}return s},n=this&&this.__spreadArray||function(t,e,r){if(r||2===arguments.length)for(var i,o=0,n=e.length;o<n;o++)!i&&o in e||(i||(i=Array.prototype.slice.call(e,0,o)),i[o]=e[o]);return t.concat(i||Array.prototype.slice.call(e))};Object.defineProperty(e,"__esModule",{value:!0}),e.AbstractVisitor=void 0;var s=r(5437),a=function(){function t(e){var r,o;this.nodeHandlers=new Map;try{for(var n=i(e.getKinds()),s=n.next();!s.done;s=n.next()){var a=s.value,l=this[t.methodName(a)];l&&this.nodeHandlers.set(a,l)}}catch(t){r={error:t}}finally{try{s&&!s.done&&(o=n.return)&&o.call(n)}finally{if(r)throw r.error}}}return t.methodName=function(t){return"visit"+(t.charAt(0).toUpperCase()+t.substr(1)).replace(/[^a-z0-9_]/gi,"_")+"Node"},t.prototype.visitTree=function(t){for(var e=[],r=1;r<arguments.length;r++)e[r-1]=arguments[r];return this.visitNode.apply(this,n([t],o(e),!1))},t.prototype.visitNode=function(t){for(var e=[],r=1;r<arguments.length;r++)e[r-1]=arguments[r];var i=this.nodeHandlers.get(t.kind)||this.visitDefault;return i.call.apply(i,n([this,t],o(e),!1))},t.prototype.visitDefault=function(t){for(var e,r,a=[],l=1;l<arguments.length;l++)a[l-1]=arguments[l];if(t instanceof s.AbstractNode)try{for(var u=i(t.childNodes),c=u.next();!c.done;c=u.next()){var p=c.value;this.visitNode.apply(this,n([p],o(a),!1))}}catch(t){e={error:t}}finally{try{c&&!c.done&&(r=u.return)&&r.call(u)}finally{if(e)throw e.error}}},t.prototype.setNodeHandler=function(t,e){this.nodeHandlers.set(t,e)},t.prototype.removeNodeHandler=function(t){this.nodeHandlers.delete(t)},t}();e.AbstractVisitor=a}}]);
//# sourceMappingURL=8245.nbdime.js.map