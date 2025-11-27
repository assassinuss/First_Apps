import math

g = 9.81  # m/s^2

def from_force_and_angle(F, m, theta_deg):
    theta = math.radians(theta_deg)
    v0 = F / m
    t_up = v0 * math.sin(theta) / g
    max_height = (v0**2) * (math.sin(theta)**2) / (2 * g)
    t_flight = 2 * t_up
    range_ = (v0**2) * math.sin(2 * theta) / g
    v_impact = v0
    return {
        "range": range_,
        "max_height": max_height,
        "t_flight": t_flight,
        "t_up": t_up,
        "v0": v0,
        "v_impact": v_impact
    }

def from_range_and_angle(range_, m, theta_deg):
    theta = math.radians(theta_deg)
    v0 = math.sqrt(range_ * g / math.sin(2 * theta))
    F = v0 * m
    t_up = v0 * math.sin(theta) / g
    max_height = (v0**2) * (math.sin(theta)**2) / (2 * g)
    t_flight = 2 * t_up
    v_impact = v0
    return {
        "F": F,
        "max_height": max_height,
        "t_flight": t_flight,
        "t_up": t_up,
        "v0": v0,
        "v_impact": v_impact
    }

def from_max_height_and_angle(max_height, m, theta_deg):
    theta = math.radians(theta_deg)
    v0 = math.sqrt(2 * g * max_height) / math.sin(theta)
    F = v0 * m
    t_up = v0 * math.sin(theta) / g
    t_flight = 2 * t_up
    range_ = (v0**2) * math.sin(2 * theta) / g
    v_impact = v0
    return {
        "F": F,
        "range": range_,
        "t_flight": t_flight,
        "t_up": t_up,
        "v0": v0,
        "v_impact": v_impact
    }

def from_time_and_angle(t_flight, m, theta_deg):
    theta = math.radians(theta_deg)
    t_up = t_flight / 2
    v0 = t_up * g / math.sin(theta)
    F = v0 * m
    max_height = (v0**2) * (math.sin(theta)**2) / (2 * g)
    range_ = (v0**2) * math.sin(2 * theta) / g
    v_impact = v0
    return {
        "F": F,
        "range": range_,
        "max_height": max_height,
        "t_up": t_up,
        "v0": v0,
        "v_impact": v_impact
    }

def print_results(results):
    for k, v in results.items():
        print(f"{k}: {v:.2f}")

def menu():
    print("Space Projectile Calculator (am uitat de forta de frecare si mi-e rau) Menu:")
    print("1. Given force, mass, and angle")
    print("2. Given range, mass, and angle")
    print("3. Given max height, mass, and angle")
    print("4. Given time of flight, mass, and angle")
    choice = input("Select option (1-4): ")
    if choice == "1":
        F = float(input("Enter force (N): "))
        m = float(input("Enter mass (kg): "))
        theta = float(input("Enter launch angle (deg): "))
        results = from_force_and_angle(F, m, theta)
        print_results(results)
    elif choice == "2":
        range_ = float(input("Enter range (m): "))
        m = float(input("Enter mass (kg): "))
        theta = float(input("Enter launch angle (deg): "))
        results = from_range_and_angle(range_, m, theta)
        print_results(results)
    elif choice == "3":
        max_height = float(input("Enter max height (m): "))
        m = float(input("Enter mass (kg): "))
        theta = float(input("Enter launch angle (deg): "))
        results = from_max_height_and_angle(max_height, m, theta)
        print_results(results)
    elif choice == "4":
        t_flight = float(input("Enter time of flight (s): "))
        m = float(input("Enter mass (kg): "))
        theta = float(input("Enter launch angle (deg): "))
        results = from_time_and_angle(t_flight, m, theta)
        print_results(results)
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    menu()
