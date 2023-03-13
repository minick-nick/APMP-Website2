from apmp import CONSTANTS, app, db, mail
from apmp.models import Client, Admin, Lot, VisitorMessage, LotPromo, NewsContent, LotPurchaseDetail, MonthlyAmortization, PaymentHistory, AvailableAndNotAvailbaleLots, login_manager
from flask import render_template, redirect, url_for, request, flash
from flask_login import login_user, login_required
from apmp.forms import AddClientForm, LotPromoForm, LotPromoForm,NewsContentForm, SearchClientForm, PayMonthlyAmortizationForm, AddClientLotForm, SendEmailForm
from markdown import markdown
from apmp.util import modify_html_code, generate_payment_schedule, con_receipt_to_image, generate_client_id
from apmp.util import Dashboard
from datetime import datetime
import json
from apmp.db_helper import make_lot_unavail, get_lots, get_all_lots
from flask_mail import Message

@app.route('/admin')
@app.route('/admin/dashboard')
@login_required
def admin():
    dash = Dashboard()
    return render_template('admin/dashboard.html', dash=dash)

@app.route('/admin/clients', methods=['GET', 'POST'])
@login_required
def clients():
    clients = Client.query.all()
    search_bar = SearchClientForm()

    if request.method == 'POST':
        if search_bar.validate_on_submit:
            keyword = search_bar.name_to_search.data

            found_fname = Client.query.filter_by(first_name=keyword)
            found_lname = Client.query.filter_by(last_name=keyword)
            found_email = Client.query.filter_by(email=keyword)

            clients_found = None

            if found_fname.first():
                clients_found = found_fname
            elif found_lname.first():
                clients_found = found_lname
            elif found_email.first():
                clients_found = found_email

            if clients_found:
                clients = clients_found
                print(clients.first())
            else:
                print("Client not found")
                flash(f'{keyword} not found', category='warning')


    return render_template('admin/clients.html', clients=clients, search_bar=search_bar)

@app.route('/admin/queries/visitors', methods=['GET', 'POST'])
@login_required
def visitors_queries():
    send_email_form = SendEmailForm()

    if request.method == 'POST':
        if send_email_form.validate_on_submit:
            r = send_email_form.recepient.data
            s = send_email_form.subject.data
            msg = send_email_form.message.data

            sender = 'dominicdofredo16@gmail.com'
            message = Message(sender=sender, recipients=[r], subject=s)
            message.body = msg
            mail.send(message)

            client_msg = VisitorMessage.query.filter_by(email=r).first()

            if client_msg:
                client_msg.replied = True
                db.session.commit()
            

            flash(f'Message sent', category='successs')


            return redirect(url_for('visitors_queries'))

    visitors_msgs = VisitorMessage.query.all()

    for visitor_msg in visitors_msgs:
        visitor_msg.date_received = str(visitor_msg.date_received).split()[0]

    return render_template('admin/queries/visitors.html', visitors_msgs=visitors_msgs, send_email_form=send_email_form)

@app.route('/admin/lot_image_request')
@login_required
def lot_image_request():
    return render_template('admin/lot_image_request.html')

@app.route('/admin/map')
@login_required
def map():
    label = CONSTANTS.LOT.LABEL
    status = CONSTANTS.LOT

    p1l3_lots = get_all_lots(1,3)
    p1l4_lots = get_all_lots(1,4)
    p1l5_lots = get_all_lots(1,5)
    p2l1_lots = get_all_lots(2, 1)
    p2l2_lots = get_all_lots(2, 2)
    p2l3_lots = get_all_lots(2, 3)


    all_lots_occupied = Lot.query.all()
 
    
    return render_template('admin/map.html',
                          p1l3_lots = p1l3_lots,
                           p1l5_lots = p1l5_lots,
                            p2l1_lots = p2l1_lots,
                             p2l2_lots = p2l2_lots,
                              p2l3_lots = p2l3_lots,
                           LABEL=label,
                           STATUS=status, 
                           all_all_lots=all_lots_occupied)

@app.route('/admin/add_client', methods=['GET', 'POST'])
@login_required
def add_client():
    add_client_form = AddClientForm()

    if request.method == 'POST':
        if add_client_form.validate_on_submit():
            client = Client()
            client_lot = Lot()
            purchase_detail = LotPurchaseDetail()
            monthly_amortization = MonthlyAmortization()

            
            client.first_name = add_client_form.first_name.data
            client.middle_name = add_client_form.middle_name.data
            client.last_name = add_client_form.last_name.data
            client.email = add_client_form.email.data
            client.mobile_number = add_client_form.mobile_number.data
            client.address = add_client_form.address.data
            client.birth_date = add_client_form.birth_date.data
            client.name_of_spouse = add_client_form.name_of_spouse.data
            client.client_id = generate_client_id()
            client.password = add_client_form.password.data
            
            db.session.add(client)
            db.session.commit()

            # if the client table is empty 
            # if Client.query.filter_by(client_id=CLIENT_ID_START).first() == None:
            #    client.client_id = CLIENT_ID_START


            #bridge
            phase_number = add_client_form.phase_number.data
            lawn_number = add_client_form.lawn_number.data
            lot_number = add_client_form.lot_number.data

            client_lot.phase_number = phase_number
            client_lot.lawn_number = lawn_number
            client_lot.lot_number = lot_number
            client_lot.lot_type = add_client_form.lot_types.data
            client_lot.status = add_client_form.lot_status.data
            client_lot.client = client
            db.session.add(client_lot)
            db.session.commit()

            make_lot_unavail(phase_number, lawn_number, lot_number, client_lot.lot_id, client_lot.status)

            purchase_type = add_client_form.purchase_type.data
            purchase_detail.purchase_type = purchase_type

            selected_promo = {}

            if purchase_type == CONSTANTS.PURCHASE_TYPES.SPOT_CASH:
                promo = LotPromo.query.filter_by(lot_promo_id=add_client_form.spot_cash_promo.data).first()
                
                selected_promo = {
                    "TYPE": promo.type,
                    "LABEL": promo.label,
                    "IS_SPOT_CASH": promo.is_spot_cash,
                    "LIST_PRICE": promo.list_price,
                    "DISC_PER": promo.disc_per,
                    "DISC_VALUE": promo.disc_value,
                    "PERP_CARE_FUND_PER": promo.perp_care_fund_per,
                    "PERP_CARE_VALUE": promo.perp_care_value,
                    "VAT_PER": promo.vat_per,
                    "VAT_VAL": promo.vat_val,
                    "TOTAL": promo.total
                }

                purchase_detail.selected_promo = str(selected_promo)
                purchase_detail.lot = client_lot
                db.session.add(purchase_detail)
                db.session.commit()
            
            elif purchase_type == CONSTANTS.PURCHASE_TYPES.MONTHLY_AMORTIZATION:
                promo = LotPromo.query.filter_by(lot_promo_id=add_client_form.monthly_amortization_promo.data).first()

                selected_promo = {
                    "TYPE": promo.type,
                    "LABEL": promo.label,
                    "IS_SPOT_CASH": promo.is_spot_cash,
                    "NUM_OF_MOS_TO_PAY": promo.num_of_mos_to_pay,
                    "LIST_PRICE": promo.list_price,
                    "PERP_CARE_FUND_PER": promo.perp_care_fund_per,
                    "PERP_CARE_VALUE": promo.perp_care_value,
                    "VAT_PER": promo.vat_per,
                    "VAT_VAL": promo.vat_val,
                    "MONTHLY_PAY": promo.monthly_pay,
                    "TOTAL": promo.total
                }

                schedule_type = add_client_form.schedule_types.data
                monthly_amortization.status = CONSTANTS.MONTHLY_AMORTIZATION.PAYING
                monthly_amortization.total_payment = selected_promo['TOTAL']
                monthly_amortization.balance = selected_promo['TOTAL']
                monthly_amortization.num_of_mos_to_pay = selected_promo['NUM_OF_MOS_TO_PAY']
                monthly_amortization.monthly_payment = selected_promo['MONTHLY_PAY']
                date_start = add_client_form.date_start.data
                
                date = str(date_start).split('-')
                year = int(date[0])
                month = int(date[1])
                day = int(date[2])

                s = generate_payment_schedule(date_start=datetime(year=year, month=month, day=day),
                schedule_type=schedule_type,
                num_months=selected_promo['NUM_OF_MOS_TO_PAY'])
                
                monthly_amortization.payment_schedule = json.dumps(s)
                monthly_amortization.schedule_type = schedule_type
                monthly_amortization.lot_purchase_detail = purchase_detail
            
                purchase_detail.selected_promo = json.dumps(selected_promo)
                purchase_detail.lot = client_lot
                db.session.add_all([purchase_detail, monthly_amortization])
                db.session.commit()

            flash(f'{client.first_name} {client.last_name} is successfully registered.', category='success')
            
            return redirect(url_for('view_client', client_id = client.client_id))

    if add_client_form.errors != {}:
        for err_msg in add_client_form.errors.values():

            flash(f'{err_msg}', category='warning')

    return render_template('admin/forms/add_client_form.html', add_client_form=add_client_form)

@app.route('/admin/edit_website_content/interest_promo', methods=['POST', 'GET'])
@login_required
def edit_interest_promo():
    PROMOS = LotPromo.query.order_by(LotPromo.lot_promo_id)
    lot_promo_form = LotPromoForm()

    if request.method == 'POST':
        if lot_promo_form.validate_on_submit:

            edit_promo = request.form.get('edit_promo')
            print(str(edit_promo)+">>>>>>>")
            promo = LotPromo.query.filter_by(lot_promo_id=edit_promo).first()

            if promo:
                promo.label = lot_promo_form.label.data
                promo.num_of_mos_to_pay = lot_promo_form.num_of_mos_to_pay.data
                promo.list_price = lot_promo_form.list_price.data
                promo.disc_price = lot_promo_form.disc_per.data
                promo.disc_value = lot_promo_form.disc_value.data
                promo.perp_care_fund_per = lot_promo_form.perp_care_fund_per.data
                promo.perp_care_value = lot_promo_form.perp_care_value.data
                promo.vat_per = lot_promo_form.vat_per.data
                promo.vat_val = lot_promo_form.vat_val.data
                promo.total = lot_promo_form.total.data
                promo.monthly_pay = lot_promo_form.monthly_pay.data
                
                db.session.commit()

                return redirect(url_for('edit_interest_promo'))

    return render_template('admin/website_content/edit_interest_promo.html', PROMOS=PROMOS, 
    lot_promo_form=lot_promo_form)


@app.route('/admin/edit_website_content/edit_news', methods=['POST', 'GET'])
@login_required
def edit_news():
    current_md_code =  NewsContent.query.filter_by(id=1).first()
    news_content_form = NewsContentForm()


    if request.method == 'POST':
        if news_content_form.validate_on_submit:
            current_md_code.md_code = news_content_form.md_code.data
            db.session.commit()
            return redirect('edit_news')
    
    news_content_form.md_code.data = current_md_code.md_code
    html_code = markdown(current_md_code.md_code)
    news = modify_html_code(html_code)

    return render_template('admin/website_content/edit_news.html', news=news, news_content_form=news_content_form)

@app.route('/admin/view_client/<client_id>')
@login_required
def view_client(client_id):

    client_info = Client.query.filter_by(client_id=client_id).first()
    return render_template('admin/view_client.html', client_info = client_info)

@app.route('/admin/view_client/monthly_amortization/<monthly_amor_id>', methods=['POST', 'GET'])
@login_required
def monthly_amor(monthly_amor_id):

    m_amortization = MonthlyAmortization.query.filter_by(monthly_amortization_id=monthly_amor_id).first()
    payment_sche = m_amortization.payment_schedule
    payment_sche = json.loads(payment_sche)
    payment_sche = payment_sche['SCHEDULE']

    payment_history = m_amortization.payment_history

    m_amor_pay_form = PayMonthlyAmortizationForm()

    if request.method == 'POST':
        if m_amor_pay_form.validate_on_submit():
            payment_history = PaymentHistory()

            month_num = request.form.get('month_num')

            payment_history.payment_method = m_amor_pay_form.payment_methods.data
            payment_history.paid_for_month_of = payment_sche[int(month_num)-1]['DATE_TO_PAY'] 
            payment_history.amount_paid = m_amor_pay_form.amount_paid.data
            payment_history.change =  m_amor_pay_form.amount_paid.data - m_amortization.monthly_payment
            
            balance =  m_amortization.balance - m_amortization.monthly_payment
            
            payment_history.remaining_amount_to_pay = balance
            payment_history.monthly_amortization = m_amortization


            # modifying specific monthly amortization
            m_amortization.balance = balance
            
            if balance == 0.0:
                m_amortization.status = CONSTANTS.MONTHLY_AMORTIZATION.FULLY_PAID

            payment_sche[int(month_num)-1]['STATUS'] = CONSTANTS.MONTHLY_AMORTIZATION.PAID
            m_amortization.payment_schedule = json.dumps({'SCHEDULE': payment_sche})

            db.session.add(payment_history)
            db.session.commit()

            return redirect(url_for('monthly_amor', monthly_amor_id=monthly_amor_id))    
    return render_template('admin/view_monthly_amortization.html', m_amortization=m_amortization, payment_his=payment_history, payment_sche=payment_sche, pay_form=m_amor_pay_form)


@app.route('/admin/client/add_lot/<client_id>', methods=['GET', 'POST'])
@login_required
def add_client_lot(client_id):
    add_client_lot_form = AddClientLotForm()
    client = Client.query.filter_by(client_id=client_id).first()

    if request.method == 'POST':
        if add_client_lot_form.validate_on_submit():
            client_lot = Lot()
            purchase_detail = LotPurchaseDetail()
            monthly_amortization = MonthlyAmortization()

            phase_number = add_client_lot_form.phase_number.data
            lawn_number = add_client_lot_form.lawn_number.data
            lot_number = add_client_lot_form.lot_number.data

            client_lot.phase_number = phase_number
            client_lot.lawn_number = lawn_number
            client_lot.lot_number = lot_number
            client_lot.lot_type = add_client_lot_form.lot_types.data
            client_lot.status = add_client_lot_form.lot_status.data
            client_lot.client = client
            db.session.add(client_lot)
            db.session.commit()

            make_lot_unavail(phase_number, lawn_number, lot_number, client_lot.lot_id, client_lot.status)

            purchase_type = add_client_lot_form.purchase_type.data
            purchase_detail.purchase_type = purchase_type

            selected_promo = {}

            if purchase_type == CONSTANTS.PURCHASE_TYPES.SPOT_CASH:
                promo = LotPromo.query.filter_by(lot_promo_id=add_client_lot_form.spot_cash_promo.data).first()
                
                selected_promo = {
                    "TYPE": promo.type,
                    "LABEL": promo.label,
                    "IS_SPOT_CASH": promo.is_spot_cash,
                    "LIST_PRICE": promo.list_price,
                    "DISC_PER": promo.disc_per,
                    "DISC_VALUE": promo.disc_value,
                    "PERP_CARE_FUND_PER": promo.perp_care_fund_per,
                    "PERP_CARE_VALUE": promo.perp_care_value,
                    "VAT_PER": promo.vat_per,
                    "VAT_VAL": promo.vat_val,
                    "TOTAL": promo.total
                }

                purchase_detail.selected_promo = str(selected_promo)
                purchase_detail.lot = client_lot
                db.session.add(purchase_detail)
                db.session.commit()
            
            elif purchase_type == CONSTANTS.PURCHASE_TYPES.MONTHLY_AMORTIZATION:
                promo = LotPromo.query.filter_by(lot_promo_id=add_client_lot_form.monthly_amortization_promo.data).first()

                selected_promo = {
                    "TYPE": promo.type,
                    "LABEL": promo.label,
                    "IS_SPOT_CASH": promo.is_spot_cash,
                    "NUM_OF_MOS_TO_PAY": promo.num_of_mos_to_pay,
                    "LIST_PRICE": promo.list_price,
                    "PERP_CARE_FUND_PER": promo.perp_care_fund_per,
                    "PERP_CARE_VALUE": promo.perp_care_value,
                    "VAT_PER": promo.vat_per,
                    "VAT_VAL": promo.vat_val,
                    "MONTHLY_PAY": promo.monthly_pay,
                    "TOTAL": promo.total
                }


                schedule_type = add_client_lot_form.schedule_types.data
                monthly_amortization.status = CONSTANTS.MONTHLY_AMORTIZATION.PAYING
                monthly_amortization.total_payment = selected_promo['TOTAL']
                monthly_amortization.balance = selected_promo['TOTAL']
                monthly_amortization.num_of_mos_to_pay = selected_promo['NUM_OF_MOS_TO_PAY']
                monthly_amortization.monthly_payment = selected_promo['MONTHLY_PAY']
                date_start = add_client_lot_form.date_start.data
                
                date = str(date_start).split('-')
                year = int(date[0])
                month = int(date[1])
                day = int(date[2])

                s = generate_payment_schedule(date_start=datetime(year=year, month=month, day=day),
                schedule_type=schedule_type,
                num_months=selected_promo['NUM_OF_MOS_TO_PAY'])
                
                monthly_amortization.payment_schedule = json.dumps(s)
                monthly_amortization.schedule_type = schedule_type
                monthly_amortization.lot_purchase_detail = purchase_detail
            
                purchase_detail.selected_promo = json.dumps(selected_promo)
                purchase_detail.lot = client_lot
                db.session.add_all([purchase_detail, monthly_amortization])
                db.session.commit()

            #flash(f'{client.first_name} {client.last_name} is successfully registered.', category='success')
            
            return redirect(url_for('view_client', client_id = client.client_id))

    if add_client_lot_form.errors != {}:
        for err_msg in add_client_lot_form.errors.values():

            flash(f'{err_msg}', category='warning')

    return render_template('admin/forms/add_client_lot_form.html', add_lot_form=add_client_lot_form)



# to-do: will do later
@app.route('/admin/view_client/monthly_amortization/download_receipt')
@login_required
def download_receipt():
    con_receipt_to_image(url_for('templates', filename='home.html'), 'hello.jpg')
    pass
