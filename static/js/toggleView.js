console.log("toggleView.js loaded!");
document.addEventListener('DOMContentLoaded', () => {
    const listViewBtn = document.getElementById('listViewBtn');
    const gridViewBtn = document.getElementById('gridViewBtn');
    const listView = document.getElementById('listView');
    const gridView = document.getElementById('gridView');
  
    // Ensure both views exist before adding event listeners
    if (listViewBtn && gridViewBtn && listView && gridView) {
        // Default to list view (matching your original screenshot)
        listView.classList.add('active');
        listViewBtn.classList.add('active');
  
        listViewBtn.addEventListener('click', () => {
            // Switch to list view
            listView.classList.add('active');
            gridView.classList.remove('active');
            
            // Update button active states
            listViewBtn.classList.add('active');
            gridViewBtn.classList.remove('active');
        });
    
        gridViewBtn.addEventListener('click', () => {
            // Switch to grid view
            gridView.classList.add('active');
            listView.classList.remove('active');
            
            // Update button active states
            gridViewBtn.classList.add('active');
            listViewBtn.classList.remove('active');
        });
    } else {
        console.error('Toggle view elements not found');
    }
});