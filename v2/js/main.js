(function(){
  const burger = document.querySelector('[data-burger]');
  const nav = document.querySelector('[data-nav]');
  if (burger && nav) {
    burger.addEventListener('click', () => {
      const open = nav.classList.toggle('open');
      burger.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
  }
  document.querySelectorAll('[data-gallery]').forEach(root => {
    const main = root.querySelector('[data-gallery-main]');
    root.querySelectorAll('[data-thumb]').forEach(btn => {
      btn.addEventListener('click', () => {
        const src = btn.getAttribute('data-thumb');
        if (main && src) {
          main.src = src;
          root.querySelectorAll('[data-thumb]').forEach(b => b.setAttribute('aria-current','false'));
          btn.setAttribute('aria-current','true');
        }
      });
    });
  });
})();
