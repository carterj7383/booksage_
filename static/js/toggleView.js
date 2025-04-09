console.log("toggleView.js loaded!");
document.addEventListener('DOMContentLoaded', () => {
    const listViewBtn = document.getElementById('listViewBtn');
    const gridViewBtn = document.getElementById('gridViewBtn');
    const listView = document.getElementById('listView');
    const gridView = document.getElementById('gridView');
  
    // Default to list view
    listView.style.display = 'block';
    gridView.style.display = 'none';
    listViewBtn.classList.add('active');
  
    listViewBtn.addEventListener('click', () => {
      // Show list view
      listView.style.display = 'block';
      gridView.style.display = 'none';
      
      // Update button active states
      listViewBtn.classList.add('active');
      gridViewBtn.classList.remove('active');
    });
  
    gridViewBtn.addEventListener('click', () => {
      // Show grid view
      gridView.style.display = 'block';
      listView.style.display = 'none';
      
      // Update button active states
      gridViewBtn.classList.add('active');
      listViewBtn.classList.remove('active');
    });
});