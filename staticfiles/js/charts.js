// Get the canvas
const ctx = document.getElementById("usageChart").getContext("2d");

// Dummy Data
const dailyData = {
  labels: ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
  datasets: [{
    label: "Daily Usage (kWh)",
    data: [12, 19, 7, 15, 10, 5, 8],
    backgroundColor: "rgba(54, 162, 235, 0.6)"
  }]
};

const weeklyData = {
  labels: ["Week 1", "Week 2", "Week 3", "Week 4"],
  datasets: [{
    label: "Weekly Usage (kWh)",
    data: [80, 95, 70, 100],
    borderColor: "rgba(255, 99, 132, 1)",
    backgroundColor: "rgba(255, 99, 132, 0.2)",
    tension: 0.4,
    fill: true
  }]
};

const monthlyData = {
  labels: ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
  datasets: [{
    label: "Monthly Usage (kWh)",
    data: [300, 250, 400, 350, 280, 500],
    backgroundColor: [
      "rgba(255, 99, 132, 0.6)",
      "rgba(54, 162, 235, 0.6)",
      "rgba(255, 206, 86, 0.6)",
      "rgba(75, 192, 192, 0.6)",
      "rgba(153, 102, 255, 0.6)",
      "rgba(255, 159, 64, 0.6)"
    ]
  }]
};

// Default Chart (Daywise)
let usageChart = new Chart(ctx, {
  type: "bar",
  data: dailyData,
  options: { responsive: true }
});

// Handle dropdown change
document.getElementById("chartType").addEventListener("change", function () {
  const selected = this.value;

  usageChart.destroy(); // Destroy old chart

  if (selected === "day") {
    usageChart = new Chart(ctx, { type: "bar", data: dailyData, options: { responsive: true } });
  } else if (selected === "week") {
    usageChart = new Chart(ctx, { type: "line", data: weeklyData, options: { responsive: true } });
  } else if (selected === "month") {
    usageChart = new Chart(ctx, { type: "pie", data: monthlyData, options: { responsive: true } });
  }
});
