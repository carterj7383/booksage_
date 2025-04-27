
console.log("toggleView.js loaded!");
document.addEventListener('DOMContentLoaded', () => {
    const listViewBtn = document.getElementById('listViewBtn');
    const gridViewBtn = document.getElementById('gridViewBtn');
    const listView = document.getElementById('listView');
    const gridView = document.getElementById('gridView');
  
    // Function to switch views
    function showListView() {
        // Hide grid view first
        gridView.style.display = 'none';
        // Then show list view
        listView.style.display = 'block';
        
        // Update button active states
        listViewBtn.classList.add('active');
        gridViewBtn.classList.remove('active');
    }
    
    function showGridView() {
        // Hide list view first
        listView.style.display = 'none';
        // Then show grid view with grid display
        gridView.style.display = 'grid';
        
        // Update button active states
        gridViewBtn.classList.add('active');
        listViewBtn.classList.remove('active');
    }
  
    // Default to list view on page load
    showListView();
  
    // Add event listeners
    listViewBtn.addEventListener('click', showListView);
    gridViewBtn.addEventListener('click', showGridView);
});