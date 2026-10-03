/* Whole-page depth choreography, independent from the introductory WebGL scene. */
(() => {
 'use strict';
 const decks=[...document.querySelectorAll('.depth-deck')];if(!decks.length)return;
 const rail=[...document.querySelectorAll('.layer-rail a')],canvas=document.getElementById('architecture-canvas'),ctx=canvas.getContext('2d');
 const reduced=matchMedia('(prefers-reduced-motion: reduce)'),fine=matchMedia('(pointer:fine)');
 let frame=0,last=0,spin=.3,dirty=true,current=0,background=false;
 const cards=document.querySelectorAll('.case-card,.repo,.skill,.proj');
 cards.forEach(card=>{card.classList.remove('reveal');card.classList.add('depth-card');});
 function schedule(){dirty=true;if(!frame&&!document.hidden)frame=requestAnimationFrame(tick);}
 function layout(){
  const vh=innerHeight,activation=vh*.35;
  let next=0;
  decks.forEach((deck,i)=>{
   const r=deck.getBoundingClientRect(),surface=deck.querySelector('.depth-surface');
   if(r.top<activation)next=i;
   if(r.bottom<0||r.top>vh*1.2)return;
   const entry=Math.max(0,Math.min(1,(r.top-vh*.12)/(vh*.95)));
   const angle=reduced.matches?0:entry*(innerWidth<600?5:9);
   surface.style.setProperty('--deck-fold',`${angle.toFixed(2)}deg`);
   surface.style.setProperty('--deck-lift',`${(reduced.matches?0:entry*24).toFixed(1)}px`);
   surface.style.setProperty('--deck-turn',`${(reduced.matches?0:Math.sin(i*1.9)*entry*.7).toFixed(2)}deg`);
   deck.style.setProperty('--glyph-angle',`${reduced.matches?32:32+i*12+Math.max(0,-r.top)/30}deg`);
  });
  current=next;rail.forEach((a,i)=>{if(i===current)a.setAttribute('aria-current','location');else a.removeAttribute('aria-current');});
  background=decks[0].getBoundingClientRect().top<vh;
 }
 function space(){
  if(!ctx||!background)return;
  const dpr=Math.min(devicePixelRatio||1,1.25),w=Math.round(canvas.clientWidth*dpr),h=Math.round(canvas.clientHeight*dpr);
  if(canvas.width!==w||canvas.height!==h){canvas.width=w;canvas.height=h;}
  ctx.clearRect(0,0,w,h);ctx.lineWidth=dpr*.8;
  const ry=(v,a)=>[Math.cos(a)*v[0]+Math.sin(a)*v[2],v[1],-Math.sin(a)*v[0]+Math.cos(a)*v[2]];
  const faces=[];
  for(let layer=0;layer<7;layer++){
   const y=(layer-3)*.55,points=[];
   for(let side=0;side<6;side++){const a=side*Math.PI/3;let v=ry([Math.cos(a)*1.55,y,Math.sin(a)*1.55],spin+layer*.12+current*.35);v=[v[0],v[1]*.91-v[2]*.35,v[1]*.35+v[2]*.91-6];points.push(v);}
   faces.push({points,layer,z:points.reduce((s,v)=>s+v[2],0)/6});
  }
  faces.sort((a,b)=>a.z-b.z).forEach(({points,layer})=>{
   ctx.beginPath();points.forEach((v,i)=>{const x=w*.91+v[0]*h/-v[2],y=h*.52-v[1]*h/-v[2];i?ctx.lineTo(x,y):ctx.moveTo(x,y);});ctx.closePath();
   ctx.fillStyle=`rgba(${70+layer*12},85,160,.08)`;ctx.fill();ctx.strokeStyle=`rgba(${115+layer*14},${195-layer*9},255,.6)`;ctx.shadowColor='#a67dff';ctx.shadowBlur=12*dpr;ctx.stroke();ctx.shadowBlur=0;
  });
 }
 function tick(now){
  frame=0;if(document.hidden)return;
  if(now-last<42&&!dirty){if(background&&!reduced.matches)frame=requestAnimationFrame(tick);return;}
  const dt=Math.min((now-last)/1000,.08);last=now;
  if(dirty){layout();dirty=false;}if(!reduced.matches)spin+=dt*.08;space();
  if(background&&!reduced.matches)frame=requestAnimationFrame(tick);
 }
 // Delegation also handles GitHub cards that arrive after initial rendering.
 let tilted;
 document.querySelector('main').addEventListener('pointermove',event=>{
  if(reduced.matches||!fine.matches)return;
  const card=event.target.closest('.depth-card,.repo');if(!card)return;
  if(tilted&&tilted!==card){tilted.style.removeProperty('--card-x');tilted.style.removeProperty('--card-y');}
  card.classList.add('depth-card');tilted=card;const r=card.getBoundingClientRect();
  card.style.setProperty('--card-x',`${((.5-(event.clientY-r.top)/r.height)*3).toFixed(2)}deg`);
  card.style.setProperty('--card-y',`${(((event.clientX-r.left)/r.width-.5)*3).toFixed(2)}deg`);
 },{passive:true});
 document.querySelector('main').addEventListener('pointerout',event=>{if(tilted&&!tilted.contains(event.relatedTarget)){tilted.style.removeProperty('--card-x');tilted.style.removeProperty('--card-y');tilted=null;}},{passive:true});
 addEventListener('scroll',schedule,{passive:true});addEventListener('resize',schedule,{passive:true});
 if('ResizeObserver'in window)new ResizeObserver(schedule).observe(document.querySelector('main'));
 document.addEventListener('visibilitychange',()=>{if(document.hidden){cancelAnimationFrame(frame);frame=0;}else schedule();});
 reduced.addEventListener('change',schedule);schedule();
})();
