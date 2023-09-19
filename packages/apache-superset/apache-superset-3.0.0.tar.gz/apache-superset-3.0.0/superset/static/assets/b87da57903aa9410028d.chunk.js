"use strict";(globalThis.webpackChunksuperset=globalThis.webpackChunksuperset||[]).push([[137],{36665:(t,e,o)=>{o.d(e,{Z:()=>u});var a=o(78580),r=o.n(a),s=o(67294),i=o(45697),n=o.n(i),l=o(51995),p=o(67190),h=o(11965);const c=l.iK.div`
  ${t=>{let{theme:e}=t;return`\n    font-size: ${e.typography.sizes.s}px;\n    position: absolute;\n    background: ${e.colors.grayscale.light5};\n    box-shadow: 0 0 ${e.gridUnit}px ${e.colors.grayscale.light2};\n    margin: ${6*e.gridUnit}px;\n    padding: ${3*e.gridUnit}px ${5*e.gridUnit}px;\n    outline: none;\n    overflow-y: scroll;\n    max-height: 200px;\n\n    & ul {\n      list-style: none;\n      padding-left: 0;\n      margin: 0;\n\n      & li a {\n        color: ${e.colors.grayscale.base};\n        text-decoration: none;\n\n        & span {\n          margin-right: ${3*e.gridUnit}px;\n        }\n      }\n    }\n  `}}
`,d=" - ",g={categories:n().object,forceCategorical:n().bool,format:n().string,position:n().oneOf([null,"tl","tr","bl","br"]),showSingleCategory:n().func,toggleCategory:n().func};class u extends s.PureComponent{format(t){if(!this.props.format||this.props.forceCategorical)return t;const e=parseFloat(t);return(0,p.uf)(this.props.format,e)}formatCategoryLabel(t){if(!this.props.format)return t;if(r()(t).call(t,d)){const e=t.split(d);return this.format(e[0])+d+this.format(e[1])}return this.format(t)}render(){if(0===Object.keys(this.props.categories).length||null===this.props.position)return null;const t=Object.entries(this.props.categories).map((t=>{let[e,o]=t;const a={color:`rgba(${o.color.join(", ")})`},r=o.enabled?"◼":"◻";return(0,h.tZ)("li",{key:e},(0,h.tZ)("a",{href:"#",onClick:()=>this.props.toggleCategory(e),onDoubleClick:()=>this.props.showSingleCategory(e)},(0,h.tZ)("span",{style:a},r)," ",this.formatCategoryLabel(e)))})),e={position:"absolute",["t"===this.props.position.charAt(0)?"top":"bottom"]:"0px",["r"===this.props.position.charAt(1)?"right":"left"]:"10px"};return(0,h.tZ)(c,{style:e},(0,h.tZ)("ul",null,t))}}u.propTypes=g,u.defaultProps={categories:{},forceCategorical:!1,format:null,position:"tr",showSingleCategory:()=>{},toggleCategory:()=>{}}},14228:(t,e,o)=>{o.r(e),o.d(e,{default:()=>c,getLayer:()=>h});var a=o(62112),r=(o(67294),o(52154)),s=o(21207),i=o(26331),n=o(1740),l=o(11965);function p(t){return t.object.extraProps&&(0,l.tZ)("div",{className:"deckgl-tooltip"},Object.keys(t.object.extraProps).map(((e,o)=>(0,l.tZ)(n.Z,{key:`prop-${o}`,label:`${e}: `,value:`${t.object.extraProps[e]}`}))))}function h(t,e,o,i){const n=t,l=n.color_picker,h=[l.r,l.g,l.b,255*l.a];let c=e.data.features.map((t=>({...t,path:t.path,width:n.line_width,color:h})));return n.js_data_mutator&&(c=(0,s.Z)(n.js_data_mutator)(c)),new a.Z({id:`path-layer-${n.slice_id}`,getColor:t=>t.color,getPath:t=>t.path,getWidth:t=>t.width,data:c,rounded:!0,widthScale:1,...(0,r.N)(n,i,p)})}const c=(0,i.G)(h,(function(t){let e=[];return t.forEach((t=>{e=e.concat(t.path)})),e}))},26331:(t,e,o)=>{o.d(e,{B:()=>_,G:()=>C});var a=o(18446),r=o.n(a),s=o(67294),i=o(84502),n=o(45697),l=o.n(n),p=o(28062),h=o(85531),c=o(36665),d=o(64106),g=o(66911),u=o(21207),m=o(40461),f=o(11965);const{getScale:y}=p,b={datasource:l().object.isRequired,formData:l().object.isRequired,getLayer:l().func.isRequired,getPoints:l().func.isRequired,height:l().number.isRequired,mapboxApiKey:l().string.isRequired,onAddFilter:l().func,payload:l().object.isRequired,setControlValue:l().func.isRequired,viewport:l().object.isRequired,width:l().number.isRequired};class w extends s.PureComponent{constructor(t){super(t),this.containerRef=s.createRef(),this.setTooltip=t=>{const{current:e}=this.containerRef;e&&e.setTooltip(t)},this.state=this.getStateFromProps(t),this.getLayers=this.getLayers.bind(this),this.onValuesChange=this.onValuesChange.bind(this),this.toggleCategory=this.toggleCategory.bind(this),this.showSingleCategory=this.showSingleCategory.bind(this)}UNSAFE_componentWillReceiveProps(t){t.payload.form_data!==this.state.formData&&this.setState({...this.getStateFromProps(t)})}onValuesChange(t){this.setState({values:Array.isArray(t)?t:[t,t+this.state.getStep(t)]})}getStateFromProps(t,e){const o=t.payload.data.features||[],a=o.map((t=>t.__timestamp)),r=function(t,e){const o=t.color_picker||{r:0,g:0,b:0,a:1},a=[o.r,o.g,o.b,255*o.a],r=y(t.color_scheme),s={};return e.forEach((e=>{if(null!=e.cat_color&&!s.hasOwnProperty(e.cat_color)){let i;i=t.dimension?(0,d.hexToRGB)(r(e.cat_color,t.sliceId),255*o.a):a,s[e.cat_color]={color:i,enabled:!0}}})),s}(t.formData,o);if(e&&t.payload.form_data===e.formData)return{...e,categories:r};const s=t.payload.form_data.time_grain_sqla||t.payload.form_data.granularity||"P1D",{start:i,end:n,getStep:l,values:p,disabled:h}=(0,g.g)(a,s),{width:c,height:u,formData:f}=t;let{viewport:b}=t;return f.autozoom&&(b=(0,m.Z)(b,{width:c,height:u,points:t.getPoints(o)})),b.zoom<0&&(b.zoom=0),{start:i,end:n,getStep:l,values:p,disabled:h,viewport:b,selected:[],lastClick:0,formData:t.payload.form_data,categories:r}}getLayers(t){const{getLayer:e,payload:o,formData:a,onAddFilter:r}=this.props;let s=o.data.features?[...o.data.features]:[];s=this.addColor(s,a),a.js_data_mutator&&(s=(0,u.Z)(a.js_data_mutator)(s)),s=t[0]===t[1]||t[1]===this.end?s.filter((e=>e.__timestamp>=t[0]&&e.__timestamp<=t[1])):s.filter((e=>e.__timestamp>=t[0]&&e.__timestamp<t[1]));const i=this.state.categories;return a.dimension&&(s=s.filter((t=>i[t.cat_color]&&i[t.cat_color].enabled))),[e(a,{...o,data:{...o.data,features:s}},r,this.setTooltip,this.props.datasource)]}addColor(t,e){const o=e.color_picker||{r:0,g:0,b:0,a:1},a=y(e.color_scheme);return t.map((t=>{let r;return e.dimension?(r=(0,d.hexToRGB)(a(t.cat_color,e.sliceId),255*o.a),{...t,color:r}):t}))}toggleCategory(t){const e=this.state.categories[t],o={...this.state.categories,[t]:{...e,enabled:!e.enabled}};Object.values(o).every((t=>!t.enabled))&&Object.values(o).forEach((t=>{t.enabled=!0})),this.setState({categories:o})}showSingleCategory(t){const e={...this.state.categories};Object.values(e).forEach((t=>{t.enabled=!1})),e[t].enabled=!0,this.setState({categories:e})}render(){return(0,f.tZ)("div",{style:{position:"relative"}},(0,f.tZ)(h.Z,{ref:this.containerRef,getLayers:this.getLayers,start:this.state.start,end:this.state.end,getStep:this.state.getStep,values:this.state.values,disabled:this.state.disabled,viewport:this.state.viewport,mapboxApiAccessToken:this.props.mapboxApiKey,mapStyle:this.props.formData.mapbox_style,setControlValue:this.props.setControlValue,width:this.props.width,height:this.props.height},(0,f.tZ)(c.Z,{forceCategorical:!0,categories:this.state.categories,format:this.props.formData.legend_format,position:this.props.formData.legend_position,showSingleCategory:this.showSingleCategory,toggleCategory:this.toggleCategory})))}}function C(t,e){class o extends s.PureComponent{constructor(t){super(t),this.containerRef=s.createRef(),this.setTooltip=t=>{const{current:e}=this.containerRef;e&&(null==e||e.setTooltip(t))};const{width:o,height:a,formData:r}=t;let{viewport:i}=t;r.autozoom&&(i=(0,m.Z)(i,{width:o,height:a,points:e(t.payload.data.features)})),this.state={viewport:i,layer:this.computeLayer(t)},this.onViewportChange=this.onViewportChange.bind(this)}UNSAFE_componentWillReceiveProps(t){const e={...t.formData,viewport:null},o={...this.props.formData,viewport:null};r()(e,o)&&t.payload===this.props.payload||this.setState({layer:this.computeLayer(t)})}onViewportChange(t){this.setState({viewport:t})}computeLayer(e){const{formData:o,payload:a,onAddFilter:r}=e;return t(o,a,r,this.setTooltip)}render(){const{formData:t,payload:e,setControlValue:o,height:a,width:r}=this.props,{layer:s,viewport:n}=this.state;return(0,f.tZ)(i.F,{ref:this.containerRef,mapboxApiAccessToken:e.data.mapboxApiKey,viewport:n,layers:[s],mapStyle:t.mapbox_style,setControlValue:o,width:r,height:a,onViewportChange:this.onViewportChange})}}return o}function _(t,e){return function(o){const{datasource:a,formData:r,height:s,payload:i,setControlValue:n,viewport:l,width:p}=o;return(0,f.tZ)(w,{datasource:a,formData:r,mapboxApiKey:i.data.mapboxApiKey,setControlValue:n,viewport:l,getLayer:t,payload:i,getPoints:e,width:p,height:s})}}w.propTypes=b}}]);
//# sourceMappingURL=b87da57903aa9410028d.chunk.js.map