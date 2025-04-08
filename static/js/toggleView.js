console.log("toggleView.js loaded!");
document.addEventListener('DOMContentLoaded', () => {
    const listViewBtn = document.getElementById('listViewBtn');
    const gridViewBtn = document.getElementById('gridViewBtn');
    const listView = document.getElementById('listView');
    const gridView = document.getElementById('gridView');
  
    // Default to grid view
    gridView.classList.add('active');
    gridViewBtn.classList.add('active');
  
    listViewBtn.addEventListener('click', () => {
      // Show list view
      listView.classList.add('active');
      gridView.classList.remove('active');
      
      // Update button active states
      listViewBtn.classList.add('active');
      gridViewBtn.classList.remove('active');
    });
  
    gridViewBtn.addEventListener('click', () => {
      // Show grid view
      gridView.classList.add('active');
      listView.classList.remove('active');
      
      // Update button active states
      gridViewBtn.classList.add('active');
      listViewBtn.classList.remove('active');
    });
});