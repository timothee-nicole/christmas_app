from app import app
from flask import render_template, flash, redirect, request, url_for
from app.forms import LoginForm
from app.models import User, Gift
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse
from app.forms import RegistrationForm, NewGiftForm
from app import db, htpasswd


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect('index')
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect('login')
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = 'index'
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect('index')


@app.route('/register', methods=['GET', 'POST'])
@htpasswd.required
def register(user=None):
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route('/new_gift', methods=['GET', 'POST'])
@login_required
def new_gift():
    form = NewGiftForm()
    gifts = Gift.query.filter_by(user_id=current_user.id).all()
    if form.validate_on_submit():
        gift = Gift(name=form.name.data,
                    description=form.description.data,
                    user_id=current_user.id)
        db.session.add(gift)
        db.session.commit()
    return render_template('new_gift.html', title='New gift', form=form, gifts=gifts)


@app.route('/list_gifts', methods=['GET', 'POST'])
@login_required
def list_gifts():
    gifts = Gift.query.filter_by(user_id=current_user.id).all()
    if request.method == 'POST':
        id = int(list(request.form.keys())[0])
        gift = Gift.query.filter_by(id=id).one_or_none()
        if gift is None:
            return redirect('/list_gifts')
        db.session.delete(gift)
        db.session.commit()
        return redirect('/list_gifts')
    return render_template('list_gifts.html', title='Home', gifts=gifts)


@app.route('/offer_gift', methods=['GET', 'POST'])
@login_required
def offer_gift():
    users = [user for user in User.query.distinct(User.username) if user.id != current_user.id]
    if request.method == 'POST':
        if 'user' in request.form:
            id = request.form['user']
            gifts = [gift for gift in Gift.query.filter_by(user_id=id).all() if gift.who_offers_it is None]
            return render_template('offer_gift.html', title='Home', users=users, gifts=gifts)
        else:
            gift_id = [int(gift.replace('gift_', ''))
                       for gift in request.form.keys() if 'gift' in gift][0]
            Gift.query.filter_by(id=gift_id).update({'who_offers_it': current_user.id})
            db.session.commit()
            return redirect('/gifts_you_offer')
    return render_template('offer_gift.html', title='Home', users=users)


@app.route('/gifts_you_offer', methods=['GET', 'POST'])
@login_required
def gift_you_offer():
    gifts = Gift.query.filter_by(who_offers_it=current_user.id).all()
    if request.method == 'POST':
        gift_id = [int(gift.replace('gift_', ''))
                   for gift in request.form.keys()][0]
        gift_to_change = Gift.query.filter_by(id=gift_id).first()
        gift_to_change.who_offers_it = None
        db.session.commit()
        return redirect('gifts_you_offer')
    return render_template('gift_you_offer.html', title='Gifts you offer', gifts=gifts)
