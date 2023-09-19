#Enbridge
def default_schema_enbridge():
    return {
        "properties" : {
            "customer_name": {"type": "string"},
            "account_number": {"type": "string"},
            "service_address": {"type": "string"},
            "bill_date": {"type": "string"},
            "meter_reading": {"type": "array", "items": {"type": "integer"}},
            "you_used_m3": {"type": "number"},
            "billing_period": {"type": "string"},
            "billing_period_start": {"type": "string"},
            "billing_period_end": {"type": "string"},
            "balance_from_previous_bill": {"type": "number"},
            "balance_forward": {"type": "number"},
            "amount_due": {"type": "number"},
            "reversal_of_prev._billed_charges": {"type": "array", "items": {"type": "number"}, "nullable": True},
            "customer_charge": {"type": "array", "items": {"type": "number"}, "nullable": True},
            "delivery_to_you": {"type": "array", "items": {"type": "number"}, "nullable": True},
            "transportation_to_enbridge": {"type": "array", "items": {"type": "number"}, "nullable": True},
            "federal_carbon_charge": {"type": "array", "items": {"type": "number"}, "nullable": True},
            "gas_supply_charge": {"type": "array", "items": {"type": "number"}, "nullable": True},
            "cost_adjustment": {"type": "array", "items": {"type": "number"}, "nullable": True},
            "direct_purchase_admin_charge": {"type": "array", "items": {"type": "number"}, "nullable": True},
            "total_other_enbridge_charges": {"type": "array", "items": {"type": "number"}, "nullable": True},
            "charges_for_natural_gas": {"type": "number"},
            "hst": {"type": "number"},
            "total_charges_for_natural_gas": {"type": "number"},
            "source": {"type": "string", "nullable": True}
        },
        "required" : [
            "customer_name", "account_number", "service_address", "bill_date", "meter_reading", "you_used_m3", "billing_period", "billing_period_start", "billing_period_end", "balance_from_previous_bill", "balance_forward", "amount_due", "charges_for_natural_gas", "hst", "total_charges_for_natural_gas"
        ],
    }

#Alectra
def default_schema_alectra():
    return {
        "properties": {
            "customer_name": {"type": "string"},
            "account_number": {"type": "string"},
            "statement_date": {"type": "string"},
            "amount_due": {"type": "number"},
            "due_date": {"type": "string"},
            "service_location": {"type": "string"},
            "premise_number": {"type": "integer"},
            "bill_number": {"type": "integer"},
            "service_type": {"type": "array", "items": {"type": "string"}, "nullable": True},
            "meter_number": {"type": "array", "items": {"type": "integer"}, "nullable": True},
            "from_date": {"type": "array", "items": {"type": "string"}, "nullable": True},
            "to_date": {"type": "array", "items": {"type": "string"}, "nullable": True},
            "total_days": {"type": "array", "items": {"type": "integer"}, "nullable": True},
            "previous_reading": {"type": "array", "items": {"type": "number"}, "nullable": True},
            "current_reading": {"type": "array", "items": {"type": "number"}, "nullable": True},
            "read_type": {"type": "array", "items": {"type": "string"}, "nullable": True},
            "multiplier": {"type": "array", "items": {"type": "number"}, "nullable": True},
            "usage": {"type": "array", "items": {"type": "number"}, "nullable": True},
            "adjustment_factor": {"type": "array", "items": {"type": "number"}, "nullable": True},
            "adjusted_usage": {"type": "array", "items": {"type": "number"}, "nullable": True},
            "amount_of_last_bill": {"type": "number"},
            "balance_forward": {"type": "number"},
            "fire_line_charge": {"type": "array", "items": {"type": "number"}, "nullable": True},
            "total_water_fixed_charge": {"type": "array", "items": {"type": "number"}, "nullable": True},
            "total_consumption": {"type": "array", "items": {"type": "number"}, "nullable": True},
            "total_wastewater_storm_fixed_charge": {"type": "array", "items": {"type": "number"}, "nullable": True},
            "total_treatment": {"type": "array", "items": {"type": "number"}, "nullable": True},
            "total_water_and_wastewater_storm_charges": {"type": "number"}
        },
        "required": [
            "customer_name", "account_number", "statement_date", "amount_due", "due_date", "service_location", "premise_number", "bill_number", "amount_of_last_bill", "balance_forward", "total_water_and_wastewater_storm_charges"
        ],
    }












