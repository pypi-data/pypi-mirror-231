"use strict";(globalThis.webpackChunksuperset=globalThis.webpackChunksuperset||[]).push([[323],{40323:(e,t,n)=>{n.d(t,{Z:()=>E});var r=n(67294),i=n(45697),s=n.n(i),o="undefined"!=typeof window?window:null,a=null===o,u=a?void 0:o.document,l="horizontal",c=function(){return!1},d=a?"calc":["","-webkit-","-moz-","-o-"].filter((function(e){var t=u.createElement("div");return t.style.cssText="width:"+e+"calc(9px)",!!t.style.length})).shift()+"calc",p=function(e){return"string"==typeof e||e instanceof String},f=function(e){if(p(e)){var t=u.querySelector(e);if(!t)throw new Error("Selector "+e+" did not match a DOM element");return t}return e},v=function(e,t,n){var r=e[t];return void 0!==r?r:n},g=function(e,t,n,r){if(t){if("end"===r)return 0;if("center"===r)return e/2}else if(n){if("start"===r)return 0;if("center"===r)return e/2}return e},m=function(e,t){var n=u.createElement("div");return n.className="gutter gutter-"+t,n},h=function(e,t,n){var r={};return p(t)?r[e]=t:r[e]=d+"("+t+"% - "+n+"px)",r},y=function(e,t){var n;return(n={})[e]=t+"px",n};const z=function(e,t){if(void 0===t&&(t={}),a)return{};var n,r,i,s,d,p,z=e;Array.from&&(z=Array.from(z));var S=f(z[0]).parentNode,b=getComputedStyle?getComputedStyle(S):null,E=b?b.flexDirection:null,_=v(t,"sizes")||z.map((function(){return 100/z.length})),O=v(t,"minSize",100),L=Array.isArray(O)?O:z.map((function(){return O})),w=v(t,"expandToMin",!1),D=v(t,"gutterSize",10),A=v(t,"gutterAlign","center"),x=v(t,"snapOffset",30),M=v(t,"dragInterval",1),T=v(t,"direction",l),k=v(t,"cursor",T===l?"col-resize":"row-resize"),C=v(t,"gutter",m),U=v(t,"elementStyle",h),I=v(t,"gutterStyle",y);function j(e,t,r,i){var s=U(n,t,r,i);Object.keys(s).forEach((function(t){e.style[t]=s[t]}))}function B(){return p.map((function(e){return e.size}))}function F(e){return"touches"in e?e.touches[0][r]:e[r]}function N(e){var t=p[this.a],n=p[this.b],r=t.size+n.size;t.size=e/this.size*r,n.size=r-e/this.size*r,j(t.element,t.size,this._b,t.i),j(n.element,n.size,this._c,n.i)}function R(e){var n,r=p[this.a],i=p[this.b];this.dragging&&(n=F(e)-this.start+(this._b-this.dragOffset),M>1&&(n=Math.round(n/M)*M),n<=r.minSize+x+this._b?n=r.minSize+this._b:n>=this.size-(i.minSize+x+this._c)&&(n=this.size-(i.minSize+this._c)),N.call(this,n),v(t,"onDrag",c)(B()))}function G(){var e=p[this.a].element,t=p[this.b].element,r=e.getBoundingClientRect(),o=t.getBoundingClientRect();this.size=r[n]+o[n]+this._b+this._c,this.start=r[i],this.end=r[s]}function P(e){var t=function(e){if(!getComputedStyle)return null;var t=getComputedStyle(e);if(!t)return null;var n=e[d];return 0===n?null:n-=T===l?parseFloat(t.paddingLeft)+parseFloat(t.paddingRight):parseFloat(t.paddingTop)+parseFloat(t.paddingBottom)}(S);if(null===t)return e;if(L.reduce((function(e,t){return e+t}),0)>t)return e;var n=0,r=[],i=e.map((function(i,s){var o=t*i/100,a=g(D,0===s,s===e.length-1,A),u=L[s]+a;return o<u?(n+=u-o,r.push(0),u):(r.push(o-u),o)}));return 0===n?e:i.map((function(e,i){var s=e;if(n>0&&r[i]-n>0){var o=Math.min(n,r[i]-n);n-=o,s=e-o}return s/t*100}))}function W(){var e=this,n=p[e.a].element,r=p[e.b].element;e.dragging&&v(t,"onDragEnd",c)(B()),e.dragging=!1,o.removeEventListener("mouseup",e.stop),o.removeEventListener("touchend",e.stop),o.removeEventListener("touchcancel",e.stop),o.removeEventListener("mousemove",e.move),o.removeEventListener("touchmove",e.move),e.stop=null,e.move=null,n.removeEventListener("selectstart",c),n.removeEventListener("dragstart",c),r.removeEventListener("selectstart",c),r.removeEventListener("dragstart",c),n.style.userSelect="",n.style.webkitUserSelect="",n.style.MozUserSelect="",n.style.pointerEvents="",r.style.userSelect="",r.style.webkitUserSelect="",r.style.MozUserSelect="",r.style.pointerEvents="",e.gutter.style.cursor="",e.parent.style.cursor="",u.body.style.cursor=""}function q(e){if(!("button"in e)||0===e.button){var n=this,r=p[n.a].element,i=p[n.b].element;n.dragging||v(t,"onDragStart",c)(B()),e.preventDefault(),n.dragging=!0,n.move=R.bind(n),n.stop=W.bind(n),o.addEventListener("mouseup",n.stop),o.addEventListener("touchend",n.stop),o.addEventListener("touchcancel",n.stop),o.addEventListener("mousemove",n.move),o.addEventListener("touchmove",n.move),r.addEventListener("selectstart",c),r.addEventListener("dragstart",c),i.addEventListener("selectstart",c),i.addEventListener("dragstart",c),r.style.userSelect="none",r.style.webkitUserSelect="none",r.style.MozUserSelect="none",r.style.pointerEvents="none",i.style.userSelect="none",i.style.webkitUserSelect="none",i.style.MozUserSelect="none",i.style.pointerEvents="none",n.gutter.style.cursor=k,n.parent.style.cursor=k,u.body.style.cursor=k,G.call(n),n.dragOffset=F(e)-n.end}}T===l?(n="width",r="clientX",i="left",s="right",d="clientWidth"):"vertical"===T&&(n="height",r="clientY",i="top",s="bottom",d="clientHeight"),_=P(_);var H=[];function X(e){var t=e.i===H.length,n=t?H[e.i-1]:H[e.i];G.call(n);var r=t?n.size-e.minSize-n._c:e.minSize+n._b;N.call(n,r)}return(p=z.map((function(e,t){var r,i={element:f(e),size:_[t],minSize:L[t],i:t};if(t>0&&((r={a:t-1,b:t,dragging:!1,direction:T,parent:S})._b=g(D,t-1==0,!1,A),r._c=g(D,!1,t===z.length-1,A),"row-reverse"===E||"column-reverse"===E)){var s=r.a;r.a=r.b,r.b=s}if(t>0){var o=C(t,T,i.element);!function(e,t,r){var i=I(n,t,r);Object.keys(i).forEach((function(t){e.style[t]=i[t]}))}(o,D,t),r._a=q.bind(r),o.addEventListener("mousedown",r._a),o.addEventListener("touchstart",r._a),S.insertBefore(o,i.element),r.gutter=o}return j(i.element,i.size,g(D,0===t,t===z.length-1,A),t),t>0&&H.push(r),i}))).forEach((function(e){var t=e.element.getBoundingClientRect()[n];t<e.minSize&&(w?X(e):e.minSize=t)})),{setSizes:function(e){var t=P(e);t.forEach((function(e,n){if(n>0){var r=H[n-1],i=p[r.a],s=p[r.b];i.size=t[n-1],s.size=e,j(i.element,i.size,r._b,i.i),j(s.element,s.size,r._c,s.i)}}))},getSizes:B,collapse:function(e){X(p[e])},destroy:function(e,t){H.forEach((function(r){if(!0!==t?r.parent.removeChild(r.gutter):(r.gutter.removeEventListener("mousedown",r._a),r.gutter.removeEventListener("touchstart",r._a)),!0!==e){var i=U(n,r.a.size,r._b);Object.keys(i).forEach((function(e){p[r.a].element.style[e]="",p[r.b].element.style[e]=""}))}}))},parent:S,pairs:H}};function S(e,t){var n={};for(var r in e)Object.prototype.hasOwnProperty.call(e,r)&&-1===t.indexOf(r)&&(n[r]=e[r]);return n}var b=function(e){function t(){e.apply(this,arguments)}return e&&(t.__proto__=e),t.prototype=Object.create(e&&e.prototype),t.prototype.constructor=t,t.prototype.componentDidMount=function(){var e=this.props;e.children;var t=e.gutter,n=S(e,["children","gutter"]);n.gutter=function(e,n){var r;return t?r=t(e,n):(r=document.createElement("div")).className="gutter gutter-"+n,r.__isSplitGutter=!0,r},this.split=z(this.parent.children,n)},t.prototype.componentDidUpdate=function(e){var t=this,n=this.props;n.children;var r=n.minSize,i=n.sizes,s=n.collapsed,o=S(n,["children","minSize","sizes","collapsed"]),a=e.minSize,u=e.sizes,l=e.collapsed,c=["maxSize","expandToMin","gutterSize","gutterAlign","snapOffset","dragInterval","direction","cursor"].map((function(n){return t.props[n]!==e[n]})).reduce((function(e,t){return e||t}),!1);if(Array.isArray(r)&&Array.isArray(a)){var d=!1;r.forEach((function(e,t){d=d||e!==a[t]})),c=c||d}else c=!(!Array.isArray(r)&&!Array.isArray(a))||c||r!==a;if(c)o.minSize=r,o.sizes=i||this.split.getSizes(),this.split.destroy(!0,!0),o.gutter=function(e,t,n){return n.previousSibling},this.split=z(Array.from(this.parent.children).filter((function(e){return!e.__isSplitGutter})),o);else if(i){var p=!1;i.forEach((function(e,t){p=p||e!==u[t]})),p&&this.split.setSizes(this.props.sizes)}Number.isInteger(s)&&(s!==l||c)&&this.split.collapse(s)},t.prototype.componentWillUnmount=function(){this.split.destroy(),delete this.split},t.prototype.render=function(){var e=this,t=this.props;t.sizes,t.minSize,t.maxSize,t.expandToMin,t.gutterSize,t.gutterAlign,t.snapOffset,t.dragInterval,t.direction,t.cursor,t.gutter,t.elementStyle,t.gutterStyle,t.onDrag,t.onDragStart,t.onDragEnd,t.collapsed;var n=t.children,i=S(t,["sizes","minSize","maxSize","expandToMin","gutterSize","gutterAlign","snapOffset","dragInterval","direction","cursor","gutter","elementStyle","gutterStyle","onDrag","onDragStart","onDragEnd","collapsed","children"]);return r.createElement("div",Object.assign({},{ref:function(t){e.parent=t}},i),n)},t}(r.Component);b.propTypes={sizes:s().arrayOf(s().number),minSize:s().oneOfType([s().number,s().arrayOf(s().number)]),maxSize:s().oneOfType([s().number,s().arrayOf(s().number)]),expandToMin:s().bool,gutterSize:s().number,gutterAlign:s().string,snapOffset:s().oneOfType([s().number,s().arrayOf(s().number)]),dragInterval:s().number,direction:s().string,cursor:s().string,gutter:s().func,elementStyle:s().func,gutterStyle:s().func,onDrag:s().func,onDragStart:s().func,onDragEnd:s().func,collapsed:s().number,children:s().arrayOf(s().element)},b.defaultProps={sizes:void 0,minSize:void 0,maxSize:void 0,expandToMin:void 0,gutterSize:void 0,gutterAlign:void 0,snapOffset:void 0,dragInterval:void 0,direction:void 0,cursor:void 0,gutter:void 0,elementStyle:void 0,gutterStyle:void 0,onDrag:void 0,onDragStart:void 0,onDragEnd:void 0,collapsed:void 0,children:void 0};const E=b}}]);
//# sourceMappingURL=323.323ae901ba7565bddc59.entry.js.map