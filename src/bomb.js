// BOMb language implementation

// Function to calculate area
@function calculateArea(width, height) {
    @return width * height;
}

// Event listener for button click
@eventListener("click", ".btn", function() {
    alert("Button clicked!");
});

// Selector for box styling
@selector(".box") {
    @property("background-color", "red");
    
    // Media query for box width
    @media("min-width: 768px") {
        @property("width", "50%");
    }
}

// Keyframes for slide-in animation
@keyframes slideIn {
    from {
        @property("transform", "translateX(-100%)");
    }
    to {
        @property("transform", "translateX(0)");
    }
}

// Selector for element animation
@selector(".element") {
    @property("animation", "slideIn 1s forwards");
  }
  
