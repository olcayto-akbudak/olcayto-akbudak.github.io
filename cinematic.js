/* Native WebGL: illuminated folding planes, depth, perspective and scroll choreography. */
(() => {
  'use strict';
  const journey=document.querySelector('.fold-journey');
  if(!journey)return;
  const stage=journey.querySelector('.fold-stage'),canvas=document.getElementById('fold-canvas');
  const panels=[...journey.querySelectorAll('.fold-panel')],marks=[...journey.querySelectorAll('.fold-track b')];
  const preference=matchMedia('(prefers-reduced-motion: reduce)');
  let stopped=preference.matches,visible=true,frame=0,last=0,spin=0,gl,ctx,mesh=[],program,buffer,wireBuffer,count=0,wireCount=0;
  let pointer={x:0,y:0},smoothed=0,dirty=true;
  document.body.classList.add('fold-enhanced');
  function setControl(){document.body.classList.toggle('fold-static',stopped);if(stopped){smoothed=0;choreography(0);draw(0);}}
  preference.addEventListener('change',()=>{stopped=preference.matches;setControl();dirty=true;start();});setControl();
  function progress(){const rect=journey.getBoundingClientRect();return Math.max(0,Math.min(1,-rect.top/Math.max(1,journey.offsetHeight-innerHeight)));}
  function choreography(p){
    const selected=p<.32?0:p<.68?1:2;
    panels.forEach((panel,i)=>{
      const d=p-(i===0?0:i===1?.49:1);
      let opacity=i===0?1-Math.max(0,(p-.12)/.2):i===1?Math.min((p-.25)/.13,(.78-p)/.13):(p-.64)/.16;
      opacity=Math.max(0,Math.min(1,opacity));
      panel.hidden=opacity<.01;panel.style.opacity=opacity;
      panel.style.transform=`translateY(calc(-42% + ${d*-120}px)) perspective(1000px) rotateX(${d*12}deg) rotateY(${d*-10}deg)`;
      panel.style.filter=`blur(${(1-opacity)*6}px)`;panel.style.pointerEvents=i===selected?'auto':'none';
      panel.inert=i!==selected;
    });
    marks.forEach((mark,i)=>mark.classList.toggle('active',i===selected));
  }
  const vertex=`attribute vec3 aPosition;attribute vec3 aNormal;attribute float aLayer;
uniform float uTime,uProgress,uAspect,uMobile;uniform vec2 uPointer;varying vec3 vNormal;varying vec3 vPosition;varying float vLayer;
vec3 ry(vec3 p,float a){return vec3(cos(a)*p.x+sin(a)*p.z,p.y,-sin(a)*p.x+cos(a)*p.z);}
vec3 rx(vec3 p,float a){return vec3(p.x,cos(a)*p.y-sin(a)*p.z,sin(a)*p.y+cos(a)*p.z);}
void main(){float explode=sin(uProgress*3.14159265);float fold=(aLayer-3.5)*.17*explode;
vec3 p=aPosition;p.y+=(aLayer-3.5)*explode*.18;p=ry(p,fold);p=rx(p,-.25+uProgress*.45);
float angle=uTime+uProgress*2.5+uPointer.x*.12;p=ry(p,angle);p=rx(p,uPointer.y*.08);
vNormal=rx(ry(aNormal,angle+fold),-.25+uProgress*.45);vPosition=p;vLayer=aLayer;
p.x+=mix(1.35,.85,uMobile);p.y+=mix(.0,-.48,uMobile);p.z-=6.3;
float near=.1,far=40.;float f=2.35;gl_Position=vec4(f*p.x/uAspect,f*p.y,((far+near)/(near-far))*p.z+(2.*far*near/(near-far)),-p.z);}`;
  const fragment=`precision mediump float;varying vec3 vNormal;varying vec3 vPosition;varying float vLayer;uniform float uWire;
void main(){vec3 n=normalize(vNormal);float lit=max(0.,dot(n,normalize(vec3(-1.,2.,3.))));float rim=pow(1.-abs(n.z),2.);
vec3 cool=vec3(.22,.44,.72),warm=vec3(.62,.35,.86);vec3 base=mix(cool,warm,vLayer/7.);
vec3 col=base*(.38+lit*1.15)+vec3(.32,.47,.62)*rim*.35;
if(uWire>.5)col=mix(vec3(.40,.61,.79),vec3(.72,.52,.94),vLayer/7.);
gl_FragColor=vec4(col,1.);}`;
  function init(){
    try{
      gl=canvas.getContext('webgl',{alpha:true,antialias:true,powerPreference:'low-power'});if(!gl){initSoftware();return;}
      function shader(type,source){const s=gl.createShader(type);gl.shaderSource(s,source);gl.compileShader(s);if(!gl.getShaderParameter(s,gl.COMPILE_STATUS))throw Error(gl.getShaderInfoLog(s));return s;}
      program=gl.createProgram();gl.attachShader(program,shader(gl.VERTEX_SHADER,vertex));gl.attachShader(program,shader(gl.FRAGMENT_SHADER,fragment));gl.linkProgram(program);if(!gl.getProgramParameter(program,gl.LINK_STATUS))throw Error('Shader link');
      const data=[],lines=[];
      function triangle(a,b,c,layer){const u=b.map((x,i)=>x-a[i]),v=c.map((x,i)=>x-a[i]);const n=[u[1]*v[2]-u[2]*v[1],u[2]*v[0]-u[0]*v[2],u[0]*v[1]-u[1]*v[0]];for(const p of [a,b,c])data.push(...p,...n,layer);for(const p of [a,b,b,c,c,a])lines.push(...p,...n,layer);}
      for(let layer=0;layer<8;layer++){
        const y=(layer-3.5)*.25,r=1.05+Math.sin(layer/7*Math.PI)*.25;
        for(let side=0;side<6;side++){
          const angle=side*Math.PI/3+.25,angle2=(side+1)*Math.PI/3+.25;
          const a=[Math.cos(angle)*r,y,Math.sin(angle)*r],b=[Math.cos(angle2)*r,y,Math.sin(angle2)*r];
          const c=[b[0]*.75,y+.09,b[2]*.75],d=[a[0]*.75,y+.09,a[2]*.75];
          triangle(a,b,c,layer);triangle(a,c,d,layer);
          const e=[0,y+.18,0];triangle(d,c,e,layer);
          const lowerA=[a[0],y-.05,a[2]],lowerB=[b[0],y-.05,b[2]];
          triangle(lowerA,lowerB,b,layer);triangle(lowerA,b,a,layer);
        }
      }
      count=data.length/7;wireCount=lines.length/7;
      buffer=gl.createBuffer();gl.bindBuffer(gl.ARRAY_BUFFER,buffer);gl.bufferData(gl.ARRAY_BUFFER,new Float32Array(data),gl.STATIC_DRAW);
      wireBuffer=gl.createBuffer();gl.bindBuffer(gl.ARRAY_BUFFER,wireBuffer);gl.bufferData(gl.ARRAY_BUFFER,new Float32Array(lines),gl.STATIC_DRAW);
      gl.enable(gl.DEPTH_TEST);gl.enable(gl.BLEND);gl.blendFunc(gl.SRC_ALPHA,gl.ONE_MINUS_SRC_ALPHA);
      journey.classList.add('webgl-ready');
    }catch(error){gl=null;console.warn('3D sahne statik görünümle sunuluyor.',error.message);}
  }
  function initSoftware(){
    ctx=canvas.getContext('2d');if(!ctx)return;
    mesh=[];
    for(let layer=0;layer<8;layer++){
      const y=(layer-3.5)*.25,r=1.05+Math.sin(layer/7*Math.PI)*.25;
      for(let side=0;side<6;side++){
        const a=side*Math.PI/3+.25,b=(side+1)*Math.PI/3+.25;
        const A=[Math.cos(a)*r,y,Math.sin(a)*r],B=[Math.cos(b)*r,y,Math.sin(b)*r];
        const C=[B[0]*.75,y+.09,B[2]*.75],D=[A[0]*.75,y+.09,A[2]*.75];
        mesh.push({layer,points:[A,B,C,D]},{layer,points:[D,C,[0,y+.18,0]]},{layer,points:[[A[0],y-.05,A[2]],[B[0],y-.05,B[2]],B,A]});
      }
    }
    journey.classList.add('webgl-ready');canvas.dataset.renderer='software-3d';
  }
  function drawSoftware(p,w,h){
    const ry=(v,a)=>[Math.cos(a)*v[0]+Math.sin(a)*v[2],v[1],-Math.sin(a)*v[0]+Math.cos(a)*v[2]];
    const rx=(v,a)=>[v[0],Math.cos(a)*v[1]-Math.sin(a)*v[2],Math.sin(a)*v[1]+Math.cos(a)*v[2]];
    const mobile=innerWidth<600,explode=Math.sin(p*Math.PI),angle=spin+p*2.5+pointer.x*.12;
    const faces=mesh.map(face=>{
      const points=face.points.map(v=>{
        let q=[v[0],v[1]+(face.layer-3.5)*explode*.18,v[2]];
        q=rx(ry(q,(face.layer-3.5)*.17*explode),-.25+p*.45);
        q=rx(ry(q,angle),pointer.y*.08);
        q[0]+=mobile?.85:1.35;q[1]+=mobile?-.48:0;q[2]-=6.3;return q;
      });
      return {...face,points,depth:points.reduce((sum,v)=>sum+v[2],0)/points.length};
    }).sort((a,b)=>a.depth-b.depth);
    ctx.clearRect(0,0,w,h);ctx.lineWidth=Math.max(1,w/stage.clientWidth);
    for(const face of faces){
      const [a,b,c]=face.points,u=b.map((v,i)=>v-a[i]),v=c.map((n,i)=>n-a[i]);
      const n=[u[1]*v[2]-u[2]*v[1],u[2]*v[0]-u[0]*v[2],u[0]*v[1]-u[1]*v[0]],len=Math.hypot(...n)||1;
      const light=.38+Math.max(0,(-n[0]+2*n[1]+3*n[2])/len/Math.sqrt(14))*1.15;
      const t=face.layer/7,base=[55+82*t,105-22*t,180+30*t];
      ctx.fillStyle=`rgb(${base.map(x=>Math.round(x*light)).join(',')})`;
      ctx.strokeStyle=`rgba(${102+82*t},${156-23*t},${201+39*t},.96)`;
      ctx.beginPath();face.points.forEach((q,i)=>{const x=w/2+q[0]*h*1.17/-q[2],y=h/2-q[1]*h*1.17/-q[2];if(i===0)ctx.moveTo(x,y);else ctx.lineTo(x,y);});ctx.closePath();ctx.fill();ctx.stroke();
    }
  }
  function draw(p){
    if(!gl&&!ctx)return;
    const dpr=Math.min(devicePixelRatio||1,innerWidth<700?1.25:1.75),w=Math.round(stage.clientWidth*dpr),h=Math.round(stage.clientHeight*dpr);
    if(canvas.width!==w||canvas.height!==h){canvas.width=w;canvas.height=h;if(gl)gl.viewport(0,0,w,h);}
    if(ctx){drawSoftware(p,w,h);return;}
    gl.clearColor(0,0,0,0);gl.clear(gl.COLOR_BUFFER_BIT|gl.DEPTH_BUFFER_BIT);gl.useProgram(program);
    for(const [name,value] of Object.entries({uTime:spin,uProgress:p,uAspect:w/h,uMobile:innerWidth<600?1:0}))gl.uniform1f(gl.getUniformLocation(program,name),value);
    gl.uniform2f(gl.getUniformLocation(program,'uPointer'),pointer.x,pointer.y);
    function geometry(source,mode,n,wire){gl.bindBuffer(gl.ARRAY_BUFFER,source);for(const [name,size,offset] of [['aPosition',3,0],['aNormal',3,12],['aLayer',1,24]]){const at=gl.getAttribLocation(program,name);gl.enableVertexAttribArray(at);gl.vertexAttribPointer(at,size,gl.FLOAT,false,28,offset);}gl.uniform1f(gl.getUniformLocation(program,'uWire'),wire);gl.drawArrays(mode,0,n);}
    gl.enable(gl.POLYGON_OFFSET_FILL);gl.polygonOffset(1,1);geometry(buffer,gl.TRIANGLES,count,0);gl.disable(gl.POLYGON_OFFSET_FILL);geometry(wireBuffer,gl.LINES,wireCount,1);
  }
  function tick(now){
    frame=0;if(!visible||document.hidden)return;
    if(now-last<33&&!dirty){frame=requestAnimationFrame(tick);return;}
    const dt=Math.min((now-last)/1000,.05);last=now;
    const target=stopped||preference.matches?0:progress();smoothed+= (target-smoothed)*.17;if(stopped||preference.matches)smoothed=target;
    if(!stopped)spin+=dt*.10;
    choreography(smoothed);draw(smoothed);dirty=false;
    if(!stopped||Math.abs(target-smoothed)>.001)frame=requestAnimationFrame(tick);
  }
  function start(){if(!frame&&visible&&!document.hidden)frame=requestAnimationFrame(tick);}
  addEventListener('scroll',()=>{dirty=true;start();},{passive:true});addEventListener('resize',()=>{dirty=true;start();},{passive:true});
  stage.addEventListener('pointermove',event=>{if(stopped||preference.matches)return;pointer={x:(event.clientX/innerWidth-.5)*2,y:(event.clientY/innerHeight-.5)*2};dirty=true;start();},{passive:true});
  document.addEventListener('visibilitychange',()=>{if(document.hidden&&frame){cancelAnimationFrame(frame);frame=0;}else start();});
  if('IntersectionObserver'in window)new IntersectionObserver(entries=>{visible=entries[0].isIntersecting;if(!visible&&frame){cancelAnimationFrame(frame);frame=0;}else start();},{rootMargin:'100px'}).observe(journey);
  canvas.addEventListener('webglcontextlost',event=>{event.preventDefault();gl=null;journey.classList.remove('webgl-ready');});
  canvas.addEventListener('webglcontextrestored',()=>{init();dirty=true;start();});
  init();start();
})();
