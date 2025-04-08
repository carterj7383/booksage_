console.log("toggleView.js loaded!");
document.addEventListener('DOMContentLoaded', () => {
    const listViewBtn = document.getElementById('listViewBtn');
    const gridViewBtn = document.getElementById('gridViewBtn');
    const listView = document.getElementById('listView');
    const gridView = document.getElementById('gridView');
  
    listViewBtn.addEventListener('click', () => {
      // Show list view
      listView.classList.add('active');
      listView.style.display = 'block';
      
      // Hide grid view
      gridView.classList.remove('active');
      gridView.style.display = 'none';
      
      // Update button active states
      listViewBtn.classList.add('active');
      gridViewBtn.classList.remove('active');
    });
  
    gridViewBtn.addEventListener('click', () => {
      // Show grid view
      gridView.classList.add('active');
      gridView.style.display = 'grid';
      
      // Hide list view
      listView.classList.remove('active');
      listView.style.display = 'none';
      
      // Update button active states
      gridViewBtn.classList.add('active');
      listViewBtn.classList.remove('active');
    });
});