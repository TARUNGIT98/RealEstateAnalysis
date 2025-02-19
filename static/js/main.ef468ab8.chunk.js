(this.webpackJsonphouse_price_estimator=this.webpackJsonphouse_price_estimator||[]).push([[0],{13:function(e,t,a){},14:function(e,t,a){},15:function(e,t,a){"use strict";a.r(t);var n=a(0),c=a.n(n),l=a(3),o=a.n(l);a(13),a(14);var r=()=>{const[e,t]=Object(n.useState)(1e3),[a,l]=Object(n.useState)(2),[o,r]=Object(n.useState)(2),[i,s]=Object(n.useState)(""),[m,u]=Object(n.useState)([]),[h,p]=Object(n.useState)(null);Object(n.useEffect)(()=>{fetch("http://127.0.0.1:5000/api/get_location_names").then(e=>e.json()).then(e=>{e.locations&&u(e.locations)}).catch(e=>console.error("Error fetching locations:",e))},[]);return c.a.createElement("div",{className:"container"},c.a.createElement("div",{className:"form"},c.a.createElement("h2",null,"Area (Square Feet)"),c.a.createElement("input",{className:"area-input",type:"number",value:e,onChange:e=>t(e.target.value)}),c.a.createElement("h2",null,"BHK"),c.a.createElement("div",{className:"switch-field"},[1,2,3,4,5].map(e=>c.a.createElement(c.a.Fragment,{key:e},c.a.createElement("input",{type:"radio",id:"bhk-"+e,name:"bhk",value:e,checked:a===e,onChange:()=>l(e)}),c.a.createElement("label",{htmlFor:"bhk-"+e},e)))),c.a.createElement("h2",null,"Bath"),c.a.createElement("div",{className:"switch-field"},[1,2,3,4,5].map(e=>c.a.createElement(c.a.Fragment,{key:e},c.a.createElement("input",{type:"radio",id:"bath-"+e,name:"bath",value:e,checked:o===e,onChange:()=>r(e)}),c.a.createElement("label",{htmlFor:"bath-"+e},e)))),c.a.createElement("h2",null,"Location"),c.a.createElement("select",{className:"select-field",value:i,onChange:e=>s(e.target.value)},c.a.createElement("option",{value:"",disabled:!0},"Choose a Location"),m.map(e=>c.a.createElement("option",{key:e,value:e},e))),c.a.createElement("button",{type:"button",className:"submit-button",onClick:async()=>{if(!i)return void alert("Please select a location.");const t=await fetch("http://127.0.0.1:5000/api/predict_home_price",{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify({total_sqft:parseFloat(e),bhk:a,bath:o,location:i})}),n=await t.json();p(n.estimated_price)}},"Estimate Price"),h&&c.a.createElement("div",{className:"result"},c.a.createElement("h2",null,"Estimated Price: \u20b9",h," Lakh"))))};var i=e=>{e&&e instanceof Function&&a.e(3).then(a.bind(null,16)).then(t=>{let{getCLS:a,getFID:n,getFCP:c,getLCP:l,getTTFB:o}=t;a(e),n(e),c(e),l(e),o(e)})};o.a.createRoot(document.getElementById("root")).render(c.a.createElement(c.a.StrictMode,null,c.a.createElement(r,null))),i()},4:function(e,t,a){e.exports=a(15)}},[[4,1,2]]]);
//# sourceMappingURL=main.ef468ab8.chunk.js.map