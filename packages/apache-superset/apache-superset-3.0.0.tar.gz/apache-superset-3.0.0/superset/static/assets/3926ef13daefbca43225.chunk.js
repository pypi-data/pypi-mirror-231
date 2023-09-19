"use strict";(globalThis.webpackChunksuperset=globalThis.webpackChunksuperset||[]).push([[1877,8623],{88623:(t,e,o)=>{o.r(e),o.d(e,{DEFAULT_MAX_ZOOM:()=>f,DEFAULT_POINT_RADIUS:()=>v,default:()=>M});var i=o(5872),r=o.n(i),n=o(67294),s=o(45697),a=o.n(s),u=o(90530),h=o(81458);function p(t,e){let o,i=e;return o=e?Math.round(t*(i=10**i))/i:Math.round(t),o}function l(t,e,o){const i=e*(Math.PI/180);return p(t/(40075.16*Math.cos(i)/2**(o+9)),2)}var d=o(11965);const c={aggregation:a().string,compositeOperation:a().string,dotRadius:a().number,lngLatAccessor:a().func,locations:a().arrayOf(a().object).isRequired,pointRadiusUnit:a().string,renderWhileDragging:a().bool,rgb:a().arrayOf(a().oneOfType([a().string,a().number])),zoom:a().number};class g extends n.PureComponent{constructor(t){super(t),this.redraw=this.redraw.bind(this)}drawText(t,e,o){void 0===o&&(o={});const{fontHeight:i=0,label:r="",radius:n=0,rgb:s=[0,0,0],shadow:a=!1}=o,u=1.8*n,h=.2126*s[1]+.7152*s[2]+.0722*s[3];t.globalCompositeOperation="source-over",t.fillStyle=h<=110?"white":"black",t.font=`${i}px sans-serif`,t.textAlign="center",t.textBaseline="middle",a&&(t.shadowBlur=15,t.shadowColor=h<=110?"black":"");const p=t.measureText(r).width;if(p>u){const e=i/p;t.font=e*u+"px sans-serif"}const{compositeOperation:l}=this.props;t.fillText(r,e[0],e[1]),t.globalCompositeOperation=l,t.shadowBlur=0,t.shadowColor=""}redraw(t){let{width:e,height:o,ctx:i,isDragging:r,project:n}=t;const{aggregation:s,compositeOperation:a,dotRadius:u,lngLatAccessor:h,locations:d,pointRadiusUnit:c,renderWhileDragging:g,rgb:m,zoom:f}=this.props,v=u,b=[];d.forEach(((t,e)=>{t.properties.cluster&&(b[e]=((t,e)=>{const o=t.point_count;if(!e)return o;if("sum"===e||"min"===e||"max"===e)return t[e];const{sum:i}=t,r=i/o;if("mean"===e)return Math.round(100*r)/100;const{squaredSum:n}=t,s=n/o-(i/o)**2;return"var"===e?Math.round(100*s)/100:"stdev"===e?Math.round(100*Math.sqrt(s))/100:o})(t.properties,s))}),this);const w=Math.max(...b.filter((t=>!Number.isNaN(t))));i.clearRect(0,0,e,o),i.globalCompositeOperation=a,!g&&r||!d||d.forEach((function(t,r){const s=n(h(t)),a=[p(s[0],1),p(s[1],1)];if(a[0]+v>=0&&a[0]-v<e&&a[1]+v>=0&&a[1]-v<o)if(i.beginPath(),t.properties.cluster){let t=b[r];const e=p((t/w)**.5*v,1),o=p(.5*e,1),[n,s]=a,u=i.createRadialGradient(n,s,e,n,s,0);u.addColorStop(1,`rgba(${m[1]}, ${m[2]}, ${m[3]}, 0.8)`),u.addColorStop(0,`rgba(${m[1]}, ${m[2]}, ${m[3]}, 0)`),i.arc(a[0],a[1],e,0,2*Math.PI),i.fillStyle=u,i.fill(),Number.isFinite(parseFloat(t))&&(t>=1e4?t=`${Math.round(t/1e3)}k`:t>=1e3&&(t=Math.round(t/100)/10+"k"),this.drawText(i,a,{fontHeight:o,label:t,radius:e,rgb:m,shadow:!0}))}else{const e=v/6,o=t.properties.radius,r=t.properties.metric;let n,s=null===o?e:o;if(null!==o){const e=h(t)[1];"Kilometers"===c?(n=`${p(s,2)}km`,s=l(s,e,f)):"Miles"===c&&(n=`${p(s,2)}mi`,s=l(1.60934*s,e,f))}null!==r&&(n=Number.isFinite(parseFloat(r))?p(r,2):r),s||(s=e),i.arc(a[0],a[1],p(s,1),0,2*Math.PI),i.fillStyle=`rgb(${m[1]}, ${m[2]}, ${m[3]})`,i.fill(),void 0!==n&&this.drawText(i,a,{fontHeight:p(s,1),label:n,radius:s,rgb:m,shadow:!1})}}),this)}render(){return(0,d.tZ)(u.s0,{redraw:this.redraw})}}g.propTypes=c,g.defaultProps={compositeOperation:"source-over",dotRadius:4,lngLatAccessor:t=>[t[0],t[1]],renderWhileDragging:!0};const m=g,f=16,v=60,b={width:a().number,height:a().number,aggregatorName:a().string,clusterer:a().object,globalOpacity:a().number,hasCustomMetric:a().bool,mapStyle:a().string,mapboxApiKey:a().string.isRequired,onViewportChange:a().func,pointRadius:a().number,pointRadiusUnit:a().string,renderWhileDragging:a().bool,rgb:a().array,bounds:a().array},w={width:400,height:400,globalOpacity:1,onViewportChange:()=>{},pointRadius:v,pointRadiusUnit:"Pixels"};class x extends n.Component{constructor(t){super(t);const{width:e,height:o,bounds:i}=this.props,r=new h.Z({width:e,height:o}).fitBounds(i),{latitude:n,longitude:s,zoom:a}=r;this.state={viewport:{longitude:s,latitude:n,zoom:a}},this.handleViewportChange=this.handleViewportChange.bind(this)}handleViewportChange(t){this.setState({viewport:t});const{onViewportChange:e}=this.props;e(t)}render(){const{width:t,height:e,aggregatorName:o,clusterer:i,globalOpacity:n,mapStyle:s,mapboxApiKey:a,pointRadius:h,pointRadiusUnit:p,renderWhileDragging:l,rgb:c,hasCustomMetric:g,bounds:f}=this.props,{viewport:v}=this.state,b=void 0!==v.isDragging&&v.isDragging,w=.5*t/100,x=.5*e/100,M=[f[0][0]-w,f[0][1]-x,f[1][0]+w,f[1][1]+x],y=i.getClusters(M,Math.round(v.zoom));return(0,d.tZ)(u.ZP,r()({},v,{mapStyle:s,width:t,height:e,mapboxApiAccessToken:a,onViewportChange:this.handleViewportChange,preserveDrawingBuffer:!0}),(0,d.tZ)(m,r()({},v,{isDragging:b,locations:y,dotRadius:h,pointRadiusUnit:p,rgb:c,globalOpacity:n,compositeOperation:"screen",renderWhileDragging:l,aggregation:g?o:null,lngLatAccessor:t=>{const{coordinates:e}=t.geometry;return[e[0],e[1]]}})))}}x.propTypes=b,x.defaultProps=w;const M=x},1877:(t,e,o)=>{function i(t,e,o,n,s,a){if(!(s-n<=o)){var u=Math.floor((n+s)/2);r(t,e,u,n,s,a%2),i(t,e,o,n,u-1,a+1),i(t,e,o,u+1,s,a+1)}}function r(t,e,o,i,s,a){for(;s>i;){if(s-i>600){var u=s-i+1,h=o-i+1,p=Math.log(u),l=.5*Math.exp(2*p/3),d=.5*Math.sqrt(p*l*(u-l)/u)*(h-u/2<0?-1:1);r(t,e,o,Math.max(i,Math.floor(o-h*l/u+d)),Math.min(s,Math.floor(o+(u-h)*l/u+d)),a)}var c=e[2*o+a],g=i,m=s;for(n(t,e,i,o),e[2*s+a]>c&&n(t,e,i,s);g<m;){for(n(t,e,g,m),g++,m--;e[2*g+a]<c;)g++;for(;e[2*m+a]>c;)m--}e[2*i+a]===c?n(t,e,i,m):n(t,e,++m,s),m<=o&&(i=m+1),o<=m&&(s=m-1)}}function n(t,e,o,i){s(t,o,i),s(e,2*o,2*i),s(e,2*o+1,2*i+1)}function s(t,e,o){var i=t[e];t[e]=t[o],t[o]=i}function a(t,e,o,i){var r=t-o,n=e-i;return r*r+n*n}function u(t,e,o,i,r){return new h(t,e,o,i,r)}function h(t,e,o,r,n){e=e||p,o=o||l,n=n||Array,this.nodeSize=r||64,this.points=t,this.ids=new n(t.length),this.coords=new n(2*t.length);for(var s=0;s<t.length;s++)this.ids[s]=s,this.coords[2*s]=e(t[s]),this.coords[2*s+1]=o(t[s]);i(this.ids,this.coords,this.nodeSize,0,this.ids.length-1,0)}function p(t){return t[0]}function l(t){return t[1]}function d(t){this.options=b(Object.create(this.options),t),this.trees=new Array(this.options.maxZoom+1)}function c(t,e,o,i,r){return{x:t,y:e,zoom:1/0,id:o,parentId:-1,numPoints:i,properties:r}}function g(t){return{type:"Feature",id:t.id,properties:m(t),geometry:{type:"Point",coordinates:[(i=t.x,360*(i-.5)),(e=t.y,o=(180-360*e)*Math.PI/180,360*Math.atan(Math.exp(o))/Math.PI-90)]}};var e,o,i}function m(t){var e=t.numPoints,o=e>=1e4?Math.round(e/1e3)+"k":e>=1e3?Math.round(e/100)/10+"k":e;return b(b({},t.properties),{cluster:!0,cluster_id:t.id,point_count:e,point_count_abbreviated:o})}function f(t){return t/360+.5}function v(t){var e=Math.sin(t*Math.PI/180),o=.5-.25*Math.log((1+e)/(1-e))/Math.PI;return o<0?0:o>1?1:o}function b(t,e){for(var o in e)t[o]=e[o];return t}function w(t){return t.x}function x(t){return t.y}o.r(e),o.d(e,{default:()=>C}),h.prototype={range:function(t,e,o,i){return function(t,e,o,i,r,n,s){for(var a,u,h=[0,t.length-1,0],p=[];h.length;){var l=h.pop(),d=h.pop(),c=h.pop();if(d-c<=s)for(var g=c;g<=d;g++)a=e[2*g],u=e[2*g+1],a>=o&&a<=r&&u>=i&&u<=n&&p.push(t[g]);else{var m=Math.floor((c+d)/2);a=e[2*m],u=e[2*m+1],a>=o&&a<=r&&u>=i&&u<=n&&p.push(t[m]);var f=(l+1)%2;(0===l?o<=a:i<=u)&&(h.push(c),h.push(m-1),h.push(f)),(0===l?r>=a:n>=u)&&(h.push(m+1),h.push(d),h.push(f))}}return p}(this.ids,this.coords,t,e,o,i,this.nodeSize)},within:function(t,e,o){return function(t,e,o,i,r,n){for(var s=[0,t.length-1,0],u=[],h=r*r;s.length;){var p=s.pop(),l=s.pop(),d=s.pop();if(l-d<=n)for(var c=d;c<=l;c++)a(e[2*c],e[2*c+1],o,i)<=h&&u.push(t[c]);else{var g=Math.floor((d+l)/2),m=e[2*g],f=e[2*g+1];a(m,f,o,i)<=h&&u.push(t[g]);var v=(p+1)%2;(0===p?o-r<=m:i-r<=f)&&(s.push(d),s.push(g-1),s.push(v)),(0===p?o+r>=m:i+r>=f)&&(s.push(g+1),s.push(l),s.push(v))}}return u}(this.ids,this.coords,t,e,o,this.nodeSize)}},d.prototype={options:{minZoom:0,maxZoom:16,radius:40,extent:512,nodeSize:64,log:!1,reduce:null,initial:function(){return{}},map:function(t){return t}},load:function(t){var e=this.options.log;e&&console.time("total time");var o="prepare "+t.length+" points";e&&console.time(o),this.points=t;for(var i,r,n=[],s=0;s<t.length;s++)t[s].geometry&&n.push((i=s,void 0,{x:f((r=t[s].geometry.coordinates)[0]),y:v(r[1]),zoom:1/0,index:i,parentId:-1}));this.trees[this.options.maxZoom+1]=u(n,w,x,this.options.nodeSize,Float32Array),e&&console.timeEnd(o);for(var a=this.options.maxZoom;a>=this.options.minZoom;a--){var h=+Date.now();n=this._cluster(n,a),this.trees[a]=u(n,w,x,this.options.nodeSize,Float32Array),e&&console.log("z%d: %d clusters in %dms",a,n.length,+Date.now()-h)}return e&&console.timeEnd("total time"),this},getClusters:function(t,e){var o=((t[0]+180)%360+360)%360-180,i=Math.max(-90,Math.min(90,t[1])),r=180===t[2]?180:((t[2]+180)%360+360)%360-180,n=Math.max(-90,Math.min(90,t[3]));if(t[2]-t[0]>=360)o=-180,r=180;else if(o>r){var s=this.getClusters([o,i,180,n],e),a=this.getClusters([-180,i,r,n],e);return s.concat(a)}for(var u=this.trees[this._limitZoom(e)],h=u.range(f(o),v(n),f(r),v(i)),p=[],l=0;l<h.length;l++){var d=u.points[h[l]];p.push(d.numPoints?g(d):this.points[d.index])}return p},getChildren:function(t){var e=t>>5,o=t%32,i="No cluster with the specified id.",r=this.trees[o];if(!r)throw new Error(i);var n=r.points[e];if(!n)throw new Error(i);for(var s=this.options.radius/(this.options.extent*Math.pow(2,o-1)),a=r.within(n.x,n.y,s),u=[],h=0;h<a.length;h++){var p=r.points[a[h]];p.parentId===t&&u.push(p.numPoints?g(p):this.points[p.index])}if(0===u.length)throw new Error(i);return u},getLeaves:function(t,e,o){e=e||10,o=o||0;var i=[];return this._appendLeaves(i,t,e,o,0),i},getTile:function(t,e,o){var i=this.trees[this._limitZoom(t)],r=Math.pow(2,t),n=this.options.extent,s=this.options.radius/n,a=(o-s)/r,u=(o+1+s)/r,h={features:[]};return this._addTileFeatures(i.range((e-s)/r,a,(e+1+s)/r,u),i.points,e,o,r,h),0===e&&this._addTileFeatures(i.range(1-s/r,a,1,u),i.points,r,o,r,h),e===r-1&&this._addTileFeatures(i.range(0,a,s/r,u),i.points,-1,o,r,h),h.features.length?h:null},getClusterExpansionZoom:function(t){for(var e=t%32-1;e<this.options.maxZoom;){var o=this.getChildren(t);if(e++,1!==o.length)break;t=o[0].properties.cluster_id}return e},_appendLeaves:function(t,e,o,i,r){for(var n=this.getChildren(e),s=0;s<n.length;s++){var a=n[s].properties;if(a&&a.cluster?r+a.point_count<=i?r+=a.point_count:r=this._appendLeaves(t,a.cluster_id,o,i,r):r<i?r++:t.push(n[s]),t.length===o)break}return r},_addTileFeatures:function(t,e,o,i,r,n){for(var s=0;s<t.length;s++){var a=e[t[s]],u={type:1,geometry:[[Math.round(this.options.extent*(a.x*r-o)),Math.round(this.options.extent*(a.y*r-i))]],tags:a.numPoints?m(a):this.points[a.index].properties},h=a.numPoints?a.id:this.points[a.index].id;void 0!==h&&(u.id=h),n.features.push(u)}},_limitZoom:function(t){return Math.max(this.options.minZoom,Math.min(t,this.options.maxZoom+1))},_cluster:function(t,e){for(var o=[],i=this.options.radius/(this.options.extent*Math.pow(2,e)),r=0;r<t.length;r++){var n=t[r];if(!(n.zoom<=e)){n.zoom=e;var s=this.trees[e+1],a=s.within(n.x,n.y,i),u=n.numPoints||1,h=n.x*u,p=n.y*u,l=null;this.options.reduce&&(l=this.options.initial(),this._accumulate(l,n));for(var d=(r<<5)+(e+1),g=0;g<a.length;g++){var m=s.points[a[g]];if(!(m.zoom<=e)){m.zoom=e;var f=m.numPoints||1;h+=m.x*f,p+=m.y*f,u+=f,m.parentId=d,this.options.reduce&&this._accumulate(l,m)}}1===u?o.push(n):(n.parentId=d,o.push(c(h/u,p/u,d,u,l)))}}return o},_accumulate:function(t,e){var o=e.numPoints?e.properties:this.options.map(this.points[e.index].properties);this.options.reduce(t,o)}};var M=o(88623);const y=()=>{};function C(t){const{width:e,height:o,formData:i,hooks:r,queriesData:n}=t,{onError:s=y,setControlValue:a=y}=r,{bounds:u,geoJSON:h,hasCustomMetric:p,mapboxApiKey:l}=n[0].data,{clusteringRadius:c,globalOpacity:g,mapboxColor:m,mapboxStyle:f,pandasAggfunc:v,pointRadius:b,pointRadiusUnit:w,renderWhileDragging:x}=i,C=/^rgb\((\d{1,3}),\s*(\d{1,3}),\s*(\d{1,3})\)$/.exec(m);if(null===C)return s("Color field must be of form 'rgb(%d, %d, %d)'"),{};const _={maxZoom:M.DEFAULT_MAX_ZOOM,radius:c};p&&(_.initial=()=>({sum:0,squaredSum:0,min:1/0,max:-1/0}),_.map=t=>({sum:t.metric,squaredSum:t.metric**2,min:t.metric,max:t.metric}),_.reduce=(t,e)=>{t.sum+=e.sum,t.squaredSum+=e.squaredSum,t.min=Math.min(t.min,e.min),t.max=Math.max(t.max,e.max)});const S=new d(_);return S.load(h.features),{width:e,height:o,aggregatorName:v,bounds:u,clusterer:S,globalOpacity:g,hasCustomMetric:p,mapboxApiKey:l,mapStyle:f,onViewportChange(t){let{latitude:e,longitude:o,zoom:i}=t;a("viewport_longitude",o),a("viewport_latitude",e),a("viewport_zoom",i)},pointRadius:"Auto"===b?M.DEFAULT_POINT_RADIUS:b,pointRadiusUnit:w,renderWhileDragging:x,rgb:C}}}}]);
//# sourceMappingURL=3926ef13daefbca43225.chunk.js.map