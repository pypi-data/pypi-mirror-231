"use strict";(globalThis.webpackChunksuperset=globalThis.webpackChunksuperset||[]).push([[3197],{93197:(e,t,n)=>{n.d(t,{tR:()=>T,iZ:()=>R,iA:()=>N,ex:()=>y,ZP:()=>A});var l=n(5872),o=n.n(l),r=n(67294),i=n(2307),s=n(31929),a=n(51995),d=n(55867),u=n(68492),c=n(38703);const h=(e,t,n)=>{let l=!1;const o=t-e;return o>0&&o<=n&&(l=!0),l};class g{constructor(e,t,n){var l=this;this.tableRef=void 0,this.columnRef=void 0,this.setDerivedColumns=void 0,this.isDragging=void 0,this.resizable=void 0,this.reorderable=void 0,this.derivedColumns=void 0,this.RESIZE_INDICATOR_THRESHOLD=void 0,this.clearListeners=()=>{document.removeEventListener("mouseup",this.handleMouseup),this.initializeResizableColumns(!1,this.tableRef),this.initializeDragDropColumns(!1,this.tableRef)},this.setTableRef=e=>{this.tableRef=e},this.getColumnIndex=()=>{var e;let t=-1;const n=null==(e=this.columnRef)?void 0:e.parentNode;return n&&(t=Array.prototype.indexOf.call(n.children,this.columnRef)),t},this.handleColumnDragStart=e=>{var t;const n=null==e?void 0:e.currentTarget;n&&(this.columnRef=n),this.isDragging=!0;const l=this.getColumnIndex(),o={index:l,columnData:this.derivedColumns[l]};null==e||null==(t=e.dataTransfer)||t.setData(R,JSON.stringify(o))},this.handleDragDrop=e=>{var t;if(null==(t=e.dataTransfer)||null==t.getData?void 0:t.getData(R)){var n;e.preventDefault();const t=null==(n=e.currentTarget)?void 0:n.parentNode,l=Array.prototype.indexOf.call(t.children,e.currentTarget),o=this.getColumnIndex(),r=[...this.derivedColumns],i=r.slice(o,o+1);r.splice(o,1),r.splice(l,0,i[0]),this.derivedColumns=[...r],this.setDerivedColumns(r)}},this.allowDrop=e=>{e.preventDefault()},this.handleMouseDown=e=>{const t=null==e?void 0:e.currentTarget;t&&(this.columnRef=t,e&&h(e.offsetX,t.offsetWidth,this.RESIZE_INDICATOR_THRESHOLD)?(t.mouseDown=!0,t.oldX=e.x,t.oldWidth=t.offsetWidth,t.draggable=!1):this.reorderable&&(t.draggable=!0))},this.handleMouseMove=e=>{if(!0===this.resizable&&!this.isDragging){const t=e.currentTarget;e&&h(e.offsetX,t.offsetWidth,this.RESIZE_INDICATOR_THRESHOLD)?t.style.cursor="col-resize":t.style.cursor="default";const n=this.columnRef;if(null!=n&&n.mouseDown){let t=n.oldWidth;const l=e.x-n.oldX;n.oldWidth+(e.x-n.oldX)>0&&(t=n.oldWidth+l);const o=this.getColumnIndex();if(!Number.isNaN(o)){const e={...this.derivedColumns[o]};e.width=t,this.derivedColumns[o]=e,this.setDerivedColumns([...this.derivedColumns])}}}},this.handleMouseup=()=>{this.columnRef&&(this.columnRef.mouseDown=!1,this.columnRef.style.cursor="default",this.columnRef.draggable=!1),this.isDragging=!1},this.initializeResizableColumns=function(e,t){var n,o;void 0===e&&(e=!1),l.tableRef=t;const r=null==(n=l.tableRef)||null==(o=n.rows)?void 0:o[0];if(r){const{cells:t}=r,n=t.length;for(let o=0;o<n;o+=1){const n=t[o];!0===e?(l.resizable=!0,n.addEventListener("mousedown",l.handleMouseDown),n.addEventListener("mousemove",l.handleMouseMove,!0)):(l.resizable=!1,n.removeEventListener("mousedown",l.handleMouseDown),n.removeEventListener("mousemove",l.handleMouseMove,!0))}}},this.initializeDragDropColumns=function(e,t){var n,o;void 0===e&&(e=!1),l.tableRef=t;const r=null==(n=l.tableRef)||null==(o=n.rows)?void 0:o[0];if(r){const{cells:t}=r,n=t.length;for(let o=0;o<n;o+=1){const n=t[o];!0===e?(l.reorderable=!0,n.addEventListener("mousedown",l.handleMouseDown),n.addEventListener("dragover",l.allowDrop),n.addEventListener("dragstart",l.handleColumnDragStart),n.addEventListener("drop",l.handleDragDrop)):(l.reorderable=!1,n.draggable=!1,n.removeEventListener("mousedown",l.handleMouseDown),n.removeEventListener("dragover",l.allowDrop),n.removeEventListener("dragstart",l.handleColumnDragStart),n.removeEventListener("drop",l.handleDragDrop))}}},this.setDerivedColumns=n,this.tableRef=e,this.isDragging=!1,this.RESIZE_INDICATOR_THRESHOLD=8,this.resizable=!1,this.reorderable=!1,this.derivedColumns=[...t],document.addEventListener("mouseup",this.handleMouseup)}}var f=n(94184),p=n.n(f),v=n(99612),m=n(74061),b=n(32103),w=n(11965);const D=(0,a.iK)("div")((e=>{let{theme:t,height:n}=e;return`\n  white-space: nowrap;\n  overflow: hidden;\n  text-overflow: ellipsis;\n  padding-left: ${2*t.gridUnit}px;\n  padding-right: ${t.gridUnit}px;\n  border-bottom: 1px solid ${t.colors.grayscale.light3};\n  transition: background 0.3s;\n  line-height: ${n}px;\n  box-sizing: border-box;\n`})),E=(0,a.iK)(i.Z)((e=>{let{theme:t}=e;return`\n    th.ant-table-cell {\n      font-weight: ${t.typography.weights.bold};\n      color: ${t.colors.grayscale.dark1};\n      user-select: none;\n      white-space: nowrap;\n      overflow: hidden;\n      text-overflow: ellipsis;\n    }\n\n    .ant-pagination-item-active {\n      border-color: ${t.colors.primary.base};\n      }\n    }\n    .ant-table.ant-table-small {\n      font-size: ${t.typography.sizes.s}px;\n    }\n`})),R="superset/table-column";var C,T,y;!function(e){e.DISABLED="disabled",e.SINGLE="single",e.MULTI="multi"}(C||(C={})),function(e){e.PAGINATE="paginate",e.SORT="sort",e.FILTER="filter"}(T||(T={})),function(e){e.SMALL="small",e.MIDDLE="middle"}(y||(y={}));const L=[],S=(0,a.iK)(i.Z)((e=>{let{theme:t,height:n}=e;return`\n    .ant-table-body {\n      overflow: auto;\n      height: ${n?`${n}px`:void 0};\n    }\n\n    th.ant-table-cell {\n      font-weight: ${t.typography.weights.bold};\n      color: ${t.colors.grayscale.dark1};\n      user-select: none;\n      white-space: nowrap;\n      overflow: hidden;\n      text-overflow: ellipsis;\n    }\n\n    .ant-table-tbody > tr > td {\n      user-select: none;\n      white-space: nowrap;\n      overflow: hidden;\n      text-overflow: ellipsis;\n      border-bottom: 1px solid ${t.colors.grayscale.light3};\n    }\n\n    .ant-pagination-item-active {\n      border-color: ${t.colors.primary.base};\n    }\n\n    .ant-table.ant-table-small {\n      font-size: ${t.typography.sizes.s}px;\n    }\n  `})),x=(0,a.iK)((e=>{var t;const{columns:n,pagination:l,onChange:i,height:s,scroll:d,size:u,allowHTML:c=!1}=e,[h,g]=(0,r.useState)(0),f=(0,r.useCallback)((e=>{g(e)}),[]),{ref:R}=(0,v.NB)({onResize:f}),C=(0,a.Fg)(),L=37*(null==C?void 0:C.gridUnit)||150,S=n.filter((e=>{let{width:t}=e;return!t})).length;let x=0;null==n||n.forEach((e=>{e.width&&(x+=e.width)}));let I=0;const z=Math.max(Math.floor((h-x)/S),50),M=null!=(t=null==n||null==n.map?void 0:n.map((e=>{const t={...e};return e.width||(t.width=z),I+=t.width,t})))?t:[];if(I<h){const e=M[M.length-1];e.width=e.width+Math.floor(h-I)}const N=(0,r.useRef)(),[A]=(0,r.useState)((()=>{const e={};return Object.defineProperty(e,"scrollLeft",{get:()=>{var e,t;return N.current?null==(e=N.current)||null==(t=e.state)?void 0:t.scrollLeft:null},set:e=>{N.current&&N.current.scrollTo({scrollLeft:e})}}),e})),Z=()=>{var e;null==(e=N.current)||e.resetAfterIndices({columnIndex:0,shouldForceUpdate:!0})};(0,r.useEffect)((()=>Z),[h,n,u]);const O={...l,onChange:(e,t)=>{var n;null==(n=N.current)||null==n.scrollTo||n.scrollTo({scrollTop:0}),null==i||i({...l,current:e,pageSize:t},{},{},{action:T.PAGINATE,currentDataSource:[]})}};return(0,w.tZ)("div",{ref:R},(0,w.tZ)(E,o()({},e,{sticky:!1,className:"virtual-table",columns:M,components:{body:(e,t)=>{let{ref:n,onScroll:l}=t;n.current=A;const o=u===y.MIDDLE?47:39;return(0,w.tZ)(m.cd,{ref:N,className:"virtual-grid",columnCount:M.length,columnWidth:e=>{const{width:t=L}=M[e];return t},height:s||d.y,rowCount:e.length,rowHeight:()=>o,width:h,onScroll:e=>{let{scrollLeft:t}=e;l({scrollLeft:t})}},(t=>{var n,l;let{columnIndex:r,rowIndex:i,style:s}=t;const a=null==e?void 0:e[i];let d=null==a?void 0:a[null==M||null==(n=M[r])?void 0:n.dataIndex];const u=null==(l=M[r])?void 0:l.render;return"function"==typeof u&&(d=u(d,a,i)),c&&"string"==typeof d&&(d=(0,b.Ul)(d)),(0,w.tZ)(D,{className:p()("virtual-table-cell",{"virtual-table-cell-last":r===M.length-1}),style:s,title:"string"==typeof d?d:void 0,theme:C,height:o},d)}))}},pagination:!!l&&O})))}))((e=>{let{theme:t}=e;return`\n  .virtual-table .ant-table-container:before,\n  .virtual-table .ant-table-container:after {\n    display: none;\n  }\n  .virtual-table-cell {\n    box-sizing: border-box;\n    padding: ${4*t.gridUnit}px;\n    white-space: nowrap;\n    overflow: hidden;\n    text-overflow: ellipsis;\n  }\n`})),I={filterTitle:(0,d.t)("Filter menu"),filterConfirm:(0,d.t)("OK"),filterReset:(0,d.t)("Reset"),filterEmptyText:(0,d.t)("No filters"),filterCheckall:(0,d.t)("Select all items"),filterSearchPlaceholder:(0,d.t)("Search in filters"),emptyText:(0,d.t)("No data"),selectAll:(0,d.t)("Select current page"),selectInvert:(0,d.t)("Invert current page"),selectNone:(0,d.t)("Clear all data"),selectionAll:(0,d.t)("Select all data"),sortTitle:(0,d.t)("Sort"),expand:(0,d.t)("Expand row"),collapse:(0,d.t)("Collapse row"),triggerDesc:(0,d.t)("Click to sort descending"),triggerAsc:(0,d.t)("Click to sort ascending"),cancelSort:(0,d.t)("Click to cancel sorting")},z={},M=()=>{};function N(e){const{data:t,bordered:n,columns:l,selectedRows:i=L,handleRowSelection:d,size:h=y.SMALL,selectionType:f=C.DISABLED,sticky:p=!0,loading:v=!1,resizable:m=!1,reorderable:b=!1,usePagination:D=!0,defaultPageSize:E=15,pageSizeOptions:R=["5","15","25","50","100"],hideData:T=!1,emptyComponent:N,locale:A,height:Z,virtualize:O=!1,onChange:k=M,recordCount:$,onRow:H,allowHTML:P=!1}=e,U=(0,r.useRef)(null),[W,_]=(0,r.useState)(l),[B,F]=(0,r.useState)(E),[X,K]=(0,r.useState)({...I}),[G,j]=(0,r.useState)(i),J=(0,r.useRef)(null),q=z[f],Q={type:q,selectedRowKeys:G,onChange:e=>{j(e),null==d||d(e)}};(0,r.useEffect)((()=>{!0===b&&u.Z.warn('EXPERIMENTAL FEATURE ENABLED: The "reorderable" prop of Table is experimental and NOT recommended for use in production deployments.'),!0===m&&u.Z.warn('EXPERIMENTAL FEATURE ENABLED: The "resizable" prop of Table is experimental and NOT recommended for use in production deployments.')}),[b,m]),(0,r.useEffect)((()=>{let e;e=A?{...I,...A}:{...I},K(e)}),[A]),(0,r.useEffect)((()=>_(l)),[l]),(0,r.useEffect)((()=>{var e,t;J.current&&(null==(t=J.current)||t.clearListeners());const n=null==(e=U.current)?void 0:e.getElementsByTagName("table")[0];var l,o;n&&(J.current=new g(n,W,_),b&&(null==J||null==(l=J.current)||l.initializeDragDropColumns(b,n)),m&&(null==J||null==(o=J.current)||o.initializeResizableColumns(m,n)));return()=>{var e;null==J||null==(e=J.current)||null==e.clearListeners||e.clearListeners()}}),[U,b,m,O,J]);const V=(0,a.Fg)(),Y=!!D&&{hideOnSinglePage:!0,pageSize:B,pageSizeOptions:R,onShowSizeChange:(e,t)=>F(t)};Y&&$&&(Y.total=$);let ee=Z;ee&&(ee-=68,D&&$&&$>B&&(ee-=40));const te={loading:{spinning:null!=v&&v,indicator:(0,w.tZ)(c.Z,null)},hasData:!T&&t,columns:W,dataSource:T?void 0:t,size:h,pagination:Y,locale:X,showSorterTooltip:!1,onChange:k,onRow:H,theme:V,height:ee,bordered:n};return(0,w.tZ)(s.default,{renderEmpty:()=>null!=N?N:(0,w.tZ)("div",null,X.emptyText)},(0,w.tZ)("div",{ref:U},!O&&(0,w.tZ)(S,o()({},te,{rowSelection:q?Q:void 0,sticky:p})),O&&(0,w.tZ)(x,o()({},te,{scroll:{y:300,x:"100vw",...!1},allowHTML:P}))))}z[C.MULTI]="checkbox",z[C.SINGLE]="radio",z[C.DISABLED]=null;const A=N}}]);
//# sourceMappingURL=3197.1cd8561c0296667b196a.entry.js.map