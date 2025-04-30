# solar-estimator-python
This Python tool estimates the optimal solar system size, number of panels, expected savings, and payback period based on a user's electricity usage, location, panel orientation, and cost of electricity.

## 🔧 Features

- User input prompts for daily usage, panel size, region, and direction
- Auto-calculates:
  - System size (kW)
  - Number of panels
  - Estimated annual solar production (kWh)
  - Cost savings and payback time
- Simulated ROI with federal tax incentive
- Bar chart comparing cost with vs. without solar using `matplotlib`

## 📌 Example Inputs

- Daily usage: `25 kWh`
- Panel size: `400 W`
- Location: `SoCal`
- Direction: `S`
- Cost per kWh: `$0.32`
