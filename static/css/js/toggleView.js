console.log("toggleView.js loaded!");
document.addEventListener('DOMContentLoaded', () => {
    const listViewBtn = document.getElementById('listViewBtn');
    const gridViewBtn = document.getElementById('gridViewBtn');
    const listView = document.getElementById('listView');
    const gridView = document.getElementById('gridView');
  
    listViewBtn.addEventListener('click', () => {
      listView.style.display = 'block';
      gridView.style.display = 'none';
      listViewBtn.classList.add('active');
      gridViewBtn.classList.remove('active');
    });
  
    gridViewBtn.addEventListener('click', () => {
      gridView.style.display = 'grid'; // or 'block' depending on your CSS
      listView.style.display = 'none';
      gridViewBtn.classList.add('active');
      listViewBtn.classList.remove('active');
    });
  });
  