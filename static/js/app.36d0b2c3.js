(function(e){function t(t){for(var o,c,i=t[0],l=t[1],u=t[2],s=0,p=[];s<i.length;s++)c=i[s],Object.prototype.hasOwnProperty.call(a,c)&&a[c]&&p.push(a[c][0]),a[c]=0;for(o in l)Object.prototype.hasOwnProperty.call(l,o)&&(e[o]=l[o]);d&&d(t);while(p.length)p.shift()();return r.push.apply(r,u||[]),n()}function n(){for(var e,t=0;t<r.length;t++){for(var n=r[t],o=!0,i=1;i<n.length;i++){var l=n[i];0!==a[l]&&(o=!1)}o&&(r.splice(t--,1),e=c(c.s=n[0]))}return e}var o={},a={app:0},r=[];function c(t){if(o[t])return o[t].exports;var n=o[t]={i:t,l:!1,exports:{}};return e[t].call(n.exports,n,n.exports,c),n.l=!0,n.exports}c.m=e,c.c=o,c.d=function(e,t,n){c.o(e,t)||Object.defineProperty(e,t,{enumerable:!0,get:n})},c.r=function(e){"undefined"!==typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(e,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(e,"__esModule",{value:!0})},c.t=function(e,t){if(1&t&&(e=c(e)),8&t)return e;if(4&t&&"object"===typeof e&&e&&e.__esModule)return e;var n=Object.create(null);if(c.r(n),Object.defineProperty(n,"default",{enumerable:!0,value:e}),2&t&&"string"!=typeof e)for(var o in e)c.d(n,o,function(t){return e[t]}.bind(null,o));return n},c.n=function(e){var t=e&&e.__esModule?function(){return e["default"]}:function(){return e};return c.d(t,"a",t),t},c.o=function(e,t){return Object.prototype.hasOwnProperty.call(e,t)},c.p="/";var i=window["webpackJsonp"]=window["webpackJsonp"]||[],l=i.push.bind(i);i.push=t,i=i.slice();for(var u=0;u<i.length;u++)t(i[u]);var d=l;r.push([0,"chunk-vendors"]),n()})({0:function(e,t,n){e.exports=n("cd49")},"362d":function(e,t,n){},6265:function(e,t,n){},6877:function(e,t,n){},"6bec":function(e,t,n){},"8c45":function(e,t,n){e.exports=n.p+"static/img/HART-logo.37e960de.png"},cd49:function(e,t,n){"use strict";n.r(t);n("e260"),n("e6cf"),n("cca6"),n("a79d"),n("0cdd");var o=n("7a23"),a=Object(o["L"])("data-v-0e53b5f2");Object(o["v"])("data-v-0e53b5f2");var r={id:"app"},c={id:"content",class:"p-shadow-2"};Object(o["t"])();var i=a((function(e,t,n,i,l,u){var d=Object(o["A"])("Navbar"),s=Object(o["A"])("router-view");return Object(o["s"])(),Object(o["f"])("div",r,[Object(o["i"])(d),Object(o["i"])("div",c,[(Object(o["s"])(),Object(o["f"])(o["b"],null,{default:a((function(){return[Object(o["i"])(s)]})),_:1}))])])})),l=Object(o["L"])("data-v-5ad1927a");Object(o["v"])("data-v-5ad1927a");var u=Object(o["h"])("something else");Object(o["t"])();var d=l((function(e,t,n,a,r,c){var i=Object(o["A"])("TabMenu");return Object(o["s"])(),Object(o["f"])(i,{model:e.items,class:"p-shadow-2"},{default:l((function(){return[u]})),_:1},8,["model"])})),s=Object(o["j"])({name:"Navbar",setup:function(){var e=[{label:"Home",icon:"pi pi-fw pi-home",to:"/"},{label:"Documentation",icon:"pi pi-fw pi-file",to:"/documentation"},{label:"Phonemes",icon:"pi pi-fw pi-comment",to:"/phonemes"},{label:"Words",icon:"pi pi-fw pi-comments",to:"/words"},{label:"Audio",icon:"pi pi-fw pi-play",to:"/audio"}];return{items:e}}}),p=n("6b0d"),m=n.n(p);const h=m()(s,[["render",d],["__scopeId","data-v-5ad1927a"]]);var f=h,b=Object(o["j"])({name:"App",components:{Navbar:f}});const g=m()(b,[["render",i],["__scopeId","data-v-0e53b5f2"]]);var v=g,j=n("9319"),O=n("bb57"),w=(n("6265"),n("6877"),n("e1ae"),n("4121"),n("bddf"),n("c35b")),y=n("6c02"),x=n("8c45"),k=n.n(x),_=Object(o["L"])("data-v-0199e766");Object(o["v"])("data-v-0199e766");var A={style:{display:"flex","justify-content":"center","align-items":"center",width:"100%",height:"100%"}},P=Object(o["i"])("div",{style:{width:"600px",height:"600px"}},[Object(o["i"])("img",{src:k.a,height:"600",style:{"margin-top":"100px"}})],-1);Object(o["t"])();var R=_((function(e,t,n,a,r,c){return Object(o["s"])(),Object(o["f"])("div",A,[P])})),C=Object(o["j"])({name:"Home",setup:function(){var e="Home Message!";return{home_message:e}},created:function(){document.title="HART Prototype"}});const S=m()(C,[["render",R],["__scopeId","data-v-0199e766"]]);var L=S,T=Object(o["L"])("data-v-1b9fdfa1");Object(o["v"])("data-v-1b9fdfa1");var M={style:{"margin-left":"auto","margin-right":"auto",width:"70%"}},I=Object(o["i"])("h1",null,"How to get started",-1),W=Object(o["i"])("p",null,"In the tab for phonemes, you can do everything related to phonemes! This includes viewing all the phonemes that are used, just training single phonemes, but also taking a test. In the tab 'Words', you can do similar stuff as in the phonemes tab, but then with words. In the 'Audio' tab, you can upload an audio file for processing.",-1),B=Object(o["i"])("p",null,"Before getting started, put on the sleeve and check whether all the motors work correctly!",-1),E=Object(o["h"])("Check all motors in order!"),F=Object(o["i"])("br",null,null,-1),V=Object(o["h"])("Check specific motor");Object(o["t"])();var H=T((function(e,t,n,a,r,c){var i=Object(o["A"])("Button"),l=Object(o["A"])("Dropdown"),u=Object(o["A"])("Panel");return Object(o["s"])(),Object(o["f"])("div",M,[I,Object(o["i"])(u,{class:"p-shadow-4"},{default:T((function(){return[W,B,Object(o["i"])(i,{onClick:t[1]||(t[1]=function(t){return e.check_motors()}),class:"p-shadow-2",style:{padding:"0.9rem","margin-bottom":"20px"}},{default:T((function(){return[E]})),_:1}),F,Object(o["i"])(l,{modelValue:e.selectedMotor,"onUpdate:modelValue":t[2]||(t[2]=function(t){return e.selectedMotor=t}),options:e.motors,class:"p-shadow-2",optionLabel:"coord",placeholder:"Select a motor",filter:!0,style:{"margin-right":"10px"}},null,8,["modelValue","options"]),Object(o["i"])(i,{onClick:t[3]||(t[3]=function(t){return e.check_specific_motor()}),class:"p-shadow-2",style:{padding:"0.9rem"}},{default:T((function(){return[V]})),_:1})]})),_:1})])})),D=(n("96cf"),n("9ab4")),U=(n("99af"),n("d4ec")),q=n("bee2"),G=n("bc3a"),N=n.n(G),J="http://127.0.0.1:5000/",Y=N.a.create({baseURL:J}),z=function(e){e.status;var t=e.data,n=e.config;n.method,n.url;return t},K=function(e){var t=e.response,n=t.data,o=t.status,a=t.statusText;console.log(a+" - "+o+": "+n)},Q=function(){function e(){Object(U["a"])(this,e)}return Object(q["a"])(e,null,[{key:"getPhonemes",value:function(){return Y.get("/api/v1/phonemes").then(z).catch(K)}},{key:"checkMotors",value:function(){return Y.post("/api/v1/check_motors").then(z).catch(K)}},{key:"checkSpecificMotor",value:function(e,t){return Y.post("/api/v1/check_specific_motor",e,t).then(z).catch(K)}},{key:"sendPhonemeMicrocontroller",value:function(e,t){return Object(D["a"])(this,void 0,void 0,regeneratorRuntime.mark((function n(){return regeneratorRuntime.wrap((function(n){while(1)switch(n.prev=n.next){case 0:return n.abrupt("return",Y.post("/api/v1/microcontroller/phonemes",e,t).then(z).catch(K));case 1:case"end":return n.stop()}}),n)})))}},{key:"sendWordsMicrocontroller",value:function(e,t){return Object(D["a"])(this,void 0,void 0,regeneratorRuntime.mark((function n(){return regeneratorRuntime.wrap((function(n){while(1)switch(n.prev=n.next){case 0:return n.abrupt("return",Y.post("/api/v1/microcontroller/words",e,t).then(z).catch(K));case 1:case"end":return n.stop()}}),n)})))}},{key:"sendSentencesMicrocontroller",value:function(e,t){return Object(D["a"])(this,void 0,void 0,regeneratorRuntime.mark((function n(){return regeneratorRuntime.wrap((function(n){while(1)switch(n.prev=n.next){case 0:return n.abrupt("return",Y.post("/api/v1/microcontroller/sentences",e,t).then(z).catch(K));case 1:case"end":return n.stop()}}),n)})))}},{key:"sendAudioFile",value:function(e,t,n){return Object(D["a"])(this,void 0,void 0,regeneratorRuntime.mark((function n(){var o;return regeneratorRuntime.wrap((function(n){while(1)switch(n.prev=n.next){case 0:return o=new FormData,o.append("file",e),o.append("data",new Blob([JSON.stringify(t)],{type:"application/json"})),n.abrupt("return",Y.post("/api/v1/microcontroller/audiofile",o).then(z).catch(K));case 4:case"end":return n.stop()}}),n)})))}}]),e}(),X=Object(o["j"])({name:"Documentation",setup:function(){return Object(D["a"])(void 0,void 0,void 0,regeneratorRuntime.mark((function e(){var t,n,a,r;return regeneratorRuntime.wrap((function(e){while(1)switch(e.prev=e.next){case 0:return r=function(){Q.checkSpecificMotor({coord:t.value.coord})},a=function(){Q.checkMotors()},t=Object(o["x"])(),n=[{coord:"11"},{coord:"12"},{coord:"13"},{coord:"14"},{coord:"15"},{coord:"16"},{coord:"21"},{coord:"22"},{coord:"23"},{coord:"24"},{coord:"25"},{coord:"26"},{coord:"31"},{coord:"32"},{coord:"33"},{coord:"34"},{coord:"35"},{coord:"36"},{coord:"41"},{coord:"42"},{coord:"43"},{coord:"44"},{coord:"45"},{coord:"46"}],e.abrupt("return",{check_motors:a,selectedMotor:t,motors:n,check_specific_motor:r});case 5:case"end":return e.stop()}}),e)})))},created:function(){document.title="HART Prototype - Documentation"}});const Z=m()(X,[["render",H],["__scopeId","data-v-1b9fdfa1"]]);var $=Z,ee=(n("b0c0"),Object(o["L"])("data-v-f1691678"));Object(o["v"])("data-v-f1691678");var te={style:{"margin-left":"auto","margin-right":"auto",width:"70%"}},ne=Object(o["i"])("h1",{style:{"margin-bottom":"4px"}},"Phonemes",-1),oe=Object(o["i"])("p",null,"To just try out how a single phoneme feels, and play it on the sleeve, you can select a phoneme in the dropdown menu and send it to the sleeve.",-1),ae=Object(o["h"])("Send phoneme"),re=Object(o["i"])("p",null,"Select which phonemes you want to train on.",-1),ce={style:{"margin-bottom":"10px"}},ie=Object(o["h"])("Select all "),le=Object(o["h"])("Deselect all"),ue={style:{width:"min(100%, max(60%, 600px))","margin-top":"20px"}},de=Object(o["i"])("br",null,null,-1),se=Object(o["i"])("p",null,"By clicking the button, a phoneme will be send to the sleeve, and you will get to see three buttons, and have to choose which one you felt.",-1),pe=Object(o["h"])("Forced identification "),me=Object(o["i"])("div",{id:"forcedIdentificationButtons"},null,-1),he=Object(o["i"])("table",{id:"phoneme-table"},[Object(o["i"])("tr",null,[Object(o["i"])("th",null,"Round"),Object(o["i"])("th",null,"Correct answer"),Object(o["i"])("th",null,"Guessed answers")])],-1),fe=Object(o["h"])("Send random phoneme "),be=Object(o["i"])("table",{id:"random-phoneme-table"},[Object(o["i"])("tr",null,[Object(o["i"])("th",null,"Round"),Object(o["i"])("th",null,"Correct answer")])],-1);Object(o["t"])();var ge=ee((function(e,t,n,a,r,c){var i=Object(o["A"])("Dropdown"),l=Object(o["A"])("Button"),u=Object(o["A"])("Panel"),d=Object(o["A"])("Checkbox"),s=Object(o["A"])("Fieldset");return Object(o["s"])(),Object(o["f"])("div",te,[ne,Object(o["i"])(u,{header:"Send a chosen phoneme",class:"p-shadow-4",style:{"margin-bottom":"50px"}},{default:ee((function(){return[oe,Object(o["i"])(i,{modelValue:e.dropdownPhoneme,"onUpdate:modelValue":t[1]||(t[1]=function(t){return e.dropdownPhoneme=t}),class:"p-shadow-2",options:e.phonemes,optionLabel:"name",placeholder:"Phoneme",filter:!0,style:{"margin-right":"10px"}},null,8,["modelValue","options"]),Object(o["i"])(l,{onClick:t[2]||(t[2]=function(t){return e.sendDropdownPhoneme()}),class:"p-shadow-2",style:{padding:"0.9rem"}},{default:ee((function(){return[ae]})),_:1})]})),_:1}),Object(o["i"])(u,{header:"Training",class:"p-shadow-4"},{default:ee((function(){return[re,Object(o["i"])("div",ce,[Object(o["i"])(l,{onClick:t[3]||(t[3]=function(t){return e.selectAllPhonemes()}),class:"p-shadow-2",style:{padding:"0.9rem","margin-right":"10px"}},{default:ee((function(){return[ie]})),_:1}),Object(o["i"])(l,{onClick:t[4]||(t[4]=function(t){return e.deselectAllPhonemes()}),class:"p-shadow-2",style:{padding:"0.9rem"}},{default:ee((function(){return[le]})),_:1})]),Object(o["i"])("div",ue,[(Object(o["s"])(!0),Object(o["f"])(o["a"],null,Object(o["y"])(e.phonemes,(function(n){return Object(o["s"])(),Object(o["f"])("div",{key:n.name,class:"p-field-checkbox",style:{display:"inline-block",width:"70px"}},[Object(o["i"])(d,{id:"checkbox_"+n.name,name:"item.name",value:n.name,modelValue:e.selectedTrainPhonemes,"onUpdate:modelValue":t[5]||(t[5]=function(t){return e.selectedTrainPhonemes=t})},null,8,["id","value","modelValue"]),Object(o["i"])("label",{for:n},Object(o["D"])(n.name),9,["for"])])})),128))]),de,Object(o["i"])(u,{header:"Forced identification",class:"p-shadow-2",style:{"margin-top":"20px","margin-bottom":"20px"}},{default:ee((function(){return[se,Object(o["i"])(l,{onClick:t[6]||(t[6]=function(t){return e.sendForcedIdentification()}),class:"p-shadow-2",style:{padding:"0.9rem"}},{default:ee((function(){return[pe]})),_:1}),me,Object(o["i"])(s,{legend:"Answers (history)",toggleable:!0,collapsed:!0,style:{"margin-top":"20px"}},{default:ee((function(){return[he]})),_:1})]})),_:1}),Object(o["i"])(u,{header:"Send random",class:"p-shadow-2"},{default:ee((function(){return[Object(o["i"])(l,{onClick:t[7]||(t[7]=function(t){return e.sendRandomPhoneme()}),class:"p-shadow-2",style:{padding:"0.9rem","margin-top":"20px"}},{default:ee((function(){return[fe]})),_:1}),Object(o["i"])(s,{legend:"Answers (history)",toggleable:!0,collapsed:!0,style:{"margin-top":"20px"}},{default:ee((function(){return[be]})),_:1})]})),_:1})]})),_:1})])}));n("4160"),n("159b");function ve(e,t){var n=new Array(t),o=e.length,a=new Array(o);if(t>o)throw new RangeError("array.helper.getRandom: more elements taken than available.");while(t--){var r=Math.floor(Math.random()*o);n[t]=e[r in a?a[r]:r],a[r]=--o in a?a[o]:o}return n}var je=Object(o["j"])({name:"Phonemes",extends:{Button:O["a"]},setup:function(){return Object(D["a"])(void 0,void 0,void 0,regeneratorRuntime.mark((function e(){var t,n,a,r,c,i,l,u,d,s,p;return regeneratorRuntime.wrap((function(e){while(1)switch(e.prev=e.next){case 0:return p=function(){n.value=[]},s=function(){n.value=[],t.forEach((function(e){n.value.push(e)}))},u=function(){var e=document.getElementById("forcedIdentificationButtons");if(null!==e)if(e.innerHTML="",0!==n.value.length){var t=n.value,a=ve(t,1)[0];Q.sendPhonemeMicrocontroller({phonemes:[a]}),r.value++;var c=document.getElementById("phoneme-table");if(null!==c){var i=document.createElement("tr");i.innerHTML="<td>"+r.value+"</td><td>"+a+"</td><td id='pTableRow_"+r.value+"'></td>",c.appendChild(i);var l=document.createElement("div");l.innerHTML="<p>Which phoneme was just played?</p>",e.appendChild(l),t.forEach((function(t){var n=document.createElement("div");n.style.display="inline-block",n.style.marginRight="10px",e.appendChild(n),Object(o["e"])(O["a"],{label:t,id:"fid_"+t,class:"p-shadow-2",style:"margin-bottom: 4px"}).mount(n);var c=document.getElementById("fid_"+t),i=document.getElementById("pTableRow_"+r.value);null!==c&&null!==i&&c.addEventListener("click",(function(){var e=c.style.background;t===a?(c.style.background="green",i.innerHTML+="<span style='margin-right: 4px; margin-bottom: 4px; padding: 5px; color: #8800FF; font-weight: bolder'>"+t+"</span>"):(c.style.background="red",i.innerHTML+="<span style='margin-right: 4px; margin-bottom: 4px; padding: 5px'>"+t+"</span>"),setTimeout((function(){c.style.background=e}),1e3)}))}))}}else alert("Please select phonemes to train on")},l=function(){if(0===n.value.length)alert("Please select phonemes to train on");else{var e=n.value[Math.floor(Math.random()*n.value.length)],t={phonemes:[e]};Q.sendPhonemeMicrocontroller(t);var o=document.getElementById("random-phoneme-table");if(null===o)return;var a=document.createElement("tr");c.value++,a.insertCell(),a.innerHTML="<td>"+c.value+"</td><td>"+e+"</td>",o.appendChild(a)}},i=function(){if(void 0!==a.value){var e={phonemes:[a.value.name]};Q.sendPhonemeMicrocontroller(e)}else alert("Please select a phoneme to send")},e.next=7,Q.getPhonemes();case 7:return t=e.sent.phonemes,n=Object(o["x"])([]),a=Object(o["x"])(),r=Object(o["x"])(0),c=Object(o["x"])(0),d=[],t.forEach((function(e){d.push({name:e})})),e.abrupt("return",{phonemes:d,selectedTrainPhonemes:n,dropdownPhoneme:a,fiRows:r,raRows:c,sendDropdownPhoneme:i,sendRandomPhoneme:l,sendForcedIdentification:u,selectAllPhonemes:s,deselectAllPhonemes:p});case 15:case"end":return e.stop()}}),e)})))},created:function(){document.title="HART Prototype - Phonemes"}});const Oe=m()(je,[["render",ge],["__scopeId","data-v-f1691678"]]);var we=Oe,ye=Object(o["L"])("data-v-5152cadd");Object(o["v"])("data-v-5152cadd");var xe={style:{"margin-left":"auto","margin-right":"auto",width:"70%"}},ke=Object(o["i"])("h1",{style:{"margin-bottom":"4px"}},"Words",-1),_e=Object(o["i"])("p",null,"In this panel you can configure the list by adding (or removing) word to (from) the preprogrammed list of words. Additionally, you can send any word you want to the sleeve.",-1),Ae=Object(o["h"])("Add word to list "),Pe=Object(o["h"])("Remove word from list "),Re=Object(o["h"])("Send word"),Ce=Object(o["i"])("p",null,"Select the words that you would like to train on. Only words from the list (which can be configured above) can be used for training.",-1),Se={style:{"margin-bottom":"10px"}},Le=Object(o["h"])("Select all words "),Te=Object(o["h"])("Deselect all words"),Me=Object(o["i"])("p",null,"By clicking the button, a word will be send to the sleeve. You will then get to see three buttons representing words, and you will have to choose which one you felt.",-1),Ie=Object(o["h"])("Forced identification "),We=Object(o["i"])("div",{id:"forcedIdentificationButtons"},null,-1),Be=Object(o["i"])("table",{id:"fi-answer-table"},[Object(o["i"])("tr",null,[Object(o["i"])("th",null,"Round"),Object(o["i"])("th",null,"Correct answer"),Object(o["i"])("th",null,"Guessed answers")])],-1),Ee=Object(o["i"])("p",null,"Type a sentence you want to send to the sleeve and select a language that it is written in.",-1),Fe=Object(o["h"])("Send sentence! ");Object(o["t"])();var Ve=ye((function(e,t,n,a,r,c){var i=Object(o["A"])("AutoComplete"),l=Object(o["A"])("Button"),u=Object(o["A"])("Panel"),d=Object(o["A"])("Fieldset"),s=Object(o["A"])("InputText");return Object(o["s"])(),Object(o["f"])("div",xe,[ke,Object(o["i"])(u,{header:"Configure list of words, and send specific words",class:"p-shadow-4",style:{"margin-bottom":"50px"}},{default:ye((function(){return[_e,Object(o["i"])(i,{modelValue:e.selectedWord,"onUpdate:modelValue":t[1]||(t[1]=function(t){return e.selectedWord=t}),dropdown:!0,suggestions:e.filteredWords.value,onComplete:t[2]||(t[2]=function(t){return e.searchWord(t)}),field:"name",style:{"margin-right":"10px"}},null,8,["modelValue","suggestions"]),Object(o["i"])(l,{onClick:t[3]||(t[3]=function(t){return e.addWord()}),class:"p-shadow-2",style:{padding:"0.9rem","margin-right":"10px"}},{default:ye((function(){return[Ae]})),_:1}),Object(o["i"])(l,{onClick:t[4]||(t[4]=function(t){return e.removeWord()}),class:"p-shadow-2",style:{padding:"0.9rem","margin-right":"10px"}},{default:ye((function(){return[Pe]})),_:1}),Object(o["i"])(l,{onClick:t[5]||(t[5]=function(t){return e.sendACWord()}),class:"p-shadow-2",style:{padding:"0.9rem"}},{default:ye((function(){return[Re]})),_:1})]})),_:1}),Object(o["i"])(u,{header:"Selection based training",class:"p-shadow-4",style:{"margin-bottom":"50px"}},{default:ye((function(){return[Ce,Object(o["i"])("div",Se,[Object(o["i"])(l,{onClick:t[6]||(t[6]=function(t){return e.selectAllWords()}),class:"p-shadow-2",style:{padding:"0.9rem","margin-right":"10px"}},{default:ye((function(){return[Le]})),_:1}),Object(o["i"])(l,{onClick:t[7]||(t[7]=function(t){return e.deselectAllWords()}),class:"p-shadow-2",style:{padding:"0.9rem"}},{default:ye((function(){return[Te]})),_:1})]),Object(o["i"])(i,{multiple:!0,modelValue:e.selectedWords,"onUpdate:modelValue":t[8]||(t[8]=function(t){return e.selectedWords=t}),suggestions:e.filteredWords.value,dropdown:!0,onComplete:t[9]||(t[9]=function(t){return e.searchWord(t)}),field:"name",style:{width:"100%","margin-bottom":"10px"}},null,8,["modelValue","suggestions"]),Object(o["i"])(u,{header:"Forced identification",class:"p-shadow-2",style:{"margin-top":"20px"}},{default:ye((function(){return[Me,Object(o["i"])(l,{onClick:t[10]||(t[10]=function(t){return e.sendForcedIdentification()}),class:"p-shadow-2",style:{padding:"0.9rem"}},{default:ye((function(){return[Ie]})),_:1}),We,Object(o["i"])(d,{legend:"Answers (history)",toggleable:!0,collapsed:!0,style:{"margin-top":"20px"}},{default:ye((function(){return[Be]})),_:1})]})),_:1})]})),_:1}),Object(o["i"])(u,{header:"Send sentences",class:"p-shadow-4"},{default:ye((function(){return[Ee,Object(o["i"])(s,{type:"text",class:"p-shadow-2",modelValue:e.inputSentence,"onUpdate:modelValue":t[11]||(t[11]=function(t){return e.inputSentence=t}),style:{width:"100%","margin-bottom":"10px"}},null,8,["modelValue"]),Object(o["i"])(i,{modelValue:e.selectedLanguage,"onUpdate:modelValue":t[12]||(t[12]=function(t){return e.selectedLanguage=t}),dropdown:!0,suggestions:e.filteredLanguages.value,placeholder:"Select language",onComplete:t[13]||(t[13]=function(t){return e.searchLanguage(t)}),field:"language",style:{"margin-right":"10px"}},null,8,["modelValue","suggestions"]),Object(o["i"])(l,{onClick:t[14]||(t[14]=function(t){return e.sendSentence()}),class:"p-shadow-2",style:{padding:"0.9rem","margin-right":"10px"}},{default:ye((function(){return[Fe]})),_:1})]})),_:1})])})),He=(n("4de4"),n("c740"),n("caad"),n("d81d"),n("a434"),n("2532"),Object(o["j"])({name:"Words",setup:function(){return Object(D["a"])(void 0,void 0,void 0,regeneratorRuntime.mark((function e(){var t,n,a,r,c,i,l,u,d,s,p,m,h,f,b,g,v,j;return regeneratorRuntime.wrap((function(e){while(1)switch(e.prev=e.next){case 0:return j=function(){n.value=[]},v=function(){n.value=[],i.value.forEach((function(e){n.value.push(e)}))},g=function(){if(void 0===t.value)alert("Please type a word first before removing!");else{var e=i.value.findIndex((function(e){return e.name===t.value.name||e.name===t.value}));-1===e?alert("Word not found in list, thus cannot be removed."):(alert("'"+i.value[e].name+"' was removed from the list"),i.value.splice(e,1),t.value="")}},b=function(){void 0===t.value?alert("Please type a word first before inserting!"):(alert("'"+t.value+"' was added to the list"),i.value.push({name:t.value}),t.value="")},f=function(){void 0===a.value&&alert("Please select a language in which the sentence is written."),void 0===r.value&&alert("Please write a sentence that you would like to send."),Q.sendSentencesMicrocontroller({sentences:[r.value],language:a.value.short})},h=function(){if(0!==n.value.length){var e=n.value.map((function(e){return e.name})),t=ve(e,1)[0];Q.sendWordsMicrocontroller({words:[t]}),c.value++;var a=document.getElementById("forcedIdentificationButtons");if(null!==a){a.innerHTML="";var r=document.createElement("div");r.innerHTML="<p>Which word was just played?</p>",a.appendChild(r);var i=document.getElementById("fi-answer-table");if(null!==i){var l=document.createElement("tr");l.innerHTML="<td>"+c.value+"</td><td>"+t+"</td><td id='fi-answer-table-row_"+c.value+"'></td>",i.appendChild(l),e.forEach((function(e){var n=document.createElement("div");n.style.display="inline-block",n.style.marginRight="10px",a.appendChild(n),Object(o["e"])(O["a"],{label:e,id:"fid_"+e,class:"p-shadow-2",style:"margin-bottom: 4px"}).mount(n);var r=document.getElementById("fid_"+e),i=document.getElementById("fi-answer-table-row_"+c.value);null!==r&&null!==i&&r.addEventListener("click",(function(){var n=r.style.background;e===t?(r.style.background="green",i.innerHTML+="<span style='margin-right: 4px; margin-bottom: 4px; padding: 5px; color: #8800FF; font-weight: bolder'>"+e+"</span>"):(r.style.background="red",i.innerHTML+="<span style='margin-right: 4px; margin-bottom: 4px; padding: 5px'>"+e+"</span>"),setTimeout((function(){r.style.background=n}),1e3)}))}))}}}else alert("Please select words to train on")},m=function(){void 0!==t.value?"string"!==typeof t.value?Q.sendWordsMicrocontroller({words:[t.value.name]}):Q.sendWordsMicrocontroller({words:[t.value]}):alert("Please insert a word to send")},p=function(e){d.value=Object(o["x"])(l.value.map((function(t){return t.language.includes(e.query)?t:null})).filter((function(e){return!!e})))},s=function(e){u.value=Object(o["x"])(i.value.map((function(t){return t.name.includes(e.query)?t:null})).filter((function(e){return!!e})))},t=Object(o["x"])(),n=Object(o["x"])([]),a=Object(o["x"])(),r=Object(o["x"])(),c=Object(o["x"])(0),i=Object(o["x"])([{name:"human"},{name:"purple"},{name:"laptop"},{name:"jacket"},{name:"cyborg"},{name:"sleeve"},{name:"prototype"},{name:"keyword"},{name:"phone"},{name:"charger"},{name:"battery"},{name:"students"},{name:"HART"},{name:"research"},{name:"innovation"},{name:"augmentation"},{name:"hearing"},{name:"sense"},{name:"feeling"},{name:"showcase"},{name:"student team"}]),l=Object(o["x"])([{language:"English",short:"en"},{language:"French",short:"fr"},{language:"German",short:"de"},{language:"French",short:"fr"},{language:"Russian",short:"ru"}]),u=Object(o["x"])(i.value),d=Object(o["x"])(l.value),e.abrupt("return",{selectedWord:t,selectedWords:n,filteredWords:u,words:i,languages:l,filteredLanguages:d,selectedLanguage:a,inputSentence:r,searchWord:s,searchLanguage:p,sendACWord:m,sendForcedIdentification:h,sendSentence:f,addWord:b,removeWord:g,selectAllWords:v,deselectAllWords:j});case 19:case"end":return e.stop()}}),e)})))},created:function(){document.title="HART Prototype - Words"}}));const De=m()(He,[["render",Ve],["__scopeId","data-v-5152cadd"]]);var Ue=De,qe=Object(o["L"])("data-v-561bf55f");Object(o["v"])("data-v-561bf55f");var Ge={style:{"margin-left":"auto","margin-right":"auto",width:"70%"}},Ne=Object(o["i"])("h1",null,"Audio!",-1),Je=Object(o["i"])("p",null,"Select and upload a file you want to send to the microcontroller and select a language that it is spoken in.",-1),Ye=Object(o["i"])("br",null,null,-1),ze=Object(o["i"])("br",null,null,-1),Ke=Object(o["h"])("Send File to Microcontroller"),Qe=Object(o["i"])("p",null,"In this panel, you can record some audio, select the language which you spoke and then send that for processing towards the microcontroller. Be aware, the compression on the audio is quite severe, so quality is not very good.",-1),Xe=Object(o["h"])(" Record "),Ze=Object(o["h"])(" Stop Recording "),$e=Object(o["h"])("play"),et=Object(o["i"])("br",null,null,-1),tt=Object(o["i"])("br",null,null,-1),nt=Object(o["h"])("Send Audio!");Object(o["t"])();var ot=qe((function(e,t,n,a,r,c){var i=Object(o["A"])("AutoComplete"),l=Object(o["A"])("Button"),u=Object(o["A"])("Panel");return Object(o["s"])(),Object(o["f"])("div",Ge,[Ne,Object(o["i"])(u,{header:"Send audio file",class:"p-shadow-4"},{default:qe((function(){return[Je,Object(o["i"])("input",{type:"file",ref:"fileInput",onChange:t[1]||(t[1]=function(t){return e.onFileSelected(t)})},null,544),Ye,Object(o["i"])(i,{modelValue:e.selectedLanguage1,"onUpdate:modelValue":t[2]||(t[2]=function(t){return e.selectedLanguage1=t}),dropdown:!0,suggestions:e.filteredLanguages.value,placeholder:"Select language",onComplete:t[3]||(t[3]=function(t){return e.searchLanguage(t)}),field:"language",style:{"margin-bottom":"10px","margin-top":"10px"}},null,8,["modelValue","suggestions"]),ze,Object(o["i"])(l,{onClick:t[4]||(t[4]=function(t){return e.sendFile()}),style:{"margin-right":"10px"},class:"p-shadow-2"},{default:qe((function(){return[Ke]})),_:1})]})),_:1}),Object(o["i"])(u,{header:"Record Audio",class:"p-shadow-4"},{default:qe((function(){return[Qe,Object(o["i"])(l,{onClick:t[5]||(t[5]=function(t){return e.startRecord()}),type:"button",id:"button_record",class:"p-button p-shadow-2",style:{"margin-right":"10px"}},{default:qe((function(){return[Xe]})),_:1}),Object(o["i"])(l,{onClick:t[6]||(t[6]=function(t){return e.stopRecord()}),type:"button",id:"button_stop",class:"p-button-danger p-shadow-2",style:{"margin-right":"10px"}},{default:qe((function(){return[Ze]})),_:1}),Object(o["i"])(l,{id:"play-btn",class:"p-button p-shadow-2",disabled:""},{default:qe((function(){return[$e]})),_:1}),et,Object(o["i"])(i,{modelValue:e.selectedLanguage2,"onUpdate:modelValue":t[7]||(t[7]=function(t){return e.selectedLanguage2=t}),dropdown:!0,suggestions:e.filteredLanguages.value,placeholder:"Select language",onComplete:t[8]||(t[8]=function(t){return e.searchLanguage(t)}),field:"language",style:{"margin-bottom":"10px","margin-top":"10px"}},null,8,["modelValue","suggestions"]),tt,Object(o["i"])(l,{onClick:t[9]||(t[9]=function(t){return e.sendRecording()}),id:"send-btn",class:"p-button p-shadow-2",disabled:""},{default:qe((function(){return[nt]})),_:1})]})),_:1})])})),at=Object(o["j"])({name:"Audio",setup:function(){return Object(D["a"])(void 0,void 0,void 0,regeneratorRuntime.mark((function e(){var t,n,a,r,c,i,l,u,d,s,p,m,h,f,b,g,v;return regeneratorRuntime.wrap((function(e){while(1)switch(e.prev=e.next){case 0:return v=function(e){var t=new AudioContext,n=new FileReader;n.onload=function(){return t.decodeAudioData(n.result).then((function(e){var n=document.getElementById("play-btn");n.onclick=function(){var n=t.createBufferSource();n.buffer=e,n.connect(t.destination),n.start(0)},n.disabled=!1;var o=document.getElementById("send-btn");o.disabled=!1}))},n.readAsArrayBuffer(e)},g=function(e){i=new Blob(e,{type:c}),v(i)},b=function(){r.stop()},f=function(e){var t=[];c=["audio/webm","audio/ogg"].filter(MediaRecorder.isTypeSupported)[0],r=new MediaRecorder(e,{mimeType:c}),r.addEventListener("start",(function(){t.length=0})),r.ondataavailable=function(e){t.push(e.data)},r.onstop=function(){e.getTracks().forEach((function(e){return e.stop()})),g(t)},r.start()},h=function(){navigator.mediaDevices.getUserMedia({audio:!0}).then(f).catch(console.error)},m=function(e){u.value=Object(o["x"])(l.value.map((function(t){return t.language.toLowerCase().includes(e.query.toLowerCase())?t:null})).filter((function(e){return!!e})))},p=function(e){t=e.target.files[0],console.log(t)},s=function(){return void 0===a.value?alert("Please select the spoken language"):void 0===i?alert("Record some audio first!"):void Q.sendAudioFile(i,{source_language:a.value.short,target_language:"en",type:c})},d=function(){void 0!==n.value?void 0!==t?Q.sendAudioFile(t,{source_language:n.value.short,target_language:"en",type:"audio/flac"}):alert("Please upload an audio file"):alert("Please select the spoken language")},t=void 0,n=Object(o["x"])(),a=Object(o["x"])(),i=void 0,l=Object(o["x"])([{language:"Dutch",short:"nl"},{language:"English",short:"en"},{language:"French",short:"fr"},{language:"German",short:"de"},{language:"Russian",short:"ru"}]),u=Object(o["x"])(l.value),e.abrupt("return",{selectedLanguage1:n,selectedLanguage2:a,filteredLanguages:u,languages:l,sendFile:d,onFileSelected:p,searchLanguage:m,startRecord:h,stopRecord:b,sendRecording:s});case 16:case"end":return e.stop()}}),e)})))},created:function(){document.title="HART Prototype - Audio"}});const rt=m()(at,[["render",ot],["__scopeId","data-v-561bf55f"]]);var ct=rt,it=Object(o["L"])("data-v-4a6d696a");Object(o["v"])("data-v-4a6d696a");var lt=Object(o["i"])("h1",null,"Settings",-1),ut=Object(o["h"])("Switch Themes!");Object(o["t"])();var dt=it((function(e,t,n,a,r,c){var i=Object(o["A"])("Button");return Object(o["s"])(),Object(o["f"])(o["a"],null,[lt,Object(o["i"])(i,{onClick:e.darkThemeSwitch},{default:it((function(){return[ut]})),_:1},8,["onClick"])],64)})),st=function(){function e(){Object(U["a"])(this,e)}return Object(q["a"])(e,[{key:"darkThemeSwitch",value:function(){var e=document.styleSheets;e[0].disabled=!e[0].disabled,e[1].disabled=!e[1].disabled,e[2].disabled=!e[2].disabled,e[3].disabled=!e[3].disabled}}]),e}(),pt=Object(o["j"])({name:"Settings",created:function(){document.title="HART Prototype - Settings"},setup:function(){var e=new st;return{themeChanger:e}},methods:{darkThemeSwitch:function(){this.themeChanger.darkThemeSwitch()}}});const mt=m()(pt,[["render",dt],["__scopeId","data-v-4a6d696a"]]);var ht=mt,ft=[{path:"/",name:"Home",component:L},{path:"/documentation",name:"Documentation",component:$},{path:"/phonemes",name:"Phonemes",component:we},{path:"/words",name:"Words",component:Ue},{path:"/audio",name:"Audio",component:ct},{path:"/settings",name:"Settings",component:ht}],bt=Object(y["a"])({history:Object(y["b"])(),routes:ft}),gt=n("2052"),vt=n("0100"),jt=n("1e2d"),Ot=n("743f"),wt=n("8398"),yt=n("4084"),xt=(n("6bec"),n("362d"),Object(o["e"])(v));xt.use(j["a"],{ripple:!0}),xt.use(bt),xt.component("Button",O["a"]),xt.component("TabMenu",w["a"]),xt.component("Checkbox",gt["a"]),xt.component("Dropdown",vt["a"]),xt.component("Panel",jt["a"]),xt.component("Fieldset",Ot["a"]),xt.component("AutoComplete",yt["a"]),xt.component("InputText",wt["a"]),xt.mount("#app")}});
//# sourceMappingURL=app.36d0b2c3.js.map