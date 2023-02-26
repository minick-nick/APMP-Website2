from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TelField, EmailField, TextAreaField, IntegerField, DateField, SelectField, FloatField, SearchField
from wtforms.validators import Email, DataRequired, ValidationError
from apmp.models import Client
from apmp import CONSTANTS
from apmp.db_helper import get_lots, get_downpayment_promos
import datetime

class LoginFormClient(FlaskForm):
    client_id = StringField(label='Client ID', validators=[DataRequired()])
    password = PasswordField(label='Password', validators=[DataRequired()])
    submit = SubmitField(label='Log In')

class LoginFormAdmin(FlaskForm):
    username= StringField(label='Username', validators=[DataRequired()])
    password = PasswordField(label='Password', validators=[DataRequired()])
    submit = SubmitField(label='Log In')

class AddClientForm(FlaskForm):
    # for personal information of client
    first_name= StringField(label='First Name', validators=[DataRequired()])
    middle_name= StringField(label='Middle Name', validators=[DataRequired()])
    last_name= StringField(label='Last Name', validators=[DataRequired()])
    email = EmailField(label="Email", validators=[DataRequired(), Email()])
    mobile_number = StringField(label="Mobile Number", validators=[DataRequired()])
    address = StringField(label="Address", validators=[DataRequired()])
    birth_date = DateField(label="Birth Date", validators=[DataRequired()])
    name_of_spouse = StringField(label="Name of spouse", validators=[DataRequired()])
    password = PasswordField(label='Password', validators=[DataRequired()])
    
    # lot information
    phase_number = IntegerField(label='Phase number', validators=[DataRequired()])
    lawn_number = IntegerField(label='Lawn number', validators=[DataRequired()])
    lot_number = IntegerField(label='Lot number', validators=[DataRequired()])
    lot_types = SelectField(label='Lot type', choices=CONSTANTS.LOT.TYPES)
    lot_status = SelectField(label='Status', choices=CONSTANTS.LOT.LOT_STATUS)

    # lot purchase informations
    purchase_type = SelectField(label='Purchase type', choices= CONSTANTS.PURCHASE_TYPES.PURCHASE_TYPES)
    spot_cash_promo = SelectField(label='Spot cash promo', choices=get_downpayment_promos(True))
    monthly_amortization_promo = SelectField(label='Monthly amortization promo',  choices=get_downpayment_promos(False))
    # lot_price = FloatField(label='Lot price', validators=[DataRequired()])
    # monthly amortization details
    # down_payment_type = StringField(label='Down payment type', choices=)

    # monthly amortization payment schedule
    schedule_types = SelectField(label='Payment schedule type', choices=CONSTANTS.SCHEDULE_TYPES.SCHEDULE_TYPES)
    date_start = DateField(label='Payment date start')
    submit = SubmitField(label='Save')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not self.date_start.data:
            self.date_start.data = datetime.date.today()

    def validate_phase_number(self, phase_number):
        if int(phase_number.data) > CONSTANTS.LOT.NUM_OF_PHASES or int(phase_number.data) < 1:
            raise ValidationError(f"Invalid phase number. Pleaese select phase number between 1 and { CONSTANTS.LOT.NUM_OF_PHASES} only.")

    def validate_lawn_number(self, lawn_number):
        if int(self.phase_number.data) == 1:
            if int(lawn_number.data) > CONSTANTS.LOT.PHASE_1.NUM_OF_LAWNS or int(lawn_number.data) < 1:
                raise ValidationError(f"Invalid lawn number. Phase 1 have only {CONSTANTS.LOT.PHASE_1.NUM_OF_LAWNS} lawns. Pleaese select lawn number between 1 and { CONSTANTS.LOT.PHASE_1.NUM_OF_LAWNS } only.")
        elif int(self.phase_number.data) == 2:
            if int(lawn_number.data) > CONSTANTS.LOT.PHASE_2.NUM_OF_LAWNS or int(lawn_number.data) < 1:
                raise ValidationError(f"Invalid lawn number. Phase 2 have only {CONSTANTS.LOT.PHASE_2.NUM_OF_LAWNS} lawns. Pleaese select lawn number between 1 and { CONSTANTS.LOT.PHASE_2.NUM_OF_LAWNS } only.")

        else:
            raise ValidationError(f"Invalid phase number. Pleaese select phase number between 1 and { CONSTANTS.LOT.NUM_OF_PHASES} only.")
    
    def validate_lot_number(self, lot_number):
        if int(self.phase_number.data) == 1:
            if self.lawn_number.data == 1:
                if lot_number.data in [lot_num for id, lot_num, status in get_lots(1, 1, False)]:
                    raise ValidationError(f"Lot {lot_number.data} is not vailable in lawn 1 at phase 1")
            if self.lawn_number.data == 2:
                if lot_number.data in [lot_num for id, lot_num, status in get_lots(1, 2, False)]:
                    raise ValidationError(f"Lot {lot_number.data} is not vailable in lawn 2 at phase 1")
                
            if self.lawn_number.data == 3:
                if lot_number.data in [lot_num for id, lot_num, status in get_lots(1, 3, False)]:
                    raise ValidationError(f"Lot {lot_number.data} is not vailable in lawn 3 at phase 1")

            if self.lawn_number.data == 4:
                if lot_number.data in [lot_num for id, lot_num, status in get_lots(1, 4, False)]:
                    raise ValidationError(f"Lot {lot_number.data} is not vailable in lawn 4 at phase 1")
                
            if self.lawn_number.data == 5:
                if lot_number.data in [lot_num for id, lot_num, status in get_lots(1, 5, False)]:
                    raise ValidationError(f"Lot {lot_number.data} is not vailable in lawn 5 at phase 1")
        
        elif int(self.phase_number.data) == 2:
            if self.lawn_number.data == 1:
                if lot_number.data in [lot_num for id, lot_num, status in get_lots(2, 1, False)]:
                    raise ValidationError(f"Lot {lot_number.data} is not vailable in lawn 1 at phase 2")
                
            if self.lawn_number.data == 2:
                if lot_number.data in [lot_num for id, lot_num, status in get_lots(2, 2, False)]:
                    raise ValidationError(f"Lot {lot_number.data} is not vailable in lawn 2 at phase 2")
                
            if self.lawn_number.data == 3:
                if lot_number.data in [lot_num for id, lot_num, status in get_lots(2, 3, False)]:
                    raise ValidationError(f"Lot {lot_number.data} is not vailable in lawn 3 at phase 2")


    # to-do: make validation for lawn number and lot number
    def validate_email(self, email):
        email_found = Client.query.filter_by(email=email.data).first()

        if email_found:
            raise ValidationError('Email already exists! Please try a different email.')

    def validate_mobile_number(self, mobile_number):
        mobile_number_found = Client.query.filter_by(mobile_number=mobile_number.data).first()

        if mobile_number_found:
            raise ValidationError('Mobile number already exists! Please try a different mobile number.')
            
class MessageForm(FlaskForm):
    name = StringField(label='Name', validators=[DataRequired()])
    email = EmailField(label='Email', validators=[DataRequired(), Email()])
    contact_number = TelField(label='Contact number', validators=[DataRequired()])
    message = TextAreaField(label='Message', validators=[DataRequired()])
    submit = SubmitField(label='Send')

class LotPromoForm(FlaskForm):
    label = StringField(label='Label', validators=[DataRequired()])
    num_of_mos_to_pay = IntegerField(label='Number of months to pay', validators=[DataRequired()])
    list_price = FloatField(label='Price', validators=[DataRequired()])
    disc_per = IntegerField(label='Discount percentage', validators=[DataRequired()])
    disc_value = FloatField(label='Discount value', validators=[DataRequired()])
    perp_care_fund_per = IntegerField(label='Perpetual care fund percentage', validators=[DataRequired()])
    perp_care_value = FloatField(label='Perpetual care', validators=[DataRequired()])
    vat_per = IntegerField(label='Vat percentage', validators=[DataRequired()])
    vat_val = FloatField(label='Vat value', validators=[DataRequired()])
    total = FloatField(label='Total', validators=[DataRequired()])
    monthly_pay = FloatField(label='Monthly payment', validators=[DataRequired()])
    submit = SubmitField(label='Save')

class NewsContentForm(FlaskForm):
    md_code = TextAreaField(label='Input content of news page', validators=[DataRequired()])
    save = SubmitField(label='Save')

class SearchClientForm(FlaskForm):
    name_to_search = SearchField(validators=[DataRequired()])
    search = SubmitField(label='Search')

class PayMonthlyAmortizationForm(FlaskForm):
    amount_paid = FloatField(label="Amount paid", validators=[DataRequired()])
    payment_methods = SelectField(label="Payment method", choices=CONSTANTS.PAYMENT_METHODS.PAYMENT_METHODS)
    # paid_for_the_month_of = SelectField(label="Pay for the month of", choices=['June', 'July']) # for bulk payment
    confirm = SubmitField(label='Confirm')

class AddClientLotForm(FlaskForm):
    # lot information
    phase_number = IntegerField(label='Phase number', validators=[DataRequired()])
    lawn_number = IntegerField(label='Lawn number', validators=[DataRequired()])
    lot_number = IntegerField(label='Lot number', validators=[DataRequired()])
    lot_types = SelectField(label='Lot type', choices=CONSTANTS.LOT.TYPES)
    lot_status = SelectField(label='Status', choices=CONSTANTS.LOT.LOT_STATUS)

    # lot purchase informations
    purchase_type = SelectField(label='Purchase type', choices= CONSTANTS.PURCHASE_TYPES.PURCHASE_TYPES)
    spot_cash_promo = SelectField(label='Spot cash promo', choices=get_downpayment_promos(True))
    monthly_amortization_promo = SelectField(label='Monthly amortization promo',  choices=get_downpayment_promos(False))

    schedule_types = SelectField(label='Payment schedule type', choices=CONSTANTS.SCHEDULE_TYPES.SCHEDULE_TYPES)
    date_start = DateField(label='Payment date start', validators=[DataRequired()])

    submit = SubmitField(label='Save')

    def validate_phase_number(self, phase_number):
        if int(phase_number.data) > CONSTANTS.LOT.NUM_OF_PHASES or int(phase_number.data) < 1:
            raise ValidationError(f"Invalid phase number. Pleaese select phase number between 1 and { CONSTANTS.LOT.NUM_OF_PHASES} only.")

    def validate_lawn_number(self, lawn_number):
        if int(self.phase_number.data) == 1:
            if int(lawn_number.data) > CONSTANTS.LOT.PHASE_1.NUM_OF_LAWNS or int(lawn_number.data) < 1:
                raise ValidationError(f"Invalid lawn number. Phase 1 have only {CONSTANTS.LOT.PHASE_1.NUM_OF_LAWNS} lawns. Pleaese select lawn number between 1 and { CONSTANTS.LOT.PHASE_1.NUM_OF_LAWNS } only.")
        elif int(self.phase_number.data) == 2:
            if int(lawn_number.data) > CONSTANTS.LOT.PHASE_2.NUM_OF_LAWNS or int(lawn_number.data) < 1:
                raise ValidationError(f"Invalid lawn number. Phase 2 have only {CONSTANTS.LOT.PHASE_2.NUM_OF_LAWNS} lawns. Pleaese select lawn number between 1 and { CONSTANTS.LOT.PHASE_2.NUM_OF_LAWNS } only.")

        else:
            raise ValidationError(f"Invalid phase number. Pleaese select phase number between 1 and { CONSTANTS.LOT.NUM_OF_PHASES} only.")
    
    def validate_lot_number(self, lot_number):
        if int(self.phase_number.data) == 1:
            if self.lawn_number.data == 1:
                if lot_number.data in [lot_num for id, lot_num, sta in get_lots(1, 1, False)]:
                    raise ValidationError(f"Lot {lot_number.data} is not available in lawn 1 at phase 1")
            if self.lawn_number.data == 2:
                if lot_number.data in [lot_num for id, lot_num, sta in get_lots(1, 2, False)]:
                    raise ValidationError(f"Lot {lot_number.data} is not available in lawn 2 at phase 1")
                
            if self.lawn_number.data == 3:
                if lot_number.data in [lot_num for id, lot_num, sta in get_lots(1, 3, False)]:
                    raise ValidationError(f"Lot {lot_number.data} is not available in lawn 3 at phase 1")

            if self.lawn_number.data == 4:
                if lot_number.data in [lot_num for id, lot_num, sta in get_lots(1, 4, False)]:
                    raise ValidationError(f"Lot {lot_number.data} is not available in lawn 4 at phase 1")
                
            if self.lawn_number.data == 5:
                if lot_number.data in [lot_num for id, lot_num, sta in get_lots(1, 5, False)]:
                    raise ValidationError(f"Lot {lot_number.data} is not available in lawn 5 at phase 1")
        
        elif int(self.phase_number.data) == 2:
            if self.lawn_number.data == 1:
                if lot_number.data in [lot_num for id, lot_num, sta in get_lots(2, 1, False)]:
                    raise ValidationError(f"Lot {lot_number.data} is not available in lawn 1 at phase 2")
                
            if self.lawn_number.data == 2:
                if lot_number.data in [lot_num for id, lot_num, sta in get_lots(2, 2, False)]:
                    raise ValidationError(f"Lot {lot_number.data} is not available in lawn 2 at phase 2")
                
            if self.lawn_number.data == 3:
                if lot_number.data in [lot_num for id, lot_num, sta in get_lots(2, 3, False)]:
                    raise ValidationError(f"Lot {lot_number.data} is not available in lawn 3 at phase 2")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not self.date_start.data:
            self.date_start.data = datetime.date.today()


    def validate_phase_number(self, phase_number):
        if int(phase_number.data) < 1 or int(phase_number.data) > 2:
            raise ValidationError("Invalid phase number. Pleaese select phase number between 1 and 2 only.")

            