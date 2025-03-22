def savings(gross_pay, tax_rate, expenses):
    after_tax_pay = gross_pay - int(gross_pay * tax_rate)
    left = after_tax_pay - expenses
    return left

# 2/4

def material_waste(total_material, material_units, num_jobs, job_consumption):
    total_materials_consumed = num_jobs * job_consumption
    remaining_material = total_material - total_materials_consumed
    return f"{remaining_material}{material_units}"
#{"results": [{"expected": "85kg", "actual": "85kg", "correct?": true}, {"expected": "1lbs", "actual": "1lbs", "correct?": true}, {"expected": "2units", "actual": "2units", "correct?": true}, {"expected": "0items", "actual": "0items", "correct?": true}, {"expected": "6oz", "actual": "6oz", "correct?": true}], "max_score": 4, "actual_score": 4}
# 4/4

def interest(principal, rate, periods):
    interest_earned = principal * rate * periods
    final_value = principal + interest_earned
    return int(final_value)
# {"results": [{"expected": 13500, "actual": 13500, "correct?": true}, {"expected": 63343501, "actual": 63343501, "correct?": true}, {"expected": 111195332, "actual": 111195332, "correct?": true}, {"expected": 5450, "actual": 5450, "correct?": true}, {"expected": 15000, "actual": 15000, "correct?": true}], "max_score": 4, "actual_score": 4}
# 4/4