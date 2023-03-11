
class LOT():
   class LABEL():
      SOLD_LOT_VACANT = '#4EDB4B'
      SOLD_LOT_OCCUPIED= '#2686BC'
      SOLD_LOT_CONSUMED = '#E95252'
      MONTHLY_AMORTIZATION = '#DBCD4B'
      TRANSFERRED_LOT_VACANT = '#1DB535'
      TRANSFERRED_LOT_OCCUPIED = '#D84BDB'
      TRANSFERRED_LOT_CONSUMED =  '#36A1DD'
   
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

   NUM_OF_PHASES = 2

   class PHASE_1():
      NUM_OF_LAWNS = 5
      LAWN_1_NUM_OF_LOTS = 179
      LAWN_2_NUM_OF_LOTS = 782
      LAWN_3_NUM_OF_LOTS = 400
      LAWN_4_NUM_OF_LOTS = 631
      LAWN_5_NUM_OF_LOTS = 400

   class PHASE_2():
      NUM_OF_LAWNS = 3
      LAWN_1_NUM_OF_LOTS = 250
      LAWN_2_NUM_OF_LOTS = 100
      LAWN_3_NUM_OF_LOTS = 500 

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


   STANDARD = 'STANDARD LOT'
   PRIME = 'PRIME LOT'
   SUPER_PRIME = 'SUPER PRIME LOT'
   FAMILY = 'FAMILY LOT'

   TYPES = (STANDARD, PRIME, SUPER_PRIME, FAMILY)

class PURCHASE_TYPES():
   SPOT_CASH = 'SPOT CASH'
   MONTHLY_AMORTIZATION = 'MONTHLY AMORTIZATION'
   PURCHASE_TYPES = (SPOT_CASH, MONTHLY_AMORTIZATION)

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

class SCHEDULE_TYPES():
   EVERY_LAST_DAY_OF_MONTH = 'EVERY LAST DAY OF MONTH'
   EVERY_FIRST_DAY_OF_MONTH = 'EVERY FIRST DAY OF MONTH'

   SCHEDULE_TYPES = (EVERY_FIRST_DAY_OF_MONTH, EVERY_LAST_DAY_OF_MONTH)

class MONTHLY_AMORTIZATION():
   NOT_PAID = "NOT PAID"
   PAID = 'PAID'

   FULLY_PAID = 'FULLY PAID'
   PAYING = 'PAYING'

class PAYMENT_METHODS():
   GCASH = 'GCASH'
   BANK_TRANSFER = 'BANK TRANSFER'
   CASH = 'CASH'

   PAYMENT_METHODS = (GCASH, BANK_TRANSFER, CASH)
