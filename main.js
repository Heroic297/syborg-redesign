const button = document.querySelector('.menu-button');
const navigation = document.querySelector('#navigation');
function closeMenu(){navigation.classList.remove('open');button.setAttribute('aria-expanded','false');}
button.addEventListener('click',()=>{const open=navigation.classList.toggle('open');button.setAttribute('aria-expanded',String(open));});
navigation.querySelectorAll('a').forEach(link=>link.addEventListener('click',closeMenu));
document.addEventListener('keydown',event=>{if(event.key==='Escape'&&navigation.classList.contains('open')){closeMenu();button.focus();}});
document.addEventListener('click',event=>{if(!navigation.contains(event.target)&&!button.contains(event.target))closeMenu();});
window.matchMedia('(min-width: 761px)').addEventListener('change',closeMenu);
