"use strict";(self.webpackChunknbdime_webapp=self.webpackChunknbdime_webapp||[]).push([[5190],{28849:(t,e)=>{Object.defineProperty(e,"__esModule",{value:!0}),e.VERSION=void 0,e.VERSION="3.2.2"},9203:function(t,e,r){var n,o=this&&this.__extends||(n=function(t,e){return n=Object.setPrototypeOf||{__proto__:[]}instanceof Array&&function(t,e){t.__proto__=e}||function(t,e){for(var r in e)Object.prototype.hasOwnProperty.call(e,r)&&(t[r]=e[r])},n(t,e)},function(t,e){if("function"!=typeof e&&null!==e)throw new TypeError("Class extends value "+String(e)+" is not a constructor or null");function r(){this.constructor=t}n(t,e),t.prototype=null===e?Object.create(e):(r.prototype=e.prototype,new r)}),i=this&&this.__values||function(t){var e="function"==typeof Symbol&&Symbol.iterator,r=e&&t[e],n=0;if(r)return r.call(t);if(t&&"number"==typeof t.length)return{next:function(){return t&&n>=t.length&&(t=void 0),{value:t&&t[n++],done:!t}}};throw new TypeError(e?"Object is not iterable.":"Symbol.iterator is not defined.")};Object.defineProperty(e,"__esModule",{value:!0}),e.HandlerList=void 0;var u=function(t){function e(){return null!==t&&t.apply(this,arguments)||this}return o(e,t),e.prototype.register=function(t){return this.add(t,t.priority)},e.prototype.unregister=function(t){this.remove(t)},e.prototype.handlesDocument=function(t){var e,r;try{for(var n=i(this),o=n.next();!o.done;o=n.next()){var u=o.value.item;if(u.handlesDocument(t))return u}}catch(t){e={error:t}}finally{try{o&&!o.done&&(r=n.return)&&r.call(n)}finally{if(e)throw e.error}}throw new Error("Can't find handler for document")},e.prototype.document=function(t,e){return void 0===e&&(e=null),this.handlesDocument(t).create(t,e)},e}(r(83801).PrioritizedList);e.HandlerList=u},85190:(t,e,r)=>{Object.defineProperty(e,"__esModule",{value:!0}),e.mathjax=void 0;var n=r(28849),o=r(9203),i=r(38708);e.mathjax={version:n.VERSION,handlers:new o.HandlerList,document:function(t,r){return e.mathjax.handlers.document(t,r)},handleRetriesFor:i.handleRetriesFor,retryAfter:i.retryAfter,asyncLoad:null}},83801:(t,e)=>{Object.defineProperty(e,"__esModule",{value:!0}),e.PrioritizedList=void 0;var r=function(){function t(){this.items=[],this.items=[]}return t.prototype[Symbol.iterator]=function(){var t=0,e=this.items;return{next:function(){return{value:e[t++],done:t>e.length}}}},t.prototype.add=function(e,r){void 0===r&&(r=t.DEFAULTPRIORITY);var n=this.items.length;do{n--}while(n>=0&&r<this.items[n].priority);return this.items.splice(n+1,0,{item:e,priority:r}),e},t.prototype.remove=function(t){var e=this.items.length;do{e--}while(e>=0&&this.items[e].item!==t);e>=0&&this.items.splice(e,1)},t.DEFAULTPRIORITY=5,t}();e.PrioritizedList=r},38708:(t,e)=>{Object.defineProperty(e,"__esModule",{value:!0}),e.retryAfter=e.handleRetriesFor=void 0,e.handleRetriesFor=function(t){return new Promise((function e(r,n){try{r(t())}catch(t){t.retry&&t.retry instanceof Promise?t.retry.then((function(){return e(r,n)})).catch((function(t){return n(t)})):t.restart&&t.restart.isCallback?MathJax.Callback.After((function(){return e(r,n)}),t.restart):n(t)}}))},e.retryAfter=function(t){var e=new Error("MathJax retry");throw e.retry=t,e}}}]);
//# sourceMappingURL=5190.nbdime.js.map