console.log("toggleView.js loaded!");
document.addEventListener('DOMContentLoaded', () => {
    const listViewBtn = document.getElementById('listViewBtn');
    const gridViewBtn = document.getElementById('gridViewBtn');
    const listView = document.getElementById('listView');
    const gridView = document.getElementById('gridView');
  
    // Function to switch views
    function showListView() {
        listView.classList.add('active');
        gridView.classList.remove('active');
        listViewBtn.classList.add('active');
        gridViewBtn.classList.remove('active');
    }
    
    function showGridView() {
        gridView.classList.add('active');
        listView.classList.remove('active');
        gridViewBtn.classList.add('active');
        listViewBtn.classList.remove('active');
    }
  
    // Default to list view on page load
    showListView();
  
    // Add event listeners
    listViewBtn.addEventListener('click', showListView);
    gridViewBtn.addEventListener('click', showGridView);
});