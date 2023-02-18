
SOLD_LOT_VACANT = 'Sold Lot (Vacant)'
SOLD_LOT_OCCUPIED = 'Sold Lot (Occupied)'
SOLD_LOT_CONSUMED = 'Sold Lot (Consumed)'
MONTHLY_AMORTIZATION = 'Monthly Amortization'
TRANSFERRED_LOT_VACANT = 'Transferred Lot (Vacant)'
TRANSFERRED_LOT_OCCUPIED = 'Transferred Lot (Occupied)'
TRANSFERRED_LOT_CONSUMED =  'Transferred Lot (Consumed)'

LOT_STATUS = (
    SOLD_LOT_VACANT, 
    SOLD_LOT_OCCUPIED,
    SOLD_LOT_CONSUMED,
    MONTHLY_AMORTIZATION,
    TRANSFERRED_LOT_VACANT,
    TRANSFERRED_LOT_OCCUPIED,
    TRANSFERRED_LOT_CONSUMED)


PROMOS = [
     {  "TYPE": "STANDARD",
        "LABEL": "Spot Cash (3 mos)",
        "IS_SPOT_CASH": True,
        "NUM_OF_MOS_TO_PAY": 3,
        "LIST_PRICE": 70000,
        "DISC_PER": 10,
        "DISC_VALUE": 63000,
        "PERP_CARE_FUND_PER": 15,
        "PERP_CARE_VALUE": 10500,
        "VAT_PER": 12,
        "VAT_VAL": 7560,
        "MONTHLY_PAY": None,
        "TOTAL": 81060
     },
     {  "TYPE": "STANDARD",
        "LABEL": "12 Months",
        "IS_SPOT_CASH": False,
        "NUM_OF_MOS_TO_PAY": 12,
        "LIST_PRICE": 70000,
        "DISC_PER": None,
        "DISC_VALUE": None,
        "PERP_CARE_FUND_PER": 15,
        "PERP_CARE_VALUE": 10500,
        "VAT_PER": 12,
        "VAT_VAL": 8400,
        "MONTHLY_PAY": 7408.33,
        "TOTAL": 88900
     },
     {  
        "TYPE": "STANDARD",
        "LABEL": "24 Months",
        "IS_SPOT_CASH": False,
        "NUM_OF_MOS_TO_PAY": 24,
        "LIST_PRICE": 70000,
        "DISC_PER": None,
        "DISC_VALUE": None,
        "PERP_CARE_FUND_PER": 15,
        "PERP_CARE_VALUE": 10500,
        "VAT_PER": 12,
        "VAT_VAL": 8400,
        "MONTHLY_PAY": 3704.17,
        "TOTAL": 88900
     },
      {  
        "TYPE": "STANDARD",
        "LABEL": "36 Months",
        "IS_SPOT_CASH": False,
        "NUM_OF_MOS_TO_PAY": 36,
        "LIST_PRICE": 70000,
        "DISC_PER": None,
        "DISC_VALUE": None,
        "PERP_CARE_FUND_PER": 15,
        "PERP_CARE_VALUE": 10500,
        "VAT_PER": 12,
        "VAT_VAL": 8400,
        "MONTHLY_PAY": 2469.44,
        "TOTAL": 88900
     },

      { "TYPE": "PREMIUM",
        "LABEL": "Spot Cash (3 mos)",
        "IS_SPOT_CASH": True,
        "NUM_OF_MOS_TO_PAY": 3,
        "LIST_PRICE": 77000,
        "DISC_PER": 10,
        "DISC_VALUE": 69300,
        "PERP_CARE_FUND_PER": 15,
        "PERP_CARE_VALUE": 11550,
        "VAT_PER": 12,
        "VAT_VAL": 8316,
        "MONTHLY_PAY": None,
        "TOTAL": 89166
     },
     {  "TYPE": "PREMIUM",
        "LABEL": "12 Months",
        "IS_SPOT_CASH": False,
        "NUM_OF_MOS_TO_PAY": 12,
        "LIST_PRICE": 77000,
        "DISC_PER": None,
        "DISC_VALUE": None,
        "PERP_CARE_FUND_PER": 15,
        "PERP_CARE_VALUE": 11550,
        "VAT_PER": 12,
        "VAT_VAL": 9240,
        "MONTHLY_PAY": 8149.17,
        "TOTAL": 97790
     },
     {  
        "TYPE": "PREMIUM",
        "LABEL": "24 Months",
        "IS_SPOT_CASH": False,
        "NUM_OF_MOS_TO_PAY": 24,
        "LIST_PRICE": 77000,
        "DISC_PER": None,
        "DISC_VALUE": None,
        "PERP_CARE_FUND_PER": 15,
        "PERP_CARE_VALUE": 11550,
        "VAT_PER": 12,
        "VAT_VAL": 9240,
        "MONTHLY_PAY": 4074.58,
        "TOTAL": 97790
     },
      {  
        "TYPE": "PREMIUM",
        "LABEL": "36 Months",
        "IS_SPOT_CASH": False,
        "NUM_OF_MOS_TO_PAY": 36,
        "LIST_PRICE": 77000,
        "DISC_PER": None,
        "DISC_VALUE": None,
        "PERP_CARE_FUND_PER": 15,
        "PERP_CARE_VALUE": 11500,
        "VAT_PER": 12,
        "VAT_VAL": 9240,
        "MONTHLY_PAY": 2716.39,
        "TOTAL": 97790
     },

     {  "TYPE": "SUPER PREMIUM",
        "LABEL": "Spot Cash (3 mos)",
        "IS_SPOT_CASH": True,
        "NUM_OF_MOS_TO_PAY": 3,
        "LIST_PRICE": 85000,
        "DISC_PER": 10,
        "DISC_VALUE": 76500,
        "PERP_CARE_FUND_PER": 15,
        "PERP_CARE_VALUE": 12750,
        "VAT_PER": 12,
        "VAT_VAL": 9180,
        "MONTHLY_PAY": None,
        "TOTAL": 98430
     },
     {  "TYPE": "SUPER PREMIUM",
        "LABEL": "12 Months",
        "IS_SPOT_CASH": False,
        "NUM_OF_MOS_TO_PAY": 12,
        "LIST_PRICE": 85000,
        "DISC_PER": None,
        "DISC_VALUE": None,
        "PERP_CARE_FUND_PER": 15,
        "PERP_CARE_VALUE": 12750,
        "VAT_PER": 12,
        "VAT_VAL": 10200,
        "MONTHLY_PAY": 8995.83,
        "TOTAL": 107950
     },
     {  
        "TYPE": "SUPER PREMIUM",
        "LABEL": "24 Months",
        "IS_SPOT_CASH": False,
        "NUM_OF_MOS_TO_PAY": 24,
        "LIST_PRICE": 85000,
        "DISC_PER": None,
        "DISC_VALUE": None,
        "PERP_CARE_FUND_PER": 15,
        "PERP_CARE_VALUE": 12750,
        "VAT_PER": 12,
        "VAT_VAL": 10200,
        "MONTHLY_PAY": 4497.92,
        "TOTAL": 107950
     },
      {  
        "TYPE": "SUPER PREMIUM",
        "LABEL": "36 Months",
        "IS_SPOT_CASH": False,
        "NUM_OF_MOS_TO_PAY": 36,
        "LIST_PRICE": 85000,
        "DISC_PER": None,
        "DISC_VALUE": None,
        "PERP_CARE_FUND_PER": 15,
        "PERP_CARE_VALUE": 12750,
        "VAT_PER": 12,
        "VAT_VAL": 10200,
        "MONTHLY_PAY": 2998.61,
        "TOTAL": 107950
     },
]


STANDARD = 'STANDARD'
PRIME = 'PRIME'
SUPRIME = 'SUPRIME'
FAMILY = 'FAMILY'

TYPES = (STANDARD, PRIME, SUPRIME, FAMILY)

ONE_TIME_PAYMENT = 'ONE TIME PAYMENT'
MONTHLY_AMORTIZATION = 'MONTHLY AMORTIZATION'

PURCHASE_TYPES = (ONE_TIME_PAYMENT, MONTHLY_AMORTIZATION)

NEWS = '''
### Comming Soon
* Crematory Services
* Virtual Funeral
* Mortuary Services
* Columbarium

### Comming Soon
This is paragraphs  simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.

1. sfdfsdfsdf
3. sdfsdf

### Second Section 
This is paragraphs  simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not.

only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.
'''