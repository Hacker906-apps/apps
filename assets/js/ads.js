/* Ad network placements. Scripts are inserted once per page; keep the supplied URLs unchanged. */
(function(){
  const slots = document.querySelectorAll('[data-ad-slot]');
  if (!slots.length) return;
  function addScript(src, attrs={}) { const s=document.createElement('script'); s.src=src; Object.entries(attrs).forEach(([k,v])=>s.setAttribute(k,v)); document.head.appendChild(s); }
  // Native ad unit: displayed in the reserved collection/detail placement.
  const native=document.querySelector('[data-ad-slot="native"]');
  if(native){const box=document.createElement('div');box.id='container-6cd227031ab99d74dff79fa724a095bd';native.appendChild(box);addScript('https://pl31745653.profitableratecpmnetwork.com/6cd227031ab99d74dff79fa724a095bd/invoke.js',{'async':'async','data-cfasync':'false'});}
  // 320x50 banner. Keep it inside a labeled ad slot, away from download controls.
  const banner=document.querySelector('[data-ad-slot="banner"]');
  if(banner){window.atOptions={key:'9c9b77fad1fef8bf1af2dfdfe4c46233',format:'iframe',height:50,width:320,params:{}};addScript('https://www.highrevenueformat.com/9c9b77fad1fef8bf1af2dfdfe4c46233/invoke.js');}
  // Other supplied Adsterra scripts are placed in a dedicated below-content slot.
  const other=document.querySelector('[data-ad-slot="other"]');
  if(other){addScript('https://pl31745651.profitableratecpmnetwork.com/f2/ca/23/f2ca23cfdf5e27c3a73077cad75d2ceb.js');addScript('https://pl31745654.profitableratecpmnetwork.com/ac/8b/49/ac8b4931a348ed13d58994331be824c9.js');const link=document.createElement('a');link.href='https://www.profitableratecpmnetwork.com/h80ei4jea?key=18e23cc122128bffebe9af53c84e8447';link.target='_blank';link.rel='sponsored noopener noreferrer';link.textContent='Sponsored link';link.style.cssText='display:inline-block;margin:14px auto 10px;color:var(--muted);font-size:10px;text-decoration:underline;';other.appendChild(link);}
  // The direct-link URL is shown only as a clearly labeled, user-initiated sponsored link.
})();
