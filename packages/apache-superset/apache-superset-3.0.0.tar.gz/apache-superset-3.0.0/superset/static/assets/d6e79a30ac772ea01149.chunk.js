"use strict";(globalThis.webpackChunksuperset=globalThis.webpackChunksuperset||[]).push([[9563],{29848:(e,t,l)=>{l.d(t,{Z:()=>c}),l(67294);var r=l(51995),a=l(58593),o=l(70163),n=l(11965);const s=r.iK.span`
  white-space: nowrap;
  min-width: 100px;
  svg,
  i {
    margin-right: 8px;

    &:hover {
      path {
        fill: ${e=>{let{theme:t}=e;return t.colors.primary.base}};
      }
    }
  }
`,i=r.iK.span`
  color: ${e=>{let{theme:t}=e;return t.colors.grayscale.base}};
`;function c(e){let{actions:t}=e;return(0,n.tZ)(s,{className:"actions"},t.map(((e,t)=>{const l=o.Z[e.icon];return e.tooltip?(0,n.tZ)(a.u,{id:`${e.label}-tooltip`,title:e.tooltip,placement:e.placement,key:t},(0,n.tZ)(i,{role:"button",tabIndex:0,className:"action-button",onClick:e.onClick},(0,n.tZ)(l,null))):(0,n.tZ)(i,{role:"button",tabIndex:0,className:"action-button",onClick:e.onClick,key:t},(0,n.tZ)(l,null))})))}},94222:(e,t,l)=>{l.d(t,{Z:()=>u});var r=l(51995),a=l(55867),o=(l(67294),l(58593)),n=l(70163),s=l(90335),i=l(11965);function c(e,t,l){switch(e){case s.Z.Working:return l.colors.primary.base;case s.Z.Error:return l.colors.error.base;case s.Z.Success:return t?l.colors.success.base:l.colors.alert.base;case s.Z.Noop:return l.colors.success.base;case s.Z.Grace:return l.colors.alert.base;default:return l.colors.grayscale.base}}function u(e){let{state:t,isReportEnabled:l=!1}=e;const u=(0,r.Fg)(),d={icon:n.Z.Check,label:"",status:""};switch(t){case s.Z.Success:d.icon=l?n.Z.Check:n.Z.AlertSolidSmall,d.label=l?(0,a.t)("Report sent"):(0,a.t)("Alert triggered, notification sent"),d.status=s.Z.Success;break;case s.Z.Working:d.icon=n.Z.Running,d.label=l?(0,a.t)("Report sending"):(0,a.t)("Alert running"),d.status=s.Z.Working;break;case s.Z.Error:d.icon=n.Z.XSmall,d.label=l?(0,a.t)("Report failed"):(0,a.t)("Alert failed"),d.status=s.Z.Error;break;case s.Z.Noop:d.icon=n.Z.Check,d.label=(0,a.t)("Nothing triggered"),d.status=s.Z.Noop;break;case s.Z.Grace:d.icon=n.Z.AlertSolidSmall,d.label=(0,a.t)("Alert Triggered, In Grace Period"),d.status=s.Z.Grace;break;default:d.icon=n.Z.Check,d.label=(0,a.t)("Nothing triggered"),d.status=s.Z.Noop}const p=d.icon;return(0,i.tZ)(o.u,{title:d.label,placement:"bottomLeft"},(0,i.tZ)(p,{iconColor:c(d.status,l,u)}))}},90335:(e,t,l)=>{var r,a;l.d(t,{Z:()=>r,u:()=>a}),function(e){e.Success="Success",e.Working="Working",e.Error="Error",e.Noop="Not triggered",e.Grace="On Grace"}(r||(r={})),function(e){e.Email="Email",e.Slack="Slack"}(a||(a={}))},32635:(e,t,l)=>{l.r(t),l.d(t,{default:()=>K});var r=l(78580),a=l.n(r),o=l(67294),n=l(16550),s=l(75049),i=l(55867),c=l(22102),u=l(51995),d=l(31069),p=l(30381),m=l.n(p),b=l(29848),g=l(34581),Z=l(58593),h=l(18782),k=l(86074),y=l(73192),f=l(27600),w=l(14114),S=l(94222),v=l(11965),C=l(70163),E=l(90335);const $=e=>v.iv`
  color: ${e.colors.grayscale.light1};
  margin-right: ${2*e.gridUnit}px;
`;function x(e){let{type:t}=e;const l={icon:null,label:""};switch(t){case E.u.Email:l.icon=(0,v.tZ)(C.Z.Email,{css:$}),l.label=E.u.Email;break;case E.u.Slack:l.icon=(0,v.tZ)(C.Z.Slack,{css:$}),l.label=E.u.Slack;break;default:l.icon=null,l.label=""}return l.icon?(0,v.tZ)(Z.u,{title:l.label,placement:"bottom"},l.icon):null}var _=l(19259),A=l(17198);m().updateLocale("en",{calendar:{lastDay:"[Yesterday at] LTS",sameDay:"[Today at] LTS",nextDay:"[Tomorrow at] LTS",lastWeek:"[last] dddd [at] LTS",nextWeek:"dddd [at] LTS",sameElse:"L"}});const N=u.iK.span`
  color: ${e=>{let{theme:t}=e;return t.colors.grayscale.base}};
`,T=(0,u.iK)(C.Z.Refresh)`
  color: ${e=>{let{theme:t}=e;return t.colors.primary.base}};
  width: auto;
  height: ${e=>{let{theme:t}=e;return 5*t.gridUnit}}px;
  position: relative;
  top: ${e=>{let{theme:t}=e;return t.gridUnit}}px;
  left: ${e=>{let{theme:t}=e;return t.gridUnit}}px;
  cursor: pointer;
`,z=e=>{let{updatedAt:t,update:l}=e;const[r,a]=(0,o.useState)(m()(t));return(0,o.useEffect)((()=>{a((()=>m()(t)));const e=setInterval((()=>{a((()=>m()(t)))}),6e4);return()=>clearInterval(e)}),[t]),(0,v.tZ)(N,null,(0,i.t)("Last Updated %s",r.isValid()?r.calendar():"--"),l&&(0,v.tZ)(T,{onClick:l}))};var L=l(34858),R=l(40768),H=l(22318),D=l(20095);const W=(0,s.I)(),G={[E.Z.Success]:(0,i.t)("Success"),[E.Z.Working]:(0,i.t)("Working"),[E.Z.Error]:(0,i.t)("Error"),[E.Z.Noop]:(0,i.t)("Not triggered"),[E.Z.Grace]:(0,i.t)("On Grace")},B=(0,c.Z)({requestType:"rison",method:"DELETE",endpoint:"/api/v1/report/"}),I=u.iK.div`
  width: 100%;
  padding: 0 ${e=>{let{theme:t}=e;return 4*t.gridUnit}}px
    ${e=>{let{theme:t}=e;return 3*t.gridUnit}}px;
  background-color: ${e=>{let{theme:t}=e;return t.colors.grayscale.light5}};
`,U=u.iK.div`
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: center;
  > *:first-child {
    margin-right: ${e=>{let{theme:t}=e;return t.gridUnit}}px;
  }
`,M=W.get("alertsreports.header.icon"),K=(0,w.ZP)((function(e){let{addDangerToast:t,isReportEnabled:l=!1,user:r,addSuccessToast:s}=e;const c=l?(0,i.t)("report"):(0,i.t)("alert"),u=l?(0,i.t)("reports"):(0,i.t)("alerts"),p=l?"Reports":"Alerts",w=(0,o.useMemo)((()=>[{id:"type",operator:h.p.equals,value:l?"Report":"Alert"}]),[l]),{state:{loading:C,resourceCount:$,resourceCollection:N,bulkSelectEnabled:T,lastFetched:W},hasPerm:K,fetchData:F,setResourceCollection:O,refreshData:P,toggleBulkSelect:q}=(0,L.Yi)("report",(0,i.t)("reports"),t,!0,void 0,w),{updateResource:V}=(0,L.LE)("report",(0,i.t)("reports"),t),[Y,j]=(0,o.useState)(!1),[X,J]=(0,o.useState)(null),[Q,ee]=(0,o.useState)(null);function te(e){J(e),j(!0)}const le=K("can_write"),re=K("can_write"),ae=K("can_write");(0,o.useEffect)((()=>{T&&re&&q()}),[l]);const oe=[{id:"name",desc:!0}],ne=(0,o.useCallback)(((e,t)=>{if(null!=e&&e.id){const l=e.id,r=[...N];O(r.map((l=>(null==l?void 0:l.id)===e.id?{...l,active:t}:l))),V(l,{active:t},!1,!1).then().catch((()=>O(r)))}}),[N,O,V]),se=(0,o.useMemo)((()=>[{Cell:e=>{let{row:{original:{last_state:t}}}=e;return(0,v.tZ)(S.Z,{state:t,isReportEnabled:l})},accessor:"last_state",size:"xs",disableSortBy:!0},{Cell:e=>{let{row:{original:{last_eval_dttm:t}}}=e;return t?m().utc(t).local().format(f.v2):""},accessor:"last_eval_dttm",Header:(0,i.t)("Last run"),size:"lg"},{accessor:"name",Header:(0,i.t)("Name"),size:"xl"},{Header:(0,i.t)("Schedule"),accessor:"crontab_humanized",size:"xl",Cell:e=>{let{row:{original:{crontab_humanized:t="",timezone:l}}}=e;return(0,v.tZ)(Z.u,{title:`${t} (${l})`,placement:"topLeft"},(0,v.tZ)("span",null,`${t} (${l})`))}},{Cell:e=>{let{row:{original:{recipients:t}}}=e;return t.map((e=>(0,v.tZ)(x,{key:e.id,type:e.type})))},accessor:"recipients",Header:(0,i.t)("Notification method"),disableSortBy:!0,size:"xl"},{Cell:e=>{let{row:{original:{created_by:t}}}=e;return t?`${t.first_name} ${t.last_name}`:""},Header:(0,i.t)("Created by"),id:"created_by",disableSortBy:!0,size:"xl"},{Cell:e=>{let{row:{original:{owners:t=[]}}}=e;return(0,v.tZ)(g.Z,{users:t})},Header:(0,i.t)("Owners"),id:"owners",disableSortBy:!0,size:"xl"},{Cell:e=>{let{row:{original:{changed_on_delta_humanized:t}}}=e;return(0,v.tZ)("span",{className:"no-wrap"},t)},Header:(0,i.t)("Modified"),accessor:"changed_on_delta_humanized",size:"xl"},{Cell:e=>{var t;let{row:{original:l}}=e;const o=a()(t=l.owners.map((e=>e.id))).call(t,r.userId)||(0,H.i5)(r);return(0,v.tZ)(y.r,{disabled:!o,checked:l.active,onClick:e=>ne(l,e),size:"small"})},Header:(0,i.t)("Active"),accessor:"active",id:"active",size:"xl"},{Cell:e=>{var t;let{row:{original:l}}=e;const o=(0,n.k6)(),s=a()(t=l.owners.map((e=>e.id))).call(t,r.userId)||(0,H.i5)(r),c=[le?{label:"execution-log-action",tooltip:(0,i.t)("Execution log"),placement:"bottom",icon:"Note",onClick:()=>o.push(`/${l.type.toLowerCase()}/${l.id}/log`)}:null,le?{label:s?"edit-action":"preview-action",tooltip:s?(0,i.t)("Edit"):(0,i.t)("View"),placement:"bottom",icon:s?"Edit":"Binoculars",onClick:()=>te(l)}:null,s&&re?{label:"delete-action",tooltip:(0,i.t)("Delete"),placement:"bottom",icon:"Trash",onClick:()=>ee(l)}:null].filter((e=>null!==e));return(0,v.tZ)(b.Z,{actions:c})},Header:(0,i.t)("Actions"),id:"actions",hidden:!le&&!re,disableSortBy:!0,size:"xl"}]),[re,le,l,ne]),ie=[];ae&&ie.push({name:(0,v.tZ)(o.Fragment,null,(0,v.tZ)("i",{className:"fa fa-plus"})," ",c),buttonStyle:"primary",onClick:()=>{te(null)}}),re&&ie.push({name:(0,i.t)("Bulk select"),onClick:q,buttonStyle:"secondary","data-test":"bulk-select-toggle"});const ce={title:(0,i.t)("No %s yet",u),image:"filter-results.svg",buttonAction:()=>te(null),buttonText:ae?(0,v.tZ)(o.Fragment,null,(0,v.tZ)("i",{className:"fa fa-plus"})," ",c," "):null},ue=(0,o.useMemo)((()=>[{Header:(0,i.t)("Owner"),key:"owner",id:"owners",input:"select",operator:h.p.relationManyMany,unfilteredLabel:(0,i.t)("All"),fetchSelects:(0,R.tm)("report","owners",(0,R.v$)((e=>(0,i.t)("An error occurred while fetching owners values: %s",e))),r),paginate:!0},{Header:(0,i.t)("Created by"),key:"created_by",id:"created_by",input:"select",operator:h.p.relationOneMany,unfilteredLabel:"All",fetchSelects:(0,R.tm)("report","created_by",(0,R.v$)((e=>(0,i.t)("An error occurred while fetching created by values: %s",e))),r),paginate:!0},{Header:(0,i.t)("Status"),key:"status",id:"last_state",input:"select",operator:h.p.equals,unfilteredLabel:"Any",selects:[{label:G[E.Z.Success],value:E.Z.Success},{label:G[E.Z.Working],value:E.Z.Working},{label:G[E.Z.Error],value:E.Z.Error},{label:G[E.Z.Noop],value:E.Z.Noop},{label:G[E.Z.Grace],value:E.Z.Grace}]},{Header:(0,i.t)("Search"),key:"search",id:"name",input:"search",operator:h.p.contains}]),[]),de=M?(0,v.tZ)(U,null,(0,v.tZ)("div",null,(0,i.t)("Alerts & reports")),(0,v.tZ)(M,null)):(0,i.t)("Alerts & reports");return(0,v.tZ)(o.Fragment,null,(0,v.tZ)(k.Z,{activeChild:p,name:de,tabs:[{name:"Alerts",label:(0,i.t)("Alerts"),url:"/alert/list/",usesRouter:!0,"data-test":"alert-list"},{name:"Reports",label:(0,i.t)("Reports"),url:"/report/list/",usesRouter:!0,"data-test":"report-list"}],buttons:ie},(0,v.tZ)(I,null,(0,v.tZ)(z,{updatedAt:W,update:()=>P()}))),(0,v.tZ)(D.ZP,{alert:X,addDangerToast:t,layer:X,onHide:()=>{j(!1),J(null),P()},show:Y,isReport:l,key:(null==X?void 0:X.id)||`${(new Date).getTime()}`}),Q&&(0,v.tZ)(A.Z,{description:(0,i.t)("This action will permanently delete %s.",Q.name),onConfirm:()=>{Q&&(e=>{let{id:l,name:r}=e;d.Z.delete({endpoint:`/api/v1/report/${l}`}).then((()=>{P(),ee(null),s((0,i.t)("Deleted: %s",r))}),(0,R.v$)((e=>t((0,i.t)("There was an issue deleting %s: %s",r,e)))))})(Q)},onHide:()=>ee(null),open:!0,title:(0,i.t)("Delete %s?",c)}),(0,v.tZ)(_.Z,{title:(0,i.t)("Please confirm"),description:(0,i.t)("Are you sure you want to delete the selected %s?",u),onConfirm:async e=>{try{const{message:t}=await B(e.map((e=>{let{id:t}=e;return t})));P(),s(t)}catch(e){(0,R.v$)((e=>t((0,i.t)("There was an issue deleting the selected %s: %s",u,e))))(e)}}},(e=>{const t=re?[{key:"delete",name:(0,i.t)("Delete"),onSelect:e,type:"danger"}]:[];return(0,v.tZ)(h.Z,{className:"alerts-list-view",columns:se,count:$,data:N,emptyState:ce,fetchData:F,filters:ue,initialSort:oe,loading:C,bulkActions:t,bulkSelectEnabled:T,disableBulkSelect:q,pageSize:25})})))}))}}]);
//# sourceMappingURL=d6e79a30ac772ea01149.chunk.js.map