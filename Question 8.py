"""Question 8
● Title: Pesticide Database Query
● Question: Store information about pesticides in a dictionary where keys are trade
names. The values should be another dictionary containing details like
'active_ingredient' and 'application_rate'. Write a script to print all pesticide trade
names that have 'Glyphosate' as their active ingredient."""


pesticides = {
    'Roundup': {'active_ingredient': 'Glyphosate', 'application_rate': '2L/ha'},
    'WeedAway': {'active_ingredient': 'Paraquat', 'application_rate': '1.5L/ha'},
    'ClearField': {'active_ingredient': 'Glyphosate', 'application_rate': '2.5L/ha'},
    'Spraying': {'active_ingredient':'Glyphosate','application_rate': '1.5L/ha'}
}

print("Pesticides with Glyphosate as active ingredient are :")
for trade_name, details in pesticides.items():
    if details['active_ingredient'] == 'Glyphosate':
        print(trade_name)