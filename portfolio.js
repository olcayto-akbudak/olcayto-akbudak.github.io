/* Perspective-projected folding planes. No dependencies; 24 fps, offscreen pause. */
(() => {
 const host=document.querySelector('.page-orbit');if(!host)return;
 const canvas=host.querySelector('canvas'),ctx=canvas.getContext('2d');if(!ctx)return;
 const reduced=matchMedia('(prefers-reduced-motion: reduce)');
 const mesh=[];let frame=0,last=0,angle=.45,shown=true,pointer=0;
 for(let layer=0;layer<8;layer++)for(let side=0;side<6;side++){
  const y=(layer-3.5)*.27,r=1.24,a=side*Math.PI/3,b=(side+1)*Math.PI/3;
  const A=[Math.cos(a)*r,y,Math.sin(a)*r],B=[Math.cos(b)*r,y,Math.sin(b)*r];
  mesh.push({layer,points:[A,B,[B[0]*.78,y+.12,B[2]*.78],[A[0]*.78,y+.12,A[2]*.78]]});
  mesh.push({layer,points:[[A[0]*.78,y+.12,A[2]*.78],[B[0]*.78,y+.12,B[2]*.78],[0,y+.25,0]]});
 }
 const ry=(v,a)=>[Math.cos(a)*v[0]+Math.sin(a)*v[2],v[1],-Math.sin(a)*v[0]+Math.cos(a)*v[2]];
 const rx=(v,a)=>[v[0],Math.cos(a)*v[1]-Math.sin(a)*v[2],Math.sin(a)*v[1]+Math.cos(a)*v[2]];
 function render(){
  const dpr=Math.min(devicePixelRatio||1,1.5),w=Math.round(host.clientWidth*dpr),h=Math.round(host.clientHeight*dpr);
  if(canvas.width!==w||canvas.height!==h){canvas.width=w;canvas.height=h;}
  const scroll=Math.min(scrollY/Math.max(innerHeight,1),2),spread=reduced.matches?.18:.28+Math.sin(scroll*1.3)*.34;
  const faces=mesh.map(face=>{const points=face.points.map(v=>{let q=[v[0],v[1]+(face.layer-3.5)*spread*.28,v[2]];q=rx(ry(q,angle+pointer+(face.layer-3.5)*spread*.2),-.35+scroll*.14);q[2]-=5.1;return q;});return {...face,points,depth:points.reduce((s,v)=>s+v[2],0)/points.length};}).sort((a,b)=>a.depth-b.depth);
  ctx.clearRect(0,0,w,h);ctx.lineWidth=dpr;
  for(const face of faces){const t=face.layer/7;ctx.beginPath();face.points.forEach((q,i)=>{const x=w*.52+q[0]*h*1.22/-q[2],y=h*.50-q[1]*h*1.22/-q[2];i?ctx.lineTo(x,y):ctx.moveTo(x,y);});ctx.closePath();ctx.fillStyle=`rgba(${55+75*t},${105-30*t},${180+40*t},.33)`;ctx.fill();ctx.shadowColor=t>.5?'#bd84ff':'#75caff';ctx.shadowBlur=8*dpr;ctx.strokeStyle=`rgba(${135+65*t},${210-70*t},255,.94)`;ctx.stroke();ctx.shadowBlur=0;}
  host.style.opacity=String(Math.max(.12,(innerWidth<760?.5:.98)-scroll*.4));
 }
 function tick(now){frame=0;if(document.hidden||!shown)return;if(now-last<42){frame=requestAnimationFrame(tick);return;}const dt=Math.min((now-last)/1000,.08);last=now;if(!reduced.matches)angle+=dt*.12;render();if(!reduced.matches)frame=requestAnimationFrame(tick);}
 function start(){if(!frame&&!document.hidden&&shown)frame=requestAnimationFrame(tick);}
 addEventListener('resize',start,{passive:true});addEventListener('scroll',()=>{render();start();},{passive:true});addEventListener('pointermove',e=>{if(!reduced.matches)pointer=(e.clientX/innerWidth-.5)*.16;},{passive:true});
 document.addEventListener('visibilitychange',()=>{if(document.hidden){cancelAnimationFrame(frame);frame=0;}else start();});reduced.addEventListener('change',()=>{render();start();});
 new IntersectionObserver(entries=>{shown=entries[0].isIntersecting;if(shown)start();else{cancelAnimationFrame(frame);frame=0;}}).observe(host);start();
})();
