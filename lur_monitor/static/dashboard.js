/* Created bt Tivotal */

const btn = document.querySelector(".btn-select");
const items = document.querySelectorAll(".item");
btn.addEventListener("click", () => {
  btn.classList.toggle("open");
});
function updateCalendar() {
  const calendarInterval = document.getElementById("calendarInterval").value;
  const calendarContainer = document.getElementById("calendar");

  // Clear previous calendar content
  calendarContainer.innerHTML = "";

  // Get the current date
  const currentDate = new Date();

  if (calendarInterval === "current") {
      // Display current date
      calendarContainer.innerHTML = currentDate.toDateString();
  } else if (calendarInterval === "weekly") {
      // Display weekly calendar
    
          const day = new Date(currentDate);
          day.setDate(currentDate.getDate() + 7); 
          calendarContainer.innerHTML += `<div>${currentDate.toDateString()}-${day.toDateString()}</div>`;
          
  } else if (calendarInterval === "monthly") {
      // Display monthly calendar
      const day = new Date(currentDate);
      day.setDate(currentDate.getDate() + 31); 
      calendarContainer.innerHTML += `<div>${currentDate.toDateString()}-${day.toDateString()}</div>`;
      
  }
  
}

// Initial calendar update
updateCalendar();


