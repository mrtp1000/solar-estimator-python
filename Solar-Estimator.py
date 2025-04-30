import matplotlib.pyplot as plt


def solar_estimator():
    print("Welcome to my solar Estimator, Let's quickly estimate what are your solar needs!!!!")

    daily_kwh = float(input("Could you give me an estimated daily energy usage in kwh?"))
    panelsize=float(input("How about the size of your panels in Watts?"))


    location=input("Where are you located? (NorCal, SoCal or Phoenix)?").lower()
    

    if "norcal" in location:
        sun_hour=4

    elif "socal" in location:
        sun_hour=5.5

    elif "phoenix" in location:
        sun_hour=8;
    else:
        print("❗ Invalid city. Please enter one of the following: (NorCal, SoCal or Phoenix)?")
        return

    direction=input("Where are you going to place you panels (N,S,W,E)?").upper()

    if "N" in direction:
        efficiency=.75

    elif "W" in direction:
        efficiency=.9

    elif "E" in direction:
        efficiency=.9;
    elif "S" in direction:
        efficiency=1;
    
    else:
        print("❗ Invalid direction. Please enter one of the following: (N,S,W,E)")
        return
    
    cost=float(input("What is the average cost per kwh in your city? "))


    #calculation

    system_kw=daily_kwh/(sun_hour*efficiency)
    num_panels = round((system_kw*1000)/panelsize)

    without_cost= daily_kwh * 365*cost
    annual_production_kwh = system_kw * sun_hour * efficiency * 365 
    with_solar_cost = (daily_kwh * 365 - annual_production_kwh) * cost
    savings = without_cost - with_solar_cost

    # Estimated system cost (before incentives)
    cost_per_watt = 3.00  # You can adjust this
    gross_cost = system_kw * 1000 * cost_per_watt

    # Net cost after 30% tax credit
    tax_credit = 0.30
    net_cost = gross_cost * (1 - tax_credit)

    # Payback period and ROI
    payback_years = net_cost / savings if savings > 0 else float('inf')
    roi = (savings / net_cost) * 100 if net_cost > 0 else 0

        # Output
    print("\n✅ ESTIMATION RESULTS")
    print(f"📍 Location: {location.title()}, Facing: {direction}")
    print(f"☀️ Sun Hours/Day (adjusted): {sun_hour * efficiency:.2f}")
    print(f"🔋 Required System Size: {system_kw:.2f} kW")
    print(f"📦 Approx. Number of Panels: {num_panels} × {int(panelsize)}W")
    print(f" Cost without Solar Per Year: ${without_cost:,.2f}")
    print(f" Cost With Solar Per Year: ${with_solar_cost:,.2f}")
    print(f" Savings Each Year: ${savings:,.2f}")
    print(f"🧾 Estimated System Cost (Net after 30% tax incentive): ${net_cost:,.2f}")
    print(f"⏳ Payback Period: {payback_years:.1f} years")
    print(f"📈 Estimated ROI: {roi:.1f}%")



    plt.bar(["Without Solar", "With Solar"], [without_cost, with_solar_cost], color=["#FF6B6B", "#4ECDC4"])
    plt.title("Annual Electricity Cost Comparison")
    plt.ylabel("Cost ($)")
    plt.tight_layout()
    plt.grid(axis='y')
    plt.show()



solar_estimator()

