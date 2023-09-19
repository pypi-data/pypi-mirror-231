"use strict";(globalThis.webpackChunksuperset=globalThis.webpackChunksuperset||[]).push([[7156],{16579:(t,e,n)=>{n.r(e),n.d(e,{default:()=>T}),n(67294);var s=n(43323),a=n(51995),r=n(78580),l=n.n(r),i=n(15078),o=n.n(i),c=n(45697),p=n.n(c),h=n(28062),u=n(67190),d=n(45636),m=n(55867),g=n(45511);function y(t,e,n){t.each((function(){const t=o().select(this),s=t.text().split(/\s+/);let a=[],r=0;const l=t.attr("x"),i=t.attr("y"),c=parseFloat(t.attr("dy"));let p=t.text(null).append("tspan").attr("x",l).attr("y",i).attr("dy",`${c}em`),h=!1;s.forEach((n=>{a.push(n),p.text(a.join(" ")),p.node().getComputedTextLength()>e&&(r+=1,a.pop(),p.text(a.join(" ")),a=[n],p=t.append("tspan").attr("x",l).attr("y",i).attr("dy",`${1*r+c}em`).text(n),h=!0)})),h||void 0===n||p.attr("y",n)}))}const f={data:p().arrayOf(p().array),width:p().number,height:p().number,colorScheme:p().string,linearColorScheme:p().string,numberFormat:p().string,metrics:p().arrayOf(p().oneOfType([p().string,p().object]))};function b(t){return"string"==typeof t||t instanceof String?t:t.label}function x(t,e){const n=o().select(t),{data:s,width:a,height:r,colorScheme:i,linearColorScheme:c,metrics:p,numberFormat:f,sliceId:x}=e,$=function(t){return t>500?"l":t>200&&t<=500?"m":"s"}(a),v="s"===$;n.attr("class",`superset-legacy-chart-sunburst ${$}`);const w=a,T=r,N=.085*T,k=w-5-5,C=T-10-10-N,A=Math.min(k,C)/2;let S,z,P,W,Z,R,I,M=!0;const _=h.getScale(i);let j;const E=o().layout.partition().size([2*Math.PI,A*A]).value((t=>t.m1)),O=o().svg.arc().startAngle((t=>t.x)).endAngle((t=>t.x+t.dx)).innerRadius((t=>Math.sqrt(t.y))).outerRadius((t=>Math.sqrt(t.y+t.dy))),U=(0,u.JB)(f||d.Z.SI_3_DIGIT),D=(0,u.JB)(d.Z.PERCENT_3_POINT);n.select("svg").remove();const F=n.append("svg:svg").attr("width",w).attr("height",T);function L(t,e){const n=[];return v?(n.push("0,0"),n.push(`${a},0`),n.push(`${a},0`),n.push(`${a},${z.height}`),n.push(`0,${z.height}`)):(n.push("0,0"),n.push(`${z.width},0`),n.push(`${z.width+z.tipTailWidth},${z.height/2}`),n.push(`${z.width},${z.height}`),n.push(`0,${z.height}`),e>0&&n.push(`${z.tipTailWidth},${z.height/2}`)),n.join(" ")}function q(t){const e=function(t){const e=[];let n=t;for(;n.parent;)e.unshift(n),n=n.parent;return e}(t),n=e[e.length-2]||null,s=(t.m1/P).toPrecision(3),r=n?(t.m1/n.m1).toPrecision(3):null,i=D(s),c=n?D(r):"",h=function(t){return t>500?["0","20","40","60"]:t>200&&t<=500?["0","15","30","45"]:["0","10","20","30"]}(a);let u=0;const d=Math.abs(t.m1-t.m2)<1e-5;I.selectAll("*").remove(),u+=1,I.append("text").attr("class","path-abs-percent").attr("y",h[u]).text(i+" "+(0,m.t)("of total"));const g=(0,m.t)("of parent");c&&(u+=1,I.append("text").attr("class","path-cond-percent").attr("y",h[u]).text(`${c} ${g}`)),u+=1,I.append("text").attr("class","path-metrics").attr("y",h[u]).text(`${b(p[0])}: ${U(t.m1)}${d?"":`, ${b(p[1])}: ${U(t.m2)}`}`),u+=1,I.append("text").attr("class","path-ratio").attr("y",h[u]).text(d?"":`${b(p[1])}/${b(p[0])}: ${D(t.m2/t.m1)}`),R.selectAll("path").style("stroke-width",null).style("stroke",null).style("opacity",.3),R.selectAll("path").filter((t=>l()(e).call(e,t))).style("opacity",1).style("stroke","#aaa"),function(t,e){const n=v?a:z.width,s=W.selectAll("g").data(t,(t=>t.name+t.depth)),r=s.enter().append("svg:g");r.append("svg:polygon").attr("points",L).style("fill",(t=>M?_(t.name,x):j(t.m2/t.m1))),r.append("svg:text").attr("x",(n+z.tipTailWidth)/2).attr("y",z.height/4).attr("dy","0.35em").style("fill",(t=>o().hsl(M?_(t.name,x):j(t.m2/t.m1)).l<.5?"white":"black")).attr("class","step-label").text((t=>t.name.replace(/_/g," "))).call(y,n,z.height/2),s.attr("transform",((t,e)=>v?`translate(0, ${e*(z.height+z.spacing)})`:`translate(${e*(z.width+z.spacing)}, 0)`)),s.exit().remove(),W.select(".end-label").attr("x",(()=>v?(n+z.tipTailWidth)/2:(t.length+.5)*(z.width+z.spacing))).attr("y",(()=>v?(t.length+1)*z.height:z.height/2)).attr("dy","0.35em").text(e),W.style("visibility",null)}(e,i)}function B(){W.style("visibility","hidden"),I.selectAll("*").remove(),R.selectAll("path").on("mouseenter",null),R.selectAll("path").transition().duration(200).style("opacity",1).style("stroke",null).style("stroke-width",null).each("end",(function(){o().select(this).on("mouseenter",q)}))}var J;J=s[0],S=J.length-2+1,z={width:k/S,height:.8*N,spacing:3,tipTailWidth:10},W=F.append("svg:g").attr("class","breadcrumbs").attr("transform","translate(5,10)"),W.append("svg:text").attr("class","end-label"),function(t){const e=function(t){const e={name:"root",children:[]};return t.forEach((t=>{const n=Number(t[t.length-2]),s=Number(t[t.length-1]),a=t.slice(0,-2);if(Number.isNaN(n))return;let r=e;for(let t=0;t<a.length;t+=1){const e=r.children||[],l=a[t].toString();let i;t>=a.length-1||0===a[t+1]?0!==l&&(i={name:l,m1:n,m2:s},e.push(i)):(i=e.find((e=>e.name===l&&e.level===t)),i||(i={name:l,children:[],level:t},e.push(i)),r=i)}})),function t(e){if(e.children){let n,s=0,a=0;for(let r=0;r<e.children.length;r+=1)n=t(e.children[r]),s+=n[0],a+=n[1];e.m1=s,e.m2=a}return[e.m1,e.m2]}(e),e}(t);S=t[0].length-2,Z=F.append("svg:g").attr("class","sunburst-vis").attr("transform",`translate(${5+k/2},${10+(v?N*S:N)+C/2})`).on("mouseleave",B),R=Z.append("svg:g").attr("id","arcs"),I=Z.append("svg:g").attr("class","center-label"),R.append("svg:circle").attr("r",A).style("opacity",0);const n=E.nodes(e).filter((t=>t.dx>.005));if(p[0]!==p[1]&&p[1]){M=!1;const t=o().extent(n,(t=>t.m2/t.m1));j=(0,g.Z)().get(c).createLinearScale(t)}R.selectAll("path").data(n).enter().append("svg:path").attr("display",(t=>t.depth?null:"none")).attr("d",O).attr("fill-rule","evenodd").style("fill",(t=>M?_(t.name,x):j(t.m2/t.m1))).style("opacity",1).on("mouseenter",q),P=e.value}(s)}x.displayName="Sunburst",x.propTypes=f;const $=x;var v=n(11965);const w=(0,s.Z)($),T=(0,a.iK)((t=>{let{className:e,...n}=t;return(0,v.tZ)("div",{className:e},(0,v.tZ)(w,n))}))`
  ${t=>{let{theme:e}=t;return`\n    .superset-legacy-chart-sunburst text {\n      text-rendering: optimizeLegibility;\n    }\n    .superset-legacy-chart-sunburst path {\n      stroke: ${e.colors.grayscale.light2};\n      stroke-width: 0.5px;\n    }\n    .superset-legacy-chart-sunburst .center-label {\n      text-anchor: middle;\n      fill: ${e.colors.grayscale.dark1};\n      pointer-events: none;\n    }\n    .superset-legacy-chart-sunburst .path-abs-percent {\n      font-size: ${e.typography.sizes.m}px;\n      font-weight: ${e.typography.weights.bold};\n    }\n    .superset-legacy-chart-sunburst .path-cond-percent {\n      font-size: ${e.typography.sizes.s}px;\n    }\n    .superset-legacy-chart-sunburst .path-metrics {\n      color: ${e.colors.grayscale.base};\n    }\n    .superset-legacy-chart-sunburst .path-ratio {\n      color: ${e.colors.grayscale.base};\n    }\n\n    .superset-legacy-chart-sunburst .breadcrumbs text {\n      font-weight: ${e.typography.weights.bold};\n      font-size: ${e.typography.sizes.m}px;\n      text-anchor: middle;\n      fill: ${e.colors.grayscale.dark1};\n    }\n  `}}
`},43323:(t,e,n)=>{n.d(e,{Z:()=>r});var s=n(67294),a=n(11965);function r(t,e){class n extends s.Component{constructor(t){super(t),this.container=void 0,this.setContainerRef=this.setContainerRef.bind(this)}componentDidMount(){this.execute()}componentDidUpdate(){this.execute()}componentWillUnmount(){this.container=void 0,null!=e&&e.componentWillUnmount&&e.componentWillUnmount.bind(this)()}setContainerRef(t){this.container=t}execute(){this.container&&t(this.container,this.props)}render(){const{id:t,className:e}=this.props;return(0,a.tZ)("div",{ref:this.setContainerRef,id:t,className:e})}}const r=n;return t.displayName&&(r.displayName=t.displayName),t.propTypes&&(r.propTypes={...r.propTypes,...t.propTypes}),t.defaultProps&&(r.defaultProps=t.defaultProps),n}}}]);
//# sourceMappingURL=2dd1002db8b996ecacc5.chunk.js.map